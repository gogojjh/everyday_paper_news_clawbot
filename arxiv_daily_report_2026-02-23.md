# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-02-23 10:20

**今日新增**: 15 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 3/15 篇提供

**🌟 Highlight**: 3 篇 | **📌 Poster**: 12 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图*

---

### 1. CapNav: Benchmarking Vision Language Models on Capability-conditioned Indoor Navigation

- **作者**: Xia Su, Ruiqi Chen, Benlin Liu, Jingwei Ma, Zonglin Di, Ranjay Krishna, Jon Froehlich
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.18424v1)
- **发表日期**: 2026-02-20
- **匹配关键词**: VLN, navigation
- **arXiv**: [2602.18424v1](http://arxiv.org/abs/2602.18424v1)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/makeabilitylab/CapNav
- **中文摘要**: 视觉语言模型在视觉语言导航领域展现出显著进展，为导航决策开辟了新可能，有望同时惠及机器人平台与人类用户。然而现实世界的导航行为本质上受限于智能体的移动能力约束。例如扫地机器人无法跨越楼梯，而四足机器人则可以。我们提出能力条件导航基准，旨在评估视觉语言模型在给定智能体特定物理与操作能力的前提下，如何在复杂室内空间进行导航。该基准定义了五个具有代表性的人类与机器人智能体，每个智能体均通过物理尺寸、移动能力和环境交互能力进行描述。基准包含45个真实室内场景、473项导航任务及2365组问答对，用于测试视觉语言模型能否基于智能体能力在室内环境中穿行。通过对13个现代视觉语言模型的评估，我们发现当前模型的导航性能随移动约束收紧而急剧下降，即使是前沿模型在面对需要空间维度推理的障碍类型时也表现不佳。最后我们探讨了能力感知导航的意义，以及在未来视觉语言模型中推进具身空间推理的机遇。该基准可通过https://github.com/makeabilitylab/CapNav获取。

---

### 2. Role-Adaptive Collaborative Formation Planning for Team of Quadruped Robots in Cluttered Environments

- **作者**: Magnus Norén, Marios-Nektarios Stamatopoulos, Avijit Banerjee, George Nikolakopoulos
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.18260v1)
- **发表日期**: 2026-02-20
- **匹配关键词**: obstacle avoidance, navigation
- **arXiv**: [2602.18260v1](http://arxiv.org/abs/2602.18260v1)
- **🔒 开源**: 未提及
- **中文摘要**: 本文提出了一种基于角色自适应领导者-跟随者的四足机器人编队规划与控制框架，适用于在杂乱环境中运行的机器人团队。与传统固定领导者或刚性编队角色的方法不同，所提出的方法整合了动态角色分配与局部目标规划，实现了在复杂场景中灵活、无碰撞的导航。通过虚拟弹簧阻尼系统与新型避障层相结合，确保了编队稳定性和机器人间的安全性，该避障层能够自适应调整每个智能体的速度。动态前瞻参考生成器进一步增强了灵活性，允许编队临时变形以绕过障碍物，同时保持目标导向运动。快速行进平方（FM2）算法作为规划核心，为领导者提供全局路径，为跟随者提供局部路径。该框架通过大量仿真和四足机器人团队的实际实验进行了验证。结果表明，在复杂、非结构化环境中，系统能够实现平滑协调、自适应角色切换和稳健的编队保持。包含仿真与物理实验及其相关可视化的视频可在 https://youtu.be/scq37Tua9W4 查看。

---

### 3. GrandTour: A Legged Robotics Dataset in the Wild for Multi-Modal Perception and State Estimation

- **作者**: Jonas Frey, Turcan Tuna, Frank Fu, Katharine Patterson, Tianao Xu, Maurice Fallon, Cesar Cadena, Marco Hutter
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.18164v1)
- **发表日期**: 2026-02-20
- **匹配关键词**: navigation
- **arXiv**: [2602.18164v1](http://arxiv.org/abs/2602.18164v1)
- **🔓 开源**: HUGGINGFACE
- **中文摘要**: 精确的状态估计与多模态感知是足式机器人在复杂大规模环境中实现自主运行的前提。目前，尚未有大规模公开的足式机器人数据集能够满足开发与评估足式机器人状态估计、感知及导航算法所需的真实世界条件。为此，我们推出GrandTour数据集——一个在多模态足式机器人领域具有里程碑意义的数据集，采集自具有挑战性的户外与室内环境。该数据集以搭载\boxi多模态传感器负载的ANYbotics ANYmal-D四足机器人为平台，覆盖从高山景观、森林到拆除建筑及城市区域等多种测试场地，涵盖不同规模、复杂度、光照及天气条件的广泛变化。数据集提供时间同步的传感器数据，包括旋转激光雷达、多台特性互补的RGB相机、本体感知传感器以及立体深度相机。此外，还包含基于卫星的RTK-GNSS和徕卡测量系统全站仪提供的高精度真值轨迹。本数据集支持SLAM、高精度状态估计及多模态学习等领域的研究，为足式机器人系统中的传感器融合方法提供了严格的评估与开发基础。凭借其广泛覆盖范围，GrandTour成为迄今规模最大的开源足式机器人数据集。数据集可通过https://grand-tour.leggedrobotics.com获取，提供HuggingFace平台（独立于ROS）及ROS格式版本，并附有工具与演示资源。

---

## 📌 Poster

*其他相关研究*

---

### 1. Zero-shot Interactive Perception

- **作者**: Venkatesh Sripada, Frank Guerin, Amir Ghalamzan
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.18374v1)
- **发表日期**: 2026-02-20
- **匹配关键词**: interactive perception, affordance
- **arXiv**: [2602.18374v1](http://arxiv.org/abs/2602.18374v1)
- **🔒 开源**: 未提及
- **中文摘要**: 交互式感知（IP）使机器人能够通过物理交互改变环境状态，从而提取工作空间中隐藏的信息并执行操作规划——这对于解决复杂、部分可观测场景中的遮挡和模糊性问题至关重要。我们提出零样本交互式感知（ZS-IP）框架，该框架将多策略操作（推动与抓取）与记忆驱动的视觉语言模型（VLM）相结合，以指导机器人交互并解决语义查询。ZS-IP包含三个核心组件：（1）增强观察模块，通过传统关键点与我们提出的"推进行"（一种专为推动动作设计的新型二维视觉增强方法）共同提升VLM的视觉感知能力；（2）记忆引导行动模块，通过上下文检索强化语义推理；（3）机器人控制器，根据VLM输出执行推动、拉动或抓取动作。与针对抓放任务优化的网格增强方法不同，"推进行"能够捕捉密集接触动作的功能特性，显著提升推动任务性能。我们在7自由度Franka Panda机械臂上，针对不同遮挡程度和任务复杂度的多样化场景评估ZS-IP。实验表明，ZS-IP在推动任务中显著优于基于标记的视觉提示（MOKA）等被动及视点感知技术，同时能保持非目标元素的完整性。

---

### 2. MUOT_3M: A 3 Million Frame Multimodal Underwater Benchmark and the MUTrack Tracking Method

- **作者**: Ahsan Baidar Bakht, Mohamad Alansari, Muhayy Ud Din, Muzammal Naseer, Sajid Javed, Irfan Hussain, Jiri Matas, Arif Mahmood
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.18006v1)
- **发表日期**: 2026-02-20
- **匹配关键词**: exploration
- **arXiv**: [2602.18006v1](http://arxiv.org/abs/2602.18006v1)
- **🔒 开源**: 未提及
- **中文摘要**: 水下目标跟踪技术对高效海洋机器人作业、大规模生态监测及海洋探索至关重要，但其发展长期受限于大规模、多模态、多样化数据集的匮乏。现有基准数据集规模较小且仅含RGB模态，在严重色偏、浑浊水体及低能见度条件下的鲁棒性受限。本研究提出首个伪多模态水下跟踪基准数据集MUOT_3M，包含来自3,030段视频（总时长27.8小时）的300万帧图像，标注涵盖32项跟踪属性、677个细粒度类别，并同步提供经海洋生物学家验证的RGB模态、增强RGB估计模态、深度估计模态及语言模态。基于该数据集，我们提出基于SAM架构的多模态转单模态跟踪器MUTrack，其具备视觉几何对齐、视觉语言融合及四级知识蒸馏机制，可将多模态知识迁移至单模态学生模型。在五个水下跟踪基准上的广泛实验表明，MUTrack相比现有最强基线方法在AUC指标上最高提升8.40%，精确度最高提升7.80%，同时保持24帧/秒的实时运行速度。MUOT_3M数据集与MUTrack模型为可扩展、多模态训练且具备实际部署价值的水下跟踪研究奠定了新基础。

---

### 3. Latent Diffeomorphic Co-Design of End-Effectors for Deformable and Fragile Object Manipulation

- **作者**: Kei Ikemura, Yifei Dong, Florian T. Pokorny
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.17921v1)
- **发表日期**: 2026-02-20
- **匹配关键词**: object manipulation
- **arXiv**: [2602.17921v1](http://arxiv.org/abs/2602.17921v1)
- **🔒 开源**: 未提及
- **中文摘要**: 由于复杂的接触动力学及对物体完整性的严格要求，操纵可变形与易碎物体始终是机器人学领域的核心挑战。现有方法通常孤立地优化末端执行器设计或控制策略，限制了性能的进一步提升。本研究首次提出一种协同设计框架，针对可变形与易碎物体的操控任务，联合优化末端执行器形态与操控策略。我们创新性地引入：（1）基于隐空间微分同胚的形状参数化方法，实现高表现力且可处理的末端执行器几何优化；（2）融合形态学与控制优化的应力感知双层协同设计流程；（3）面向零样本现实场景部署的“特权信息-点云”策略蒸馏方案。通过在抓取果冻、推动果冻及舀取鱼片等高难度食品操控任务上的验证，仿真与实物实验均证明了该方法的有效性。

---

### 4. Convex Block-Cholesky Approach to Risk-Constrained Low-thrust Trajectory Design under Operational Uncertainty

- **作者**: Kenshiro Oguri, Gregory Lantoine
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.18416v1)
- **发表日期**: 2026-02-20
- **匹配关键词**: navigation, exploration
- **arXiv**: [2602.18416v1](http://arxiv.org/abs/2602.18416v1)
- **🔒 开源**: 未提及
- **中文摘要**: 设计在不确定性条件下的鲁棒轨迹是一项新兴技术，可能代表着空间任务设计领域的关键范式转变。随着我们追求更具雄心的科学目标（例如多卫星巡游任务、具有高度自主组件的任务），在任务设计中充分考虑导航过程变得愈发重要。导航过程本质上具有统计特性，包括轨道确定和飞行路径控制两个环节。因此，这种任务设计范式需要采用能够恰当量化导航统计效应、评估相关风险的技术，并设计出既能确保足够低风险又能优化统计性能指标的任务方案；常用的指标是Delta-V99：包含统计性飞行路径控制的最坏情况（99%分位数）速度增量消耗。

为应对这一需求，本文针对由初始状态散布、导航误差、机动执行误差及动力学建模不完善等操作不确定性因素，开发了一种风险约束下的轨迹优化算法。我们将该问题构建为非线性随机最优控制问题，并提出一种结合最优协方差导向与序列凸规划的计算可行算法。具体而言，所提算法采用块状乔列斯基分解方法实现最优协方差导向的凸优化建模，并借助最新的序列凸规划算法SCvx*确保可靠的数值收敛性。我们将开发的算法应用于火星引力辅助探测矮行星谷神星的风险约束统计轨迹优化问题，并通过非线性蒙特卡洛仿真验证了统计最优轨迹及飞行路径控制策略的鲁棒性。

---

### 5. Leakage and Second-Order Dynamics Improve Hippocampal RNN Replay

- **作者**: Josue Casco-Rodriguez, Nanda H. Krishna, Richard G. Baraniuk
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.18401v1)
- **发表日期**: 2026-02-20
- **匹配关键词**: exploration
- **arXiv**: [2602.18401v1](http://arxiv.org/abs/2602.18401v1)
- **🔒 开源**: 未提及
- **中文摘要**: 生物神经网络（如海马体）能够内部生成类似刺激驱动活动的“重放”。近期关于重放的计算模型采用经过路径整合训练的噪声循环神经网络（RNN）。这些网络中的重放现象曾被描述为朗之万采样，但新的噪声RNN重放修正机制已超越这一描述。我们重新审视噪声RNN重放作为采样过程，通过三种方式理解或改进该机制：（1）在简单假设下，我们证明重放活动应遵循的梯度具有时变特性且难以估计，但这直接启发了在RNN中利用隐藏状态泄漏实现重放。（2）我们证实隐藏状态适应（负反馈）能促进重放中的探索行为，但同时发现它会导致非马尔可夫采样并减缓重放速度。（3）我们首次提出通过隐藏状态动量实现噪声路径整合RNN中时间压缩重放的模型，将其与欠阻尼朗之万采样相关联，并证明该机制与适应机制结合可在保持探索性的同时克服速度迟缓问题。我们通过二维三角形路径、T型迷宫路径以及合成大鼠位置细胞活动的高维路径整合实验验证了这些发现。

---

### 6. Have We Mastered Scale in Deep Monocular Visual SLAM? The ScaleMaster Dataset and Benchmark

- **作者**: Hyoseok Ju, Bokeon Suh, Giseop Kim
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.18174v1)
- **发表日期**: 2026-02-20
- **匹配关键词**: localization and mapping
- **arXiv**: [2602.18174v1](http://arxiv.org/abs/2602.18174v1)
- **🔒 开源**: 未提及
- **中文摘要**: 深度单目视觉同步定位与建图（SLAM）技术近期在精度与稠密重建能力方面取得了显著进展，但其在大规模室内环境中应对尺度不一致性的鲁棒性仍待深入探索。现有基准测试多局限于房间尺度或结构简单的场景，未能充分解决会话内尺度漂移与会话间尺度模糊性等关键问题。为填补这一空白，我们推出了ScaleMaster数据集——首个专门针对多楼层结构、长轨迹、重复视角及低纹理区域等挑战性场景下尺度一致性评估的基准测试集。我们系统分析了当前先进的深度单目视觉SLAM系统对尺度不一致性的脆弱性，并提供了定量与定性评估。尤为重要的是，我们的分析超越了传统轨迹评估指标，通过引入倒角距离等度量方式，实现了基于高精度三维真值的地图间质量直接评估。实验结果表明，尽管现有深度单目视觉SLAM系统在传统基准测试中表现优异，但在真实大规模室内环境中仍面临严重的尺度相关失效问题。通过开源ScaleMaster数据集及基线结果，我们旨在为未来开发具有尺度一致性与可靠性的视觉SLAM系统奠定研究基础。

---

### 7. Interacting safely with cyclists using Hamilton-Jacobi reachability and reinforcement learning

- **作者**: Aarati Andrea Noronha, Jean Oh
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.18097v1)
- **发表日期**: 2026-02-20
- **匹配关键词**: navigation
- **arXiv**: [2602.18097v1](http://arxiv.org/abs/2602.18097v1)
- **🔒 开源**: 未提及
- **中文摘要**: 本文提出了一种框架，使自动驾驶车辆能够以兼顾安全性与最优性的方式与骑行者进行交互。该方法将汉密尔顿-雅可比可达性分析与深度Q学习相结合，共同解决安全保障与时间效率优化问题。通过求解时变汉密尔顿-雅可比-贝尔曼不等式，计算得到表征系统各状态安全程度的量化价值函数。该安全度量指标被构建为强化学习框架中的结构化奖励信号。该方法进一步建模了骑行者对车辆的潜在反应，使干扰输入能够反映人类舒适度与行为适应性。通过仿真实验，并与人类驾驶行为及现有先进方法进行对比，对所提框架进行了评估验证。

---

### 8. Flow Matching with Injected Noise for Offline-to-Online Reinforcement Learning

- **作者**: Yongjae Shin, Jongseong Chae, Jongeui Park, Youngchul Sung
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.18117v1)
- **发表日期**: 2026-02-20
- **匹配关键词**: exploration
- **arXiv**: [2602.18117v1](http://arxiv.org/abs/2602.18117v1)
- **🔒 开源**: 未提及
- **中文摘要**: 生成模型近期在多个领域展现出卓越成效，这促使研究者将其作为强化学习中的表达性策略进行探索。尽管这类模型在离线强化学习中表现出色——尤其是在目标分布明确的情况下，但其向在线微调的延伸大多被简单视为离线预训练的延续，尚未解决关键性挑战。本文提出基于噪声注入流匹配的离线至在线强化学习方法，该方法利用流匹配策略提升离线至在线强化学习的样本效率。通过在策略训练中注入噪声，该方法鼓励智能体采取超出离线数据集观测范围的多样化动作，从而实现高效探索。除探索增强的流策略训练外，我们还结合熵引导采样机制来平衡探索与利用，使策略能够在在线微调过程中动态调整行为。在多种复杂任务上的实验表明，该方法在有限在线预算条件下始终能取得更优性能。

---

### 9. In-Context Learning for Pure Exploration in Continuous Spaces

- **作者**: Alessio Russo, Yin-Ching Lee, Ryan Welch, Aldo Pacchiano
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.17976v1)
- **发表日期**: 2026-02-20
- **匹配关键词**: exploration
- **arXiv**: [2602.17976v1](http://arxiv.org/abs/2602.17976v1)
- **🔒 开源**: 未提及
- **中文摘要**: 在主动序贯测试（亦称纯探索）中，学习者的目标是通过自适应获取信息，以尽可能少的查询次数识别未知的真实假设。这一由Chernoff于1959年首次研究的问题具有多重应用场景：经典形式包括多臂赌博机中的最优臂识别（BAI）——其中动作对应假设索引，以及广义搜索问题——通过策略性选择的查询揭示隐藏标签的部分信息。然而，在现代诸多场景中，假设空间是连续的且自然与查询/动作空间重合：例如在连续臂赌博机中识别最优动作、定位包含于目标区域的$ε$球、或通过观测序列估计未知函数的最小值点。本研究针对此类连续空间中的纯探索问题，提出适用于该领域的连续上下文内纯探索框架。我们设计了C-ICPE-TS算法，该算法通过元训练深度神经策略网络，将观测历史映射至（i）下一个连续查询动作及（ii）预测假设，从而直接从数据中学习可迁移的序贯测试策略。在推理阶段，C-ICPE-TS能够主动收集新任务的证据，无需参数更新或显式手工构建信息模型即可推断真实假设。我们在连续最优臂识别、区域定位和函数最小值点识别等一系列基准测试中验证了C-ICPE-TS的有效性。

---

### 10. Memory-Based Advantage Shaping for LLM-Guided Reinforcement Learning

- **作者**: Narjes Nourzad, Carlee Joe-Wong
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.17931v1)
- **发表日期**: 2026-02-20
- **匹配关键词**: exploration
- **arXiv**: [2602.17931v1](http://arxiv.org/abs/2602.17931v1)
- **🔒 开源**: 未提及
- **中文摘要**: 在奖励稀疏或延迟的环境中，强化学习（RL）因需要大量交互进行学习而面临样本复杂度高的问题。这一局限性促使研究者利用大语言模型（LLMs）进行子目标发现与轨迹引导。虽然LLMs能够辅助探索，但频繁调用LLM会引发可扩展性与可靠性方面的担忧。为解决这些问题，我们构建了一个记忆图，该图编码了来自LLM引导及智能体自身成功轨迹的子目标与路径。基于此图，我们推导出一个效用函数，用于评估智能体轨迹与先前成功策略的契合程度。该效用函数通过调整优势函数，在不改变奖励机制的前提下为评价者提供额外指导。我们的方法主要依赖离线输入，仅需偶尔进行在线查询，从而避免了对持续LLM监督的依赖。在基准环境中的初步实验表明，相较于基线RL方法，本方法在样本效率与早期学习速度方面均有提升，且最终回报与需要频繁LLM交互的方法相当。

---

### 11. Diffusing to Coordinate: Efficient Online Multi-Agent Diffusion Policies

- **作者**: Zhuoran Li, Hai Zhong, Xun Wang, Qingxin Xia, Lihua Zhang, Longbo Huang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.18291v1)
- **发表日期**: 2026-02-20
- **匹配关键词**: exploration
- **arXiv**: [2602.18291v1](http://arxiv.org/abs/2602.18291v1)
- **🔒 开源**: 未提及
- **中文摘要**: 在线多智能体强化学习（MARL）是提升智能体协同效率的重要框架。其中，增强策略表达能力对于实现卓越性能至关重要。基于扩散的生成模型因其在图像生成和离线场景中展现出的卓越表达能力与多模态表征能力，恰好能满足这一需求。然而，其在在线MARL领域的潜力仍待深入挖掘。主要障碍在于扩散模型难以处理的似然性，这阻碍了基于熵的探索与协同机制。为应对这一挑战，我们率先提出了一种基于扩散策略的在线离轨多智能体强化学习框架（OMAD），以优化协同机制。本研究的核心创新在于提出了一种松弛策略目标，通过最大化缩放联合熵来促进有效探索，而无需依赖可处理的似然性。在此基础上，结合集中训练分散执行（CTDE）范式，我们采用联合分布价值函数来优化分散式扩散策略。该方法利用可处理的熵增强目标引导扩散策略的同步更新，从而确保稳定的协同效果。通过在MPE和MAMuJoCo平台上的广泛评估，我们的方法在10项多样化任务中均达到最新最优性能，样本效率实现了2.5倍至5倍的显著提升。

---

### 12. PRISM: Parallel Reward Integration with Symmetry for MORL

- **作者**: Finn van der Knaap, Kejiang Qian, Zheng Xu, Fengxiang He
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.18277v1)
- **发表日期**: 2026-02-20
- **匹配关键词**: exploration
- **arXiv**: [2602.18277v1](http://arxiv.org/abs/2602.18277v1)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/EVIEHub/PRISM, https://github.com/EVIEHub/PRISM
- **中文摘要**: 本研究探讨异构多目标强化学习（MORL），其中各目标在时间频率上可能存在显著差异。这种异构性导致密集目标主导学习过程，而稀疏的长时程奖励则因信用分配薄弱而影响样本效率。为此，我们提出一种具有对称性的并行奖励集成算法（PRISM），通过引入反射对称性作为归纳偏置来对齐奖励通道。PRISM的核心是理论驱动的ReSymNet模型，该模型利用残差块学习缩放机会价值，以协调目标间的时间频率失配，在加速探索的同时保持最优策略。我们还提出反射等变性正则化器SymReg，强制智能体镜像行为并将策略搜索约束在反射等变子空间中。理论证明这种约束能降低假设复杂度并提升泛化能力。在MuJoCo基准测试中，PRISM持续优于稀疏奖励基线及使用全密集奖励训练的预言机模型，显著提升了帕累托覆盖度与分布平衡性：其超体积指标较基线提升超过100%，较预言机模型提升最高达32%。代码发布于\href{https://github.com/EVIEHub/PRISM}{https://github.com/EVIEHub/PRISM}。

---

