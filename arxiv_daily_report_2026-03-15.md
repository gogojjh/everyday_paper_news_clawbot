# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-03-15 08:06

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 5/20 篇提供

**🌟 Highlight**: 6 篇 | **📌 Poster**: 14 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. SaPaVe: Towards Active Perception and Manipulation in Vision-Language-Action Models for Robotics

- **作者**: Mengzhen Liu, Enshen Zhou, Cheng Chi, Yi Han, Shanyu Rong, Liming Chen, Pengwei Wang, Zhongyuan Wang, Shanghang Zhang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.12193v1)
- **发表日期**: 2026-03-12
- **匹配关键词**: vision-language-action model, vision-language-action, active perception, perception and manipulation
- **arXiv**: [2603.12193v1](http://arxiv.org/abs/2603.12193v1)
- **📥 PDF**: 已下载至本地 (`2603.12193v1_SaPaVe_Towards_Active_Perception_and_Manipulation_in_Vision-Language-Action_Models_for_Robotics.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://lmzpai.github.io/SaPaVe
- **中文摘要**: 主动感知与操作是机器人在复杂场景中进行交互的关键。现有方法难以将语义驱动的主动感知与稳健、视角无关的执行能力统一起来。我们提出SaPaVe框架，通过数据高效的方式端到端联合学习这两种能力。该方法将相机控制与操作动作解耦而非置于共享动作空间，并采用自底向上的训练策略：首先在大规模数据集上训练语义相机控制，随后利用混合数据联合优化两类动作。为支撑该框架，我们构建了包含20万组图像-语言-相机运动对的ActiveViewPose-200K数据集用于语义相机运动学习，并设计了提升动态视角下执行鲁棒性的三维几何感知模块。同时我们推出首个超越固定视角设置的主动操作评估基准ActiveManip-Bench。在仿真与真实环境中的大量实验表明，SaPaVe在现实任务中成功率最高可提升31.25%，优于GR00T N1、\(π_0\)等近期视觉-语言-动作模型。这些结果证明，通过解耦但协调的策略进行训练，紧密耦合的感知与执行能够实现高效且可泛化的主动操作。项目页面：https://lmzpai.github.io/SaPaVe

---

### 2. Concurrent Prehensile and Nonprehensile Manipulation: A Practical Approach to Multi-Stage Dexterous Tasks

- **作者**: Hao Jiang, Yue Wu, Yue Wang, Gaurav S. Sukhatme, Daniel Seita
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.11655v1)
- **发表日期**: 2026-03-12
- **匹配关键词**: diffusion policy
- **arXiv**: [2603.11655v1](http://arxiv.org/abs/2603.11655v1)
- **📥 PDF**: 已下载至本地 (`2603.11655v1_Concurrent_Prehensile_and_Nonprehensile_Manipulation_A_Practical_Approach_to_Multi-Stage_Dexterous_T.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 灵巧手能够实现抓握与非抓握并行的操作，例如在持握一个物体的同时与另一个物体进行交互，这种能力在日常任务中至关重要，但在机器人领域尚未得到充分探索。学习这种长时程、高接触的多阶段行为具有挑战性，因为收集演示数据成本高昂，且端到端策略需要大量数据才能适应不同物体几何形状和摆放位置的变化。我们提出DexMulti方法，这是一种样本高效的现实世界灵巧多任务操作方案，通过将演示分解为具有明确时间边界的以物体为中心的技能。与学习单一整体策略不同，我们的方法根据当前物体几何形状检索已演示技能，利用跟踪质心和偏航角的不确定性感知估计器将其与观测到的物体状态对齐，并通过检索-对齐-执行范式实现技能调用。我们在两个灵巧手平台（Allegro和LEAP）上对三种需要并行操作的多阶段任务（抓取+拉动、抓取+开启、抓取+抓取）进行了超过1000次真实世界试验评估。该方法仅需每个物体3-4次演示，就在训练物体上达到平均66%的成功率，性能超越扩散策略基线2-3倍，同时所需演示数据大幅减少。实验结果表明，该方法对未见过的物体及±25厘米范围内的空间变化均展现出鲁棒的泛化能力。

---

### 3. RoboClaw: An Agentic Framework for Scalable Long-Horizon Robotic Tasks

- **作者**: Ruiying Li, Yunlang Zhou, YuYao Zhu, Kylin Chen, Jingyuan Wang, Sukai Wang, Kongtao Hu, Minhui Yu, Bowen Jiang, Zhan Su, Jiayao Ma, Xin He, Yongjian Shen, Yangyang, Guanghui Ren, Maoqing Yao, Wenhao Wang, Yao Mu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.11558v1)
- **发表日期**: 2026-03-12
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2603.11558v1](http://arxiv.org/abs/2603.11558v1)
- **📥 PDF**: 已下载至本地 (`2603.11558v1_RoboClaw_An_Agentic_Framework_for_Scalable_Long-Horizon_Robotic_Tasks.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）系统在语言驱动的机器人操作方面展现出巨大潜力，但将其扩展至长周期任务仍面临挑战。现有技术流程通常将数据收集、策略学习和任务执行分离，导致严重依赖人工环境重置且多策略执行脆弱。我们提出RoboClaw——一个智能机器人框架，在单一VLM驱动控制器下统一了数据收集、策略学习与任务执行。在策略层面，RoboClaw引入纠缠动作对（EAP），通过将正向操作行为与逆向恢复动作耦合，形成自主数据收集的自重置循环。该机制能以最少人工干预实现持续的在线策略数据采集与迭代策略优化。在部署阶段，同一智能体执行高层推理并动态编排已学习的策略基元，以完成长周期任务。通过保持数据收集与执行阶段一致的上下文语义，RoboClaw减少了两个阶段间的失配，提升了多策略鲁棒性。真实世界操作任务实验表明，相比传统开环流程，该系统在提升稳定性与可扩展性的同时，显著减少了机器人全生命周期中的人力投入——在长周期任务上成功率较基线方法提升25%，人力时间投入降低53.7%。

---

### 4. Node-RF: Learning Generalized Continuous Space-Time Scene Dynamics with Neural ODE-based NeRFs

- **作者**: Hiran Sarkar, Liming Kuang, Yordanka Velikova, Benjamin Busam
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.12078v1)
- **发表日期**: 2026-03-12
- **匹配关键词**: nerf, neural radiance field
- **arXiv**: [2603.12078v1](http://arxiv.org/abs/2603.12078v1)
- **📥 PDF**: 已下载至本地 (`2603.12078v1_Node-RF_Learning_Generalized_Continuous_Space-Time_Scene_Dynamics_with_Neural_ODE-based_NeRFs.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 从视觉观测中预测场景动态具有挑战性。现有方法仅能捕捉观测边界内的动态，难以在训练序列范围外进行有效外推。Node-RF（基于神经常微分方程的神经辐射场）通过将神经常微分方程与动态神经辐射场相结合，构建了连续时空表征，能够在恒定内存成本下实现超越观测轨迹的泛化能力。该系统从视觉输入中学习隐式场景状态，通过常微分方程求解器实现状态演化，并借助微分运算传播特征嵌入。基于神经辐射场的渲染器通过解析计算得到的嵌入特征，可合成任意视角以实现长程外推。通过对具有共享动态特性的多组运动序列进行训练，该方法能够泛化至未观测场景。实验表明，Node-RF无需显式模型即可表征抽象系统行为，并能识别未来预测的关键节点。

---

### 5. AstroSplat: Physics-Based Gaussian Splatting for Rendering and Reconstruction of Small Celestial Bodies

- **作者**: Jennifer Nolan, Travis Driver, John Christian
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.11969v1)
- **发表日期**: 2026-03-12
- **匹配关键词**: gaussian splatting, neural scene representation, navigation
- **arXiv**: [2603.11969v1](http://arxiv.org/abs/2603.11969v1)
- **📥 PDF**: 已下载至本地 (`2603.11969v1_AstroSplat_Physics-Based_Gaussian_Splatting_for_Rendering_and_Reconstruction_of_Small_Celestial_Bodi.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 基于图像的表面重建与表征对小天体（如小行星）探测任务至关重要，它为任务规划、导航和科学分析提供关键信息。高斯溅射技术的最新进展实现了高保真度的神经场景表征，但通常依赖于球谐光照强度参数化方法，该方法严格基于外观表现，未显式建模材料属性或光与表面的相互作用。我们提出AstroSplat——一个基于物理的高斯溅射框架，该框架整合行星反射率模型，旨在通过原位影像提升小天体表面的自主重建与光度特征分析能力。该框架在美国宇航局"黎明号"任务拍摄的真实影像数据上得到验证，实验证明相较于传统球谐参数化方法，本框架在渲染效果与表面重建精度方面均表现出显著优势。

---

### 6. CEI-3D: Collaborative Explicit-Implicit 3D Reconstruction for Realistic and Fine-Grained Object Editing

- **作者**: Yue Shi, Rui Shi, Yuxuan Xiong, Bingbing Ni, Wenjun Zhang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.11810v1)
- **发表日期**: 2026-03-12
- **匹配关键词**: 3d reconstruction, 3D reconstruction, implicit representation
- **arXiv**: [2603.11810v1](http://arxiv.org/abs/2603.11810v1)
- **📥 PDF**: 已下载至本地 (`2603.11810v1_CEI-3D_Collaborative_Explicit-Implicit_3D_Reconstruction_for_Realistic_and_Fine-Grained_Object_Editi.pdf`)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/shiyue001/CEI-3D.
- **中文摘要**: 现有三维编辑方法因其重建网络的高度集成特性，常导致编辑结果失真且不够精细。为解决这一挑战，本文提出CEI-3D——一种面向编辑的重建流程，旨在实现真实且细粒度的三维编辑。具体而言，我们设计了一种显隐协同的重建方法，通过隐式符号距离函数网络与差异化采样、局部可控的操控点集合共同表征目标物体。隐式网络提供平滑连续的几何先验，而显式操控点则实现局部控制，使全局三维结构与用户指定的局部编辑区域能够相互引导。为独立控制操控点的各项属性，我们设计了物理属性解耦模块，将操控点的颜色信息分解为独立的物理属性。该模块还提出双漫反射反照率网络，通过独立分支分别处理编辑区域与非编辑区域，从而避免编辑操作产生非预期的干扰。基于解耦属性后的显隐协同重建表示，我们进一步提出空间感知编辑模块，支持对相关操控点进行分区域调整。该模块采用基于跨视图传播的三维分割策略，帮助用户高效编辑目标部件的特定物理属性。在真实与合成数据集上的大量实验表明，相较于现有最优方法，本方法能以更短的编辑时间获得更真实、更精细的编辑效果。代码已开源：https://github.com/shiyue001/CEI-3D。

---

## 📌 Poster

*其他相关研究*

---

### 1. RADAR: Closed-Loop Robotic Data Generation via Semantic Planning and Autonomous Causal Environment Reset

- **作者**: Yongzhong Wang, Keyu Zhu, Yong Zhong, Liqiong Wang, Jinyu Yang, Feng Zheng
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.11811v1)
- **发表日期**: 2026-03-12
- **匹配关键词**: object manipulation
- **arXiv**: [2603.11811v1](http://arxiv.org/abs/2603.11811v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 大规模物理交互数据的获取作为现代机器人学习的关键前提，正因人工参与式采集模式的高成本与可扩展性限制而遭遇严重瓶颈。为突破此障碍，我们提出机器人鲁棒自主数据采集系统（RADAR）——一种完全自主的闭环数据生成引擎，彻底消除了采集周期中的人工干预。该系统通过四模块流水线实现认知负荷的合理分配：以2-5个三维人体演示作为几何先验，视觉语言模型首先通过精确的语义物体定位与技能检索，生成与场景相关的任务序列；随后，图神经网络策略通过上下文模仿学习将这些子任务转化为物理动作；执行完成后，视觉语言模型通过结构化视觉问答流程进行自动化成功评估；最后，为突破人工重置的瓶颈，有限状态机协调自主环境重置与非对称数据路由机制。该系统采用严格后进先出因果序列的正反向同步规划，能无缝恢复非结构化工作空间，并从执行故障中稳健恢复。这种持续的大脑-小脑协同将数据采集转化为自我维持的过程。大量实验验证了RADAR的卓越泛化能力：在仿真环境中，该框架在复杂长周期任务中达成高达90%的成功率，轻松解决传统基线方法性能趋近于零的挑战；在现实场景部署中，系统通过少量样本适应即可可靠执行多样化、高接触度的技能（如可变形物体操控），无需领域特定微调，为机器人数据采集提供了高度可扩展的范式。

---

### 2. HiSync: Spatio-Temporally Aligning Hand Motion from Wearable IMU and On-Robot Camera for Command Source Identification in Long-Range HRI

- **作者**: Chengwen Zhang, Chun Yu, Borong Zhuang, Haopeng Jin, Qingyang Wan, Zhuojun Li, Zhe He, Zhoutong Ye, Yu Mei, Chang Liu, Weinan Shi, Yuanchun Shi
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.11809v1)
- **发表日期**: 2026-03-12
- **匹配关键词**: HRI, human-robot interaction
- **arXiv**: [2603.11809v1](http://arxiv.org/abs/2603.11809v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 远距离人机交互（HRI）领域仍待深入探索。其中，指令源识别（CSI）——即确定指令发出者——因多用户场景及远距离导致的传感器模糊性而尤为困难。本文提出HiSync光学-惯性融合框架，通过将机器人搭载摄像机的光流数据与佩戴于手部的惯性测量单元（IMU）信号进行对齐，将手部运动作为绑定线索。我们首先通过用户调研（N=12）构建手势集，并在远距离多用户HRI场景中采集多模态指令手势数据集（N=38）。HiSync从摄像机与IMU数据中提取频域手部运动特征，通过训练的CSINet网络对IMU读数降噪、实现多模态时序对齐，并采用距离感知的多窗口融合机制计算细微自然手势的跨模态相似度，从而实现鲁棒的CSI。在34米范围内的三人交互场景中，HiSync达到92.32%的CSI准确率，较现有最优方法提升48.44%。该系统在真实机器人部署中得到验证。通过实现可靠自然的指令源识别，HiSync为公共空间人机交互提供了实用基础模块与设计指南。

---

### 3. Coupling Tensor Trains with Graph of Convex Sets: Effective Compression, Exploration, and Planning in the C-Space

- **作者**: Gerhard Reinerth, Riddhiman Laha, Marcello Romano
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.11658v1)
- **发表日期**: 2026-03-12
- **匹配关键词**: motion planning, exploration
- **arXiv**: [2603.11658v1](http://arxiv.org/abs/2603.11658v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出TANGO（张量与图优化）——一种创新的运动规划框架，该框架将基于张量的压缩技术与结构化图优化相结合，以实现高效且可扩展的轨迹生成。尽管基于优化的规划器（如凸集图GCS）为生成平滑最优轨迹提供了强大工具，但它们通常依赖于对高维构型空间进行预定义的凸特性描述，这一要求在通用机器人任务中往往难以实现。TANGO通过采用张量链分解技术，以压缩形式近似表示可行构型空间，从而实现对任务相关区域的快速发现与估计。这些区域随后被嵌入到类GCS结构中，支持在遵循系统约束与环境复杂性的前提下进行几何感知的运动规划。通过将张量压缩与结构化图推理相结合，TANGO实现了高效的几何感知运动规划，并为未来机器人系统中构型空间的更具表现力与可扩展性表征奠定了基础。在平面机器人与真实机器人上的严格仿真研究证实了该框架在有效压缩与生成更高质量轨迹方面的优势。

---

### 4. A Hybrid Neural-Assisted Unscented Kalman Filter for Unmanned Ground Vehicle Navigation

- **作者**: Gal Versano, Itzik Klein
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.11649v1)
- **发表日期**: 2026-03-12
- **匹配关键词**: autonomous navigation, navigation
- **arXiv**: [2603.11649v1](http://arxiv.org/abs/2603.11649v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 现代无人地面车辆的自主导航依赖于多种估计器来融合惯性传感器与全球导航卫星系统测量数据。然而，固定噪声协方差矩阵往往难以适应动态变化的实际环境条件。本研究提出一种混合估计框架，将经典状态估计原理与现代深度学习方法相结合。该框架不改变无迹卡尔曼滤波的基本方程，而是通过专门设计的深度神经网络直接从原始惯性和GNSS测量数据中预测过程噪声与测量噪声的不确定性。我们采用仿真到现实的训练策略，仅使用模拟数据进行模型训练。这种方法既能提供完美的地面真实数据，又避免了大量实际数据采集的负担。为评估所提方法并检验其泛化能力，我们采用来自三个数据集的160分钟测试集，每个数据集包含不同类型的车辆（越野车、乘用车和移动机器人）、惯性传感器、路面状况及环境条件。实验结果表明，在三个数据集上，相较于基于自适应模型的方法，本方法实现了12.7%的位置精度提升，从而为无人地面车辆导航任务提供了更具扩展性和鲁棒性的解决方案。

---

### 5. From Pets to Robots: MojiKit as a Data-Informed Toolkit for Affective HRI Design

- **作者**: Liwen He, Pingting Chen, Ziheng Tang, Yixiao Liu, Jihong Jeung, Teng Han, Xin Tong
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.11632v1)
- **发表日期**: 2026-03-12
- **匹配关键词**: HRI
- **arXiv**: [2603.11632v1](http://arxiv.org/abs/2603.11632v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 为动物仿生社交机器人设计情感行为常依赖直觉与个人经验，导致设计成果零散化。为提供更系统化的指导，我们首先对人类与宠物互动视频进行编码分析，通过文献研究和访谈验证洞察，并创建结构化参考卡片以映射宠物仿生情感交互的设计空间。在此基础上，我们开发了MojiKit工具包，该工具包整合了参考卡片、仿生机器人原型（MomoBot）以及行为控制工作室。通过对18名参与者开展协同创作工作坊评估，我们发现MojiKit帮助参与者基于自身宠物经验之外设计了35种情感交互模式，同时零代码工作室降低了技术门槛并增强了创作自主性。我们的贡献包括：为宠物仿生人机情感交互设计提供数据驱动的结构化资源；搭建连接参考资料与动手实践的集成化工具包；以及通过实证研究证明MojiKit如何帮助用户系统化地创造更丰富多元的情感机器人行为。

---

### 6. SVLL: Staged Vision-Language Learning for Physically Grounded Embodied Task Planning

- **作者**: Yuyuan Yang, Junkun Hong, Hongrong Wang, Honghao Cai, Xunpeng Ren, Ge Wang, Mingcong Lei, Shenhao Yan, Jiahao Yang, Chengsi Yao, Xi Li, Yiming Zhao, Yatong Han, Jinke Ren
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.11563v1)
- **发表日期**: 2026-03-12
- **匹配关键词**: affordance
- **arXiv**: [2603.11563v1](http://arxiv.org/abs/2603.11563v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: CODE
- **中文摘要**: 具身任务规划要求视觉语言模型生成既能在视觉上扎根又能在时间上保持因果连贯的动作序列。然而，现有训练范式面临一个关键权衡：联合端到端训练常导致过早的时间绑定，而标准强化学习方法则存在优化不稳定的问题。为弥合这一差距，我们提出了分阶段视觉语言学习（SVLL），这是一个用于实现稳健、物理扎根的具身规划的统一三阶段框架。在前两个阶段，SVLL将空间扎根与时间推理解耦，在引入序列动作历史之前建立稳健的视觉依赖。在最后阶段，我们发现了标准直接偏好优化（DPO）的一个关键局限——其纯粹相对性：仅优化获胜与失败轨迹间的偏好差距，而忽略最优路径的绝对似然约束，这常导致不安全或幻觉行为。为解决此问题，我们进一步引入偏置-DPO，这是一种新颖的对齐目标，通过显式最大化真实动作的似然性，同时惩罚过度自信的幻觉，从而注入对专家轨迹的归纳偏置。通过将策略锚定在专家流形上并缓解因果错位，由偏置-DPO驱动的SVLL确保严格遵循环境可供性，并有效抑制物理上不可能的捷径。最后，在交互式AI2-THOR基准测试和真实世界机器人部署中的大量实验表明，SVLL在任务成功率上优于最先进的开源模型（如Qwen2.5-VL-7B）和闭源模型（如GPT-4o、Gemini-2.0-flash），同时显著减少了物理约束违反情况。

---

### 7. CoViLLM: An Adaptive Human-Robot Collaborative Assembly Framework Using Large Language Models for Manufacturing

- **作者**: Jiabao Zhao, Jonghan Lim, Hongliang Li, Ilya Kovalenko
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.11461v1)
- **发表日期**: 2026-03-12
- **匹配关键词**: human-robot collaboration
- **arXiv**: [2603.11461v1](http://arxiv.org/abs/2603.11461v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 随着大规模定制需求的日益增长，依赖规则化操作的传统制造机器人缺乏适应定制化或新型产品变体的灵活性。人机协作通过结合人类的多变性和决策能力，已展现出提升系统适应性的潜力。然而，现有的人机协作框架通常依赖于预定义的感知-操作流程，限制了其为新产品装配自主生成任务规划的能力。本研究提出CoViLLM，一种自适应的人机协作装配框架，支持定制化及先前未见产品的装配。CoViLLM结合了基于深度摄像头的物体定位估计、用于识别新组件的人类操作员分类，以及基于自然语言指令进行装配任务规划的大型语言模型。该框架在NIST装配任务板上针对已知、定制化及新产品案例进行了验证。实验结果表明，所提出的框架通过将人机协作扩展到预定义产品和任务设置之外，实现了灵活的协作装配。

---

### 8. Enhancing Lightweight Vision Language Models through Group Competitive Learning for Socially Compliant Navigation

- **作者**: Xinyu Zhang, Atsushi Konno, Toshihiko Yamasaki, Ling Xiao
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.11447v1)
- **发表日期**: 2026-03-12
- **匹配关键词**: social navigation, robot navigation, navigation
- **arXiv**: [2603.11447v1](http://arxiv.org/abs/2603.11447v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 社交机器人导航需要场景语义与人类社交规范的高度融合。扩大视觉语言模型（VLM）规模通常能提升社交合规导航的推理与决策能力，但模型体量的增长会带来显著计算开销，限制了其在实时机器人部署中的适用性。反之，轻量级VLMs虽能实现高效推理，却在复杂社交环境中常表现出较弱的推理与决策性能。如何同时实现强推理能力与高效率仍是一个开放挑战。为弥合这一差距，我们提出群体竞争学习（GCL）策略，旨在增强轻量级VLMs的能力。该策略通过引入群体竞争目标（GCO）协调全局语义与分布正则化，并采用非对称群体优化（AGO）探索模型性能上限。在社交导航基准测试中的实证评估表明，GCL能显著提升VLM性能：具体而言，GCL使Qwen2.5-VL-3B学习模型和引导模型Qwen3-VL-4B分别达到0.968和0.914的F1分数，较原始监督微调（SFT）提升40%和12%。值得注意的是，在原始SFT下，3B模型初始性能落后于8B模型（F1分数0.692对0.755），而通过GCL优化后，3B模型反超8B基线模型达28%。这些结果表明，GCL为实际部署中同时实现高精度与计算效率提供了有效解决方案。

---

### 9. Separable neural architectures as a primitive for unified predictive and generative intelligence

- **作者**: Reza T. Batley, Apurba Sarker, Rajib Mostakim, Andrew Klichine, Sourav Saha
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.12244v1)
- **发表日期**: 2026-03-12
- **匹配关键词**: navigation
- **arXiv**: [2603.12244v1](http://arxiv.org/abs/2603.12244v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 跨物理、语言和感知领域的智能系统常呈现可分解结构，但现有建模通常采用单一神经架构，未能显式利用这种结构特征。可分离神经架构通过形式化表征类别，统一了加法模型、二次模型与张量分解神经模型。通过约束交互阶数与张量秩，该架构施加结构性归纳偏置，将高维映射分解为低元组件。可分离性并非系统固有属性，而常体现于表达系统所采用的坐标或表征形式。关键突破在于，这种坐标感知的构建方式揭示了混沌时空动力学与语言自回归之间的结构类比。通过将连续物理状态视为平滑可分离嵌入，该架构实现了混沌系统的分布建模。该方法既缓解了确定性算子产生的非物理漂移特性，又保持对离散序列的适用性。该架构的组合灵活性在四个领域得到验证：基于强化学习的自主航点导航、多功能微结构的逆向生成、湍流的分布建模以及神经语言建模。这些成果确立了可分离神经架构作为预测与生成智能的领域无关基元，能够统一确定性与分布性表征。

---

### 10. SceneAssistant: A Visual Feedback Agent for Open-Vocabulary 3D Scene Generation

- **作者**: Jun Luo, Jiaxiang Tang, Ruijie Lu, Gang Zeng
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.12238v1)
- **发表日期**: 2026-03-12
- **匹配关键词**: visual feedback
- **arXiv**: [2603.12238v1](http://arxiv.org/abs/2603.12238v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: GITHUB
  - 链接：https://github.com/ROUJINN/SceneAssistant
- **中文摘要**: 从自然语言生成三维场景对于数字内容创作具有重要价值。然而现有方法大多受限于特定领域或依赖预定义的空间关系，难以实现无约束的开放词汇三维场景合成。本文提出SceneAssistant——一种基于视觉反馈驱动的智能体，专为开放词汇三维场景生成而设计。该框架结合现代三维物体生成模型与视觉语言模型的空间推理规划能力。为实现开放词汇场景构建，我们为视觉语言模型提供了一套完整的原子操作指令集（如缩放、旋转、聚焦等）。在每次交互步骤中，视觉语言模型接收渲染后的视觉反馈并执行相应操作，通过迭代优化使场景空间布局更趋合理，同时提升与输入文本的契合度。实验结果表明，本方法能够生成多样化、开放词汇且高质量的三维场景。定性分析与定量人工评估均证实本方法优于现有技术。此外，用户可通过自然语言指令引导智能体对现有场景进行编辑。项目代码已开源：https://github.com/ROUJINN/SceneAssistant

---

### 11. Incremental Neural Network Verification via Learned Conflicts

- **作者**: Raya Elsaleh, Liam Davis, Haoze Wu, Guy Katz
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.12232v1)
- **发表日期**: 2026-03-12
- **匹配关键词**: exploration
- **arXiv**: [2603.12232v1](http://arxiv.org/abs/2603.12232v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 神经网络验证常作为大型分析流程的核心组成部分，这些流程会在同一网络上生成一系列紧密相关的验证查询。现有神经网络验证器通常独立处理每个查询，丢弃先前运行中获得的信息，导致对搜索空间中相同不可行区域的重复探索。本研究旨在通过减少这种冗余来加速验证过程。我们提出一种增量验证技术，能够在相关验证查询间复用已学习的冲突信息。该技术可应用于任何基于分支定界的神经网络验证器之上。在验证过程中，验证器会记录与学习到的激活相位不可行组合相对应的冲突，并在多次运行中保留这些信息。我们形式化定义了验证查询间的精化关系，并证明在精化条件下已学习的冲突保持有效，从而实现可靠的冲突继承。继承的冲突通过SAT求解器进行一致性检查和传播处理，使得在搜索过程中能够早期检测并剪枝不可行子问题。我们在Marabou验证器中实现了该技术，并在三个验证任务中进行了评估：局部鲁棒性半径确定、输入分割验证以及最小充分特征集提取。实验表明，增量式冲突复用能有效降低验证开销，相比非增量基线方法最高可获得$1.9\times$的加速效果。

---

### 12. Strategic Navigation or Stochastic Search? How Agents and Humans Reason Over Document Collections

- **作者**: Łukasz Borchmann, Jordy Van Landeghem, Michał Turski, Shreyansh Padarha, Ryan Othniel Kearns, Adam Mahdi, Niels Rogge, Clémentine Fourrier, Siwei Han, Huaxiu Yao, Artemis Llabrés, Yiming Xu, Dimosthenis Karatzas, Hao Zhang, Anupam Datta
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.12180v1)
- **发表日期**: 2026-03-12
- **匹配关键词**: navigation
- **arXiv**: [2603.12180v1](http://arxiv.org/abs/2603.12180v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 多模态智能体为自动化复杂的文档密集型工作流程提供了前景广阔的路径。然而一个关键问题依然存在：这些智能体展现的是真正的策略性推理能力，还是仅仅依靠随机试错搜索？为探究这一问题，我们推出了MADQA基准测试集，该数据集基于800份异构PDF文档构建，包含2,250道人工设计的问题。在经典测试理论指导下，我们通过最大化不同智能体能力水平的区分度来设计评估体系。为评估智能体行为，我们创新性地提出了衡量准确率与努力程度权衡关系的评估方案。运用该框架分析发现，虽然最优智能体在原始准确率上能媲美人类搜索者，但其成功解答的问题类型存在显著差异，且依赖暴力搜索来弥补策略规划能力的不足。这些智能体未能弥合与理论最优性能近20%的差距，持续陷入低效循环。我们公开数据集与评估工具包，以期推动从暴力检索向精准高效推理的范式转变。

---

### 13. O3N: Omnidirectional Open-Vocabulary Occupancy Prediction

- **作者**: Mengfei Duan, Hao Shi, Fei Teng, Guoqiang Zhao, Yuheng Zhang, Zhiyong Li, Kailun Yang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.12144v1)
- **发表日期**: 2026-03-12
- **匹配关键词**: exploration
- **arXiv**: [2603.12144v1](http://arxiv.org/abs/2603.12144v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: GITHUB, CODE
  - 链接：https://github.com/MengfeiD/O3N.
- **中文摘要**: 通过全向感知理解并重建三维世界，是自主智能体与具身智能发展的必然趋势。然而，现有三维占据预测方法受限于有限视角输入与预定义训练分布，难以适用于开放世界探索中需要全面、安全场景感知的具身智能体。为此，我们提出了O3N——首个纯视觉、端到端的全向开放词汇占据预测框架。O3N通过极坐标螺旋状态空间模块，将全向体素嵌入极坐标螺旋拓扑结构，实现连续空间表征与360°长程上下文建模。占据代价聚合模块引入统一体素空间几何监督与语义监督的原理性机制，确保重建几何与底层语义结构的一致性。此外，自然模态对齐模块构建了无梯度对齐路径，协调视觉特征、体素嵌入与文本语义，形成一致的“像素-体素-文本”表征三元组。在多个模型上的大量实验表明，我们的方法不仅在QuadOcc和Human360Occ基准测试中达到最先进性能，还展现出卓越的跨场景泛化能力与语义可扩展性，为通用三维世界建模开辟了新路径。源代码将在https://github.com/MengfeiD/O3N公开。

---

### 14. HATS: Hardness-Aware Trajectory Synthesis for GUI Agents

- **作者**: Rui Shao, Ruize Gao, Bin Xie, Yixing Li, Kaiwen Zhou, Shuai Wang, Weili Guan, Gongwei Chen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.12138v1)
- **发表日期**: 2026-03-12
- **匹配关键词**: exploration
- **arXiv**: [2603.12138v1](http://arxiv.org/abs/2603.12138v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 基于大型视觉语言模型（VLM）的图形用户界面（GUI）智能体在自动化数字任务方面展现出巨大潜力，这凸显了高质量轨迹数据对支持智能体有效训练的重要性。然而，现有的轨迹合成流程往往导致智能体难以泛化至简单交互之外的任务。我们认为这一局限源于对语义模糊性操作的忽视——这类操作的含义具有上下文依赖性、序列依赖性或视觉模糊性。此类操作对现实场景的鲁棒性至关重要，但在现有数据集中代表性不足且处理不当，导致任务指令与执行过程之间存在语义错位。为解决这些问题，我们提出了HATS（难度感知轨迹合成框架），旨在减轻语义模糊性带来的影响。我们将操作难度定义为与其相关的语义模糊程度，并开发了两个互补模块：（1）难度驱动探索模块，引导数据收集聚焦于模糊但信息丰富的交互；（2）对齐引导优化模块，迭代验证并修复指令与执行的对齐关系。这两个模块形成闭环运行：探索模块为优化模块提供具有挑战性的轨迹，而优化反馈则更新难度信号以指导后续探索。大量实验表明，使用HATS框架训练的智能体在各类基准GUI环境中均持续优于当前最先进的基线模型。

---

