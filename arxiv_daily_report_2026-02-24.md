# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-02-24 10:33

**今日新增**: 15 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 5/15 篇提供

**🌟 Highlight**: 3 篇 | **📌 Poster**: 12 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图*

---

### 1. WildOS: Open-Vocabulary Object Search in the Wild

- **作者**: Hardik Shah, Erica Tevere, Deegan Atha, Marcel Kaufmann, Shehryar Khattak, Manthan Patel, Marco Hutter, Jonas Frey, Patrick Spieler
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.19308v1)
- **发表日期**: 2026-02-22
- **匹配关键词**: exploration, semantic navigation, navigation, autonomous navigation
- **arXiv**: [2602.19308v1](http://arxiv.org/abs/2602.19308v1)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://leggedrobotics.github.io/wildos/
- **中文摘要**: 在复杂、非结构化的户外环境中实现自主导航，要求机器人能够在无先验地图且深度感知受限的情况下进行长距离作业。在此类场景中，仅依赖几何边界进行探索往往不够充分，而通过语义推理判断行进方向与安全路径的能力，对于实现稳健高效的探索至关重要。本研究提出WildOS系统——一个结合安全几何探索与语义视觉推理的长距离开放词汇目标搜索统一框架。该系统通过构建稀疏导航图以维持空间记忆，并利用基于基础模型的视觉模块ExploRFM对图的边界节点进行评分。ExploRFM能够在图像空间中同步预测可通行性、视觉边界及目标相似度，从而实现实时的机载语义导航任务。这种基于视觉评分的导航图使机器人能够在确保几何安全的前提下，沿具有语义意义的方向进行探索。此外，我们引入一种基于粒子滤波的开放词汇目标粗定位方法，可估算超出机器人即时深度感知范围的候选目标位置，从而实现对远距离目标的有效路径规划。通过在多种越野与城市地形中进行的大量闭环实地实验表明，WildOS系统能够实现稳健的自主导航，在效率与自主性方面显著优于纯几何方法与纯视觉基线方案。我们的研究成果凸显了视觉基础模型在推动兼具语义感知与几何约束的开放世界机器人行为方面的潜力。项目页面：https://leggedrobotics.github.io/wildos/

---

### 2. Learning to Localize Reference Trajectories in Image-Space for Visual Navigation

- **作者**: Finn Lukas Busch, Matti Vahs, Quantao Yang, Jesús Gerardo Ortega Peimbert, Yixi Cai, Jana Tumova, Olov Andersson
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.18803v1)
- **发表日期**: 2026-02-21
- **匹配关键词**: visual navigation, navigation
- **arXiv**: [2602.18803v1](http://arxiv.org/abs/2602.18803v1)
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出LoTIS模型，这是一种视觉导航模型，通过将参考RGB轨迹定位到机器人当前视野中，提供与机器人无关的图像空间引导，无需相机标定、位姿信息或针对特定机器人的训练。与预测绑定特定机器人的动作不同，我们预测参考轨迹在机器人当前视野中呈现的图像空间坐标。这种设计创造了与机器人无关的视觉引导，可轻松与局部规划系统集成。因此，我们的模型能够实现跨不同机器人平台的零样本引导能力。通过将感知与动作解耦，并学习定位轨迹点而非模仿行为先验，我们采用跨轨迹训练策略以增强对视角和相机变化的鲁棒性。在传统前向导航任务中，我们的成功率比现有最优方法高出20-50个百分点，在多种仿真和真实环境中达到94-98%的成功率。此外，在基线方法失效的挑战性任务（如反向行进）中，我们实现了超过5倍的性能提升。本系统使用简便：我们演示了如何仅用手机拍摄的视频就能让不同机器人导航至轨迹上的任意点。视频、演示及代码详见https://finnbusch.com/lotis。

---

### 3. Scout-Rover cooperation: online terrain strength mapping and traversal risk estimation for planetary-analog explorations

- **作者**: Shipeng Liu, J. Diego Caporale, Yifeng Zhang, Xingjue Liao, William Hoganson, Wilson Hu, Shivangi Misra, Neha Peddinti, Rachel Holladay, Ethan Fulcher, Akshay Ram Panyam, Andrik Puentes, Jordan M. Bretzfelder, Michael Zanetti, Uland Wong, Daniel E. Koditschek, Mark Yim, Douglas Jerolmack, Cynthia Sung, Feifei Qian
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.18688v1)
- **发表日期**: 2026-02-21
- **匹配关键词**: exploration, path planning, navigation
- **arXiv**: [2602.18688v1](http://arxiv.org/abs/2602.18688v1)
- **🔒 开源**: 未提及
- **中文摘要**: 机器人辅助的行星表面探测对于理解地质过程至关重要，然而许多具有重要科学价值的区域——如火星沙丘和月球陨石坑——因存在松散易变形的风化层而充满危险。本文提出一种侦察车-漫游车协同框架，通过腿式与轮式机器人组成的混合团队扩展对此类地形的安全探测能力。在该框架中，高机动性腿式机器人作为移动侦察单元，利用本体感知的腿-地形交互作用在行进过程中实时评估风化层强度，并构建空间分辨率地形图。这些地图与漫游车运动模型相结合，用于评估穿越风险并指导路径规划。

我们在NASA艾姆斯月球模拟试验场和白沙国家公园沙丘区通过模拟任务验证了该框架。实验证明：（1）基于腿式运动的实时地形强度测绘可行；（2）针对特定漫游车的穿越风险评估能实现科学目标的安全导航。结果表明，侦察单元生成的地形图能可靠捕捉空间变异特征并预测移动故障模式，从而实现规避危险区域的风险感知路径规划。通过将具身化地形感知与异构漫游车协同相结合，该框架增强了可变形行星环境中的操作鲁棒性，拓展了可抵达的科学工作空间。

---

## 📌 Poster

*其他相关研究*

---

### 1. Online Navigation Planning for Long-term Autonomous Operation of Underwater Gliders

- **作者**: Victor-Alexandru Darvariu, Charlotte Z. Reed, Jan Stratmann, Bruno Lacerda, Benjamin Allsup, Stephen Woodward, Elizabeth Siddle, Trishna Saeharaseelan, Owain Jones, Dan Jones, Tobias Ferreira, Chloe Baker, Kevin Chaplin, James Kirk, Ashley Morris, Ryan Patmore, Jeff Polton, Charlotte Williams, Alexandra Kokkinaki, Alvaro Lorenzo Lopez, Justin J. H. Buck, Nick Hawes
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.19315v1)
- **发表日期**: 2026-02-22
- **匹配关键词**: navigation
- **arXiv**: [2602.19315v1](http://arxiv.org/abs/2602.19315v1)
- **🔒 开源**: 未提及
- **中文摘要**: 水下滑翔机器人已成为海洋采样不可或缺的工具。尽管相关方呼吁开发工具以管理日益庞大的滑翔机群，但迄今为止成功的自主长期部署案例仍然稀少，这表明缺乏合适的方法论和系统。本研究将滑翔机导航规划构建为随机最短路径马尔可夫决策过程，并提出基于蒙特卡洛树搜索的采样在线规划器。采样通过物理信息模拟器生成，该模拟器在保持计算可行性的同时，能捕捉控制执行的不确定性和洋流预测。模拟器参数通过历史滑翔机数据进行拟合。我们将这些方法集成至Slocum滑翔机的自主指挥控制系统中，实现每次上浮时的闭环重规划。该集成系统在北海开展的两次实地部署中得到验证，累计实现约3个月、1000公里的自主航行。结果表明，相较于直线航向导航，该系统能提升航行效率，并证明了采样规划方法在长期海洋自主作业中的实用性。

---

### 2. Safe and Interpretable Multimodal Path Planning for Multi-Agent Cooperation

- **作者**: Haojun Shi, Suyu Ye, Katherine M. Guerrerio, Jianzhi Shen, Yifan Yin, Daniel Khashabi, Chien-Ming Huang, Tianmin Shu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.19304v1)
- **发表日期**: 2026-02-22
- **匹配关键词**: path planning
- **arXiv**: [2602.19304v1](http://arxiv.org/abs/2602.19304v1)
- **🔒 开源**: 未提及
- **中文摘要**: 分散式智能体间的成功协作要求每个智能体能够快速根据其他智能体的行为调整自身计划。在智能体难以准确预测彼此意图与行动方案的情境中，语言交流对保障安全至关重要。本研究聚焦路径层面的协作问题——智能体需通过相互调整行动路径以避免碰撞或完成物理协作任务（如协同搬运）。我们提出一种安全可解释的多模态路径规划方法CaPE（代码即路径编辑器），该方法能根据环境信息与其他智能体的语言交流，生成并动态更新智能体的行动路径。CaPE利用视觉语言模型合成经模型规划器验证的路径编辑程序，通过安全可解释的方式将语言交流转化为路径规划的调整依据。我们在多样化仿真与真实场景中评估该方法，包括自动驾驶、家庭环境及协同搬运任务中的多机器人协作与人机协作。实验结果表明，CaPE可作为即插即用模块集成至不同机器人系统，显著提升机器人根据其他机器人或人类语言交流调整行动规划的能力。研究同时证明，基于视觉语言模型的路径编辑程序合成与模型规划安全机制的融合，使机器人在保持安全性与可解释性的同时，能够实现开放式的协作任务。

---

### 3. 3D Shape Control of Extensible Multi-Section Soft Continuum Robots via Visual Servoing

- **作者**: Abhinav Gandhi, Shou-Shan Chiang, Cagdas D. Onal, Berk Calli
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.19273v1)
- **发表日期**: 2026-02-22
- **匹配关键词**: visual servoing, object manipulation
- **arXiv**: [2602.19273v1](http://arxiv.org/abs/2602.19273v1)
- **🔒 开源**: 未提及
- **中文摘要**: 本文提出了一种新颖的基于视觉的控制算法，用于调节可扩展多节段软体连续型机械臂的整体形态。与现有文献中仅调控机器人末端执行器位姿的视觉控制算法不同，我们提出的控制算法能够调控机器人的整体构型，从而充分利用其运动学冗余特性。相较于文献中报道存在局部极小值问题的相近研究，我们基于模型的2.5维形态视觉伺服方法在机器人三维工作空间中实现了全局稳定的渐近收敛。与现有视觉伺服算法相比，该方法无需依赖本体感知传感器的信息，适用于不具备此类传感能力的连续型机械臂。机器人状态完全通过外部摄像头采集的图像进行估计，该摄像头同时观测机器人整体形态并用于闭合形态控制回路。传统视觉伺服方案需要获取参考位姿下的机器人图像以生成参考特征，而本研究通过逆运动学求解器直接为目标构型生成参考特征，无需实际获取参考位姿图像。在多节段连续型机械臂上进行的实验表明，该控制器在精确定位末端执行器的同时，能够有效调控机器人整体形态。实验结果验证了控制器在保持平滑瞬态响应的前提下，可将稳态误差控制在1毫米以内，成功实现了连续型机器人的形态调控。通过概念验证性物体操作实验（包括堆叠、倾倒和牵引任务），进一步证明了该控制器的实际应用潜力。

---

### 4. Human-to-Robot Interaction: Learning from Video Demonstration for Robot Imitation

- **作者**: Thanh Nguyen Canh, Thanh-Tuan Tran, Haolan Zhang, Ziyan Gao, Nak Young Chong, Xiem HoangVan
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.19184v1)
- **发表日期**: 2026-02-22
- **匹配关键词**: HRI
- **arXiv**: [2602.19184v1](http://arxiv.org/abs/2602.19184v1)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://thanhnguyencanh.github.io/LfD4hri.
- **中文摘要**: 从演示中学习（LfD）为机器人技能获取提供了一种前景广阔的模式。现有方法尝试直接从视频演示中提取操作指令，但仍面临两大关键挑战：（1）通用视频描述模型侧重于全局场景特征而非任务相关物体，生成的描述难以用于精确的机器人执行；（2）将视觉理解与策略学习耦合的端到端架构需要大量配对数据集，且难以跨物体和场景泛化。为突破这些局限，受人类通过观察模仿进行学习的能力启发，我们提出了一种创新的“人机交互”模仿学习框架，使机器人能够直接从非结构化视频演示中获取操作技能。该框架的核心创新在于模块化设计，将学习过程解耦为两个独立阶段：（1）视频理解阶段，通过时序移位模块（TSM）与视觉语言模型（VLM）相结合，提取动作并识别交互物体；（2）机器人模仿阶段，采用基于TD3的深度强化学习执行演示操作。我们在PyBullet仿真环境（使用UR5e机械臂）和真实场景（使用UF850机械臂）中验证了该方法，涵盖到达、抓取、移动、放置四项基础动作。在视频理解方面，本方法在标准物体上实现89.97%的动作分类准确率，BLEU-4得分达0.351；在新物体上BLEU-4得分为0.265，较最佳基线分别提升76.4%和128.4%。在机器人操作方面，框架在所有动作中平均成功率87.5%，其中到达任务成功率100%，复杂抓放操作成功率最高达90%。项目网站详见https://thanhnguyencanh.github.io/LfD4hri。

---

### 5. Understanding Fire Through Thermal Radiation Fields for Mobile Robots

- **作者**: Anton R. Wagner, Madhan Balaji Rao, Xuesu Xiao, Sören Pirk
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.19108v1)
- **发表日期**: 2026-02-22
- **匹配关键词**: navigation, robot navigation
- **arXiv**: [2602.19108v1](http://arxiv.org/abs/2602.19108v1)
- **🔒 开源**: 未提及
- **中文摘要**: 在火灾影响环境中安全移动是部署于灾难响应场景的自主移动机器人必须具备的关键能力。本研究提出一种创新方法，使移动机器人能够通过构建实时热辐射场来理解火情。我们通过配准深度图像与热成像数据，获得带有温度标注的三维点云。基于这些数据，我们识别火源并运用斯特藩-玻尔兹曼定律估算空白区域的热辐射强度，从而构建覆盖整个环境的连续热辐射场。研究表明，该表征方法可应用于机器人导航系统——通过将热辐射约束嵌入代价地图，计算机器人可通行的热安全路径。我们在受控实验环境中使用波士顿动力Spot机器人验证了该方法的有效性，实验证明机器人能够在规避危险区域的同时完成导航任务。本方法为自主部署于火灾环境的移动机器人技术开辟了新路径，在搜救、消防及危险物质处置等领域具有广阔应用前景。

---

### 6. Path planning for unmanned surface vehicle based on predictive artificial potential field. International Journal of Advanced Robotic Systems

- **作者**: Jia Song, Ce Hao, Jiangcheng Su
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.19062v1)
- **发表日期**: 2026-02-22
- **匹配关键词**: path planning
- **arXiv**: [2602.19062v1](http://arxiv.org/abs/2602.19062v1)
- **🔒 开源**: 未提及
- **中文摘要**: 高速无人水面艇的路径规划需要更复杂的解决方案以缩短航行时间并节约能源。本文提出了一种融合时间信息与预测势能的新型预测人工势场法，用于规划更平滑的路径。研究在考虑艇体动力学特性和局部极小值可达性的基础上，深入探讨了人工势场法的基本原理。首先分析了最先进的传统人工势场法及其在全局与局部路径规划中的局限性，随后针对预测人工势场法提出三项改进措施——角度限制、速度调节和预测势能，以提升生成路径的可行性与平顺性。通过传统方法与预测人工势场法的对比实验表明，后者能有效限制最大转向角度、缩短航行时间并实现智能避障。仿真结果进一步验证了预测人工势场法能够解决凹形局部极小值问题，提升特殊场景下的可达性，最终为无人水面艇生成更高效的路径，实现航行时间与能源消耗的双重优化。

---

### 7. A Checklist for Deploying Robots in Public: Articulating Tacit Knowledge in the HRI Community

- **作者**: Claire Liang, Franziska Babel, Hannah Pelikan, Sydney Thompson, Xiang Zhi Tan
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.19038v1)
- **发表日期**: 2026-02-22
- **匹配关键词**: HRI
- **arXiv**: [2602.19038v1](http://arxiv.org/abs/2602.19038v1)
- **🔓 开源**: CODE
- **中文摘要**: 尽管在机器人公开部署实践中存在许多共性问题，但大量实际挑战仍未被系统记录。这种状况不仅抬高了研究门槛，更导致可避免的错误反复出现。为将人机交互领域的隐性知识显性化，本研究以清单形式提出一套指导框架，助力研究者开展公共场景机器人部署工作。基于团队在公共机器人部署中的实践经验，我们系统梳理了公共人机交互研究的关键议题，并将其构建为分层表格中的模块化翻转卡片体系，按部署阶段与核心领域进行结构化组织。通过对六位跨学科公共人机交互专家的深度访谈，我们展示了社区智慧如何优化清单架构。研究进一步通过真实公共场景案例演示了清单的实际应用。最终，我们以开源可定制社区资源的形式发布该清单——它既能汇聚集体智慧实现持续演进，也可作为清单文件、卡片套装及交互式网络工具投入实际使用。

---

### 8. Bumper Drone: Elastic Morphology Design for Aerial Physical Interaction

- **作者**: Pongporn Supa, Alex Dunnett, Feng Xiao, Rui Wu, Mirko Kovac, Basaran Bahadir Kocer
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.18976v1)
- **发表日期**: 2026-02-21
- **匹配关键词**: exploration, navigation, obstacle avoidance
- **arXiv**: [2602.18976v1](http://arxiv.org/abs/2602.18976v1)
- **🔒 开源**: 未提及
- **中文摘要**: 空中机器人正从规避障碍物向利用环境接触交互进行导航、探索与操作的方向演进。此类空中物理交互的核心挑战在于处理未知目标上的不确定接触力，这通常需要精确传感与主动控制。我们研发了一款配备弹性触角的无人机平台，可实现"接触即离"机动——这是一种通过自我调节的连续碰撞运动，使无人机在不依赖主动避障的情况下保持与墙面的邻近状态。该平台将环境交互作为具身控制的一种形式，其底层稳定与近障碍导航能力源于无人机-障碍物系统（类似质量-弹簧-阻尼系统）的被动动态响应。实验表明，弹性触角在吸收冲击能量的同时能维持飞行器稳定性，与刚性触角构型相比俯仰振荡降低38%。低位触角布局更可将俯仰振荡减少约54%。除间歇性接触外，配备弹性触角的平台仅依靠标准姿态PID控制器，还能实现与静态物体的稳定持续接触。

---

### 9. Temporal-Logic-Aware Frontier-Based Exploration

- **作者**: Azizollah Taheri, Derya Aksaray
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.18951v1)
- **发表日期**: 2026-02-21
- **匹配关键词**: exploration, motion planning
- **arXiv**: [2602.18951v1](http://arxiv.org/abs/2602.18951v1)
- **🔒 开源**: 未提及
- **中文摘要**: 本文研究了在未知环境中自主机器人的时序逻辑运动规划问题。目标是在期望标签的确切位置未知的情况下，使机器人能够满足语法协同安全的线性时序逻辑规范。我们引入了一种新型自动机状态，称为承诺状态。这些状态捕捉了由不可逆行动产生的中间任务进展。换言之，在执行那些导致承诺状态的行动后，某些未来满足任务的路径将变得不可行。通过利用承诺状态，我们提出了一种基于前沿探索的完备算法，该算法能策略性地引导机器人在保持所有可能满足任务方式的同时推进任务进展。仿真实验验证了所提方法的有效性。

---

### 10. TPRU: Advancing Temporal and Procedural Understanding in Large Multimodal Models

- **作者**: Zhenkun Gao, Xuhong Wang, Xin Tan, Yuan Xie
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.18884v1)
- **发表日期**: 2026-02-21
- **匹配关键词**: navigation
- **arXiv**: [2602.18884v1](http://arxiv.org/abs/2602.18884v1)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/Stephen-gzk/TPRU/
- **中文摘要**: 多模态大语言模型（MLLMs），特别是可部署的小型变体，在理解时序和流程性视觉数据方面存在显著缺陷，这一瓶颈阻碍了其在现实世界具身人工智能中的应用。该问题主要源于训练范式的系统性缺失——缺乏大规模、流程连贯的数据。为解决这一难题，我们提出了TPRU数据集，该数据集源自机器人操作和图形界面导航等多种具身场景，通过时序重排、下一帧预测和上一帧回顾三项互补任务进行系统性设计，以培养时序推理能力。其关键特征在于引入具有挑战性的负样本，迫使模型从被动观察转向主动的跨模态验证。我们结合强化学习微调方法利用TPRU数据集，重点提升资源高效型模型的性能。实验表明该方法带来显著提升：在我们手动构建的TPRU测试集上，TPRU-7B模型的准确率从50.33%跃升至75.70%，这一突破性成果显著超越了包括GPT-4o在内的更大规模基线模型。更重要的是，这些能力展现出良好的泛化性，在现有基准测试中实现了实质性改进。相关代码库已发布于https://github.com/Stephen-gzk/TPRU/。

---

### 11. HeRO: Hierarchical 3D Semantic Representation for Pose-aware Object Manipulation

- **作者**: Chongyang Xu, Shen Cheng, Haipeng Li, Haoqiang Fan, Ziliang Feng, Shuaicheng Liu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.18817v1)
- **发表日期**: 2026-02-21
- **匹配关键词**: object manipulation
- **arXiv**: [2602.18817v1](http://arxiv.org/abs/2602.18817v1)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/Chongyang-99/HeRO.
- **中文摘要**: 机器人操作的模仿学习已从二维图像策略发展到明确编码几何信息的三维表示。然而，纯几何策略往往缺乏显式的部件级语义，而这对于姿态感知操作（例如区分鞋头与鞋跟）至关重要。本文提出HeRO——一种基于扩散模型的策略，通过分层语义场耦合几何与语义信息。HeRO采用密集语义提升技术，将DINOv2具有判别性的几何敏感特征与Stable Diffusion提供的平滑全局一致性对应关系相融合，生成兼具细粒度特性和空间一致性的密集特征。这些特征经过处理与划分后，构建出全局场和一组局部场。通过置换不变网络架构，分层条件模块将全局场和局部场作为生成去噪器的条件输入，从而避免顺序敏感偏差，为姿态感知操作生成连贯的控制策略。在多项测试中，HeRO创造了新的性能标杆，在"放置双鞋"任务上成功率提升12.3%，并在六项具有挑战性的姿态感知任务中平均获得6.5%的性能提升。代码发布于https://github.com/Chongyang-99/HeRO。

---

### 12. Temporal Action Representation Learning for Tactical Resource Control and Subsequent Maneuver Generation

- **作者**: Hoseong Jung, Sungil Son, Daesol Cho, Jonghae Park, Changhyun Choi, H. Jin Kim
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.18716v1)
- **发表日期**: 2026-02-21
- **匹配关键词**: navigation
- **arXiv**: [2602.18716v1](http://arxiv.org/abs/2602.18716v1)
- **🔒 开源**: 未提及
- **中文摘要**: 自主机器人系统应能对资源控制及其对后续机动动作的影响进行推理，这在能量预算有限或感知受限的操作场景中尤为重要。基于学习的控制方法能有效处理复杂动态系统，并将问题建模为统一离散资源使用与连续机动动作的混合动作空间。然而，现有混合动作空间研究未能充分捕捉资源使用与机动动作之间的因果依赖关系，同时忽略了战术决策的多模态特性，这两者在快速演变的场景中至关重要。本文提出TART——一种面向战术资源控制与后续机动动作生成的时序动作表征学习框架。TART基于互信息目标构建对比学习机制，旨在捕捉资源-机动交互中固有的时序依赖关系。通过学习得到的表征被量化为离散码本条目，用于条件化策略生成，从而捕获循环出现的战术模式，实现多模态且时序连贯的行为决策。我们在两个资源部署至关重要的领域评估TART：（i）迷宫导航任务中，有限离散动作预算可提供增强的移动能力；（ii）高保真空战模拟环境中，F-16智能体需协调武器系统、防御系统与飞行机动动作。实验表明，TART在两个领域均持续优于混合动作基线方法，验证了其在利用有限资源生成情境感知的后续机动动作方面的有效性。

---

