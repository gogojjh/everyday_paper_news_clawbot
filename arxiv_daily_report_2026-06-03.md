# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-06-03 08:03

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 9/20 篇提供

**🌟 Highlight**: 13 篇 | **📌 Poster**: 7 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. IMAC-AgriVLN: Can Agricultural Vision-and-Language Navigation Agents be Aware of Instruction Mistakes?

- **作者**: Xiaobei Zhao, Xingqi Lyu, Xin Chen, Xiang Li
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.02519v1)
- **发表日期**: 2026-06-01
- **匹配关键词**: vision-and-language navigation, navigation, VLN
- **arXiv**: [2606.02519v1](http://arxiv.org/abs/2606.02519v1)
- **📥 PDF**: 已下载至本地 (`2606.02519v1_IMAC-AgriVLN_Can_Agricultural_Vision-and-Language_Navigation_Agents_be_Aware_of_Instruction_Mistakes.pdf`)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/AlexTraveling/IMAC-AgriVLN.
- **中文摘要**: 农业机器人正作为强大助手广泛应用于各类农业任务，但其移动方式仍高度依赖人工操作或轨道系统。AgriVLN方法与A2A基准率先将视觉语言导航（VLN）拓展至农业领域，使机器人能够根据自然语言指令导航至目标位置。然而，现有方法几乎都采用"给定指令本身正确"的理想假设，这与现实场景存在偏差——任何人都可能说出包含错误的指令。为弥合这一差距，我们提出A2A-MI基准，通过构建半自动数据标注器，以更丰富高效的方式为每条原始指令插入三类错误。我们测试了多个最先进的农业VLN智能体，发现其成功率（SR）下降57%，导航误差（NE）增加9%，这表明农业VLN智能体倾向于假设指令正确，当观测场景与接收指令不符时缺乏质疑意识。为建立指令错误感知能力，我们提出IMAC模块，通过分析指令与当前前方图像，判断指令是否存在错误并在必要时尝试修正。将IMAC集成至基线模型后，我们观察到显著性能提升，有效缩小了与无错误指令场景的性能差距。项目地址：https://github.com/AlexTraveling/IMAC-AgriVLN。

---

### 2. FATE-VLA:Failue-aware test generation for vision-language-action models

- **作者**: Arusa Kanwal, Pablo Valle, Shaukat Ali, Aitor Arrieta
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.02307v1)
- **发表日期**: 2026-06-01
- **匹配关键词**: vision-language-action, vision-language-action model, exploration, VLA
- **arXiv**: [2606.02307v1](http://arxiv.org/abs/2606.02307v1)
- **📥 PDF**: 已下载至本地 (`2606.02307v1_FATE-VLAFailue-aware_test_generation_for_vision-language-action_models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型正越来越多地被用作通用机器人策略，然而其评估仍主要依赖于随机采样任务场景的静态基准测试。在高维具身空间中，失败是稀疏且聚集的，因此静态基准测试可能低估鲁棒性风险。我们将VLA评估重新定义为主动故障发现问题，并提出一种故障感知的测试生成方法，该方法将多样性驱动的探索与从观测执行中学习的代理模型相结合。该方法将测试引导向高风险且多样化的场景区域。在四个最先进的VLA模型上，该方法发现了显著更多的故障（相比选定基线最多提升29.7%），同时揭示了更多样化的故障模式。这意味着，例如在GR00T-N1.6模型中，成功率从64.4%下降至34.7%。更广泛而言，我们的研究结果呼吁VLA评估的范式转变：从固定任务套件上的被动测量转向部署前暴露模型弱点结构的自适应、故障寻求型测试生成。

---

### 3. RoboSemanticBench: Diagnosing Semantic Grounding in Action Prediction for VLA Models

- **作者**: Bin Yu, Yao Zhang, Haishan Liu, Shijie Lian, Yuliang Wei, Xiaopeng Lin, Zhaolong Shen, Changti Wu, Ruina Hu, Bailing Wang, Cong Huang, Kai Chen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.02277v1)
- **发表日期**: 2026-06-01
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2606.02277v1](http://arxiv.org/abs/2606.02277v1)
- **📥 PDF**: 已下载至本地 (`2606.02277v1_RoboSemanticBench_Diagnosing_Semantic_Grounding_in_Action_Prediction_for_VLA_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型建立在这样一个前提之上：预训练的语言或视觉-语言骨干网络所获得的语义理解应指导机器人动作预测。然而，机器人微调被优化为对特定任务动作分布的模仿学习，且许多评估可以通过视觉或指令-动作捷径来解决。我们提出了RoboSemanticBench（RSB），这是一个用于诊断动作预测中语义基础能力的具身基准测试：即经过后训练的VLA模型能否利用复杂指令语义来选择和操控正确的物理目标。在每个测试回合中，机器人会收到一道多项选择的数学或常识问题，观察候选答案方块，并必须抓取与正确答案对应的方块。RSB涵盖了受控算术、小学数学理解以及常识或事实理解，包含四选一和十选一两种套件。在具有代表性的VLA模型上，我们发现许多策略学会了抓取候选方块，但在控制抓取成功率后，选择语义正确方块的概率接近随机或低于随机水平，揭示了骨干网络层面的语义能力与动作预测之间持续存在的差距。

---

### 4. Co-training with Ego-centric Video and Demonstration for Robot Navigation Task

- **作者**: Shoya Kuno, Yumo Ouchi, Kanata Suzuki
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.01951v1)
- **发表日期**: 2026-06-01
- **匹配关键词**: navigation, vision-language-action, VLA, robot navigation
- **arXiv**: [2606.01951v1](http://arxiv.org/abs/2606.01951v1)
- **📥 PDF**: 已下载至本地 (`2606.01951v1_Co-training_with_Ego-centric_Video_and_Demonstration_for_Robot_Navigation_Task.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型在多样化机器人任务中展现出巨大潜力，但其性能高度依赖大规模高质量训练数据，而真实机器人上的数据采集成本高昂且耗时。尽管已有研究探索利用以自我为中心的人类视频扩充操作数据集，但由于运动过程中的视角变化，将此类方法应用于移动机器人导航仍面临挑战。本文提出一种框架，将自我中心行走视频转化为移动机器人模仿学习数据集。该方法从人类视频中估计相机运动，并将其转换为与地面移动机器人兼容的动作表征。通过联合训练基于人类数据与机器人采集数据的VLA模型，该模型在语言理解能力和动作生成鲁棒性上均优于仅使用单一数据源的训练结果。在水果搜索导航任务上的实验表明，人类自我中心视频为移动机器人学习提供了有效且可扩展的数据来源。

---

### 5. Learning Action-Conditional and Object-Centric Gaussian Splatting World Models for Rigid Objects

- **作者**: Jens U. Kreber, Lukas Mack, Joerg Stueckler
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.01950v1)
- **发表日期**: 2026-06-01
- **匹配关键词**: gaussian splatting
- **arXiv**: [2606.01950v1](http://arxiv.org/abs/2606.01950v1)
- **📥 PDF**: 已下载至本地 (`2606.01950v1_Learning_Action-Conditional_and_Object-Centric_Gaussian_Splatting_World_Models_for_Rigid_Objects.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 世界模型使智能体能够预测其行为对环境产生的后果。本文提出多刚体对象高斯世界模型（MRO-GWM），这是一种学习三维空间中刚体对象动作条件动力学的新型模型。通过以对象为中心的高斯体表征场景，我们能够表示任意形状的物体及多对象场景。我们开发了一种新颖的时空变换器架构，该架构能够根据对象高斯体的历史状态与未来动作预测刚体运动。对象通过其规范坐标系中的高斯体进行表征，从而将物体运动描述为刚体变换。该模型基于多视角重建数据进行训练，要求模型能处理因遮挡导致的物体局部观测问题。我们在由典型家居物体构成、包含多对象动力学及机器人末端执行器交互的合成数据集上分析了预测性能，并在仿真环境中通过模型预测控制方法评估了该模型在非抓取操作任务中的表现。

---

### 6. Set-Supervised Diffusion Policy: Learning Action-Chunking Diffusion through Corrections

- **作者**: Zhaoting Li, Gang Chen, Javier Alonso-Mora, Cosimo Della Santina, Jens Kober
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.01865v1)
- **发表日期**: 2026-06-01
- **匹配关键词**: diffusion policy
- **arXiv**: [2606.01865v1](http://arxiv.org/abs/2606.01865v1)
- **📥 PDF**: 已下载至本地 (`2606.01865v1_Set-Supervised_Diffusion_Policy_Learning_Action-Chunking_Diffusion_through_Corrections.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 扩散策略近期已成为机器人操作领域的一种强大框架。然而，与其他行为克隆方法类似，这类策略仍易受分布偏移影响，部署时常需人工干预来修正故障。这种交互过程自然形成了配对监督信号：即机器人的非期望动作与人类教师的修正动作。但现有数据聚合流程及标准行为克隆损失函数大多忽略了非期望动作中的负向信号，导致模型过度拟合教师动作，并日益依赖昂贵专家数据。为解决这一局限，我们提出集合监督扩散策略（SDP），这是一种利用对比动作片段数据从人类修正中训练扩散策略的新型学习框架。通过配对的正负动作片段，SDP构建期望动作片段集合，并设计训练流程促使扩散策略与该集合对齐。在多项机器人操作任务的广泛实验中，我们证明SDP能持续提升策略性能，尤其在噪声数据鲁棒性方面表现突出。此外，SDP可生成高质量聚合数据集，使基于人工循环修正的策略学习更高效可靠。我们的代码已开源至https://set-supervised-diffusion-policy.github.io/。

---

### 7. The Lie We Tell: Correcting the Euclidean Fallacy in Vision Language Action Policies via Score Matching on Tangent Space

- **作者**: Bing-Cheng Chuang, I-Hsuan Chu, Bor-Jiun Lin, YuanFu Yang, Min Sun, Chun-Yi Lee
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.01847v1)
- **发表日期**: 2026-06-01
- **匹配关键词**: vision-language-action, vision language action
- **arXiv**: [2606.01847v1](http://arxiv.org/abs/2606.01847v1)
- **📥 PDF**: 已下载至本地 (`2606.01847v1_The_Lie_We_Tell_Correcting_the_Euclidean_Fallacy_in_Vision_Language_Action_Policies_via_Score_Matchi.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 基于扩散的视觉-语言-动作策略在机器人操作中取得了显著成功，但存在一个我们称之为$\textbf{欧几里得谬误}$的根本性几何错误：将SE(3)位姿表示为平坦的$\mathbb{R}^{12}$向量。这种近似会导致：(1)违反SO(3)约束的流形漂移，(2)坐标变换下等变性的破坏，以及(3)运动学代价过高的非测地线轨迹。我们提出$\textbf{李扩散执行器(LDA)}$，这是一个内在运行于SE(3)上的扩散框架。该方法通过左不变随机微分方程注入噪声，在切空间中预测分数，并通过指数映射回缩样本。该公式通过构造消除了流形漂移，同时保证了坐标框架等变性和测地线最优性。在CALVIN ABC$\rightarrow$D上，LDA将平均任务长度从$3.27$提升至$3.51$（提升$7.3\%$）。我们进一步在真实机器人上验证了该方法，结果表明我们的方法在大多数任务上优于基线。

---

### 8. PlatonicNav: Unveiling Semantic Correspondence in Navigation with Platonic Topological Maps

- **作者**: Junlin Long, Zeyu Zhang, Xu Deng, Yiran Wang, Yue Yang, Luke Borgnolo, Maxwell Twelftree, Yang Zhao
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.01788v1)
- **发表日期**: 2026-06-01
- **匹配关键词**: vision-and-language navigation, exploration, navigation, visual navigation, VLN
- **arXiv**: [2606.01788v1](http://arxiv.org/abs/2606.01788v1)
- **📥 PDF**: 已下载至本地 (`2606.01788v1_PlatonicNav_Unveiling_Semantic_Correspondence_in_Navigation_with_Platonic_Topological_Maps.pdf`)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/AIGeeksGroup/PlatonicNav., https://aigeeksgroup.github.io/PlatonicNav.
- **中文摘要**: 具身视觉导航——智能体感知复杂环境并通过原始感官输入采取行动以达成目标——支撑着家庭服务机器人、辅助机器人大规模自主探索等广泛应用。然而，近期试图统一视觉-语言导航（VLN）与物体目标导航（ObjNav）的研究仍停留在架构融合、混合任务训练和大规模视觉-语言预训练层面，尚未探究独立训练的视觉与语言编码器是否已共享共同的语义结构。此外，即使是面向物体的拓扑地图，仍需通过显式跨模态监督（如CLIP或大型视觉-语言模型）来锚定语言目标，这引发了一个问题：这种锚定能否仅通过纯视觉构建的地图实现？为应对这些挑战，我们将柏拉图表征假说扩展至具身导航领域，将纯视觉ObjNav、跨模态ObjNav和VLN重新定义为同一物体中心语义流形的三种不同接口。我们进一步提出无需训练的PlatonicNav框架，其柏拉图拓扑地图融合了自监督视觉编码器生成的几何与语义节点距离，并通过盲匹配实现语言目标锚定，无需任何配对视觉-语言数据。在HM3D-IIN、OVON、R2R-CE（基于MP3D）等仿真基准及宇树Go2机器人上的实验表明，PlatonicNav无需显式跨模态训练即可跨任务、跨模态、跨具身形态泛化。代码：https://github.com/AIGeeksGroup/PlatonicNav。网站：https://aigeeksgroup.github.io/PlatonicNav。

---

### 9. Goal2Pixel: Grounding Goals to Pixels for Vision-Language Navigation

- **作者**: Muyi Bao, Yuxin Cai, Hang Xu, Zongtai Li, Jinxi He, Jingfan Tang, Chen Lv, Ji Zhang, Yaqi Xie, Wenshan Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.01621v1)
- **发表日期**: 2026-06-01
- **匹配关键词**: vision-and-language navigation, navigation, VLN
- **arXiv**: [2606.01621v1](http://arxiv.org/abs/2606.01621v1)
- **📥 PDF**: 已下载至本地 (`2606.01621v1_Goal2Pixel_Grounding_Goals_to_Pixels_for_Vision-Language_Navigation.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://baobao0926.github.io/Goal2Pixel/.
- **中文摘要**: 视觉-语言模型（VLMs）已成为连续环境下视觉-语言导航（VLN-CE）的通用基础架构。然而，现有基于VLM的方法大多将导航任务转化为底层动作预测，这种接口存在歧义性、受限于短时运动基元，且因重复调用VLM导致效率低下。我们提出Goal2Pixel——一种纯像素范式，将VLN-CE重新定义为可导航像素定位任务。不同于预测动作，Goal2Pixel将图像平面作为VLM推理与机器人运动之间的统一空间接口：模型预测智能体可见的可导航像素，该像素通过反投影转换为3D航路点用于前向导航。针对非前向动作，我们在图像平面附加辅助指令区域，其中左/右/下区域分别对应左转、右转和停止指令。为实现长时域导航，我们提出可见性感知的关键帧记忆机制，用于紧凑且信息丰富的历史表征。为适配预训练VLM完成可导航像素定位，我们引入语义嵌入与坐标感知辅助损失函数。Goal2Pixel在减少VLM推理调用次数的同时，取得了具有竞争力的最优性能。在R2R-CE Val-Unseen数据集上，该方法以每轮仅7.75次VLM调用实现54.1%的成功率（SR）和52.5%的路径长度加权成功率（SPL），相比直接动作预测方法（32.9% SR需46.62次调用）减少6倍调用量。该趋势在RxR-CE数据集上同样得到验证。项目页面：https://baobao0926.github.io/Goal2Pixel/。

---

### 10. LEGS: Fine-Tuning Teleop-Free VLAs for Humanoid Loco-manipulation in an Embodied Gaussian Splatting World

- **作者**: Hojune Kim, Timothy Chen, Jiankai Sun, Lars W. Osterberg, Qianzhong Chen, Ke Wang, Mac Schwager
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.01458v1)
- **发表日期**: 2026-05-31
- **匹配关键词**: gaussian splatting, vision-language-action, 3D gaussian splatting, VLA
- **arXiv**: [2606.01458v1](http://arxiv.org/abs/2606.01458v1)
- **📥 PDF**: 已下载至本地 (`2606.01458v1_LEGS_Fine-Tuning_Teleop-Free_VLAs_for_Humanoid_Loco-manipulation_in_an_Embodied_Gaussian_Splatting_W.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://legsvla.github.io/.
- **中文摘要**: 训练人形机器人全身操作（loco-manipulation）的视觉-语言-动作（VLA）策略受限于人类遥操作演示的高昂成本和复杂性。迄今为止，在模拟器中微调的VLA策略未能有效迁移至人形机器人全身操作任务。我们提出LEGS（基于具身高斯泼溅的全身操作），这是一种混合模拟器，将网格前景（机器人、物体、道具）合成到从手持场景采集重建的逼真3D高斯泼溅（3DGS）背景上。LEGS使用程序化运动基元生成器，无需人类遥操作即可大规模合成带标注的演示，并通过确定性两阶段颜色校准，使渲染的3DGS图像与机器人部署相机对齐。在宇树G1人形机器人上，针对三个全身难度递增的抓取放置任务和三种VLA骨干网络（psi_0、pi_0.5、GR00T N1.6），完全基于LEGS数据训练的策略在每项实验中均达到或超越基于人类遥操作演示训练的策略。该策略还优于消融3DGS背景效果的纯网格模拟基线，表明逼真渲染是合成数据迁移的关键使能因素。LEGS中人形机器人运动与场景外观独立记录，使得同一自动生成的演示可在新背景和物体网格下重新渲染——覆盖新场景的成本比遥操作低15倍以上——从而增强训练数据对场景变化的鲁棒性。在物体与场景外观联合偏移的情况下，基于重新渲染的LEGS-AUG数据训练的策略保持任务成功，而基于遥操作数据训练的基线则完全失败。我们的项目页面位于https://legsvla.github.io/。

---

### 11. OneVLA: A Unified Framework for Embodied Tasks

- **作者**: Lingfeng Zhang, Xiaoshuai Hao, Yingbo Tang, Lei Zhou, Shuyi Zhang, Jinkun Liu, Hongsheng Li, Chenhao Zhang, Qiang Zhang, Hangjun Ye, Xiaojun Liang, Long Chen, Wenbo Ding
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.01241v1)
- **发表日期**: 2026-05-31
- **匹配关键词**: navigation, navigation and manipulation, VLA, vision-language-action
- **arXiv**: [2606.01241v1](http://arxiv.org/abs/2606.01241v1)
- **📥 PDF**: 已下载至本地 (`2606.01241v1_OneVLA_A_Unified_Framework_for_Embodied_Tasks.pdf`)
- **🔓 开源**: CODE
- **中文摘要**: 导航与操作是具身智能的核心能力，使机器人能够理解自然语言指令并与物理环境进行交互。然而，当前的视觉-语言-动作（VLA）模型仍受限于特定任务的架构设计，专精于导航或操作单一领域，这阻碍了通用型机器人智能体的发展。为弥合这一鸿沟，我们提出OneVLA——一种将不同任务整合至统一框架的集成架构。具体而言，我们设计了统一动作头，无需针对特定任务变体即可同时生成导航与操作动作。此外，我们提出多阶段渐进式训练策略，通过精心构建的数据集与思维链（CoT）微调，促进两个领域间的强正向迁移与相互增强。在仿真与真实环境中的大量实验表明，OneVLA实现了最先进的性能，显著优于专用单任务模型及现有跨任务模型。通过统一这些核心能力，OneVLA为真正通用型机器人系统铺平了道路。模型与源代码将公开发布。

---

### 12. Towards Interactive Video World Modeling: Frontiers, Challenges, Benchmarks, and Future Trends

- **作者**: Jiuming Liu, Chaojun Ni, Mengmeng Liu, Chensheng Peng, Fangjinhua Wang, Sitian Shen, Marc Pollefeys, Masayoshi Tomizuka, Ayush Tewari, Per Ola Kristensson ⭐
  - **高亮作者**: Marc Pollefeys
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.01164v1)
- **发表日期**: 2026-05-31
- **匹配关键词**: exploration
- **arXiv**: [2606.01164v1](http://arxiv.org/abs/2606.01164v1)
- **📥 PDF**: 已下载至本地 (`2606.01164v1_Towards_Interactive_Video_World_Modeling_Frontiers,_Challenges,_Benchmarks,_and_Future_Trends.pdf`)
- **🔓 开源**: GITHUB, CODE
  - 链接：https://github.com/liujiuming123/Awesome-Interactive-World-Model.
- **中文摘要**: 随着大语言模型和基于扩散的内容生成技术的快速发展，世界建模日益受到研究关注，并惠及游戏引擎、具身人工智能、自动驾驶等多个下游领域。通过将用户动作显式融入世界状态变迁，近期研究以动作条件化的视频或3D生成范式赋予世界建模交互性，进一步增强了世界演化的可控性，使用户能够自由漫游、操控、导航并个性化定制状态演化过程。本文旨在系统梳理交互式世界建模的最新研究趋势、技术进展、评估基准，并展望未来潜在发展方向。具体而言，我们首先从应用场景、世界状态演化、场景模态三个维度总结近期研究成果与趋势；继而深入探讨动作条件化可控性、长程交互与记忆、实时交互的动作跟随响应性三大关键技术挑战；此外，系统比较了开放世界探索、游戏引擎、自动驾驶、机器人四个特定应用领域的现有基准与评估指标；最后，探讨了实现下一代交互式世界建模的若干前瞻性方向。相关资源库已公开于：https://github.com/liujiuming123/Awesome-Interactive-World-Model。

---

### 13. Beyond Task Success: Behavioral and Representational Diagnostics for WAM and VLA

- **作者**: Hung Mai, Bin Zhu, Tuan Do
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.01095v1)
- **发表日期**: 2026-05-31
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2606.01095v1](http://arxiv.org/abs/2606.01095v1)
- **📥 PDF**: 已下载至本地 (`2606.01095v1_Beyond_Task_Success_Behavioral_and_Representational_Diagnostics_for_WAM_and_VLA.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）策略与世界-动作模型（WAM）代表了机器人操作领域中两种日益重要的范式。然而，尚不明确WAM中的未来预测是否能在最终任务成功之外带来行为层面的实质性改进。本文探究WAM是否仅仅增加了未来预测功能，还是以可操作于控制的方式改变了机器人的行为与内部表征。我们提出了一种与模型无关的诊断框架，通过两个互补视角——行为轨迹分析与基于稀疏自编码器的特征分析——对WAM与VLA进行比较。行为协议测量动作动态一致性、目标物体进展、干扰物影响及运行成本；特征空间协议则将内部表征划分为记忆型、反应型或预测型，揭示模型是否编码了面向未来的结构。在LIBERO与RoboTwin2.0数据集上，我们评估了涵盖直接VLA以及联合、序列、辅助WAM的7种策略。结果表明，仅凭成功率会掩盖关键差异：WAM通常能改善物体级行为与目标选择性，但其收益依赖于架构设计，且推理成本更高。序列WAM展现出最清晰的预测结构，而辅助与联合WAM则分别压缩或纠缠了未来信息。这些发现为WAM设计指明了未来方向，以保留行为可操作的未来表征，从而实现高效操作。

---

## 📌 Poster

*其他相关研究*

---

### 1. AFUN: Towards an Affordance Foundation Model for Functionality Understanding

- **作者**: Zhaoning Wang, Yi Zhong, Jiawei Fu, Henrik I. Christensen, Jun Gao
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.02551v1)
- **发表日期**: 2026-06-01
- **匹配关键词**: affordance
- **arXiv**: [2606.02551v1](http://arxiv.org/abs/2606.02551v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: PROJECT_PAGE
- **中文摘要**: 功能理解连接了视觉感知与物理动作，为机器人在开放非结构化真实环境中的操作提供了可解释的接口。然而，构建一个不仅能理解交互位置与方式，还能跨不同环境、物体和任务泛化的功能基础模型，仍是一个长期的研究挑战。现有方法通常仅解决部分问题：要么定位任务相关区域但未指定可执行动作，要么预测动作但可扩展性有限。本文提出我们的模型，向功能理解的基础模型迈进一步。通过单张RGB-D图像和语言任务描述，我们的模型可预测任务条件功能掩膜（交互位置）和三维接触后运动曲线（交互方式）。为支持开放世界泛化，我们构建了大规模标准化数据管道，将异构的机器人、人类、仿真及真实世界扫描数据转换为包含语言、掩膜和以物体为中心的三维运动标签的共享功能模式。我们从三个方面评估模型：功能分割方面，在4个基准的8个测试集上，模型以大幅优势超越所有基线，平均gIoU/cIoU提升+23.9/+26.3；接触点预测方面，模型预测精度显著提升，命中率较最佳基线提高12.7%-61.3%；三维运动方面，模型在全部三个测试集上均取得最优性能。该模型可直接部署于真实机器人操作任务，无需针对机器人形态微调或使用任务特定启发式规则，展现出适应开放世界功能任务的能力。项目页面：https://www.zhaoningwang.com/AFUN

---

### 2. Adversarial Attacks on Robot Localization Systems via Deep Feature Perturbation

- **作者**: Zhenyu Li, Tianyi Shang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.01892v1)
- **发表日期**: 2026-06-01
- **匹配关键词**: navigation, autonomous navigation
- **arXiv**: [2606.01892v1](http://arxiv.org/abs/2606.01892v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 机器人定位系统对自主导航与安全性至关重要。对抗性扰动可能误导这些系统，导致定位错误、导航偏差或危险交互，尤其在关键任务场景中。本文研究了基于深度学习的定位流水线对对抗攻击的脆弱性，提出了一种新型框架，专门针对视觉定位系统中的乘积量化（PQ）生成对抗性查询。该方法采用轻量级乘积量化网络（LPQN）扰动查询特征编码，通过返回语义无关的数据库条目来误导检索过程。对抗性查询通过两阶段流程生成：前向传播阶段扰动特征分布，反向传播阶段通过优化精炼扰动。LPQN的轻量化设计使其能以最小计算开销产生细微却高效的扰动。在受控环境与真实机器人环境中的大量实验表明，该方法显著降低了PQN性能，暴露了实际应用中的关键脆弱性。

---

### 3. Trans2Occ: Voxel Occupancy Estimation and Grasp for Transparent Objects from Simulation to Reality

- **作者**: Yixuan Yang, Sha Zhang, Rui Li, Zhenfei Yin, Xinzhu Ma, Yiran Qin, Lei Bai, Xudong Xu, Shilin Shan, Wangmeng Zuo, Yanyong Zhang, Wanli Ouyang, Feng Zheng, Shixiang Tang, Dongzhan Zhou
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.01777v1)
- **发表日期**: 2026-06-01
- **匹配关键词**: perception and manipulation
- **arXiv**: [2606.01777v1](http://arxiv.org/abs/2606.01777v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 透明物体因折射和反射导致深度感知不可靠，始终是机器人感知领域的挑战。现有方法多依赖多视角重建或深度补全，但往往难以在实际机器人系统中扩展或部署。本文提出一种基于单视角RGB输入的透明物体感知与操作实用框架。该方法直接从单张图像预测体素空间占有率，生成支持下游机器人抓取的几何感知表征。为支持大规模训练，我们构建了仿真管线，可在不同材质与光照条件下生成配对的RGB图像与体素占有率标注。实验证明，预测的占有率表征对域迁移具有鲁棒性，无需微调即可从仿真有效迁移至真实机器人场景。基于该占有率构建的简单规则抓取策略，进一步实现了透明物体的可靠抓取性能。在仿真与真实环境中的大量实验表明，本框架能提供精确的三维理解，并实现透明物体的实用化操作。这些结果表明，单视角占有率预测为机器人透明物体感知提供了可扩展且有效的解决方案。

---

### 4. PhyScene3D: Physically Consistent Interactive 3D Tabletop Scene Generation

- **作者**: Weixing Chen, Zhuoqian Feng, Yang Liu, Yexin Zhang, Yifan Wen, Yinghong Liao, Weichao Qiu, Guanbin Li, Liang Lin
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.01649v1)
- **发表日期**: 2026-06-01
- **匹配关键词**: affordance
- **arXiv**: [2606.01649v1](http://arxiv.org/abs/2606.01649v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 生成物理一致的3D桌面场景是交互式与通用机器人学习中一个基础但尚未充分探索的问题。其挑战源于密集的物体层级关系与非规则的功能可供性。此处所指的交互式场景，是指可直接加载至物理模拟器中的物理有效、无碰撞环境。现有方法从解耦的符号求解器到端到端回归模型，常受误差传播或对包含广泛物理违例的噪声监督过拟合等问题困扰。为克服这些局限，我们提出PhyScene3D框架，将生成过程重构为类人建构流程。所提出的认知拓扑推理链（CTRC）将场景合成分解为顺序的锚点条件化过程，采用基于3D AABB的布局方案施加强结构归纳偏置。针对不完美监督与物理不可行性问题，我们引入物理感知去噪对齐（PADA）机制，通过融合可微符号距离场（SDF）与测试时优化（TTO），在保持语义意图的同时将生成场景投影至物理可行流形。实验表明，PhyScene3D在语义准确性与物理有效性上均超越现有最优方法，相较于人工标注训练数据，场景级碰撞率降低40%。

---

### 5. Physics-Informed Modeling and Control of Emergent Behaviors in Robot Swarms

- **作者**: Zixuan Jin, Wenzhuo Zhang, Shuxian Quan, Zirui Dong, Fangwen Ye, Yuchen Shi, Cheng Xu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.01597v1)
- **发表日期**: 2026-06-01
- **匹配关键词**: navigation
- **arXiv**: [2606.01597v1](http://arxiv.org/abs/2606.01597v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 机器人群体可以通过局部感知、有限通信和分散决策展现出连贯的集体行为，然而当行为在多个阶段展开时，对这种涌现现象的建模与控制仍具挑战性。本文提出PhySwarm——一种基于物理信息的微观-宏观框架，将多阶段群体涌现表示为受物理约束的密度场演化与可执行机器人运动的耦合。在宏观层面，多相平流-扩散-反应模型通过定向输运、基于扩散的空间调节以及行为相变来描述与阶段相关的群体密度演化。在微观层面，等效确定性运动模型通过势场平流、密度梯度补偿以及速率或事件门控的相位切换来实现这些机制。神经物理控制器将局部观测与时序记忆映射为有界物理参数，并通过结合任务奖励、宏观密度残差与微观运动一致性约束的强化学习-物理信息神经网络目标进行训练。在多项概念验证的群体任务中——包括路径引导觅食、构型可重构导航以及角色自适应搜索救援——我们证明PhySwarm能够在统一的物理信息建模框架内生成不同的多阶段涌现行为。学习得到的密度场与物理参数为平流、扩散和反应如何共同调控多阶段群体组织提供了可解释的证据。这些结果为学习、解释和控制机器人群体涌现行为建立了一条基于物理信息的路径。

---

### 6. Hierarchical Object Representation for Spatial Robot Perception: Points, Meshes, and Superquadrics

- **作者**: Ceng Zhang, Wan Su, Mohamed Samshad, Gregory S. Chirikjian, Rajat Talak
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.01545v1)
- **发表日期**: 2026-06-01
- **匹配关键词**: scene graph, navigation, long-term autonomy, robot navigation
- **arXiv**: [2606.01545v1](http://arxiv.org/abs/2606.01545v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: GITHUB
  - 链接：https://github.com/perceptica-robotics/Hickory.
- **中文摘要**: 层次化三维场景图（3DSG）已成为一种可操作且可扩展的长期自主性表征方法，能够在场景中整合度量、语义和拓扑信息。然而，大多数方法仅采用简化几何模型（如局部点云或三维边界框），导致3DSG中物体的几何表征问题被忽视。本研究提出一种层次化物体表征方法，可用于高保真物体级重建、基于物体的鲁棒重定位或地图对齐，以及在密集杂乱环境中实现安全机器人导航规划的高效解析式碰撞检测。该表征在结构上分为四个层次，逐步将原始传感器数据抽象为密集三维网格，再进一步抽象为超二次曲面等解析基元，从而为物体几何提供稀疏且可解析的表征。我们开发了一套从机器人采集的RGB-D图像流构建层次化物体表征的流程，并在室内外真实开放集物体场景中验证其有效性。通过涵盖HOPE、ReplicaCAD、Kimera-Multi及宇树B2机器人采集的NUS校园数据集等多个数据集的广泛实验，验证了本流程在室内外环境中的表现。实验表明，基于超二次曲面的地图对齐方法优于当前最先进的基于物体的地图对齐方法ROMAN。相关代码已开源：https://github.com/perceptica-robotics/Hickory。

---

### 7. Crazyflow: An Accurate, GPU-Accelerated, Differentiable Drone Simulator in JAX

- **作者**: Martin Schuck, Marcel P. Rath, Yufei Hua, AbhisheK Goudar, SiQi Zhou, Angela P. Schoellig
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.01478v1)
- **发表日期**: 2026-05-31
- **匹配关键词**: obstacle avoidance
- **arXiv**: [2606.01478v1](http://arxiv.org/abs/2606.01478v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: CODE
- **中文摘要**: 来自仿真的高质量、大规模合成数据正成为提升机器人算法能力的关键基石。尽管空中机器人仿真器已各自独立发展出支持保真度、可微性和集群等专业需求的能力，但尚缺乏一个能够跨所有领域合成数据的统一平台。为此，我们提出Crazyflow仿真器，旨在突破空中机器人算法开发的极限——涵盖从基于模型到数据驱动、从梯度方法到采样方法、从单智能体到多智能体系统的全谱系方法。与现有顶尖无人机仿真器相比，Crazyflow对单架无人机的仿真速度提升超过一个数量级，并可同时模拟数千个由4000架无人机组成的集群。真实世界实验表明，Crazyflow既支持基于解析梯度的策略学习（无需域随机化即可实现亚厘米级轨迹跟踪精度），也支持每秒超过5亿步的采样避障方法。突破传统"训练-部署"范式，其前所未有的速度甚至实现了飞行中强化学习：我们将实体无人机抛向空中，在0.38秒内从零开始训练恢复策略，成功稳定无人机。Crazyflow支持多层级仿真抽象，直接兼容所有开源Crazyflie模型，并通过提供轻量级系统辨识流程，实现跨定制无人机平台与应用的快速重构。通过同步提升精度、速度与可微性，Crazyflow为合成数据生成提供开源资源，并具备在线执行学习与优化的大规模并行化能力，为新型算法开发开辟道路。

---

