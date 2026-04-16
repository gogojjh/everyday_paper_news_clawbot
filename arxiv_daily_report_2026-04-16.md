# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-04-16 08:03

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 3/20 篇提供

**🌟 Highlight**: 10 篇 | **📌 Poster**: 10 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. Tree Learning: A Multi-Skill Continual Learning Framework for Humanoid Robots

- **作者**: Yifei Yan, Linqi Ye
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.12909v1)
- **发表日期**: 2026-04-14
- **匹配关键词**: navigation, autonomous navigation
- **arXiv**: [2604.12909v1](http://arxiv.org/abs/2604.12909v1)
- **📥 PDF**: 已下载至本地 (`2604.12909v1_Tree_Learning_A_Multi-Skill_Continual_Learning_Framework_for_Humanoid_Robots.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 随着人形机器人强化学习从单任务向多技能范式演进，如何在高效拓展新技能的同时避免灾难性遗忘，已成为具身智能领域的关键挑战。现有方法或依赖混合专家模型的复杂拓扑调整，或需训练超大规模模型，难以实现轻量化部署。为此，我们提出面向人形机器人的多技能持续学习框架——树状学习。该框架采用根-枝分层参数继承机制，通过参数复用为分支技能提供运动先验，从根本上防止灾难性遗忘；设计了融合相位调制与插值的多模态前馈适应机制，同时支持周期性与非周期性运动；并提出任务级奖励塑形策略以加速技能收敛。基于Unity的仿真实验表明：相较于同步多任务训练，树状学习在多种代表性运动技能中均获得更高奖励，同时保持100%技能留存率，可实现多技能无缝切换与实时交互控制。我们进一步在两类差异显著的Unity仿真任务中验证了树状学习的性能与泛化能力：受超级马里奥启发的交互场景，以及经典中式园林环境中的自主导航。

---

### 2. Robotic Manipulation is Vision-to-Geometry Mapping ($f(v) \rightarrow G$): Vision-Geometry Backbones over Language and Video Models

- **作者**: Zijian Song, Qichang Li, Jiawei Zhou, Zhenlong Yuan, Tianshui Chen, Liang Lin, Guangrun Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.12908v1)
- **发表日期**: 2026-04-14
- **匹配关键词**: VLA
- **arXiv**: [2604.12908v1](http://arxiv.org/abs/2604.12908v1)
- **📥 PDF**: 已下载至本地 (`2604.12908v1_Robotic_Manipulation_is_Vision-to-Geometry_Mapping_($f(v)_rightarrow_G$)_Vision-Geometry_Backbones_o.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 机器人操作的核心本质是视觉到几何的映射问题（$f(v) \rightarrow G$）。物理动作从根本上由三维位置与空间关系等几何属性定义。因此我们认为，可泛化机器人控制的基础应当是视觉-几何主干网络，而非当前广泛采用的视觉-语言或视频模型。传统的视觉语言模型与视频预测模型依赖于在大规模二维图文或时序像素数据上预训练的主干网络，虽然有效，但其表征主要受语义概念或二维先验信息塑造，本质上无法满足物理操作所需的精确三维几何特性。基于这一洞见，我们提出视觉-几何-动作模型，该模型直接在预训练的原生三维表征上构建动作生成机制。具体而言，VGA采用预训练的三维世界模型替代传统的语言或视频主干网络，建立起从视觉输入到物理动作的无缝视觉-几何映射。为增强几何一致性，我们进一步提出渐进式体素调制模块并采用联合训练策略。大量实验验证了本方法的有效性：在仿真基准测试中，VGA在包括$π_{0.5}$与GeoVLA在内的顶尖视觉语言模型基线上表现更优，展现出精确操作方面的卓越性能；更重要的是，在真实场景部署中，VGA对未见视角展现出显著的零样本泛化能力，持续超越$π_{0.5}$。这些结果表明，基于原生三维表征进行运算——而非通过语言或二维视频先验进行转换——是实现可泛化物理智能的极具前景的研究方向。

---

### 3. DeCoNav: Dialog enhanced Long-Horizon Collaborative Vision-Language Navigation

- **作者**: Sunyao Zhou, Yunzi Wu, Tianhang Wang, Xinhai Li, Guang Chen, Lizheng Liu, Chenjia Bai, Xuelong Li
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.12486v1)
- **发表日期**: 2026-04-14
- **匹配关键词**: navigation, VLN
- **arXiv**: [2604.12486v1](http://arxiv.org/abs/2604.12486v1)
- **📥 PDF**: 已下载至本地 (`2604.12486v1_DeCoNav_Dialog_enhanced_Long-Horizon_Collaborative_Vision-Language_Navigation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 长时程协作视觉语言导航（VLN）对多机器人系统完成超越单智能体能力的复杂任务至关重要。CoNavBench率先提出了首个包含接力式多机器人任务的协作长时程VLN基准，建立了协作分类体系，并采用图基生成与评估方法来建模共享环境中的交接与会合。然而，现有基准与评估方法通常未强制要求双机器人在共享世界时间线上严格同步推进，且多依赖静态协调策略，无法在出现跨智能体新证据时动态调整。本文提出对话增强型长时程协作视觉语言导航（DeCoNav），该去中心化框架将事件触发式对话与动态任务分配及重规划相结合，实现实时自适应协调。在DeCoNav中，机器人通过对话交换紧凑语义状态而无需中央控制器。当出现新证据、不确定性或冲突等关键事件时，系统触发对话机制，在同步执行过程中动态重新分配子目标并实施重规划。通过在DeCoNavBench中实现——涵盖176个HM3D场景的1,213项任务——DeCoNav将双机协同成功率（BSR）提升69.2%，证明了对话驱动、动态重分配规划对多机器人协作的有效性。

---

### 4. HazardArena: Evaluating Semantic Safety in Vision-Language-Action Models

- **作者**: Zixing Chen, Yifeng Gao, Li Wang, Yunhan Zhao, Yi Liu, Jiayu Li, Xiang Zheng, Zuxuan Wu, Cong Wang, Xingjun Ma, Yu-Gang Jiang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.12447v1)
- **发表日期**: 2026-04-14
- **匹配关键词**: vision-language-action, vision-language-action model, VLA
- **arXiv**: [2604.12447v1](http://arxiv.org/abs/2604.12447v1)
- **📥 PDF**: 已下载至本地 (`2604.12447v1_HazardArena_Evaluating_Semantic_Safety_in_Vision-Language-Action_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作模型继承了视觉-语言主干网络丰富的世界知识，并通过动作演示获得可执行技能。然而现有评估主要关注动作执行成功率，导致动作策略与视觉-语言语义的耦合度不足。这种脱节暴露了系统性漏洞——在语义风险下，正确的动作执行可能引发不安全后果。为揭示此漏洞，我们推出HazardArena基准测试，旨在受控但具风险的情境中评估VLA模型的语义安全性。该基准通过构建安全/不安全孪生场景实现，这些场景共享相同的物体、布局和动作要求，仅通过决定动作是否安全的语义语境进行区分。研究发现，仅在安全场景训练的VLA模型面对对应不安全场景时往往无法保持安全行为。HazardArena包含2000余个资产和40项风险敏感任务，涵盖基于成熟机器人安全标准的7个现实风险类别。为缓解此漏洞，我们提出无需训练的安全选项层，通过语义属性或视觉-语言裁判约束动作执行，在基本不影响任务性能的前提下显著减少不安全行为。我们希望HazardArena能促使学界重新思考VLA模型在迈向现实部署过程中，应如何评估和保障语义安全性。

---

### 5. ReefMapGS: Enabling Large-Scale Underwater Reconstruction by Closing the Loop Between Multimodal SLAM and Gaussian Splatting

- **作者**: Daniel Yang, Jungseok Hong, John J. Leonard, Yogesh Girdhar
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.11992v1)
- **发表日期**: 2026-04-13
- **匹配关键词**: 3D gaussian splatting, 3D reconstruction, gaussian splatting, 3d reconstruction
- **arXiv**: [2604.11992v1](http://arxiv.org/abs/2604.11992v1)
- **📥 PDF**: 已下载至本地 (`2604.11992v1_ReefMapGS_Enabling_Large-Scale_Underwater_Reconstruction_by_Closing_the_Loop_Between_Multimodal_SLAM.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 三维高斯泼溅是一种强大的视觉表示方法，能够实现高质量且高效的三维场景重建，但其关键依赖于通过运动恢复结构等计算密集型过程获取的精确相机位姿，这类方法不适用于野外机器人应用。然而在这些应用领域中，来自声学、惯性、压力及视觉传感器的多模态数据是可获取的，且适用于基于位姿图优化的SLAM方法——这类方法既能估计载体运动轨迹（即我们所需的相机位姿），同时还能提供不确定性度量。我们提出了一种基于3DGS的增量式重建框架ReefMapGS，该框架从高置信度区域构建初始模型，并逐步扩展至整合整个场景。我们通过交替执行新图像观测的局部跟踪与底层3DGS场景优化来实现场景的增量重建。优化后的位姿将反馈至位姿图中，以实现对整个轨迹的全局优化。我们在两个具有复杂几何结构的水下珊瑚礁场址中实现了无需COLMAP的三维重建，并在长达700米的勘测轨迹上为自主水下航行器提供了更精确的全局位姿估计。

---

### 6. StarVLA-$α$: Reducing Complexity in Vision-Language-Action Systems

- **作者**: Jinhui Ye, Ning Gao, Senqiao Yang, Jinliang Zheng, Zixuan Wang, Yuxin Chen, Pengguang Chen, Yilun Chen, Shu Liu, Jiaya Jia
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.11757v1)
- **发表日期**: 2026-04-13
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2604.11757v1](http://arxiv.org/abs/2604.11757v1)
- **📥 PDF**: 已下载至本地 (`2604.11757v1_StarVLA-$α$_Reducing_Complexity_in_Vision-Language-Action_Systems.pdf`)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/starVLA/starVLA.
- **中文摘要**: 视觉-语言-动作（VLA）模型近年来已成为构建通用机器人智能体的重要范式。然而，当前VLA领域仍呈现高度碎片化与复杂性：现有方法在架构设计、训练数据、具身配置以及面向特定基准的工程实现等方面存在显著差异。本研究提出StarVLA-$α$——一个简洁而强大的基线模型，旨在受控条件下系统研究VLA设计选择。该模型通过刻意简化架构与流程复杂度，减少实验干扰因素，实现可系统化分析的设计验证。具体而言，我们重新评估了动作建模策略、机器人专用预训练及交互界面工程等关键设计维度。通过在LIBERO、SimplerEnv、RoboTwin和RoboCasa四个基准上的统一多任务训练，这一简洁基线模型始终保持强大竞争力，表明仅需将强健的视觉语言模型主干与极简设计结合，即可在不依赖复杂架构或工程技巧的情况下实现优异性能。值得注意的是，我们的单一通用模型在公开真实世界基准RoboChallenge上以20%的优势超越$π_{0.5}$模型。我们期待StarVLA-$α$能为未来VLA领域研究提供坚实的起点。代码将在https://github.com/starVLA/starVLA发布。

---

### 7. LARY: A Latent Action Representation Yielding Benchmark for Generalizable Vision-to-Action Alignment

- **作者**: Dujun Nie, Fengjiao Chen, Qi Lv, Jun Kuang, Xiaoyu Li, Xuezhi Cao, Xunliang Cai
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.11689v1)
- **发表日期**: 2026-04-13
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2604.11689v1](http://arxiv.org/abs/2604.11689v1)
- **📥 PDF**: 已下载至本地 (`2604.11689v1_LARY_A_Latent_Action_Representation_Yielding_Benchmark_for_Generalizable_Vision-to-Action_Alignment.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 显性动作数据的匮乏限制了视觉-语言-动作（VLA）模型的发展，而人类动作视频则提供了可扩展但未标注的数据源。利用大规模人类视频数据集的关键挑战在于将视觉信号转化为独立于本体的表征，即潜在动作。然而，潜在动作表征从视觉观察中推导出稳健控制的能力尚未得到严格评估。我们提出了潜在动作表征生成（LARY）基准，这是一个用于评估潜在动作表征在高层语义动作（做什么）和低层机器人控制（如何做）方面的统一框架。该精心策划的数据集包含超过一百万段视频（1000小时），涵盖151个动作类别，以及62万张图像对和59.5万条运动轨迹，覆盖了多样化的实体和环境。我们的实验揭示了两个关键发现：（i）未经任何动作监督训练的通用视觉基础模型，始终优于专门的具身潜在动作模型。（ii）基于潜在表征的视觉空间在本质上比基于像素的空间更符合物理动作空间。这些结果表明，通用视觉表征固有地编码了物理控制所需的动作相关知识，并且语义层面的抽象是从视觉到动作的根本上更有效的途径，而非像素层面的重建。

---

### 8. AffordSim: A Scalable Data Generator and Benchmark for Affordance-Aware Robotic Manipulation

- **作者**: Mingyang Li, Haofan Xu, Haowen Sun, Xinzhe Chen, Sihua Ren, Liqi Huang, Xinyang Sui, Chenyang Miao, Qiongjie Cui, Zeyang Liu, Xingyu Chen, Xuguang Lan
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.11674v1)
- **发表日期**: 2026-04-13
- **匹配关键词**: diffusion policy, affordance
- **arXiv**: [2604.11674v1](http://arxiv.org/abs/2604.11674v1)
- **📥 PDF**: 已下载至本地 (`2604.11674v1_AffordSim_A_Scalable_Data_Generator_and_Benchmark_for_Affordance-Aware_Robotic_Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 基于仿真的数据生成已成为训练机器人操作策略的主流范式，但现有平台未将物体可供性信息纳入轨迹生成过程。这导致需要与特定功能区域进行精确交互的任务——如抓握杯柄、从杯沿倾倒或将杯子挂上挂钩——无法自动生成语义正确的轨迹。我们提出AffordSim，这是首个将开放词汇3D可供性预测集成到操作数据生成流程的仿真框架。AffordSim采用我们开发的VoxAfford模型（一种通过多尺度几何特征增强MLLM输出标记的开放词汇3D可供性检测器），在物体点云上预测可供性分布图，从而引导抓取姿态估计朝向任务相关的功能区域。该框架基于NVIDIA Isaac Sim构建，具备跨本体支持（Franka FR3、Panda、UR5e、Kinova）、VLM驱动的任务生成能力，以及通过基于DA3的实拍照片3D高斯重建实现的新型域随机化技术，能够自动化、规模化地生成可供性感知的操作数据。我们建立了涵盖7个类别（抓取、放置、堆叠、推/拉、倾倒、挂杯、长时程复合任务）共50项任务的基准测试集，并评估了4种模仿学习基线方法（BC、Diffusion Policy、ACT、Pi 0.5）。实验结果表明：虽然抓取任务已基本解决（成功率53-93%），但对可供性敏感的任务——如向窄口容器倾倒（成功率1-43%）和挂杯操作（成功率0-47%）——对当前模仿学习方法仍极具挑战，这凸显了可供性感知数据生成的必要性。在真实Franka FR3机器人上进行的零样本仿真到现实迁移实验，验证了生成数据的可迁移性。

---

### 9. DA-PTQ: Drift-Aware Post-Training Quantization for Efficient Vision-Language-Action Models

- **作者**: Siyuan Xu, Tianshi Wang, Fengling Li, Lei Zhu, Heng Tao Shen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.11572v1)
- **发表日期**: 2026-04-13
- **匹配关键词**: vision-language-action, vision-language-action model, VLA
- **arXiv**: [2604.11572v1](http://arxiv.org/abs/2604.11572v1)
- **📥 PDF**: 已下载至本地 (`2604.11572v1_DA-PTQ_Drift-Aware_Post-Training_Quantization_for_Efficient_Vision-Language-Action_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作模型（VLAs）在具身智能领域展现出巨大潜力，但其在资源受限机器人上的部署仍面临高内存与计算需求的挑战。后训练量化（PTQ）虽能提供高效解决方案，但直接应用于VLAs时往往导致序列控制中的性能严重下降。我们发现时间误差累积是关键因素——视觉语言到动作接口处的量化扰动会逐级放大，最终引发执行轨迹的运动学漂移。为解决该问题，我们提出漂移感知后训练量化方法（DA-PTQ），将量化问题构建为序列决策过程中的漂移感知优化问题。该方法包含两个核心组件：（1）跨空间表征补偿机制，通过缓解多模态表征与动作空间之间的结构化失真来提升动作一致性；（2）运动驱动的混合精度分配策略，依据最小化轨迹级运动误差的原则分配比特位宽。大量实验表明，DA-PTQ能显著降低运动学漂移，在低比特设置下达到与全精度模型相当的性能，为VLAs在资源受限机器人平台的实际部署提供了可行方案。

---

### 10. MR.ScaleMaster: Scale-Consistent Collaborative Mapping from Crowd-Sourced Monocular Videos

- **作者**: Hyoseok Ju, Giseop Kim
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.11372v2)
- **发表日期**: 2026-04-13
- **匹配关键词**: 3D reconstruction, 3d reconstruction
- **arXiv**: [2604.11372v2](http://arxiv.org/abs/2604.11372v2)
- **📥 PDF**: 已下载至本地 (`2604.11372v2_MR.ScaleMaster_Scale-Consistent_Collaborative_Mapping_from_Crowd-Sourced_Monocular_Videos.pdf`)
- **🔓 开源**: CODE
- **中文摘要**: 基于单目相机的众包协同建图技术有望在不依赖专业传感器的情况下实现可扩展的三维重建，但仍受限于两种尺度相关的失效模式：在重复环境中因误报回环检测导致的尺度突变崩溃，以及长轨迹上的渐进尺度漂移与单机器人尺度歧义问题，这些障碍阻碍了多会话数据的直接融合。我们提出\textbf{MR.ScaleMaster}系统，这是一个面向众包单目视频的协同建图系统，可同时解决上述两种失效模式。\textbf{MR.ScaleMaster}引入了三项核心机制：首先，尺度崩溃预警机制能在虚假回环破坏位姿图之前将其剔除；其次，通过Sim(3)锚节点框架将经典SE(3)框架泛化，显式估计各会话尺度，从而消除单机器人尺度歧义并保障全局尺度一致性；最后，采用模块化、开源、即插即用接口设计，使得任何单目重建模型无需修改后端即可集成。在包含多达15个智能体的KITTI序列测试中，Sim(3)框架相较于SE(3)基线实现了7.2倍的绝对轨迹误差降低，预警机制在保留所有有效约束的同时完全剔除了误报回环。我们进一步展示了异构多机器人稠密建图能力，成功将MASt3R-SLAM、pi3和VGGT-SLAM 2.0系统融合至统一地图中。

---

## 📌 Poster

*其他相关研究*

---

### 1. FastGrasp: Learning-based Whole-body Control method for Fast Dexterous Grasping with Mobile Manipulators

- **作者**: Heng Tao, Yiming Zhong, Zemin Yang, Yuexin Ma
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.12879v1)
- **发表日期**: 2026-04-14
- **匹配关键词**: dexterous grasping, mobile manipulator
- **arXiv**: [2604.12879v1](http://arxiv.org/abs/2604.12879v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 快速抓取对于物流、制造和服务应用中的移动机器人至关重要。现有方法受限于固定基座、简单夹爪或缓慢的触觉响应能力，在高速运动下的冲击稳定、实时全身协调以及跨不同物体与场景的泛化方面面临根本性挑战。我们提出\textbf{FastGrasp}——一种基于学习的框架，集成了抓取引导、全身控制和触觉反馈以实现移动快速抓取。我们的两阶段强化学习策略首先通过以物体点云为条件的变分自编码器生成多样化抓取候选方案，随后在最优抓取选择指导下执行移动基座、机械臂和手爪的协调运动。触觉感知支持实时抓取调整以应对冲击效应和物体变化。大量实验在仿真和真实场景中均展现出卓越的抓取性能，通过有效的仿真到现实迁移实现了跨不同几何形态物体的鲁棒操作。

---

### 2. Evolving the Complete Muscle: Efficient Morphology-Control Co-design for Musculoskeletal Locomotion

- **作者**: Lidong Sun, Wentao Zhao, Ye Wang, Huaping Liu, Fuchun Sun
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.12855v1)
- **发表日期**: 2026-04-14
- **匹配关键词**: exploration
- **arXiv**: [2604.12855v1](http://arxiv.org/abs/2604.12855v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 肌肉骨骼机器人凭借其固有的柔顺性与灵活性，为多场景运动提供了极具前景的范式。然而现有研究通常依赖固定肌肉生理参数的模型，这种静态物理设定难以适应复杂任务中多样化的动态需求，本质上限制了机器人的性能上限。本研究聚焦于肌肉骨骼系统的形态与控制协同设计，区别于以往仅优化刚度等单一生理属性的研究，我们提出了完整肌肉骨骼形态演化空间，同步进化肌肉力量、速度与刚度。为应对全面演化带来的探索空间指数级扩张，我们提出谱系设计进化框架——一种高效的协同优化方法。该框架通过融合双侧对称先验与主成分分析，将复杂肌肉参数映射至低维谱流形，实现高效的形态探索。在MyoSuite框架下对行走、爬梯、丘陵及崎岖地形四项任务进行评估，本方法相较于固定形态与标准进化基线，展现出更优的学习效率与运动稳定性。

---

### 3. Reliability-Guided Depth Fusion for Glare-Resilient Navigation Costmaps

- **作者**: Shang-En Tsai, Wei-Cheng Sun
- **单位**: Department of Computer Science and Information Engineering, Chang Jung Christian University; Department of Computer Science and Information Engineering, Chang Jung Christian University
- **发表日期**: 2026-04-14
- **匹配关键词**: navigation
- **arXiv**: [2604.12753v1](http://arxiv.org/abs/2604.12753v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 镜面反射光常导致反光地板与玻璃表面的RGB-D深度测量失真，产生空洞与尖峰噪声，这些误差在占据栅格代价地图中会累积形成持续的虚拟障碍物。本文提出一种基于显式深度可靠性建模的抗眩光代价地图构建方法。通过轻量级深度可靠性地图估计器预测镜面干扰下各像素点的测量可信度，并采用可靠性引导融合机制，在失真数据累积入地图前，依据该信号调节占据状态更新。在配备英特尔实感D435相机与Jetson Orin Nano平台的真实移动机器人实验中表明：该方法在真实反光地板与玻璃表面场景下，能显著减少虚假障碍物插入并提升自由空间保持能力，同时仅引入适度计算开销。研究结果表明，将眩光问题转化为测量可靠性问题，可为安全关键型室内环境中提升代价地图准确性与导航鲁棒性提供实用且轻量化的解决方案。

---

### 4. A hierarchical spatial-aware algorithm with efficient reinforcement learning for human-robot task planning and allocation in production

- **作者**: Jintao Xue, Xiao Li, Nianmin Zhang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.12669v1)
- **发表日期**: 2026-04-14
- **匹配关键词**: path planning
- **arXiv**: [2604.12669v1](http://arxiv.org/abs/2604.12669v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 在先进制造系统中，人与机器人协同完成生产流程。有效的任务规划与分配对实现高效生产至关重要，但在复杂动态的制造环境中仍面临挑战。人与机器人的动态特性，特别是需要考虑空间信息（如人员的实时位置及完成任务需移动的距离），使得任务规划与分配问题显著复杂化。为解决上述问题，我们将生产任务分解为可管理的子任务，并实现了一种实时分层人机任务规划与分配算法，包含负责任务规划的高层智能体与负责任务分配的低层智能体。针对高层智能体，我们提出了一种高效的基于缓冲区的深度Q学习方法，该方法能减少训练时间，并在具有长期稀疏奖励特性的生产问题中提升性能。对于低层智能体，我们设计了基于路径规划的空间感知方法，将任务分配给合适的人机资源，从而实现相应的顺序子任务。我们在三维模拟器中针对复杂实时生产过程进行了实验验证，结果表明所提出的EBQ&SAP方法能有效解决复杂动态生产过程中的人机任务规划与分配问题。

---

### 5. Scalable Trajectory Generation for Whole-Body Mobile Manipulation

- **作者**: Yida Niu, Xinhai Chang, Xin Liu, Ziyuan Jiao, Yixin Zhu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.12565v1)
- **发表日期**: 2026-04-14
- **匹配关键词**: mobile manipulation, articulated object
- **arXiv**: [2604.12565v1](http://arxiv.org/abs/2604.12565v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 部署在非结构化环境中的机器人必须协调全身运动——同时移动移动基座和机械臂——以与物理世界互动。这种移动性与灵巧性的结合产生了一个随场景和物体多样性呈组合增长的状态空间，所需的数据集远大于固定基座操作所需规模。然而现有的采集方法（包括遥操作和规划）要么劳动密集，要么在规模化时计算成本过高。核心瓶颈在于缺乏一个可扩展的流程，用于跨不同机器本体和环境生成大规模、物理有效的协调轨迹数据。本文提出AutoMoMa框架，该框架通过GPU加速将AKR建模（将基座、机械臂和物体运动学整合为单一运动链）与并行化轨迹优化相结合。AutoMoMa实现每GPU小时生成5000条轨迹（比基于CPU的基线快80倍以上），构建了包含超过50万条物理有效轨迹的数据集，涵盖330个场景、多样化关节物体及多种机器人本体。以往数据集不得不在规模、多样性或运动学保真度上做出妥协，而AutoMoMa能同时兼顾三者。下游模仿学习策略的训练进一步表明，即使是单个关节物体任务也需要数万条示范数据才能使前沿方法达到约80%的成功率，这证实数据稀缺（而非算法局限）才是关键制约因素。AutoMoMa由此连接了高性能规划与基于模仿学习的可靠控制，为协调移动操作研究提供了此前缺失的基础设施。通过实现大规模、运动学有效的训练数据生成，AutoMoMa展示了可泛化的全身机器人策略在真实世界多样化非结构化环境中的操作能力。

---

### 6. Whole-Body Mobile Manipulation using Offline Reinforcement Learning on Sub-optimal Controllers

- **作者**: Snehal Jauhri, Vignesh Prasad, Georgia Chalvatzaki
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.12509v1)
- **发表日期**: 2026-04-14
- **匹配关键词**: mobile manipulator, mobile manipulation, articulated object
- **arXiv**: [2604.12509v1](http://arxiv.org/abs/2604.12509v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 移动操作（MoMa）关节物体，如开门、开抽屉和开橱柜，需要机器人底座与手臂之间进行同步的全身协调。经典全身控制器（WBCs）可通过分层优化解决此类问题，但需要大量手动调优且仍显脆弱。相比之下，基于学习的方法展现出强大的泛化能力，但通常依赖昂贵的全身遥操作数据或复杂的奖励工程。我们观察到，即使是一个次优的WBC也能作为强大的结构化先验：它可用于在状态-动作空间的任务相关约束区域内收集数据，并且其行为仍可通过离线强化学习进一步优化。基于此，我们提出WHOLE-MoMa——一个两阶段流程：首先通过随机化轻量级WBC生成多样化演示数据，随后应用离线强化学习，通过奖励信号识别并整合改进行为。为支持复杂协调任务所需的表达性动作分块扩散策略，我们扩展了离线隐式Q学习，引入Q分块机制实现分块级评价器评估和优势加权策略提取。在使用仿真环境中的TIAGo++移动操作器进行的三个难度递增任务中，WHOLE-MoMa显著优于WBC、行为克隆及多种离线强化学习基线方法。策略无需微调即可直接迁移至真实机器人，在双手抽屉操作任务中达到80%成功率，在同步开橱柜与放置物体任务中达到68%成功率，且全程未使用任何遥操作或真实世界训练数据。

---

### 7. Designing for Error Recovery in Human-Robot Interaction

- **作者**: Christopher D. Wallbridge, Erwin Jose Lopez Pulgarin
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.12473v1)
- **发表日期**: 2026-04-14
- **匹配关键词**: human-robot interaction
- **arXiv**: [2604.12473v1](http://arxiv.org/abs/2604.12473v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 本立场文件简要探讨了当前机器人人工智能系统的编程方法。许多人工智能系统致力于将单一系统的性能提升至超越所谓人类基准的水平。然而，这些系统往往关注单次单向决策，而现实世界更具连续性与交互性。人类却常能从错误中恢复并汲取经验，从而达成更高的成功率。本文以核工业机器人手套箱为应用案例，探讨构建具备自主错误检测与恢复能力的系统所面临的挑战，并进一步阐述初步的基础设计方案。

---

### 8. Robotic Nanoparticle Synthesis via Solution-based Processes

- **作者**: Dasharadhan Mahalingam, Michael Gallagher, Nilanjan Chakraborty, Stanislaus S. Wong
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.12169v1)
- **发表日期**: 2026-04-14
- **匹配关键词**: motion planning
- **arXiv**: [2604.12169v1](http://arxiv.org/abs/2604.12169v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出了一种基于螺旋几何的机器人操作规划框架，用于实现溶液法合成的自动化，并以金和磁铁矿纳米颗粒的制备为例进行验证。合成方案本质上是长周期、多步骤的任务，需要拾取放置、倾倒、旋钮调节及周期性视觉检测反应完成度等技能。核心挑战在于某些技能（特别是倾倒、转移溶液容器和旋钮操作）对末端执行器的运动施加了几何与运动学约束。为此，我们采用示教编程范式，通过单次演示即可提取这些约束条件。这种螺旋运动表征与示教驱动规范相结合的方式，使得化学家等领域专家能够轻松调整系统以适应新的实验方案和实验室配置，无需具备机器人学或运动规划的专业知识。我们从演示中提取恒定螺旋序列，这种表示方法在保持坐标系不变性的同时，紧凑地编码了运动约束。该表征方式能够稳健地适应抓取位置的变化，并支持基于单次示例习得技能的参数化复用。通过按照合成方案组合这些螺旋参数化的基础动作，机器人能够自主生成运动规划，在重复实验中执行完整的实验流程。我们的研究结果表明，螺旋理论规划与示教编程相结合，为长周期实验室自动化提供了严谨且可推广的理论基础，从而使基础运动学能够在开发可扩展的溶液法合成方案中推动机器人技术的实际应用。

---

### 9. Human-Inspired Context-Selective Multimodal Memory for Social Robots

- **作者**: Hangyeol Kang, Slava Voloshynovskiy, Nadia Magnenat Thalmann
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.12081v1)
- **发表日期**: 2026-04-13
- **匹配关键词**: human-robot interaction
- **arXiv**: [2604.12081v1](http://arxiv.org/abs/2604.12081v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 记忆是社会互动的基础，它使人类能够回忆有意义的历史经历，并根据情境调整自身行为。然而，当前大多数社交机器人与具身智能体依赖非选择性的文本记忆，限制了其支持个性化、情境感知交互的能力。受认知神经科学启发，我们为社交机器人提出了一种情境选择性多模态记忆架构，该架构能够捕获并检索文本与视觉情景痕迹，优先存储具有高情感显著性或场景新颖性的时刻。通过将这些记忆与个体用户关联，我们的系统实现了社交个性化回忆及更自然、更接地气的对话。我们使用精选的社会场景数据集对选择性存储机制进行评估，获得了0.506的斯皮尔曼相关系数，超越了人类一致性水平（ρ=0.415），并优于现有图像记忆性模型。在多模态检索实验中，我们的融合方法将Recall@1指标最高提升了13%，显著优于单模态文本或图像检索。实时性评估证实系统能够保持实时性能。定性分析进一步表明，相较于基线模型，该框架能生成更丰富且更具社交相关性的回应。本研究通过融合人类启发的选择性与多模态检索机制，推动了社交机器人记忆设计的进步，从而增强了长期个性化人机交互体验。

---

### 10. M2HRI: An LLM-Driven Multimodal Multi-Agent Framework for Personalized Human-Robot Interaction

- **作者**: Shaid Hasan, Breenice Lee, Sujan Sarker, Tariq Iqbal
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.11975v1)
- **发表日期**: 2026-04-13
- **匹配关键词**: HRI, human-robot interaction
- **arXiv**: [2604.11975v1](http://arxiv.org/abs/2604.11975v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://project-m2hri.github.io/.
- **中文摘要**: 多机器人系统在家庭和医院等社会环境中展现出巨大潜力，但现有研究通常将机器人视为功能相同的个体，忽视了机器人个体身份如何影响用户感知，以及在存在个体差异时协调机制如何塑造多机器人行为。为此，我们提出了M2HRI——一个基于大语言模型的多模态多智能体框架，该框架为每个机器人配备独特的个性特征与长期记忆系统，并建立了基于个体差异的协调机制。通过在多智能体人机交互场景中开展的受控用户研究（样本量n=105），我们发现：大语言模型驱动的个性特征具有显著区分度并能提升交互质量，长期记忆系统增强了个性化服务与偏好感知能力，集中式协调机制在显著减少任务重叠的同时提升了整体交互质量。这些结果表明，智能体个体特性与结构化协调机制对于实现连贯且符合社会规范的多智能体人机交互至关重要。项目网站与代码详见https://project-m2hri.github.io/。

---

