# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-03-18 08:04

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 5/20 篇提供

**🌟 Highlight**: 17 篇 | **📌 Poster**: 3 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. Towards Generalizable Robotic Manipulation in Dynamic Environments

- **作者**: Heng Fang, Shangru Li, Shuhan Wang, Xuanyang Xi, Dingkang Liang, Xiang Bai
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.15620v1)
- **发表日期**: 2026-03-16
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2603.15620v1](http://arxiv.org/abs/2603.15620v1)
- **📥 PDF**: 已下载至本地 (`2603.15620v1_Towards_Generalizable_Robotic_Manipulation_in_Dynamic_Environments.pdf`)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/H-EmbodVis/DOMINO.
- **中文摘要**: 视觉-语言-动作（VLA）模型在静态操作任务中表现出色，但在涉及移动目标的动态环境中表现欠佳。这一性能差距主要源于动态操作数据集的稀缺性，以及主流VLA模型对单帧观测的依赖，限制了其时空推理能力。为解决这一问题，我们提出了DOMINO——一个面向可泛化动态操作的大规模数据集与基准测试平台，包含35项具有层次化复杂度的任务、超过11万条专家轨迹以及多维度的评估体系。通过系统性的实验，我们全面评估了现有VLA模型在动态任务上的表现，探索了提升动态感知能力的有效训练策略，并验证了动态数据的泛化价值。此外，我们提出了PUMA——一种具备动态感知能力的VLA架构。该架构通过融合以场景为中心的历史光流信息和专门设计的世界查询机制，隐式预测以物体为中心的未来状态，实现了历史感知与短期预测的耦合。实验结果表明，PUMA取得了最先进的性能，其成功率较基线模型绝对提升6.3%。同时，我们证明动态数据训练能够形成可迁移至静态任务的鲁棒时空表征。所有代码与数据均已开源：https://github.com/H-EmbodVis/DOMINO。

---

### 2. Look Before Acting: Enhancing Vision Foundation Representations for Vision-Language-Action Models

- **作者**: Yulin Luo, Hao Chen, Zhuangzhe Wu, Bowen Sui, Jiaming Liu, Chenyang Gu, Zhuoyang Liu, Qiuxuan Feng, Jiale Yu, Shuo Gu, Peng Jia, Pheng-Ann Heng, Shanghang Zhang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.15618v1)
- **发表日期**: 2026-03-16
- **匹配关键词**: vision-language-action, vision-language-action model, VLA
- **arXiv**: [2603.15618v1](http://arxiv.org/abs/2603.15618v1)
- **📥 PDF**: 已下载至本地 (`2603.15618v1_Look_Before_Acting_Enhancing_Vision_Foundation_Representations_for_Vision-Language-Action_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型近年来成为机器人操作领域的前沿范式，其动作预测的可靠性高度依赖于对语言指令引导下视觉观测的精准解析与融合。尽管近期研究致力于提升VLA模型的视觉处理能力，但多数方法将大语言模型主干视为黑箱，未能深入揭示视觉信息如何转化为动作生成的机制。为此，我们对多种动作生成范式下的VLA模型展开系统性分析，发现模型在动作生成过程中对视觉特征的敏感度随网络层数加深而逐层衰减。基于此发现，我们提出基于**视觉-语言混合变换器（VL-MoT）** 框架的**DeepVision-VLA**模型。该框架通过视觉基础模型与VLA主干网络间的共享注意力机制，将视觉专家模型的多层级特征注入VLA主干深层，从而增强复杂精细操作任务中的视觉表征能力。此外，我们提出**动作引导视觉剪枝（AGVP）** 方法，利用浅层注意力机制筛选任务相关视觉特征并剔除冗余信息，在最小计算开销下强化操作任务的关键视觉线索。实验表明，DeepVision-VLA在仿真与真实场景任务中分别以9.0%和7.5%的优势超越现有最优方法，为视觉增强型VLA模型的设计提供了新思路。

---

### 3. HSImul3R: Physics-in-the-Loop Reconstruction of Simulation-Ready Human-Scene Interactions

- **作者**: Yukang Cao, Haozhe Xie, Fangzhou Hong, Long Zhuo, Zhaoxi Chen, Liang Pan, Ziwei Liu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.15612v1)
- **发表日期**: 2026-03-16
- **匹配关键词**: 3D reconstruction, 3d reconstruction
- **arXiv**: [2603.15612v1](http://arxiv.org/abs/2603.15612v1)
- **📥 PDF**: 已下载至本地 (`2603.15612v1_HSImul3R_Physics-in-the-Loop_Reconstruction_of_Simulation-Ready_Human-Scene_Interactions.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出HSImul3R框架，这是一个从稀疏视角图像和单目视频等日常捕捉数据中，实现人-场景交互三维重建的统一框架。现有方法存在感知与仿真的鸿沟：视觉上合理的重建常违反物理约束，导致物理引擎中的不稳定及具身智能应用中的失效。为弥合这一差距，我们引入基于物理的双向优化流程，将物理仿真器作为主动监督器，联合优化人体动力学与场景几何。在正向过程中，我们采用场景导向强化学习方法，在运动保真度与接触稳定性的双重监督下优化人体运动。在逆向过程中，我们提出直接仿真奖励优化机制，利用重力稳定性与交互成功率的仿真反馈来优化场景几何。我们还构建了HSIBench新基准数据集，涵盖多样化物体与交互场景。大量实验表明，HSImul3R首次实现了稳定、可直接用于仿真的HSI重建，并能直接部署于真实世界人形机器人。

---

### 4. RoCo Challenge at AAAI 2026: Benchmarking Robotic Collaborative Manipulation for Assembly Towards Industrial Automation

- **作者**: Haichao Liu, Yuheng Zhou, Zhenyu Wu, Ziheng Ji, Ziyu Shan, Qianzhun Wang, Ruixuan Liu, Zhiyuan Yang, Yejun Gu, Shalman Khan, Shijun Yan, Jun Liu, Haiyue Zhu, Changliu Liu, Jianfei Yang, Jingbing Zhang, Ziwei Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.15469v1)
- **发表日期**: 2026-03-16
- **匹配关键词**: VLA
- **arXiv**: [2603.15469v1](http://arxiv.org/abs/2603.15469v1)
- **📥 PDF**: 已下载至本地 (`2603.15469v1_RoCo_Challenge_at_AAAI_2026_Benchmarking_Robotic_Collaborative_Manipulation_for_Assembly_Towards_Ind.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 具身人工智能（EAI）正在快速发展，逐步颠覆以往从孤立感知到集成连续行动的自主系统范式。这一转变对工业机器人操作具有重要意义，有望将人类从重复、危险的日常劳动中解放出来。为评估和推进这一能力，我们推出了机器人协同装配辅助（RoCo）挑战赛，并发布了面向仿真与真实世界装配操作的数据集。该挑战以人本制造为背景，聚焦高精度行星齿轮箱装配任务——这一现代工业中要求严苛且极具代表性的操作。基于我们在Isaac Sim中自主研发的数据采集、训练与评估系统，并采用双臂机器人进行实际部署，挑战赛分为两个阶段进行。仿真轮次定义了细粒度的任务阶段以进行逐步评分，以应对装配任务的长时程特性；真实世界轮次则使用实体齿轮箱组件和高质量遥操作数据集进行镜像评估。核心任务要求从零开始装配行星齿轮箱，包括安装三个行星齿轮、一个太阳齿轮和一个齿圈。本次挑战赛吸引了来自10多个国家的60多支团队、170余名参与者，产生了高效的解决方案，其中最突出的是ARC-VLA和RoboCola。结果表明，面向长时程多任务学习的双模型框架效果显著，而策略性利用故障恢复课程数据是实现成功部署的关键洞见。本报告概述了竞赛设置、评估方法、关键发现以及工业EAI的未来方向。我们的数据集、CAD文件、代码和评估结果可在以下网址获取：https://rocochallenge.github.io/RoCo2026/。

---

### 5. MA-VLCM: A Vision Language Critic Model for Value Estimation of Policies in Multi-Agent Team Settings

- **作者**: Shahil Shaik, Aditya Parameshwaran, Anshul Nayak, Jonathon M. Smereka, Yue Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.15418v1)
- **发表日期**: 2026-03-16
- **匹配关键词**: vision-language-action, vision-language-action model, VLA
- **arXiv**: [2603.15418v1](http://arxiv.org/abs/2603.15418v1)
- **📥 PDF**: 已下载至本地 (`2603.15418v1_MA-VLCM_A_Vision_Language_Critic_Model_for_Value_Estimation_of_Policies_in_Multi-Agent_Team_Settings.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 多智能体强化学习（MARL）通常依赖集中式评价器来估计价值函数。然而，从头开始学习这样的评价器样本效率极低，且往往缺乏跨环境的泛化能力。与此同时，基于互联网规模数据训练的大型视觉-语言-动作模型（VLA）展现出强大的多模态推理和零样本泛化能力，但直接将其部署于机器人执行任务仍面临计算成本过高的问题，特别是在具有异构形态和资源约束的多机器人系统中。为应对这些挑战，我们提出多智能体视觉-语言评价模型（MA-VLCM），该框架使用经过微调的预训练视觉-语言模型替代MARL中的学习型集中评价器，用以评估多智能体行为。MA-VLCM作为集中式评价器，其条件输入包括自然语言任务描述、视觉轨迹观测以及结构化多智能体状态信息。通过在策略优化过程中消除评价器学习环节，我们的方法显著提升了样本效率，同时生成适用于资源受限机器人的紧凑执行策略。实验结果表明，在多智能体团队场景中，采用不同VLM骨干的模型在分布内与分布外情境下均展现出良好的零样本回报估计能力。

---

### 6. HapticVLA: Contact-Rich Manipulation via Vision-Language-Action Model without Inference-Time Tactile Sensing

- **作者**: Konstantin Gubernatorov, Mikhail Sannikov, Ilya Mikhalchuk, Egor Kuznetsov, Makar Artemov, Ogunwoye Faith Ouwatobi, Marcelino Fernando, Artem Asanov, Ziang Guo, Dzmitry Tsetserukou
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.15257v1)
- **发表日期**: 2026-03-16
- **匹配关键词**: vision-language-action, vision-language-action model, contact-rich manipulation, VLA
- **arXiv**: [2603.15257v1](http://arxiv.org/abs/2603.15257v1)
- **📥 PDF**: 已下载至本地 (`2603.15257v1_HapticVLA_Contact-Rich_Manipulation_via_Vision-Language-Action_Model_without_Inference-Time_Tactile_.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 触觉感知是视觉-语言-动作架构的关键能力，它使机器人能够在接触密集型任务中实现灵巧且安全的操作。然而，依赖专用触觉硬件会增加成本并降低跨机器人平台的可复现性。我们认为触觉感知操作可通过离线学习实现，并在推理阶段无需依赖直接触觉反馈即可部署。为此，我们提出HapticVLA模型，其包含两个紧密耦合的阶段：安全感知奖励加权流匹配与触觉蒸馏。安全感知奖励加权流匹配训练一个流匹配动作专家模型，该模型融合了预计算的安全感知触觉奖励机制，对过度抓握力和次优抓取轨迹进行惩罚。触觉蒸馏进一步将这种触觉感知能力迁移至传统视觉-语言-动作架构：我们从安全感知奖励加权流匹配教师模型中蒸馏出紧凑的触觉表征标记，并训练学生视觉-语言-动作模型通过视觉与状态模态预测该标记，从而在推理阶段无需搭载触觉传感器即可生成具备触觉感知能力的动作。该设计在保持视觉-语言-动作架构内接触密集型触觉感知推理能力的同时，消除了部署阶段对机载触觉传感器的依赖。在真实世界实验中，HapticVLA实现了86.7%的平均成功率，持续优于基线视觉-语言-动作模型——包括在推理阶段提供直接触觉反馈的版本。

---

### 7. NavGSim: High-Fidelity Gaussian Splatting Simulator for Large-Scale Navigation

- **作者**: Jiahang Liu, Yuanxing Duan, Jiazhao Zhang, Minghan Li, Shaoan Wang, Zhizheng Zhang, He Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.15186v1)
- **发表日期**: 2026-03-16
- **匹配关键词**: navigation, VLA, gaussian splatting, 3D gaussian splatting, vision-language-action
- **arXiv**: [2603.15186v1](http://arxiv.org/abs/2603.15186v1)
- **📥 PDF**: 已下载至本地 (`2603.15186v1_NavGSim_High-Fidelity_Gaussian_Splatting_Simulator_for_Large-Scale_Navigation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 为机器人模拟真实环境被广泛认为是机器人学习领域的关键挑战，尤其在渲染和物理仿真方面。这一挑战在导航任务中尤为突出，因为轨迹常常跨越多个房间甚至整层楼宇。本研究提出NavGSim——一个基于高斯泼溅技术的仿真器，专门用于生成高保真度的大规模导航环境。NavGSim建立在分层式3D高斯泼溅框架之上，能够在数百平方米的广阔场景中实现照片级真实感渲染。为模拟导航碰撞，我们创新性地引入基于高斯泼溅的切片技术，可直接从重建的高斯模型中提取可通行区域。此外，为提升易用性，我们提供了支持多GPU开发的完整NavGSim应用程序接口，包含自定义场景重建、机器人配置、策略训练与评估等全套工具。为验证NavGSim的有效性，我们使用在该仿真器中采集的轨迹训练视觉-语言-动作模型，并在仿真环境与真实场景中评估其性能。实验结果表明，NavGSim显著增强了VLA模型对场景的理解能力，使策略能够有效处理多样化的导航查询。

---

### 8. ForceVLA2: Unleashing Hybrid Force-Position Control with Force Awareness for Contact-Rich Manipulation

- **作者**: Yang Li, Zhaxizhuoma, Hongru Jiang, Junjie Xia, Hongquan Zhang, Jinda Du, Yunsong Zhou, Jia Zeng, Ce Hao, Jieji Ren, Qiaojun Yu, Cewu Lu, Yu Qiao, Jiangmiao Pang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.15169v1)
- **发表日期**: 2026-03-16
- **匹配关键词**: vision-language-action, contact-rich manipulation, VLA
- **arXiv**: [2603.15169v1](http://arxiv.org/abs/2603.15169v1)
- **📥 PDF**: 已下载至本地 (`2603.15169v1_ForceVLA2_Unleashing_Hybrid_Force-Position_Control_with_Force_Awareness_for_Contact-Rich_Manipulatio.pdf`)
- **🔓 开源**: PROJECT_PAGE
- **中文摘要**: 面向接触密集型操作的具身智能主要依赖于位置控制，而交互力的显式感知与调节机制仍待深入探索，这限制了实际任务中的稳定性、精度与鲁棒性。我们提出ForceVLA2——一种端到端的视觉-语言-动作框架，为机器人配备混合力-位置控制与显式力感知能力。该框架通过向视觉语言模型专家引入基于力的提示，构建跨阶段的力感知任务概念，并在动作专家中采用跨尺度混合专家机制，自适应地将这些概念与实时交互力融合，实现闭环混合力-位置调节。为支持学习与评估，我们构建了ForceVLA2数据集，涵盖擦拭、按压、装配等5类接触密集型任务的1000条轨迹数据，包含多视角图像、任务提示、本体感知状态及力信号。大量实验表明，ForceVLA2在接触密集型操作中显著提升了成功率与可靠性：在5项任务中分别超越pi0和pi0.5模型48.0%和35.0%，有效缓解了机械臂过载、接触失稳等常见故障模式，从而积极推动了视觉语言动作模型中力感知交互物理智能的发展。项目页面详见https://sites.google.com/view/force-vla2/home。

---

### 9. Master Micro Residual Correction with Adaptive Tactile Fusion and Force-Mixed Control for Contact-Rich Manipulation

- **作者**: Xingting Li, Yifan Xie, Han Liu, Wei Hou, Guangyu Chen, Shoujie Li, Wenbo Ding
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.15152v1)
- **发表日期**: 2026-03-16
- **匹配关键词**: diffusion policy, contact-rich manipulation
- **arXiv**: [2603.15152v1](http://arxiv.org/abs/2603.15152v1)
- **📥 PDF**: 已下载至本地 (`2603.15152v1_Master_Micro_Residual_Correction_with_Adaptive_Tactile_Fusion_and_Force-Mixed_Control_for_Contact-Ri.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 机器人接触丰富且精细的操作仍面临重大挑战，这源于复杂的交互动力学与多时间尺度控制的竞争性需求。当前视觉模仿学习方法虽擅长长时程规划，却常难以感知摩擦变化或初始滑动等关键交互线索，且在全局任务连贯性与局部反应反馈间难以平衡。为解决这些问题，我们提出M2-ResiPolicy——一种新型主从式残差控制架构，将高层动作引导与低层修正协同整合。该框架包含以10赫兹运行的主引导策略，其通过扩散模型主干生成时序一致的动作块，并采用触觉强度驱动的自适应融合机制动态调节视觉与触觉的感知权重。同时，高频（60赫兹）微残差校正器利用轻量级GRU网络，基于工具中心点力矩反馈提供实时动作补偿。该策略进一步与力混合PBIC执行层集成，有效调控接触力以确保交互安全。在易碎物体抓取、精密插接等多个高要求任务中的实验表明，M2-ResiPolicy显著优于标准扩散策略及前沿反应式扩散策略，在芯片抓取任务中实现93%的无损成功率，并展现出更优的力控稳定性。

---

### 10. AnoleVLA: Lightweight Vision-Language-Action Model with Deep State Space Models for Mobile Manipulation

- **作者**: Yusuke Takagi, Motonari Kambara, Daichi Yashima, Koki Seno, Kento Tokura, Komei Sugiura
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.15046v1)
- **发表日期**: 2026-03-16
- **匹配关键词**: vision-language-action model, vision-language-action, mobile manipulation, VLA
- **arXiv**: [2603.15046v1](http://arxiv.org/abs/2603.15046v1)
- **📥 PDF**: 已下载至本地 (`2603.15046v1_AnoleVLA_Lightweight_Vision-Language-Action_Model_with_Deep_State_Space_Models_for_Mobile_Manipulati.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 本研究聚焦于语言引导的机器人操作问题，即要求机器人基于视觉观察和自然语言指令完成对各类物体的操作。这项任务对于在人类环境中运行的服务机器人至关重要，需要兼顾安全性、效率及任务层面的通用性。尽管视觉-语言-动作模型（VLA）在此类任务中展现出优异性能，但由于标准Transformer主干网络的计算成本较高，其在资源受限环境中的部署仍面临挑战。为突破这一限制，我们提出AnoleVLA——一种采用深度状态空间模型高效处理多模态序列的轻量化VLA。该模型凭借其轻量级架构与快速序列状态建模能力，能够高效处理视觉与文本输入，从而生成精准的机器人运动轨迹。我们在仿真与物理实验中对该方法进行了全面评估。值得注意的是，在真实环境测试中，AnoleVLA的任务成功率较代表性大规模VLA模型提升21个百分点，同时推理速度提升约三倍。

---

### 11. ReMAP-DP: Reprojected Multi-view Aligned PointMaps for Diffusion Policy

- **作者**: Xinzhang Yang, Renjun Wu, Jinyan Liu, Xuesong Li
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.14977v1)
- **发表日期**: 2026-03-16
- **匹配关键词**: diffusion policy
- **arXiv**: [2603.14977v1](http://arxiv.org/abs/2603.14977v1)
- **📥 PDF**: 已下载至本地 (`2603.14977v1_ReMAP-DP_Reprojected_Multi-view_Aligned_PointMaps_for_Diffusion_Policy.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://icr-lab.github.io/ReMAP-DP/
- **中文摘要**: 基于二维视觉表征构建的通用机器人策略在语义推理方面表现出色，但本质上缺乏高精度任务所需的显式三维空间感知能力。现有三维集成方法因稀疏点云的结构不规则性及多视角正交渲染引入的几何形变而难以弥合这一鸿沟。为突破这些障碍，我们提出ReMAP-DP框架——该创新方案将标准化透视重投影与结构感知双流扩散策略深度融合。通过将重投影视图与像素对齐的点云地图耦合，我们的双流架构利用可学习的模态嵌入融合冻结语义特征与显式几何描述符，确保精确的隐式块级对齐。在仿真与真实环境中的大量实验表明，ReMAP-DP在多样化操作任务中均展现出卓越性能：在RoboTwin 2.0平台上实现59.3%的平均成功率，较DP3基线提升6.6%；在ManiSkill 3环境中，针对几何复杂度高的堆叠立方体任务，本方法较DP3提升28%。此外，ReMAP-DP展现出卓越的现实世界鲁棒性，仅需少量演示即可实现高精度动态操作，并具有优越的数据效率。项目页面详见：https://icr-lab.github.io/ReMAP-DP/

---

### 12. Exploring the dynamic properties and motion reproducibility of a small upper-body humanoid robot with 13-DOF pneumatic actuation for data-driven control

- **作者**: Hiroshi Atsuta, Hisashi Ishihara, Minoru Asada
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.14787v1)
- **发表日期**: 2026-03-16
- **匹配关键词**: human-robot interaction
- **arXiv**: [2603.14787v1](http://arxiv.org/abs/2603.14787v1)
- **📥 PDF**: 已下载至本地 (`2603.14787v1_Exploring_the_dynamic_properties_and_motion_reproducibility_of_a_small_upper-body_humanoid_robot_wit.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 具有高自由度的气动仿人机器人在人机物理交互领域展现出巨大潜力。然而，由于气动执行器固有的非线性特性，其精确控制面临挑战。本文介绍了一款紧凑型13自由度上半身仿人机器人的研发过程。为评估有效控制器的可行性，我们首先研究了系统的关键动态特性（如驱动时间延迟），并确认该系统具有高度可复现的行为特征。基于这种可复现性，我们为4自由度手臂子系统设计了一种基于多层感知器的数据驱动控制器，该控制器具备显式时间延迟补偿功能。通过随机运动数据训练神经网络，使其能够生成压力指令以跟踪任意轨迹。与传统PID控制器的对比实验表明，该数据驱动控制器在轨迹跟踪性能上表现更优，凸显了数据驱动方法在控制复杂高自由度气动机器人方面的应用潜力。

---

### 13. CyboRacket: A Perception-to-Action Framework for Humanoid Racket Sports

- **作者**: Peng Ren, Chuan Qi, Haoyang Ge, Qiyuan Su, Xuguo He, Cong Huang, Pei Chi, Jiang Zhao, Kai Chen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.14605v1)
- **发表日期**: 2026-03-15
- **匹配关键词**: visual tracking, perception-action
- **arXiv**: [2603.14605v1](http://arxiv.org/abs/2603.14605v1)
- **📥 PDF**: 已下载至本地 (`2603.14605v1_CyboRacket_A_Perception-to-Action_Framework_for_Humanoid_Racket_Sports.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 动态球类交互任务对机器人而言仍具挑战性，因其需要在有限反应时间内实现感知与动作的紧密耦合。这一挑战在人形机器人球拍运动中尤为突出，成功拦截需要精准的视觉追踪、轨迹预测、协调步态以及稳定的全身击打动作。现有机器人球拍运动系统通常依赖外部动作捕捉进行状态估计，或采用需在不同任务与平台间重新训练的任务专用底层控制器。我们提出CyboRacket——一个面向人形机器人球拍运动的分层感知-动作框架，该框架集成了机载视觉感知、基于物理的轨迹预测及大规模预训练的全身控制系统。该框架通过机载摄像头追踪来球，预测其未来轨迹，并将估算的拦截状态转换为目标末端执行器与基座运动指令，由Unitree G1人形机器人搭载的SONIC系统执行全身动作。我们在基于视觉的人形机器人网球击打任务中评估了该框架。实验结果表明，系统能实现实时视觉追踪、轨迹预测，并仅通过机载传感成功完成击打动作。

---

### 14. EAAE: Energy-Aware Autonomous Exploration for UAVs in Unknown 3D Environments

- **作者**: Jacob Elskamp, Moji Shi, Leonard Bauersfeld, Davide Scaramuzza, Marija Popović ⭐
  - **高亮作者**: Davide Scaramuzza
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.15604v1)
- **发表日期**: 2026-03-16
- **匹配关键词**: exploration
- **arXiv**: [2603.15604v1](http://arxiv.org/abs/2603.15604v1)
- **📥 PDF**: 已下载至本地 (`2603.15604v1_EAAE_Energy-Aware_Autonomous_Exploration_for_UAVs_in_Unknown_3D_Environments.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 电池驱动的多旋翼无人机能够快速测绘未知环境，但其任务性能往往受限于能量而非单纯几何因素。传统的以覆盖范围或时间为优化目标的探索策略可能因高机动性轨迹而浪费能量。本文针对多旋翼无人机在初始未知环境中的能量感知自主三维探索问题展开研究，提出能量感知自主探索框架——一种基于前沿探测的模块化系统，将能量作为前沿选择过程中的显式决策变量。该框架通过将探测前沿聚类为视觉一致性区域，为信息量最大的集群规划动态可行的候选轨迹，并利用离线功率估计循环预测执行能耗。随后通过双层规划架构，在保证探索进度的同时最小化预测轨迹能耗，从而选定安全执行的最优目标。我们在完整探索流程中，基于旋翼转速功率模型，在复杂度递增的模拟三维环境中对该框架进行评估。与典型的基于距离和基于信息增益的前沿基准方法相比，该框架在保持竞争性探索时间与可比地图质量的同时，持续降低总能耗，为前沿探索提供了可直接部署的能量感知解决方案。

---

### 15. Trajectory-Diversity-Driven Robust Vision-and-Language Navigation

- **作者**: Jiangyang Li, Cong Wan, SongLin Dong, Chenhao Ding, Qiang Wang, Zhiheng Ma, Yihong Gong
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.15370v1)
- **发表日期**: 2026-03-16
- **匹配关键词**: navigation, vision-and-language navigation, VLN
- **arXiv**: [2603.15370v1](http://arxiv.org/abs/2603.15370v1)
- **📥 PDF**: 已下载至本地 (`2603.15370v1_Trajectory-Diversity-Driven_Robust_Vision-and-Language_Navigation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉与语言导航任务要求智能体根据自然语言指令在逼真环境中进行导航。现有方法主要依赖模仿学习，存在泛化能力有限、对执行扰动鲁棒性差的问题。本文提出NavGRPO强化学习框架，通过群体相对策略优化学习目标导向的导航策略。该方法通过探索多样化轨迹并利用组内性能比较进行优化，使智能体能够识别专家路径之外的有效策略，且无需额外价值网络支持。基于ScaleVLN构建的NavGRPO在R2R和REVERIE基准测试中展现出卓越的鲁棒性，在未见环境中分别实现SPL指标+3.0%和+1.71%的提升。在极端早期扰动条件下，相较基线方法获得+14.89%的SPL增益，证实目标导向的强化学习训练能构建显著更鲁棒的导航策略。代码与模型将开源发布。

---

### 16. IRIS: Intersection-aware Ray-based Implicit Editable Scenes

- **作者**: Grzegorz Wilczyński, Mikołaj Zieliński, Krzysztof Byrski, Joanna Waczyńska, Dominik Belter, Przemysław Spurek
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.15368v1)
- **发表日期**: 2026-03-16
- **匹配关键词**: 3D gaussian splatting, neural radiance field, gaussian splatting
- **arXiv**: [2603.15368v1](http://arxiv.org/abs/2603.15368v1)
- **📥 PDF**: 已下载至本地 (`2603.15368v1_IRIS_Intersection-aware_Ray-based_Implicit_Editable_Scenes.pdf`)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/gwilczynski95/iris.
- **中文摘要**: 神经辐射场能够实现高保真的场景表示，但其训练和渲染成本高昂，而三维高斯泼溅技术虽能提供实时性能且实证效果显著，却存在明显不足。近期研究尝试结合两者优势，利用高斯分布作为代理来指导神经场评估，但仍面临严重的计算效率问题。这类方法通常依赖随机体素采样进行特征聚合，严重制约了渲染性能。为解决这一难题，本文提出名为IRIS（基于交点的射线式隐式可编辑场景）的创新框架，旨在实现高效交互式场景编辑。为突破传统光线步进法的局限，该框架采用解析采样策略，精确识别光线与场景基元之间的交点，从而有效避免无效空间处理。此外，针对空间邻近查找的计算瓶颈，研究引入了沿射线直接操作的连续特征聚合机制。通过对排序交点的潜在属性进行插值计算，该方法绕过了昂贵的三维搜索过程，在确保几何一致性的同时，实现了高保真实时渲染与灵活的形状编辑功能。代码开源地址：https://github.com/gwilczynski95/iris。

---

### 17. MeMix: Writing Less, Remembering More for Streaming 3D Reconstruction

- **作者**: Jiacheng Dong, Huan Li, Sicheng Zhou, Wenhao Hu, Weili Xu, Yan Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.15330v1)
- **发表日期**: 2026-03-16
- **匹配关键词**: 3D reconstruction, 3d reconstruction
- **arXiv**: [2603.15330v1](http://arxiv.org/abs/2603.15330v1)
- **📥 PDF**: 已下载至本地 (`2603.15330v1_MeMix_Writing_Less,_Remembering_More_for_Streaming_3D_Reconstruction.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 三维重建是三维视觉中的基础任务，也是空间智能的核心能力。特别是流式三维重建对于实时空间感知至关重要，然而现有的循环在线模型常因状态漂移和遗忘问题在长序列上出现渐进性退化，这促使了推理阶段补救方法的研究。我们提出MeMix——一种无需训练、即插即用的模块，通过将循环状态重构为记忆混合体来提升流式重建性能。MeMix将状态划分为多个独立记忆块，仅更新对齐度最低的记忆块，同时严格保留其他记忆块。这种选择性更新机制在保持O(1)推理内存的同时缓解了灾难性遗忘问题，且无需微调或额外可学习参数，可直接应用于现有循环重建模型。在标准基准测试集（ScanNet、7-Scenes、KITTI等）上，采用相同骨干网络和推理设置时，MeMix在7-Scenes数据集300-500帧流上平均降低重建完整性误差15.3%（最高达40.0%）。代码已开源：https://dongjiacheng06.github.io/MeMix/

---

## 📌 Poster

*其他相关研究*

---

### 1. Perception-Aware Autonomous Exploration in Feature-Limited Environments

- **作者**: Moji Shi, Rajitha de Silva, Hang Yu, Riccardo Polvara, Marija Popović
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.15605v1)
- **发表日期**: 2026-03-16
- **匹配关键词**: exploration
- **arXiv**: [2603.15605v1](http://arxiv.org/abs/2603.15605v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 未知环境中的自主探索通常依赖于机载状态估计进行定位与建图。现有探索方法主要追求覆盖效率最大化，但往往忽视视觉惯性里程计（VIO）性能高度依赖稳定视觉特征的可用性。这导致探索策略可能驱动机器人进入特征稀疏区域，造成跟踪性能下降、里程计漂移、地图失真乃至任务失败。我们提出一种面向配备双目相机的无人机分层感知探索框架，将探索进程与特征可观测性进行显式耦合。该方法（1）通过全局特征地图将候选前沿点与预期特征质量关联，优先选择视觉信息丰富的子目标；（2）沿规划路径优化连续偏航轨迹以维持稳定特征跟踪。我们在不同纹理等级的环境仿真及大面积无纹理墙面的真实室内场景中评估本方法。相较于忽略特征质量和/或不优化连续偏航的基准方法，本方法能保持更可靠的特征跟踪，降低里程计漂移，在里程计误差超过设定阈值前平均实现30%更高的环境覆盖率。

---

### 2. End-to-End Dexterous Grasp Learning from Single-View Point Clouds via a Multi-Object Scene Dataset

- **作者**: Tao Geng, Dapeng Yang, Ziwei Liu, Le Zhang, Le Qi, WangYang Li, Yi Ren, Shan Luo, Fenglei Ni
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.15410v1)
- **发表日期**: 2026-03-16
- **匹配关键词**: grasp synthesis, dexterous grasping
- **arXiv**: [2603.15410v1](http://arxiv.org/abs/2603.15410v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: GITHUB
  - 链接：https://github.com/4taotao8/DGS-Net.
- **中文摘要**: 多物体场景中的灵巧抓取是机器人操作领域的一项基础性挑战。当前主流的抓取数据集主要集中于单物体场景和预定义的抓取构型，往往忽略了环境干扰因素及灵巧预抓取姿态的建模，从而限制了其在真实场景中的泛化能力。为此，我们提出DGS-Net——一种能够从多物体场景的单视角点云中学习密集抓取构型的端到端抓取预测网络。此外，我们提出了一种两阶段抓取数据生成策略，从密集单物体抓取合成逐步推进到密集场景级抓取生成。我们的数据集包含307个物体、240个多物体场景以及超过35万个经过验证的抓取样本。通过显式建模抓取偏移量与预抓取构型，该数据集为灵巧抓取学习提供了更鲁棒、更精确的监督信息。实验结果表明，DGS-Net在仿真环境中达到88.63%的抓取成功率，在真实机器人平台上达到78.98%的成功率，同时展现出更低的穿透率（平均穿透深度0.375毫米，穿透体积559.45立方毫米），其性能优于现有方法，表现出强大的有效性与泛化能力。我们的数据集已发布于https://github.com/4taotao8/DGS-Net。

---

### 3. Pointing-Based Object Recognition

- **作者**: Lukáš Hajdúch, Viktor Kocur
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.15403v1)
- **发表日期**: 2026-03-16
- **匹配关键词**: human-robot interaction
- **arXiv**: [2603.15403v1](http://arxiv.org/abs/2603.15403v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 本文提出了一种基于RGB图像识别人类指向手势目标物体的完整流程。随着人机交互向更直观的界面发展，识别非语言交流目标的能力变得至关重要。我们提出的系统整合了多种现有先进方法，包括目标检测、人体姿态估计、单目深度估计以及视觉语言模型。我们评估了从单张图像重建的三维空间信息的影响，以及图像描述模型在修正分类错误方面的效用。在自定义数据集上的实验结果表明，融入深度信息能显著提升目标识别性能，特别是在物体重叠的复杂场景中。该方法的模块化特性使其能够在缺乏专用深度传感器的环境中部署。

---

