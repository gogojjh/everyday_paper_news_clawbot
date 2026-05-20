# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-05-20 08:02

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 2/20 篇提供

**🌟 Highlight**: 9 篇 | **📌 Poster**: 11 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. RGB-only Active 3D Scene Graph Generation for Indoor Mobile Robots

- **作者**: Giorgia Modi, Davide Buoso, Giuseppe Averta, Daniele De Martini
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.18197v1)
- **发表日期**: 2026-05-18
- **匹配关键词**: scene graph, scene graph generation, exploration, 3D reconstruction, 3d reconstruction
- **arXiv**: [2605.18197v1](http://arxiv.org/abs/2605.18197v1)
- **📥 PDF**: 已下载至本地 (`2605.18197v1_RGB-only_Active_3D_Scene_Graph_Generation_for_Indoor_Mobile_Robots.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 当前的三维场景图生成方法依赖专用深度传感器（如激光雷达或RGB-D相机）进行度量三维重建，这限制了其在专用机器人平台上的部署，并排除了仅配备RGB相机的场景（如固定外部基础设施）。现有流程通常基于被动采集的观测轨迹运行，而非根据部分构建的场景表示选择视角，因此无法在探索过程中有效利用图中编码的语义与空间信息。本文提出了一种全视觉框架，仅通过RGB输入即可主动、增量式地构建三维场景图，同时解决了上述两个局限性。该方法围绕一种共享的结构化表示统一感知与规划，该表示能够捕捉物体语义、三维几何、关系上下文以及多视角信息。由于该框架与硬件无关且仅依赖RGB观测，它可以将机载机器人相机与固定外部相机的输入整合到同一表示中。在Replica数据集上的实验表明，仅使用RGB的流程在F1分数上与使用真实深度数据的基线方法持平。在ReplicaCAD上的主动探索实验进一步显示，在相同探索预算下，基于语义驱动的视角选择比基于几何前沿的基线方法多检测两倍以上的物体。最后，外部相机设置证明，互补的RGB视角能够有效引导场景图的构建，并在不增加探索成本的情况下提升上下文理解能力。

---

### 2. Fixed External Cameras as Common Prior Maps for Active 3D Scene Graph Generation

- **作者**: Giorgia Modi, Davide Buoso, Giuseppe Averta, Daniele De Martini
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.18184v1)
- **发表日期**: 2026-05-18
- **匹配关键词**: scene graph, scene graph generation, exploration, 3D reconstruction, 3d reconstruction
- **arXiv**: [2605.18184v1](http://arxiv.org/abs/2605.18184v1)
- **📥 PDF**: 已下载至本地 (`2605.18184v1_Fixed_External_Cameras_as_Common_Prior_Maps_for_Active_3D_Scene_Graph_Generation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 常见的先验信息，如BIM模型、楼层平面图和遥感影像，能够为自主机器人系统提供有价值的几何与语义背景。本文将固定外部RGB摄像头的观测视为通用先验地图（CPMs）：在机器人运动开始前，这些环境广角视图可初始化场景的语义与几何先验。我们提出了一种基于纯RGB的主动增量式三维场景图（3DSG）生成框架，该框架通过单一硬件无关的流水线，无缝融合机器人机载摄像头与固定外部摄像头的观测数据。系统仅依赖前馈三维重建模型处理的RGB观测，将所有摄像头（机载或外部）一视同仁，无需任何硬件改造。随后，基于图的主动语义探索框架直接利用部分场景图，引导机器人前往语义不确定性高的区域，逐步完善并优化先验信息。实验表明，即使仅通过单个外部摄像头引导场景图初始化，初始物体召回率最高可提升79%，且更丰富的先验上下文能显著提升后续主动探索的效率。

---

### 3. Efficient 3D Content Reconstruction and Generation

- **作者**: Jiahao Li
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.18052v1)
- **发表日期**: 2026-05-18
- **匹配关键词**: 3D reconstruction, 3d reconstruction
- **arXiv**: [2605.18052v1](http://arxiv.org/abs/2605.18052v1)
- **📥 PDF**: 已下载至本地 (`2605.18052v1_Efficient_3D_Content_Reconstruction_and_Generation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 自动三维内容创建旨在用能够直接从文本或图像合成或恢复三维资产的系统，取代劳动密集型的建模与扫描流程。其应用涵盖电子游戏、虚拟现实、机器人技术和仿真领域，可实现快速资产原型设计、多样化交互世界生成，以及为训练基础模型提供高效的三维数据采集。当代解决方案主要遵循两种互补范式：（i）文本或图像到三维的生成，通过学习三维几何与外观的先验知识，从自然语言或单视角图像创建全新资产；（ii）三维重建，从RGB图像中估计相机位姿与几何结构。本论文对这两个方向均进行了推进。在生成方面，我提出了Instant3D，该方法将多视角扩散与前馈稀疏视角三维重建相结合，可在5-20秒内生成高质量资产。在重建方面，我开发了FastMap——一种运动恢复结构流程，通过广泛使用融合GPU内核的一阶优化，在保持相当位姿精度与下游新视角合成质量的同时，相比先前最先进方法实现了高达10倍的加速。

---

### 4. Imaging Hidden Objects with Consumer LiDAR via Motion Induced Sampling

- **作者**: Siddharth Somasundaram, Aaron Young, Akshat Dave, Adithya Pediredla, Ramesh Raskar
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.17865v1)
- **发表日期**: 2026-05-18
- **匹配关键词**: 3D reconstruction, 3d reconstruction
- **arXiv**: [2605.17865v1](http://arxiv.org/abs/2605.17865v1)
- **📥 PDF**: 已下载至本地 (`2605.17865v1_Imaging_Hidden_Objects_with_Consumer_LiDAR_via_Motion_Induced_Sampling.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 激光雷达正越来越多地应用于手持设备、可穿戴设备和机器人等消费级成像场景。这类传感器能以皮秒级精度捕捉光的飞行时间，理论上可获取视野外隐藏物体的信息。尽管这种非视域成像能力已在研究级激光雷达上得到验证，但由于消费级设备存在激光功率低、空间分辨率不足以及物体与相机运动等问题导致的信号质量差，实现该功能仍具挑战性。受连拍成像与合成孔径雷达启发，我们提出多帧融合策略以攻克这些难题，并在消费级激光雷达上实现了非视域成像。首先引入运动诱导孔径采样模型，将物体形状、物体运动与相机运动的影响统一纳入单一测量模型。基于该模型，我们在手机级激光雷达上实现了多项非视域功能：(1)三维重建，(2)单目标与多目标追踪，(3)利用隐藏物体进行相机定位。此前非视域成像能力主要局限于需要复杂设置与校准的笨重昂贵研究级硬件。我们的成果标志着向即插即用型非视域成像的转变——任何人只需使用现成硬件（成本低于100美元）且无需额外设置即可对隐藏物体成像。我们相信，这种能力的普及将推动非视域成像在消费领域的应用发展。

---

### 5. Mono-Hydra++: Real-Time Monocular Scene Graph Construction with Multi-Task Learning for 3D Indoor Mapping

- **作者**: U. V. B. L. Udugama, George Vosselman, Francesco Nex
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.17661v1)
- **发表日期**: 2026-05-17
- **匹配关键词**: scene graph, exploration
- **arXiv**: [2605.17661v1](http://arxiv.org/abs/2605.17661v1)
- **📥 PDF**: 已下载至本地 (`2605.17661v1_Mono-Hydra++_Real-Time_Monocular_Scene_Graph_Construction_with_Multi-Task_Learning_for_3D_Indoor_Map.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 自主敏捷机器人需要的不仅仅是度量几何：它们必须理解物体、房间、场所及空间关系，以完成搜索、检查、探索和人机交互任务。传统度量地图支持定位与避障，但无法提供这种语义与关系结构。3D场景图通过将几何信息与物体级、房间级理解相连接，弥补了这一空白。然而，在敏捷平台上构建此类表征仍具挑战性，因为空中机器人和轻量级机器人受限于严格的载荷、功耗和计算约束，使得RGB-D相机和LiDAR传感器在多数机载场景中难以实用。我们提出Mono-Hydra++，一种面向室内度量语义建图与分层3D场景图构建的实时单目RGB+IMU流水线。该系统将基于DINOv3的多任务深度与语义模型M2H-MX，与深度特征视觉惯性里程计前端、VIO位姿图中的稀疏预测深度约束、动态区域语义掩码、以及体素融合前的位姿感知时序对齐相结合。在Go-SLAM ScanNet评估子集上，Mono-Hydra++的平均轨迹误差比对比中最强的RGB-D基线低1.6%，且仅使用单目RGB+IMU输入。在校准后的7-Scenes数据集上，其平均ATE比最强校准基线提升29.8%。我们进一步在真实ITC建筑部署中利用RealSense RGB+IMU验证了Mono-Hydra++，并通过在Jetson Orin NX 16GB上以25.53 FPS运行ONNX/TensorRT FP16 M2H-MX-L感知模型，证明了其嵌入式可行性。这些结果表明，Mono-Hydra++能够为资源受限的机器人平台提供实时度量语义建图与场景图构建，且无需依赖主动深度传感器。

---

### 6. Motion-Uncertainty-Aware Next-Best-View Planning for Moving Object Reconstruction

- **作者**: Karen Li, Mattia Mantovani, Robert J. Wood, Lorenzo Sabattini, Stephanie Gil
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.17593v1)
- **发表日期**: 2026-05-17
- **匹配关键词**: 3D reconstruction, 3d reconstruction, active perception
- **arXiv**: [2605.17593v1](http://arxiv.org/abs/2605.17593v1)
- **📥 PDF**: 已下载至本地 (`2605.17593v1_Motion-Uncertainty-Aware_Next-Best-View_Planning_for_Moving_Object_Reconstruction.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 面向运动物体的主动三维重建，需要在决策到执行延迟期间，在考虑物体运动不确定性的同时选择信息量丰富的视角。现有方法仅解决该问题的部分环节：面向物体重建的下一最佳视角（NBV）规划器通常优化表面覆盖率但假设物体静止，而面向运动目标的运动感知主动方法虽考虑目标运动，却优先保障跟踪或可见性而非重建覆盖率。本文提出一种运动不确定性感知的NBV框架，用于重建进行平面运动的未知刚体，该框架利用物体的含噪平面位置测量数据与移动机器人的深度观测。核心思想是：不基于单一预测物体位姿，而是通过评估候选视角在由运动与测量不确定性引发的合理未来物体状态下的预期观测质量来评价该视角。为获取这种预测置信状态，采用固定滞后高斯过程平滑器从含噪位置测量中估计并预测物体状态。基于该置信状态，在预测物体位置周围生成候选视角，通过可达性筛选后估算其预期覆盖率驱动评分。仿真与实物实验表明，相较于非预测性NBV及纯预测跟踪方法，本方法显著提升了重建完整性，弥合了覆盖率驱动的主动重建与预测驱动跟踪之间的鸿沟。

---

### 7. AffordVLA: Injecting Affordance Representations into Vision-Language-Action Models via Implicit Feature Alignment

- **作者**: Weijie Kong, Zhian Su, Wei Yu, Huixu Dong
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.17517v1)
- **发表日期**: 2026-05-17
- **匹配关键词**: implicit representation, affordance, vision-language-action, VLA, vision-language-action model
- **arXiv**: [2605.17517v1](http://arxiv.org/abs/2605.17517v1)
- **📥 PDF**: 已下载至本地 (`2605.17517v1_AffordVLA_Injecting_Affordance_Representations_into_Vision-Language-Action_Models_via_Implicit_Featu.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 近期，视觉-语言-动作（VLA）模型在通用机器人操作领域展现出巨大潜力。然而，多数VLA模型的视觉表征往往被全局物体外观主导，难以聚焦与任务相关的功能性交互区域，这限制了其在非结构化环境中的鲁棒性。现有基于功能可供性的方法通常依赖显式掩码注入或外部感知模块，不仅需要额外标注，还会引入级联感知误差与推理开销。为解决上述问题，我们提出AffordVLA——一种通过隐式表征对齐将操作中心化的功能可供性感知内化至VLA视觉表征的功能增强型VLA框架。具体而言，我们构建零样本功能可供性教师模型，从RGB观测与语言指令中提取任务条件化的功能可供性视觉表征。AffordVLA将VLA的中间视觉表征与教师模型提取的功能可供性视觉表征进行对齐，从而将操作中心化的功能可供性感知隐式注入VLA视觉表征，提升动作精度。大量仿真与真实世界实验表明，AffordVLA及其功能可供性教师模型均达到最优性能，显著超越强基线模型。消融分析证实，AffordVLA在保持推理效率的同时有效重塑VLA视觉表征，进而提升操作成功率与训练效率。

---

### 8. HCLM: A Hierarchical Framework for Cooperative Loco-Manipulation with Dual Quadrupeds

- **作者**: Qixuan Li, Chen Le, Jincheng Yu, Xinlei Chen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.17300v1)
- **发表日期**: 2026-05-17
- **匹配关键词**: diffusion policy
- **arXiv**: [2605.17300v1](http://arxiv.org/abs/2605.17300v1)
- **📥 PDF**: 已下载至本地 (`2605.17300v1_HCLM_A_Hierarchical_Framework_for_Cooperative_Loco-Manipulation_with_Dual_Quadrupeds.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出HCLM，一种面向双四足系统通用协作式全身操控的分层框架。协调多机器人浮动基座间的协同操控极具挑战性，这源于空间协调、鲁棒运动与闭链物理交互之间的冲突需求。为解决该问题，本架构系统性地将高层协作推理与低层鲁棒运动执行解耦。在高层，集中式联合扩散策略利用SE(3)不变的任务空间表征，学习与坐标系无关的空间协调模式。为将这些与框架无关的参考转化为物理运动，以任务为中心的混合全身控制器将用于无碰撞速度分布的主动运动学模型预测控制与反应式执行层协同运作。关键之处在于，该反应层既能保证末端执行器精准追踪的快速响应性，又通过协作导纳方案集成主动力调节，以安全解决运动学冲突并严格约束闭链交互中的内部应力。我们在逐步提升难度的仿真场景（包括协作搬运、打包与交接）中验证该框架，并成功将后者部署至真实环境。实验结果展示了可靠的任务执行能力、严格的任务无关性，以及对剧烈物理扰动的卓越鲁棒性，为多机器人具身协调提供了高度稳健的解决方案。

---

### 9. Event-Grounded Sparse Autoencoders for Vision-Language-Action Policies

- **作者**: Xinchen Jin, Aditya Chatterjee, Pranav Kumar, Rohan Paleja
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.17204v1)
- **发表日期**: 2026-05-17
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2605.17204v1](http://arxiv.org/abs/2605.17204v1)
- **📥 PDF**: 已下载至本地 (`2605.17204v1_Event-Grounded_Sparse_Autoencoders_for_Vision-Language-Action_Policies.pdf`)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/xc-j/Event-SAE
- **中文摘要**: 视觉-语言-动作（VLA）策略将语言和视觉输入转化为机器人动作，其隐藏表征直接塑造闭环行为。然而，来自语言和视觉-语言模型的机制可解释性工具无法直接迁移至VLA：输出为机器人动作而非人类可读的标记，且干预措施只能通过昂贵的闭环部署进行测试。我们提出了一种基于事件的可解释性流程，将稀疏自编码器（SAE）特征分析锚定于行为事件而非文本语境。通过视觉、状态和时间线索对每个任务中的末端执行器关键帧进行聚类，将SAE特征与行为显著事件相关联，并通过可选的视觉-语言模型（VLM）注释与语义上下文建立联系。据我们所知，我们的流程是首个将基于SAE的VLA分析扎根于闭环行为事件的方法。在两个仿真架构和一项真实机器人研究中，基于事件的排序对OpenVLA产生了最强的因果效应，并迁移至π₀.₅的连续动作块。SAE是一种稀疏但非完美的干预基础：其可用性因架构和干预位置而异，激进的干预揭示了安全性与可解释性的局限。总体而言，基于事件的SAE分析为行为锚定的VLA可解释性提供了实用起点，激励未来在超越动作对齐坐标的SAE特征、更细粒度的闭环评估以及高风险VLA部署的安全干预方面开展研究。代码已开源：\url{https://github.com/xc-j/Event-SAE}。

---

## 📌 Poster

*其他相关研究*

---

### 1. Robo-Cortex: A Self-Evolving Embodied Agent via Dual-Grain Cognitive Memory and Autonomous Knowledge Induction

- **作者**: Nga Teng Chan, Yi Zhang, Yechi Liu, Renwen Cui, Fanhu Zeng, Zeyuan Ding, Xiancong Ren, Zhang Zhang, Qifeng Chen, Jian Liu, Yong Dai, Xiaozhu Ju
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.18729v1)
- **发表日期**: 2026-05-18
- **匹配关键词**: navigation, exploration
- **arXiv**: [2605.18729v1](http://arxiv.org/abs/2605.18729v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 在复杂环境中导航与交互的能力是现实世界具身智能体的核心，然而由于"经验性失忆"——现有基于轨迹驱动或反应式策略无法从过往交互中归纳出可泛化的策略——在未知环境中的导航仍具挑战性。本文提出Robo-Cortex，一种自进化框架，使机器人能够通过持续反思-适应循环自主归纳导航启发式策略并优化认知策略。通过将成功模式与失败陷阱抽象为自然语言启发式规则，Robo-Cortex实现了从被动执行到主动策略演化的转变。其核心创新在于自主知识归纳机制，该机制将多模态轨迹蒸馏为结构化导航启发式知识库以实现知识泛化。架构进一步包含双粒度认知记忆系统：短期反思记忆用于实时局部进程分析，长期原则记忆则将历史轨迹抽象为可复用的指导原则与警示原则。为确保决策鲁棒性，我们引入多模态"想象-验证"循环，通过世界模型模拟潜在结果，并基于视觉语言模型的评估器验证行动方案。在IGNav、AR和AEQA上的广泛评估表明，Robo-Cortex在任务成功率和探索效率上均持续超越强基线方法，相较于最优先验方法SPL提升最高达+4.16%，在启发式策略迁移至未知环境时SPL提升最高达+15.30%。初步真实世界机器人实验进一步验证了Robo-Cortex在物理环境中的有效性。

---

### 2. ManiSoft: Towards Vision-Language Manipulation for Soft Continuum Robotics

- **作者**: Ziyu Wei, Luting Wang, Chen Gao, Li Wen, Si Liu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.18617v1)
- **发表日期**: 2026-05-18
- **匹配关键词**: obstacle avoidance
- **arXiv**: [2605.18617v1](http://arxiv.org/abs/2605.18617v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 大多数现有的视觉-语言操控研究针对刚性机械臂，其固定形态限制了在杂乱或狭窄空间中的适应性。软体机械臂因其可变形性成为一种有吸引力的替代方案，但面临本体感知不可靠和分布式底层驱动等挑战。为探究这些挑战，我们提出ManiSoft——一个面向软体机械臂的视觉-语言操控基准平台。ManiSoft配备定制化仿真器，通过弹性力约束将真实软体动力学与密集接触交互相结合。在此基础上，ManiSoft定义了四项任务，每项任务突出可变形控制的不同方面，从基础末端执行器协调到避障。为支持策略训练与评估，ManiSoft包含自动化流水线，可生成6,300个多样化场景及对应的专家轨迹。为大规模生成高质量轨迹，我们首先采用高层规划器将每项任务分解为一系列路径点序列，随后通过低层强化学习策略生成力矩指令以跟踪路径点。对三种代表性策略模型的基准测试显示，其在干净场景中表现相对良好，但在随机化条件下性能显著下降。可视化分析表明，失败主要源于对本体感知状态的视觉估计不准确，以及未能充分利用可变形性实现自适应避障。我们期望ManiSoft能成为连接刚性机械臂与软体机械臂在视觉-语言操控领域的重要测试平台。代码与数据集已发布于https://buaa-colalab.github.io/ManiSoft。

---

### 3. Not What You Asked For: Typographic Attacks in Household Robot Manipulation

- **作者**: Ali Iranmanesh, Peng Liu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.18593v1)
- **发表日期**: 2026-05-18
- **匹配关键词**: navigation
- **arXiv**: [2605.18593v1](http://arxiv.org/abs/2605.18593v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 开放词汇具身智能体日益依赖视觉-语言模型（如CLIP）进行物体感知与任务锚定。然而，这种灵活性所依赖的共享嵌入空间存在结构性漏洞，易受文字攻击——物理场景中的印刷文字会语义性地覆盖视觉判断。尽管先前研究已在静态二维基准测试和三维导航任务中量化了这一威胁，但其对家庭机器人操作完整"感知-规划-执行"流程的影响仍未被探索。

本研究基于HomeRobot基准在Habitat仿真环境中评估文字攻击。我们提出一种解耦感知架构，在通过DETIC保持几何锚定的同时，使冻结的CLIP编码器暴露于对抗性贴纸。在59个可归因情节的受控评估池中，该攻击在未进行感知优化、视角不受控且存在遮挡的条件下，整体攻击成功率（ASR）达67.8%，在完全成功的情节中升至70.0%。

关键发现是：感知错误会通过持久化三维语义地图传播，产生动力学失效——即由对抗性污染的语义状态驱动，导致机器人物理执行错误物体的抓取与搬运。在这些案例中，机器人实际抓取并运送错误物体至目标容器。这些结果证实，文字分类错误对模块化操作流程的安全性构成真实、可量化且具物理后果的威胁，而此前文字攻击研究对此尚未涉及。

---

### 4. When Fireflies Cluster; Enhancing Automatic Clustering via Centroid-Guided Firefly Optimization

- **作者**: MKA Ariyaratne, Azwirman Gusrialdi, Yury Nikulin, Jaakko Peltonen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.18460v1)
- **发表日期**: 2026-05-18
- **匹配关键词**: navigation
- **arXiv**: [2605.18460v1](http://arxiv.org/abs/2605.18460v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 本文提出了一种用于数据聚类的萤火虫算法（FA）新变体，旨在解决传统方法（如K-Means）在处理非均匀聚类形状、密度差异以及需预先指定聚类数量等方面的局限性。该算法引入了一种质心移动策略和一种多目标适应度函数，该函数平衡了紧凑性、分离性以及一种基于旅行商问题（TSP）的新型导航惩罚项。算法能够自动估计最优聚类数量，并动态调整聚类边界。将其应用于机器人传感器网络，凸显了其实用价值。实验结果表明，与K-Means相比，该算法提升了聚类质量，并缩短了簇内路径距离。这些结果证实了该算法在复杂空间聚类任务中的鲁棒性，并具备未来向高维及自适应场景扩展的潜力。

---

### 5. REACT: Environment-Adaptive Architecture for Continuous Formation Navigation of Wheeled Mobile Robots

- **作者**: Jianghong Dong, Yifeng Zhang, Jiawei Wang, Mengchi Cai, Keqiang Li, Guillaume Sartoretti
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.18441v1)
- **发表日期**: 2026-05-18
- **匹配关键词**: navigation
- **arXiv**: [2605.18441v1](http://arxiv.org/abs/2605.18441v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://dongjh20.github.io/REACT-website.
- **中文摘要**: 轮式移动机器人（WMRs）的编队控制因其在物流运输、环境监测、搜索救援等领域的广泛应用而受到广泛研究。然而，现有工作大多聚焦于跟踪预定义编队，这限制了其在复杂真实环境中的适应性。为此，我们提出REACT（实时环境自适应连续编队导航架构），这是一种融合集中式编队生成与分布式编队维护的分层架构。具体而言，上层模块在必要时生成适应环境的新编队，并采用我们提出的TCF-R2T（无轨迹冲突的机器人-目标分配）算法，在多项式时间内计算无冲突的WMR-目标分配，实现无轨迹冲突的编队及时切换。下层模块中，每个WMR执行我们开发的JSTP（联合时空轨迹规划）方法，通过同步优化空间位置与时间跨度来维持生成的编队，从而增强WMR间的协调性，使其能在障碍物密集环境和动态障碍场景中实现连续导航。仿真与真实实验均验证了REACT的有效性与实际应用价值。实验视频详见项目网站：https://dongjh20.github.io/REACT-website。

---

### 6. Towards Ubiquitous Mapping and Localization for Dynamic Indoor Environments

- **作者**: Halim Djerroud, Nico Steyn, Olivier Rabreau, Patrick Bonnin, Abderraouf Benali
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.18385v1)
- **发表日期**: 2026-05-18
- **匹配关键词**: navigation, human-robot interaction
- **arXiv**: [2605.18385v1](http://arxiv.org/abs/2605.18385v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出UbiSLAM，一种面向动态室内环境的实时建图与定位创新方案。通过在作业空间内策略性部署固定RGB-D相机网络，UbiSLAM解决了传统SLAM系统常见的局限性，例如对环境变化的敏感性以及对移动单元传感器的依赖。这种固定传感器方法实现了实时、全面的建图，提升了环境中运行机器人的定位精度与响应能力。UbiSLAM生成的集中式地图持续更新，为机器人提供精确的全局视图，从而改善导航性能、减少碰撞风险，并促进共享空间中更顺畅的人机交互。除优势外，UbiSLAM仍面临挑战，特别是在确保空间全覆盖与处理盲区方面，这需要整合机器人自身的数据。本文探讨了潜在解决方案，例如通过自动校准实现最优相机部署与朝向，以及增强实时数据共享的通信协议。该模型降低了单个机器人单元的计算负载，使复杂度较低的机器人平台也能有效运行，同时增强了整体系统的鲁棒性。

---

### 7. AtlasVA: Self-Evolving Visual Skill Memory for Teacher-Free VLM Agents

- **作者**: Pan Wang, Yihao Hu, Xiujin Liu, Jingchu Yang, Hang Wang, Zhihao Wen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.17933v1)
- **发表日期**: 2026-05-18
- **匹配关键词**: navigation
- **arXiv**: [2605.17933v1](http://arxiv.org/abs/2605.17933v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言模型（VLM）智能体日益依赖记忆增强强化学习来在长时域任务中复用经验，然而现有框架大多以文本形式存储记忆，并依赖专有教师模型进行总结或精炼。这种设计与空间决策任务存在根本性不匹配：几何先验被压缩为有损语言，稀疏交互往往通过延迟的文本反馈而非密集的视觉接地信号进行监督。我们认为，VLM智能体的可复用经验应保持视觉接地特性。基于这一洞察，我们提出\textbf{AtlasVA}——一种无教师视觉技能记忆框架，将记忆组织为三个互补层次：空间热力图、视觉范例和符号化文本技能。AtlasVA进一步直接从轨迹统计和轻量级网格启发式方法中演化出危险亲和图集，并将这些自演化图集作为基于势能的塑形奖励用于强化学习。这实现了感知、记忆与优化的统一，无需外部大语言模型监督。在\textsc{Sokoban}、\textsc{FrozenLake}、3D具身导航和3D机器人操作基准上的实验表明，AtlasVA持续优于以文本为中心的记忆基线和具有竞争力的VLM智能体，在空间密集型任务上尤其表现出显著优势。主页：https://wangpan-ustc.github.io/AtlasvaWeb

---

### 8. From a Single Demonstration to a General Policy for Contact-Rich Manipulation

- **作者**: Xing Li, Oliver Brock
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.17601v1)
- **发表日期**: 2026-05-17
- **匹配关键词**: contact-rich manipulation, exploration
- **arXiv**: [2605.17601v1](http://arxiv.org/abs/2605.17601v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出了一种基于示教学习（LfD）的框架，能够在多阶段、高接触性的操作任务中实现一次性泛化。该方法的核心在于利用环境约束作为归纳偏置。通过将示教过程表示为一系列利用环境约束的行为，机器人能够将任务通用结构（即约束类型及其转换）与实例特定细节（如精确的示教轨迹、姿态和局部几何形状）分离开来。我们的四阶段流程基于这一表示构建完整的策略：机器人首先将单次示教抽象为环境约束基元，然后通过自主探索消除歧义，接着吸收针对分布外变化的目标性人工修正，最后通过柔顺交互在线恢复被抽象化的细节。由于最终策略遵循约束而非模仿轨迹，它能够泛化到不同物体姿态、局部几何形状以及未建模的接触动力学。我们在七项真实世界多阶段高接触性操作任务中验证了该方法，成功率超过90%。这些广泛的实验结果确立了环境约束作为示教学习中高效泛化的基础构建模块。

---

### 9. Visual Sculpting: Visually-Aligned Planning Representations for Long-Horizon Robot Clay Sculpting

- **作者**: Peter Schaldenbrand, Jean Oh
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.17556v1)
- **发表日期**: 2026-05-17
- **匹配关键词**: object manipulation
- **arXiv**: [2605.17556v1](http://arxiv.org/abs/2605.17556v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 黏土雕塑是一项精细的艺术任务，需要灵巧的操作和长远的规划来实现高层次目标。作为机器人学问题，我们将黏土塑形定义为形状匹配挑战。先前的可变形物体操控研究要么需要针对每个目标重新训练策略，要么依赖将状态表示为稀疏点云的动力学模型，而这类模型难以充分捕捉黏土的纹理等重要特征。我们提出了一种方法，在视觉对齐的表征中建模可变形材料的动力学特性，并规划机器人雕塑动作，该表征能够捕捉光照和纹理特征。通过三种不同可变形材料及多种末端执行器的实验证明，我们的动力学模型性能与现有最优方法相当，且额外具备兼容视觉规划的优势。我们将动作表示为单个末端执行器对黏土的参数化推挤操作，实验表明该方法适用于长时域（超过100个动作）的黏土浮雕创作。最后，我们展示了在视觉对齐表征中进行规划的优势，同时通过分析揭示了相较于三维表征，该表征在规划中更具挑战性的原因。

---

### 10. MUSE: Multimodal Uncertainty Quantification of State Estimation

- **作者**: Minkyung Kim, Henry Che, Bhargav Chandaka, Bhumsitt Pramuanpornsatid, Chengyu Yang, Sheng Cheng, Xiaofeng Wang, Naira Hovakimyan, Shenlong Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.17421v1)
- **发表日期**: 2026-05-17
- **匹配关键词**: navigation, robot navigation
- **arXiv**: [2605.17421v1](http://arxiv.org/abs/2605.17421v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 精确的视觉状态估计一直是机器人学的核心课题，在机器人导航、自动驾驶和自主飞行等领域具有广泛应用。近年来机器人感知技术的进步显著提升了状态估计的准确性和鲁棒性，但如何量化与校准其精度（即对估计结果的置信度评估及故障检测能力）仍是一项根本性挑战。这一问题在视觉-惯性里程计（VIO）中尤为突出，其异方差性和多模态特性使得不确定性量化异常困难。本文提出MUSE（状态估计的多模态不确定性量化）——一种基于学习的实时框架，通过利用Mamba模型强大且高效的序列建模能力，从多异步传感器数据流中估计定位不确定性。在公开数据集与内部数据集上的实验表明，与现有不确定性量化方法相比，MUSE展现出更优的可靠性和鲁棒性，消融实验也验证了其关键设计选择的优势。

---

### 11. Beyond Geometry: Efficient Topologically-Grounded Navigation in Complex 3D Environments

- **作者**: Yifan Du, Chengwei Zhang, Siyu Liao, Zhongfeng Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.17302v1)
- **发表日期**: 2026-05-17
- **匹配关键词**: navigation, robot navigation
- **arXiv**: [2605.17302v1](http://arxiv.org/abs/2605.17302v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 地面机器人在复杂三维环境中的导航常受几何模糊性阻碍，例如家具等不可通行结构在局部几何特性上与可通行地面相似。此外，大规模体素空间的搜索计算成本仍是重大挑战。为解决这些问题，我们提出了一种表面提取框架，通过施加地面支撑、顶部净空和基于种子点的连通性约束，构建物理可达站立位置的简化状态空间。在五个Matterport3D室内场景和三个PCT基准场景上的评估表明，状态空间缩减超过80%，在Matterport3D场景上实现亚毫秒级A*搜索，且所有300个测试查询的规划成功率达100%。

---

