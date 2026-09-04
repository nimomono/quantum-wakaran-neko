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


Q2_RESULT_DEPENDENCIES: dict[str, set[str]] = {
    "R181B": {"R112"},
    "R181C": {"R112", "R181B"},
    "R181D": {"R112", "R161", "R162", "R164", "R170", "R181A"},
    "R177": {"R181B", "R181C", "R181D"},
    "R178D": {"R181D"},
    "R179": {"R112", "R161", "R162"},
    "R180A": {"R181C", "R181D"},
    "R180B": {"R181A"},
    "R180C": {"R181B", "R181D", "R180A", "R180B"},
}

Q2_LEDGER_ROOTS: dict[str, set[str]] = {
    "Q2-1": {"R181B", "R181C", "R181D"},
    "Q2-2": {"R180C"},
    "Q2-3": {"R177"},
    "Q2-4": {"R181C", "R181D", "R178D", "R179"},
}

Q2_LEDGER_MODELS: dict[str, set[str]] = {
    "Q2-1": {"M54", "M50"},
    "Q2-2": {"M54", "M50", "receiver"},
    "Q2-3": {"M54", "M50"},
    "Q2-4": {"M54"},
}


def dependency_closure(roots: set[str]) -> set[str]:
    closure = set(roots)
    pending = list(roots)
    while pending:
        result = pending.pop()
        for dependency in Q2_RESULT_DEPENDENCIES.get(result, set()):
            if dependency not in closure:
                closure.add(dependency)
                pending.append(dependency)
    return closure


def result_ids(cell: str) -> set[str]:
    results: set[str] = set()
    occupied: list[tuple[int, int]] = []
    range_pattern = re.compile(r"R(\d+)([A-Z]?)--R(\d+)([A-Z]?)")
    for match in range_pattern.finditer(cell):
        start_number, start_suffix, end_number, end_suffix = match.groups()
        occupied.append(match.span())
        if start_number == end_number and start_suffix and end_suffix:
            for codepoint in range(ord(start_suffix), ord(end_suffix) + 1):
                results.add(f"R{start_number}{chr(codepoint)}")
        elif not start_suffix and not end_suffix:
            for number in range(int(start_number), int(end_number) + 1):
                results.add(f"R{number}")
        else:
            raise ValueError(f"展開できない結果範囲: {match.group(0)}")
    for match in re.finditer(r"R\d+[A-Z]?", cell):
        if not any(start <= match.start() < end for start, end in occupied):
            results.add(match.group(0))
    return results


def table_evidence(
    text: str,
    goal_id: str,
    model_index: int,
    result_index: int,
    required_status: str | None = None,
) -> tuple[str, str]:
    for line in text.splitlines():
        if not line.startswith(f"| {goal_id} |"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if required_status is not None and (
            len(cells) < 2 or cells[1] != required_status
        ):
            continue
        if len(cells) > result_index and "R" in cells[result_index]:
            return cells[model_index], cells[result_index]
    raise ValueError(f"{goal_id}: 根拠台帳行がない")


def validate_q2_dependency_ledgers() -> None:
    ledgers = (
        (
            "PROJECT_STATUS.md",
            (ROOT / "PROJECT_STATUS.md").read_text(encoding="utf-8"),
            2,
            3,
            "条件付き達成",
        ),
        ("README.md", (ROOT / "README.md").read_text(encoding="utf-8"), 1, 2, None),
        (
            "sections/01_scope_and_cycle.md",
            (SECTIONS / "01_scope_and_cycle.md").read_text(encoding="utf-8"),
            2,
            3,
            "条件付き達成",
        ),
    )
    expected_results = {
        goal_id: dependency_closure(roots)
        for goal_id, roots in Q2_LEDGER_ROOTS.items()
    }
    for label, text, model_index, result_index, required_status in ledgers:
        for goal_id in Q2_LEDGER_ROOTS:
            model_cell, result_cell = table_evidence(
                text,
                goal_id,
                model_index,
                result_index,
                required_status,
            )
            missing_models = sorted(
                model
                for model in Q2_LEDGER_MODELS[goal_id]
                if model not in model_cell
            )
            actual_results = result_ids(result_cell)
            missing_results = sorted(expected_results[goal_id] - actual_results)
            unexpected_results = sorted(actual_results - expected_results[goal_id])
            if missing_models or missing_results or unexpected_results:
                details = []
                if missing_models:
                    details.append("不足模型=" + ",".join(missing_models))
                if missing_results:
                    details.append("不足結果=" + ",".join(missing_results))
                if unexpected_results:
                    details.append("依存グラフ外結果=" + ",".join(unexpected_results))
                raise ValueError(f"{label}の{goal_id}依存台帳が不整合: " + "、".join(details))


def validate_fixed_goal_language() -> None:
    """Guard the fixed goals and the current M54/R181 dependency boundary."""
    status_text = (ROOT / "PROJECT_STATUS.md").read_text(encoding="utf-8")
    readme_text = (ROOT / "README.md").read_text(encoding="utf-8")
    fixed_block = status_text.split("### 固定目標一覧", 1)[1].split(
        "### 現在地", 1
    )[0]
    readme_block = readme_text.split("## 長期目標の現在地", 1)[1].split(
        "詳しい達成判定", 1
    )[0]

    for label, block in (
        ("PROJECT_STATUS.mdの固定目標", fixed_block),
        ("README.mdの長期目標", readme_block),
    ):
        if re.search(r"(?<![A-Za-z])[MR]\d+", block):
            raise ValueError(f"{label}: モデルまたは結果IDを検出")

    required_goal_fragments = (
        "Q1-2 | 射影測定統計とZeno効果",
        "同軸再測定の反復分布",
        "異なる軸による逐次測定分布",
        "Q2-3 | 3量子ビット型二段ゲート合成",
        "測定、経路選択、共同モーメントへの置換、再準備",
        "Q2-4 | 多項式外部制御による量子出力サンプリング",
        "一出力標本",
        "全変動距離",
        "指数長の係数表",
        "事後選別",
    )
    missing = [token for token in required_goal_fragments if token not in fixed_block]
    if missing:
        raise ValueError("固定目標の文言が不足: " + "、".join(missing))

    expected_status = {
        "Q1-1": "達成",
        "Q1-2": "部分達成",
        "Q2-1": "条件付き達成",
        "Q2-2": "条件付き達成",
        "Q2-3": "条件付き達成",
        "Q2-4": "条件付き達成",
        "Q3-1": "達成",
        "Q3-2": "未達",
        "Q3-3": "達成",
        "Q3-4": "条件付き達成",
        "Q3-5": "条件付き達成",
    }
    for goal_id, expected in expected_status.items():
        if not re.search(
            rf"^\| {re.escape(goal_id)} \| {re.escape(expected)} \|",
            status_text,
            flags=re.MULTILINE,
        ):
            raise ValueError(f"{goal_id}: 現在地が{expected}ではない")
    for block in (fixed_block, readme_block, status_text):
        if re.search(r"^\| Q1-(?:3|4) \||^\| Q2-5 \|", block, re.MULTILINE):
            raise ValueError("退役した固定目標の現行行が残っている")

    validate_q2_dependency_ledgers()

    required_paths = (
        SECTIONS / "04_m54_q2_specializations.md",
        SECTIONS / "05_m54_setting_pre_receiver.md",
        SECTIONS / "A3_m54_q2_specialization_proofs.md",
        SECTIONS / "A4_m54_receiver_cycle_proofs.md",
        SECTIONS / "A9_m54_setting_pre_paired_hopf_receiver.md",
        SECTIONS / "A13_m54_template_port_preparation.md",
        SECTIONS / "A15_m54_uniform_register.md",
        SECTIONS / "A16_m54_projector_tree_receiver.md",
        SECTIONS / "A17_m54_uniform_supply.md",
        ROOT / "tools" / "verify_r181a_template_port.py",
        ROOT / "tools" / "verify_r181d_projector_tree.py",
        ROOT / "tools" / "verify_m54_q2_composition.py",
        ROOT / "tools" / "verify_r179_m54_supply.py",
        ROOT / "tools" / "verify_r180_m54_receiver.py",
    )
    retired_paths = (
        SECTIONS / "04_q1xq1_common_bath_gate.md",
        SECTIONS / "05_m52_setting_pre_receiver.md",
        SECTIONS / "A3_q1xq1_common_bath_gate_proofs.md",
        SECTIONS / "A4_m52_receiver_cycle_proofs.md",
        SECTIONS / "A9_m52_setting_pre_paired_hopf_receiver.md",
        SECTIONS / "A13_common_open_preparation.md",
        SECTIONS / "A15_q2_uniform_sequential_sampler.md",
        SECTIONS / "A16_q2_fresh_tape_aperture.md",
        SECTIONS / "A17_q2_uniform_supply.md",
    )
    for path in required_paths:
        if not path.is_file():
            raise ValueError(f"現行M54ファイルがない: {path.relative_to(ROOT)}")
    for path in retired_paths:
        if path.exists():
            raise ValueError(f"退役パスが残っている: {path.relative_to(ROOT)}")

    active_paths = [
        ROOT / "README.md",
        ROOT / "PROJECT_STATUS.md",
        *sorted(SECTIONS.glob("*.md")),
    ]
    active_text = "\n".join(path.read_text(encoding="utf-8") for path in active_paths)
    retired_id = re.compile(
        r"M(?:51|52|53)(?!\d)|R171(?!\d)|R176[ABC](?![A-Z])|"
        r"R178[ABCEF](?![A-Z])|R145(?!\d)"
    )
    hits = sorted(
        path.relative_to(ROOT).as_posix()
        for path in active_paths
        if retired_id.search(path.read_text(encoding="utf-8"))
    )
    if hits:
        raise ValueError("現行文書に退役IDが残っている: " + "、".join(hits))

    theorem_ids = (
        "R181A", "R181B", "R181C", "R181D", "R178D", "R179",
        "R180A", "R180B", "R180C", "R161", "R162", "R164",
        "R123", "R124", "R125",
    )
    for result_id in theorem_ids:
        count = active_text.count(f"定理（{result_id}：")
        if count != 1:
            raise ValueError(f"{result_id}の定理宣言数が{count}である")

    common_text = (SECTIONS / "02_common_canonical_modules.md").read_text(
        encoding="utf-8"
    )
    receiver_text = (SECTIONS / "A16_m54_projector_tree_receiver.md").read_text(
        encoding="utf-8"
    )
    supply_text = (SECTIONS / "A17_m54_uniform_supply.md").read_text(
        encoding="utf-8"
    )
    required_current_tokens = (
        r"\Gamma_{54}^{(n)}",
        r"A_{u,b}^\delta=J_{u,b}+\delta q_bJ_\Sigma",
        "raw比較",
        "selectorをlock",
        "radial-only",
        r"2m(\tau+\gamma)",
        "成功試行だけを再規格化しない",
        "controllerへ書き戻さない",
    )
    current_bundle = common_text + "\n" + receiver_text
    absent = [token for token in required_current_tokens if token not in current_bundle]
    if absent:
        raise ValueError("M54/R181Dの必須要素がない: " + "、".join(absent))
    for token in (
        "aggregate cold誤差",
        "同一の静的二次Hamiltonian",
        "collision cell",
        "spent",
        "総熱は指数的でもよい",
    ):
        if token not in supply_text:
            raise ValueError(f"R179供給境界の必須要素がない: {token}")


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
        "SOURCE_DATE_EPOCH": "1788480000",
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
