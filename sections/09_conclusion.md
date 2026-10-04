@number: 9
@chapter: 本文
@title: 結論
@status: M54共通signal・状態層、M67 finite-Hamiltonian physical parent、M66/R205 thermal open/effective層を総括する。Q3 continuous-tracerはR214A--R214B、generic flow/bathはR209A/R209B、coherent compatibilityはR210A、finite-graphはR208Dを使う。Q1ではR211A--R211C、Q2 thermal sectorではR212A--R212CからM66/R205へ接続する。fixed-goal、strengthening、M0を別判定として維持する。

本稿で得られた最も大きな整理は、量子型構造の古典実現を1つの万能模型へ押し込めるのではなく、**共通signal層**、**M67 finite-Hamiltonian physical parent**、**M66/R205 thermal open/effective層**を分け、その上に用途別の物理模型を接続できる形へしたことである。

第1の共通層はM54である。各試行の実正準自由度から派生複素信号を作り、準備済み入力境界、永続記憶部、作業領域、時計、記録、接続規約をQ1--Q3で共通化する。M37/R86はこのsignal層の具体的な古典振動子実装を与え、R187条件下ではW型最低2正常モードをQ1制御へ接続する。

thermal sectorのfinite-Hamiltonian parentはM67/R212A--R212Cであり、そのopen/effective層がM66/R205A--R205Fである。resolved classical degreeとthermal reservoirの間に現れるphase-volume、mean-flow、matched capacity--conductance、thermal sampling、passive separationを共通化する。中心となるfree energyは

```math
F_{\rm res}(w)
=
-k_BT\log w+C
```

であり、R205Eでは

```math
p_{\rm eq}(Q)
\propto
w(Q)e^{-\beta H_{\rm cfg}(Q)}
```

を得る。R205Cによりmean-flow shiftは同じreservoirのpartition weightを変えずに共存でき、R205Fは空間分離時のgenerator decoupling条件を与える。

ただし、このphysical-parent接続はM64またはM65の全模型、R206 common-hub apparatus全体をM67/R212から導出したという意味ではない。M64/R203Bのpartition/free-energyとmean-flow sectorはR205Cへ対応する。一方、R205D fixed-hub corollaryは旧R204Bと数学的に対応するが、draft-140以後のM65 canonical first-passage lawのphysical liftではない。M64 tracer dynamicsとM65 two-result first-passage lawはそれぞれ固有の物理責務を持つ。R206はM67/R212->M66のQ2終端specializationであり、R207はR212B-rot/R212C->R205A/R205E/R205FをQ2-2のprojection phase-volume共同準備・二端読出しへ特殊化する現行fixed-goal主線である。

Q1では、M37/R187/R140が2モード可逆signalとRabi運動を与え、R189Aが測定に必要な2作用を保持する。M65のtwo-result first-passage selectorがcanonical open result形成を担い、R181Dは固定された安全結果に対応する非規格化射影成分を同じ試行の次操作へ渡す。さらにM67/R211A--R211Cは、二安定basinだけを持つdouble-well marker、phase-volume free energy、finite marker bathからR204Eと同じcomplete-result contractを回収するfinite-Hamiltonian strengtheningを与える。M65のPoisson waiting-time law自体はphysical liftの一致条件にしない。

Q2-1とQ2-3ではR181B/R181Cが永続多モードsignal上でテンソル積状態とgate列を作り、末端4結果または8結果をR206で1回に標本化する。Q2-4ではR206Eで $0^n$ rootを一様準備し、R181Cの一般gate列後に $L=2^n$ のR206 samplerへ接続する。reader側の逐次leaf探索、R181D tree、非終端作用回復、結果別pointer resetを固定主線から外した。一方、M54 direct-amplitude registerへ全自由度加法ノイズが入るR186の障害はreader側とは独立に残り、Q2-4は条件付き達成を維持する。

Q2-2 fixed-goalはM67/R212->M66/R205->R207 projection phase-volume経路で達成する。R212B-rotによりR207A target densityはM67 finite-Hamiltonian two-rotor canonical marginalとしても厳密に回収される。setting directionsと二つのhidden directionをnear-contactでthermal preparationし、projection phase volumeとisotropic lockから一般Bloch方向の余弦共同統計へ接続する。finite thickness/finite lockでも任意精度のsinglet共同分布へ近づき、局所周辺は非信号である。分離後local response factorizationを保つ一方、source hidden stateの分布はsetting-dependentなのでmeasurement independenceは成立しない。

M67はQ3だけでなくQ1 selectorとQ2 thermal sectorにも共通する二実体finite-Hamiltonian physical parentである。Q3では一つのstructured reservoir内部にM37 coherent module、phase-volume、flow、finite bath、R210B bounded dephasing sectorを置き、marker sectorはparticle/readout profileでclassical tracerとして使う。R210Aはfull M67 coherent trajectoryからM37/R86への有限時間compatibilityを、prepared reservoir energy shellから導く $O(N_0^{-1})$ load boundと既存R86 carrier errorに分離して与える。R210BはR123と同じ有限時刻dephasing/revival lawを下方有界なfinite Hamiltonianで回収する。

Q3-2ではR214A/R214BがM67 Brownian dumbbell profileをM64/R203Cのcanonical open lawへ縮約し、R161/R185へ接続する。R209A/R209Bはgeneric flow / finite-bath補題として内部から使い、R210Aはdumbbellを含む任意profileのcoherent loadを $O(N_0^{-1})$ で制御する。Q3-3A--Q3-3CはM67 dephasing profileからR210B/R123へ、Q3-4A/B/5はM67 finite-graph profileからR208D/R203DとR124/R182/R125/R161へ接続する。M37、M64、R123は削除せず、それぞれcoherent module、open effective reduction、effective dephasing lawとしてactiveに残る。R162はR161 lawのoptional Poisson realizationであり、M67の基礎的存在論には含めない。

固定目標の達成と、より強い物理実装は分けて判定する。現行fixed-goalではQ1-1、Q1-2、Q2-1、Q2-2、Q2-3、Q3-1--Q3-5を達成、Q2-4を条件付き達成、Q3-6を未達とする。A1/A2/B1--B3は独立のstrengtheningであり、fixed-goal達成から自動的に上がらない。

残る主要課題は5群に整理できる。第1にQ2-4のR186 direct-amplitude register robustness、第2にQ2 signal/NBL/register/gateとR206 apparatus全体のM67統合、第3にQ3-6の位相量子化、第4に各系列のA1/A2/B1--B3、第5にM0である。M0ではM54/M66という共通原理を共有するだけでは足りず、主要自由度、物理接続端、準備、操作、測定、永久記録、reset、clock、renewalを1つのjoint microscopic device/processと共通反復周期へ接続する必要がある。

従って現時点の統一は、**同一のsignal原理とreservoir原理を複数の量子型現象へ再利用できること**にある。全現象を1つの製造済み装置、1つの単一bath、1つの閉鎖Hamiltonian全系へ統合したという主張ではない。そこを明確に分けることで、すでに閉じた固定目標と、次に検査すべき物理実装・数値・実験の課題を同じ体系で管理できる。

M67ではR214A--R214Bをcontinuous Q3-2、R208Dをfinite-graph dispatch、R209A/R209Bをgeneric flow/bath、R210A/R210Bをcoherent/dephasing compatibilityとして採用する。R211A--R211CはQ1 selector、R212A--R212CはM66/R205 thermal layerのfinite-Hamiltonian physical parentとして採用する。ただしこれはQ1全体、Q2 signal/register/gate、R206 apparatus全体を同じ装置へ統合したこと、M0を達成したこと、A1/A2を自動達成したことを意味しない。Q3-6の位相量子化、strict locality、continuous-space一様極限、多粒子、全周期統合は別課題として残る。

draft-145ではR214A--R214BをQ3 continuous-tracerのrequired主線へ昇格する。有限自然長を持つ三次元伸縮Brownian dumbbellの内部位相空間が $\rho+\rho_T$ に比例する自由エネルギーを近似し、finite bathによる実時間熱化、small-mass $W_1$ bridge、single-dumbbell FDT補正、$O(N_0^{-1})$ signal backreactionまで同じM67二実体architecture内で閉じる。R208B/R208C/R209CはPR1ではactive regressionとして残し、退役は後続PRへ分離する。
