# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-02-25 10:58

**今日新增**: 15 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 0/15 篇提供

**🌟 Highlight**: 3 篇 | **📌 Poster**: 12 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. Task-oriented grasping for dexterous robots using postural synergies and reinforcement learning

- **作者**: Dimitrios Dimou, José Santos-Victor, Plinio Moreno
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.20915v1)
- **发表日期**: 2026-02-24
- **匹配关键词**: exploration
- **arXiv**: [2602.20915v1](http://arxiv.org/abs/2602.20915v1)
- **📥 PDF**: 已下载至本地 (`2602.20915v1_Task-oriented_grasping_for_dexterous_robots_using_postural_synergies_and_reinforcement_learning.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 本文针对仿人机器人的任务导向抓取问题展开研究，重点探讨如何使其符合人类社交规范并满足特定任务需求。现有方法虽采用多种开环与闭环控制策略，但缺乏能够同时抓取多个物体并兼顾下游任务约束的端到端解决方案。我们提出的方法运用强化学习技术优化任务导向抓取过程，特别关注智能体的抓取后意图。通过从ContactPose数据集中提取人类抓取偏好，并基于变分自编码器训练手部协同模型以模拟参与者的抓取动作，我们构建了能够同时抓取多个物体且兼顾不同任务特定抓取后意图的智能体。通过将人类抓取行为的数据驱动洞察与强化学习提供的探索式学习相结合，我们得以开发出具备情境感知操作能力的仿人机器人，为人本环境中的协同作业提供支持。

---

### 2. Energy-Based Injury Protection Database: Including Shearing Contact Thresholds for Hand and Finger Using Porcine Surrogates

- **作者**: Robin Jeanne Kirschner, Anna Huber, Carina M. Micheler, Dirk Müller, Nader Rajaei, Rainer Burgkart, Sami Haddadin
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.20362v1)
- **发表日期**: 2026-02-23
- **匹配关键词**: human-robot interaction
- **arXiv**: [2602.20362v1](http://arxiv.org/abs/2602.20362v1)
- **📥 PDF**: 已下载至本地 (`2602.20362v1_Energy-Based_Injury_Protection_Database_Including_Shearing_Contact_Thresholds_for_Hand_and_Finger_Us.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 尽管机器人研究持续提出人机交互中的避碰策略，但受限于实际环境约束及未来仿人系统的发展，接触碰撞在所难免。为降低伤害风险，能量约束控制方法被广泛采用，其安全阈值通常依据EN ISO 10218-2:2025标准中的钝性冲击数据设定。然而该数据集并未涵盖边缘或尖端碰撞场景。由于缺乏覆盖多样化接触场景、具有临床依据且可扩展的数据集，安全验证工作仍存在局限。先前研究通过评估不同几何形态下基于替代模型的速率与质量限制，聚焦垂直冲击场景，为此领域奠定了基础。本研究通过纳入无约束碰撞中的剪切接触场景，拓展了现有数据集，揭示出碰撞角度对伤害结果的显著影响。值得注意的是，无约束剪切接触造成的伤害少于垂直碰撞。通过重新评估所有既往猪替代模型数据，我们建立了跨几何形态与接触类型的能量阈值，构建了首个基于能量的伤害防护数据库。这将推动开发具有实际意义的能量限制控制器，确保在广泛真实碰撞场景中的安全性。

---

### 3. To Move or Not to Move: Constraint-based Planning Enables Zero-Shot Generalization for Interactive Navigation

- **作者**: Apoorva Vashisth, Manav Kulshrestha, Pranav Bakshi, Damon Conover, Guillaume Sartoretti, Aniket Bera
- **单位**: Purdue University; Purdue University; IIT Kharagpur...
- **发表日期**: 2026-02-23
- **匹配关键词**: scene graph, navigation, active perception, visual navigation
- **arXiv**: [2602.20055v1](http://arxiv.org/abs/2602.20055v1)
- **📥 PDF**: 已下载至本地 (`2602.20055v1_To_Move_or_Not_to_Move_Constraint-based_Planning_Enables_Zero-Shot_Generalization_for_Interactive_Na.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉导航通常假设起点与目标点之间存在至少一条无障碍路径，机器人需自主发现或规划该路径。然而在现实场景中，例如家庭环境与仓库场景，杂物堆积可能阻塞所有通道。针对此类情况，我们提出终身交互式导航问题：具备操作能力的移动机器人可通过移动杂物自主开辟路径，以完成连续物体摆放任务——每项任务需将指定物体（如闹钟、枕头）放置于目标物体（如餐桌、书桌、床铺）之上。为应对环境变化效应持续累积并产生长期影响的终身场景，我们提出一种基于大语言模型驱动、融合主动感知的约束规划框架。该框架使大语言模型能够对已发现物体与障碍物构成的结构化场景图进行推理，自主决策移动何种物体、放置于何处、以及下一步探查哪些区域以获取任务相关信息。这种推理与主动感知的耦合机制使智能体能够聚焦探索对任务完成具有预期贡献的区域，而非对环境进行穷尽式测绘。标准运动规划器随后执行对应的导航-抓取-放置或绕行序列，确保可靠的低层控制。在支持物理仿真的ProcTHOR-10k模拟器中评估表明，本方法优于非学习型及基于学习的基线模型。我们进一步在真实硬件平台上对本方法进行了定性验证。

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
- **中文摘要**: 随着对能够轻柔、精确处理各类物体的软体机器人平台需求日益增长，现有基于表面的操控系统在精细操作方面仍缺乏必要的柔顺性和触觉反馈。本研究提出了一种集成感应传感器的柔顺多孔弹性软体传感系统（COPESS），该系统具备自适应物体操控与局部感知能力。其设计核心在于采用可调谐的晶格结构层，该层能同时调控机械柔顺性与传感性能。通过调整晶格几何参数，系统的刚度和传感器响应均可根据目标物体的不同力学特性进行定制。实验表明，仅通过将晶格密度从7%调整至20%这一简单参数调节，即可实现灵敏度与操作力范围的显著变化（分别提升约23倍和9倍）。这一方法为创建机械性能与感知特性协同优化的自适应传感表面提供了设计蓝图，实现了被动式但可编程的精细操控。

---

### 2. LST-SLAM: A Stereo Thermal SLAM System for Kilometer-Scale Dynamic Environments

- **作者**: Zeyu Jiang, Kuan Xu, Changhao Chen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.20925v1)
- **发表日期**: 2026-02-24
- **匹配关键词**: localization and mapping
- **arXiv**: [2602.20925v1](http://arxiv.org/abs/2602.20925v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 热成像相机在挑战性光照与天气条件下为机器人感知提供了强大潜力。然而，由于特征提取不可靠、运动跟踪不稳定以及全局位姿与地图构建不一致，热成像同步定位与建图技术仍面临困难，尤其在动态大规模户外环境中。为应对这些挑战，我们提出LST-SLAM——一种新型大规模立体热成像SLAM系统，能在复杂动态场景中实现鲁棒性能。该方法融合了自监督热特征学习、立体双层级运动跟踪与几何位姿优化技术。我们还提出语义-几何混合约束机制，可抑制缺乏帧间强几何一致性的潜在动态特征。此外，我们开发了用于闭环检测的在线增量词袋模型，并结合全局位姿优化以缓解累积漂移。在千米级动态热成像数据集上的大量实验表明，LST-SLAM在鲁棒性与精度方面均显著优于近期代表性SLAM系统（包括AirSLAM与DROID-SLAM）。

---

### 3. SoK: Agentic Skills -- Beyond Tool Use in LLM Agents

- **作者**: Yanna Jiang, Delong Li, Haiyu Deng, Baihe Ma, Xu Wang, Qin Wang, Guangsheng Yu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.20867v1)
- **发表日期**: 2026-02-24
- **匹配关键词**: tool use
- **arXiv**: [2602.20867v1](http://arxiv.org/abs/2602.20867v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 智能体系统日益依赖可复用的程序化能力——即智能体技能——来可靠地执行长周期工作流。这些能力是可调用模块，将程序性知识与明确的适用条件、执行策略、终止标准及可复用接口封装在一起。与一次性计划或原子化工具调用不同，技能能够跨任务运行（且通常表现良好）。

本文系统梳理了技能层在全生命周期（发现、实践、提炼、存储、组合、评估与更新）中的运作机制，并提出两种互补的分类体系。首先是系统层面的**七种设计模式**，涵盖从元数据驱动的渐进式呈现、可执行代码技能，到自我演化的技能库及市场分发的实际技能封装与执行方式。其次是正交的**表征形式×作用域**分类法，描述技能的本质形态（自然语言、代码、策略、混合型）及其运作环境（网络、操作系统、软件工程、机器人领域）。

我们分析了基于技能的智能体在安全与治理层面的影响，涵盖供应链风险、通过技能载荷进行的提示注入攻击及信任分级执行机制，并以ClawHavoc攻击活动为案例进行实证研究——该活动中近1200个恶意技能渗透主流智能体市场，大规模窃取API密钥、加密货币钱包及浏览器凭证。我们进一步系统考察了确定性评估方法，基于近期基准测试证据表明：经人工优化的技能可显著提升智能体成功率，而自主生成的技能可能适得其反。最后，我们提出面向现实世界自主智能体构建稳健、可验证、可认证技能体系所面临的开放挑战。

---

### 4. IG-RFT: An Interaction-Guided RL Framework for VLA Models in Long-Horizon Robotic Manipulation

- **作者**: Zhian Su, Weijie Kong, Haonan Dong, Huixu Dong
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.20715v1)
- **发表日期**: 2026-02-24
- **匹配关键词**: exploration
- **arXiv**: [2602.20715v1](http://arxiv.org/abs/2602.20715v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型已展现出作为通用机器人策略的巨大潜力，但由于分布偏移和高质量演示数据的稀缺，其在真实新场景中长期复杂任务中的泛化能力仍面临挑战。尽管强化学习为策略优化提供了可行路径，但在真实场景中对VLA模型进行微调时，仍存在探索效率、训练稳定性和样本成本等方面的难题。为此，我们提出IG-RFT——一种面向流式VLA模型的交互引导强化微调系统。首先，为实现高效策略优化，我们设计了交互引导优势加权回归算法，该强化学习算法能根据机器人交互状态动态调节探索强度。其次，针对稀疏奖励或任务特定奖励的局限性，我们构建了一种融合轨迹级奖励与子任务级奖励的新型混合稠密奖励函数。最后，我们搭建了包含监督微调、离线强化学习和人在回路强化学习的三阶段强化学习系统，用于VLA模型的微调。在四项具有挑战性的长期任务中进行的大规模真实场景实验表明，IG-RFT平均成功率可达85.0%，显著优于监督微调（18.8%）和标准离线强化学习基线方法（40.0%）。消融实验验证了交互引导优势加权回归算法与混合奖励塑形机制的关键作用。本研究为真实机器人操作场景中的VLA模型构建并验证了一套创新的强化微调系统。

---

### 5. Robot Local Planner: A Periodic Sampling-Based Motion Planner with Minimal Waypoints for Home Environments

- **作者**: Keisuke Takeshita, Takahiro Yamazaki, Tomohiro Ono, Takashi Yamamoto
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.20645v1)
- **发表日期**: 2026-02-24
- **匹配关键词**: motion planning
- **arXiv**: [2602.20645v1](http://arxiv.org/abs/2602.20645v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 本研究旨在实现家庭环境中快速且安全的操控任务。具体而言，我们致力于开发一种能够在运动过程中识别周围环境并定位目标物体的系统，使其能够据此规划并执行相应动作。我们提出了一种基于周期性采样的全身轨迹规划方法，称为"机器人局部规划器（RLP）"。该方法利用家庭环境的独特特性，在确保安全的前提下，显著提升了计算效率、运动最优性以及对识别与控制误差的鲁棒性。RLP通过以最少路径点进行规划并生成安全轨迹，大幅缩短了计算时间。此外，通过周期性执行轨迹规划以选择更优动作，整体运动最优性得到进一步提升。该方法采用了对基座位置误差具有鲁棒性的逆运动学模型，从而进一步增强了系统的稳定性。评估实验表明，RLP在运动规划时间、运动持续时间和鲁棒性方面均优于现有方法，证实了其在家庭环境中的有效性。此外，通过整理收纳任务的应用实验取得了高成功率和短操作时间，进一步凸显了其实用可行性。

---

### 6. Learning Physical Principles from Interaction: Self-Evolving Planning via Test-Time Memory

- **作者**: Haoyang Li, Yang You, Hao Su, Leonidas Guibas
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.20323v1)
- **发表日期**: 2026-02-23
- **匹配关键词**: object manipulation
- **arXiv**: [2602.20323v1](http://arxiv.org/abs/2602.20323v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 可靠的物体操控需要理解随物体和环境变化的物理属性。视觉语言模型（VLM）规划器能够从宏观层面推理摩擦力和稳定性；然而，若缺乏直接经验，它们往往无法预测特定球体在具体表面上的滚动轨迹，或判断哪块石头能提供稳固支撑。我们提出PhysMem记忆框架，使VLM机器人规划器能够在测试阶段通过交互学习物理原理，而无需更新模型参数。该系统记录交互经验，生成候选假设，并通过针对性交互验证假设，最终将经过验证的知识提升为未来决策的指导依据。核心设计理念在于"先验证后应用"：系统通过新观察数据检验假设，而非直接套用过往经验，从而在物理条件变化时减少对历史经验的僵化依赖。我们在三项真实世界操控任务和四种VLM基座的仿真基准测试中评估PhysMem。在受控的积木插接任务中，基于原理抽象的方法实现了76%的成功率，而直接经验检索仅为23%；真实环境实验显示，该系统在30分钟部署周期内持续保持性能提升。

---

### 7. UniLACT: Depth-Aware RGB Latent Action Learning for Vision-Language-Action Models

- **作者**: Manish Kumar Govind, Dominick Reilly, Pu Wang, Srijan Das
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.20231v1)
- **发表日期**: 2026-02-23
- **匹配关键词**: contact-rich manipulation
- **arXiv**: [2602.20231v1](http://arxiv.org/abs/2602.20231v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 从无标注视频中学习到的潜在动作表征，近期已成为无需显式机器人动作监督即可预训练视觉-语言-动作模型的有效范式。然而，仅从RGB观测数据推导的潜在动作主要编码外观驱动的动态特征，缺乏对精确且接触密集的操作至关重要的显式三维几何结构。为突破这一局限，我们提出UniLACT——一种基于Transformer的视觉-语言-动作模型，通过深度感知潜在预训练融入几何结构，使下游策略能够继承更强的空间先验。为实现这一目标，我们设计了UniLARN统一潜在动作学习框架，该框架基于逆向与正向动力学目标，在RGB与深度数据间构建共享嵌入空间，并显式建模跨模态交互。该框架生成的模态专用与统一潜在动作表征，可作为UniLACT深度感知预训练的伪标签。大量仿真与真实场景实验验证了深度感知统一潜在动作表征的有效性。无论是在域内还是域外预训练场景下，亦或是在已见与未见操作任务中，UniLACT均持续超越基于RGB的潜在动作基线模型。

---

### 8. EEG-Driven Intention Decoding: Offline Deep Learning Benchmarking on a Robotic Rover

- **作者**: Ghadah Alosaimi, Maha Alsayyari, Yixin Sun, Stamos Katsigiannis, Amir Atapour-Abarghouei, Toby P. Breckon
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.20041v1)
- **发表日期**: 2026-02-23
- **匹配关键词**: navigation
- **arXiv**: [2602.20041v1](http://arxiv.org/abs/2602.20041v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 脑机接口为移动机器人提供了一种无需手动的控制方式，但在真实导航场景中解码用户意图仍具挑战。本研究提出一种脑控机器人框架，用于在机器人漫游车操作期间离线解码驾驶指令。12名参与者通过操纵杆远程控制4WD Rover Pro平台，沿预设路线执行前进、后退、左转、右转及停止指令。研究使用16通道OpenBCI帽记录脑电图信号，并将其与Δ=0毫秒及未来预测时间窗（Δ>0毫秒）的运动动作进行同步对齐。经过预处理后，对包括卷积神经网络、循环神经网络和Transformer架构在内的多种深度学习模型进行性能评估。结果显示ShallowConvNet在动作预测和意图预测任务中均表现最优。通过将真实机器人控制与多时间窗脑电意图解码相结合，本研究不仅建立了可复现的基准测试体系，更为基于预测性深度学习的脑机接口系统揭示了关键设计思路。

---

### 9. Contextual Safety Reasoning and Grounding for Open-World Robots

- **作者**: Zachary Ravichadran, David Snyder, Alexander Robey, Hamed Hassani, Vijay Kumar, George J. Pappas
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.19983v1)
- **发表日期**: 2026-02-23
- **匹配关键词**: navigation
- **arXiv**: [2602.19983v1](http://arxiv.org/abs/2602.19983v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 机器人在开放世界环境中的运行日益增多，其安全行为往往取决于具体情境：同一条走廊在拥挤与空旷时，或在紧急状态与正常运营期间，可能需要采用不同的导航策略。传统安全方法在用户预设情境中强制执行固定约束，限制了其应对现实部署中开放式情境变化的能力。我们通过CORE框架填补这一空白，该框架支持在线情境推理、环境映射与规则执行，且无需预先掌握环境信息（如地图或安全规范）。CORE利用视觉语言模型持续从视觉观测中直接推理情境相关的安全规则，将这些规则映射到物理环境，并通过控制屏障函数执行由此产生的空间定义安全集。我们为CORE提供了考虑感知不确定性的概率安全保证，并通过仿真与真实环境实验证明，CORE能在未知环境中执行符合情境要求的行为，其表现显著优于缺乏在线情境推理能力的传统语义安全方法。消融实验验证了我们的理论保证，并凸显了基于视觉语言模型的推理与空间映射对于在新环境中实现情境安全的重要性。更多资源请访问https://zacravichandran.github.io/CORE。

---

### 10. TactiVerse: Generalizing Multi-Point Tactile Sensing in Soft Robotics Using Single-Point Data

- **作者**: Junhui Lee, Hyosung Kim, Saekwang Nam
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.19850v1)
- **发表日期**: 2026-02-23
- **匹配关键词**: tactile perception
- **arXiv**: [2602.19850v1](http://arxiv.org/abs/2602.19850v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 高顺应性软材料的实时形变预测仍是软体机器人领域的重大挑战。基于视觉的软体触觉传感器虽能追踪内部标记点位移，但基于学习的接触力三维估计模型严重依赖训练数据集，其泛化至多点传感等复杂场景的能力存在固有局限。为突破此限制，我们提出TactiVerse——一种基于U-Net架构的框架，将接触几何估计转化为空间热力图预测任务。该架构仅使用单点压痕的有限数据集进行训练，即可实现高精度单点传感，其平均绝对误差达0.0589毫米，优于传统基于回归的CNN基线模型的0.0612毫米。进一步研究表明，通过引入多点接触数据增强训练集，可显著提升传感器的多点感知能力，将两点辨别的整体平均MAE从1.214毫米大幅提升至0.383毫米。该方法通过从基础交互中成功推演复杂接触几何，实现了先进的多点与大面积形状感知，最终极大简化了基于标记点的软体传感器开发流程，为现实世界的触觉感知提供了高度可扩展的解决方案。

---

### 11. Scalable Low-Density Distributed Manipulation Using an Interconnected Actuator Array

- **作者**: Bailey Dacre, Rodrigo Moreno, Jørn Lambertsen, Kasper Stoy, Andrés Faíña
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.19653v1)
- **发表日期**: 2026-02-23
- **匹配关键词**: object manipulation
- **arXiv**: [2602.19653v1](http://arxiv.org/abs/2602.19653v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 分布式机械臂系统由机器人执行器阵列构成，通常需要密集的执行器阵列才能有效操控微小物体。本文提出一种由模块化三自由度机器人单元组成的系统，这些单元通过柔性表层相互连接，形成连续可控的操作界面。柔性表层允许增大执行器间距而不影响物体操控能力，在保持对微小物体稳健操控的同时显著降低了执行器密度。我们对阵列的耦合工作空间进行建模，并开发出能够在N×N阵列中将物体平移至任意位置的操作策略。通过最小化的2×2原型机进行实验验证，该方法成功实现了对不同形状尺寸物体的精准操控。

---

### 12. An Approach to Combining Video and Speech with Large Language Models in Human-Robot Interaction

- **作者**: Guanting Shen, Zi Tian
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.20219v1)
- **发表日期**: 2026-02-23
- **匹配关键词**: human-robot collaboration, human-robot interaction, object manipulation, HRI
- **arXiv**: [2602.20219v1](http://arxiv.org/abs/2602.20219v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 准确解读人类意图是人机交互（HRI）领域的核心挑战，也是实现更自然、更直观人机协作的关键要求。本研究提出了一种新颖的多模态人机交互框架，该框架结合了先进的视觉语言模型、语音处理和模糊逻辑技术，实现了对Dobot Magician机械臂的精准自适应控制。该系统集成Florence-2进行物体检测，采用Llama 3.1实现自然语言理解，并利用Whisper进行语音识别，为用户通过语音指令操控物体提供了无缝直观的交互界面。通过协同处理场景感知与动作规划，该方法显著提升了指令解读与执行的可靠性。在消费级硬件上进行的实验评估显示，系统指令执行准确率达到75%，充分证明了其鲁棒性与适应性。除当前性能表现外，该架构为人机交互未来研究提供了灵活可扩展的基础框架，通过紧密耦合的语音与视觉语言处理，为迈向更复杂、更自然的人机协作提供了实用路径。

---

