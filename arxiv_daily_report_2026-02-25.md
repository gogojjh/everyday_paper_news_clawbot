# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-02-25 00:06

**今日新增**: 15 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 3/15 篇提供

**🌟 Highlight**: 3 篇 | **📌 Poster**: 12 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图*

---

### 1. To Move or Not to Move: Constraint-based Planning Enables Zero-Shot Generalization for Interactive Navigation

- **作者**: Apoorva Vashisth, Manav Kulshrestha, Pranav Bakshi, Damon Conover, Guillaume Sartoretti, Aniket Bera
- **单位**: Purdue University; Purdue University; IIT Kharagpur...
- **发表日期**: 2026-02-23
- **匹配关键词**: navigation, visual navigation
- **arXiv**: [2602.20055v1](http://arxiv.org/abs/2602.20055v1)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉导航通常假设起点与目标之间存在至少一条无障碍路径，机器人需自主发现或规划该路径。然而在现实场景中，如家庭环境与仓库场景，杂物堆积可能阻塞所有通道。针对此类情况，我们提出终身交互式导航问题：具备操作能力的移动机器人可通过移动杂物自主开辟路径，以完成序列化物体放置任务——每个任务需将指定物体（如闹钟、枕头）放置到目标物体（如餐桌、书桌、床铺）之上。为应对环境变化效应持续累积并产生长期影响的终身场景，我们提出基于大语言模型的主动感知约束规划框架。该框架使大语言模型能够对已发现物体与障碍物构成的场景图进行推理，决策移动何种物体、放置于何处、以及下一步探查哪些区域以获取任务相关信息。这种推理与主动感知的耦合机制，使智能体能够聚焦探索对任务完成具有预期贡献的区域，而非对环境进行穷尽式测绘。标准运动规划器随后执行对应的导航-抓取-放置或绕行序列，确保可靠的低层控制。在具备物理引擎的ProcTHOR-10k模拟器中评估表明，本方法优于非学习型及基于学习的基线模型。我们进一步在真实硬件平台上进行了定性验证。

---

### 2. Hilbert-Augmented Reinforcement Learning for Scalable Multi-Robot Coverage and Exploration

- **作者**: Tamil Selvan Gurunathan, Aryya Gangopadhyay
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.19400v1)
- **发表日期**: 2026-02-23
- **匹配关键词**: exploration
- **arXiv**: [2602.19400v1](http://arxiv.org/abs/2602.19400v1)
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出一种覆盖框架，将希尔伯特空间填充先验整合到去中心化多机器人学习与执行中。通过为DQN和PPO算法引入基于希尔伯特的空间索引机制，我们在稀疏奖励环境中构建结构化探索并降低冗余度，并在多机器人网格覆盖任务中评估其可扩展性。进一步设计了航点接口，将希尔伯特序列转化为曲率有界、时间参数化的SE(2)轨迹（平面(x, y, θ)），使资源受限的机器人能够实现机载可行执行。实验表明，相较于DQN/PPO基线方法，该框架在覆盖效率、冗余控制与收敛速度方面均有提升。此外，我们在波士顿动力Spot四足机器人上验证了该方法，通过在室内环境执行生成轨迹，观察到低冗余度的可靠覆盖效果。这些结果表明几何先验能有效提升集群机器人与足式机器人系统的自主性与可扩展性。

---

### 3. WildOS: Open-Vocabulary Object Search in the Wild

- **作者**: Hardik Shah, Erica Tevere, Deegan Atha, Marcel Kaufmann, Shehryar Khattak, Manthan Patel, Marco Hutter, Jonas Frey, Patrick Spieler
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.19308v1)
- **发表日期**: 2026-02-22
- **匹配关键词**: autonomous navigation, exploration, navigation, semantic navigation
- **arXiv**: [2602.19308v1](http://arxiv.org/abs/2602.19308v1)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://leggedrobotics.github.io/wildos/
- **中文摘要**: 在复杂、无结构的户外环境中实现自主导航，要求机器人能够在没有先验地图且深度感知受限的情况下进行长距离作业。在此类场景中，仅依赖几何边界进行探索往往是不够的，而通过语义推理判断行进方向与安全通行区域的能力，对于实现稳健高效的探索至关重要。本研究提出WildOS系统——一个结合安全几何探索与语义视觉推理的长距离开放词汇目标搜索统一框架。该系统通过构建稀疏导航图来维持空间记忆，同时利用基于基础模型的视觉模块ExploRFM对图的边界节点进行评分。ExploRFM能够在图像空间中同步预测可通行性、视觉边界及目标相似度，从而实现实时的机载语义导航任务。这种基于视觉评分的导航图使机器人能够在确保几何安全的前提下，沿具有语义意义的方向进行探索。此外，我们引入了一种基于粒子滤波的开放词汇目标粗定位方法，可估算超出机器人即时深度感知范围的候选目标位置，从而实现对远距离目标的有效路径规划。通过在多种越野与城市地形中开展的闭环实地实验表明，WildOS系统能够实现稳健的导航性能，在效率与自主性方面显著优于纯几何方法和纯视觉基线。我们的研究成果凸显了视觉基础模型在驱动兼具语义感知与几何约束的开放世界机器人行为方面的潜力。项目页面：https://leggedrobotics.github.io/wildos/

---

## 📌 Poster

*其他相关研究*

---

### 1. EEG-Driven Intention Decoding: Offline Deep Learning Benchmarking on a Robotic Rover

- **作者**: Ghadah Alosaimi, Maha Alsayyari, Yixin Sun, Stamos Katsigiannis, Amir Atapour-Abarghouei, Toby P. Breckon
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.20041v1)
- **发表日期**: 2026-02-23
- **匹配关键词**: navigation
- **arXiv**: [2602.20041v1](http://arxiv.org/abs/2602.20041v1)
- **🔒 开源**: 未提及
- **中文摘要**: 脑机接口为移动机器人提供了一种无需手动的控制方式，但在真实导航场景中解码用户意图仍具挑战性。本研究提出一种脑控机器人框架，用于在机器人漫游车操作期间离线解码驾驶指令。12名参与者通过操纵杆远程控制4WD Rover Pro平台，沿预设路线执行前进、后退、左转、右转及停止指令。研究使用16通道OpenBCI帽采集脑电图信号，并将其与Δ=0毫秒的实时动作及未来预测时间窗（Δ>0毫秒）的动作进行对齐。经过预处理后，本研究对多种深度学习模型进行了性能评估，包括卷积神经网络、循环神经网络和Transformer架构。其中ShallowConvNet在动作预测和意图预测任务中均表现最优。通过将真实机器人控制与多时间窗脑电意图解码相结合，本研究不仅建立了可复现的基准测试体系，更为基于预测性深度学习的脑机接口系统揭示了关键设计思路。

---

### 2. Contextual Safety Reasoning and Grounding for Open-World Robots

- **作者**: Zachary Ravichadran, David Snyder, Alexander Robey, Hamed Hassani, Vijay Kumar, George J. Pappas
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.19983v1)
- **发表日期**: 2026-02-23
- **匹配关键词**: navigation
- **arXiv**: [2602.19983v1](http://arxiv.org/abs/2602.19983v1)
- **🔒 开源**: 未提及
- **中文摘要**: 机器人在开放世界环境中的运行日益增多，其安全行为往往取决于具体情境：同一条走廊在拥挤与空旷时，或在紧急状态与正常运营期间，可能需要采用不同的导航策略。传统安全方法在用户预设的情境中强制执行固定约束，限制了其应对现实部署中开放式情境变化的能力。为此，我们提出CORE安全框架，通过在线情境推理、环境映射与规则执行来填补这一空白，且无需预先掌握环境信息（如地图或安全规范）。CORE利用视觉语言模型直接根据视觉观测持续推理情境相关的安全规则，将这些规则映射到物理环境中，并通过控制屏障函数强制执行由此产生的空间定义安全集。我们为CORE提供了考虑感知不确定性的概率安全保证，并通过仿真与真实环境实验证明，CORE能在未知环境中执行符合情境要求的行为，其表现显著优于缺乏在线情境推理能力的传统语义安全方法。消融实验验证了我们的理论保证，并凸显了基于视觉语言模型的推理与空间映射在全新场景中实现情境安全的重要性。更多资源请访问https://zacravichandran.github.io/CORE。

---

### 3. Scalable Low-Density Distributed Manipulation Using an Interconnected Actuator Array

- **作者**: Bailey Dacre, Rodrigo Moreno, Jørn Lambertsen, Kasper Stoy, Andrés Faíña
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.19653v1)
- **发表日期**: 2026-02-23
- **匹配关键词**: object manipulation
- **arXiv**: [2602.19653v1](http://arxiv.org/abs/2602.19653v1)
- **🔒 开源**: 未提及
- **中文摘要**: 分布式机械臂系统由机器人执行器阵列构成，通常需要密集的执行器阵列才能有效操控微小物体。本文提出一种由模块化三自由度机器人单元组成的系统，这些单元通过柔性表层相互连接，形成连续可控的操作界面。柔性表层允许增大执行器间距而不影响物体操控能力，在保持对微小物体稳健操控的同时显著降低了执行器密度。我们对阵列的耦合工作空间进行建模，并开发出能在N×N阵列中将物体平移至任意位置的操作策略。通过最小化的2×2原型机进行实验验证，该方法成功实现了对不同形状尺寸物体的精准操控。

---

### 4. Chasing Ghosts: A Simulation-to-Real Olfactory Navigation Stack with Optional Vision Augmentation

- **作者**: Kordel K. France, Ovidiu Daescu, Latifur Khan, Rohith Peddi
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.19577v1)
- **发表日期**: 2026-02-23
- **匹配关键词**: navigation
- **arXiv**: [2602.19577v1](http://arxiv.org/abs/2602.19577v1)
- **🔓 开源**: GITHUB, CODE
  - 链接：https://github.com/KordelFranceTech/ChasingGhosts.
- **中文摘要**: 自主气味源定位对飞行机器人而言仍具挑战性，这主要源于湍流、稀疏且延迟的感官信号，以及严格的载荷与计算限制。尽管先前基于无人机（UAV）的嗅觉系统已实现气体分布图绘制或反应式羽流追踪，但这些系统依赖于预定义的覆盖模式、外部基础设施或复杂的传感与协调机制。本研究提出了一套完整的开源无人机系统，通过最小化传感器配置实现在线气味源定位。该系统集成了定制嗅觉硬件、机载传感模块，以及基于学习的导航策略——该策略在仿真环境中训练并部署于真实四旋翼飞行器。借助这一极简框架，无人机无需构建显式气体分布图或依赖外部定位系统即可直接导航至气味源。视觉感知作为可选补充模态被引入，以在特定条件下加速导航过程。我们通过在大型室内环境中使用乙醇源进行真实飞行实验验证了所提系统，证明其在真实气流条件下具有稳定的气味源搜寻能力。本工作的核心贡献在于提供了一套可复现的系统与方法框架，用于在最小化传感假设下实现基于无人机的嗅觉导航与气味源搜寻。我们详细阐述了硬件设计，并向社区开源了无人机固件、仿真代码、嗅觉-视觉数据集及电路板设计。相关代码、数据与设计文件可通过https://github.com/KordelFranceTech/ChasingGhosts获取。

---

### 5. Positioning Modular Co-Design in Future HRI Design Research

- **作者**: Lingyun Chen, Qing Xiao, Zitao Zhang, Eli Blevis, Selma Šabanović
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.19422v1)
- **发表日期**: 2026-02-23
- **匹配关键词**: HRI
- **arXiv**: [2602.19422v1](http://arxiv.org/abs/2602.19422v1)
- **🔒 开源**: 未提及
- **中文摘要**: 面向设计的HRI研究日益关注机器人作为长期伴侣的可能性，但许多设计仍固守固定形态与稳定功能集。我们提出一项持续进行的设计研究计划，将模块化视为一种设计媒介——通过协同设计使长期人机关系变得可讨论、可具象化。在一系列面向生命周期的协同设计活动中，参与者反复为不同人生阶段重构同一机器人，借助模块化部件表达变化的需求、价值观与角色定位。基于这些成果，我们提出PAS框架（个性化-适应性-可持续性）作为以人为本的观察视角，揭示人们实践中如何运用模块化：通过配置实现自我表达，跨越人生阶段进行适应性调整，借助维修、复用与延续性实现机器人可持续使用。继而我们勾勒出面向制造、社区可扩展的模块化平台发展路径，并提出设计导向型HRI工作的评估标准——重点关注表达充分性、生命周期合理性、使用可维修性与责任管理，而非仅局限于可用性或性能指标。

---

### 6. Design and Control of Modular Magnetic Millirobots for Multimodal Locomotion and Shape Reconfiguration

- **作者**: Erik Garcia Oyono, Jialin Lin, Dandan Zhang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.19346v1)
- **发表日期**: 2026-02-22
- **匹配关键词**: navigation, path planning
- **arXiv**: [2602.19346v1](http://arxiv.org/abs/2602.19346v1)
- **🔒 开源**: 未提及
- **中文摘要**: 模块化小型机器人具备按需组装与拆卸的能力，可在动态受限环境中实现任务适应性重构。然而，现有模块化磁控平台通常依赖工作空间碰撞实现重构，采用笨重的三维电磁系统，且缺乏稳健的单模块控制能力，限制了其在生物医学场景中的应用。本研究提出一种模块化磁控毫米机器人平台，由三个立方体模块构成，各模块内置永磁体并承担特定功能：支持自组装与重构的自由模块、实现翻转行走运动的固定模块、以及用于货物操作的抓取模块。通过编程组合时变二维均匀磁场与梯度磁场输入，驱动系统完成运动与重构。实验基于实时视觉反馈与A*路径规划实现了闭环导航，验证了稳健的单模块控制能力。除运动功能外，该系统在低场强条件下实现了自组装、多模态转换及拆卸操作。链式结构向抓取器的转换成功率高达90%，而链式向方形结构的转换稳定性较低，凸显了模块几何构型对重构可靠性的影响。该研究构建了一个具备多模态行为与稳健控制能力的通用模块化机器人平台，为在受限环境中实现可扩展的自适应任务执行提供了可行路径。

---

### 7. Online Navigation Planning for Long-term Autonomous Operation of Underwater Gliders

- **作者**: Victor-Alexandru Darvariu, Charlotte Z. Reed, Jan Stratmann, Bruno Lacerda, Benjamin Allsup, Stephen Woodward, Elizabeth Siddle, Trishna Saeharaseelan, Owain Jones, Dan Jones, Tobias Ferreira, Chloe Baker, Kevin Chaplin, James Kirk, Ashley Morris, Ryan Patmore, Jeff Polton, Charlotte Williams, Alexandra Kokkinaki, Alvaro Lorenzo Lopez, Justin J. H. Buck, Nick Hawes
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.19315v1)
- **发表日期**: 2026-02-22
- **匹配关键词**: navigation
- **arXiv**: [2602.19315v1](http://arxiv.org/abs/2602.19315v1)
- **🔒 开源**: 未提及
- **中文摘要**: 水下滑翔机器人已成为海洋采样不可或缺的工具。尽管相关方呼吁开发工具以管理日益庞大的滑翔机集群，但迄今为止成功的自主长期部署案例仍然稀少，这表明缺乏合适的方法论和系统。本研究将滑翔机导航规划构建为随机最短路径马尔可夫决策过程，并提出基于蒙特卡洛树搜索的采样式在线规划器。采样通过物理信息模拟器生成，该模拟器在保持计算可行性的同时，能捕捉控制执行的不确定性和洋流预测变化。模拟器参数使用历史滑翔机数据进行拟合。我们将这些方法集成至Slocum滑翔机的自主指挥控制系统中，实现每次上浮时的闭环重规划。该集成系统在北海进行的两次实地部署中得到验证，累计实现约3个月、1000公里的自主航行。实验结果表明，相较于直线航向导航，该系统能显著提升航行效率，并证明了采样式规划方法在长期海洋自主作业中的实用性。

---

### 8. Safe and Interpretable Multimodal Path Planning for Multi-Agent Cooperation

- **作者**: Haojun Shi, Suyu Ye, Katherine M. Guerrerio, Jianzhi Shen, Yifan Yin, Daniel Khashabi, Chien-Ming Huang, Tianmin Shu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.19304v1)
- **发表日期**: 2026-02-22
- **匹配关键词**: path planning
- **arXiv**: [2602.19304v1](http://arxiv.org/abs/2602.19304v1)
- **🔒 开源**: 未提及
- **中文摘要**: 分散式智能体间的成功协作要求每个智能体能够快速调整自身计划以适应其他智能体的行为。在智能体难以准确预测彼此意图与行动方案的场景中，语言交流对于保障安全至关重要。本研究聚焦于路径层面的协作问题，即智能体必须通过相互调整路径来避免碰撞或完成物理协作任务（如联合搬运）。我们提出了一种安全可解释的多模态路径规划方法CaPE（代码即路径编辑器），该方法能根据环境信息与其他智能体的语言交流，生成并更新智能体的路径规划方案。CaPE利用视觉语言模型合成经过模型化规划器验证的路径编辑程序，通过安全可解释的方式将语言交流转化为路径规划的更新指令。我们在多样化仿真与真实场景中评估了该方法，包括自动驾驶、家庭环境及联合搬运任务中的多机器人协作与人机协作。实验结果表明，CaPE可作为即插即用模块集成至不同机器人系统，显著提升机器人根据其他机器人或人类语言交流调整自身规划的能力。研究还表明，基于视觉语言模型的路径编辑程序合成与模型化规划安全机制的融合，使机器人在保持安全性与可解释性的同时，能够实现开放式的协作。

---

### 9. 3D Shape Control of Extensible Multi-Section Soft Continuum Robots via Visual Servoing

- **作者**: Abhinav Gandhi, Shou-Shan Chiang, Cagdas D. Onal, Berk Calli
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.19273v1)
- **发表日期**: 2026-02-22
- **匹配关键词**: visual servoing, object manipulation
- **arXiv**: [2602.19273v1](http://arxiv.org/abs/2602.19273v1)
- **🔒 开源**: 未提及
- **中文摘要**: 本文提出了一种新颖的基于视觉的控制算法，用于调节可扩展多节段软体连续型机械臂的整体形态。与现有文献中仅调控机器人末端执行器位姿的视觉控制算法不同，我们提出的控制算法能够调控机器人的整体构型，从而充分利用其运动学冗余特性。相较于文献中报道存在局部极小值问题的同类研究，我们基于模型的2.5维形态视觉伺服方法在机器人三维工作空间中实现了全局稳定的渐近收敛。与现有视觉伺服算法相比，该方法无需依赖本体感知传感器的信息，因此适用于不具备此类传感能力的连续型机械臂。机器人状态完全通过外部摄像头采集的图像进行估计，该摄像头同时观测机器人整体形态并用于闭合形态控制回路。传统视觉伺服方案需要获取参考位姿下的机器人图像以生成参考特征，而本研究通过逆运动学求解器直接为目标构型生成参考特征，无需实际采集参考位姿图像。我们在多节段连续型机械臂上进行了实验验证，结果表明该控制器在精确定位末端执行器的同时，能够有效调控机器人整体形态。实验数据证实了控制器在保持平滑瞬态响应的前提下，可将稳态误差控制在1毫米以内，成功实现了连续型机器人的形态调控。通过堆叠、倾倒、牵引等概念验证性物体操作实验，进一步证明了该控制器的实际应用价值。

---

### 10. Human-to-Robot Interaction: Learning from Video Demonstration for Robot Imitation

- **作者**: Thanh Nguyen Canh, Thanh-Tuan Tran, Haolan Zhang, Ziyan Gao, Nak Young Chong, Xiem HoangVan
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.19184v1)
- **发表日期**: 2026-02-22
- **匹配关键词**: HRI
- **arXiv**: [2602.19184v1](http://arxiv.org/abs/2602.19184v1)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://thanhnguyencanh.github.io/LfD4hri.
- **中文摘要**: 从演示中学习（LfD）为机器人技能获取提供了一种前景广阔的模式。现有方法尝试直接从视频演示中提取操作指令，但仍面临两大关键挑战：（1）通用视频描述模型侧重于全局场景特征而非任务相关对象，生成的描述难以用于精确的机器人执行；（2）将视觉理解与策略学习耦合的端到端架构需要大量配对数据集，且难以跨对象和场景泛化。为突破这些局限，受人类通过观察模仿进行学习的能力启发，我们提出了一种创新的“人机交互”模仿学习框架，使机器人能够直接从非结构化视频演示中获取操作技能。我们的核心创新在于模块化架构，将学习过程解耦为两个独立阶段：（1）视频理解阶段，结合时序移位模块（TSM）与视觉语言模型（VLM）提取动作并识别交互对象；（2）机器人模仿阶段，采用基于TD3的深度强化学习执行演示操作。我们在PyBullet仿真环境（使用UR5e机械臂）和真实世界实验（使用UF850机械臂）中验证了该方法，涵盖到达、抓取、移动、放置四项基础动作。在视频理解方面，我们的方法在标准物体上实现89.97%的动作分类准确率，BLEU-4得分达0.351；在新物体上BLEU-4得分为0.265，分别较最佳基线提升76.4%和128.4%。在机器人操作方面，该框架在所有动作中平均成功率87.5%，其中到达任务成功率100%，复杂抓放操作成功率最高达90%。项目网站详见https://thanhnguyencanh.github.io/LfD4hri。

---

### 11. Understanding Fire Through Thermal Radiation Fields for Mobile Robots

- **作者**: Anton R. Wagner, Madhan Balaji Rao, Xuesu Xiao, Sören Pirk
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.19108v1)
- **发表日期**: 2026-02-22
- **匹配关键词**: robot navigation, navigation
- **arXiv**: [2602.19108v1](http://arxiv.org/abs/2602.19108v1)
- **🔒 开源**: 未提及
- **中文摘要**: 在火灾影响环境中安全移动是部署于灾难响应场景的自主移动机器人必须具备的关键能力。本研究提出一种创新方法，使移动机器人能够通过构建实时热辐射场来理解火情。我们通过配准深度图像与热成像数据，获得带有温度标注的三维点云。基于这些数据，我们识别火源并运用斯特藩-玻尔兹曼定律估算空白区域的热辐射强度，从而构建覆盖整个环境的连续热辐射场。研究表明，该表征方法可用于机器人导航——通过将热约束嵌入代价地图，可计算出无碰撞且满足热安全要求的路径。我们在受控实验环境中使用波士顿动力Spot机器人验证了该方法的有效性，实验证明机器人能够在规避危险区域的同时完成导航任务。本方法为移动机器人自主部署于火灾环境开辟了新途径，在搜救、消防及危险物质处置等领域具有广阔应用前景。

---

### 12. Path planning for unmanned surface vehicle based on predictive artificial potential field. International Journal of Advanced Robotic Systems

- **作者**: Jia Song, Ce Hao, Jiangcheng Su
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.19062v1)
- **发表日期**: 2026-02-22
- **匹配关键词**: path planning
- **arXiv**: [2602.19062v1](http://arxiv.org/abs/2602.19062v1)
- **🔒 开源**: 未提及
- **中文摘要**: 高速无人水面艇的路径规划需要更复杂的解决方案以缩短航行时间并节约能源。本文提出了一种融合时间信息与预测势能的新型预测人工势场法，用于规划更平滑的路径。研究在考虑艇体动力学特性和局部极小值可达性的基础上，深入探讨了人工势场法的原理。首先分析了最先进的传统人工势场法及其在全局与局部路径规划中的局限性，随后针对预测人工势场法提出三项改进措施——角度限制、速度调节和预测势能，以提升生成路径的可行性与平顺性。通过传统方法与预测人工势场法的对比实验表明，后者能有效限制最大转向角度、缩短航行时间并实现智能避障。仿真结果进一步验证了预测人工势场法能够解决凹形局部极小值问题，提升特殊场景下的可达性，最终为无人水面艇生成更高效的路径，实现航行时间与能源消耗的双重优化。

---

