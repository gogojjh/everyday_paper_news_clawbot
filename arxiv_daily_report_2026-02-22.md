# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-02-22 14:15

**今日新增**: 11 篇

**搜索关键词**: `lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR online SLAM OR incremental SLAM OR place recognition OR visual relocalization | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR semantic navigation OR visual navigation OR VLN OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 1/11 篇提供

---

## 🧭 Navigation

### 1. Graph Neural Model Predictive Control for High-Dimensional Systems

- **作者**: Patrick Benito Eberhard, Luis Pabon, Daniele Gammelli, Hugo Buurmeijer, Amon Lahr, Mark Leone, Andrea Carron, Marco Pavone
- **发表日期**: 2026-02-19
- **匹配关键词**: obstacle avoidance
- **arXiv**: [2602.17601v1](http://arxiv.org/abs/2602.17601v1)
- **🔒 开源**: 未提及
- **中文摘要**: 对软体机器人等高维系统的控制，需要既能精确捕捉复杂动态特性又保持计算可行性的模型。本研究提出一种框架，将基于图神经网络（GNN）的动态模型与结构利用模型预测控制相结合，实现对高维系统的实时控制。通过将系统表示为具有局部交互作用的图结构，GNN保持了稀疏性，而定制化的凝聚算法则从控制问题中消除状态变量，确保计算效率。该凝聚算法的复杂度随系统节点数量线性增长，并利用图形处理器（GPU）并行化实现实时性能。所提方法在仿真和物理软体机器人躯干实验中均得到验证。结果表明，该方法可扩展至1000个节点系统在100赫兹闭环频率下运行，在硬件上实现亚厘米精度的实时参考轨迹跟踪，性能较基线方法提升63.6%。最后，我们展示了该方法实现有效全身避障的能力。

---

### 2. RA-Nav: A Risk-Aware Navigation System Based on Semantic Segmentation for Aerial Robots in Unpredictable Environments

- **作者**: Ziyi Zong, Xin Dong, Jinwu Xiang, Daochun Li, Zhan Tu
- **发表日期**: 2026-02-19
- **匹配关键词**: navigation, robot navigation
- **arXiv**: [2602.17515v1](http://arxiv.org/abs/2602.17515v1)
- **🔒 开源**: 未提及
- **中文摘要**: 现有空中机器人导航系统通常围绕静态与动态障碍物规划路径，但当静态障碍物突然移动时无法有效适应。通过融入环境语义感知能力，可实现对突发移动障碍物潜在风险的评估。本文提出RA-Nav——一种基于语义分割的风险感知导航框架。轻量级多尺度语义分割网络实时识别障碍物类别，将其进一步划分为静止型、临时静态型与动态型三类。针对每类障碍物设计相应风险估计函数，实现实时风险预测，并据此构建完整的局部风险地图。基于该地图设计风险感知路径搜索算法，确保规划结果兼顾路径效率与安全性。随后通过轨迹优化生成安全、平滑且符合动力学可行性的轨迹。对比仿真表明，在突发障碍物状态转换场景中，RA-Nav相比基线方法获得更高成功率。基于真实世界数据的仿真实验进一步验证了该框架的有效性。

---

### 3. Flickering Multi-Armed Bandits

- **作者**: Sourav Chakraborty, Amit Kiran Rege, Claire Monteleoni, Lijun Chen
- **发表日期**: 2026-02-19
- **匹配关键词**: navigation, exploration
- **arXiv**: [2602.17315v1](http://arxiv.org/abs/2602.17315v1)
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出闪烁多臂赌博机（FMAB）这一新型MAB框架，其中可用臂集（或行动集）每轮都可能发生变化，且任意时刻的可用集合可能取决于智能体先前选择的臂。我们通过随机图过程对这种受限且动态变化的可用性进行建模，其中臂对应节点，智能体的移动被限制在其局部邻域内。我们在两种随机图模型下分析该问题：独立同分布的埃尔德什-雷尼（ER）过程和边马尔可夫过程。我们提出并分析了一种两阶段算法，该算法采用惰性随机游走进行探索以高效识别最优臂，随后通过导航与锁定阶段进行利用。我们为两种图设置建立了高概率且期望的次线性遗憾界。通过为该问题类别建立匹配的信息论下界，我们证明该算法的探索成本接近最优，这凸显了局部移动约束下探索的基本成本。我们通过数值模拟（包括地面机器人侦察灾区的场景）对理论保证进行了补充验证。

---

### 4. Hybrid System Planning using a Mixed-Integer ADMM Heuristic and Hybrid Zonotopes

- **作者**: Joshua A. Robbins, Andrew F. Thompson, Jonah J. Glunt, Herschel C. Pangborn
- **发表日期**: 2026-02-19
- **匹配关键词**: motion planning
- **arXiv**: [2602.17574v1](http://arxiv.org/abs/2602.17574v1)
- **🔒 开源**: 未提及
- **中文摘要**: 基于嵌入式优化的混合系统规划因采用计算密集且常对特定数值公式敏感的混合整数规划而面临挑战。为应对这一挑战，本文提出一种混合系统运动规划框架，该框架将先进集合表示方法——混合Zonotope与新型交替方向乘子法（ADMM）混合整数规划启发式算法相结合。研究首先提出基于混合Zonotode的分段仿射系统可达性分析通用处理方法，并将其扩展至最优规划问题的构建。相较于既有技术生成的等效集合，采用本方法生成的集合具有更低的内存复杂度与更紧凑的凸松弛特性。所提出的ADMM启发式算法能高效利用混合Zonotope结构特性。对于以混合Zonotope形式构建的规划问题，相较于现有最先进的混合整数规划启发式算法，本方法实现了收敛速度的显著提升。最终，所提出的嵌入式硬件混合系统规划方法在自动驾驶行为与运动联合规划场景中进行了实验验证。

---

### 5. MASPO: Unifying Gradient Utilization, Probability Mass, and Signal Reliability for Robust and Sample-Efficient LLM Reasoning

- **作者**: Xiaoliang Fu, Jiaye Lin, Yangyi Fang, Binbin Zheng, Chaowen Hu, Zekai Shao, Cong Qin, Lu Pan, Ke Zeng, Xunliang Cai
- **发表日期**: 2026-02-19
- **匹配关键词**: exploration
- **arXiv**: [2602.17550v1](http://arxiv.org/abs/2602.17550v1)
- **🔒 开源**: 未提及
- **中文摘要**: 现有可验证奖励强化学习（RLVR）算法（如GRPO）依赖于僵化、均匀且对称的置信域机制，这些机制与大型语言模型（LLMs）复杂的优化动态存在根本性错位。本文指出此类方法存在三个关键挑战：（1）硬截断的二元截止机制导致梯度利用效率低下；（2）均匀比率约束忽视词元分布特性，引发概率质量敏感度不足；（3）正负样本间信用分配模糊度差异造成信号可靠性不对称。为弥合这些缺陷，我们提出质量自适应软策略优化（MASPO）——一个统一框架，旨在协调这三个维度。MASPO集成了可微分软高斯门控以最大化梯度效用，采用质量自适应限幅器平衡概率谱上的探索，并通过非对称风险控制器使更新幅度与信号置信度对齐。大量实验评估表明，MASPO作为稳健的一体化RLVR解决方案，显著优于现有基线方法。代码已开源：https://anonymous.4open.science/r/ma1/README.md。

---

### 6. Dodging the Moose: Experimental Insights in Real-Life Automated Collision Avoidance

- **作者**: Leila Gharavi, Simone Baldi, Yuki Hosomi, Tona Sato, Bart De Schutter, Binh-Minh Nguyen, Hiroshi Fujimoto
- **发表日期**: 2026-02-19
- **匹配关键词**: motion planning
- **arXiv**: [2602.17512v1](http://arxiv.org/abs/2602.17512v1)
- **🔒 开源**: 未提及
- **中文摘要**: 道路突发静态障碍物（即麋鹿测试）是自动驾驶避撞领域中一个广为人知的紧急场景。在现有技术中，模型预测控制（MPC）长期被用于自动驾驶车辆的规划与控制。然而，由于MPC在此类危险场景中执行规避动作时的高计算需求，麋鹿测试等紧急情况下的实时自动避撞问题仍未得到解决。本文通过实验实现MPC在突发意外静态障碍物出现后的运动规划，为实时避撞提供了新的见解。鉴于当前最先进的非线性MPC在实时提供可接受解决方案方面能力有限，我们提出了一种类人前馈规划器，用于在MPC优化问题因初始猜测质量差而不可行或无法找到合适解决方案时提供辅助。我们引入最大转向操作的概念来设计前馈规划器，模拟人类在检测到道路静态障碍物后的反应。使用FPEV2-Kanon电动汽车在不同速度和紧急程度下进行了实际实验。此外，通过与最先进的MPC运动规划器进行比较，我们验证了所提出规划策略的有效性。

---

### 7. Bluetooth Phased-array Aided Inertial Navigation Using Factor Graphs: Experimental Verification

- **作者**: Glen Hjelmerud Mørkbak Sørensen, Torleiv H. Bryne, Kristoffer Gryte, Tor Arne Johansen
- **发表日期**: 2026-02-19
- **匹配关键词**: navigation
- **arXiv**: [2602.17407v1](http://arxiv.org/abs/2602.17407v1)
- **🔒 开源**: 未提及
- **中文摘要**: 相控阵蓝牙系统已成为在仓库物流、无人机着陆和自主对接等GNSS受限场景下实现辅助惯性导航的低成本替代方案。基于商用现成组件构建导航系统可降低相控阵无线电导航系统的应用门槛，但代价是测量噪声显著增加且有效作用距离相对较短。本文通过多旋翼无人机飞行实验数据，对比了基于因子图优化估计器的鲁棒估计策略。我们评估了在GNSS信号丢失情况下，借助蓝牙角度测量以及距离或气压测量辅助时的系统性能表现。

---

### 8. Multi-session Localization and Mapping Exploiting Topological Information

- **作者**: Lorenzo Montano-Olivan, Julio A. Placed, Luis Montano, Maria T. Lazaro
- **发表日期**: 2026-02-19
- **匹配关键词**: localization and mapping
- **arXiv**: [2602.17226v1](http://arxiv.org/abs/2602.17226v1)
- **🔒 开源**: 未提及
- **中文摘要**: 在已访问环境中进行操作对自主系统而言正变得日益重要，其在自动驾驶、测绘以及仓储或家庭机器人等领域具有直接应用价值。这种对同一区域的重复观测给建图与定位——实现任何高级任务的关键环节——带来了重大挑战。不同于当前普遍采用的贪婪式全SLAM会话及后续地图匹配方法，本研究提出了一种基于地图定位的新型多会话框架。该框架引入拓扑感知的智能决策机制，通过分析位姿图结构检测低连通性区域，并选择性触发建图与闭环检测模块。生成的增量地图与位姿图可无缝整合至现有模型中，有效降低累积误差并提升全局一致性。我们在数据集重叠序列上验证了该方法，并在真实矿井类环境中证明了其有效性。

---

### 9. From Labor to Collaboration: A Methodological Experiment Using AI Agents to Augment Research Perspectives in Taiwan's Humanities and Social Sciences

- **作者**: Yi-Chih Huang
- **发表日期**: 2026-02-19
- **匹配关键词**: exploration
- **arXiv**: [2602.17221v1](http://arxiv.org/abs/2602.17221v1)
- **🔒 开源**: 未提及
- **中文摘要**: 生成式人工智能正在重塑知识工作，但现有研究主要聚焦于软件工程与自然科学领域，对人文社会科学的方法论探索尚显不足。本研究作为一项"方法论实验"，提出适用于人文社会科学研究的AI智能体协同工作流程（Agentic Workflow），并以Anthropic经济指数（AEI）中台湾地区Claude.ai使用数据（2025年11月，N=7,729组对话）作为实证载体，验证该方法的可行性。

本研究在两个层面展开：主要层面是方法论框架的设计与验证——构建基于任务模块化、人机分工、可验证性三原则的七阶段模块化工作流程，每个阶段明确人类研究者（研究判断与伦理决策）与AI智能体（信息检索与文本生成）的角色分工；次要层面是对AEI台湾数据的实证分析——作为工作流程应用于二手数据研究的操作示范，同时展现研究过程与成果质量（参见附录A）。

本研究的贡献在于：为人文社会科学研究者提出可复现的AI协作框架，并通过操作过程的反思性记录，识别出人机协作的三种操作模式——直接执行、迭代优化、人类主导。这种分类揭示了人类在研究问题构建、理论阐释、情境化推理及伦理反思等方面不可替代的判断作用。研究同时承认了单平台数据、横截面设计及AI可靠性风险等局限性。

---

## 👥 Human-Robot Interaction

### 1. FR-GESTURE: An RGBD Dataset For Gesture-based Human-Robot Interaction In First Responder Operations

- **作者**: Konstantinos Foteinos, Georgios Angelidis, Aggelos Psiris, Vasileios Argyriou, Panagiotis Sarigiannidis, Georgios Th. Papadopoulos
- **发表日期**: 2026-02-19
- **匹配关键词**: human-robot interaction
- **arXiv**: [2602.17573v1](http://arxiv.org/abs/2602.17573v1)
- **🔓 开源**: CODE
- **中文摘要**: 灾害强度和频次的持续攀升使得应急救援人员的工作愈发艰巨。人工智能与机器人技术有望通过辅助操作来缓解这些困难。为此，我们提出一套面向应急救援人员手势控制无人地面车辆的数据集，借鉴现有应急救援手势与战术手语体系，在吸纳资深救援人员反馈后，最终形成包含12种指令的手势系统。通过双视角七距离的采集方式，共获得3312组RGBD配对数据。据我们所知，这是首个专门针对应急救援人员手势引导无人地面车辆的数据集。我们为这套命名为FR-GESTURE的RGBD数据集制定了评估标准，并开展了基线实验以供后续优化。所有数据已公开以推动该领域研究：https://doi.org/10.5281/zenodo.18131333。

---

### 2. Distributed Virtual Model Control for Scalable Human-Robot Collaboration in Shared Workspace

- **作者**: Yi Zhang, Omar Faris, Chapa Sirithunge, Kai-Fung Chu, Fumiya Iida, Fulvio Forni
- **发表日期**: 2026-02-19
- **匹配关键词**: human-robot collaboration
- **arXiv**: [2602.17415v1](http://arxiv.org/abs/2602.17415v1)
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出了一种基于虚拟模型控制（VMC）的去中心化、智能体无关且具备安全感知的人机协作控制框架。在该框架中，人与机器人被置于同一虚拟组件构成的工作空间内，其运动通过与虚拟弹簧和阻尼器的交互产生，而非依赖显式轨迹规划。我们采用去中心化的基于力的停滞检测机制识别死锁状态，并通过协商机制予以解决。实验表明，该方法将机器人在方块放置任务中的卡死概率从最高61.2%降至零。得益于分布式实现，该框架无需结构调整即可扩展：实验中我们实现了最多两台机器人与两名人类的安全协作，仿真中更扩展至四台机器人，同时保持智能体间约20厘米的间距。结果表明，通过调整控制参数可直观塑造机器人行为，并在所有测试场景中实现不同团队规模下的无死锁运行。

---

