# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-03-08 08:03

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 4/20 篇提供

**🌟 Highlight**: 17 篇 | **📌 Poster**: 3 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. Safe-SAGE: Social-Semantic Adaptive Guidance for Safe Engagement through Laplace-Modulated Poisson Safety Functions

- **作者**: Lizhi Yang, Ryan M. Bena, Meg Wilkinson, Gilbert Bahati, Andy Navarro Brenes, Ryan K. Cosner, Aaron D. Ames
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.05497v1)
- **发表日期**: 2026-03-05
- **匹配关键词**: navigation
- **arXiv**: [2603.05497v1](http://arxiv.org/abs/2603.05497v1)
- **📥 PDF**: 已下载至本地 (`2603.05497v1_Safe-SAGE_Social-Semantic_Adaptive_Guidance_for_Safe_Engagement_through_Laplace-Modulated_Poisson_Sa.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 传统安全关键控制方法（如控制屏障函数）存在语义盲区，无论障碍物的情境意义如何，其避障行为均呈现一致性。这一局限导致所有障碍物被同等对待，忽略了其语义差异。本文提出Safe-SAGE（安全交互的社会语义自适应引导）框架，通过拉普拉斯引导场调制的泊松安全函数，构建了高层语义理解与底层安全关键控制之间的桥梁。该框架通过融合多传感器点云、基于视觉的实例分割及持续目标追踪技术，实现对摄像机视场外动态环境的实时语义感知。基于环境语义理解，采用多层安全滤波器调制系统输入以实现安全导航。该安全滤波器包含模型预测控制层与控制屏障函数层，均利用泊松安全函数与引导场的通量调制机制，针对环境中不同障碍物实施差异化的保守策略与多智能体通行规则。本框架使足式机器人能够在语义丰富的动态环境中，根据情境保持差异化安全边界，同时确保严格的安全保障。

---

### 2. Observing and Controlling Features in Vision-Language-Action Models

- **作者**: Hugo Buurmeijer, Carmen Amo Alonso, Aiden Swann, Marco Pavone
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.05487v1)
- **发表日期**: 2026-03-05
- **匹配关键词**: vision-language-action, VLA, vision-language-action model
- **arXiv**: [2603.05487v1](http://arxiv.org/abs/2603.05487v1)
- **📥 PDF**: 已下载至本地 (`2603.05487v1_Observing_and_Controlling_Features_in_Vision-Language-Action_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作模型（VLAs）在具身智能领域展现出显著进展。尽管其架构部分借鉴了大语言模型（LLMs），但由于多模态输入/输出特性以及常融合Transformer与扩散头的混合架构，VLAs呈现出更高的复杂性。这也部分解释了为何LLMs机制可解释性研究中揭示的内部表征与输出行为关联的洞见，难以直接迁移至VLA模型。本研究通过引入并分析两个核心概念——特征可观测性与特征可控性，致力于填补这一空白。我们首先探究表征空间中线性编码的特征，并展示如何通过线性分类器实现特征观测；随后基于最优控制理论设计最小线性干预方法，精准定位内部表征并引导VLA输出至目标区域。实验结果表明，这种定向轻量级干预能在保持闭环能力的同时可靠引导机器人行为。通过对不同VLA架构（$π_{0.5}$与OpenVLA）的仿真实验验证，我们发现VLAs具备可解释的内部结构，支持无需微调的在线自适应，能够实时适应用户偏好与任务需求。

---

### 3. RealWonder: Real-Time Physical Action-Conditioned Video Generation

- **作者**: Wei Liu, Ziyu Chen, Zizhang Li, Yue Wang, Hong-Xing Yu, Jiajun Wu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.05449v1)
- **发表日期**: 2026-03-05
- **匹配关键词**: 3D reconstruction, 3d reconstruction, exploration
- **arXiv**: [2603.05449v1](http://arxiv.org/abs/2603.05449v1)
- **📥 PDF**: 已下载至本地 (`2603.05449v1_RealWonder_Real-Time_Physical_Action-Conditioned_Video_Generation.pdf`)
- **🔓 开源**: PROJECT_PAGE, MODEL, CODE
  - 链接：https://liuwei283.github.io/RealWonder/
- **中文摘要**: 当前视频生成模型无法模拟三维动作（如力和机器人操作）的物理效应，因为它们缺乏对动作如何影响三维场景的结构性理解。我们提出了RealWonder，这是首个基于单张图像实现动作条件视频生成的实时系统。我们的核心思路是利用物理模拟作为中间桥梁：不直接编码连续动作，而是通过物理模拟将其转化为视频模型可处理的视觉表征（光流与RGB图像）。RealWonder集成三大模块：单图像三维重建、物理模拟，以及仅需4步扩散过程的蒸馏视频生成器。该系统在480×832分辨率下达到13.2帧/秒的实时性能，支持对刚性物体、可变形体、流体及颗粒材料进行力作用、机器人操作和相机控制的交互式探索。我们预见RealWonder将为视频模型在沉浸式体验、增强现实/虚拟现实及机器人学习领域的应用开辟新机遇。代码与模型权重已在项目网站开源：https://liuwei283.github.io/RealWonder/

---

### 4. PhysiFlow: Physics-Aware Humanoid Whole-Body VLA via Multi-Brain Latent Flow Matching and Robust Tracking

- **作者**: Weikai Qin, Sichen Wu, Ci Chen, Mengfan Liu, Linxi Feng, Xinru Cui, Haoqi Han, Hesheng Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.05410v1)
- **发表日期**: 2026-03-05
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2603.05410v1](http://arxiv.org/abs/2603.05410v1)
- **📥 PDF**: 已下载至本地 (`2603.05410v1_PhysiFlow_Physics-Aware_Humanoid_Whole-Body_VLA_via_Multi-Brain_Latent_Flow_Matching_and_Robust_Trac.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 在人形机器人控制领域，视觉-语言-动作融合与全身控制的结合对于实现语义引导的现实任务执行至关重要。然而，现有方法在视觉-语言-动作推理效率低下或缺乏对全身控制的有效语义引导方面面临挑战，导致动态肢体协调任务执行不稳定。为弥补这一差距，我们提出了一种语义-运动意图引导、物理感知的多脑视觉-语言-动作框架，用于人形机器人全身控制。通过一系列实验评估了所提出框架的性能，实验结果表明该框架能够为人形机器人实现可靠的视觉-语言引导全身协调控制。

---

### 5. Accelerating Sampling-Based Control via Learned Linear Koopman Dynamics

- **作者**: Wenjian Hao, Yuxuan Fang, Zehui Lu, Shaoshuai Mou
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.05385v1)
- **发表日期**: 2026-03-05
- **匹配关键词**: navigation
- **arXiv**: [2603.05385v1](http://arxiv.org/abs/2603.05385v1)
- **📥 PDF**: 已下载至本地 (`2603.05385v1_Accelerating_Sampling-Based_Control_via_Learned_Linear_Koopman_Dynamics.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 本文提出了一种针对复杂非线性动力学系统的高效模型预测路径积分控制框架。为在保持控制性能的同时提升经典MPPI算法的计算效率，我们采用学习得到的线性深度库普曼算子模型替代传统非线性动力学进行轨迹传播，从而实现更快速的轨迹推演与更高效的轨迹采样。深度库普曼动力学模型直接从交互数据中学习获得，无需依赖解析系统模型。我们将所提出的控制器命名为MPPI-DK，通过倒立摆平衡与水面航行器导航任务的仿真实验进行评估，并在四足机器人平台上通过轨迹跟踪实验进行硬件验证。实验结果表明，MPPI-DK在显著降低计算成本的同时，能够达到接近真实动力学MPPI的控制性能，为机器人平台实现高效实时控制提供了可行方案。

---

### 6. OpenFrontier: General Navigation with Visual-Language Grounded Frontiers

- **作者**: Esteban Padilla, Boyang Sun, Marc Pollefeys, Hermann Blum ⭐
  - **高亮作者**: Marc Pollefeys
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.05377v1)
- **发表日期**: 2026-03-05
- **匹配关键词**: 3D reconstruction, VLA, navigation, VLN, 3d reconstruction
- **arXiv**: [2603.05377v1](http://arxiv.org/abs/2603.05377v1)
- **📥 PDF**: 已下载至本地 (`2603.05377v1_OpenFrontier_General_Navigation_with_Visual-Language_Grounded_Frontiers.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 开放世界导航要求机器人在复杂的日常环境中做出决策，同时适应灵活的任务需求。传统的导航方法通常依赖于密集的三维重建和手工设计的目标度量，这限制了它们在不同任务和环境间的泛化能力。近年来，视觉-语言导航（VLN）和视觉-语言-动作（VLA）模型的进展使得基于自然语言的条件端到端策略成为可能，但这些方法通常需要交互式训练、大规模数据收集或通过移动代理进行任务特定的微调。我们将导航问题形式化为稀疏子目标识别与到达问题，并观察到为高层语义先验提供视觉锚定目标能够实现高效的目标条件导航。基于这一洞见，我们选择导航前沿作为语义锚点，提出了OpenFrontier——一种无需训练即可无缝集成多种视觉-语言先验模型的导航框架。OpenFrontier通过轻量级系统设计实现高效导航，无需密集三维建图、策略训练或模型微调。我们在多个导航基准测试中评估OpenFrontier，展示了其强大的零样本性能，以及在移动机器人上的有效实际部署能力。

---

### 7. Critic in the Loop: A Tri-System VLA Framework for Robust Long-Horizon Manipulation

- **作者**: Pengfei Yi, Yingjie Ma, Wenjiang Xu, Yanan Hao, Shuai Gan, Wanting Li, Shanlin Zhong
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.05185v1)
- **发表日期**: 2026-03-05
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2603.05185v1](http://arxiv.org/abs/2603.05185v1)
- **📥 PDF**: 已下载至本地 (`2603.05185v1_Critic_in_the_Loop_A_Tri-System_VLA_Framework_for_Robust_Long-Horizon_Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 在视觉机器人操作领域，如何平衡高层语义推理与低层反应控制仍是核心挑战。视觉语言模型虽擅长认知规划，但其推理延迟阻碍了实时执行；而快速反应的视觉语言动作模型往往缺乏处理复杂长周期任务所需的语义深度。为弥合这一鸿沟，我们提出"闭环评审"框架——一种基于动态视觉语言模型-专家调度的自适应分层系统。其核心是仿生三重架构：负责全局推理的视觉语言模型"大脑"、执行反应控制的视觉语言动作"小脑"，以及轻量级视觉"评审器"。评审器通过持续监控工作空间动态分配控制权：常规子任务由视觉语言动作模型维持快速闭环执行；当检测到任务停滞或执行异常时，则自适应触发视觉语言模型进行重规划。该架构还无缝集成类人规则，可直观打破无限重试循环。这种基于视觉感知的调度机制在最小化昂贵视觉语言模型查询的同时，显著提升了系统在分布外场景下的鲁棒性与自主性。在具有挑战性的长周期操作基准测试中，综合实验表明我们的方法实现了最先进的性能表现。

---

### 8. Act, Think or Abstain: Complexity-Aware Adaptive Inference for Vision-Language-Action Models

- **作者**: Riccardo Andrea Izzo, Gianluca Bardaro, Matteo Matteucci
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.05147v1)
- **发表日期**: 2026-03-05
- **匹配关键词**: vision-language-action, VLA, vision-language-action model
- **arXiv**: [2603.05147v1](http://arxiv.org/abs/2603.05147v1)
- **📥 PDF**: 已下载至本地 (`2603.05147v1_Act,_Think_or_Abstain_Complexity-Aware_Adaptive_Inference_for_Vision-Language-Action_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 当前关于视觉-语言-动作（VLA）模型的研究主要集中于通过成熟的推理技术提升泛化能力。尽管这些方法有效，但其改进不可避免地增加了计算复杂度和推理延迟。此外，这些机制通常被不加区分地应用，导致在简单任务上资源分配效率低下，同时无法提供必要的置信度估计以防止在分布外任务上出现灾难性失败。受人类认知机制启发，我们提出一种自适应框架，能够根据感知状态的复杂度动态路由VLA执行流程。该方法通过将潜在嵌入投影到参数化与非参数化估计器的集成空间中，将VLA的视觉-语言主干转化为主动检测工具。这使得系统能够立即执行已知任务（执行），对模糊场景进行推理（思考），并在遇到显著物理或语义异常时主动中止执行（弃权）。在实证分析中，我们观察到因语言语义不变性，仅使用视觉嵌入在推断任务复杂度方面表现更优。通过在LIBERO和LIBERO-PRO基准测试及真实机器人上的评估，我们的纯视觉配置仅需5%的训练数据即可达到80%的F1分数，证明了其作为可靠高效任务复杂度检测器的性能。

---

### 9. SeedPolicy: Horizon Scaling via Self-Evolving Diffusion Policy for Robot Manipulation

- **作者**: Youqiang Gui, Yuxuan Zhou, Shen Cheng, Xinyang Yuan, Haoqiang Fan, Peng Cheng, Shuaicheng Liu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.05117v1)
- **发表日期**: 2026-03-05
- **匹配关键词**: vision-language-action, diffusion policy, vision-language-action model
- **arXiv**: [2603.05117v1](http://arxiv.org/abs/2603.05117v1)
- **📥 PDF**: 已下载至本地 (`2603.05117v1_SeedPolicy_Horizon_Scaling_via_Self-Evolving_Diffusion_Policy_for_Robot_Manipulation.pdf`)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/Youqiang-Gui/SeedPolicy.
- **中文摘要**: 模仿学习（IL）使机器人能够通过专家演示掌握操作技能。扩散策略（DP）能够建模多模态专家行为，但随着观测时域的延长，其性能会下降，从而限制了长时域操作任务的应用。本文提出自演化门控注意力（SEGA）时序模块，该模块通过门控注意力机制维护随时间演化的潜在状态，实现高效的循环更新，将长时域观测压缩为固定大小的表征，同时过滤无关的时序信息。将SEGA集成到DP中，形成了自演化扩散策略（SeedPolicy），该方法解决了时序建模瓶颈，实现了以适度开销扩展时域的可扩展性。在包含50项操作任务的RoboTwin 2.0基准测试中，SeedPolicy的表现优于DP及其他IL基线方法。在CNN和Transformer两种骨干网络架构下，SeedPolicy在标准设置中相对DP实现了36.8%的性能提升，在随机化挑战设置中相对提升达到169%。与拥有12亿参数的视觉-语言-动作模型（如RDT）相比，SeedPolicy仅用其百分之一到十分之一的参数量即达到相当的性能水平，展现出卓越的效率和可扩展性。这些成果确立了SeedPolicy作为长时域机器人操作任务中领先的模仿学习方法。代码已开源：https://github.com/Youqiang-Gui/SeedPolicy。

---

### 10. GaussTwin: Unified Simulation and Correction with Gaussian Splatting for Robotic Digital Twins

- **作者**: Yichen Cai, Paul Jansonnie, Cristiana de Farias, Oleg Arenz, Jan Peters
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.05108v1)
- **发表日期**: 2026-03-05
- **匹配关键词**: gaussian splatting
- **arXiv**: [2603.05108v1](http://arxiv.org/abs/2603.05108v1)
- **📥 PDF**: 已下载至本地 (`2603.05108v1_GaussTwin_Unified_Simulation_and_Correction_with_Gaussian_Splatting_for_Robotic_Digital_Twins.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 数字孪生技术通过维持现实世界感知与仿真之间的持续连接，有望提升机器人操控能力。然而，现有系统大多面临统一模型缺失、复杂动态交互困难以及虚实差距等挑战，限制了模型预测控制等下游应用的发展。为此，我们提出GaussTwin——一种实时数字孪生系统，它结合基于位置的动力学与离散Cosserat杆模型实现物理基础仿真，并采用高斯泼溅技术进行高效渲染与视觉校正。通过将高斯模型锚定于物理基元，并基于光度误差与分割掩码驱动一致的SE(3)更新，GaussTwin在保持物理保真度的同时实现了稳定的预测-校正机制。通过在仿真环境及Franka Research 3平台上的实验，我们证明相较于形状匹配与纯刚性基线方法，GaussTwin能持续提升跟踪精度与鲁棒性，同时支持基于推力的规划等下游任务。这些成果标志着GaussTwin向构建统一且具有物理意义的数字孪生系统迈出重要一步，为闭环机器人交互与学习提供了有力支撑。

---

### 11. VinePT-Map: Pole-Trunk Semantic Mapping for Resilient Autonomous Robotics in Vineyards

- **作者**: Giorgio Audrito, Mauro Martini, Alessandro Navone, Giorgia Galluzzo, Marcello Chiaberge
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.05070v1)
- **发表日期**: 2026-03-05
- **匹配关键词**: localization and mapping
- **arXiv**: [2603.05070v1](http://arxiv.org/abs/2603.05070v1)
- **📥 PDF**: 已下载至本地 (`2603.05070v1_VinePT-Map_Pole-Trunk_Semantic_Mapping_for_Resilient_Autonomous_Robotics_in_Vineyards.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 在农业环境中，由于感知混淆、季节性变化以及作物冠层的动态特性，实现自主机器人的长期可靠部署仍具挑战。葡萄园因其重复的行列结构和物候阶段显著的视觉变化，成为关键领域难题，限制了传统基于特征的定位与建图方法的鲁棒性。本文提出VinePT-Map语义建图框架，该框架利用葡萄树干和支撑杆作为持久结构地标，实现不受季节影响的稳健机器人定位。所提方法将建图问题建模为因子图，通过利用葡萄园结构的鲁棒几何约束，整合GPS、IMU和RGB-D观测数据。基于实例分割与追踪的高效感知流程，结合用于异常值剔除和位姿优化的聚类滤波器，使得使用低成本传感器和机载计算实现精确地标检测成为可能。为验证该流程，我们提出了用于树干与支撑杆分割追踪的多季节数据集。跨季节开展的广泛实地实验证明了所提方法的鲁棒性与精确性，突显了其在农业环境中长期自主运行的适用性。

---

### 12. VPWEM: Non-Markovian Visuomotor Policy with Working and Episodic Memory

- **作者**: Yuheng Lei, Zhixuan Liang, Hongyuan Zhang, Ping Luo
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.04910v1)
- **发表日期**: 2026-03-05
- **匹配关键词**: vision-language-action, VLA, mobile manipulation
- **arXiv**: [2603.04910v1](http://arxiv.org/abs/2603.04910v1)
- **📥 PDF**: 已下载至本地 (`2603.04910v1_VPWEM_Non-Markovian_Visuomotor_Policy_with_Working_and_Episodic_Memory.pdf`)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/HarryLui98/code_vpwem.
- **中文摘要**: 基于人类演示的模仿学习在机器人控制领域已取得显著成功，但大多数视觉运动策略仍依赖于单步观测或短上下文历史，导致其在需要长期记忆的非马尔可夫任务中表现不佳。单纯扩大上下文窗口会带来巨大的计算与内存开销，并容易导致对虚假关联的过拟合，从而在分布偏移时引发灾难性故障，同时违反机器人系统的实时性约束。相比之下，人类能够将重要过往经验压缩为长期记忆，并利用这些记忆解决终身任务。本文提出VPWEM——一种配备工作记忆与情景记忆的非马尔可夫视觉运动策略。VPWEM将近期观测标记保留为滑动窗口形式的短期工作记忆，同时引入基于Transformer的上下文记忆压缩器，递归地将窗口外观测转换为固定数量的情景记忆标记。该压缩器通过对历史摘要标记缓存进行自注意力计算，并结合对历史观测缓存的交叉注意力机制，与策略进行联合训练。我们将VPWEM实例化于扩散策略中，以利用短期及全周期信息生成动作，同时保持每步近乎恒定的内存与计算开销。实验表明，在MIKASA的记忆密集型操作任务中，VPWEM比包括扩散策略和视觉-语言-动作模型在内的先进基线方法性能提升超过20%，并在移动操作基准测试MoMaRT上平均提升5%。代码发布于https://github.com/HarryLui98/code_vpwem。

---

### 13. Task-Relevant and Irrelevant Region-Aware Augmentation for Generalizable Vision-Based Imitation Learning in Agricultural Manipulation

- **作者**: Shun Hattori, Hikaru Sasaki, Takumi Hachimine, Yusuke Mizutani, Takamitsu Matsubara
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.04845v1)
- **发表日期**: 2026-03-05
- **匹配关键词**: diffusion policy
- **arXiv**: [2603.04845v1](http://arxiv.org/abs/2603.04845v1)
- **📥 PDF**: 已下载至本地 (`2603.04845v1_Task-Relevant_and_Irrelevant_Region-Aware_Augmentation_for_Generalizable_Vision-Based_Imitation_Lear.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 基于视觉的模仿学习在机器人操作领域展现出潜力，但其在实际农业任务中的泛化能力仍然有限。这种局限性源于示范数据稀缺以及由以下两方面因素造成的显著视觉域差异：i) 作物特有的外观多样性，ii) 背景环境变化。为突破这一局限，我们提出面向模仿学习的双区域增强框架，这是一种专为农业操作中可泛化的视觉模仿学习设计的区域感知增强框架。该框架将视觉观察显式分离为任务相关区域与任务无关区域：任务相关区域采用领域知识驱动的方式进行增强以保留关键视觉特征，而任务无关区域则通过主动随机化处理来抑制虚假背景关联。通过协同处理这两类视觉变异源，该框架推动学习策略依赖任务本质特征而非偶然性视觉线索。我们通过在人工蔬菜收获和真实生菜缺陷叶片采摘准备任务上的机器人实验，评估了基于扩散策略的视觉运动控制器应用该框架的效果。结果显示，相较于基线方法，该框架在未见视觉条件下的成功率获得持续提升。进一步的注意力分析和表征泛化度量表明，学习到的策略更依赖于任务本质视觉特征，从而实现了更强的鲁棒性与泛化能力。

---

### 14. Diffusion Policy through Conditional Proximal Policy Optimization

- **作者**: Ben Liu, Shunpeng Yang, Hua Chen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.04790v1)
- **发表日期**: 2026-03-05
- **匹配关键词**: diffusion policy
- **arXiv**: [2603.04790v1](http://arxiv.org/abs/2603.04790v1)
- **📥 PDF**: 已下载至本地 (`2603.04790v1_Diffusion_Policy_through_Conditional_Proximal_Policy_Optimization.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 强化学习（RL）已被广泛应用于游戏和机器人等多种决策问题中。近年来，扩散策略在建模多模态行为方面展现出巨大潜力，相比传统的高斯策略，能够生成更多样化和灵活的动作。尽管已有多种尝试将强化学习与扩散模型结合，但一个关键挑战在于难以计算扩散模型下的动作对数似然。这极大地阻碍了扩散策略在在线策略强化学习中的直接应用。现有方法大多通过扩散模型中的完整去噪过程来计算或近似对数似然，这在内存和计算上效率较低。为克服这一挑战，我们提出了一种新颖且高效的方法，用于在在线策略设置中训练扩散策略，该方法仅需评估简单的高斯概率。这是通过将策略迭代与扩散过程对齐实现的，与先前工作相比，这是一种独特的范式。此外，我们的公式能够自然地处理熵正则化，而这通常是扩散策略难以融入的。实验表明，所提出的方法能够产生多模态策略行为，并在IsaacLab和MuJoCo Playground的多种基准任务中取得了优越的性能。

---

### 15. FaceCam: Portrait Video Camera Control via Scale-Aware Conditioning

- **作者**: Weijie Lyu, Ming-Hsuan Yang, Zhixin Shu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.05506v1)
- **发表日期**: 2026-03-05
- **匹配关键词**: 3D reconstruction, 3d reconstruction
- **arXiv**: [2603.05506v1](http://arxiv.org/abs/2603.05506v1)
- **📥 PDF**: 已下载至本地 (`2603.05506v1_FaceCam_Portrait_Video_Camera_Control_via_Scale-Aware_Conditioning.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 我们推出FaceCam系统，该系统能够为单目人像视频输入生成可定制相机轨迹的视频。当前基于大型视频生成模型的相机控制方法虽已取得显著进展，但在人像视频中常因尺度模糊的相机表征或三维重建误差而产生几何畸变与视觉伪影。为突破这些局限，我们提出一种面向人脸的尺度感知相机变换表征方法，该方案无需依赖三维先验知识即可提供确定性条件约束。我们利用多视角工作室采集数据与真实场景单目视频训练视频生成模型，并引入两种相机控制数据生成策略：合成相机运动与多镜头拼接技术，从而在利用静态训练相机数据的同时，实现推理阶段对动态连续相机轨迹的泛化能力。在Ava-256数据集及多样化真实场景视频上的实验表明，FaceCam在相机可控性、视觉质量、身份特征与运动保持方面均展现出卓越性能。

---

### 16. Towards 3D Scene Understanding of Gas Plumes in LWIR Hyperspectral Images Using Neural Radiance Fields

- **作者**: Scout Jarman, Zigfried Hampel-Arias, Adra Carr, Kevin R. Moon
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.05473v1)
- **发表日期**: 2026-03-05
- **匹配关键词**: nerf, neural radiance field
- **arXiv**: [2603.05473v1](http://arxiv.org/abs/2603.05473v1)
- **📥 PDF**: 已下载至本地 (`2603.05473v1_Towards_3D_Scene_Understanding_of_Gas_Plumes_in_LWIR_Hyperspectral_Images_Using_Neural_Radiance_Fiel.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 高光谱图像（HSI）在环境监测到国家安全等多个领域具有广泛应用，可用于材料检测与识别。长波红外（LWIR）高光谱图像特别适用于气体羽流检测与分析。在实际应用中，通常只能获取目标场景的少量图像并进行独立分析。若能将多幅图像信息融合为统一连贯的表征，通过提供更丰富的场景几何结构与光谱特性背景，有望显著提升分析效能。神经辐射场（NeRF）技术通过构建场景体属性的潜在神经表征，实现了新颖视角渲染与几何重建，为高光谱三维场景重建提供了创新路径。本研究探索利用NeRF技术从长波红外高光谱图像构建三维场景重建的可能性，并验证该模型可应用于气体羽流检测的基础下游分析任务。基于物理机理的DIRSIG软件套件被用于生成包含强六氟化硫气体羽流的简易设施合成多视角长波红外高光谱数据集。本研究方法基于标准Mip-NeRF架构，融合了高光谱NeRF与稀疏视角NeRF的前沿技术，并引入新型自适应加权均方误差损失函数。最终构建的NeRF方法相比标准Mip-NeRF减少约50%训练图像需求，仅用30张训练图像即可实现39.8 dB的平均峰值信噪比。通过自适应相干估计器对NeRF渲染测试图像进行气体羽流检测，与真实测试图像生成的检测掩模相比，平均曲线下面积达到0.821。

---

### 17. SSR-GS: Separating Specular Reflection in Gaussian Splatting for Glossy Surface Reconstruction

- **作者**: Ningjing Fan, Yiqun Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.05152v1)
- **发表日期**: 2026-03-05
- **匹配关键词**: 3D gaussian splatting, gaussian splatting
- **arXiv**: [2603.05152v1](http://arxiv.org/abs/2603.05152v1)
- **📥 PDF**: 已下载至本地 (`2603.05152v1_SSR-GS_Separating_Specular_Reflection_in_Gaussian_Splatting_for_Glossy_Surface_Reconstruction.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 近年来，三维高斯溅射（3DGS）在新视角合成领域取得了显著进展。然而，在复杂光照条件下精确重建光泽表面仍具挑战性，特别是在存在强镜面反射和多表面相互反射的场景中。为解决这一问题，我们提出SSR-GS——一种面向光泽表面重建的镜面反射建模框架。具体而言，我们引入预滤波Mip-Cubemap来高效建模直接镜面反射，并提出IndiASG模块以捕捉间接镜面反射。

此外，我们设计了视觉几何先验（VGP），通过反射分数（RS）耦合反射感知的视觉先验，以降低反射主导区域对光度损失的贡献权重，同时结合源自VGGT的几何先验，包括渐进衰减深度监督与变换法向约束。在合成数据集和真实场景数据集上的大量实验表明，SSR-GS在光泽表面重建任务中达到了最先进的性能水平。

---

## 📌 Poster

*其他相关研究*

---

### 1. UltraDexGrasp: Learning Universal Dexterous Grasping for Bimanual Robots with Synthetic Data

- **作者**: Sizhe Yang, Yiman Xie, Zhixuan Liang, Yang Tian, Jia Zeng, Dahua Lin, Jiangmiao Pang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.05312v1)
- **发表日期**: 2026-03-05
- **匹配关键词**: grasp synthesis, dexterous grasping
- **arXiv**: [2603.05312v1](http://arxiv.org/abs/2603.05312v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: GITHUB, CODE
  - 链接：https://github.com/InternRobotics/UltraDexGrasp.
- **中文摘要**: 抓取是机器人与物理世界交互的基础能力。人类凭借双手能够根据物体的形状、尺寸和重量自主选择合适的抓取策略，实现稳健抓取及后续操作。相比之下，当前机器人抓取能力仍存在局限，尤其在多策略场景中。尽管针对平行夹爪和单手机器人的研究已取得显著进展，但面向双手机器人的灵巧抓取仍探索不足，其中数据是主要瓶颈。实现既能承受外部力矩又符合几何约束的物理可信抓取面临重大挑战。为解决这些问题，我们提出了UltraDexGrasp框架——一种面向双手机器人的通用灵巧抓取系统。该数据生成流程将基于优化的抓取合成与基于规划的示范生成相结合，在多种抓取策略中产生高质量、多样化的轨迹。基于此框架，我们构建了UltraDexGrasp-20M数据集，这是一个包含1000个物体、2000万帧数据的大规模多策略抓取数据集。依托该数据集，我们进一步开发了简洁高效的抓取策略：以点云为输入，通过单向注意力机制聚合场景特征，并预测控制指令。该策略仅通过合成数据训练，即可实现稳健的零样本仿真到现实迁移，在面对不同形状、尺寸和重量的新物体时保持稳定性能，在真实世界通用灵巧抓取任务中平均成功率可达81.2%。为促进双手机器人抓取研究的发展，我们在https://github.com/InternRobotics/UltraDexGrasp开源了数据生成流程。

---

### 2. Latent Policy Steering through One-Step Flow Policies

- **作者**: Hokyun Im, Andrey Kolobov, Jianlong Fu, Youngwoon Lee
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.05296v1)
- **发表日期**: 2026-03-05
- **匹配关键词**: exploration
- **arXiv**: [2603.05296v1](http://arxiv.org/abs/2603.05296v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 离线强化学习（RL）使机器人能够从离线数据集中学习，无需进行风险探索。然而，离线RL的性能往往取决于（1）回报最大化（可能导致策略偏离数据集支持范围）与（2）行为约束（通常需要精细的超参数调优）之间脆弱的权衡关系。潜在空间引导为RL训练期间保持在数据集支持范围内提供了结构化方法，但现有离线改进方案通常通过间接蒸馏学习潜在空间评价器来近似动作价值，这可能导致信息丢失并阻碍收敛。我们提出潜在策略引导（LPS）方法，通过可微分单步均值流策略将原始动作空间的Q梯度反向传播至潜在动作空间执行器，实现高保真度的潜在策略改进。通过消除代理潜在评价器，LPS允许原始动作空间评价器指导端到端的潜在空间优化，同时单步均值流策略作为行为约束的生成先验。这种解耦设计产生了鲁棒性强的方法，仅需极少调参即可直接应用。在OGBench基准测试和真实机器人任务中，LPS均取得最先进的性能表现，持续超越行为克隆及现有潜在空间引导基线方法。

---

### 3. Curve-Induced Dynamical Systems on Riemannian Manifolds and Lie Groups

- **作者**: Saray Bakker, Martin Schonger, Tobias Löw, Javier Alonso-Mora, Sylvain Calinon
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.05268v1)
- **发表日期**: 2026-03-05
- **匹配关键词**: mobile manipulator
- **arXiv**: [2603.05268v1](http://arxiv.org/abs/2603.05268v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 在家庭环境中部署机器人需要安全、适应性强且可解释的行为，这些行为需尊重任务的几何结构。这类行为通常用李群和黎曼流形表示，包括SE(3)上的位姿或编码刚度/阻尼矩阵的对称正定矩阵。在此背景下，基于动力系统的方法为生成此类行为提供了自然框架，既能保证稳定性和收敛性，又能对环境变化保持响应。我们提出光滑流形上的曲线诱导动力系统（CDSM），这是一个直接在黎曼流形和李群上构建动力系统的实时框架。该方法通过在流形上构建标称曲线，生成一个结合切向分量与法向分量的动力系统：切向分量驱动状态沿曲线运动，法向分量则将状态吸引至曲线。我们对所得动力系统进行了稳定性分析，并定量验证了该方法的有效性。在S2基准测试中，CDSM相较于现有先进方法，展现出更高的轨迹精度、更低的路径偏差以及更快的生成与查询速度。最后，我们通过机械臂（在线调整SE(3)位姿和SPD(n)阻尼矩阵）和移动机械臂的实际应用，验证了该框架的实践可行性。

---

