# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-05-17 08:03

**今日新增**: 8 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 2/8 篇提供

**🌟 Highlight**: 1 篇 | **📌 Poster**: 7 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. Exploring Bottlenecks in VLM-LLM Navigation: How 3D Scene Understanding Capability Impacts Zero-Shot VLN

- **作者**: Ziyi Xia, Chaoran Xiong, Litao Wei, Xinhao Hu, Ling Pei
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.14801v1)
- **发表日期**: 2026-05-14
- **匹配关键词**: VLN, navigation, vision-and-language navigation, scene graph
- **arXiv**: [2605.14801v1](http://arxiv.org/abs/2605.14801v1)
- **📥 PDF**: 已下载至本地 (`2605.14801v1_Exploring_Bottlenecks_in_VLM-LLM_Navigation_How_3D_Scene_Understanding_Capability_Impacts_Zero-Shot_.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 零样本视觉与语言导航（VLN）因数据采集成本极低且具备天然泛化能力而备受关注。该范式通常由预训练的视觉语言模型（VLM）与大语言模型（LLM）协同驱动：VLM负责构建三维场景图，LLM则处理高层推理与决策。然而，该系统存在关键瓶颈：当前三维感知模型追求像素级精度，这与具身导航对严格计算限制和实时效率的要求直接冲突。为弥合这一差距，本文量化了三维场景理解能力对VLN性能的实际影响。基于典型VLM-LLM框架，我们为两个核心子系统提出统计成功率（SR）上限：1）依赖拓扑映射语义的慢速LLM规划器，2）利用空间坐标与边界框执行LLM决策的快速反应导航器。采用最先进的三维场景理解模型进行验证，结果证实了所提上限，并揭示了感知饱和现象——当感知精度超过特定阈值后，其对导航成功率的提升效果逐渐减弱。研究结果表明，VLN的三维场景理解应摆脱对像素级精度的严格追求，优先关注与导航相关的核心词汇及准确的边界框比例。

---

## 📌 Poster

*其他相关研究*

---

### 1. FU-MPC: Frontier- and Uncertainty-Aware Model Predictive Control for Efficient and Accurate UAV Exploration with Motorized LiDAR

- **作者**: Jianping Li, Pengfei Wan, Zhongyuan Liu, Yi Wang, Yiheng Chen, Xinhang Xu, Rui Jin, Boyu Zhou, Lihua Xie
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.14920v1)
- **发表日期**: 2026-05-14
- **匹配关键词**: navigation, exploration
- **arXiv**: [2605.14920v1](http://arxiv.org/abs/2605.14920v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://kafeiyin00.github.io/FU-MPC/.
- **中文摘要**: 在未知环境中实现高效无人机探索，既需要快速扩展覆盖范围，又需保持精准可靠的定位能力——因为复杂场景下的安全导航依赖于一致的地图构建与位姿估计。然而，对于传统配备激光雷达的无人机而言，可观测区域与无人机位姿及运动状态紧密耦合。扩展覆盖范围通常需要额外的平移或旋转机动，这会降低探索效率，并在几何特征匮乏的环境中增加定位退化风险。电机驱动旋转式激光雷达通过主动调整传感器观测方向（无需改变无人机运动）提供了解决方案，由此引入额外的感知自由度。但现有探索系统鲜少将这种扫描自由度作为与探索进度和定位质量直接关联的显式决策变量。为填补这一空白，我们开发了搭载独立驱动旋转激光雷达的无人机平台，并提出分层式探索框架：全局规划器将前沿点组织为代表性视点，并利用拓扑感知转移成本对其进行排序；基于该规划器，FU-MPC作为局部滚动时域扫描控制器，沿预测飞行轨迹优化激光雷达旋转角度。该控制器联合考虑前沿感知探索效用与方向依赖的定位不确定性，通过轻量化代理评估实现实时机载计算。复杂环境实验表明，与固定模式扫描及仅考虑不确定性的基线方法相比，本系统在保持稳健定位性能的同时提升了探索效率。项目页面详见https://kafeiyin00.github.io/FU-MPC/。

---

### 2. Chrono-Gymnasium: An Open-Source, Gymnasium-Compatible Distributed Simulation Framework

- **作者**: Bocheng Zou, Harry Zhang, Khailanii Slaton, Jingquan Wang, Derrick Ruan, Huzaifa Mustafa Unjhawala, Radu Serban, Dan Negrut
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.14911v1)
- **发表日期**: 2026-05-14
- **匹配关键词**: navigation
- **arXiv**: [2605.14911v1](http://arxiv.org/abs/2605.14911v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: CODE
- **中文摘要**: 高保真物理仿真对于弥合机器人与复杂机械系统中仿真与现实的差距至关重要。然而，高保真引擎的计算开销往往限制了其在强化学习和全局优化等数据密集型任务中的应用。我们提出Chrono-Gymnasium，这是一个分布式计算框架，能够将Project Chrono的高保真多体动力学仿真扩展至大规模计算集群。该框架基于Ray构建，提供标准化的Gymnasium接口，既能与现代机器学习库无缝集成，又内置了分布式执行所需的同步与消息传递原语。我们通过两个典型案例验证了该框架的能力：（1）在复杂地形中训练自主机器人导航的强化学习智能体；（2）对行星着陆器设计参数进行贝叶斯优化以确保着陆稳定性。实验结果表明，Chrono-Gymnasium在保持物理精度的前提下缩短了高保真仿真的运行时间，为复杂机器人系统的设计与控制提供了可扩展的解决方案。

---

### 3. CaMeRL: Collision-Aware and Memory-Enhanced Reinforcement Learning for UAV Navigation in Multi-Scale Obstacle Environments

- **作者**: Hong Hong, Feiyu Liao, Yongheng Liang, Boning Zhang, Haitao Wang, Hejun Wu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.14810v1)
- **发表日期**: 2026-05-14
- **匹配关键词**: obstacle avoidance, navigation
- **arXiv**: [2605.14810v1](http://arxiv.org/abs/2605.14810v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 在无人机避障导航中，障碍物尺度的变化相较于障碍物数量或密度受到的关注明显不足。现有方法通常从单帧深度观测中提取纯几何特征，这种表征方式容易忽略小尺度障碍物，并在大障碍物遮挡下丢失空间上下文信息，导致在多尺度障碍物环境中性能显著下降。针对该问题，我们提出CaMeRL——一种面向无人机导航的碰撞感知与记忆增强强化学习框架。其中，碰撞感知隐式表征通过编码风险敏感深度线索保留精细的障碍物结构，从而提升对小障碍物的敏感性；时序记忆模块则整合多帧观测信息，缓解大障碍物遮挡造成的部分可观测性问题。我们在包含超小和超大障碍物设置的多尺度障碍物场景中评估了CaMeRL。结果表明，CaMeRL在所有尺度上均优于现有最优基线方法，在超小和超大障碍物设置下的成功率分别提升0.48和0.28。更重要的是，CaMeRL能在杂乱室外环境中实现可靠导航。

---

### 4. When Robots Do the Chores: A Benchmark and Agent for Long-Horizon Household Task Execution

- **作者**: Zilin Zhu, Longteng Guo, Yanghong Mei, Bowen Pang, Zongxun Zhang, Xingjian He, Ruyi Ji, Jing Liu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.14504v1)
- **发表日期**: 2026-05-14
- **匹配关键词**: navigation
- **arXiv**: [2605.14504v1](http://arxiv.org/abs/2605.14504v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 长时域家庭任务要求强大的高层规划与持续推理能力，而现有具身智能基准测试多聚焦于短时域导航或操作任务，且依赖固定任务类别，忽视了这些能力。为此，我们提出LongAct基准测试，专门评估通过自由形式指令指定的长时域家庭任务中的规划级自主性。通过剥离具身化底层控制，LongAct聚焦于高层认知能力，包括指令理解、依赖管理、记忆维护与自适应规划。我们进一步提出HoloMind——一种基于视觉语言模型的智能体，其包含基于有向无环图的长时域分层规划器、用于持久世界建模的多模态空间记忆、用于经验复用的情景记忆，以及用于反思性监督的全局评判器。基于GPT-5与Qwen3-VL模型的实验表明，HoloMind在显著提升长时域任务性能的同时降低了对模型规模的依赖。即便顶尖模型也仅达到59%的目标完成率与16%的全任务成功率，这凸显了LongAct的挑战性，以及具身智能体亟需更强的长时域规划能力。

---

### 5. Analogical Trajectory Transfer

- **作者**: Junho Kim, Eun Sun Lee, Gwangtak Bae, Seunggu Kang, Young Min Kim
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.14393v1)
- **发表日期**: 2026-05-14
- **匹配关键词**: scene graph
- **arXiv**: [2605.14393v1](http://arxiv.org/abs/2605.14393v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 我们研究类比轨迹迁移问题，其目标是将三维环境中的运动轨迹迁移至另一个语义相似的位置。这种能力将使机器能够进行类比空间推理，可应用于增强现实/虚拟现实（AR/VR）共在、内容创作和机器人技术。然而，即使语义相似的场景在物体布局、尺度和空间排布上仍可能存在显著差异，因此简单的语义匹配会导致碰撞或几何畸变。此外，由于映射必须保持语义和功能性，同时避免轨迹断裂或碰撞，每个轨迹点的迁移位置搜索空间极为庞大。我们的核心见解是将问题分解为空间分离的子问题，并通过合并子问题解来生成语义一致且空间连贯的迁移结果。具体而言，我们将场景划分为以物体为中心的聚类，利用编码物体与开放空间布局上下文信息的三维基础模型特征，通过分层平滑映射预测估计跨场景映射关系。随后通过组合各聚类映射生成初始迁移结果，并优化消除碰撞与畸变，最终获得空间连贯的轨迹。该方法无需训练，运行时间约0.6秒，性能优于基于大语言模型（LLM）、视觉语言模型（VLM）和场景图匹配的基线方法。我们还展示了在虚拟共在、多轨迹迁移、相机迁移及人机运动迁移等场景中的应用，表明本工作对AR/VR和机器人领域的广泛适用性。

---

### 6. Towards Real-Time Autonomous Navigation: Transformer-Based Catheter Tip Tracking in Fluoroscopy

- **作者**: Harry Robertshaw, Yanghe Hao, Weiyuan Deng, Benjamin Jackson, S. M. Hadi Sadati, Nikola Fischer, Tom Vercauteren, Alejandro Granados, Thomas C. Booth
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.14253v1)
- **发表日期**: 2026-05-14
- **匹配关键词**: navigation, autonomous navigation
- **arXiv**: [2605.14253v1](http://arxiv.org/abs/2605.14253v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 目的：机械取栓术（MT）可改善卒中预后，但因缺乏本地治疗条件而受限。基于强化学习（RL）的机器人系统可通过自主导航缓解这一挑战，但现有RL方法需实时追踪器械尖端坐标。本文旨在开发并评估一种透视引导下的实时导管尖端追踪流程，以解决低对比度、噪声及器械遮挡等难题。方法：设计多线程流程，集成图像读取、预处理、推理及后处理模块。采用U-Net、U-Net+Transformer及SegFormer等深度学习分割模型，通过二分类与三分类方案进行训练与基准测试。后处理包含两步组件过滤、单像素中轴骨架化及基于轮廓回退的贪婪弧长路径追踪。结果：在人工标注的中等复杂度透视视频数据中，二分类SegFormer模型平均绝对误差为4.44 mm，优于U-Net（4.60 mm）、U-Net+Transformer（6.20 mm）及所有三分类模型（5.19-7.74 mm）。在分割基准测试中，该系统超越当前最优的CathAction方法，三分割Dice评分提升达5%。结论：结果表明，所提出的多线程追踪框架在复杂成像条件下保持稳定性能，优于先前基准，为基于RL的自主MT导航提供了可靠高效的基础。

---

### 7. Action-Conditioned Risk Gating for Safety-Critical Control under Partial Observability

- **作者**: Yushen Liu, Yin-Jen Chen, Ziyi Chen, Tao Wang, Heng Huang, Xugui Zhou, Yanfu Zhang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.14246v1)
- **发表日期**: 2026-05-14
- **匹配关键词**: navigation
- **arXiv**: [2605.14246v1](http://arxiv.org/abs/2605.14246v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 许多安全关键控制问题被建模为风险敏感的部分可观测马尔可夫决策过程，其中控制器必须在不完全观测下做出决策，同时平衡任务性能与安全风险。尽管信念空间规划提供了理论上的解决方案，但在实际应用中，维护和规划信念的计算成本较高，且对模型规范敏感。我们提出了一种轻量级风险门控强化学习近似方法，用于部分可观测条件下的风险敏感控制。该方法构建了一个紧凑的有限历史代理状态，并学习了一个基于动作的短期安全违规预测器。该预测的候选动作风险以两种互补方式使用：作为价值学习中的风险惩罚，以及作为决策时间门控，在乐观与保守的集成价值估计之间进行插值。因此，低风险动作更接近追求奖励的估计值，而高风险动作则被更保守地评估。我们在两个安全关键的部分可观测领域评估了该方法：自动血糖调节和安全约束导航。在成人和青少年血糖控制队列中，该方法改善了整体血糖权衡，并相对于信念空间规划基线大幅减少了运行时间。在Safety-Gym导航基准测试中，与无约束强化学习和几种标准安全强化学习基线相比，该方法实现了更优的奖励-成本平衡。这些结果表明，当完整的信念空间规划不可行时，基于动作的短期风险可以为近似风险敏感POMDP控制提供有效的局部信号。

---

