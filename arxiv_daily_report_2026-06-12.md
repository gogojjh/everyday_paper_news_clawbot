# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-06-12 08:03

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 8/20 篇提供

**🌟 Highlight**: 20 篇 | **📌 Poster**: 0 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. World Pilot: Steering Vision-Language-Action Models with World-Action Priors

- **作者**: Zefu Lin, Rongxu Cui, Junjia Xu, Xiaojuan Jin, Wenling Li, Lue Fan, Zhaoxiang Zhang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.12403v1)
- **发表日期**: 2026-06-10
- **匹配关键词**: VLA, vision-language-action, vision-language-action model
- **arXiv**: [2606.12403v1](http://arxiv.org/abs/2606.12403v1)
- **📥 PDF**: 已下载至本地 (`2606.12403v1_World_Pilot_Steering_Vision-Language-Action_Models_with_World-Action_Priors.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://world-pilot.github.io/
- **中文摘要**: 视觉-语言-动作（VLA）模型继承自大规模预训练的语义基础，并在分布内的操作任务中表现出色。然而，这种语义基础建立在静态图像-文本对之上，而操作是一个连续的、密集接触的过程，其动态特性无法通过此类预训练捕捉。我们提出World Pilot，一种VLA框架，通过世界-动作模型（WAM）的先验知识增强策略，并通过两条互补路径将其融入决策链。潜空间引导通过场景演化潜变量调节感知层，动作引导则提供预期轨迹作为动作生成器的运动先验。这两个先验共同赋予VLA对场景的预期视角和轨迹级运动提示，同时保留其语义条件，并且即使由未经动作后训练的视频预训练世界模型提供，场景演化先验依然有效。World Pilot在LIBERO-Plus零样本OOD基准测试中达到了84.7%的最优总成功率，并在四项操作任务的所有真实机器人场景中均取得最高成功率，在视角、几何、可变形状态和姿态变化下展现出最大优势。项目网站：https://world-pilot.github.io/

---

### 2. DIRECT: When and Where Should You Allocate Test-Time Compute in Embodied Planners?

- **作者**: Jadelynn Dao, Milan Ganai, Yasmina Abukhadra, Ajay Sridhar, Mozhgan Nasr Azadani, Katie Luo, Clark Barrett, Jiajun Wu, Chelsea Finn, Marco Pavone ⭐
  - **高亮作者**: Chelsea Finn
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.12402v1)
- **发表日期**: 2026-06-10
- **匹配关键词**: VLA
- **arXiv**: [2606.12402v1](http://arxiv.org/abs/2606.12402v1)
- **📥 PDF**: 已下载至本地 (`2606.12402v1_DIRECT_When_and_Where_Should_You_Allocate_Test-Time_Compute_in_Embodied_Planners?.pdf`)
- **🔓 开源**: PROJECT_PAGE
- **中文摘要**: 视觉-语言模型（VLMs）正越来越多地被部署为具身智能体的高层规划器，其中一种新兴策略是通过扩展测试时计算来提升能力。然而，我们观察到这种做法会增加延迟、令牌消耗和浮点运算次数，同时在下游任务中带来不均匀且往往递减的收益，从而限制了具身智能体的部署场景。我们认为，选择何时何地投入测试时计算是将前沿性能带入现实世界的关键。我们提出了DIRECT框架，这是一种路由框架，利用多模态场景上下文为每个提示分配计算资源，从而在成功-成本帕累托前沿上优于固定模型选择。在三个主要的扩展维度上，即思维链深度、模型规模和记忆历史，我们在VLABench和RoboMME上的实验表明，测试时计算并非一个统一的杠杆：不同维度会产生性质上不同的能力增益。我们在DROID设置中的物理Franka机械臂上验证了这些见解，涵盖了零样本操作和长时程链式任务，其中我们的路由器在平均延迟降低高达65%的情况下，匹配或超越了更强模型的成功率。最终，我们的结果表明，简单地扩展测试时计算是浪费的，而DIRECT能够以极低的成本在机器人系统中提供前沿水平的具身规划能力。项目页面可访问 jadee-dao.github.io/direct/。

---

### 3. Ambient Diffusion Policy: Imitation Learning from Suboptimal Data in Robotics

- **作者**: Adam Wei, Nicholas Pfaff, Thomas Cohn, Arif Kerem Dayı, Constantinos Daskalakis, Giannis Daras, Russ Tedrake
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.12365v1)
- **发表日期**: 2026-06-10
- **匹配关键词**: diffusion policy
- **arXiv**: [2606.12365v1](http://arxiv.org/abs/2606.12365v1)
- **📥 PDF**: 已下载至本地 (`2606.12365v1_Ambient_Diffusion_Policy_Imitation_Learning_from_Suboptimal_Data_in_Robotics.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出环境扩散策略（Ambient Diffusion Policy），这是一种从机器人领域次优数据中进行模仿学习的简洁且原理性方法。高质量、任务特定的机器人数据采集成本高昂且耗时，而低质量或分布外演示的次优数据集则十分丰富。现有在机器人领域对两类数据源进行联合训练的方法，往往难以区分次优样本中的有效特征与有害特征。相比之下，我们的方法通过引入机器人联合训练的新维度——噪声依赖的数据使用策略，仅提取有用特征。环境扩散策略将次优数据在训练中的贡献限制在高扩散时间和低扩散时间阶段。为严格论证该方法，我们首先观察到机器人动作数据呈现频谱幂律分布。这引出了最优扩散策略的两个重要特性：全局到局部的层次性以及局部性。我们通过简化模型对此进行了理论形式化。实验在六项任务中针对四类次优动作数据（含噪声轨迹、仿真到现实差距、任务不匹配及大规模数据混合）验证了环境扩散策略的有效性。结果表明，该方法能有效学习任意来源的次优数据。值得注意的是，当扩展至Open X-Embodiment（一个包含异质数据质量与非结构化分布偏移的大规模数据集）时，其性能较现有联合训练基线提升高达33%。总体而言，环境扩散策略提升了次优演示的利用价值，拓展了机器人领域可用数据源的范畴。

---

### 4. CHORUS: Decentralized Multi-Embodiment Collaboration with One VLA Policy

- **作者**: Ria Doshi, Tian Gao, Annie Chen, Chelsea Finn, Jeannette Bohg ⭐
  - **高亮作者**: Chelsea Finn
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.12352v1)
- **发表日期**: 2026-06-10
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2606.12352v1](http://arxiv.org/abs/2606.12352v1)
- **📥 PDF**: 已下载至本地 (`2606.12352v1_CHORUS_Decentralized_Multi-Embodiment_Collaboration_with_One_VLA_Policy.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 多机器人协作使机器人能够高效完成广泛任务，从将沙发搬过门框到在建筑工地上组装结构。然而，在移动多机器人场景中实现这种协调仍具挑战性：基于团队联合观测的集中式方法会随团队规模扩大而扩展性变差，而每台机器人独立训练策略的分散式方法通常需要显式对齐流程或推理时的信息共享来克服部分可观测性。我们的核心见解是：预训练的视觉-语言-动作（VLA）模型的视觉运动先验应能仅通过每台机器人的局部观测实现反应式、分散式协作，无需这些推理时的假设。我们提出CHORUS框架，该框架将单一VLA骨干网络适配到多样化的多机器人团队控制中。推理时，每台机器人独立运行CHORUS副本，仅依赖自身观测和机器人标识提示。在包括移动卷尺测量、图书馆书籍传递和洗衣篮搬运的真实世界实验中，CHORUS相比分散式从头训练模型实现了64%的性能提升，对队友行为的反应性提高了40个百分点，并超越了集中式基线方法。这些结果共同表明，共享的VLA骨干网络能够实现分散式多机器人协作，无需每台机器人独立策略或推理时的机器人间通信。

---

### 5. Learning What to Say to Your VLA: Mostly Harmless Vision Language Action Model Steering

- **作者**: Hyun Joe Jeong, Gokul Swamy, Andrea Bajcsy
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.12299v1)
- **发表日期**: 2026-06-10
- **匹配关键词**: VLA, vision language action, vision language action model, vision-language-action
- **arXiv**: [2606.12299v1](http://arxiv.org/abs/2606.12299v1)
- **📥 PDF**: 已下载至本地 (`2606.12299v1_Learning_What_to_Say_to_Your_VLA_Mostly_Harmless_Vision_Language_Action_Model_Steering.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型为机器人控制提供了自然语言接口，但语言到行为的映射往往脆弱且不直观：语义相似的指令可能引发截然不同的行为，而某些能力仅通过提示无法激发。因此，人类指令和零样本语言模型都难以可靠地引导VLA模型成功完成任务。本研究提出一种框架，通过交互式搜索能提升闭环VLA任务性能的语言序列，将这些序列蒸馏为测试时语言反馈策略（LFP），并学习一个预测何时语言引导能提升性能的改进头。我们对该改进头进行共形化处理，以防止在分布外场景中LFP相对于原始指令降低任务性能的有害干预。关键在于，本方法适用于任意冻结的预训练VLA模型，既无需访问原始训练分布，也无需微调基础模型。在已知环境中，共形化LFP使基础VLA模型在仿真中性能提升24.7%，在硬件中提升65.0%。面对视觉和语义扰动时，共形化LFP具有强无害性保证，并能产生开环提示无法观察到的恢复行为。

---

### 6. Bridging the Morphology Gap: Adapting VLA Models to Dexterous Manipulation via Intent-Conditioned Fine-Tuning

- **作者**: Chuanke Pang, Junyi Huang, Zhijun Zhao, Yaobing Wang, Kun Xu, Xilun Ding
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.12109v1)
- **发表日期**: 2026-06-10
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2606.12109v1](http://arxiv.org/abs/2606.12109v1)
- **📥 PDF**: 已下载至本地 (`2606.12109v1_Bridging_the_Morphology_Gap_Adapting_VLA_Models_to_Dexterous_Manipulation_via_Intent-Conditioned_Fin.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型在机器人操作中展现出显著的零样本泛化能力，然而绝大多数预训练流程仍严格局限于低自由度平行夹爪。将这些丰富的语义先验知识适配至高自由度灵巧手时，会引入严重的形态学鸿沟——直接进行端到端联合微调会因数据稀缺而导致空间推理能力的灾难性遗忘和动作流形的急剧坍缩。本文提出InDex，一种基于跨形态语义继承的新型数据高效适配框架。我们并未丢弃预训练的单自由度平行抓取输出，而是将其重新用作连续的宏观虚拟抓取意图代理，以实现控制拓扑的序列化。我们构建了两阶段解耦学习架构：第一阶段通过参数高效方式对齐VLA主干网络，使其预测连续机械臂轨迹与标量抓取意图；第二阶段冻结该空间主干网络，利用意图条件去噪扩散头解码多指末端执行器的细粒度关节运动。在包含多阶段、高接触灵巧操作任务的仿真基准测试中，InDex能以极少量演示数据有效掌握复杂技能，在保持原始VLA先验鲁棒空间泛化能力的同时，显著优于整体式基线方法。

---

### 7. Embodied-BenchClaw: An Autonomous Multi-Agent System for Embodied Spatial Intelligence Benchmark Construction

- **作者**: Baoyang Jiang, Fengchun Zhang, Leyuan Wang, Haotian Li, Yida Wang, Zhe Ji, Jinshan Lai, Xi Ren, Jianwei Hu, Qiang Ma
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.11909v1)
- **发表日期**: 2026-06-10
- **匹配关键词**: navigation, robot navigation
- **arXiv**: [2606.11909v1](http://arxiv.org/abs/2606.11909v1)
- **📥 PDF**: 已下载至本地 (`2606.11909v1_Embodied-BenchClaw_An_Autonomous_Multi-Agent_System_for_Embodied_Spatial_Intelligence_Benchmark_Cons.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 基准测试对于评估具身空间智能至关重要，但其构建过程劳动密集、难以复用且维护困难。现有具身基准测试往往静态不变，随着模型性能提升可能迅速饱和，难以区分新能力。我们提出Embodied-BenchClaw——一个用于构建具身空间智能基准的自主智能系统。给定用户指定的评估意图，Embodied-BenchClaw通过五个阶段流水线自动生成完整且可持续更新的基准测试包：意图蓝图设计、数据采集、结构化与清洗、基准合成、评估报告生成。该流水线由三个智能体协同完成规划、构建与评估任务。为提升可复用性与可靠性，Embodied-BenchClaw引入了可扩展的技能库与过程质量控制机制，使基准构建具备可组合、可验证、可修复的特性。我们实例化了多个基准测试，涵盖室内空间推理、室外空间推理、机器人操作、四足机器人导航、无人机/航拍视角理解以及静态基准增强。这些基准测试覆盖了多样化的具身载体、数据源与空间能力。通过人工评估、裁判模型评估、一致性检验、成本分析与消融实验，结果表明Embodied-BenchClaw能够构建可验证、可执行、可维护且具有诊断价值的具身空间基准测试，同时显著减少人工投入。

---

### 8. DuoBench: A Reproducible Benchmark for Bimanual Manipulation in Simulation and the Real World

- **作者**: Tobias Jülg, Seongjin Bien, Simon Hilber, Yannik Blei, Pierre Krack, Maximilian Li, Sven Parusel, Rudolf Lioutikov, Florian Walter, Wolfram Burgard ⭐
  - **高亮作者**: Wolfram Burgard
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.11901v1)
- **发表日期**: 2026-06-10
- **匹配关键词**: vision-language-action, bimanual manipulation
- **arXiv**: [2606.11901v1](http://arxiv.org/abs/2606.11901v1)
- **📥 PDF**: 已下载至本地 (`2606.11901v1_DuoBench_A_Reproducible_Benchmark_for_Bimanual_Manipulation_in_Simulation_and_the_Real_World.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 双机器人系统显著扩展了操作能力，但双臂协调引入了额外的控制复杂性和故障模式，现有基准测试未能充分捕捉这些问题。我们提出DuoBench，一个基于FR3 Duo平台的可扩展双臂操作策略基准测试框架。DuoBench包含涵盖四类协调模式的11项任务，在仿真环境中实现，并通过可复现的任务方案（含3D打印资产）在真实世界中部分复现。此外，我们提出一种基于阶段的评估方案，支持超越二元成功/失败的细粒度语义故障分析，并为所有基准任务提供人类遥操作数据集。我们在仿真环境和真实硬件上对多种双臂模仿学习与视觉-语言-动作策略进行了基准测试。结果表明，当前策略在处理双臂操作时仍面临挑战，尤其在早期交互阶段、并行手臂执行以及仿真与真实环境之间的迁移方面。DuoBench为诊断这些故障模式并研究未来双臂策略学习方法提供了可复现的测试平台。代码、数据集和视频见https://duobench.github.io/。

---

### 9. Critic Architecture Matters: Dual vs. Unified Critics for Humanoid Loco-Manipulation

- **作者**: Mehmet Turan Yardımcı
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.11891v1)
- **发表日期**: 2026-06-10
- **匹配关键词**: locomotion and manipulation
- **arXiv**: [2606.11891v1](http://arxiv.org/abs/2606.11891v1)
- **📥 PDF**: 已下载至本地 (`2606.11891v1_Critic_Architecture_Matters_Dual_vs._Unified_Critics_for_Humanoid_Loco-Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 面向人形机器人的多目标强化学习需在单一策略中协调运动与操作。一个自然的设计选择是：采用统一评价器（单一评价器）来估计所有目标的综合价值，还是采用分离评价器（双评价器）处理不相交的奖励信号。我们在NVIDIA Isaac Lab中基于Unitree G1人形机器人（23个主动自由度）进行了控制对比实验，通过包含13个难度等级（从静态抓取到变向目标行走）的序列化课程训练运动-操作策略。在标准化评估中，双评价器策略相比统一评价器策略：目标到达速度提升3.5倍（6.5步 vs 22.6步仿真步数），吞吐量提升2倍（每千步有效到达次数14.3次 vs 7.0次），有效到达率更高（65.2% vs 53.8%）。值得注意的是，额外添加的反博弈奖励机制在架构变更基础上未带来进一步提升（60.9% vs 65.2%）。这些结果对新兴的模仿学习策略强化学习微调范式具有直接启示：当用强化学习优化预训练操作策略时，统一评价器可能因竞争性运动梯度而抑制已习得行为。研究表明，评价器架构是人形机器人多目标强化学习中首要且常被忽视的设计选择，其对到达效率的影响远超奖励工程。

---

### 10. SG2Loc: Sequential Visual Localization on 3D Scene Graphs

- **作者**: Nicole Damblon, Olga Vysotska, Federico Tombari, Marc Pollefeys, Daniel Barath ⭐
  - **高亮作者**: Marc Pollefeys
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.11880v1)
- **发表日期**: 2026-06-10
- **匹配关键词**: scene graph
- **arXiv**: [2606.11880v1](http://arxiv.org/abs/2606.11880v1)
- **📥 PDF**: 已下载至本地 (`2606.11880v1_SG2Loc_Sequential_Visual_Localization_on_3D_Scene_Graphs.pdf`)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/DmblnNicole/sg2loc.
- **中文摘要**: 复杂室内环境中的视觉定位仍是机器人和增强现实应用面临的关键挑战。对于自主智能体而言，通过时序优化位姿估计的序列定位方法至关重要。然而传统方法通常需要存储大量图像数据库或点云数据，导致显著的系统开销。本文提出了一种基于三维场景图的轻量级序列视觉定位新方法。该方法采用紧凑的场景图表示环境，其中节点代表物体（附带粗粒度网格），边编码空间关系。在定位阶段，我们对每张输入图像提取逐块语义特征，预测物体身份。定位过程在粒子滤波框架内完成：每个代表相机位姿的粒子将场景图中的粗粒度物体网格投影至图像，根据可见性为图像块分配物体身份。通过比较输入图像中逐块特征与场景图物体特征的相似度，确定粒子权重。后续图像被顺序整合，持续优化位姿估计。通过利用紧凑场景图与高效语义匹配，本方法在保持真实世界数据集性能的同时显著降低了存储需求。代码将开源至https://github.com/DmblnNicole/sg2loc。

---

### 11. Blind Dexterous Grasping via Real2Sim2Real Tactile Policy Learning

- **作者**: Shengcheng Luo, Xiyan Huang, Zhe Xu, Wanlin Li, Ziyuan Jiao, Chenxi Xiao
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.11767v1)
- **发表日期**: 2026-06-10
- **匹配关键词**: diffusion policy, dexterous grasping, diffusion-based policy
- **arXiv**: [2606.11767v1](http://arxiv.org/abs/2606.11767v1)
- **📥 PDF**: 已下载至本地 (`2606.11767v1_Blind_Dexterous_Grasping_via_Real2Sim2Real_Tactile_Policy_Learning.pdf`)
- **🔓 开源**: PROJECT_PAGE
- **中文摘要**: 灵巧手的盲抓是一项关键的操作能力。然而，由于触觉模拟与真实环境之间的差距以及稀疏触觉信号的有限表达能力，为真实机器人学习这种仅依赖触觉的策略仍然具有挑战性。为弥合这一差距，我们提出了一种可在物理多指机器人手上部署的仅触觉盲抓框架。该方法结合了三个关键组成部分。首先，我们引入了一个真实到模拟的触觉校准流程，构建了一个能够复现真实触觉信号的接触校准数字孪生模拟器。其次，我们利用布局感知的触觉编码器提高了稀疏触觉观测的表达能力，该编码器通过自监督预训练融入了传感器几何先验知识。第三，为提升对未见物体的泛化能力，我们在校准后的模拟器中训练了面向特定物体的强化学习专家，并将其成功抓取轨迹聚合为触觉条件扩散策略。我们在配备分布式触觉传感器的物理LEAP手上对方法进行了评估，测试对象包括10个已知物体和10个未知物体。部署的策略在所有20个物体上实现了27%的真实世界抓取成功率，且无需真实抓取演示或视觉输入。模拟消融实验表明，布局感知的触觉预训练提升了抓取性能，而传感层面的评估证实真实到模拟的校准提高了模拟与硬件之间触觉接触事件的一致性。这些结果表明，接触事件校准、几何感知触觉表征学习以及基于扩散的策略聚合，为在真实灵巧手上实现仅触觉盲抓提供了一条有效路径。项目页面：Dex-Blind-Grasp.github.io。

---

### 12. TacCoRL: Integrating Tactile Feedback into VLA via Simulation

- **作者**: Siyu Ma, Yuqi Liang, Chang Yu, Yunuo Chen, Hao Su, Yixin Zhu, Yin Yang, Chenfanfu Jiang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.11743v1)
- **发表日期**: 2026-06-10
- **匹配关键词**: VLA, vision-language-action, exploration
- **arXiv**: [2606.11743v1](http://arxiv.org/abs/2606.11743v1)
- **📥 PDF**: 已下载至本地 (`2606.11743v1_TacCoRL_Integrating_Tactile_Feedback_into_VLA_via_Simulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型为机器人操作提供了强大的视觉、语言和动作先验知识，但仅凭视觉观测往往无法捕捉接触密集型任务所需的局部接触状态。我们提出TacCoRL——一种可扩展的框架，通过将触觉反馈注入VLA策略，并借助仿真-真实协同训练与基于仿真的强化学习（RL）来改进策略，无需大规模触觉预训练或大量真实世界接触探索。其核心思想不仅在于将触觉作为输入，更在于学习在接近失败状态时接触读数应如何调节动作响应——这类状态在演示中罕见且通过硬件采集风险较高。我们采用与真实环境对齐的仿真器作为接触交互的闭环训练环境。混合仿真与真实轨迹首先对预训练策略中的触觉条件化动作进行热启动。随后，基于可验证任务奖励的强化学习利用仿真接触轨迹优化策略：强化能完成任务的触觉条件化动作，同时通过真实轨迹上的监督目标使优化后的策略锚定于部署时的视觉、触觉与动作分布。最终策略可直接迁移至真实机器人，无需特权仿真状态或在线真实世界强化学习。在四项双臂接触密集型任务中，最终视觉-触觉策略的平均成功率达72.5%，而基线方法仅为50.0%。结果视频及更多详情请访问https://tac-corl.github.io/。

---

### 13. SAFER-Nav: Enhancing Safety for Visual Robot Navigation via Segmentation-Aware Fine-Tuning

- **作者**: Geonyeong Ko, Giung Lee, Changjoo Nam
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.11636v1)
- **发表日期**: 2026-06-10
- **匹配关键词**: navigation, robot navigation
- **arXiv**: [2606.11636v1](http://arxiv.org/abs/2606.11636v1)
- **📥 PDF**: 已下载至本地 (`2606.11636v1_SAFER-Nav_Enhancing_Safety_for_Visual_Robot_Navigation_via_Segmentation-Aware_Fine-Tuning.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 基于视觉的导航模型，特别是基础模型，能够仅从RGB观测中生成可行的轨迹。然而，即使是最先进的基于Transformer和扩散模型的策略，在包含未知障碍物或条件变化的陌生部署环境中仍难以泛化。由此产生的轨迹往往具有目标导向性，但安全性不足。现有工作通过外部轨迹修正或内部几何先验来提升安全性，但所得到的策略并未被训练以显式表示障碍物边界或可通行自由空间结构。为解决这一问题，我们提出了一种导航模型，该模型通过微调将这些结构直接融入策略中，并设计为兼容多种基于RGB的骨干网络。在多个机器人平台、室内环境以及静态和动态障碍物场景中，我们的方法相较于ViNT、NoMaD及其CARE增强变体，在保持目标到达性能的同时，降低了碰撞频率。

---

### 14. Adversarial Attacks on Learned Policies for Surgical Robotic Tasks

- **作者**: Shutong Jin, Ziyang Chen, Preethi Satish, Paavan Gupta, Florian T. Pokorny, Ken Goldberg
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.11535v1)
- **发表日期**: 2026-06-10
- **匹配关键词**: diffusion policy
- **arXiv**: [2606.11535v1](http://arxiv.org/abs/2606.11535v1)
- **📥 PDF**: 已下载至本地 (`2606.11535v1_Adversarial_Attacks_on_Learned_Policies_for_Surgical_Robotic_Tasks.pdf`)
- **🔓 开源**: PROJECT_PAGE
- **中文摘要**: 基于学习的策略正被考虑用于增强机器人辅助手术中人类外科医生的灵巧性。从视觉观察到机器人动作的端到端映射是否容易受到对抗性攻击，从而可能导致患者受伤？本文首次研究了手术机器人中基于学习策略面临的对抗性威胁。我们探讨了两种威胁模式：（a）破坏性攻击，即难以察觉的视觉扰动中断策略执行；（b）导向攻击，即此类扰动将策略动作引向攻击者指定的方向。我们提出了三种对抗性攻击方法，每种方法对策略信息的访问权限逐步增加，并评估了它们对两项手术子任务（清创术和缝合术）的影响。评估覆盖了三种端到端策略架构：ACT、扩散策略和Pi0。此外，我们引入了一类新型光度对抗攻击，通过模拟自然视觉变化（如光照变化）生成有效且视觉上合理的扰动。基于560次使用清创和缝合模型的物理实验结果表明，最先进的策略可能被显著干扰，导致手术子任务成功率平均降低61%。项目页面：https://sites.google.com/view/adversary-surgery

---

### 15. Dynamic Execution Horizon Prediction for Chunk-based Robot Policies

- **作者**: Yuchi Zhao, Miroslav Bogdanovic, Arjun Sohal, Liyu Tao, Kourosh Darvish, Alán Aspuru-Guzik, Florian Shkurti, Animesh Garg
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.11408v1)
- **发表日期**: 2026-06-09
- **匹配关键词**: vision-language-action, vision-language-action model
- **arXiv**: [2606.11408v1](http://arxiv.org/abs/2606.11408v1)
- **📥 PDF**: 已下载至本地 (`2606.11408v1_Dynamic_Execution_Horizon_Prediction_for_Chunk-based_Robot_Policies.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://dehp-chunking.github.io/
- **中文摘要**: 动作分块已成为现代机器人策略中的标准设计，从扩散/流策略到视觉-语言-动作模型，策略会预测一系列动作并执行固定数量的动作，而非逐步执行。然而，这一范式依赖于一个关键假设：固定的执行步长。在分块执行过程中，策略以开环方式运行，这对于需要频繁重新规划的精细操作任务而言尤为不利。实践中，执行步长通常通过经验调参确定，且高度依赖具体任务。为此，我们提出动态执行步长预测（DEHP）方法，该方法通过在线强化学习训练轻量级执行步长预测分支，同时完全冻结预训练的分块策略。这使得该方法兼容黑盒分块策略，并将执行步长调整的影响与底层动作生成器的变化相隔离。在多项评估中，DEHP大幅提升了不同高精度和长时程操作任务的成功率。定性分析进一步表明，DEHP在任务的精细操作阶段预测更短的执行步长，而在自由空间运动中预测更长的步长。通过这种方式，DEHP平衡了开环分块执行的效率与闭环单步控制的响应性。项目页面：https://dehp-chunking.github.io/

---

### 16. Embodied-R1.5: Evolving Physical Intelligence via Embodied Foundation Models

- **作者**: Yifu Yuan, Yaoting Huang, Xianze Yao, Yutong Li, Shuoheng Zhang, Linqi Han, Pengyi Li, Jiangeng Sun, Wenting Jia, Zhao Zhang, Yuhao Liu, Ruihao Liao, Yucheng Hu, Qiyu Wu, Yuxiao Li, Zibin Dong, Fei Ni, Yan Zheng, Shuyang Gu, Yi Ma, Hongyao Tang, Han Hu, Jianye Hao
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.11324v1)
- **发表日期**: 2026-06-09
- **匹配关键词**: VLA, articulated object, object manipulation, affordance
- **arXiv**: [2606.11324v1](http://arxiv.org/abs/2606.11324v1)
- **📥 PDF**: 已下载至本地 (`2606.11324v1_Embodied-R1.5_Evolving_Physical_Intelligence_via_Embodied_Foundation_Models.pdf`)
- **🔓 开源**: MODEL, CODE
- **中文摘要**: 我们提出Embodied-R1.5，一种统一的具身基础模型（EFM），它将涵盖具身认知、任务规划、纠错与指向等综合具身推理能力集成于单一架构中，旨在实现通用物理智能。通过三条自动化数据构建流水线显著扩展关键能力的数据覆盖范围，我们构建了超过150亿词元的大规模数据系统，并设计了多任务平衡的强化学习方案以缓解异构任务冲突。进一步提出规划器-基础模型-纠错器（PGC）闭环框架，使单一模型能够自主执行长时域任务并进行自我修正。仅凭80亿参数，Embodied-R1.5在24个具身视觉语言模型基准测试中的16项上达到最优水平，超越Gemini-Robotics-ER-1.5和GPT-5.4等领先模型。得益于内化的具身能力，Embodied-R1.5仅需少量数据即可微调为视觉-语言-动作模型，在4个主流操作基准套件中性能超越$π_{0.5}$等领先VLA模型。我们进一步开展大量零样本真实机器人实验，验证其在指令跟随、可供性定位、铰接物体操作及长时域复杂任务中的表现，展现出对物理世界的强泛化能力。我们开源模型权重、数据集、训练代码以及专为具身任务设计的评估框架EmbodiedEvalKit，以促进EFM领域的未来研究。

---

### 17. WorldOlympiad: Can Your World Model Survive a Triathlon?

- **作者**: Yuke Zhao, Wangbo Zhao, Weijie Wang, Zeyu Zhang, Dakai An, Akide Liu, Yinghao Yu, Jiasheng Tang, Fan Wang, Wei Wang, Bohan Zhuang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.11129v1)
- **发表日期**: 2026-06-09
- **匹配关键词**: gaussian splatting
- **arXiv**: [2606.11129v1](http://arxiv.org/abs/2606.11129v1)
- **📥 PDF**: 已下载至本地 (`2606.11129v1_WorldOlympiad_Can_Your_World_Model_Survive_a_Triathlon?.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出了WorldOlympiad，这是一个用于诊断基于视频的世界模型在物理真实性、几何一致性和交互保真度方面的基准测试。现有基准通常侧重于视觉质量、语义对齐或短期时间连贯性，但它们在判断生成视频是否遵循物理规则、保持连贯的三维结构以及支持长期可控交互方面提供的洞察有限。为填补这一空白，WorldOlympiad将世界模型评估分解为三个互补维度。物理轨道利用对象分割和MLLM作为评判标准，评估生成视频是否遵循力学、热现象和材料属性中的可解释规则。几何轨道通过高斯泼溅重建生成视频，并评估结构一致性、跨视角连贯性以及相机轨迹对齐。交互轨道则评估生成的序列是否遵循复杂的动作提示，并在连续视频片段之间保持平滑、连贯的过渡。WorldOlympiad进一步覆盖了三个主要的下游场景，包括游戏、机器人以及通用真实世界视频，捕捉从交互控制、具身操作到开放域运动和相机动态的多样化挑战。这些轨道和场景共同构成了一个可扩展且可解释的评估套件，能够揭示超出通用视频质量的失败模式。在最新模型上的实验表明，物理推理、三维一致性和长期交互方面存在显著差距，这凸显了为生成式世界模型设计更结构化评估协议的必要性。

---

### 18. VLGA: Vision-Language-Geometry-Action Models for Autonomous Driving

- **作者**: Jin Yao, Dhruva Dixith Kurra, Tom Lampo, Zezhou Cheng, Danhua Guo, Burhan Yaman
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.12396v1)
- **发表日期**: 2026-06-10
- **匹配关键词**: VLA, vision-language-action, vision-language-action model
- **arXiv**: [2606.12396v1](http://arxiv.org/abs/2606.12396v1)
- **📥 PDF**: 已下载至本地 (`2606.12396v1_VLGA_Vision-Language-Geometry-Action_Models_for_Autonomous_Driving.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型能够描述场景并基于语言进行推理，但在将动作锚定于周围密集的三维世界时仍存在困难。现有方法要么从冻结的三维基础模型中注入特征，却缺乏确保策略使用这些特征的目标函数；要么通过稀疏的边界框和地图损失约束几何结构，无法提供密集的空间信号。我们提出VLGA——首个通过重建其驾驶场景的密集三维世界进行监督的视觉-语言-动作模型。VLGA将几何作为第四模态引入视觉、语言和动作的框架中，通过专用专家模块实现，该模块利用基于激光雷达的逐像素点图回归损失进行监督。在具有挑战性的nuScenes数据集（开环评估）和Bench2Drive数据集（闭环评估）上进行的大量实验表明，VLGA相较于同类VLA方法具有显著优势。具体而言，在开环nuScenes基准测试中，VLGA在无自车状态信息的VLA方法中创下新纪录，实现了最低的L2误差（平均0.50米）和3秒碰撞率（0.18%）。在闭环Bench2Drive基准测试中，VLGA以79.08分的驾驶得分达到最优水平，较此前最强的VLA方法提升0.71分，同时保持相当的效率和舒适性。

---

### 19. APT: Action Expert Pretraining Improves Instruction Generalization of Vision-Language-Action Policies

- **作者**: Kechun Xu, Zhenjie Zhu, Anzhe Chen, Rong Xiong, Yue Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.12366v1)
- **发表日期**: 2026-06-10
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2606.12366v1](http://arxiv.org/abs/2606.12366v1)
- **📥 PDF**: 已下载至本地 (`2606.12366v1_APT_Action_Expert_Pretraining_Improves_Instruction_Generalization_of_Vision-Language-Action_Policies.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://xukechun.github.io/papers/APT/
- **中文摘要**: 视觉-语言-动作（VLA）模型通过将预训练的视觉-语言模型（VLM）与连续动作专家模块相结合，在操作任务中展现出强大性能，但对分布外（OOD）语言指令的泛化能力仍然较差。已知的一个挑战是VLA数据中的结构不平衡问题——语言内容的多样性远低于视觉和动作内容，导致策略容易依赖视觉捷径。尽管离散动作方法通过视觉-语言联合训练缓解了这一问题，但连续动作专家缺乏此类保护：它们从随机初始化开始，完全基于不平衡数据学习，产生的噪声梯度会破坏VLM并无法利用其语言能力。我们从贝叶斯视角出发，将策略分解为与语言无关的视觉-动作（VA）先验和语言条件化的VLA似然，并提出APT——一种强调动作专家预训练的两阶段训练方法。第一阶段，动作专家作为VA先验，在冻结VLM的视觉-动作对上进行预训练，从而绕过语言不平衡问题。第二阶段，通过门控融合机制注入语言标记，在保留已学习视觉运动先验的同时整合VLM特征。APT适用于主流VLA架构，包括π和GR00T风格架构。大量实验证明，APT在未见指令和组合任务上均取得一致性能提升。项目页面：https://xukechun.github.io/papers/APT/

---

### 20. Echoes of the Prior: A Computational Phenomenology of Forgetting

- **作者**: Gege Gao, Bernhard Schölkopf, Andreas Geiger ⭐
  - **高亮作者**: Andreas Geiger
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.12340v1)
- **发表日期**: 2026-06-10
- **匹配关键词**: 3d reconstruction, 3D reconstruction
- **arXiv**: [2606.12340v1](http://arxiv.org/abs/2606.12340v1)
- **📥 PDF**: 已下载至本地 (`2606.12340v1_Echoes_of_the_Prior_A_Computational_Phenomenology_of_Forgetting.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 记忆不仅仅是数据的存储，更是现实的骨架。当生物记忆消退时，世界并非简单地陷入黑暗，而是退化为无法辨认的混沌。《往昔回声》是一个互动装置，试图将这种遗忘的主观现象学可视化。通过在前馈三维重建模型中诱导受控的突触衰退，我们创造了一种艺术类比，用以表现大脑预测性先验的侵蚀。我们将神经网络定位为一种认知代理，而非工程工具——一个硅基大脑，其结构退化唤起了失去对世界掌控时那种迷失、诗意且令人恐惧的体验。最终，我们提供这一框架作为催化剂，邀请更广泛的社群探索神经形态美学在可视化智能脆弱性方面的未知潜力。互动演示见 https://decart-4d.github.io/。

---

