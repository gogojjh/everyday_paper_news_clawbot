# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-02-26 08:02

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 4/20 篇提供

**🌟 Highlight**: 6 篇 | **📌 Poster**: 14 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. Efficient Hierarchical Any-Angle Path Planning on Multi-Resolution 3D Grids

- **作者**: Victor Reijgwart, Cesar Cadena, Roland Siegwart, Lionel Ott ⭐
  - **高亮作者**: Cesar Cadena, Roland Siegwart
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.21174v1)
- **发表日期**: 2026-02-24
- **匹配关键词**: navigation, path planning
- **arXiv**: [2602.21174v1](http://arxiv.org/abs/2602.21174v1)
- **📥 PDF**: 已下载至本地 (`2602.21174v1_Efficient_Hierarchical_Any-Angle_Path_Planning_on_Multi-Resolution_3D_Grids.pdf`)
- **🔓 开源**: CODE
- **中文摘要**: 分层多分辨率体素映射方法因其能高效捕捉环境占用与连通性信息，被广泛应用于大型复杂场景的建模。然而，当前主流的路径规划方法（如采样法和轨迹优化法）并未充分利用这种显式连通信息，而基于搜索的方法（如A*算法）在大规模高分辨率地图中面临可扩展性问题。在许多应用场景中，欧几里得最短路径构成导航系统的基础。针对这类需求，任意角规划方法通过连接障碍物顶点形成直线路径段，为实现最优路径提供了简洁高效的解决方案。本文提出一种兼具任意角规划器最优性与完备性的新方法，通过利用多分辨率表征克服了基于搜索方法常见的计算可处理性问题。在真实与合成环境中的大量实验表明，所提方法在求解质量与速度上均表现优异，甚至超越了基于采样的规划方法。本框架已开源，以促进机器人学与规划领域基于本研究开展进一步探索。

---

### 2. Event-Aided Sharp Radiance Field Reconstruction for Fast-Flying Drones

- **作者**: Rong Zou, Marco Cannici, Davide Scaramuzza ⭐
  - **高亮作者**: Davide Scaramuzza
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.21101v1)
- **发表日期**: 2026-02-24
- **匹配关键词**: exploration
- **arXiv**: [2602.21101v1](http://arxiv.org/abs/2602.21101v1)
- **📥 PDF**: 已下载至本地 (`2602.21101v1_Event-Aided_Sharp_Radiance_Field_Reconstruction_for_Fast-Flying_Drones.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 在电池续航有限条件下，高速飞行的空中机器人有望实现快速巡检，在基础设施检测、地形勘探和搜救等领域具有直接应用价值。然而，高速飞行会导致图像产生严重运动模糊，并引发位姿估计的显著漂移与噪声，这使得神经辐射场（NeRF）的稠密三维重建面临特殊挑战，因为该方法对此类退化现象极为敏感。本研究提出一种统一框架，通过融合异步事件流与运动模糊图像帧，实现从敏捷无人机飞行中重建高保真辐射场。通过将事件-图像融合嵌入NeRF优化过程，并联合利用事件与图像模态精化基于事件的视觉-惯性里程计先验信息，本方法无需地面真值监督即可重建清晰辐射场与精确相机轨迹。我们在合成数据与高速飞行无人机采集的真实场景序列上验证了该方法的有效性。即使在无人机高速动态飞行导致RGB图像帧严重运动模糊、位姿先验信息不可靠的情况下，本方法仍能重建高保真辐射场并保留精细场景细节，在真实数据上相比现有最优方法实现超过50%的性能提升。

---

### 3. Task-oriented grasping for dexterous robots using postural synergies and reinforcement learning

- **作者**: Dimitrios Dimou, José Santos-Victor, Plinio Moreno
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.20915v1)
- **发表日期**: 2026-02-24
- **匹配关键词**: exploration
- **arXiv**: [2602.20915v1](http://arxiv.org/abs/2602.20915v1)
- **📥 PDF**: 已下载至本地 (`2602.20915v1_Task-oriented_grasping_for_dexterous_robots_using_postural_synergies_and_reinforcement_learning.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 本文针对仿人机器人的任务导向抓取问题展开研究，重点探讨如何使其符合人类社交规范并满足特定任务需求。现有方法虽采用多种开环与闭环控制策略，但缺乏能够同时抓取多个物体并兼顾下游任务约束的端到端解决方案。我们提出的方法运用强化学习技术优化任务导向抓取过程，特别关注智能体的抓取后意图。通过从ContactPose数据集中提取人类抓取偏好，并基于变分自编码器训练手部协同模型以模仿参与者的抓取动作，我们构建了能够同时抓取多个物体且兼顾不同任务特定抓取后意图的智能体训练体系。通过将人类抓取行为的数据驱动洞察与强化学习提供的探索式学习相结合，我们能够开发出具备情境感知操作能力的仿人机器人，从而促进以人为中心环境中的协作交互。

---

### 4. Energy-Based Injury Protection Database: Including Shearing Contact Thresholds for Hand and Finger Using Porcine Surrogates

- **作者**: Robin Jeanne Kirschner, Anna Huber, Carina M. Micheler, Dirk Müller, Nader Rajaei, Rainer Burgkart, Sami Haddadin
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.20362v1)
- **发表日期**: 2026-02-23
- **匹配关键词**: human-robot interaction
- **arXiv**: [2602.20362v1](http://arxiv.org/abs/2602.20362v1)
- **📥 PDF**: 已下载至本地 (`2602.20362v1_Energy-Based_Injury_Protection_Database_Including_Shearing_Contact_Thresholds_for_Hand_and_Finger_Us.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 尽管机器人研究持续提出人机交互中的避碰策略，但受限环境与未来仿人系统的现实使得接触不可避免。为降低伤害风险，能量约束控制方法被广泛采用，通常依赖于EN ISO 10218-2:2025标准中钝器冲击数据推导的安全阈值。然而该数据集并未涵盖边缘或尖端碰撞场景。由于缺乏覆盖多样化接触场景、可扩展且具有临床依据的数据集，安全验证仍存在局限。先前研究通过评估不同几何形状下基于替代物的速度与质量限制（聚焦垂直冲击）已奠定基础。本研究通过纳入无约束碰撞中的剪切接触场景扩展了数据集，揭示碰撞角度对伤害结果具有显著影响。值得注意的是，无约束剪切接触造成的伤害少于垂直碰撞。通过重新评估所有既往猪替代物数据，我们建立了跨几何形状与接触类型的能量阈值，构建了首个基于能量的伤害防护数据库。这将推动开发具有实际意义的能量限制控制器，确保在广泛真实碰撞场景中的安全性。

---

### 5. To Move or Not to Move: Constraint-based Planning Enables Zero-Shot Generalization for Interactive Navigation

- **作者**: Apoorva Vashisth, Manav Kulshrestha, Pranav Bakshi, Damon Conover, Guillaume Sartoretti, Aniket Bera
- **单位**: Purdue University; Purdue University; IIT Kharagpur...
- **发表日期**: 2026-02-23
- **匹配关键词**: navigation, scene graph, active perception, visual navigation
- **arXiv**: [2602.20055v1](http://arxiv.org/abs/2602.20055v1)
- **📥 PDF**: 已下载至本地 (`2602.20055v1_To_Move_or_Not_to_Move_Constraint-based_Planning_Enables_Zero-Shot_Generalization_for_Interactive_Na.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉导航通常假设起点与目标之间存在至少一条无障碍路径，机器人需自主发现或规划该路径。然而在现实场景中，如家庭环境与仓库场所，杂物堆积可能完全阻断通行路线。针对此类情况，我们提出终身交互式导航问题：具备操作能力的移动机器人可通过移动杂物自主开辟路径，以完成序列化物体放置任务——每项任务需将指定物体（如闹钟、枕头）放置于目标物体（如餐桌、书桌、床铺）之上。为应对环境变化效应持续累积并产生长期影响的终身学习场景，我们提出一种基于大语言模型驱动、结合主动感知的约束规划框架。该框架使大语言模型能够对已发现物体与障碍物构成的场景图进行推理，决策移动何种物体、放置于何处、以及下一步探查哪些区域以获取任务相关信息。这种推理与主动感知的耦合机制，使智能体能够聚焦探索对任务完成具有预期贡献的区域，而非对环境进行穷尽式测绘。标准运动规划器随后执行相应的导航-抓取-放置或绕行序列，确保可靠的低层控制。在支持物理仿真的ProcTHOR-10k模拟器中评估表明，本方法在性能上超越非学习型与基于学习的基线模型。我们进一步通过真实硬件平台对方法进行了定性验证。

---

### 6. RU4D-SLAM: Reweighting Uncertainty in Gaussian Splatting SLAM for 4D Scene Reconstruction

- **作者**: Yangfan Zhao, Hanwei Zhang, Ke Huang, Qiufeng Wang, Zhenzhou Shao, Dengyu Wu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.20807v1)
- **发表日期**: 2026-02-24
- **匹配关键词**: localization and mapping
- **arXiv**: [2602.20807v1](http://arxiv.org/abs/2602.20807v1)
- **📥 PDF**: 已下载至本地 (`2602.20807v1_RU4D-SLAM_Reweighting_Uncertainty_in_Gaussian_Splatting_SLAM_for_4D_Scene_Reconstruction.pdf`)
- **🔓 开源**: CODE
  - 链接：https://ru4d-slam.github.io
- **中文摘要**: 将三维高斯泼溅与同步定位与建图技术相结合，因其能够在运动过程中实现连续的三维环境重建而日益受到关注。然而，现有方法在动态环境中面临挑战，尤其是运动物体会使三维重建复杂化，进而影响跟踪的可靠性。四维重建技术，特别是四维高斯泼溅的出现，为解决这些挑战提供了有前景的方向，但其在四维感知SLAM中的应用潜力尚未得到充分探索。基于此，我们提出了一种鲁棒且高效的框架——高斯泼溅SLAM中的不确定性重加权四维场景重建方法，该框架将时间因素引入空间三维表示，同时融合了场景变化的不确定性感知、模糊图像合成以及动态场景重建。我们通过集成运动模糊渲染来增强动态场景表示，并通过将原本为静态场景设计的逐像素不确定性建模扩展至模糊图像处理，从而提升不确定性感知跟踪能力。此外，我们提出了一种语义引导的逐像素不确定性重加权机制，用于动态场景中的不确定性估计，并引入可学习的不透明度权重以支持自适应的四维建图。在标准基准测试上的大量实验表明，我们的方法在轨迹精度和四维场景重建方面均显著优于现有先进方法，尤其是在包含运动物体和低质量输入的动态环境中。代码已开源：https://ru4d-slam.github.io

---

## 📌 Poster

*其他相关研究*

---

### 1. Surface-based Manipulation Using Tunable Compliant Porous-Elastic Soft Sensing

- **作者**: Gayatri Indukumar, Muhammad Awais, Diana Cafiso, Matteo Lo Preti, Lucia Beccai
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.21028v1)
- **发表日期**: 2026-02-24
- **匹配关键词**: object manipulation
- **arXiv**: [2602.21028v1](http://arxiv.org/abs/2602.21028v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 随着对能够轻柔、精确处理各类物体的软体机器人平台需求日益增长，现有基于表面的操控系统在精细操作方面仍缺乏必要的柔顺性与触觉反馈。本研究提出一种集成感应传感器的柔顺多孔弹性软体传感系统（COPESS），该系统具备自适应物体操控与局部感知能力。其核心设计采用可调谐晶格结构层，能够同步调节机械柔顺性与传感性能。通过调整晶格几何参数，系统刚度和传感器响应均可根据目标物体的不同力学特性进行定制。实验表明，仅通过简单调节晶格密度这一参数（从7%增至20%），即可显著改变系统灵敏度与操作力范围（分别实现约-23倍和9倍的调节幅度）。该研究为构建机械特性与感知性能协同优化的自适应传感表面提供了设计范式，实现了被动式可编程精细操控。

---

### 2. LST-SLAM: A Stereo Thermal SLAM System for Kilometer-Scale Dynamic Environments

- **作者**: Zeyu Jiang, Kuan Xu, Changhao Chen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.20925v1)
- **发表日期**: 2026-02-24
- **匹配关键词**: localization and mapping
- **arXiv**: [2602.20925v1](http://arxiv.org/abs/2602.20925v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 热成像相机在挑战性光照和天气条件下为机器人感知提供了强大潜力。然而，由于特征提取不可靠、运动跟踪不稳定以及全局位姿与地图构建不一致，热成像同步定位与建图（SLAM）仍面临困难，特别是在动态大规模户外环境中。为解决这些挑战，我们提出LST-SLAM——一种新型大规模立体热成像SLAM系统，能在复杂动态场景中实现鲁棒性能。该方法融合了自监督热特征学习、立体双级运动跟踪与几何位姿优化技术。我们还引入语义-几何混合约束机制，有效抑制缺乏帧间几何一致性的潜在动态特征。此外，我们开发了用于闭环检测的在线增量词袋模型，并结合全局位姿优化以缓解累积漂移。在千米级动态热成像数据集上的大量实验表明，LST-SLAM在鲁棒性和精度方面显著优于近期代表性SLAM系统，包括AirSLAM和DROID-SLAM。

---

### 3. SoK: Agentic Skills -- Beyond Tool Use in LLM Agents

- **作者**: Yanna Jiang, Delong Li, Haiyu Deng, Baihe Ma, Xu Wang, Qin Wang, Guangsheng Yu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.20867v1)
- **发表日期**: 2026-02-24
- **匹配关键词**: tool use
- **arXiv**: [2602.20867v1](http://arxiv.org/abs/2602.20867v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 智能体系统日益依赖可复用的程序化能力——即**智能体技能**——以可靠执行长周期工作流。这些能力是可调用模块，将程序性知识与显式适用条件、执行策略、终止标准及可复用接口封装在一起。与一次性计划或原子化工具调用不同，技能能够跨任务运行（且通常表现优异）。

本文系统梳理了技能层在全生命周期（发现、实践、提炼、存储、组合、评估与更新）中的运作机制，并提出两种互补的分类体系。其一是系统层面的**七种设计模式**，涵盖从元数据驱动的渐进式呈现、可执行代码技能，到自进化库与市场分发的实际技能封装与执行方式。其二是正交的**表征形式×作用域**分类法，描述技能的本质形态（自然语言、代码、策略、混合型）及其运行环境（网络、操作系统、软件工程、机器人领域）。

我们分析了基于技能的智能体在安全与治理层面的影响，涵盖供应链风险、通过技能载荷进行的提示注入攻击及信任分级执行机制，并以ClawHavoc攻击活动为案例进行实证研究——该活动中近1200个恶意技能渗透主流智能体市场，大规模窃取API密钥、加密货币钱包及浏览器凭证。我们进一步系统考察了确定性评估方法，基于近期基准测试证据表明：经精心设计的技能可显著提升智能体成功率，而自主生成的技能可能适得其反。最后，我们提出面向现实世界自主智能体构建稳健、可验证、可认证技能体系所面临的开放挑战。

---

### 4. IG-RFT: An Interaction-Guided RL Framework for VLA Models in Long-Horizon Robotic Manipulation

- **作者**: Zhian Su, Weijie Kong, Haonan Dong, Huixu Dong
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.20715v1)
- **发表日期**: 2026-02-24
- **匹配关键词**: exploration
- **arXiv**: [2602.20715v1](http://arxiv.org/abs/2602.20715v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型在通用机器人策略方面展现出巨大潜力，但由于分布偏移和高质量演示数据的稀缺，其在真实新场景中长期复杂任务中的泛化能力仍面临挑战。虽然强化学习（RL）为策略优化提供了可行路径，但在真实场景中对VLA模型进行微调时，仍存在探索效率、训练稳定性和样本成本等方面的难题。为此，我们提出IG-RFT——一种面向流式VLA模型的交互引导强化微调系统。首先，为实现高效策略优化，我们设计了交互引导优势加权回归算法（IG-AWR），该RL算法能根据机器人交互状态动态调节探索强度。其次，针对稀疏奖励或任务特定奖励的局限性，我们构建了融合轨迹级奖励与子任务级奖励的新型混合稠密奖励函数。最后，我们搭建了包含监督微调、离线强化学习和人在回路强化学习的三阶段RL系统，用于VLA模型微调。在四项具有挑战性的长期任务中进行的大规模真实场景实验表明，IG-RFT平均成功率可达85.0%，显著优于监督微调（18.8%）和标准离线强化学习方法（40.0%）。消融实验验证了IG-AWR算法与混合奖励设计的关键作用。本研究为真实机器人操作场景中的VLA模型构建并验证了一套创新的强化微调系统。

---

### 5. Robot Local Planner: A Periodic Sampling-Based Motion Planner with Minimal Waypoints for Home Environments

- **作者**: Keisuke Takeshita, Takahiro Yamazaki, Tomohiro Ono, Takashi Yamamoto
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.20645v1)
- **发表日期**: 2026-02-24
- **匹配关键词**: motion planning
- **arXiv**: [2602.20645v1](http://arxiv.org/abs/2602.20645v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 本研究旨在实现家庭环境中快速且安全的操作任务。具体而言，我们致力于开发一种能够在运动过程中识别周围环境并定位目标物体的系统，使其能够据此规划并执行相应动作。我们提出了一种基于周期性采样的全身轨迹规划方法，称为"机器人局部规划器（RLP）"。该方法利用家庭环境的独特特性，在确保安全性的同时，显著提升了计算效率、运动最优性以及对识别与控制误差的鲁棒性。RLP通过以最少路径点进行规划并生成安全轨迹，最大限度地缩短了计算时间。此外，通过周期性执行轨迹规划以选择更优运动方案，整体运动最优性得到进一步提升。该方法采用了对基座位置误差具有鲁棒性的逆运动学计算，进一步增强了系统的稳定性。评估实验表明，RLP在运动规划时间、运动持续时间和鲁棒性方面均优于现有方法，证实了其在家庭环境中的有效性。此外，通过整理收纳任务的实践应用实验，该系统实现了高成功率和短操作时间，充分证明了其实用可行性。

---

### 6. Learning Physical Principles from Interaction: Self-Evolving Planning via Test-Time Memory

- **作者**: Haoyang Li, Yang You, Hao Su, Leonidas Guibas
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.20323v1)
- **发表日期**: 2026-02-23
- **匹配关键词**: object manipulation
- **arXiv**: [2602.20323v1](http://arxiv.org/abs/2602.20323v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 可靠的物体操作需要理解随物体和环境变化的物理属性。视觉语言模型（VLM）规划器能够从一般层面推理摩擦力和稳定性；然而，若缺乏直接经验，它们通常无法预测特定球体在具体表面上的滚动轨迹，或判断哪块石头能提供稳固的支撑。我们提出PhysMem记忆框架，使VLM机器人规划器能够在测试阶段通过交互学习物理原理，而无需更新模型参数。该系统记录交互经验，生成候选假设，并通过针对性交互验证假设，最终将经过验证的知识提升为未来决策的指导依据。其核心设计理念在于"先验证后应用"：系统通过新观察数据检验假设，而非直接套用过往经验，从而在物理条件变化时减少对历史经验的僵化依赖。我们在三项真实世界操作任务和四种VLM基座的仿真基准测试中评估PhysMem。在受控的砖块插入任务中，基于原理抽象的方法实现了76%的成功率，而直接经验检索仅为23%；真实环境实验显示，该系统在30分钟部署周期内持续保持性能提升。

---

### 7. UniLACT: Depth-Aware RGB Latent Action Learning for Vision-Language-Action Models

- **作者**: Manish Kumar Govind, Dominick Reilly, Pu Wang, Srijan Das
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.20231v1)
- **发表日期**: 2026-02-23
- **匹配关键词**: contact-rich manipulation
- **arXiv**: [2602.20231v1](http://arxiv.org/abs/2602.20231v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 从无标注视频中学习到的潜在动作表征，近期已成为无需显式机器人动作监督即可预训练视觉-语言-动作（VLA）模型的有效范式。然而，仅从RGB观测数据推导的潜在动作主要编码外观驱动的动态信息，缺乏对精确且接触密集的操作至关重要的显式三维几何结构。为突破这一局限，我们提出UniLACT——一种基于Transformer的VLA模型，通过深度感知潜在预训练融入几何结构，使下游策略能够继承更强的空间先验。为实现这一目标，我们设计了UniLARN统一潜在动作学习框架，该框架基于逆向与正向动力学目标，在RGB与深度数据间构建共享嵌入空间，并显式建模其跨模态交互。该框架生成的模态特定与统一潜在动作表征，可作为UniLACT深度感知预训练的伪标签。大量仿真与真实场景实验验证了深度感知统一潜在动作表征的有效性。无论在域内或域外预训练场景，还是在已见或未见操作任务中，UniLACT均持续优于基于RGB的潜在动作基线方法。

---

### 8. EEG-Driven Intention Decoding: Offline Deep Learning Benchmarking on a Robotic Rover

- **作者**: Ghadah Alosaimi, Maha Alsayyari, Yixin Sun, Stamos Katsigiannis, Amir Atapour-Abarghouei, Toby P. Breckon
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.20041v1)
- **发表日期**: 2026-02-23
- **匹配关键词**: navigation
- **arXiv**: [2602.20041v1](http://arxiv.org/abs/2602.20041v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 脑机接口为移动机器人提供了一种无需手动的控制方式，但在真实导航场景中解码用户意图仍具挑战。本研究提出一种脑控机器人框架，用于在机器人漫游车操作期间离线解码驾驶指令。12名参与者通过操纵杆远程控制4WD Rover Pro平台，沿预设路线执行前进、后退、左转、右转及停止指令。研究使用16通道OpenBCI帽记录脑电图信号，并将其与Δ=0毫秒及未来预测时间窗（Δ>0毫秒）的运动动作进行同步对齐。经过预处理后，对包括卷积神经网络、循环神经网络和Transformer架构在内的多种深度学习模型进行性能评估。结果显示ShallowConvNet在动作预测和意图预测任务中均表现最优。通过将真实机器人控制与多时间窗脑电意图解码相结合，本研究不仅建立了可复现的基准测试体系，还为基于预测性深度学习的脑机接口系统揭示了关键设计思路。

---

### 9. Contextual Safety Reasoning and Grounding for Open-World Robots

- **作者**: Zachary Ravichadran, David Snyder, Alexander Robey, Hamed Hassani, Vijay Kumar, George J. Pappas
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.19983v1)
- **发表日期**: 2026-02-23
- **匹配关键词**: navigation
- **arXiv**: [2602.19983v1](http://arxiv.org/abs/2602.19983v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 机器人在开放世界环境中的运行日益增多，其安全行为往往取决于具体情境：同一条走廊在拥挤与空旷时，或在紧急状态与正常运营期间，可能需要采用不同的导航策略。传统安全方法在用户预设情境中强制执行固定约束，限制了其应对现实部署中开放式情境变化的能力。我们通过CORE框架填补这一空白，该框架支持在线情境推理、环境映射与规则执行，且无需预先掌握环境信息（如地图或安全规范）。CORE利用视觉语言模型直接根据视觉观测持续推理情境相关的安全规则，将这些规则映射到物理环境中，并通过控制屏障函数执行由此产生的空间定义安全集。我们为CORE提供了考虑感知不确定性的概率安全保证，并通过仿真与真实环境实验证明，CORE能在未知环境中执行符合情境要求的行为，其表现显著优于缺乏在线情境推理能力的传统语义安全方法。消融实验验证了我们的理论保证，并凸显了基于视觉语言模型的推理与空间映射在新型环境中执行情境安全策略的重要性。更多资源请访问https://zacravichandran.github.io/CORE。

---

### 10. TactiVerse: Generalizing Multi-Point Tactile Sensing in Soft Robotics Using Single-Point Data

- **作者**: Junhui Lee, Hyosung Kim, Saekwang Nam
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.19850v1)
- **发表日期**: 2026-02-23
- **匹配关键词**: tactile perception
- **arXiv**: [2602.19850v1](http://arxiv.org/abs/2602.19850v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 高顺应性软材料的实时形变预测仍是软体机器人领域的重大挑战。基于视觉的软体触觉传感器虽能追踪内部标记点位移，但基于学习的接触力三维估计模型严重依赖训练数据集，本质上限制了其向多点传感等复杂场景的泛化能力。为突破这一局限，我们提出TactiVerse——一种基于U-Net架构的框架，将接触几何估计转化为空间热力图预测任务。即使在仅使用单点压痕有限数据集训练的情况下，该架构仍能实现高精度单点传感，平均绝对误差达0.0589毫米，优于传统基于回归的CNN基线模型的0.0612毫米。进一步研究表明，通过引入多点接触数据增强训练集，可显著提升传感器的多点感知能力，将两点辨别的平均MAE从1.214毫米大幅提升至0.383毫米。该方法通过从基础交互中成功推演复杂接触几何，实现了先进的多点与大面积形状感知，最终极大简化了基于标记点的软体传感器开发流程，为现实世界的触觉感知提供了高度可扩展的解决方案。

---

### 11. Scalable Low-Density Distributed Manipulation Using an Interconnected Actuator Array

- **作者**: Bailey Dacre, Rodrigo Moreno, Jørn Lambertsen, Kasper Stoy, Andrés Faíña
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.19653v1)
- **发表日期**: 2026-02-23
- **匹配关键词**: object manipulation
- **arXiv**: [2602.19653v1](http://arxiv.org/abs/2602.19653v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 分布式操纵系统由机器人执行器阵列构成，通常需要密集的执行器阵列才能有效操控微小物体。本文提出一种由模块化三自由度机器人单元组成的系统，这些单元通过柔性表层相互连接，形成连续可控的操纵界面。柔性表层允许增大执行器间距而不影响物体操控能力，在保持对微小物体稳健操控的同时显著降低了执行器密度。我们通过理论分析确定了阵列的耦合工作空间，并开发出能在N×N阵列中将物体平移至任意位置的操控策略。采用最小化的2×2原型机进行实验验证，成功实现了对不同形状尺寸物体的精准操控。

---

### 12. The Initial Exploration Problem in Knowledge Graph Exploration

- **作者**: Claire McNamara, Lucy Hederman, Declan O'Sullivan
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.21066v1)
- **发表日期**: 2026-02-24
- **匹配关键词**: exploration
- **arXiv**: [2602.21066v1](http://arxiv.org/abs/2602.21066v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 知识图谱（KGs）能够实现跨领域复杂信息的整合与表征，但其语义丰富性和结构复杂性为不熟悉语义网技术的普通用户设置了显著障碍。当面对陌生的知识图谱时，这类用户会遭遇独特的认知定向挑战：他们既不清楚可以提出何种问题，也不了解知识的结构组织方式，更不知如何开启探索过程。本文首次将这一现象理论化为"初始探索困境"，借鉴信息行为学和人机交互领域的理论框架——包括非常规信息需求理论、探索式搜索理论、信息觅食理论及认知负荷理论——构建了由三个相互关联的障碍构成的概念模型：范围不确定性、本体隐晦性和查询能力缺失。我们认为这些障碍在用户首次接触知识图谱时形成聚合效应，这与那些预设了既定起点或信息目标的相关概念存在本质区别。通过对知识图谱探索界面交互原语的分析，我们发现许多系统依赖的认知假设在初始接触阶段并不成立。这揭示了设计空间中的结构性缺失：当前缺乏能够实现"范围揭示"的交互原语，即无需用户构建查询语句或解读本体结构就能传达知识图谱内容范围的机制。通过系统阐述初始探索困境，本文为评估知识图谱界面、设计支持初始探索的入口支架提供了理论视角。

---

### 13. Le-DETR: Revisiting Real-Time Detection Transformer with Efficient Encoder Design

- **作者**: Jiannan Huang, Aditya Kane, Fengzhe Zhou, Yunchao Wei, Humphrey Shi
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.21010v1)
- **发表日期**: 2026-02-24
- **匹配关键词**: exploration
- **arXiv**: [2602.21010v1](http://arxiv.org/abs/2602.21010v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: CODE
- **中文摘要**: 实时目标检测在实际应用中至关重要，它要求高精度与低延迟兼备。尽管检测变换器（DETR）已展现出显著的性能提升，但现有实时DETR模型因主干网络预训练开销过大而难以从零复现，这限制了新主干架构的探索，阻碍了研究进展。本文旨在证明，通过采用通用优良设计，完全可以在**低预训练成本**下实现**高性能**。在对主干架构进行深入研究后，我们提出了多尺度高效NAT模型，该模型融合了现代高效卷积与局部注意力机制。此外，我们重新设计了采用局部注意力的混合编码器，显著提升了性能与推理速度。基于这些创新，我们提出了Le-DETR（**低**成本**高效**检测**变换器**），仅使用ImageNet1K和COCO2017训练数据集即在实时检测领域达到**全新SOTA水平**，相比现有方法在预训练阶段节省约80%的图像数据。我们证明，通过精心设计，实时DETR模型无需复杂且计算昂贵的预训练即可实现强劲性能。大量实验表明：Le-DETR-M/L/X在COCO Val2017数据集上达到**52.9/54.3/55.1 mAP**，在RTX4090显卡上推理耗时仅**4.45/5.01/6.68毫秒**。该模型在保持相近速度的同时超越YOLOv12-L/X达**+0.6/-0.1 mAP**，并实现**20%** 的加速；与DEIM-D-FINE相比，Le-DETR-M以略快的推理速度实现**+0.2 mAP**提升，并以仅增加**0.4毫秒**延迟的代价超越DEIM-D-FINE-L达**+0.4 mAP**。代码与权重将全面开源。

---

### 14. LongVideo-R1: Smart Navigation for Low-cost Long Video Understanding

- **作者**: Jihao Qiu, Lingxi Xie, Xinyue Huo, Qi Tian, Qixiang Ye
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.20913v1)
- **发表日期**: 2026-02-24
- **匹配关键词**: navigation, exploration
- **arXiv**: [2602.20913v1](http://arxiv.org/abs/2602.20913v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: GITHUB, CODE
  - 链接：https://github.com/qiujihao19/LongVideo-R1
- **中文摘要**: 本文针对低计算预算下的长视频理解这一关键且尚未充分探索的挑战展开研究。我们提出了LongVideo-R1——一种具备推理能力的主动式多模态大语言模型（MLLM）智能体，专为高效视频上下文导航而设计，避免了穷举搜索的冗余性。LongVideo-R1的核心在于其推理模块，该模块利用高层视觉线索推断出最具信息量的视频片段以供后续处理。在推理过程中，智能体从顶层视觉摘要开始遍历，并迭代式地细化其关注焦点，一旦获得足够信息以回答查询，便立即停止探索过程。为促进训练，我们首先从带有定位标注的视频语料库CGBench中提取层次化视频描述，并引导GPT-5生成33K条高质量的工具增强思维链轨迹。LongVideo-R1智能体基于Qwen-3-8B模型通过两阶段范式进行微调：先进行监督微调（SFT），再进行强化学习（RL）。其中RL采用特别设计的奖励函数，以最大化选择性高效片段导航能力。在多个长视频基准测试上的实验验证了该方法的有效性，其在问答准确性与效率之间实现了优越的平衡。所有整理的数据和源代码均在补充材料中提供，并将公开共享。代码与数据详见：https://github.com/qiujihao19/LongVideo-R1

---

