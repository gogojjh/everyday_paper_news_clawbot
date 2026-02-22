# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-02-22 15:27

**今日新增**: 15 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 2/15 篇提供

**🌟 Highlight**: 1 篇 | **📌 Poster**: 14 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图*

---

### 1. Benchmarking the Effects of Object Pose Estimation and Reconstruction on Robotic Grasping Success

- **作者**: Varun Burde, Pavel Burget, Torsten Sattler
- **发表日期**: 2026-02-19
- **匹配关键词**: object manipulation
- **arXiv**: [2602.17101v1](http://arxiv.org/abs/2602.17101v1)
- **🔒 开源**: 未提及
- **中文摘要**: 三维重建是机器人感知任务的基础层，涵盖六维物体姿态估计与抓取姿态生成等关键领域。当前基于多视角图像的三维物体重建方法能够生成视觉与几何表现俱佳的网格模型，但传统几何评估指标无法反映重建质量对机器人操作性能等下游任务的实际影响。本文通过构建大规模物理仿真基准填补这一空白，该基准以抓取功能有效性为核心，系统评估六维姿态估计器与三维网格模型的综合性能。我们通过在不同重建网格上生成抓取姿态，并在真实物体模型上执行仿真实验，探究基于非完美模型生成的抓取姿态如何影响实际物体交互，从而综合评估姿态误差、抓取鲁棒性及三维重建几何误差的耦合效应。实验表明：重建伪影会显著减少可行抓取姿态数量，但在姿态估计准确的前提下对抓取成功率影响甚微；抓取成功率与姿态误差的关系主要受空间误差主导，即使简单的平移误差也能有效预测对称物体的抓取成功率。本研究为理解感知系统与机器人物体操控的关联机制提供了新的视角。

---

## 📌 Poster

*其他相关研究*

---

### 1. Graph Neural Model Predictive Control for High-Dimensional Systems

- **作者**: Patrick Benito Eberhard, Luis Pabon, Daniele Gammelli, Hugo Buurmeijer, Amon Lahr, Mark Leone, Andrea Carron, Marco Pavone
- **发表日期**: 2026-02-19
- **匹配关键词**: obstacle avoidance
- **arXiv**: [2602.17601v1](http://arxiv.org/abs/2602.17601v1)
- **🔒 开源**: 未提及
- **中文摘要**: 对软体机器人等高维系统的控制，需要既能精确捕捉复杂动态特性又保持计算可行性的模型。本研究提出一种框架，将基于图神经网络（GNN）的动态模型与结构利用模型预测控制相结合，实现对高维系统的实时控制。通过将系统表示为具有局部交互作用的图结构，GNN保持了稀疏性，而定制化的凝聚算法则从控制问题中消除状态变量，确保计算效率。该凝聚算法的复杂度随系统节点数量线性增长，并利用图形处理器（GPU）并行化实现实时性能。所提方法在仿真和物理软体机器人躯干实验中均得到验证。结果表明，该方法可扩展至1000个节点系统在100赫兹闭环频率下运行，在硬件上实现亚厘米精度的实时参考轨迹跟踪，性能较基线方法提升63.6%。最后，我们展示了该方法实现有效全身避障的能力。

---

### 2. FR-GESTURE: An RGBD Dataset For Gesture-based Human-Robot Interaction In First Responder Operations

- **作者**: Konstantinos Foteinos, Georgios Angelidis, Aggelos Psiris, Vasileios Argyriou, Panagiotis Sarigiannidis, Georgios Th. Papadopoulos
- **发表日期**: 2026-02-19
- **匹配关键词**: human-robot interaction
- **arXiv**: [2602.17573v1](http://arxiv.org/abs/2602.17573v1)
- **🔓 开源**: CODE
- **中文摘要**: 灾害强度和频次的持续攀升使得应急救援人员的工作愈发艰巨。人工智能与机器人技术有望通过辅助操作来缓解这些困难。为此，我们提出一套面向应急救援人员手势控制无人地面车辆的数据集，借鉴现有应急救援手势与战术手语体系，结合资深救援人员反馈优化后，最终形成包含12种指令的手势集。通过双视角七距离的采集方式，共获得3312组RGBD配对数据。据我们所知，这是首个专门针对应急救援人员手势引导无人地面车辆的数据集。我们为这套命名为FR-GESTURE的RGBD数据集制定了评估标准，并进行了有待改进的基线实验。为促进该领域研究发展，数据已公开共享：https://doi.org/10.5281/zenodo.18131333。

---

### 3. RA-Nav: A Risk-Aware Navigation System Based on Semantic Segmentation for Aerial Robots in Unpredictable Environments

- **作者**: Ziyi Zong, Xin Dong, Jinwu Xiang, Daochun Li, Zhan Tu
- **发表日期**: 2026-02-19
- **匹配关键词**: robot navigation, navigation
- **arXiv**: [2602.17515v1](http://arxiv.org/abs/2602.17515v1)
- **🔒 开源**: 未提及
- **中文摘要**: 现有空中机器人导航系统通常围绕静态和动态障碍物规划路径，但当静态障碍物突然移动时无法适应。通过整合环境语义感知能力，能够评估突然移动障碍物带来的潜在风险。本文提出RA-Nav——一种基于语义分割的风险感知导航框架。轻量级多尺度语义分割网络实时识别障碍物类别，进一步将其划分为三类：静止型、暂时静态型和动态型。针对每种类型设计相应的风险估计函数，实现实时风险预测，并据此构建完整的局部风险地图。基于该地图，设计风险感知路径搜索算法，确保规划在路径效率与安全性之间取得平衡。随后应用轨迹优化技术，生成安全、平滑且符合动力学可行性的轨迹。对比仿真表明，在突发障碍物状态转换场景中，RA-Nav相比基线方法实现了更高的成功率。通过真实世界数据进行的仿真进一步验证了该框架的有效性。

---

### 4. Distributed Virtual Model Control for Scalable Human-Robot Collaboration in Shared Workspace

- **作者**: Yi Zhang, Omar Faris, Chapa Sirithunge, Kai-Fung Chu, Fumiya Iida, Fulvio Forni
- **发表日期**: 2026-02-19
- **匹配关键词**: human-robot collaboration
- **arXiv**: [2602.17415v1](http://arxiv.org/abs/2602.17415v1)
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出一种基于虚拟模型控制（VMC）的去中心化、智能体无关且具备安全感知的人机协作控制框架。在该框架中，人类与机器人被置于同一虚拟组件构成的工作空间内，其运动通过与虚拟弹簧和阻尼器的交互产生，而非依赖显式轨迹规划。我们采用去中心化的基于力的停滞检测器识别死锁状态，并通过协商机制予以解决。实验表明，该方法将机器人在积木放置任务中的卡死概率从最高61.2%降至零。得益于分布式架构，该框架无需结构调整即可实现规模扩展：实验中我们实现了最多两台机器人与两名人类的安全协作，在仿真中更扩展至四台机器人，同时保持智能体间约20厘米的间隔距离。结果表明，通过调整控制参数可直观塑造机器人行为，并在所有测试场景中实现不同团队规模下的无死锁运行。

---

### 5. Flickering Multi-Armed Bandits

- **作者**: Sourav Chakraborty, Amit Kiran Rege, Claire Monteleoni, Lijun Chen
- **发表日期**: 2026-02-19
- **匹配关键词**: exploration, navigation
- **arXiv**: [2602.17315v1](http://arxiv.org/abs/2602.17315v1)
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出闪烁多臂赌博机（FMAB）这一新型MAB框架，其中可用臂集（或行动集）每轮都可能发生变化，且任意时刻的可用集合可能取决于智能体先前选择的臂。我们通过随机图过程对这种受限且动态变化的可用性进行建模，其中臂对应节点，智能体的移动被限制在其局部邻域内。我们在两种随机图模型下分析该问题：独立同分布的埃尔德什-雷尼（ER）过程和边马尔可夫过程。我们提出并分析了一种两阶段算法：该算法首先采用惰性随机游走进行探索以高效识别最优臂，随后通过导航与锁定阶段进行利用。我们为两种图设置建立了高概率且期望的次线性遗憾界。通过为该问题类别建立匹配的信息论下界，我们证明了算法探索成本的近优特性，揭示了局部移动约束下探索的根本代价。我们通过数值模拟补充理论保证，包括地面机器人侦察受灾区域的场景模拟。

---

### 6. Multi-session Localization and Mapping Exploiting Topological Information

- **作者**: Lorenzo Montano-Olivan, Julio A. Placed, Luis Montano, Maria T. Lazaro
- **发表日期**: 2026-02-19
- **匹配关键词**: localization and mapping
- **arXiv**: [2602.17226v1](http://arxiv.org/abs/2602.17226v1)
- **🔒 开源**: 未提及
- **中文摘要**: 在已访问环境中进行操作对自主系统而言正变得日益重要，其在自动驾驶、测绘以及仓储或家庭机器人等领域具有直接应用价值。这种对相同区域的重复观测给建图与定位——实现任何高级任务的关键环节——带来了重大挑战。与当前普遍采用的贪婪式运行完整SLAM会话并试图在生成地图间建立对应关系的做法不同，本研究提出了一种基于地图定位的新型多会话框架。我们的方法引入了拓扑感知、不确定性决策机制，通过分析位姿图结构来检测低连通性区域，并选择性触发建图与闭环检测模块。生成的增量地图与位姿图可无缝整合至现有模型中，有效降低累积误差并提升全局一致性。我们在数据集的重叠序列上验证了该方法，并在真实矿井类环境中证明了其有效性。

---

### 7. Physical Human-Robot Interaction for Grasping in Augmented Reality via Rigid-Soft Robot Synergy

- **作者**: Huishi Huang, Jack Klusmann, Haozhe Wang, Shuchen Ji, Fengkang Ying, Yiyuan Zhang, John Nassour, Gordon Cheng, Daniela Rus, Jun Liu, Marcelo H Ang, Cecilia Laschi
- **发表日期**: 2026-02-19
- **匹配关键词**: human-robot interaction
- **arXiv**: [2602.17128v1](http://arxiv.org/abs/2602.17128v1)
- **🔒 开源**: 未提及
- **中文摘要**: 混合刚柔机器人结合了刚性机械臂的精确性与柔性臂的顺应性和适应性，为在非结构化环境中实现多功能抓取提供了前景广阔的方法。然而，由于建模、感知和跨域运动学方面的困难，协调混合机器人仍然具有挑战性。本研究提出了一种基于增强现实（AR）的新型物理人机交互框架，能够直接远程操控混合刚柔机器人完成简单的到达和抓取任务。通过使用AR头显设备，用户可与集成于通用物理引擎的机器人系统仿真模型进行交互，该模型叠加在真实系统之上，允许在实际部署前进行模拟执行。为确保虚拟机器人与物理机器人行为一致，我们引入了一种从真实到仿真的参数识别流程，该流程利用柔性机器人固有的几何特性，能够精确建模其静态和动态行为以及控制系统的响应。

---

### 8. Grasp Synthesis Matching From Rigid To Soft Robot Grippers Using Conditional Flow Matching

- **作者**: Tanisha Parulekar, Ge Shi, Josh Pinskier, David Howard, Jen Jen Chung
- **发表日期**: 2026-02-19
- **匹配关键词**: grasp synthesis
- **arXiv**: [2602.17110v1](http://arxiv.org/abs/2602.17110v1)
- **🔒 开源**: 未提及
- **中文摘要**: 刚性夹爪与柔性夹爪在抓取合成方法上存在表征差异。现有研究如Anygrasp[1]等多数抓取合成方法主要针对刚性平行夹爪设计，将其直接应用于柔性夹爪时往往难以捕捉其特有的顺应行为，导致模型训练数据需求量大且精度不足。为弥合这一差距，本文提出一种创新框架，将刚性夹爪模型的抓取姿态映射至柔性鳍条夹爪。我们采用条件流匹配这一生成模型来学习这种复杂变换。研究方法包含构建数据采集流程以生成配对的刚性-柔性抓取姿态，并利用U-Net自编码器根据深度图像中的物体几何特征对CFM模型进行条件约束，使其能够学习从初始Anygrasp姿态到稳定鳍条夹爪姿态的连续映射。通过在七自由度机器人上的实验验证，本方法生成的抓取姿态相较于基线刚性姿态（成功率分别为6%和25%），在执行柔性抓取时对已知与未知物体均取得更高综合成功率（分别为34%和46%）。该模型在柱状物体（已知/未知物体成功率50%/100%）和球状物体（已知/未知物体成功率25%/31%）上表现尤为突出，并能有效泛化至未见物体。本研究证明CFM是一种数据高效且有效的抓取策略迁移方法，为其他软体机器人系统提供了可扩展的技术路径。

---

### 9. Bluetooth Phased-array Aided Inertial Navigation Using Factor Graphs: Experimental Verification

- **作者**: Glen Hjelmerud Mørkbak Sørensen, Torleiv H. Bryne, Kristoffer Gryte, Tor Arne Johansen
- **发表日期**: 2026-02-19
- **匹配关键词**: navigation
- **arXiv**: [2602.17407v1](http://arxiv.org/abs/2602.17407v1)
- **🔒 开源**: 未提及
- **中文摘要**: 相控阵蓝牙系统已成为在仓库物流、无人机着陆和自主对接等全球导航卫星系统受限场景下实现辅助惯性导航的低成本替代方案。基于商用现成组件构建导航系统可降低相控阵无线电导航系统的应用门槛，但代价是测量噪声显著增加且有效作用距离相对较短。本文通过多旋翼无人机飞行实验数据，比较了基于因子图优化估计器的鲁棒估计策略。我们评估了在蓝牙角度测量辅助下，结合距离或气压测量时，系统在全球导航卫星信号丢失场景中的性能表现。

---

### 10. NRGS-SLAM: Monocular Non-Rigid SLAM for Endoscopy via Deformation-Aware 3D Gaussian Splatting

- **作者**: Jiwei Shan, Zeyu Cai, Yirui Li, Yongbo Chen, Lijun Han, Yun-hui Liu, Hesheng Wang, Shing Shin Cheng
- **发表日期**: 2026-02-19
- **匹配关键词**: navigation, localization and mapping
- **arXiv**: [2602.17182v1](http://arxiv.org/abs/2602.17182v1)
- **🔓 开源**: CODE
- **中文摘要**: 视觉同步定位与建图（V-SLAM）是实现自主感知与导航的基础能力。然而，内窥镜场景因持续的软组织形变而违背了刚性假设，导致相机自身运动与内在形变之间存在强烈的耦合模糊性。尽管近期单目非刚性SLAM方法取得了显著进展，但它们往往缺乏有效的解耦机制，并依赖稀疏或低保真度的场景表示，从而导致跟踪漂移和重建质量受限。为应对这些挑战，我们提出了NRGS-SLAM——一种基于3D高斯泼溅的内窥镜单目非刚性SLAM系统。为解决耦合模糊性问题，我们引入了形变感知的3D高斯地图，通过为每个高斯基元添加可学习的形变概率进行增强，并采用贝叶斯自监督策略进行优化，无需依赖外部非刚性标注。基于此表示方法，我们设计了可变形跟踪模块，通过优先处理低形变区域实现鲁棒的由粗到精姿态估计，随后进行高效的逐帧形变更新。精心设计的可变形建图模块能逐步扩展并优化地图，在表征能力与计算效率之间取得平衡。此外，系统采用统一的鲁棒几何损失函数，结合外部几何先验知识以缓解单目非刚性SLAM固有的不适定性问题。在多个公开内窥镜数据集上的大量实验表明，相较于现有先进方法，NRGS-SLAM实现了更精确的相机姿态估计（均方根误差降低达50%）和更高质量的光照真实重建。全面的消融研究进一步验证了关键设计选择的有效性。源代码将在论文录用后公开。

---

### 11. BadCLIP++: Stealthy and Persistent Backdoors in Multimodal Contrastive Learning

- **作者**: Siyuan Liang, Yongcheng Jing, Yingjie Wang, Jiaxing Huang, Ee-chien Chang, Dacheng Tao
- **发表日期**: 2026-02-19
- **匹配关键词**: HRI
- **arXiv**: [2602.17168v1](http://arxiv.org/abs/2602.17168v1)
- **🔒 开源**: 未提及
- **中文摘要**: 针对多模态对比学习模型的后门攻击研究面临两大关键挑战：隐蔽性与持续性。现有方法在强检测或持续微调下常告失效，主要原因在于：(1)跨模态不一致性暴露触发模式，(2)低投毒率下的梯度稀释加速后门遗忘。这些耦合成因尚未得到充分建模与解决。本文提出BadCLIP++统一框架以应对双重挑战。在隐蔽性方面，设计语义融合QR微触发器，将不可感知模式嵌入任务相关区域附近，在保持干净数据统计特征的同时生成紧凑的触发分布；进一步采用目标对齐子集选择策略，强化低注入率下的信号强度。在持续性方面，通过半径收缩与质心对齐稳定触发嵌入，借助曲率控制与弹性权重固化稳定模型参数，使解始终保持在抗微调的低曲率宽盆地内。我们首次给出理论分析证明：在信任区域内，干净样本微调梯度与后门目标梯度具有同向性，使得攻击成功率衰减存在非递增上界。实验表明，仅需0.3%投毒率，BadCLIP++在数字场景中即可实现99.99%的攻击成功率（ASR），较基线方法提升11.4个百分点。在十九种防御方法测试中，ASR始终高于99.90%且干净准确率下降不足0.8%。该方法在物理攻击中达到65.03%的成功率，并对抗水印去除防御具有鲁棒性。

---

### 12. Epistemology of Generative AI: The Geometry of Knowing

- **作者**: Ilya Levin
- **发表日期**: 2026-02-19
- **匹配关键词**: navigation
- **arXiv**: [2602.17116v1](http://arxiv.org/abs/2602.17116v1)
- **🔒 开源**: 未提及
- **中文摘要**: 生成式人工智能对我们关于知识及其生产的理解提出了前所未有的挑战。与以往技术变革中工程理解先于或伴随部署的情况不同，生成式AI的运作机制在认识论层面仍具模糊性。若缺乏这种理解，其负责任地融入科学、教育及制度生活便无法建立在原则性基础之上。本文认为，缺失的阐释必须始于一个尚未获得充分哲学关注的范式突破。在图灵-香农-冯·诺依曼传统中，信息以编码二进制向量形式进入机器，语义始终外在于该过程。神经网络架构打破了这一范式：符号输入被即时投射到高维空间中，其坐标对应语义参数，将二进制代码转化为意义几何空间中的位置。正是这个空间构成了塑造生成性生产的能动认识条件。通过运用高维几何的四个结构特性——测度集中、近正交性、指数级方向容量及流形正则性——本文构建了"高维空间的索引性认识论"。借鉴皮尔斯符号学与帕珀特建构主义理论，该研究将生成模型重新概念化为习得流形的导航者，并提出导航性知识作为知识生产的第三种模式，既区别于符号推理，也不同于统计重组。

---

### 13. Hybrid System Planning using a Mixed-Integer ADMM Heuristic and Hybrid Zonotopes

- **作者**: Joshua A. Robbins, Andrew F. Thompson, Jonah J. Glunt, Herschel C. Pangborn
- **发表日期**: 2026-02-19
- **匹配关键词**: motion planning
- **arXiv**: [2602.17574v1](http://arxiv.org/abs/2602.17574v1)
- **🔒 开源**: 未提及
- **中文摘要**: 基于嵌入式优化的混合系统规划因采用计算密集且常对特定数值公式敏感的组合整数规划而面临挑战。为应对这一难题，本文提出一种混合系统运动规划框架，该框架将混合Zonotope（一种先进的集合表示方法）与新型交替方向乘子法（ADMM）组合整数规划启发式算法相结合。研究首先提出基于混合Zonotope的分段仿射系统可达性分析通用处理方法，并将其扩展至最优规划问题的构建。相较于既有技术生成的等效集合，采用本方法生成的集合具有更低的内存复杂度与更紧凑的凸松弛特性。所提出的ADMM启发式算法能高效利用混合Zonotope结构特性，针对混合Zonotope构建的规划问题，该算法相比现有先进组合整数规划启发式方法实现了收敛速度的提升。最终，将所提出的嵌入式硬件混合系统规划方法应用于自动驾驶行为与运动联合规划场景中进行了实验验证。

---

### 14. MASPO: Unifying Gradient Utilization, Probability Mass, and Signal Reliability for Robust and Sample-Efficient LLM Reasoning

- **作者**: Xiaoliang Fu, Jiaye Lin, Yangyi Fang, Binbin Zheng, Chaowen Hu, Zekai Shao, Cong Qin, Lu Pan, Ke Zeng, Xunliang Cai
- **发表日期**: 2026-02-19
- **匹配关键词**: exploration
- **arXiv**: [2602.17550v1](http://arxiv.org/abs/2602.17550v1)
- **🔒 开源**: 未提及
- **中文摘要**: 现有可验证奖励强化学习（RLVR）算法（如GRPO）依赖于僵化、均匀且对称的置信域机制，这些机制与大型语言模型（LLMs）复杂的优化动态存在根本性错位。本文指出此类方法存在三个关键挑战：（1）硬截断的二元截断机制导致梯度利用效率低下；（2）均匀比例约束忽视词元分布特性，引发概率质量不敏感问题；（3）正负样本间信用分配模糊度差异导致信号可靠性不对称。为弥合这些差距，我们提出质量自适应软策略优化（MASPO）——一个统一框架，旨在协调这三个维度。MASPO集成了可微分软高斯门控以最大化梯度效用，采用质量自适应限幅器平衡概率谱上的探索，并通过非对称风险控制器使更新幅度与信号置信度对齐。大量实验表明，MASPO作为稳健的一体化RLVR解决方案，显著优于现有基线方法。代码已开源：https://anonymous.4open.science/r/ma1/README.md。

---

