# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-03-05 08:08

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 4/20 篇提供

**🌟 Highlight**: 18 篇 | **📌 Poster**: 2 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. Utonia: Toward One Encoder for All Point Clouds

- **作者**: Yujia Zhang, Xiaoyang Wu, Yunhan Yang, Xianzhe Fan, Han Li, Yuechen Zhang, Zehao Huang, Naiyan Wang, Hengshuang Zhao
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.03283v1)
- **发表日期**: 2026-03-03
- **匹配关键词**: vision-language-action
- **arXiv**: [2603.03283v1](http://arxiv.org/abs/2603.03283v1)
- **📥 PDF**: 已下载至本地 (`2603.03283v1_Utonia_Toward_One_Encoder_for_All_Point_Clouds.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 我们梦想着这样一个未来：来自所有领域的点云能够汇聚一堂，共同构建一个惠及所有领域的统一模型。为实现这一目标，我们提出了Utonia——这是迈向跨领域训练单一自监督点云Transformer编码器的第一步，涵盖遥感、室外激光雷达、室内RGB-D序列、以物体为中心的CAD模型，以及从纯RGB视频中提取的点云。尽管这些数据在感知几何、密度和先验知识上存在显著差异，Utonia仍能学习到一个跨领域一致的表示空间。这种统一不仅提升了感知能力，还揭示了仅在多领域联合训练时才会出现的引人注目的涌现行为。除了感知任务，我们还观察到Utonia的表征能力可进一步赋能具身智能与多模态推理：在机器人操作任务中，基于Utonia特征的视觉-语言-动作策略得到显著提升；将其整合到视觉-语言模型中，亦能增强空间推理性能。我们希望Utonia能成为构建稀疏三维数据基础模型的重要一步，并为增强现实/虚拟现实、机器人技术和自动驾驶等下游应用提供支持。

---

### 2. HoMMI: Learning Whole-Body Mobile Manipulation from Human Demonstrations

- **作者**: Xiaomeng Xu, Jisang Park, Han Zhang, Eric Cousineau, Aditya Bhat, Jose Barreiros, Dian Wang, Shuran Song ⭐
  - **高亮作者**: Shuran Song
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.03243v1)
- **发表日期**: 2026-03-03
- **匹配关键词**: mobile manipulation, navigation, active perception
- **arXiv**: [2603.03243v1](http://arxiv.org/abs/2603.03243v1)
- **📥 PDF**: 已下载至本地 (`2603.03243v1_HoMMI_Learning_Whole-Body_Mobile_Manipulation_from_Human_Demonstrations.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 我们推出全身移动操作界面（HoMMI），这是一个数据收集与策略学习框架，能够直接从无需机器人的真人演示中学习全身移动操作。我们通过增强UMI界面的自我中心感知能力，捕捉移动操作所需的全局环境信息，从而实现便携、无需机器人且可扩展的数据收集。然而，简单引入自我中心感知会在观察和行动空间上扩大人机形态差异，增加策略迁移难度。我们通过跨形态手眼策略设计明确弥合这一差异，包括：形态无关的视觉表征；宽松的头部动作表征；以及通过机器人特定物理约束下协调全身运动实现手眼轨迹的全身控制器。这些设计共同支持需要双手协调、全身配合、导航及主动感知的长时程移动操作任务。完整效果展示请访问：https://hommi-robot.github.io

---

### 3. Chain of World: World Model Thinking in Latent Motion

- **作者**: Fuxiang Yang, Donglin Di, Lulu Tang, Xuancheng Zhang, Lei Fan, Hao Li, Chen Wei, Tonghua Su, Baorui Ma
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.03195v1)
- **发表日期**: 2026-03-03
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2603.03195v1](http://arxiv.org/abs/2603.03195v1)
- **📥 PDF**: 已下载至本地 (`2603.03195v1_Chain_of_World_World_Model_Thinking_in_Latent_Motion.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://fx-hit.github.io/cowvla-io.
- **中文摘要**: 视觉-语言-动作（VLA）模型是实现具身智能的重要途径，但现有模型常忽略视觉动态背后的预测性与时序因果结构。世界模型类VLA通过预测未来帧来应对这一问题，却将大量计算资源消耗在冗余背景的重建上。潜在动作类VLA虽能紧凑编码帧间转换，但缺乏连续时序动态建模与世界知识。为突破这些局限，我们提出CoWVLA（世界链VLA），开创了融合世界模型时序推理与解耦潜在运动表征的"世界链"新范式。该框架首先采用预训练视频VAE作为潜在运动提取器，将视频片段显式分解为结构潜变量与运动潜变量；在预训练阶段，VLA模型根据指令与初始帧推断连续潜在运动链并预测片段终止帧；最后通过协同微调，在统一自回归解码器中联合建模稀疏关键帧与动作序列，实现潜在动态与离散动作预测的对齐。这一设计既保留了世界模型在时序推理和世界知识方面的优势，又兼具潜在动作的紧凑性与可解释性，实现了高效的视觉运动学习。在机器人仿真基准测试中的大量实验表明，CoWVLA在性能上超越现有世界模型与潜在动作方法，并展现出可观的计算效率，彰显其作为更有效VLA预训练范式的潜力。项目网站详见 https://fx-hit.github.io/cowvla-io。

---

### 4. MA-CoNav: A Master-Slave Multi-Agent Framework with Hierarchical Collaboration and Dual-Level Reflection for Long-Horizon Embodied VLN

- **作者**: Ling Luo, Qianqian Bai
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.03024v1)
- **发表日期**: 2026-03-03
- **匹配关键词**: navigation, VLN
- **arXiv**: [2603.03024v1](http://arxiv.org/abs/2603.03024v1)
- **📥 PDF**: 已下载至本地 (`2603.03024v1_MA-CoNav_A_Master-Slave_Multi-Agent_Framework_with_Hierarchical_Collaboration_and_Dual-Level_Reflect.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉语言导航旨在使机器人能够根据复杂的语言指令在陌生环境中执行长程导航。其成功关键在于建立高效的“语言理解-视觉感知-具身执行”闭环。现有方法在复杂长距离任务中，常因单智能体的认知过载而出现感知失真与决策漂移。受分布式认知理论启发，本文提出多智能体协同导航框架MA-CoNav。该框架采用“主-从”分层智能体协作架构，将导航任务所需的感知、规划、执行与记忆功能解耦并分配给专业化智能体。具体而言，主智能体负责全局统筹，从属智能体组通过明确分工协作：观测智能体生成环境描述，规划智能体执行任务分解与动态验证，执行智能体处理同步建图与行动，记忆智能体管理结构化经验。此外，框架引入“局部-全局”双阶段反思机制，动态优化整个导航流程。实验基于Limo Pro机器人采集的真实室内数据集展开，全程未对模型进行场景特定微调。结果表明，MA-CoNav在多项指标上全面超越现有主流视觉语言导航方法。

---

### 5. Watch Your Step: Learning Semantically-Guided Locomotion in Cluttered Environment

- **作者**: Denan Liang, Yuan Zhu, Ruimeng Liu, Thien-Minh Nguyen, Shenghai Yuan, Lihua Xie
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.02657v1)
- **发表日期**: 2026-03-03
- **匹配关键词**: navigation
- **arXiv**: [2603.02657v1](http://arxiv.org/abs/2603.02657v1)
- **📥 PDF**: 已下载至本地 (`2603.02657v1_Watch_Your_Step_Learning_Semantically-Guided_Locomotion_in_Cluttered_Environment.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 尽管腿式机器人在崎岖地形上展现出卓越的移动能力，但在杂乱环境中安全使用它们仍是一大挑战。核心问题在于其无法规避低矮障碍物，例如平坦地面上高价值的小型设备或电缆。这一局限源于高层语义理解与底层控制之间的脱节，以及实际运行中高程地图的误差。为解决此问题，我们提出了SemLoco——一种专为密集杂乱环境中精确避障设计的强化学习框架。该框架采用融合软硬约束的双阶段强化学习策略，通过像素级落脚点安全推理实现更精准的足部定位。同时，SemLoco整合语义地图进行可通行性成本评估，而非单纯依赖几何数据。实验表明，该框架能显著减少碰撞并提升敏感物体周边的安全性，在传统控制器易造成损坏的场景中实现可靠导航。进一步研究证实，SemLoco可有效应用于更复杂的非结构化现实环境。

---

### 6. Real-Time Generative Policy via Langevin-Guided Flow Matching for Autonomous Driving

- **作者**: Tianze Zhu, Yinuo Wang, Wenjun Zou, Tianyi Zhang, Likun Wang, Letian Tao, Feihong Zhang, Yao Lyu, Shengbo Eben Li
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.02613v1)
- **发表日期**: 2026-03-03
- **匹配关键词**: exploration
- **arXiv**: [2603.02613v1](http://arxiv.org/abs/2603.02613v1)
- **📥 PDF**: 已下载至本地 (`2603.02613v1_Real-Time_Generative_Policy_via_Langevin-Guided_Flow_Matching_for_Autonomous_Driving.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 强化学习是自动驾驶系统中的基础方法，其中生成式策略通过利用其建模复杂分布的能力来增强探索，展现出巨大潜力。然而，其固有的高推理延迟严重阻碍了其在实时决策与控制中的部署。为解决这一问题，我们提出基于流匹配的熵调节扩散行动者-评论家方法，通过将流匹配引入在线强化学习，实现在单步推理中生成具有竞争力的动作。该方法利用朗之万动力学和Q函数梯度，将经验回放中的动作动态优化至目标分布，该分布平衡了高Q值信息与探索行为。随后训练流策略以高效学习从简单先验分布到这一动态目标的映射。在复杂的多车道和交叉口仿真中，该方法在保持超低推理延迟的同时，其性能超越了基线方法熵调节扩散行动者-评论家与分布式软行动者-评论家。该方法在标准强化学习基准DeepMind控制套件上进一步展现了可扩展性，在人形站立任务中获得775.8分，超越了现有方法。综合来看，这些结果表明该方法是一种高性能且计算效率高的强化学习算法。

---

### 7. SemGS: Feed-Forward Semantic 3D Gaussian Splatting from Sparse Views for Generalizable Scene Understanding

- **作者**: Sheng Ye, Zhen-Hui Dong, Ruoyu Fan, Tian Lv, Yong-Jin Liu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.02548v1)
- **发表日期**: 2026-03-03
- **匹配关键词**: 3D gaussian splatting, gaussian splatting
- **arXiv**: [2603.02548v1](http://arxiv.org/abs/2603.02548v1)
- **📥 PDF**: 已下载至本地 (`2603.02548v1_SemGS_Feed-Forward_Semantic_3D_Gaussian_Splatting_from_Sparse_Views_for_Generalizable_Scene_Understa.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 对三维场景的语义理解是机器人在复杂环境中高效安全运行的关键。现有语义场景重建与语义感知新视角合成方法通常依赖密集多视角输入，且需针对特定场景进行优化，这限制了其在实际应用中的实用性与可扩展性。为应对这些挑战，我们提出SemGS——一种基于稀疏图像输入重建可泛化语义场的前馈式框架。SemGS采用双分支架构分别提取色彩与语义特征，其中两个分支共享浅层CNN网络，使语义推理能够利用色彩外观中的纹理与结构线索。我们在特征提取器中引入相机感知注意力机制，显式建模相机视角间的几何关系。提取的特征被解码为共享几何一致性同时保留分支特定属性的双高斯表示，并通过光栅化合成新视角下的语义图。此外，我们提出区域平滑损失函数以增强语义连贯性。实验表明，SemGS在基准数据集上达到最先进性能，同时在多样化合成与真实场景中展现出快速推理能力与强大泛化性能。

---

### 8. Safe Whole-Body Loco-Manipulation via Combined Model and Learning-based Control

- **作者**: Alexander Schperberg, Yeping Wang, Stefano Di Cairano
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.02443v1)
- **发表日期**: 2026-03-02
- **匹配关键词**: locomotion and manipulation
- **arXiv**: [2603.02443v1](http://arxiv.org/abs/2603.02443v1)
- **📥 PDF**: 已下载至本地 (`2603.02443v1_Safe_Whole-Body_Loco-Manipulation_via_Combined_Model_and_Learning-based_Control.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 同步运动与操作能力使机器人能够突破固定基座的限制，与环境进行交互。然而，在考虑接触交互过程中的安全性与顺应性的同时，协调腿部运动与手臂操作仍具挑战性。为此，我们提出一种全身控制器，将基于模型的导纳控制应用于机械臂，并结合强化学习策略控制腿部运动。导纳控制器将外部力矩（例如人类在物理交互过程中施加的力矩）映射为期望的末端执行器速度，从而实现顺应行为。手臂与腿部控制器协同跟踪这些速度，实现统一的六自由度力响应。基于模型的设计通过参考调节器实现精确的力控制与安全保障，同时采用神经网络增强的卡尔曼滤波器提升基座速度估计的可靠性，进一步增强了系统鲁棒性。我们在仿真和硬件实验中采用搭载六自由度机械臂及腕部六维力/力矩传感器的Unitree Go2四足机器人验证了该方法。实验结果表明，系统能够准确跟踪交互驱动的速度，在动态环境中表现出顺应行为，并实现安全可靠的操作性能。

---

### 9. OnlineX: Unified Online 3D Reconstruction and Understanding with Active-to-Stable State Evolution

- **作者**: Chong Xia, Fangfu Liu, Yule Wang, Yize Pang, Yueqi Duan
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.02134v2)
- **发表日期**: 2026-03-02
- **匹配关键词**: 3D gaussian splatting, 3D reconstruction, 3d reconstruction, gaussian splatting
- **arXiv**: [2603.02134v2](http://arxiv.org/abs/2603.02134v2)
- **📥 PDF**: 已下载至本地 (`2603.02134v2_OnlineX_Unified_Online_3D_Reconstruction_and_Understanding_with_Active-to-Stable_State_Evolution.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 近期，可泛化三维高斯泼溅（3DGS）技术取得了重要进展，能够在数秒内完成三维场景重建，无需针对每个场景进行单独优化。然而，现有方法主要遵循离线重建范式，缺乏连续重建能力，这限制了它们在机器人、VR/AR等在线场景中的应用。本文提出OnlineX框架，这是一种仅通过流式图像输入就能在线重建三维视觉外观与语言场的前馈式系统。在线建模的核心挑战在于累积漂移问题，其根源在于记忆状态的两种对立角色之间的根本冲突：一方面需要作为活跃状态持续更新以捕捉高频局部几何特征，另一方面又需作为稳定状态保守地积累并保持长期全局结构。为解决这一问题，我们提出了解耦的“活跃-稳定”状态演化范式。该框架将记忆状态解耦为专用的活跃状态与持久的稳定状态，并通过协同融合前者的信息到后者，实现重建的精确性与稳定性。此外，我们联合建模视觉外观与语言场，并引入隐式高斯融合模块以提升重建质量。在主流数据集上的实验表明，本方法在新视角合成与语义理解任务中均优于现有方法，在不同长度的输入序列上均展现出鲁棒性能，且具备实时推理速度。

---

### 10. Closed-Loop Action Chunks with Dynamic Corrections for Training-Free Diffusion Policy

- **作者**: Pengyuan Wu, Pingrui Zhang, Zhigang Wang, Dong Wang, Bin Zhao, Xuelong Li
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.01953v1)
- **发表日期**: 2026-03-02
- **匹配关键词**: diffusion policy
- **arXiv**: [2603.01953v1](http://arxiv.org/abs/2603.01953v1)
- **📥 PDF**: 已下载至本地 (`2603.01953v1_Closed-Loop_Action_Chunks_with_Dynamic_Corrections_for_Training-Free_Diffusion_Policy.pdf`)
- **🔓 开源**: GITHUB, PROJECT_PAGE
  - 链接：https://github.com/wupengyuan/dcdp
- **中文摘要**: 基于扩散的策略在机器人操作中取得了显著成果，但在动态场景中往往难以快速适应，导致响应延迟或任务失败。我们提出DCDP——一种动态闭环扩散策略框架，该框架将分块动作生成与实时校正相结合。DCDP通过集成自监督动态特征编码器、交叉注意力融合机制及非对称动作编码器-解码器，在执行动作前注入环境动态信息，实现实时闭环动作校正，从而增强系统在动态场景中的适应性。在动态PushT仿真实验中，DCDP无需重新训练即可提升19%的适应能力，且仅需增加5%的计算开销。其模块化设计支持即插即用集成，在包括真实世界操作任务在内的动态机器人场景中，既能保持时间连贯性，又能实现实时响应。项目页面位于：https://github.com/wupengyuan/dcdp

---

### 11. SaferPath: Hierarchical Visual Navigation with Learned Guidance and Safety-Constrained Control

- **作者**: Lingjie Zhang, Zeyu Jiang, Changhao Chen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.01898v1)
- **发表日期**: 2026-03-02
- **匹配关键词**: navigation, visual navigation
- **arXiv**: [2603.01898v1](http://arxiv.org/abs/2603.01898v1)
- **📥 PDF**: 已下载至本地 (`2603.01898v1_SaferPath_Hierarchical_Visual_Navigation_with_Learned_Guidance_and_Safety-Constrained_Control.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉导航是移动机器人的核心能力，然而端到端学习方法在未知、杂乱或狭窄环境中常面临泛化性与安全性挑战。这些局限在密集室内场景中尤为突出，碰撞风险高且端到端模型易失效。为此，我们提出SaferPath——一种分层视觉导航框架，该框架通过安全约束优化控制模块，利用现有端到端模型的学习引导信息并进行精细化处理。SaferPath将视觉观测转换为可通行区域地图，并采用模型预测斯坦因变分进化策略（MP-SVES）优化引导轨迹，仅需数次迭代即可高效生成安全轨迹。优化后的轨迹由模型预测控制器跟踪执行，确保在复杂环境中的鲁棒导航。通过在未知障碍物、密集非结构化空间及狭窄走廊场景中的大量实验证明，SaferPath能持续提升成功率并降低碰撞率，其性能优于ViNT、NoMaD等代表性基线方法，实现了在挑战性现实场景中的安全导航。

---

### 12. LoGeR: Long-Context Geometric Reconstruction with Hybrid Memory

- **作者**: Junyi Zhang, Charles Herrmann, Junhwa Hur, Chen Sun, Ming-Hsuan Yang, Forrester Cole, Trevor Darrell, Deqing Sun
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.03269v1)
- **发表日期**: 2026-03-03
- **匹配关键词**: 3D reconstruction, 3d reconstruction
- **arXiv**: [2603.03269v1](http://arxiv.org/abs/2603.03269v1)
- **📥 PDF**: 已下载至本地 (`2603.03269v1_LoGeR_Long-Context_Geometric_Reconstruction_with_Hybrid_Memory.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 前馈几何基础模型在短窗口重建方面表现出色，但将其扩展至数分钟长视频时，受限于二次注意力复杂度或循环设计中有限的有效内存。我们提出LoGeR（长上下文几何重建）——一种无需后优化即可将密集三维重建扩展至超长序列的新型架构。LoGeR通过分块处理视频流，利用强双向先验实现高保真度的块内推理。为应对跨块边界连贯性这一关键挑战，我们提出基于学习的混合记忆模块。该双组件系统结合参数化测试时训练（TTT）记忆以锚定全局坐标系并防止尺度漂移，同时采用非参数化滑动窗口注意力（SWA）机制保留未压缩上下文以实现高精度相邻对齐。值得注意的是，这种记忆架构使LoGeR能在128帧序列上训练，并在推理时泛化至数千帧。通过在标准基准测试集及新改造的VBR数据集（包含长达1.9万帧序列）上进行评估，LoGeR显著超越现有最先进的前馈方法——在KITTI数据集上降低超过74%的绝对轨迹误差——并在前所未有的时间跨度上实现了鲁棒且全局一致的重建。

---

### 13. VIRGi: View-dependent Instant Recoloring of 3D Gaussians Splats

- **作者**: Alessio Mazzucchelli, Ivan Ojeda-Martin, Fernando Rivas-Manzaneque, Elena Garces, Adrian Penate-Sanchez, Francesc Moreno-Noguer
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.02986v1)
- **发表日期**: 2026-03-03
- **匹配关键词**: 3d reconstruction, 3D reconstruction, 3D gaussian splatting, neural radiance field, gaussian splatting
- **arXiv**: [2603.02986v1](http://arxiv.org/abs/2603.02986v1)
- **📥 PDF**: 已下载至本地 (`2603.02986v1_VIRGi_View-dependent_Instant_Recoloring_of_3D_Gaussians_Splats.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 三维高斯溅射（3DGS）技术因其能够精确建模复杂三维场景并具备前所未有的渲染性能，近年来彻底革新了新视角合成与三维重建领域。然而，一个重大挑战依然存在：缺乏高效且逼真的方法来编辑场景内容的外观。本文提出VIRGi——一种在保持镜面高光等视角依赖效果的同时，快速编辑3DGS建模场景色彩的新方法。我们方法的核心在于：将色彩分解为漫反射与视角依赖分量的新型架构，以及整合多视角图像块的多视图训练策略。相较于传统的单视图批量训练，我们的3DGS表征能实现更精确的重建，并为色彩重编辑任务提供稳健的表征基础。针对3DGS色彩重编辑，我们进一步提出仅需终端用户提供一张手动编辑场景图像的快速方案。通过微调单个多层感知器的权重，结合可编辑区域单次分割模块，色彩编辑能在两秒内无缝传播至整个场景，实现实时交互并支持对视角依赖效果强度的精准控制。在多数据集上的全面验证表明，该方法相较于基于神经辐射场表征的现有技术，在定量与定性评估上均取得显著进步。

---

### 14. The Dresden Dataset for 4D Reconstruction of Non-Rigid Abdominal Surgical Scenes

- **作者**: Reuben Docea, Rayan Younis, Yonghao Long, Maxime Fleury, Jinjing Xu, Chenyang Li, André Schulze, Ann Wierick, Johannes Bender, Micha Pfeiffer, Qi Dou, Martin Wagner, Stefanie Speidel
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.02985v1)
- **发表日期**: 2026-03-03
- **匹配关键词**: 3D reconstruction, 3d reconstruction
- **arXiv**: [2603.02985v1](http://arxiv.org/abs/2603.02985v1)
- **📥 PDF**: 已下载至本地 (`2603.02985v1_The_Dresden_Dataset_for_4D_Reconstruction_of_Non-Rigid_Abdominal_Surgical_Scenes.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: D4D数据集提供了配对的腹腔镜视频与高质量结构光几何数据，用于评估真实手术条件下腹部软组织形变的三维重建效果。该数据通过达芬奇Xi立体内窥镜和Zivid结构光相机，在六次猪体实验中采集完成，并采用光学追踪与人工校核的迭代配准方法进行数据对齐。数据集包含三种序列类型——整体形变、渐进形变及相机移动片段，用于测试算法对非刚性运动、形变幅度及视野外更新的鲁棒性。每个片段均提供校正后的立体图像、逐帧器械掩膜、立体深度图、起始/终止结构光点云、校准后的相机位姿及内参。后处理阶段采用ICP与半自动配准技术完成数据对齐，并生成器械掩膜。该数据集支持可见区域与遮挡区域的定量几何评估，同时提供光度视图合成基准。数据集包含98组精选记录，总计超过30万帧图像及369个点云，可作为开发与评估非刚性SLAM、四维重建及深度估计方法的综合性基准资源。

---

### 15. TagaVLM: Topology-Aware Global Action Reasoning for Vision-Language Navigation

- **作者**: Jiaxing Liu, Zexi Zhang, Xiaoyan Li, Boyue Wang, Yongli Hu, Baocai Yin
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.02972v1)
- **发表日期**: 2026-03-03
- **匹配关键词**: navigation, VLN
- **arXiv**: [2603.02972v1](http://arxiv.org/abs/2603.02972v1)
- **📥 PDF**: 已下载至本地 (`2603.02972v1_TagaVLM_Topology-Aware_Global_Action_Reasoning_for_Vision-Language_Navigation.pdf`)
- **🔓 开源**: PROJECT_PAGE, CODE
  - 链接：https://apex-bjut.github.io/Taga-VLM
- **中文摘要**: 视觉语言导航（VLN）对大视觉语言模型（VLMs）提出了独特挑战，这源于其固有的架构不匹配：VLMs主要基于静态、非具身的视觉语言任务进行预训练，这与导航的动态性、具身性及空间结构化特性存在根本冲突。现有基于大模型的方法通常将丰富的视觉与空间信息转换为文本，迫使模型隐式推断复杂的视觉-拓扑关系，或限制其全局行动能力。为弥合这一差距，我们提出TagaVLM（拓扑感知全局行动推理框架），这是一种将拓扑结构显式注入VLM主干网络的端到端框架。为引入拓扑边信息，空间拓扑感知残差注意力机制（STAR-Att）将其直接整合至VLM的自注意力模块，在保持预训练知识的同时实现内在空间推理。为增强拓扑节点信息，交错式导航提示机制强化了节点层级的视觉-文本对齐。最终，借助嵌入的拓扑图，模型能够进行全局行动推理，实现鲁棒的路径修正。在R2R基准测试中，TagaVLM在基于大模型的方法中取得最先进性能，在未见环境中达到51.09%的成功率（SR）和47.18的SPL指标，较先前工作分别提升3.39%的SR和9.08的SPL。这表明对于具身空间推理任务，针对小型开源VLMs进行针对性增强比暴力模型缩放更为有效。代码将在论文发表后开源。项目页面：https://apex-bjut.github.io/Taga-VLM

---

### 16. Multimodal-Prior-Guided Importance Sampling for Hierarchical Gaussian Splatting in Sparse-View Novel View Synthesis

- **作者**: Kaiqiang Xiong, Zhanke Wang, Ronggang Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.02866v1)
- **发表日期**: 2026-03-03
- **匹配关键词**: 3D gaussian splatting, gaussian splatting
- **arXiv**: [2603.02866v1](http://arxiv.org/abs/2603.02866v1)
- **📥 PDF**: 已下载至本地 (`2603.02866v1_Multimodal-Prior-Guided_Importance_Sampling_for_Hierarchical_Gaussian_Splatting_in_Sparse-View_Novel.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出以多模态先验引导的重要性采样作为稀疏视角新视图合成中分层三维高斯泼溅（3DGS）的核心机制。该采样器融合了互补线索——包括光度渲染残差、语义先验与几何先验——以生成鲁棒的局部可恢复性估计，直接驱动精细高斯单元的注入位置。围绕此采样核心，我们的框架包含：（1）一种由粗到精的高斯表示，通过稳定的粗糙层编码全局形状，并在多模态度量指示可恢复细节的区域选择性添加精细基元；（2）一种几何感知的采样与保留策略，将优化集中于几何关键及复杂区域，同时保护欠约束区域中新添加的基元免于过早剪枝。通过优先处理具有一致多模态证据支持的区域而非仅依赖原始残差，我们的方法缓解了由纹理过拟合引起的误差，并抑制了位姿/外观不一致产生的噪声。在多种稀疏视角基准测试上的实验表明，该方法实现了最先进的重建效果，在DTU数据集上PSNR指标最高提升达+0.3 dB。

---

### 17. Intrinsic Geometry-Appearance Consistency Optimization for Sparse-View Gaussian Splatting

- **作者**: Kaiqiang Xiong, Rui Peng, Jiahao Wu, Zhanke Wang, Jie Liang, Xiaoyun Zheng, Feng Gao, Ronggang Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.02893v1)
- **发表日期**: 2026-03-03
- **匹配关键词**: gaussian splatting
- **arXiv**: [2603.02893v1](http://arxiv.org/abs/2603.02893v1)
- **📥 PDF**: 已下载至本地 (`2603.02893v1_Intrinsic_Geometry-Appearance_Consistency_Optimization_for_Sparse-View_Gaussian_Splatting.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 从单张图像进行三维人体重建是一个具有挑战性的问题，在学术界得到了广泛研究。近期，部分方法开始借助扩散模型进行引导，通过分数蒸馏采样优化三维表征，或生成背面视角图像以辅助重建。然而，这些方法往往会产生不理想的伪影（例如因多视角先验不一致导致的人体结构扁平化或过度平滑现象），且在真实场景的泛化能力上存在局限。本研究提出**MVD-HuGaS**方法，通过多视角人体扩散模型实现单张图像的自由视角三维人体渲染。我们首先采用增强型多视角扩散模型从单张参考图像生成多视角图像，该模型在高质量三维人体数据集上经过精细微调，融合了三维几何先验与人体结构先验。为从稀疏生成的多视角图像中推断精确相机位姿以支持重建，我们引入对齐模块来协同优化三维高斯模型与相机位姿。此外，提出基于深度的面部畸变缓解模块对生成的面部区域进行精细化处理，从而提升整体重建保真度。最终，MVD-HuGaS利用优化后的多视角图像及其精确相机位姿，对目标人体的三维高斯模型进行优化，实现高保真度的自由视角渲染。在Thuman2.0和2K2K数据集上的大量实验表明，所提出的MVD-HuGaS方法在单视角三维人体渲染任务上达到了最先进的性能水平。

---

### 18. Articulation in Motion: Prior-free Part Mobility Analysis for Articulated Objects By Dynamic-Static Disentanglement

- **作者**: Hao Ai, Wenjie Chang, Jianbo Jiao, Ales Leonardis, Ofek Eyal
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.02910v1)
- **发表日期**: 2026-03-03
- **匹配关键词**: articulated object
- **arXiv**: [2603.02910v1](http://arxiv.org/abs/2603.02910v1)
- **📥 PDF**: 已下载至本地 (`2603.02910v1_Articulation_in_Motion_Prior-free_Part_Mobility_Analysis_for_Articulated_Objects_By_Dynamic-Static_D.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://haoai-1997.github.io/AiM/.
- **中文摘要**: 铰接物体在日常生活中无处不在。我们的目标是实现高质量的重建、独立运动部件的分割以及关节运动分析。现有方法通常基于已知部件数量的先验知识，通过分析两种不同关节状态并执行逐点部件分割，利用跨状态对应关系优化各部件关节参数。这种假设极大地限制了其应用范围和性能表现——当物体无法在两种状态下清晰可见时，其鲁棒性会显著降低。为解决这些问题，本文提出名为"运动中的关节分析"（AiM）的新框架。我们通过用户-物体交互视频和初始状态扫描，推断部件级分解结构、关节运动学参数，并重建可交互的3D数字模型。该框架采用双高斯场景表示法，通过物体初始3D高斯溅射扫描和部件运动视频进行学习，利用运动线索将物体分割为不同部件并分配关节连接点。随后采用鲁棒的顺序随机抽样一致性算法，在无需任何部件级结构先验的条件下实现部件运动性分析——该方法将运动基元聚类为刚性部件，在自动确定部件数量的同时估算运动学参数。所提出的方法将物体分离为多个部件，每个部件均以3D高斯集合表示，从而实现高质量渲染。相较于现有方法，本方法在无需先验知识的情况下实现了更高质量的部件分割。通过对简单和复杂物体的广泛实验分析，验证了本方法的有效性和强大泛化能力。项目页面：https://haoai-1997.github.io/AiM/。

---

## 📌 Poster

*其他相关研究*

---

### 1. Robotic Grasping and Placement Controlled by EEG-Based Hybrid Visual and Motor Imagery

- **作者**: Yichang Liu, Tianyu Wang, Ziyi Ye, Yawei Li, Yu-Gang Jiang, Shouyan Wang, Yanwei Fu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.03181v1)
- **发表日期**: 2026-03-03
- **匹配关键词**: human-robot interaction, human-robot collaboration
- **arXiv**: [2603.03181v1](http://arxiv.org/abs/2603.03181v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出一个集成脑电图视觉与运动想象（VI/MI）与机器人控制的框架，实现实时、意图驱动的抓取与放置操作。受脑机接口驱动机器人技术提升人机交互潜力的启发，本系统通过在在线流式处理管道中以零样本方式部署离线预训练解码器，将神经信号与物理控制相连接。该框架构建了一个双通道意图接口：视觉想象用于识别待抓取物体，运动想象则确定放置姿态，从而实现对抓取目标与放置位置的双重直观控制。系统采用无提示想象协议，完全依赖脑电信号运行，实现了全流程集成与在线验证。在Base机器人平台上部署后，经过多场景测试（包括目标遮挡或参与者姿态变化等情况），系统在线解码准确率达到40.23%（视觉想象）和62.59%（运动想象），端到端任务成功率为20.88%。实验结果表明，高级视觉认知能够被实时解码并转化为可执行的机器人指令，成功弥合了神经信号与物理交互之间的鸿沟，验证了纯想象式脑机接口范式在实际人机协作应用中的灵活性。

---

### 2. From Language to Action: Can LLM-Based Agents Be Used for Embodied Robot Cognition?

- **作者**: Shinas Shaji, Fabian Huppertz, Alex Mitrevski, Sebastian Houben
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.03148v1)
- **发表日期**: 2026-03-03
- **匹配关键词**: navigation, mobile manipulator
- **arXiv**: [2603.03148v1](http://arxiv.org/abs/2603.03148v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 为使机器人能够在日常环境中灵活行动，其需要具备多种认知能力，以实现对计划的推理和执行恢复。大型语言模型（LLMs）已展现出涌现的认知特性，如推理和语言理解能力；然而，要实现对具身机器人代理的控制，需要可靠地将高层语言与低层感知控制功能相衔接。本文探讨了大型语言模型在认知机器人架构中作为规划与执行推理核心组件的潜力。为此，我们提出一种认知架构，其中具备自主性的LLM作为规划与推理的核心组件，而工作记忆与情景记忆组件则支持从经验中学习与适应。通过该架构的一个实例，我们在模拟家庭环境中控制移动机械臂，环境交互通过一组高层工具实现，包括感知、推理、导航、抓取和放置等功能，这些工具均对基于LLM的代理开放。我们在两项家庭任务（物体放置与物体置换）中评估所提出的系统，以检验代理的推理、规划及记忆运用能力。实验结果表明，LLM驱动的代理能够完成结构化任务，并展现出涌现的适应能力与基于记忆的规划能力，但也暴露出显著局限性，例如对任务成功产生幻觉性认知，以及在遵循指令方面表现欠佳——拒绝承认并完成序列任务。这些发现既凸显了将LLM用作自主机器人具身认知控制器的潜力，也揭示了其面临的挑战。

---

