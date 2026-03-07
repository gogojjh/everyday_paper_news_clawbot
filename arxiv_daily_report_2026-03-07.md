# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-03-07 08:05

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 4/20 篇提供

**🌟 Highlight**: 16 篇 | **📌 Poster**: 4 篇

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
- **中文摘要**: 传统安全关键控制方法（如控制屏障函数）存在语义盲区问题，无论障碍物的情境意义如何，其在障碍物周围均表现出相同行为。这一局限导致所有障碍物被统一对待，忽略了其语义差异。本文提出Safe-SAGE（安全交互的社会语义自适应引导）框架，通过拉普拉斯引导场调制的泊松安全函数，构建了高层语义理解与底层安全关键控制之间的桥梁。该框架通过融合多传感器点云、基于视觉的实例分割和持续目标追踪技术，实现对摄像机视场外环境的实时语义感知。基于对环境的语义理解，采用多层安全滤波器调制系统输入以实现安全导航。该安全滤波器包含模型预测控制层和控制屏障函数层，均利用泊松安全函数与引导场的通量调制机制，针对环境中不同障碍物引入差异化保守度策略和多智能体通行规范。本框架使足式机器人能够在语义丰富的动态环境中，根据情境需求保持差异化安全边界，同时确保严格的安全保障。

---

### 2. Observing and Controlling Features in Vision-Language-Action Models

- **作者**: Hugo Buurmeijer, Carmen Amo Alonso, Aiden Swann, Marco Pavone
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.05487v1)
- **发表日期**: 2026-03-05
- **匹配关键词**: VLA, vision-language-action, vision-language-action model
- **arXiv**: [2603.05487v1](http://arxiv.org/abs/2603.05487v1)
- **📥 PDF**: 已下载至本地 (`2603.05487v1_Observing_and_Controlling_Features_in_Vision-Language-Action_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作模型（VLAs）在具身智能领域展现出显著进展。尽管其架构部分借鉴了大语言模型（LLMs），但由于多模态输入/输出特性以及常融合Transformer与扩散头的混合架构，VLAs呈现出更高的复杂性。这也部分解释了为何LLMs机制可解释性研究中揭示的内部表征与输出行为关联的洞见，难以直接迁移至VLA模型。本研究通过引入并分析两个核心概念——特征可观测性与特征可控性，致力于填补这一空白。我们首先探究表征空间中线性编码的特征，并展示如何通过线性分类器实现特征观测；继而基于最优控制理论设计最小线性干预方法，精准定位内部表征并引导VLA输出至目标区域。实验结果表明，这种定向轻量级干预能在保持闭环能力的同时可靠地引导机器人行为。通过对不同VLA架构（$π_{0.5}$与OpenVLA）的仿真实验验证，我们发现VLAs具备可解释的内部结构，支持无需微调的在线自适应，能够实时适应用户偏好与任务需求。

---

### 3. RealWonder: Real-Time Physical Action-Conditioned Video Generation

- **作者**: Wei Liu, Ziyu Chen, Zizhang Li, Yue Wang, Hong-Xing Yu, Jiajun Wu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.05449v1)
- **发表日期**: 2026-03-05
- **匹配关键词**: 3D reconstruction, exploration, 3d reconstruction
- **arXiv**: [2603.05449v1](http://arxiv.org/abs/2603.05449v1)
- **📥 PDF**: 已下载至本地 (`2603.05449v1_RealWonder_Real-Time_Physical_Action-Conditioned_Video_Generation.pdf`)
- **🔓 开源**: CODE, PROJECT_PAGE, MODEL
  - 链接：https://liuwei283.github.io/RealWonder/
- **中文摘要**: 当前视频生成模型无法模拟三维动作（如力与机器人操作）的物理效应，因其缺乏对动作如何影响三维场景的结构化理解。我们提出RealWonder——首个基于单张图像实现动作条件视频生成的实时系统。我们的核心思路是以物理模拟作为中间桥梁：不直接编码连续动作，而是通过物理模拟将其转化为视频模型可处理的视觉表征（光流与RGB）。RealWonder集成三大模块：单图像三维重建、物理模拟，以及仅需4步扩散过程的蒸馏视频生成器。该系统在480×832分辨率下达到13.2帧/秒，支持对刚性物体、可变形体、流体及颗粒材料进行力作用、机器人操作和相机控制的交互式探索。我们预见RealWonder将为视频模型在沉浸式体验、增强/虚拟现实及机器人学习领域的应用开辟新机遇。代码与模型权重已在项目网站开源：https://liuwei283.github.io/RealWonder/

---

### 4. PhysiFlow: Physics-Aware Humanoid Whole-Body VLA via Multi-Brain Latent Flow Matching and Robust Tracking

- **作者**: Weikai Qin, Sichen Wu, Ci Chen, Mengfan Liu, Linxi Feng, Xinru Cui, Haoqi Han, Hesheng Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.05410v1)
- **发表日期**: 2026-03-05
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2603.05410v1](http://arxiv.org/abs/2603.05410v1)
- **📥 PDF**: 已下载至本地 (`2603.05410v1_PhysiFlow_Physics-Aware_Humanoid_Whole-Body_VLA_via_Multi-Brain_Latent_Flow_Matching_and_Robust_Trac.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 在人形机器人控制领域，视觉-语言-动作融合与全身控制的结合对于实现语义引导的现实任务执行至关重要。然而，现有方法在视觉-语言-动作推理效率低下或缺乏对全身控制的有效语义引导方面面临挑战，导致动态肢体协调任务执行不稳定。为弥补这一差距，我们提出了一种语义-运动意图引导、物理感知的多脑视觉-语言-动作框架，用于人形机器人全身控制。通过一系列实验评估了所提框架的性能，实验结果表明该框架能够为人形机器人实现可靠的视觉-语言引导全身协调控制。

---

### 5. Accelerating Sampling-Based Control via Learned Linear Koopman Dynamics

- **作者**: Wenjian Hao, Yuxuan Fang, Zehui Lu, Shaoshuai Mou
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.05385v1)
- **发表日期**: 2026-03-05
- **匹配关键词**: navigation
- **arXiv**: [2603.05385v1](http://arxiv.org/abs/2603.05385v1)
- **📥 PDF**: 已下载至本地 (`2603.05385v1_Accelerating_Sampling-Based_Control_via_Learned_Linear_Koopman_Dynamics.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 本文提出了一种针对复杂非线性动力学系统的高效模型预测路径积分控制框架。为在保持控制性能的同时提升经典MPPI算法的计算效率，我们采用学习得到的线性深度库普曼算子模型替代传统非线性动力学进行轨迹传播，从而实现更快速的轨迹推演与更高效的轨迹采样。深度库普曼动力学模型直接从交互数据中学习获得，无需依赖解析系统模型。我们将所提出的控制器命名为MPPI-DK，通过倒立摆平衡与水面航行器导航任务的仿真实验进行评估，并在四足机器人平台上通过轨迹跟踪实验进行硬件验证。实验结果表明，MPPI-DK在显著降低计算成本的同时，能够达到接近真实动力学模型MPPI的控制性能，为机器人平台实现高效实时控制提供了可行方案。

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
- **中文摘要**: 开放世界导航要求机器人在复杂的日常环境中做出决策，同时适应灵活的任务需求。传统的导航方法通常依赖于密集的三维重建和人工设计的目标度量标准，这限制了其在跨任务和环境中的泛化能力。近年来，视觉-语言导航（VLN）和视觉-语言-动作（VLA）模型的进展使得基于自然语言的端到端策略成为可能，但这些方法通常需要交互式训练、大规模数据收集或通过移动代理进行任务特定的微调。我们将导航问题形式化为稀疏子目标识别与到达问题，并观察到为高层语义先验提供视觉锚定目标能够实现高效的目标条件导航。基于这一洞见，我们选择导航前沿作为语义锚点，并提出OpenFrontier——一个无需训练即可无缝集成多种视觉-语言先验模型的导航框架。OpenFrontier通过轻量级系统设计实现高效导航，无需密集三维建图、策略训练或模型微调。我们在多个导航基准测试中评估OpenFrontier，展示了其强大的零样本性能，以及在移动机器人上的有效实际部署能力。

---

### 7. Critic in the Loop: A Tri-System VLA Framework for Robust Long-Horizon Manipulation

- **作者**: Pengfei Yi, Yingjie Ma, Wenjiang Xu, Yanan Hao, Shuai Gan, Wanting Li, Shanlin Zhong
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.05185v1)
- **发表日期**: 2026-03-05
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2603.05185v1](http://arxiv.org/abs/2603.05185v1)
- **📥 PDF**: 已下载至本地 (`2603.05185v1_Critic_in_the_Loop_A_Tri-System_VLA_Framework_for_Robust_Long-Horizon_Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 在视觉机器人操作领域，如何平衡高层语义推理与低层反应控制仍是核心挑战。视觉语言模型虽擅长认知规划，但其推理延迟阻碍了实时执行；而快速反应的视觉语言动作模型往往缺乏处理复杂长周期任务所需的语义深度。为弥合这一鸿沟，我们提出"闭环评审"框架——一种基于动态视觉语言模型-专家调度的自适应分层系统。该框架采用仿生三重系统架构：以视觉语言模型作为全局推理的"大脑"，视觉语言动作模型作为反应执行的"小脑"，并引入轻量级视觉评审模块。评审模块通过持续监控工作空间动态分配控制权：常规子任务经由视觉语言动作模型实现快速闭环执行，当检测到任务停滞或执行异常时，则自适应触发视觉语言模型进行重规划。此外，该架构无缝集成类人规则，可直观打破无限重试循环。这种基于视觉感知的调度机制在最小化昂贵视觉语言模型调用的同时，显著提升了系统在分布外场景下的鲁棒性与自主性。在具有挑战性的长周期操作基准测试中，综合实验表明我们的方法实现了最先进的性能表现。

---

### 8. Act, Think or Abstain: Complexity-Aware Adaptive Inference for Vision-Language-Action Models

- **作者**: Riccardo Andrea Izzo, Gianluca Bardaro, Matteo Matteucci
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.05147v1)
- **发表日期**: 2026-03-05
- **匹配关键词**: VLA, vision-language-action, vision-language-action model
- **arXiv**: [2603.05147v1](http://arxiv.org/abs/2603.05147v1)
- **📥 PDF**: 已下载至本地 (`2603.05147v1_Act,_Think_or_Abstain_Complexity-Aware_Adaptive_Inference_for_Vision-Language-Action_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 当前关于视觉-语言-动作模型的研究主要集中于通过成熟的推理技术提升泛化能力。这些改进虽然有效，但不可避免地增加了计算复杂度与推理延迟。此外，这些机制通常被不加区分地应用，导致简单任务占用过多资源，同时无法为分布外任务提供必要的置信度评估以避免灾难性失败。受人类认知机制启发，我们提出一种自适应框架，能够根据感知状态的复杂度动态调整VLA执行路径。该方法通过将潜在嵌入映射到参数化与非参数化估计器的集成系统中，将VLA的视觉-语言主干转化为主动检测工具，使系统能够即时执行已知任务，对模糊场景进行推理，并在遇到显著物理或语义异常时主动中止执行。实证分析中，我们观察到因语言语义不变性，仅视觉嵌入在推断任务复杂度方面表现更优。在LIBERO、LIBERO-PRO基准测试及真实机器人实验中，我们的纯视觉配置仅需5%训练数据即可达到80%的F1分数，证明了其作为可靠高效任务复杂度检测器的有效性。

---

### 9. SeedPolicy: Horizon Scaling via Self-Evolving Diffusion Policy for Robot Manipulation

- **作者**: Youqiang Gui, Yuxuan Zhou, Shen Cheng, Xinyang Yuan, Haoqiang Fan, Peng Cheng, Shuaicheng Liu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.05117v1)
- **发表日期**: 2026-03-05
- **匹配关键词**: diffusion policy, vision-language-action, vision-language-action model
- **arXiv**: [2603.05117v1](http://arxiv.org/abs/2603.05117v1)
- **📥 PDF**: 已下载至本地 (`2603.05117v1_SeedPolicy_Horizon_Scaling_via_Self-Evolving_Diffusion_Policy_for_Robot_Manipulation.pdf`)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/Youqiang-Gui/SeedPolicy.
- **中文摘要**: 模仿学习（IL）使机器人能够从专家演示中习得操作技能。扩散策略（DP）能够建模多模态专家行为，但随着观测时长的增加，其性能会下降，限制了长时程操作任务的应用。我们提出自演进门控注意力机制（SEGA），这是一种通过门控注意力保持时间演进潜在状态的时序模块，能够实现高效的循环更新，将长时程观测压缩为固定大小的表征，同时过滤无关的时序信息。将SEGA整合到DP中，我们得到了自演进扩散策略（SeedPolicy），它解决了时序建模的瓶颈，并以适中的开销实现了可扩展的时程延伸。在包含50项操作任务的RoboTwin 2.0基准测试中，SeedPolicy的表现优于DP及其他IL基线方法。在CNN和Transformer两种骨干网络的平均结果中，SeedPolicy在标准设置下相对DP实现了36.8%的性能提升，在随机化挑战设置下实现了169%的相对提升。与拥有12亿参数的视觉-语言-动作模型（如RDT）相比，SeedPolicy以少一至两个数量级的参数量取得了具有竞争力的性能，展现出强大的效率与可扩展性。这些结果表明SeedPolicy已成为长时程机器人操作任务中领先的模仿学习方法。代码发布于：https://github.com/Youqiang-Gui/SeedPolicy。

---

### 10. GaussTwin: Unified Simulation and Correction with Gaussian Splatting for Robotic Digital Twins

- **作者**: Yichen Cai, Paul Jansonnie, Cristiana de Farias, Oleg Arenz, Jan Peters
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.05108v1)
- **发表日期**: 2026-03-05
- **匹配关键词**: gaussian splatting
- **arXiv**: [2603.05108v1](http://arxiv.org/abs/2603.05108v1)
- **📥 PDF**: 已下载至本地 (`2603.05108v1_GaussTwin_Unified_Simulation_and_Correction_with_Gaussian_Splatting_for_Robotic_Digital_Twins.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 数字孪生技术通过维持真实世界感知与仿真之间的持续连接，有望提升机器人操控性能。然而，现有系统大多因缺乏统一模型、复杂的动态交互以及虚实差距等问题而受限，这制约了模型预测控制等下游应用的发展。为此，我们提出GaussTwin——一种实时数字孪生系统，它结合了基于位置的动力学与离散Cosserat杆模型以实现物理基础仿真，并采用高斯泼溅技术进行高效渲染与视觉校正。通过将高斯模型锚定于物理基元，并基于光度误差与分割掩码驱动一致的SE(3)更新，GaussTwin在保持物理真实性的同时实现了稳定的预测-校正机制。通过在仿真环境及Franka Research 3平台上的实验，我们证明相较于形状匹配和纯刚性基线方法，GaussTwin能持续提升跟踪精度与鲁棒性，同时支持基于推力的规划等下游任务。这些成果标志着GaussTwin向构建统一且具有物理意义的数字孪生系统迈出重要一步，该系统有望支持闭环机器人交互与学习。

---

### 11. VinePT-Map: Pole-Trunk Semantic Mapping for Resilient Autonomous Robotics in Vineyards

- **作者**: Giorgio Audrito, Mauro Martini, Alessandro Navone, Giorgia Galluzzo, Marcello Chiaberge
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.05070v1)
- **发表日期**: 2026-03-05
- **匹配关键词**: localization and mapping
- **arXiv**: [2603.05070v1](http://arxiv.org/abs/2603.05070v1)
- **📥 PDF**: 已下载至本地 (`2603.05070v1_VinePT-Map_Pole-Trunk_Semantic_Mapping_for_Resilient_Autonomous_Robotics_in_Vineyards.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 在农业环境中，由于感知混淆、季节性变化以及作物冠层的动态特性，实现自主机器人的长期可靠部署仍面临挑战。葡萄园因其重复的行列结构和物候阶段间显著的视觉变化，成为关键性实地挑战，限制了传统基于特征的定位与建图方法的鲁棒性。本文提出VinePT-Map语义建图框架，该框架利用葡萄树干和支撑杆作为持久性结构地标，实现不受季节影响的稳健机器人定位。所提方法将建图问题构建为因子图，通过利用葡萄园结构的鲁棒几何约束，整合GPS、IMU和RGB-D观测数据。基于实例分割与追踪的高效感知流程，结合用于异常值剔除和位姿优化的聚类滤波器，使得仅需低成本传感器和机载计算即可实现精确地标检测。为验证该流程，我们构建了用于树干与支撑杆分割追踪的多季节数据集。跨季节开展的广泛实地实验证明了所提方法的鲁棒性与精确性，突显了其在农业环境中长期自主运行的适用性。

---

### 12. VPWEM: Non-Markovian Visuomotor Policy with Working and Episodic Memory

- **作者**: Yuheng Lei, Zhixuan Liang, Hongyuan Zhang, Ping Luo
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.04910v1)
- **发表日期**: 2026-03-05
- **匹配关键词**: mobile manipulation, VLA, vision-language-action
- **arXiv**: [2603.04910v1](http://arxiv.org/abs/2603.04910v1)
- **📥 PDF**: 已下载至本地 (`2603.04910v1_VPWEM_Non-Markovian_Visuomotor_Policy_with_Working_and_Episodic_Memory.pdf`)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/HarryLui98/code_vpwem.
- **中文摘要**: 基于人类演示的模仿学习在机器人控制领域已取得显著成功，但大多数视觉运动策略仍依赖于单步观测或短时上下文历史，导致其在需要长期记忆的非马尔可夫任务中表现不佳。单纯扩大上下文窗口会带来巨大的计算与内存开销，并容易引发对虚假相关性的过拟合，从而在分布偏移时产生灾难性故障，同时违背机器人系统的实时性约束。相比之下，人类能够将重要过往经验压缩为长期记忆，并利用这些记忆解决终身任务。本文提出VPWEM——一种配备工作记忆与情景记忆的非马尔可夫视觉运动策略。VPWEM通过滑动窗口保留近期观测标记作为短期工作记忆，并引入基于Transformer的上下文记忆压缩器，递归地将窗口外观测转化为固定数量的情景记忆标记。该压缩器通过对历史摘要标记缓存进行自注意力计算，并结合对历史观测缓存的交叉注意力机制，与策略模型进行联合训练。我们将VPWEM实例化于扩散策略框架，以近乎恒定的单步内存与计算成本，综合利用短期信息与全周期信息生成动作。实验表明，在MIKASA的记忆密集型操作任务中，VPWEM相比包括扩散策略和视觉-语言-动作模型在内的前沿基线方法性能提升超过20%，并在移动操作基准测试MoMaRT上平均提升5%。代码已开源：https://github.com/HarryLui98/code_vpwem。

---

### 13. Task-Relevant and Irrelevant Region-Aware Augmentation for Generalizable Vision-Based Imitation Learning in Agricultural Manipulation

- **作者**: Shun Hattori, Hikaru Sasaki, Takumi Hachimine, Yusuke Mizutani, Takamitsu Matsubara
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.04845v1)
- **发表日期**: 2026-03-05
- **匹配关键词**: diffusion policy
- **arXiv**: [2603.04845v1](http://arxiv.org/abs/2603.04845v1)
- **📥 PDF**: 已下载至本地 (`2603.04845v1_Task-Relevant_and_Irrelevant_Region-Aware_Augmentation_for_Generalizable_Vision-Based_Imitation_Lear.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 基于视觉的模仿学习在机器人操作领域展现出潜力，但其在实际农业任务中的泛化能力仍然有限。这种局限性源于示范数据稀缺以及由以下两方面因素造成的显著视觉域差异：i) 作物特有的外观多样性，ii) 背景环境变化。为突破这一局限，我们提出了面向模仿学习的双区域增强框架，这是一种专为农业操作中可泛化的视觉模仿学习设计的区域感知增强框架。该框架将视觉观察显式分离为任务相关区域与任务无关区域：任务相关区域采用领域知识驱动的方式进行增强以保留关键视觉特征，而任务无关区域则通过主动随机化处理以抑制虚假的背景关联性。通过协同处理这两类视觉变异源，该框架促使学习策略依赖任务本质特征而非偶然性视觉线索。我们通过在人工蔬菜收获和真实生菜缺陷叶片采摘准备任务上的机器人实验，评估了基于扩散策略的视觉运动控制器应用该框架的效果。实验结果表明，相较于基线方法，该框架在未见视觉条件下的任务成功率获得持续提升。进一步的注意力分析和表征泛化度量表明，学习到的策略能更有效地聚焦于任务本质视觉特征，从而实现了更强的鲁棒性与泛化能力。

---

### 14. Diffusion Policy through Conditional Proximal Policy Optimization

- **作者**: Ben Liu, Shunpeng Yang, Hua Chen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.04790v1)
- **发表日期**: 2026-03-05
- **匹配关键词**: diffusion policy
- **arXiv**: [2603.04790v1](http://arxiv.org/abs/2603.04790v1)
- **📥 PDF**: 已下载至本地 (`2603.04790v1_Diffusion_Policy_through_Conditional_Proximal_Policy_Optimization.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 强化学习（RL）已被广泛应用于游戏与机器人等各类决策问题中。近年来，扩散策略在建模多模态行为方面展现出巨大潜力，相比传统高斯策略能够实现更丰富灵活的动作生成。尽管已有多种尝试将强化学习与扩散模型结合，但核心挑战在于难以计算扩散模型下的动作对数似然，这严重阻碍了扩散策略在在线策略强化学习中的直接应用。现有方法大多通过扩散模型的完整去噪过程计算或近似对数似然，存在内存占用大、计算效率低的问题。为突破这一限制，我们提出一种新颖高效的在线策略扩散策略训练方法，该方法仅需评估简单的高斯概率即可实现训练。其关键在于将策略迭代过程与扩散过程进行对齐，这形成了与先前研究截然不同的技术范式。此外，我们的方法框架能够自然地处理熵正则化问题——这一直是扩散策略难以有效融合的要素。实验结果表明，所提方法在IsaacLab和MuJoCo Playground的多种基准任务中，既能生成多模态策略行为，又实现了卓越的性能表现。

---

### 15. RoboMME: Benchmarking and Understanding Memory for Robotic Generalist Policies

- **作者**: Yinpei Dai, Hongze Fu, Jayjun Lee, Yuejiang Liu, Haoran Zhang, Jianing Yang, Chelsea Finn, Nima Fazeli, Joyce Chai ⭐
  - **高亮作者**: Chelsea Finn
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.04639v1)
- **发表日期**: 2026-03-04
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2603.04639v1](http://arxiv.org/abs/2603.04639v1)
- **📥 PDF**: 已下载至本地 (`2603.04639v1_RoboMME_Benchmarking_and_Understanding_Memory_for_Robotic_Generalist_Policies.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 记忆对于长时程且依赖历史信息的机器人操作至关重要。这类任务通常涉及重复动作计数或处理暂时被遮挡的物体。当前视觉-语言-动作模型已开始融入记忆机制，但其评估仍局限于狭窄的非标准化场景，这限制了对模型的系统性理解、横向比较与进展衡量。为应对这些挑战，我们推出RoboMME：一个用于评估和推进视觉-语言-动作模型在长时程历史依赖场景中表现的大规模标准化基准。该基准包含16个操作任务，基于精心设计的分类体系构建，可评估时间记忆、空间记忆、物体记忆与流程记忆。我们进一步开发了14种基于π0.5架构的记忆增强型视觉-语言-动作模型变体，通过多种集成策略系统探索不同记忆表征方式。实验结果表明，记忆表征的有效性高度依赖具体任务，不同设计方案在各任务中展现出独特的优势与局限。演示视频与代码详见项目网站https://robomme.github.io。

---

### 16. SGR3 Model: Scene Graph Retrieval-Reasoning Model in 3D

- **作者**: Zirui Wang, Ruiping Liu, Yufan Chen, Junwei Zheng, Weijia Fan, Kunyu Peng, Di Wen, Jiale Wei, Jiaming Zhang, Rainer Stiefelhagen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.04614v1)
- **发表日期**: 2026-03-04
- **匹配关键词**: 3D reconstruction, scene graph, scene graph generation, semantic scene graph, 3d reconstruction
- **arXiv**: [2603.04614v1](http://arxiv.org/abs/2603.04614v1)
- **📥 PDF**: 已下载至本地 (`2603.04614v1_SGR3_Model_Scene_Graph_Retrieval-Reasoning_Model_in_3D.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 三维场景图通过结构化表示物体实体及其关系，既能为机器人提供高层级的解释与推理能力，又保持对人类直观的可理解性。现有的三维场景图生成方法通常将场景重建与图神经网络相结合，但这类流程需要依赖可能无法始终获取的多模态数据，且其基于启发式图构建的方式可能限制关系三元组的预测。本研究提出三维场景图检索-推理模型，这是一种无需训练的框架，通过结合多模态大语言模型与检索增强生成技术实现语义场景图生成。该模型绕过了显式三维重建的需求，转而通过基于ColPali式跨模态框架检索语义对齐的场景图来增强关系推理能力。为提升检索鲁棒性，我们进一步引入加权区块级相似度选择机制，以减轻模糊或语义信息匮乏区域带来的负面影响。实验表明，该模型在无需训练的基线方法中表现出竞争力，其性能与基于图神经网络的专家模型相当。此外，对检索模块和知识库规模的消融研究表明，检索到的外部信息被显式整合至标记生成过程，而非通过抽象被隐式内化。

---

## 📌 Poster

*其他相关研究*

---

### 1. UltraDexGrasp: Learning Universal Dexterous Grasping for Bimanual Robots with Synthetic Data

- **作者**: Sizhe Yang, Yiman Xie, Zhixuan Liang, Yang Tian, Jia Zeng, Dahua Lin, Jiangmiao Pang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.05312v1)
- **发表日期**: 2026-03-05
- **匹配关键词**: dexterous grasping, grasp synthesis
- **arXiv**: [2603.05312v1](http://arxiv.org/abs/2603.05312v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: GITHUB, CODE
  - 链接：https://github.com/InternRobotics/UltraDexGrasp.
- **中文摘要**: 抓取是机器人与物理世界交互的基础能力。人类凭借双手能够根据物体的形状、尺寸和重量自主选择合适的抓取策略，实现稳健抓取及后续操作。相比之下，当前机器人抓取能力仍存在局限，尤其在多策略场景中。尽管针对平行夹爪和单手机器人的研究已取得显著进展，但面向双手机器人的灵巧抓取技术仍探索不足，其中数据瓶颈是主要制约因素。实现既能承受外部力矩又符合几何约束的物理可信抓取面临重大挑战。为此，我们提出UltraDexGrasp框架——一种面向双手机器人的通用灵巧抓取解决方案。该数据生成流程融合了基于优化的抓取合成与基于规划的示范生成技术，可跨多种抓取策略产出高质量、多样化的轨迹数据。基于此框架，我们构建了UltraDexGrasp-20M大规模多策略抓取数据集，涵盖1000个物体的2000万帧数据。依托该数据集，我们进一步开发了以点云为输入的抓取策略：通过单向注意力机制聚合场景特征，并预测控制指令。该策略仅使用合成数据训练，即可实现稳健的零样本仿真到现实迁移，在面对不同形状、尺寸和重量的新物体时保持稳定性能，在真实世界通用灵巧抓取任务中平均成功率可达81.2%。为促进双手机器人抓取研究的发展，我们已在https://github.com/InternRobotics/UltraDexGrasp开源数据生成流程。

---

### 2. Latent Policy Steering through One-Step Flow Policies

- **作者**: Hokyun Im, Andrey Kolobov, Jianlong Fu, Youngwoon Lee
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.05296v1)
- **发表日期**: 2026-03-05
- **匹配关键词**: exploration
- **arXiv**: [2603.05296v1](http://arxiv.org/abs/2603.05296v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 离线强化学习（RL）使机器人能够从离线数据集中学习，无需进行风险探索。然而，离线强化学习的性能往往取决于一个脆弱的权衡：（1）回报最大化，这可能导致策略偏离数据集支持范围；（2）行为约束，通常需要敏感的超级参数调整。潜在空间引导提供了一种在强化学习过程中保持在数据集支持范围内的结构化方法，但现有的离线适应方法通常通过间接蒸馏学习潜在空间评价器来近似动作价值，这可能导致信息丢失并阻碍收敛。我们提出潜在策略引导（LPS），该方法通过可微分的一步均值流策略将原始动作空间的Q梯度反向传播，以更新潜在动作空间的执行器，从而实现高保真度的潜在策略改进。通过消除代理潜在评价器，LPS允许原始动作空间评价器指导端到端的潜在空间优化，而一步均值流策略则作为行为约束的生成先验。这种解耦产生了一种稳健的方法，无需复杂调整即可直接应用。在OGBench和真实世界机器人任务中，LPS实现了最先进的性能，并始终优于行为克隆和强潜在空间引导基线方法。

---

### 3. Curve-Induced Dynamical Systems on Riemannian Manifolds and Lie Groups

- **作者**: Saray Bakker, Martin Schonger, Tobias Löw, Javier Alonso-Mora, Sylvain Calinon
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.05268v1)
- **发表日期**: 2026-03-05
- **匹配关键词**: mobile manipulator
- **arXiv**: [2603.05268v1](http://arxiv.org/abs/2603.05268v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 在家庭环境中部署机器人需要安全、适应性强且可解释的行为，这些行为需尊重任务的几何结构。这类行为通常用李群和黎曼流形表示，包括SE(3)上的位姿或编码刚度/阻尼矩阵的对称正定矩阵。在此背景下，基于动力系统的方法为生成此类行为提供了自然框架，既能保证稳定性和收敛性，又能对环境变化保持响应。我们提出流形曲线诱导动力系统（CDSM），这是一种直接在黎曼流形和李群上构建动力系统的实时框架。该方法通过在流形上构建标称曲线，生成一个结合切向分量与法向分量的动力系统：切向分量驱动运动沿曲线进行，法向分量则将状态吸引至曲线。我们对所得动力系统进行了稳定性分析，并定量验证了该方法的有效性。在S2基准测试中，CDSM相较于现有先进方法，展现出更高的轨迹精度、更低的路径偏差以及更快的生成与查询速度。最后，我们通过机械臂（在线调整SE(3)位姿和SPD(n)阻尼矩阵）和移动机械臂的实际应用，验证了该框架的实践可行性。

---

### 4. Rethinking the Role of Collaborative Robots in Rehabilitation

- **作者**: Vivek Gupte, Shalutha Rajapakshe, Emmanuel Senft
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.05252v1)
- **发表日期**: 2026-03-05
- **匹配关键词**: HRI, collaborative robot
- **arXiv**: [2603.05252v1](http://arxiv.org/abs/2603.05252v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 当前关于协作机器人在物理康复领域的研究，主要集中于为接受物理治疗的患者提供重复性动作训练，尽管治疗过程中包含多个可能受益于机器人协作与辅助的阶段。与此同时，残障人士与慢性病患者获得物理治疗的机会仍然有限。协作机器人既能支持患者也能辅助治疗师，并有望提升治疗可及性，但其更广泛的应用潜力尚未得到充分探索。我们建议通过设想协作机器人在治疗前、治疗中和治疗后对治疗师及患者的辅助作用，拓展其应用范畴。本文探讨了协作机器人如何通过推动基于能力的治疗方案设计、协助治疗师优化时间与精力分配，从而消除治疗可及性障碍。最后，我们指出了实现这些功能面临的挑战，包括提升用户状态识别能力、确保安全性以及将协作机器人融入治疗师工作流程。这一视角为借鉴人机交互领域在辅助机器人方面的进展开辟了新的研究问题与机遇。

---

