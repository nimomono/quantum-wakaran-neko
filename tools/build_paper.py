#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import os
import re
import shutil
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SECTIONS = ROOT / "sections"
WORK = ROOT / "build" / "latex"
TEMPLATE = ROOT / "tools" / "template.tex"
PAPER_MD = ROOT / "paper.md"
MAIN_TEX = ROOT / "main.tex"
PDF = ROOT / "paper.pdf"

THEOREM_LABELS = {
    "theorem": "定理",
    "proposition": "命題",
    "lemma": "補題",
    "corollary": "系",
    "proof": "証明",
}

CHAPTER_NUMBERS = tuple(range(1, 10))

PART_TITLES: dict[int, str] = {
    1: "問題設定と共通言語",
    3: "単一量子ビット型操作と測定",
    4: "2論理部分系とBell型統計",
    6: "空間複素振幅場と粒子位置",
    8: "総合評価",
}

PART_NUMERALS = {1: "I", 3: "II", 4: "III", 6: "IV", 8: "V"}

REFERENCE_KEYS = {
    1: "bell1964",
    2: "chsh1969",
    3: "nelson1966",
    4: "guerra_morato1983",
    5: "yasue1981",
    6: "zambrini1986",
    7: "wharton2010",
    8: "wharton_argaman2020",
    9: "hall2010",
    10: "leifer_pusey2017",
    11: "wood_spekkens2015",
    12: "ford1965",
    13: "mori1965",
    14: "zwanzig1973",
    15: "jamison1974",
    16: "doob1957",
    17: "landauer1961",
    18: "bennett1982",
    19: "wallstrom1994",
    20: "price_wharton2023",
    21: "price_wharton2024",
    22: "argaman2010",
    23: "hossenfelder_palmer2020",
    24: "thooft2016",
    25: "leonard2014",
    26: "chen_georgiou_pavon2016",
    27: "rauch_tung_striebel1965",
    28: "fuchs_goldt_seifert2016",
    29: "evans_majumdar_schehr2020",
    30: "knorst_lopes2024",
    31: "wilson_et_al2021",
    32: "leonard_roelly_zambrini2014",
    33: "marchiori_deaguiar2011",
    34: "heslot1985",
    35: "briggs_eisfeld2012",
    36: "briggs_eisfeld2013",
    37: "skinner2013",
    38: "reck_et_al1994",
    39: "clements_et_al2016",
    40: "misra_sudarshan1977",
    41: "itano_et_al1990",
    42: "ruseckas_kaulakys2001",
    43: "nielsen2002",
    44: "duerr_et_al2005",
    45: "georgii_tumulka2005",
    46: "jarzynski1997",
    47: "crooks1999",
    48: "seifert2005",
    49: "ehrich_et_al2020",
    50: "esposito2012",
    51: "jarzynski2004",
    52: "shiraishi_matsumoto2021",
}


APPENDIX_FILENAME = re.compile(r"A(\d+)_.*\.md")


def parse_source(path: Path) -> tuple[dict[str, str], list[str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    meta: dict[str, str] = {}
    while lines and lines[0].startswith("@"):
        key, value = lines.pop(0)[1:].split(":", 1)
        meta[key.strip()] = value.strip()
    return meta, lines


def ordered_appendix_paths() -> list[Path]:
    numbered: list[tuple[int, Path]] = []
    for path in SECTIONS.glob("A*_*.md"):
        match = APPENDIX_FILENAME.fullmatch(path.name)
        if match:
            numbered.append((int(match.group(1)), path))

    numbers = [number for number, _ in numbered]
    if len(numbers) != len(set(numbers)):
        raise ValueError("duplicate appendix number")

    ordered = sorted(numbered)
    for number, path in ordered:
        meta, _ = parse_source(path)
        if not 1 <= number <= 26:
            raise ValueError(f"unsupported appendix number: {path.name}")
        expected = chr(ord("A") + number - 1)
        if meta.get("number") != expected or meta.get("chapter") != "付録":
            raise ValueError(
                f"{path.name}: appendix metadata must be "
                f"@number: {expected} and @chapter: 付録"
            )
    return [path for _, path in ordered]


def citation_keys(spec: str) -> list[str]:
    numbers: list[int] = []
    for item in spec.split(","):
        if "--" in item:
            start, end = (int(value) for value in item.split("--", 1))
            numbers.extend(range(start, end + 1))
        else:
            numbers.append(int(item))
    return [REFERENCE_KEYS[number] for number in numbers]


def replace_citations(text: str) -> str:
    pattern = re.compile(r"\[((?:\d+)(?:(?:--|,)\d+)*)\]")

    def replacement(match: re.Match[str]) -> str:
        try:
            keys = citation_keys(match.group(1))
        except (KeyError, ValueError):
            return match.group(0)
        return r"\cite{" + ",".join(keys) + "}"

    return pattern.sub(replacement, text)



def restore_markdown_source(lines: list[str]) -> list[str]:
    output: list[str] = []
    index = 0
    while index < len(lines):
        line = lines[index]
        start = re.fullmatch(
            r"<!-- theorem-start:(theorem|proposition|lemma|corollary|proof) -->",
            line.strip(),
        )
        if start:
            environment = start.group(1)
            if index + 1 >= len(lines):
                raise ValueError(f"missing theorem label after {line}")
            visible = lines[index + 1].strip()
            label = THEOREM_LABELS[environment]
            plain = f"**{label}**"
            titled_prefix = f"**{label}（"
            if visible == plain:
                title = ""
            elif visible.startswith(titled_prefix) and visible.endswith("）**"):
                title = visible[len(titled_prefix):-3]
            else:
                raise ValueError(f"invalid theorem label: {visible}")
            begin = rf"\begin{{{environment}}}"
            if title:
                begin += f"[{title}]"
            output.append(begin)
            index += 2
            continue

        end = re.fullmatch(
            r"<!-- theorem-end:(theorem|proposition|lemma|corollary|proof) -->",
            line.strip(),
        )
        if end:
            output.append(rf"\end{{{end.group(1)}}}")
            index += 1
            continue

        output.append(line)
        index += 1
    return output


def validate_github_markdown(path: Path, text: str) -> None:
    if re.search(rb"[\x00-\x08\x0b\x0c\x0d\x0e-\x1f]", path.read_bytes()):
        raise ValueError(f"{path}: 規約外の制御文字を検出")
    forbidden = {
        "独自数式マクロ": r"\\(?:dd|E|R|Tr|GM|Nel)(?![A-Za-z])",
        "生の定理環境": (
            r"\\(?:begin|end)\{"
            r"(?:theorem|proposition|lemma|corollary|proof|statusbox|thebibliography)"
            r"\}"
        ),
        "数式外のTeX命令": (
            r"\\(?:chapter\*?|part|appendix|addcontentsline|cite|bibitem|url)\b"
        ),
        "規約外の数式区切り": r"\\\(|\\\[|\$\$",
        "数式命令内の日本語": (
            r"\\(?:text|mathrm|boxed)\{[^{}]*[ぁ-んァ-ヶ一-龠々〆ヵヶ][^{}]*\}"
        ),
    }
    errors = [
        name for name, pattern in forbidden.items()
        if re.search(pattern, text)
    ]
    for environment in THEOREM_LABELS:
        starts = text.count(f"<!-- theorem-start:{environment} -->")
        ends = text.count(f"<!-- theorem-end:{environment} -->")
        if starts != ends:
            errors.append(f"{environment} 境界の不一致")
    if errors:
        raise ValueError(f"{path}: " + "、".join(errors))


def validate_fixed_goal_language() -> None:
    status_text = (ROOT / "PROJECT_STATUS.md").read_text(encoding="utf-8")
    readme_text = (ROOT / "README.md").read_text(encoding="utf-8")

    fixed_block = status_text.split("### 固定目標一覧", 1)[1].split("### 現在地", 1)[0]
    readme_block = readme_text.split("## 長期目標の現在地", 1)[1].split(
        "詳しい達成判定", 1
    )[0]
    forbidden = {
        "モデルID": r"(?<![A-Za-z])M\d+",
        "結果ID": r"(?<![A-Za-z])R\d+",
        "複素振幅場": r"複素振幅場",
    }
    for label, block in (
        ("PROJECT_STATUS.mdの固定目標", fixed_block),
        ("README.mdの長期目標", readme_block),
    ):
        hits = [name for name, pattern in forbidden.items() if re.search(pattern, block)]
        if hits:
            raise ValueError(f"{label}: モデル固有語を検出: " + "、".join(hits))

    current_block = status_text.split("### 現在地", 1)[1].split(
        "### 直前版IDとの対応", 1
    )[0]
    expected_status = {
        "Q1-1": "達成",
        "Q1-2": "部分達成",
        "Q2-1": "達成",
        "Q2-2": "条件付き達成",
        "Q2-3": "条件付き達成",
        "Q2-4": "未達",
        "Q2-5": "未達",
        "Q3-1": "達成",
        "Q3-2": "未達",
        "Q3-3": "達成",
        "Q3-4": "条件付き達成",
        "Q3-5": "条件付き達成",
    }
    for goal_id, status in expected_status.items():
        pattern = rf"^\| {re.escape(goal_id)} \| {re.escape(status)} \|"
        if not re.search(pattern, current_block, flags=re.MULTILINE):
            raise ValueError(f"{goal_id}: 現在地が{status}ではない")

    retired_q1_rows = re.compile(r"^\| Q1-(?:3|4) \|", flags=re.MULTILINE)
    for label, block in (
        ("PROJECT_STATUS.mdの固定目標", fixed_block),
        ("PROJECT_STATUS.mdの現在地", current_block),
        ("README.mdの長期目標", readme_block),
    ):
        if retired_q1_rows.search(block):
            raise ValueError(f"{label}: 旧Q1-3または旧Q1-4の現行行が残っている")

    required_q1_fragments = (
        "Q1-2 | 射影測定統計とZeno効果",
        "2値Born分布",
        "同軸再測定の反復分布",
        "異なる軸による逐次測定分布",
        "Zeno型遷移抑制",
        "tiltだけによる抑制",
    )
    missing_q1_fragments = [
        fragment for fragment in required_q1_fragments if fragment not in fixed_block
    ]
    if missing_q1_fragments:
        raise ValueError(
            "Q1-2の統合達成判定が不足: " + "、".join(missing_q1_fragments)
        )
    if "Q1-2 | 射影測定統計とZeno効果" not in readme_block:
        raise ValueError("README.mdのQ1-2名称が固定目標と一致しない")

    required_goal_fragments = (
        "Q2-3 | 有限回路の機能的再現",
        "中間の非分離状態",
        "最終出力分布を事前計算",
        "Q2-4 | 多項式資源による量子出力サンプリング",
        "一出力標本",
        "全変動距離",
        "指数表",
        "事後選別",
        "Q2-5 | 自律非平衡計算と平衡化運命の決定不能性",
        "停止時刻",
        "長時間極限",
        "熱力学極限",
        "非計算可能な実数",
    )
    missing_goal_fragments = [
        fragment for fragment in required_goal_fragments if fragment not in fixed_block
    ]
    if missing_goal_fragments:
        raise ValueError(
            "Q2-3--Q2-5の達成判定が不足: " + "、".join(missing_goal_fragments)
        )

    required_readme_goals = (
        "Q2-3 | 有限回路の機能的再現",
        "Q2-4 | 多項式資源による量子出力サンプリング",
        "Q2-5 | 自律非平衡計算と平衡化運命の決定不能性",
    )
    missing_readme_goals = [
        fragment for fragment in required_readme_goals if fragment not in readme_block
    ]
    if missing_readme_goals:
        raise ValueError(
            "README.mdのQ2固定目標が不足: " + "、".join(missing_readme_goals)
        )

    body_text = "\n".join(
        path.read_text(encoding="utf-8")
        for path in (
            SECTIONS / "01_scope_and_cycle.md",
            SECTIONS / "02_common_canonical_modules.md",
            SECTIONS / "08_errors_resources_open_targets.md",
            SECTIONS / "09_conclusion.md",
        )
    )
    required_body_fragments = (
        "Q2-3有限回路の機能的再現",
        "Q2-3を条件付き達成",
        "L=2^n",
        "回路末尾",
        "Q2-4多項式資源による量子出力サンプリング",
        "Q2-5自律非平衡計算と平衡化運命の決定不能性",
        "白石と松本",
        "有限時間で非停止を判定",
    )
    missing_body_fragments = [
        fragment for fragment in required_body_fragments if fragment not in body_text
    ]
    if missing_body_fragments:
        raise ValueError(
            "Q2-3--Q2-5の本文同期が不足: " + "、".join(missing_body_fragments)
        )

    current_goal_paths = [
        ROOT / "README.md",
        ROOT / "PROJECT_STATUS.md",
        *sorted(SECTIONS.glob("*.md")),
    ]
    stale_freeze_pattern = re.compile(
        r"未達（凍結中）|未達・凍結|未達のまま凍結|凍結状態|凍結を維持"
    )
    stale_freeze_hits = [
        path.relative_to(ROOT).as_posix()
        for path in current_goal_paths
        if stale_freeze_pattern.search(path.read_text(encoding="utf-8"))
    ]
    if stale_freeze_hits:
        raise ValueError(
            "現行文書に凍結中の表記が残っている: " + "、".join(stale_freeze_hits)
        )

    integration_note = ROOT / "notes" / "q1_2_zeno_integration.md"
    obsolete_zeno_notes = (
        ROOT / "notes" / "q1_zeno_revival.md",
        ROOT / "notes" / "frozen_q1_zeno.md",
    )
    if not integration_note.is_file() or any(path.exists() for path in obsolete_zeno_notes):
        raise ValueError("Q1-2 Zeno統合メモの改名が未完了")

    required_paths = (
        SECTIONS / "03_m47_controlled_w_instrument.md",
        SECTIONS / "A2_m47_controlled_w_instrument_proofs.md",
        SECTIONS / "04_l4_two_qubit_gate.md",
        SECTIONS / "A3_l4_two_qubit_gate_proofs.md",
        SECTIONS / "05_m48_bell_cycle_and_audit.md",
        SECTIONS / "A4_m48_cycle_proofs.md",
        SECTIONS / "A6_common_signal_statistics.md",
        SECTIONS / "A8_m47_hopf_preparation.md",
        SECTIONS / "A9_m48_paired_hopf_bell_preparation.md",
        SECTIONS / "A10_q2_joint_bath_contract.md",
        SECTIONS / "A11_common_collision_bath_thermodynamics.md",
        SECTIONS / "A12_common_action_shell_state_count.md",
        SECTIONS / "A13_common_open_preparation.md",
        SECTIONS / "A14_m37_m42_spatial_token.md",
    )
    obsolete_paths = (
        SECTIONS / "03_l2_operation_measurement_zeno.md",
        SECTIONS / "A2_l2_cycle_and_zeno_proofs.md",
        SECTIONS / "05_m41_bell_cycle_and_audit.md",
        SECTIONS / "A4_m41_cycle_proofs.md",
        SECTIONS / "A6_realized_configuration_proofs.md",
        SECTIONS / "A6_particle_position_proofs.md",
        SECTIONS / "A6_m37_m50_position_instrument_proofs.md",
        SECTIONS / "A8_w_two_mode_hopf_statistics.md",
        SECTIONS / "A13_q2_action_shell_statistics.md",
    )
    for path in required_paths:
        if not path.is_file():
            raise ValueError(f"現行モデルファイルがない: {path.name}")
    for path in obsolete_paths:
        if path.exists():
            raise ValueError(f"置換済みモデルファイルが残っている: {path.name}")

    terminology_paths = [
        ROOT / "README.md",
        ROOT / "PROJECT_STATUS.md",
        ROOT / "CHANGELOG.md",
        *sorted(SECTIONS.glob("*.md")),
    ]
    inconsistent = [
        path.relative_to(ROOT).as_posix()
        for path in terminology_paths
        if re.search(r"二mode|二モード", path.read_text(encoding="utf-8"))
    ]
    if inconsistent:
        raise ValueError("2モード表記の不一致: " + "、".join(inconsistent))

    current_terminology_paths = [
        ROOT / "README.md",
        ROOT / "PROJECT_STATUS.md",
        ROOT / "MANIFEST.md",
        *sorted(SECTIONS.glob("*.md")),
    ]
    deprecated = [
        path.relative_to(ROOT).as_posix()
        for path in current_terminology_paths
        if "実現配置" in path.read_text(encoding="utf-8")
    ]
    if deprecated:
        raise ValueError("現行文書に旧称『実現配置』が残っている: " + "、".join(deprecated))

    current_sections = sorted(SECTIONS.glob("*.md"))
    retired_m42_results = [
        path.relative_to(ROOT).as_posix()
        for path in current_sections
        if re.search(r"R11[3-8](?!\d)", path.read_text(encoding="utf-8"))
    ]
    if retired_m42_results:
        raise ValueError("現行章に退役済みR113--R118が残っている: " + "、".join(retired_m42_results))

    absorbed_result_pattern = re.compile(
        r"R(?:83|84|85|87|88|89|90|97|98|99|104|105|106|136|139|141|142|146|148|149|151|154|156|157|158|163|166|167)(?!\d)"
    )
    absorbed_model_pattern = re.compile(r"M" r"35(?!\d)")
    absorbed_result_paths = [
        ROOT / "README.md",
        ROOT / "PROJECT_STATUS.md",
        *sorted(SECTIONS.glob("*.md")),
    ]
    absorbed_hits = [
        path.relative_to(ROOT).as_posix()
        for path in absorbed_result_paths
        if (
            absorbed_result_pattern.search(path.read_text(encoding="utf-8"))
            or absorbed_model_pattern.search(path.read_text(encoding="utf-8"))
        )
    ]
    if absorbed_hits:
        raise ValueError(
            "現行文書に吸収済み結果IDまたはモデルIDが残っている: " + "、".join(absorbed_hits)
        )

    all_section_text = "\n".join(
        path.read_text(encoding="utf-8") for path in sorted(SECTIONS.glob("*.md"))
    )
    for result_id in (
        "R171", "R172", "R173", "R174", "R161", "R162", "R164", "R123", "R124", "R125"
    ):
        if all_section_text.count(f"定理（{result_id}：") != 1:
            raise ValueError(f"{result_id}の定理宣言は現行章全体で1回でなければならない")

    common_text = (SECTIONS / "02_common_canonical_modules.md").read_text(
        encoding="utf-8"
    )
    for token in (
        "M51有限実正準担体の共通開放ray準備",
        "R171：M51共通開放ray準備の有限時間率と切断後輸送",
        r"\lambda_{\rm prep}",
        r"C_{Z,G_*}",
        "成功試行だけを結果分布として再規格化しない",
    ):
        if token not in common_text:
            raise ValueError(f"M51/R171共通準備の固定要素がない: {token}")

    q3_text = (SECTIONS / "06_m37_spatial_envelope.md").read_text(encoding="utf-8")
    for token in (
        "R86：M37有限時間包絡線縮約",
        "共通R135のM37有限時間特殊化",
        "R172：M37有効辺流に沿うM42局在トークンの等変輸送",
        "R173：M42の節一様正則化と有限衝突Hamiltonian近似",
        "R174：M51--M37--M42の有限時間準備・輸送・記録受渡し",
        "別のM50位置を生成せず",
        "R162の平衡率公式をそのまま用いる主張ではない",
        r"\varepsilon_{174}",
    ):
        if token not in q3_text:
            raise ValueError(f"Q3受渡し本文の固定要素がない: {token}")

    m42_text = (SECTIONS / "A14_m37_m42_spatial_token.md").read_text(
        encoding="utf-8"
    )
    for token in (
        "方向別controllerと仕事registerを持つ駆動衝突模型",
        "物理的な一様閾値座標",
        r"\nu_{e,m}",
        "成功試行だけを再規格化しない",
    ):
        if token not in m42_text:
            raise ValueError(f"M42方向別衝突模型の固定要素がない: {token}")

    m49_text = (SECTIONS / "04_l4_two_qubit_gate.md").read_text(encoding="utf-8")
    for token in (
        "R159内部補題：入力の行分解bath--粒子位置matching",
        "R159内部補題：担体・bath・粒子位置へ同期するCNOT",
        "R159：固定有限入力、入力頻度、固定積出力基底の共同入力--出力統計",
        "R160：M49固定singlet providerからM48へのsetting-free同一register受渡し",
        r"\rho_*",
        r"\varepsilon_{\rm Q2-link}",
        r"D_{\rm prog}",
        r"d_{\rm prog}",
    ):
        if token not in m49_text:
            raise ValueError(f"M49本文の固定要素がない: {token}")


def preprocess(lines: list[str]) -> list[str]:
    lines = restore_markdown_source(lines)
    output: list[str] = []
    in_math = False
    for line in lines:
        stripped = line.strip()
        if not in_math and stripped in {"$$", "```math"}:
            in_math = True
            output.append(line)
            continue
        if in_math and stripped in {"$$", "```"}:
            in_math = False
            output.append(line)
            continue
        if in_math:
            output.append(line)
            continue
        heading = re.match(r"^(#{2,3})\s+(?:\d+|[A-Z])(?:\.\d+)*\s+(.*)$", line)
        if heading:
            line = f"{heading.group(1)} {heading.group(2)}"
        output.append(replace_citations(line))
    return output


def preprocess_public(lines: list[str]) -> list[str]:
    output: list[str] = []
    in_math = False
    for line in lines:
        stripped = line.strip()
        if not in_math and stripped == "```math":
            in_math = True
            output.append(line)
            continue
        if in_math and stripped == "```":
            in_math = False
            output.append(line)
            continue
        if not in_math:
            heading = re.match(r"^(#{2,3})\s+(?:\d+|[A-Z])(?:\.\d+)*\s+(.*)$", line)
            if heading:
                line = f"{heading.group(1)} {heading.group(2)}"
        output.append(line)
    if in_math:
        raise ValueError("unclosed math fence")
    return output


def markdown_for_pandoc(text: str) -> str:
    output: list[str] = []
    in_math = False
    for line in text.splitlines():
        stripped = line.strip()
        if not in_math and stripped == "```math":
            in_math = True
            output.append("$$")
            continue
        if in_math and stripped == "```":
            in_math = False
            output.append("$$")
            continue
        if not in_math and re.match(r"^#{1,6}\s+", line):
            for github_math, tex_math in (
                ("−1/<i>T</i>", "$-1/T$"),
                ("<i>C</i><sup>1</sup>", "$C^1$"),
                ("<i>E</i><sub>∗</sub>", "$E_*$"),
            ):
                line = line.replace(github_math, tex_math)
        output.append(line)
    if in_math:
        raise ValueError("unclosed math fence")
    pandoc_text = "\n".join(output) + "\n"
    return re.sub(
        r"(?m)^\$\$\n\n(\\end\{(?:theorem|proof)\})$",
        lambda match: "$$\n" + match.group(1),
        pandoc_text,
    )


def bibliography_tex() -> str:
    _, lines = parse_source(SECTIONS / "90_references.md")
    entries: dict[int, str] = {}
    for line in lines:
        match = re.match(r"^- \[(\d+)\]\s+(.*)$", line)
        if match:
            entry = re.sub(
                r"<(https?://[^ >]+)>",
                lambda url: r"\url{" + url.group(1) + "}",
                match.group(2),
            )
            entries[int(match.group(1))] = entry
    body = [
        r"\begingroup",
        r"\small",
        r"\begin{thebibliography}{99}",
        r"\addcontentsline{toc}{chapter}{参考文献}",
    ]
    for number in range(1, max(REFERENCE_KEYS) + 1):
        body.append(rf"\bibitem{{{REFERENCE_KEYS[number]}}} {entries[number]}")
    body.extend([r"\end{thebibliography}", r"\endgroup"])
    return "\n\n".join(body)


def pandoc_markdown() -> str:
    chunks: list[str] = []
    _, overview = parse_source(SECTIONS / "00_overview_and_contents.md")
    chunks.extend([
        r"\chapter*{概要}",
        r"\addcontentsline{toc}{chapter}{概要}",
        "\n".join(preprocess(overview)),
    ])

    for number in CHAPTER_NUMBERS:
        if number in PART_TITLES:
            chunks.append(r"\part{" + PART_TITLES[number] + "}")
        path = next(SECTIONS.glob(f"{number:02d}_*.md"))
        meta, lines = parse_source(path)
        chunks.append("# " + meta["title"])
        status = meta.get("status", "")
        if status:
            chunks.append(
                "\\begin{statusbox}\n"
                + "位置づけ：" + status + "\n"
                + "\\end{statusbox}"
            )
        chunks.append("\n".join(preprocess(lines)))

    appendix_paths = ordered_appendix_paths()
    if appendix_paths:
        chunks.append(r"\appendix")
    for path in appendix_paths:
        meta, lines = parse_source(path)
        chunks.append("# " + meta["title"])
        status = meta.get("status", "")
        if status:
            chunks.append(
                "\\begin{statusbox}\n"
                + "位置づけ：" + status + "\n"
                + "\\end{statusbox}"
            )
        chunks.append("\n".join(preprocess(lines)))

    chunks.append(bibliography_tex())
    return "\n\n".join(chunks) + "\n"


def combined_markdown() -> str:
    chunks: list[str] = []
    _, overview = parse_source(SECTIONS / "00_overview_and_contents.md")
    chunks.extend([
        "# 概要",
        "\n".join(preprocess_public(overview)),
    ])

    for number in CHAPTER_NUMBERS:
        if number in PART_TITLES:
            chunks.append(
                "# 第"
                + PART_NUMERALS[number]
                + "部　"
                + PART_TITLES[number]
            )
        path = next(SECTIONS.glob(f"{number:02d}_*.md"))
        meta, lines = parse_source(path)
        chunks.append("# " + meta["title"])
        status = meta.get("status", "")
        if status:
            chunks.append("> **位置づけ：** " + status)
        chunks.append("\n".join(preprocess_public(lines)))

    appendix_paths = ordered_appendix_paths()
    if appendix_paths:
        chunks.append("# 付録")
    for path in appendix_paths:
        meta, lines = parse_source(path)
        chunks.append("# " + meta["title"])
        status = meta.get("status", "")
        if status:
            chunks.append("> **位置づけ：** " + status)
        chunks.append("\n".join(preprocess_public(lines)))

    _, references = parse_source(SECTIONS / "90_references.md")
    chunks.extend([
        "# 参考文献",
        "\n".join(preprocess_public(references)),
    ])
    return "\n\n".join(chunks) + "\n"


def run_command(command: list[str], cwd: Path | None = None) -> None:
    subprocess.run(command, cwd=cwd, env=tex_environment(), check=True)


def tex_environment() -> dict[str, str]:
    env = os.environ.copy()
    env.update({
        # Keep PDF metadata stable for the current cited draft.  Update this
        # epoch together with CITATION.cff when a new draft is released.
        "SOURCE_DATE_EPOCH": "1788220800",
        "FORCE_SOURCE_DATE": "1",
        "TZ": "UTC",
        "TEXINPUTS": "/usr/share/texlive/texmf-dist/tex//:",
        "TFMFONTS": "/usr/share/texlive/texmf-dist/fonts/tfm//:",
        "OPENTYPEFONTS": "/usr/share/texmf/fonts/opentype//:/usr/share/texlive/texmf-dist/fonts/opentype//:",
    })
    return env


def normalize_pdf_id(path: Path) -> None:
    """Normalize an xdvipdfmx trailer ID when the PDF contains one."""
    data = path.read_bytes()
    pdf_string = rb"(?:<[0-9A-Fa-f]+>|\((?:\\.|[^\\)])*\))"
    pattern = re.compile(rb"/ID\[\s*" + pdf_string + rb"\s*" + pdf_string + rb"\s*\]")
    placeholder = b"/ID[<" + b"0" * 32 + b"><" + b"0" * 32 + b">]"
    normalized, count = pattern.subn(placeholder, data)
    if count == 0:
        # TeX Live 2023 may omit /ID entirely when reproducible-output
        # variables are set.  There is then no random trailer field to fix.
        return
    if count != 1:
        raise RuntimeError(f"expected at most one PDF trailer ID in {path}, found {count}")
    stable_id = hashlib.sha256(normalized).hexdigest()[:32].encode("ascii")
    stable = b"/ID[<" + stable_id + b"><" + stable_id + b">]"
    path.write_bytes(normalized.replace(placeholder, stable, 1))


def build() -> None:
    WORK.mkdir(parents=True, exist_ok=True)
    validate_fixed_goal_language()
    for source in sorted(SECTIONS.glob("*.md")):
        validate_github_markdown(source, source.read_text(encoding="utf-8"))

    paper_text = combined_markdown()
    validate_github_markdown(PAPER_MD, paper_text)
    PAPER_MD.write_text(paper_text, encoding="utf-8")

    pandoc_source = WORK / "paper.md"
    pandoc_source.write_text(
        markdown_for_pandoc(pandoc_markdown()),
        encoding="utf-8",
    )
    body = WORK / "body.tex"
    run_command([
        "pandoc",
        "--from=markdown+raw_tex",
        "--to=latex",
        "--top-level-division=chapter",
        "--wrap=none",
        "--output", str(body),
        str(pandoc_source),
    ])

    template = TEMPLATE.read_text(encoding="utf-8")
    MAIN_TEX.write_text(template.replace("$body$", body.read_text(encoding="utf-8")), encoding="utf-8")

    # Keep the multi-pass TeX state on the local temporary filesystem.  Some
    # synced workspaces expose newly rewritten .aux files before their final
    # bytes are visible to the next XeLaTeX process.
    latex_run = Path(tempfile.mkdtemp(prefix="quantum-wakaran-neko-latex-"))
    try:
        command = [
            "xelatex",
            "-interaction=nonstopmode",
            "-halt-on-error",
            f"-output-directory={latex_run}",
            MAIN_TEX.name,
        ]
        for _ in range(3):
            run_command(command, cwd=ROOT)
        shutil.copy2(latex_run / "main.pdf", WORK / "main.pdf")
        normalize_pdf_id(WORK / "main.pdf")
    finally:
        log = latex_run / "main.log"
        if log.exists():
            shutil.copy2(log, WORK / "main.log")
        shutil.rmtree(latex_run)

    built = WORK / "main.pdf"
    shutil.copy2(built, PDF)
    print(PAPER_MD)
    print(MAIN_TEX)
    print(PDF)


if __name__ == "__main__":
    build()
