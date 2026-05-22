# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-05-22 08:03

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 2/20 篇提供

**🌟 Highlight**: 9 篇 | **📌 Poster**: 11 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. PointACT: Vision-Language-Action Models with Multi-Scale Point-Action Interaction

- **作者**: Shizhe Chen, Paul Pacaud, Cordelia Schmid
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.21414v1)
- **发表日期**: 2026-05-20
- **匹配关键词**: vision-language-action model, vision-language-action, VLA
- **arXiv**: [2605.21414v1](http://arxiv.org/abs/2605.21414v1)
- **📥 PDF**: 已下载至本地 (`2605.21414v1_PointACT_Vision-Language-Action_Models_with_Multi-Scale_Point-Action_Interaction.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型通过利用大规模预训练的视觉-语言骨干网络，在通用机器人操作任务中展现出巨大潜力。然而，现有VLA模型主要依赖二维视觉表征，这限制了其对细粒度几何结构和空间定位的推理能力——而这些能力正是三维环境中实现精准鲁棒操作的关键。本文提出PointACT，一种双系统三维感知VLA策略，将分层三维点云表征直接集成到动作解码过程中。PointACT采用多尺度点-动作交互机制与高效瓶颈窗口自注意力，使动态动作标记能够密集关注局部几何细节与全局场景结构。我们在LIBERO和RLBench基准上评估PointACT，并系统对比了单系统与双系统VLA基线模型（包括增强点云输入的变体）。PointACT在两个基准上均实现一致性提升：在具有挑战性的RLBench-10Tasks套件中，相较最先进的预训练VLA模型成功率提升10%；当冻结视觉-语言骨干网络并从头训练动作专家模块时，性能增益更为显著。大量消融实验表明，将分层三维几何表征与预训练二维语义表征紧密耦合，是实现鲁棒且具有空间感知能力的机器人控制的关键。我们的研究结果也凸显了预训练三维表征在三维感知VLA策略中的应用前景。

---

### 2. Humanoid Whole-Body Manipulation via Active Spatial Brain and Generalizable Action Cerebellum

- **作者**: Zhizhao Liang, Yi-Lin Wei, Xuhang Chen, Mu Lin, Yi-Xiang He, Zhexi Luo, Jun-Hui Liu, Kun-Yu Lin, Wei-Shi Zheng
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.21133v1)
- **发表日期**: 2026-05-20
- **匹配关键词**: whole-body manipulation
- **arXiv**: [2605.21133v1](http://arxiv.org/abs/2605.21133v1)
- **📥 PDF**: 已下载至本地 (`2605.21133v1_Humanoid_Whole-Body_Manipulation_via_Active_Spatial_Brain_and_Generalizable_Action_Cerebellum.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 本文探索了空间感知的人形全身操控任务。与桌面场景相比，该任务面临两大关键挑战：1）在具有复杂空间关系的三维环境中，空间理解极具挑战性；2）动作生成难以泛化，因为有限且成本高昂的真实机器人数据限制了数据驱动模型的泛化能力。为解决这些问题，我们提出了一种可泛化的人形移动操控框架，该框架利用多智能体大模型的空间感知与动作生成能力。具体而言，该框架包含两个组件：用于主动空间感知与决策的主动空间大脑，以及用于生成可执行机器人动作的泛化动作小脑。第一个组件主动感知空间场景，并对任务规划与子任务分解进行决策；第二个组件基于第一个模块的决策生成可执行的机器人动作，无需依赖特定任务的真实机器人数据。为评估该框架，我们从两个维度设计了一系列空间操控任务：评估空间感知与理解能力，以及评估真实机器人任务表现。实验结果表明，该框架在多样化任务与环境中均展现出优异性能。

---

### 3. WiXus: A Wheeled-Legged Robot with Wire-Driven Environmental Utilizing to Integrate Mobility and Manipulation

- **作者**: Shintaro Inoue, Kento Kawaharazuka, Temma Suzuki, Sota Yuzaki, Kei Okada
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.20932v1)
- **发表日期**: 2026-05-20
- **匹配关键词**: object manipulation
- **arXiv**: [2605.20932v1](http://arxiv.org/abs/2605.20932v1)
- **📥 PDF**: 已下载至本地 (`2605.20932v1_WiXus_A_Wheeled-Legged_Robot_with_Wire-Driven_Environmental_Utilizing_to_Integrate_Mobility_and_Mani.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 轮腿式机器人通过在足部安装轮子，并协调轮驱动与腿部驱动实现高机动性，这类机器人最初仅作为专用运动平台开发。因此，它们缺乏将腿部功能从运动领域拓展至物体操作或工具使用等其他用途的手段。本文探讨如何通过外部身体支撑将腿部从运动功能中解放出来，从而挖掘其潜在的任务执行能力。为此，我们提出并开发了一种新型机器人WiXus，该机器人融合了轮腿机构与利用外部环境的线驱动机构。所开发的WiXus不仅能够实现轮腿驱动的平面运动，还能通过协调线驱动与轮腿驱动完成悬崖攀爬等三维移动。此外，通过线驱动悬吊机身，WiXus成功将腿部重新用作机械臂，执行物体操作（如救援玩具狗）和工具使用（如用修枝剪采摘仿真苹果）。本研究证明，利用线驱动结合环境的设计方法，是拓展轮腿式机器人操作领域的新设计原则。

---

### 4. Mobile UMI: Cross-View Diffusion Policy with Decoupled Kinematics for Mobile Manipulation

- **作者**: Haoran Huang, Haonan Dong, Huixu Dong
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.20894v1)
- **发表日期**: 2026-05-20
- **匹配关键词**: mobile manipulation, navigation, diffusion policy
- **arXiv**: [2605.20894v1](http://arxiv.org/abs/2605.20894v1)
- **📥 PDF**: 已下载至本地 (`2605.20894v1_Mobile_UMI_Cross-View_Diffusion_Policy_with_Decoupled_Kinematics_for_Mobile_Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 移动式模仿学习在便携式演示接口上面临两个相互耦合的瓶颈：运动污染的动作标签，以及在持续移动基座上由推理引发的执行延迟。近期腕戴式接口降低了桌面数据采集的成本，但单一腕部视角无法捕捉基座导航所需的全局上下文。在身体上安装摄像头会将人类行走与手部运动纠缠在一起。同时，生成式策略引入数百毫秒的推理延迟，在此期间基座会越过预测路径点，迫使在动作拼接处进行反向修正。本文提出Mobile UMI——一种无需硬件的演示框架，通过三个组件解决上述两个瓶颈。首先，双摄像头采集系统在无机器人参与的情况下，记录以胸部为中心的全局上下文和以腕部为中心的局部交互。其次，基于ChArUco的一次性空间锚点统一了胸部与手部的视觉惯性坐标系；随后将手部姿态相对于胸部重新表达，以提取解耦的SE(3)操作轨迹与SE(2)基座轨迹。第三，异步滚动时域执行器执行在线状态匹配：每个生成的动作块与当前物理姿态重新对齐，使过期路径点在执行前被丢弃。该系统在四项长时域家庭任务上进行了评估，每项任务100次试验的平均成功率达83.8%。与ACT和扩散策略的对比实验表明，仅使用胸部相对标签即可缩小大部分差距；在线状态匹配则弥补了剩余差距。这些结果表明，在测试条件下的移动式模仿学习中，显式运动学分解结合状态级延迟对齐，无需对底层策略类别进行架构修改即可提供有效解决方案。

---

### 5. VLA-REPLICA: A Low-Cost, Reproducible Benchmark for Real-World Evaluation of Vision-Language-Action Models

- **作者**: Alex S. Huang, Jiahui Zhang, Shiqing Tang, Yu Xiang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.20774v1)
- **发表日期**: 2026-05-20
- **匹配关键词**: vision-language-action model, vision-language-action, VLA
- **arXiv**: [2605.20774v1](http://arxiv.org/abs/2605.20774v1)
- **📥 PDF**: 已下载至本地 (`2605.20774v1_VLA-REPLICA_A_Low-Cost,_Reproducible_Benchmark_for_Real-World_Evaluation_of_Vision-Language-Action_M.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型在通用机器人操作领域展现出巨大潜力，但其现实世界评估仍受限于缺乏易获取、可复现且一致的基准测试。仿真基准无法捕捉真实世界的复杂性，而现有真实世界基准往往需要昂贵硬件、集中式评估，或任务多样性有限。我们提出VLA-REPLICA——一种低成本、易复现的真实世界基准，用于评估VLA模型。该系统采用现成组件构建，可在不同实验室快速组装和复制，为全球范围内的策略评估提供一致环境。VLA-REPLICA包含多样化的操作任务套件及用于目标域适配的小规模演示数据集，并针对分布内和分布外场景设计了真实世界评估协议。基于模仿学习与先进VLA模型的实验揭示了模型优势与局限性，而独立搭建系统间的一致性结果则验证了本基准的可复现性。

---

### 6. GaussianDream: A Feed-Forward 3D Gaussian World Model for Robotic Manipulation

- **作者**: Zijian Zhang, Yuqing Jiang, Qian Cheng, Si Liu, Ding Zhao, Ping Luo, Weitao Zhou, Haibao Yu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.20752v1)
- **发表日期**: 2026-05-20
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2605.20752v1](http://arxiv.org/abs/2605.20752v1)
- **📥 PDF**: 已下载至本地 (`2605.20752v1_GaussianDream_A_Feed-Forward_3D_Gaussian_World_Model_for_Robotic_Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）策略通过将预训练的视觉-语言模型中的语义先验迁移到动作生成中，推动了语言条件机器人操作的发展。然而，标准的动作模仿训练通常对三维几何、密集视觉结构以及短时域环境演化提供的显式监督有限，而这些对于物理精确的操作至关重要。我们提出**GaussianDream**，一种前馈式三维高斯世界模型插件，能够将机器人轨迹转化为结构化的时空监督。其核心思想是在训练过程中将当前高斯重建与基于时域条件的未来高斯预测相结合，迫使紧凑的时空前缀可解码为可渲染的三维高斯状态。这使得无需在测试时进行高斯解码即可实现密集的RGB渲染、深度以及伪三维场景流监督。在推理阶段，GaussianDream丢弃所有辅助解码头，仅保留学习到的前缀来条件化动作生成，从而在闭环控制中避免渲染、视频推演或额外规划。在LIBERO、RoboCasa Human-50以及真实机器人任务上的实验表明，该方法具有强大且极具竞争力的性能，在LIBERO上平均成功率达到**98.4%**，在RoboCasa Human-50上达到**52.6%**，在真实世界评估中达到**50.0%**。

---

### 7. Conflict-Aware Active Perception and Control in 3D Gaussian Splatting Fields via Control Barrier Functions

- **作者**: Amirhossein Mollaei Khass, Athanasios Cosse, Vivek Pandey, Nader Motee
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.20566v1)
- **发表日期**: 2026-05-19
- **匹配关键词**: active perception, 3D gaussian splatting, gaussian splatting
- **arXiv**: [2605.20566v1](http://arxiv.org/abs/2605.20566v1)
- **📥 PDF**: 已下载至本地 (`2605.20566v1_Conflict-Aware_Active_Perception_and_Control_in_3D_Gaussian_Splatting_Fields_via_Control_Barrier_Fun.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 在不确定环境中实现主动感知，要求机器人在安全导航的同时获取信息丰富的观测数据以降低地图不确定性。这两个目标本质上存在冲突，因为信息丰富的视点往往位于碰撞风险较高的不确定区域附近。为应对这一挑战，我们开发了一种面向三维高斯泼溅（3DGS）环境表征的冲突感知主动感知与控制框架。通过采用基于平均风险价值（AV@R）碰撞风险度量的控制障碍函数（CBF）来保障安全性，该函数考虑了几何不确定性并保证安全集的前向不变性。为提升感知性能，我们提出了一种风险感知的期望信息增益（EIG）公式用于选择下一最佳视点，并引入感知障碍函数使相机朝向与局部信息上升方向对齐。针对安全与感知目标的冲突性，我们提出了一种统一的安全关键型感知感知二次规划，将安全作为硬约束强制执行，同时通过松弛变量放宽感知约束。仿真结果表明，与现有基于3DGS的方法相比，所提方法在安全性和信息获取方面均有所提升。

---

### 8. Enhancing Graph-Based SLAM in GNSS-Denied environments by leveraging leg odometry

- **作者**: Léon Perruchot-Triboulet, Luc Jaulin, Kai Xiao
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.20484v1)
- **发表日期**: 2026-05-19
- **匹配关键词**: navigation, autonomous navigation
- **arXiv**: [2605.20484v1](http://arxiv.org/abs/2605.20484v1)
- **📥 PDF**: 已下载至本地 (`2605.20484v1_Enhancing_Graph-Based_SLAM_in_GNSS-Denied_environments_by_leveraging_leg_odometry.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 在GNSS拒止环境中，足式机器人的自主导航仍面临核心挑战，其中激光雷达等外部传感器在几何稀疏或重复场景中易出现高程漂移。我们提出了一种因子图架构，通过基于本体感知腿部里程计的并行运动学支路增强LIO-SAM框架，并借助带有选择性噪声模型的恒等相对位姿约束将其与主激光雷达-惯性支路耦合。将该方法应用于灵犀D50四足平台，在总长超过一公里的两个室外环路测试中，我们的方法将高程漂移从30米以上降低至30厘米以下，并在基线方案完全失效的场景中实现了收敛。这些结果表明，已在机载步态控制中完成计算的本体感知数据，构成了GNSS拒止环境下SLAM轻量且有效的垂直锚点。

---

### 9. CEER: Compliant End-Effector and Root Control as a Unified Interface for Hierarchical Humanoid Loco-Manipulation

- **作者**: Xinyuan Luo, Xingrui Chen, Xunjian Yin, Hongxuan Wu, Boxi Xia, Zhuoqun Chen, Jinzhou Li, Boyuan Chen, Xianyi Cheng
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.19981v1)
- **发表日期**: 2026-05-19
- **匹配关键词**: contact-rich manipulation
- **arXiv**: [2605.19981v1](http://arxiv.org/abs/2605.19981v1)
- **📥 PDF**: 已下载至本地 (`2605.19981v1_CEER_Compliant_End-Effector_and_Root_Control_as_a_Unified_Interface_for_Hierarchical_Humanoid_Loco-M.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 人形机器人已在运动性能上取得显著进展，但涉及密集接触与长时程操作的任务仍是主要瓶颈。操作任务本质上需要密集接触，要求具备柔顺全身控制以实现稳定交互；同时其多样性与长时程特性更倾向于模块化、与规划器兼容的接口，而非关节空间跟踪。

我们提出CEER（柔顺末端-根基控制抽象），这是一种面向模块化人形移动操作的分层规划框架。CEER在由根基运动指令与末端执行器位姿目标定义的可解释任务空间中实现柔顺感知的全身控制，并支持与异构高层规划器的即插即用集成。采用教师-学生框架将通用运动跟踪控制器蒸馏为仅需末端-根基指令的低层策略。

进一步通过末端-根基接口构建集成异构规划器与任务模块的分层系统，无需重新训练底层全身策略即可实现多样化操作任务。仿真与硬件实验表明：末端执行器跟踪精度达3.3厘米，相较基线方法显著降低加速度突变；遥操作下实现稳定的密集接触操作；在房间尺度仿真环境中，单物体移动操作任务成功率高达70%。这些结果表明，柔顺末端-根基控制为人形移动操作提供了实用抽象，能够实现多样化技能的模块化与可扩展集成。

---

## 📌 Poster

*其他相关研究*

---

### 1. From swept contact to pose: Probe-aware registration via complementary-shape docking

- **作者**: Chen Chen, Yunwen Li, Yifan Xu, Xiangjie Yan, Chang Shu, Jianxia Hou, Shiji Song, Xiang Li
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.21398v1)
- **发表日期**: 2026-05-20
- **匹配关键词**: exploration
- **arXiv**: [2605.21398v1](http://arxiv.org/abs/2605.21398v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 先验模型与真实场景的精确配准对于高精度机器人操作至关重要，然而光学方法存在标定链长、视线约束和制造误差等问题。我们提出一种免标定替代方案，将接触配准重新定义为物体与探针扫掠体之间的互补形状对接，明确考虑探针几何形状，并同时利用接触与非接触证据。我们的求解器通过低差异SO(3)样本上的三维FFT相关实现全局到局部的搜索，随后利用李代数更新和分析接触灵敏度进行连续SE(3)精化。该流程无需脆弱的点对应关系即可实现高效探索和度量级收敛。在自由曲面网格上的仿真实现了低于0.04毫米和0.4°的精度，并对位姿噪声和接触丢失具有鲁棒性。在牙齿预备机器人上，我们的方法达到0.42毫米和3.75°的精度，优于光学跟踪仪配准，且无需外部传感器。这些结果表明该方法为手术和工业机器人提供了一种实用且精确的配准策略。

---

### 2. Learning Robust Dexterous In-Hand Manipulation from Joint Sensors with Proprioceptive Transformer

- **作者**: Senlan Yao, Chenyu Yang, Jaehoon Kim, Aristotelis Sympetheros, Robert K. Katzschmann
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.21330v1)
- **发表日期**: 2026-05-20
- **匹配关键词**: object manipulation
- **arXiv**: [2605.21330v1](http://arxiv.org/abs/2605.21330v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 手内物体操作是灵巧机器人一项基础但具有挑战性的能力。尽管灵巧操作领域取得了显著进展，现有方法仍高度依赖视觉或触觉传感来追踪物体状态，而关节传感——任何机器人手上最易获取的感知模态——在很大程度上被忽视，尤其是在腱驱动手中。本文通过探究以下问题来研究仅凭关节传感所能达到的极限：(i) 电机编码器与直接关节传感哪种能提供更好的本体感知反馈，(ii) 如何从关节测量中提取环境信息，以及(iii) 仅依赖关节控制能否在无外部感知的情况下实现具有竞争力的真实世界性能。我们提出了本体感知Transformer（PT），这是一种无需外部感知的方法，仅使用关节传感反馈在腱驱动灵巧手上实现连续立方体旋转。首先通过强化学习结合特权物体信息训练教师策略，然后将其蒸馏到仅依赖关节位置和速度历史数据的PT中。Transformer架构能有效从关节传感器读数的时间序列模式中提取隐式物体状态信息。在真实ORCA手上的实验表明，我们的方法旋转速度比基线方法快3.1倍。我们还证明，PT在立方体位置估计上的均方根误差比MLP基线低23.4%，表明其从本体感知源中提取外部感知信息的能力更优。

---

### 3. Learning Structural Latent Points for Efficient Visual Representations in Robotic Manipulation

- **作者**: Yicheng Jiang, Jiaxu Wang, Junhao He, Zesen Gan, Junhao Li, Qiang Zhang, Jingkai Sun, Jiahang Cao, Mingyuan Sun, Xiangyu Yue, Qiming Shao
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.21258v1)
- **发表日期**: 2026-05-20
- **匹配关键词**: perception and manipulation, implicit representation
- **arXiv**: [2605.21258v1](http://arxiv.org/abs/2605.21258v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 当前面向具身感知与操作的3D感知预训练方法主要基于可微渲染框架，生成完全隐式神经场或完全显式几何基元。隐式表示虽具表现力但缺乏显式结构线索，而显式表示虽保留几何结构却受限于分辨率与泛化能力不足。为解决上述局限，我们提出一种新型预训练框架，学习混合表示——结构潜在点。具体而言，我们在点云自编码器的潜在空间中插入逐点潜在变分自编码器，联合正则化逐点特征与坐标使其服从高斯先验。由此产生的紧凑潜在表示保留了粗略结构趋势，虽不编码精确几何，但能捕获更丰富的粗糙形状与语义信息，有效融合隐式表示的表现力与显式表示的结构先验。此外，受先前工作中共享设计选择的启发，我们开发了基于3DGS的轻量化高效渲染管线，刻意保持简洁性以提升效率，同时将更多表示能力留给前端潜在模块。在RLBench、ManiSkill2及真实机器人平台上的大量实验表明，相较于强基线方法，本方法在任务成功率、样本效率及对视角与场景变化的鲁棒性方面均取得一致性提升。消融研究进一步证实，框架中每个组件对整体性能均至关重要。

---

### 4. Reinforcement Learning for Risk Adaptation via Differentiable CVaR Barrier Functions

- **作者**: Xinyi Wang, Taekyung Kim, Bardh Hoxha, Georgios Fainekos, Dimitra Panagou
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.21257v1)
- **发表日期**: 2026-05-20
- **匹配关键词**: navigation
- **arXiv**: [2605.21257v1](http://arxiv.org/abs/2605.21257v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 在障碍物运动不确定的拥挤环境中进行路径规划仍然具有挑战性，因为随机交互往往会导致过度保守的行为或效率降低。为解决这一问题，我们提出了一种端到端的风险自适应框架，用于在基于高斯混合模型建模的障碍物运动不确定性下实现人群导航。该框架将强化学习与基于条件风险价值障碍函数的可微二次规划安全层相结合，联合学习标称控制输入、风险水平及安全裕度，并强制执行显式概率安全约束。这种设计实现了情境感知的自适应能力，在必要时才触发谨慎行为，从而促进高效导航。我们在动态、不确定且拥挤的环境中，针对不同障碍物密度和机器人模型进行了广泛评估，并进一步测试了三种分布外场景下的泛化能力。通过对比基于优化、基于强化学习以及强化学习与优化集成的方法，所提方法在不确定性条件下的安全性、效率和泛化能力方面展现出最优的综合性能。

---

### 5. Perception of Social Robots as Communication Partners in Healthcare for Older Adults

- **作者**: Hana Yamamoto, Carlotta Julia Mayer, Charlotte Raithel, Theresa Buchner, Christian Werner, Yasuhisa Hirata, Monika Eckstein, Katja Mombaur
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.21053v1)
- **发表日期**: 2026-05-20
- **匹配关键词**: HRI, human-robot interaction
- **arXiv**: [2605.21053v1](http://arxiv.org/abs/2605.21053v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 应对全球照护人员短缺问题，社会辅助机器人需深入理解人机交互（HRI）过程中对老年人的心理和生理影响。本研究探讨了社交机器人能否像人类一样成为有效的互动伙伴，以及"积极提示"是否也能增强此类互动。我们开展了一项包含35名70岁以上参与者的对比研究。通过整合面部表情数据、心率变异性及主观问卷的多模态分析发现，人类互动与机器人互动在整体压力水平上无显著差异。面部表情分析证实机器人被接受为有效互动伙伴，而生理数据显示机器人互动期间心率略低，表明相较于人类主导的互动，参与者处于更放松的状态。这些结果表明，社交机器人能在不引发心理压力的前提下与老年人互动，并通过执行结构化任务（如健康感知调查）减轻照护负担。未来研究应解决机器人设计中存在的"外观-内容不匹配"问题，以促进更自然有效的互动。

---

### 6. SubTGraph: Large-Scale Subterranean Environment Synthesis with Controllable Topological Variability for Robotic Autonomy Validation

- **作者**: F. Labra Caso, A. Saradagi, S. Fredriksson, S. Nordström, A. Koval, G. Nikolakopoulos
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.20917v1)
- **发表日期**: 2026-05-20
- **匹配关键词**: exploration, path planning
- **arXiv**: [2605.20917v1](http://arxiv.org/abs/2605.20917v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: CODE, GITHUB
  - 链接：https://github.com/LTU-RAI/SubTGraph.git)
- **中文摘要**: 地下（SubT）环境一直是自主机器人领域的前沿方向，这得益于采矿作业自动化需求的推动以及行星探索（如火星熔岩管）的研究兴趣。由于进入真实地下环境存在诸多挑战，在逼真的仿真环境中对自主系统进行严格验证至关重要。本文填补了一个显著的研究空白——目前缺乏基于大规模仿真环境的标准化基准测试基础设施，用于对机器人自主性进行严格的统计评估，因此地下环境研究论文通常仅能在少数环境中展示验证结果。

本文提出SubTGraph这一新型框架，可快速合成具有高度变异性的多层次地下环境。该框架整合用户对拓扑结构、维度、纹理等参数的设定，生成诸如运营矿井、天然洞穴和熔岩管等差异化环境。SubTGraph根据用户指定的结构约束构建代价矩阵，引导经典Dijkstra算法，利用DARPA世界生成器中的拓扑度量瓦片程序化生成地下世界。通过三个机器人案例研究，验证了SubTGraph在机器人自主系统不同层级严格验证中的实用性：结构语义分割基于拓扑度量真值进行验证，多智能体路径规划通过广泛测试识别算法行为模式与趋势，LIO SLAM则在具有挑战性的地下区域进行压力测试以定位失效案例。SubTGraph世界创建代码库已开源（https://github.com/LTU-RAI/SubTGraph.git），并附带包含150个高度变异地下世界的数据库。

---

### 7. ArchSIBench: Benchmarking the Architectural Spatial Intelligence of Vision-Language Models

- **作者**: Qirui Shen, Wenda Wang, Jiachen Lu, Zilong Huang, Jin Bai, Lei He, Hongxuan Chen, Weixin Huang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.20837v1)
- **发表日期**: 2026-05-20
- **匹配关键词**: robot navigation, navigation
- **arXiv**: [2605.20837v1](http://arxiv.org/abs/2605.20837v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: HUGGINGFACE
  - 链接：https://huggingface.co/datasets/ArchSIBench/ArchSIBench.
- **中文摘要**: 建筑空间智能——即识别与推理建筑空间的能力——是机器人导航、具身交互、三维场景理解与生成等任务的基础。尽管已有大量研究评估了视觉语言模型（VLM）的基本空间能力（如相对方位、距离比较和物体计数），但这些任务仅覆盖空间认知的最基础层面，很大程度上忽略了对建筑空间的高阶认知，包括布局理解、流线组织和功能分区。本研究提出ArchSIBench——一个基于建筑学、认知科学和心理学视角的建筑空间智能基准测试。ArchSIBench涵盖感知、推理、导航、转换和配置五大核心维度，包含17个细粒度子任务。通过具有建筑背景的专家进行精细人工标注，我们构建了3000个问答对，以实现对建筑空间智能的全面评估。基于ArchSIBench，我们对多种VLM进行评测，发现大多数模型的建筑空间智能与人类基线存在显著差异；此外，模型在不同能力维度上表现出较大变异性。部分最先进模型可接近未受建筑学训练的人类评估者水平，但与受过建筑学训练的人类评估者相比仍存在明显差距，尤其在空间转换和配置推理方面。我们相信ArchSIBench将为衡量和提升VLM的建筑空间智能提供重要洞见与系统性资源。数据集与代码已开源：https://huggingface.co/datasets/ArchSIBench/ArchSIBench

---

### 8. VSCD: Video-based Scene Change Detection in Unaligned Scenes

- **作者**: Jiae Yoon, Ue-Hwan Kim
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.20821v1)
- **发表日期**: 2026-05-20
- **匹配关键词**: long-term autonomy
- **arXiv**: [2605.20821v1](http://arxiv.org/abs/2605.20821v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 检测环境中的变化对于长期自主性至关重要，但大多数变化检测场景都假设固定视角、轻微错位或仅有少量变化物体。我们提出基于视频的场景变化检测（VSCD），该方法在给定同一室内空间不同时间、无约束相机运动下录制的参考视频和查询RGB视频时，为每个查询帧预测像素级变化掩码。两个视频在时间上不同步，且可能有许多物体实例出现或消失。为研究这一场景，我们构建了一个大规模基准数据集，包含超过110万帧带有像素精确变化掩码的标注，以及一个用于评估模拟之外迁移能力的真实世界测试集。我们提出一种以查询为中心的多参考模型，该模型通过变化掩码监督隐式学习时间匹配，通过局部块对应关系将候选参考特征对齐到查询，并在解码每帧高分辨率掩码之前，利用帧级和块级置信度融合每个候选的变化特征。我们的方法在基于图像和视频的强基线方法上取得了最先进的性能，并通过将其部署在移动机器人上用于两个下游应用——视觉监控和物体增量学习——验证了其在真实世界中的影响力。

---

### 9. Q-SpiRL: Quantum Spiking Reinforcement Learning for Adaptive Robot Navigation

- **作者**: Mohamed Khair Altrabulsi, Nouhaila Innan, Alberto Marchisio, Muhammad Kashif, Muhammad Shafique
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.20801v1)
- **发表日期**: 2026-05-20
- **匹配关键词**: robot navigation, navigation
- **arXiv**: [2605.20801v1](http://arxiv.org/abs/2605.20801v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 动态环境中的自适应机器人导航需要能够在可靠到达目标的同时，生成高效且稳定轨迹的策略。本文提出Q-SpiRL——一种用于障碍物感知机器人导航的量子脉冲强化学习框架。该框架开发并评估了五个智能体家族：表格型Q学习、经典MLP、经典SNN、量子增强MLP（QMLP）和量子增强脉冲神经网络（QSNN）。尽管所有模型均在统一的训练与评估流程下实现，但QSNN作为核心架构，融合了基于脉冲的时间处理与变分量子特征变换。实验在三种规模递增的网格世界环境（20×20、30×30和40×40）中展开，包含静态与动态障碍物。通过确定性推理下的成功率、成功加权路径长度、路径长度和转向率评估性能。结果表明，QSNN在任务完成度、轨迹效率与运动平滑性之间实现了最优整体权衡——在最具挑战性的场景中，其成功率高达99%，同时保持高路径效率。在IBM量子硬件上的执行进一步验证了所提混合策略在真实设备条件下的部署可行性。

---

### 10. Spacetime Optimal-Transport Attention for Visuo-Haptic Imitation Learning of Contact-Rich Manipulation

- **作者**: Yue Feng, Weicheng Huang, I-Ming Chen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.20433v1)
- **发表日期**: 2026-05-19
- **匹配关键词**: contact-rich manipulation
- **arXiv**: [2605.20433v1](http://arxiv.org/abs/2605.20433v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 高精度装配、连接器插接、抛光及曲面贴合擦拭等接触密集操作任务对数据驱动控制器构成持续挑战，因其耦合了非连续接触动力学、部分可观测性及严格安全约束。单一传感模态难以胜任：视觉在接触前提供全局场景信息，力/力矩反馈主导接触后交互，本体感知位姿则提供一致的运动学骨架。现有接触密集任务的模仿学习策略大多基于单模态或双模态信号，少数融合三模态的方法通常采用现成注意力模块，缺乏对注意力权重在任务相关区域分布的先验约束。我们提出时空最优传输注意力（SO-TA），这是一种三模态融合骨干网络，通过力-位姿衍生子查询与视觉补丁之间的熵正则化最优传输对齐，替代了基于softmax归一化的补丁注意力机制。显式边际约束作为接触密集任务的结构化归纳偏置，促进条件感知的空间选择，在光照变化、干扰物及部分遮挡条件下保持稳定。SO-TA与基于扩散的序列策略配对，将观测窗口映射为位姿-动作块。我们在三项真实机器人任务中评估SO-TA：高精度销孔装配、BCM线束连接器插接及曲面标记擦除。每项条件约200次试验中，SO-TA在高精度销孔装配任务上达到100%成功率（同等容量下交叉注意力为93%），在光照、干扰物及部分遮挡扰动下保持82.5%成功率（而拼接基线降至43.5%）。基于最优传输的补丁热力图及留一模态影响比提供了可解释的相位依赖诊断。

---

### 11. Scalable Multi-robot Motion Planning via Hierarchical Subproblem Expansion and Workspace Decomposition Refinement

- **作者**: Isaac Ngui, Courtney McBeth, James D. Motes, Marco Morales, Nancy M. Amato
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.20395v1)
- **发表日期**: 2026-05-19
- **匹配关键词**: motion planning
- **arXiv**: [2605.20395v1](http://arxiv.org/abs/2605.20395v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 多机器人运动规划中的一个基本挑战在于，既要实现足够的协调以避免机器人间的冲突，又需避免因搜索机器人群体联合构型空间而产生巨大的计算开销。本研究提出了一种多移动机器人运动规划方法，通过利用工作空间分解的离散搜索来在规划过程中实现机器人间的协调，从而将规划时间提升一个数量级。现有研究通过工作空间拓扑结构判断何时需要机器人间协调，并将机器人组合至其联合构型空间，而本研究则更进一步，通过迭代优化工作空间表征，使规划器能够搜索更小、更解耦的构型空间。

---

