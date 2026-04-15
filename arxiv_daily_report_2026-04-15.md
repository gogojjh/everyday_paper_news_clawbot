# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-04-15 08:04

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 3/20 篇提供

**🌟 Highlight**: 15 篇 | **📌 Poster**: 5 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. StarVLA-$α$: Reducing Complexity in Vision-Language-Action Systems

- **作者**: Jinhui Ye, Ning Gao, Senqiao Yang, Jinliang Zheng, Zixuan Wang, Yuxin Chen, Pengguang Chen, Yilun Chen, Shu Liu, Jiaya Jia
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.11757v1)
- **发表日期**: 2026-04-13
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2604.11757v1](http://arxiv.org/abs/2604.11757v1)
- **📥 PDF**: 已下载至本地 (`2604.11757v1_StarVLA-$α$_Reducing_Complexity_in_Vision-Language-Action_Systems.pdf`)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/starVLA/starVLA.
- **中文摘要**: 视觉-语言-动作（VLA）模型近年来已成为构建通用机器人智能体的重要范式。然而，当前VLA领域仍呈现高度碎片化与复杂性：现有方法在架构设计、训练数据、具身配置以及面向特定基准的工程实现等方面存在显著差异。本研究提出StarVLA-$α$——一个简洁而强大的基线模型，旨在受控条件下系统研究VLA设计选择。该模型通过刻意简化架构与流程复杂度，减少实验干扰因素，实现可系统化分析的设计验证。具体而言，我们重新评估了动作建模策略、机器人专用预训练及交互界面工程等关键设计维度。在LIBERO、SimplerEnv、RoboTwin和RoboCasa四个基准的统一训练框架下，这一简洁基线模型始终展现出强大竞争力，表明结合极简设计的强视觉语言模型主干已足以实现优异性能，无需依赖额外架构复杂度或工程技巧。值得注意的是，我们的单一通用模型在公开真实世界基准RoboChallenge上以20%优势超越$π_{0.5}$模型。我们期待StarVLA-$α$能为VLA领域的后续研究提供坚实基础。代码将在https://github.com/starVLA/starVLA发布。

---

### 2. LARY: A Latent Action Representation Yielding Benchmark for Generalizable Vision-to-Action Alignment

- **作者**: Dujun Nie, Fengjiao Chen, Qi Lv, Jun Kuang, Xiaoyu Li, Xuezhi Cao, Xunliang Cai
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.11689v1)
- **发表日期**: 2026-04-13
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2604.11689v1](http://arxiv.org/abs/2604.11689v1)
- **📥 PDF**: 已下载至本地 (`2604.11689v1_LARY_A_Latent_Action_Representation_Yielding_Benchmark_for_Generalizable_Vision-to-Action_Alignment.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 显性动作数据的匮乏限制了视觉-语言-动作（VLA）模型的发展，而人类动作视频则提供了可扩展但未标注的数据源。利用大规模人类视频数据集的关键挑战在于将视觉信号转化为独立于本体论的表示形式，即潜在动作。然而，潜在动作表示从视觉观察中推导出稳健控制的能力尚未得到严格评估。我们提出了潜在动作表示生成（LARY）基准，这是一个用于评估潜在动作表示在高层语义动作（做什么）和低层机器人控制（如何做）方面的统一框架。该精心策划的数据集包含超过一百万段视频（1000小时），涵盖151个动作类别，以及62万张图像对和59.5万条运动轨迹，覆盖了多样化的实体和环境。我们的实验揭示了两个关键发现：（i）未经任何动作监督训练的一般视觉基础模型，始终优于专门的具身潜在动作模型。（ii）基于潜在表示的视觉空间在本质上比基于像素的空间更符合物理动作空间。这些结果表明，一般视觉表示内在地编码了物理控制所需的动作相关知识，并且语义层面的抽象是从视觉到动作的根本上更有效的途径，而非像素层面的重建。

---

### 3. AffordSim: A Scalable Data Generator and Benchmark for Affordance-Aware Robotic Manipulation

- **作者**: Mingyang Li, Haofan Xu, Haowen Sun, Xinzhe Chen, Sihua Ren, Liqi Huang, Xinyang Sui, Chenyang Miao, Qiongjie Cui, Zeyang Liu, Xingyu Chen, Xuguang Lan
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.11674v1)
- **发表日期**: 2026-04-13
- **匹配关键词**: diffusion policy, affordance
- **arXiv**: [2604.11674v1](http://arxiv.org/abs/2604.11674v1)
- **📥 PDF**: 已下载至本地 (`2604.11674v1_AffordSim_A_Scalable_Data_Generator_and_Benchmark_for_Affordance-Aware_Robotic_Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 基于仿真的数据生成已成为训练机器人操作策略的主流范式，但现有平台未将物体可供性信息纳入轨迹生成过程。这导致需要与特定功能区域精确交互的任务——如抓握杯柄、从杯缘倾倒或将杯子挂上挂钩——无法自动生成语义正确的轨迹。我们提出AffordSim，首个将开放词汇3D可供性预测集成到操作数据生成流程的仿真框架。AffordSim采用我们开发的VoxAfford模型（一种通过多尺度几何特征增强MLLM输出标记的开放词汇3D可供性检测器），在物体点云上预测可供性图谱，从而引导抓取姿态估计朝向任务相关的功能区域。该框架基于NVIDIA Isaac Sim构建，具备跨本体支持（Franka FR3、Panda、UR5e、Kinova）、VLM驱动的任务生成能力，以及通过基于DA3的真实照片3D高斯重建实现的新型域随机化技术，能够自动化、规模化地生成可供性感知的操作数据。我们建立了涵盖7个类别（抓取、放置、堆叠、推/拉、倾倒、挂杯、长时程复合任务）共50项任务的基准测试集，并评估了4种模仿学习基线方法（BC、Diffusion Policy、ACT、Pi 0.5）。实验结果表明：虽然抓取任务已基本解决（成功率53-93%），但对于当前模仿学习方法而言，需要可供性感知的任务——如向窄口容器倾倒（成功率1-43%）和挂杯任务（成功率0-47%）——仍然极具挑战性，这凸显了可供性感知数据生成的必要性。在真实Franka FR3机器人上进行的零样本仿真到现实迁移实验，验证了生成数据的可迁移性。

---

### 4. DA-PTQ: Drift-Aware Post-Training Quantization for Efficient Vision-Language-Action Models

- **作者**: Siyuan Xu, Tianshi Wang, Fengling Li, Lei Zhu, Heng Tao Shen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.11572v1)
- **发表日期**: 2026-04-13
- **匹配关键词**: vision-language-action model, VLA, vision-language-action
- **arXiv**: [2604.11572v1](http://arxiv.org/abs/2604.11572v1)
- **📥 PDF**: 已下载至本地 (`2604.11572v1_DA-PTQ_Drift-Aware_Post-Training_Quantization_for_Efficient_Vision-Language-Action_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作模型（VLAs）在具身智能领域展现出巨大潜力，但其高内存与计算需求使其在资源受限机器人上的部署面临挑战。后训练量化（PTQ）虽能提供高效解决方案，但直接应用于VLAs时往往导致序列控制中的性能严重下降。我们发现时间误差累积是关键因素——视觉语言到动作接口处的量化扰动会逐级放大，最终引发执行轨迹的运动学漂移。为此，我们提出漂移感知后训练量化（DA-PTQ），将量化问题构建为序列决策过程中的漂移感知优化任务。该方法包含两个核心组件：（1）跨空间表征补偿机制，通过缓解多模态表征与动作空间之间的结构化失真来提升动作一致性；（2）运动驱动的混合精度分配策略，依据最小化轨迹级运动误差的原则动态分配比特位宽。大量实验表明，DA-PTQ能显著降低运动学漂移，在低比特设置下达到与全精度模型相当的性能，为VLAs在资源受限机器人平台的实际部署提供了可行方案。

---

### 5. MR.ScaleMaster: Scale-Consistent Collaborative Mapping from Crowd-Sourced Monocular Videos

- **作者**: Hyoseok Ju, Giseop Kim
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.11372v1)
- **发表日期**: 2026-04-13
- **匹配关键词**: 3D reconstruction, 3d reconstruction
- **arXiv**: [2604.11372v1](http://arxiv.org/abs/2604.11372v1)
- **📥 PDF**: 已下载至本地 (`2604.11372v1_MR.ScaleMaster_Scale-Consistent_Collaborative_Mapping_from_Crowd-Sourced_Monocular_Videos.pdf`)
- **🔓 开源**: CODE
- **中文摘要**: 基于单目相机的众包协同建图技术有望实现无需专用传感器的可扩展三维重建，但其发展仍受限于两种尺度相关的失效模式：在重复环境中因误报回环检测导致的尺度突变崩溃，以及长轨迹上的渐进尺度漂移与单机器人尺度歧义性阻碍多会话数据直接融合。我们提出MR.ScaleMaster系统，专门针对众包单目视频的协同建图任务解决这两类失效问题。该系统包含三项核心机制：首先，尺度崩溃预警机制可在虚假回环污染位姿图前将其剔除；其次，通过Sim(3)锚节点框架将经典SE(3)体系扩展为显式估计会话级尺度参数，从而消除单机器人尺度歧义并保障全局尺度一致性；最后，模块化开源即插即用接口支持任意单目重建模型无需修改后端即可集成。在包含多达15个智能体的KITTI数据集测试中，Sim(3)框架相较于SE(3)基线实现了7.2倍的绝对轨迹误差降低，预警机制在保留所有有效约束的同时完全剔除了误报回环。我们进一步演示了在统一地图中融合MASt3R-SLAM、pi3和VGGT-SLAM 2.0的异构多机器人稠密建图能力。

---

### 6. Learning to Forget -- Hierarchical Episodic Memory for Lifelong Robot Deployment

- **作者**: Leonard Bärmann, Joana Plewnia, Alex Waibel, Tamim Asfour
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.11306v1)
- **发表日期**: 2026-04-13
- **匹配关键词**: human-robot collaboration
- **arXiv**: [2604.11306v1](http://arxiv.org/abs/2604.11306v1)
- **📥 PDF**: 已下载至本地 (`2604.11306v1_Learning_to_Forget_--_Hierarchical_Episodic_Memory_for_Lifelong_Robot_Deployment.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 当用户询问"你把我的钥匙放哪儿了？"或"任务为何失败？"时，机器人需要能够描述过往经历。然而，通过持续多模态感知建立终身情景记忆（EM）会迅速超出存储限制，导致实时查询难以实现，这要求系统必须根据用户相关性的概念进行选择性遗忘。我们提出H$^2$-EMV框架，使人形机器人能够通过用户交互学习记忆策略。该方法通过三个核心机制实现：增量构建分层情景记忆系统，基于语言模型的相关性评估进行选择性遗忘（评估条件为习得的自然语言规则），并根据用户对遗忘细节的反馈动态更新规则。在模拟家务任务和ARMAR-7机器人20.5小时真实场景记录的测试中，H$^2$-EMV在保持问答准确率的同时，将内存占用降低45%，查询计算量减少35%。尤为关键的是，系统性能随时间持续提升——通过适应用户特定优先级，第二轮查询准确率提高70%。这表明习得性遗忘机制能为长期人机协作提供可扩展、个性化的情景记忆系统。

---

### 7. Ψ-Map: Panoptic Surface Integrated Mapping Enables Real2Sim Transfer

- **作者**: Xuan Yu, Yuxuan Xie, Changjian Jiang, Shichao Zhai, Rong Xiong, Yu Zhang, Yue Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.10982v1)
- **发表日期**: 2026-04-13
- **匹配关键词**: 3D gaussian splatting, gaussian splatting
- **arXiv**: [2604.10982v1](http://arxiv.org/abs/2604.10982v1)
- **📥 PDF**: 已下载至本地 (`2604.10982v1_Ψ-Map_Panoptic_Surface_Integrated_Mapping_Enables_Real2Sim_Transfer.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 开放词汇全景重建对于高级机器人感知与仿真至关重要。然而，现有基于3D高斯泼溅（3DGS）的方法在大规模场景中往往难以同时实现几何精度、连贯的全景理解与实时推理频率。本文提出一个融合几何增强、端到端全景学习与高效渲染的综合框架。首先，为确保大规模环境中的物理真实感，我们利用激光雷达数据构建平面约束的多模态高斯混合模型（GMM），并采用2D高斯面元作为地图表示，实现高精度表面对齐与连续几何监督。在此基础上，为克服传统多阶段全景分割流程中固有的误差累积与跨帧关联繁琐问题，我们设计了查询引导的端到端学习架构。通过在视锥体内采用局部交叉注意力机制，系统将2D掩码特征直接提升至3D空间，实现全局一致的全景理解。最后，针对高维语义特征引发的计算瓶颈，我们引入精确图块相交与Top-K硬选择策略以优化渲染管线。实验结果表明，本系统在大规模场景中实现了卓越的几何与全景重建质量，同时保持超过40 FPS的推理速率，满足机器人控制回路的实时性需求。

---

### 8. Fast-SegSim: Real-Time Open-Vocabulary Segmentation for Robotics in Simulation

- **作者**: Xuan Yu, Yuxuan Xie, Shichao Zhai, Shuhao Ye, Rong Xiong, Yue Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.10951v1)
- **发表日期**: 2026-04-13
- **匹配关键词**: 3d reconstruction, 3D reconstruction, gaussian splatting, navigation, nerf
- **arXiv**: [2604.10951v1](http://arxiv.org/abs/2604.10951v1)
- **📥 PDF**: 已下载至本地 (`2604.10951v1_Fast-SegSim_Real-Time_Open-Vocabulary_Segmentation_for_Robotics_in_Simulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 开放词汇全景重建对于高级机器人技术和仿真至关重要。然而，现有的三维重建方法（如神经辐射场或其高斯溅射变体）往往难以达到机器人控制回路所需的实时推理频率。现有方法在处理鲁棒性开放词汇分割所需的高维特征时会产生极高的延迟。我们提出Fast-SegSim——一个基于二维高斯溅射构建的全新、简洁、端到端框架，旨在实现实时、高保真且三维一致的开放词汇分割重建。我们的核心贡献在于高度优化的渲染管线，专门针对高通道分割特征累积的计算瓶颈。我们引入两项关键优化：通过精确图块相交减少光栅化冗余，以及创新的Top-K硬选择策略。该策略利用二维高斯表示固有的几何稀疏性，大幅简化特征累积过程并缓解带宽限制，实现超过40帧/秒的渲染速率。Fast-SegSim在机器人应用中具有关键价值：既可作为Gazebo等仿真平台的高频传感器输入，其三维一致性输出又能为下游感知任务微调提供必需的多视角“真实标注”。我们通过使用生成标注微调目标导向导航中的感知模块验证其实用性，成功将导航成功率提升一倍。卓越的渲染速度与实际效用彰显了Fast-SegSim在弥合仿真与现实差距方面的巨大潜力。

---

### 9. WARPED: Wrist-Aligned Rendering for Robot Policy Learning from Egocentric Human Demonstrations

- **作者**: Harry Freeman, Chung Hee Kim, George Kantor
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.10809v1)
- **发表日期**: 2026-04-12
- **匹配关键词**: gaussian splatting
- **arXiv**: [2604.10809v1](http://arxiv.org/abs/2604.10809v1)
- **📥 PDF**: 已下载至本地 (`2604.10809v1_WARPED_Wrist-Aligned_Rendering_for_Robot_Policy_Learning_from_Egocentric_Human_Demonstrations.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 近期，从人类演示中学习的研究进展为解决训练鲁棒视觉运动策略所需的数据收集可扩展性和高成本问题带来了希望。然而，现有方法通常受限于对多视角相机设置、深度传感器或定制硬件的依赖，且大多局限于从第三人称或第一人称视角相机执行策略。本文提出WARPED框架，该框架旨在从人类演示视频中合成逼真的腕部视角观测数据，从而仅使用单目RGB数据即可促进视觉运动策略的训练。通过从第一人称RGB相机收集数据，我们的系统利用视觉基础模型初始化交互场景，随后采用手-物交互流程追踪手部与被操作物体，并将轨迹重定向至机器人末端执行器。最后，通过高斯泼溅技术合成具有照片级真实感的腕部视角观测数据，直接用于训练机器人策略。实验表明，在五项桌面操作任务中，WARPED框架的成功率与基于遥操作演示数据训练的策略相当，同时数据收集时间减少了5-8倍。

---

### 10. OmniUMI: Towards Physically Grounded Robot Learning via Human-Aligned Multimodal Interaction

- **作者**: Shaqi Luo, Yuanyuan Li, Youhao Hu, Chenhao Yu, Chaoran Xu, Jiachen Zhang, Guocai Yao, Tiejun Huang, Ran He, Zhongyuan Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.10647v1)
- **发表日期**: 2026-04-12
- **匹配关键词**: contact-rich manipulation, diffusion policy
- **arXiv**: [2604.10647v1](http://arxiv.org/abs/2604.10647v1)
- **📥 PDF**: 已下载至本地 (`2604.10647v1_OmniUMI_Towards_Physically_Grounded_Robot_Learning_via_Human-Aligned_Multimodal_Interaction.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: UMI风格接口能够实现可扩展的机器人学习，但现有系统主要停留在视觉运动层面，依赖RGB观测与轨迹数据，仅提供有限的物理交互信号接入。这在接触密集型操作任务中形成根本性限制——此类任务的成功依赖于触觉交互、内部抓握力及外部交互力矩等难以仅凭视觉推断的接触动力学特征。我们提出OmniUMI框架，通过人类对齐的多模态交互实现物理实体化的机器人学习。该系统在紧凑的手持装置中同步采集RGB图像、深度信息、运动轨迹、触觉传感、内部抓握力与外部交互力矩数据，并通过共享实体化设计保持采集与部署的一致性。为支持人类对齐的示教过程，OmniUMI通过双边夹爪力反馈与手持实体中对外部交互力矩的自然感知实现双重力反馈机制。基于此接口，我们扩展了扩散策略模型以融合视觉、触觉及力相关观测，并通过基于阻抗控制的执行系统部署学习策略，实现对运动与接触行为的统一调控。实验验证了该系统在力敏感抓放、交互式表面擦除及触觉引导的选择性释放任务中具备可靠的传感能力与优异的下游性能。总体而言，OmniUMI将物理实体化的多模态数据采集与人类对齐的交互方式相结合，为学习接触密集型操作任务提供了可扩展的基础架构。

---

### 11. PRoID: Predicted Rate of Information Delivery in Multi-Robot Exploration and Relaying

- **作者**: Seungchan Kim, Seungjae Baek, Micah Corah, Graeme Best, Brady Moon, Sebastian Scherer ⭐
  - **高亮作者**: Sebastian Scherer
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.10433v1)
- **发表日期**: 2026-04-12
- **匹配关键词**: exploration
- **arXiv**: [2604.10433v1](http://arxiv.org/abs/2604.10433v1)
- **📥 PDF**: 已下载至本地 (`2604.10433v1_PRoID_Predicted_Rate_of_Information_Delivery_in_Multi-Robot_Exploration_and_Relaying.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 本文研究多机器人探索与中继问题：一组机器人需在任务时限内探索未知环境，并将获取的信息传输至固定基站。核心挑战在于确定每个机器人何时应停止探索并开始中继——这取决于机器人前方可能发现的未知信息、其独有的数据储备，以及即时传输与未来传输的价值权衡。现有方法要么完全忽略信息回传要求，要么依赖固定时序的中继策略，无法适应环境结构、团队构成或任务进展的动态变化。我们提出PRoID（信息传输预测速率）中继准则，该准则通过已学习的地图预测模型，结合队友当前中继状态，估算每个机器人沿规划路径的未来信息获取量。当即时返回能产生更高的单位时间信息传输量时，PRoID将触发中继行为。我们进一步提出PRoID-Safe扩展方案，该方案将机器人存活概率纳入中继决策准则，随着故障风险增加，系统会自然倾向于提前启动中继。通过在真实室内平面图数据集上的实验验证，PRoID与PRoID-Safe均优于固定时序基准方法，且在故障场景中表现出更强的相对性能优势。

---

### 12. AnySlot: Goal-Conditioned Vision-Language-Action Policies for Zero-Shot Slot-Level Placement

- **作者**: Zhaofeng Hu, Sifan Zhou, Qinbo Zhang, Rongtao Xu, Qi Su, Ci-Jyun Liang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.10432v1)
- **发表日期**: 2026-04-12
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2604.10432v1](http://arxiv.org/abs/2604.10432v1)
- **📥 PDF**: 已下载至本地 (`2604.10432v1_AnySlot_Goal-Conditioned_Vision-Language-Action_Policies_for_Zero-Shot_Slot-Level_Placement.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作策略已成为通用机器人操作的多功能范式。然而，在组合式语言指令下实现精确物体放置仍是现代单体VLA策略面临的主要挑战。插槽级任务既需要可靠的插槽定位，又要求亚厘米级的执行精度。为此，我们提出AnySlot框架，通过引入显式空间视觉目标作为语言定位与控制之间的中间表征，有效降低组合复杂度。AnySlot通过生成场景标记将语言转化为显式视觉目标，随后通过目标条件化VLA策略执行该目标。这种分层设计有效解耦了高层插槽选择与底层执行，确保语义准确性与空间鲁棒性。此外，针对现有基准测试在精度要求任务上的缺失，我们推出SlotBench——一个包含九类任务的综合仿真基准，专门用于评估插槽级放置中的结构化空间推理能力。大量实验表明，在零样本插槽级放置任务中，AnySlot显著优于平面VLA基线及先前的模块化定位方法。

---

### 13. SyncFix: Fixing 3D Reconstructions via Multi-View Synchronization

- **作者**: Deming Li, Abhay Yadav, Cheng Peng, Rama Chellappa, Anand Bhattad
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.11797v1)
- **发表日期**: 2026-04-13
- **匹配关键词**: 3D reconstruction, 3d reconstruction
- **arXiv**: [2604.11797v1](http://arxiv.org/abs/2604.11797v1)
- **📥 PDF**: 已下载至本地 (`2604.11797v1_SyncFix_Fixing_3D_Reconstructions_via_Multi-View_Synchronization.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出SyncFix框架，该框架在基于扩散模型的重建场景优化过程中强制执行跨视角一致性。SyncFix将优化过程构建为联合潜在桥匹配问题，通过同步多视角间的失真与洁净表征来修复语义和几何不一致性。这意味着SyncFix学习多视角的联合条件分布，从而在整个去噪轨迹中保持一致性。我们的训练仅需图像对数据，但在推理阶段能自然泛化至任意数量的视角。此外，重建质量随视角增加而提升，但在高视角数量时呈现收益递减趋势。定性与定量实验表明，即使在没有洁净参考图像的情况下，SyncFix仍能持续生成高质量重建结果，并超越当前最先进的基线方法。当可获得稀疏参考图像时，SyncFix能实现更高保真度的重建。

---

### 14. Grounded World Model for Semantically Generalizable Planning

- **作者**: Quanyi Li, Lan Feng, Haonan Zhang, Wuyang Li, Letian Wang, Alexandre Alahi, Harold Soh
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.11751v1)
- **发表日期**: 2026-04-13
- **匹配关键词**: VLA
- **arXiv**: [2604.11751v1](http://arxiv.org/abs/2604.11751v1)
- **📥 PDF**: 已下载至本地 (`2604.11751v1_Grounded_World_Model_for_Semantically_Generalizable_Planning.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 在模型预测控制（MPC）中，世界模型通过预测不同行动方案的未来结果，并对其进行评分以指导最优行动的选择。对于视觉运动MPC，评分函数基于预测图像与目标图像在预训练视觉编码器（如DINO和JEPA）潜在空间中的距离度量。然而，在执行任务前获取目标图像具有挑战性，尤其是在新环境中。此外，与自然语言相比，通过图像传达目标的方式交互性有限。本研究提出在视觉-语言对齐的潜在空间中学习一个接地世界模型（GWM）。通过该方法，每个行动方案的评分取决于其未来结果与任务指令的接近程度，具体通过嵌入向量的相似性来体现。这一方法将视觉运动MPC转化为视觉语言对齐模型（VLA），其在语义泛化能力上超越了基于视觉语言模型（VLM）的VLA。在提出的WISER基准测试中，GWM-MPC在包含288个任务的测试集上取得了87%的成功率，这些任务具有未见过的视觉信号和指代表达，但仍可通过训练中演示的动作解决。相比之下，传统VLA虽然在训练集上以90%的成功率过拟合，但在测试集上的平均成功率仅为22%。

---

### 15. Unfolding 3D Gaussian Splatting via Iterative Gaussian Synopsis

- **作者**: Yuqin Lu, Yang Zhou, Yihua Dai, Guiqing Li, Shengfeng He
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.11685v1)
- **发表日期**: 2026-04-13
- **匹配关键词**: 3D gaussian splatting, gaussian splatting
- **arXiv**: [2604.11685v1](http://arxiv.org/abs/2604.11685v1)
- **📥 PDF**: 已下载至本地 (`2604.11685v1_Unfolding_3D_Gaussian_Splatting_via_Iterative_Gaussian_Synopsis.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 3D高斯泼溅（3DGS）已成为实时高保真新视角合成的先进框架。然而，其巨大的存储需求与固有的非结构化表示对在流式传输和资源受限环境中的部署提出了挑战。现有的细节层次（LOD）策略，特别是基于自底向上构建的方法，常引入冗余或导致保真度下降。为克服这些限制，我们提出迭代高斯摘要——一种通过自顶向下“展开”方案实现紧凑渐进式渲染的新框架。该方法从全分辨率3DGS模型出发，通过自适应可学习的掩码剪枝机制迭代生成更粗糙的LOD层级，构建出在保持视觉质量的同时提升效率的多级层次结构。我们整合了捕获全局场景结构的层次化空间网格与建模局部细节的共享锚点码本，这种组合形成了紧凑而富有表现力的特征表示，旨在最小化冗余并支持高效的层级自适应。展开机制促进了层间可复用性，仅需极少量数据开销即可实现渐进式优化。实验表明，我们的方法在所有LOD层级均保持高渲染质量，同时实现显著的存储压缩。这些结果证明了本方法在带宽和内存受限场景下实现实时3DGS渲染的实用性与可扩展性。

---

## 📌 Poster

*其他相关研究*

---

### 1. Identifying Inductive Biases for Robot Co-Design

- **作者**: Apoorv Vaish, Oliver Brock
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.11768v1)
- **发表日期**: 2026-04-13
- **匹配关键词**: locomotion and manipulation
- **arXiv**: [2604.11768v1](http://arxiv.org/abs/2604.11768v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 协同设计机器人的形态与控制能够确保二者之间产生协同作用，这在生物有机体中普遍存在。然而，协同设计是一个高维搜索问题。为了使搜索过程易于处理，我们需要一种系统性的方法来识别适合其结构的归纳偏置。本文分析了软体运动与操作任务中的协同设计空间，并识别出在其协同设计空间各区域中普遍存在的三种模式。我们观察到，在协同设计空间的特定区域内，质量变化沿着低维流形分布。高质量区域的变化分布在更多维度上，同时形态与控制之间紧密耦合。基于这些发现，我们设计了一种高效的协同设计算法。由于这种结构的具体表现形式因任务而异且无法预先获知，我们的算法通过搜索过程中收集的信息进行推断，并适应每个任务的具体结构。与基准算法相比，该算法实现了36%的性能提升。此外，我们的算法在样本效率上比这些基准算法高出两个数量级以上，证明了利用归纳偏置进行协同设计的有效性。

---

### 2. WM-DAgger: Enabling Efficient Data Aggregation for Imitation Learning with World Models

- **作者**: Anlan Yu, Zaishu Chen, Peili Song, Zhiqing Hong, Haotian Wang, Desheng Zhang, Tian He, Yi Ding, Daqing Zhang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.11351v1)
- **发表日期**: 2026-04-13
- **匹配关键词**: eye-in-hand
- **arXiv**: [2604.11351v1](http://arxiv.org/abs/2604.11351v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: GITHUB, CODE
  - 链接：https://github.com/czs12354-xxdbd/WM-Dagger.
- **中文摘要**: 模仿学习是训练机器人策略的强大范式，但其性能受限于误差累积问题：微小的策略偏差可能使机器人进入训练集中未见的分布外状态，此时策略可能产生更大误差，最终导致任务失败。虽然数据聚合框架试图解决这一问题，但其对持续人工干预的依赖严重限制了可扩展性。本文提出WM-DAgger框架，通过利用世界模型合成分布外恢复数据，构建高效的数据聚合机制且无需人工参与。我们聚焦于眼在手配置机械臂的操控任务，仅需少量演示样本。为避免合成误导性数据并克服世界模型固有的幻觉问题，本框架引入两大核心机制：（1）校正动作合成模块，生成面向任务的恢复动作以防止误导性监督；（2）一致性引导过滤模块，通过将合成轨迹的末端帧锚定至专家演示中的真实对应帧，剔除物理不可行的轨迹。我们在多个真实机器人任务上对WM-DAgger进行了全面验证。实验结果表明，该方法显著提升了任务成功率，在仅使用五次演示的软质包裹推动任务中达到93.3%的成功率。源代码已公开于https://github.com/czs12354-xxdbd/WM-Dagger。

---

### 3. CLASP: Closed-loop Asynchronous Spatial Perception for Open-vocabulary Desktop Object Grasping

- **作者**: Yiran Ling, Wenxuan Li, Siying Dong, Yize Zhang, Xiaoyao Huang, Jing Jiang, Ruonan Li, Jie Liu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.11320v1)
- **发表日期**: 2026-04-13
- **匹配关键词**: robot grasping
- **arXiv**: [2604.11320v1](http://arxiv.org/abs/2604.11320v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 桌面物体抓取在智能制造、物流及农业领域应用广泛。尽管视觉语言模型在机器人操作中展现出巨大潜力，但其在底层抓取任务中的部署面临关键挑战：高质量多模态演示数据稀缺、几何基础薄弱导致的空间幻觉问题，以及动态环境中开环执行的脆弱性。为解决这些挑战，我们提出闭环异步空间感知框架——一种融合多模态感知、逻辑推理与状态反馈的新型异步闭环框架。首先，我们设计了双路径层次感知模块，将高层语义意图与几何基础解耦，通过引导推理模型输出确定性动作元组来减少空间幻觉。其次，构建异步闭环评估器，通过对比执行前后的状态差异生成文本诊断反馈，建立稳健的纠错循环机制，有效改善传统开环执行在动态环境中的脆弱性。最后，我们开发了可扩展的多模态数据引擎，无需人工遥操作即可从真实与合成场景中自动生成高质量空间标注与推理模板。大量实验表明，该方法显著优于现有基线模型，整体成功率高达87.0%。值得注意的是，该框架在不同物体间展现出卓越的泛化能力，成功弥合仿真与现实的差距，在几何复杂类别及杂乱场景中表现出非凡的鲁棒性。

---

### 4. ScoRe-Flow: Complete Distributional Control via Score-Based Reinforcement Learning for Flow Matching

- **作者**: Xiaotian Qiu, Lukai Chen, Jinhao Li, Qi Sun, Cheng Zhuo, Guohao Dai
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.10962v1)
- **发表日期**: 2026-04-13
- **匹配关键词**: exploration
- **arXiv**: [2604.10962v1](http://arxiv.org/abs/2604.10962v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 流匹配策略已成为机器人控制的高效核心框架，通过快速且富有表现力的动作生成能力，为近期大规模具身人工智能系统提供了重要支撑。然而，通过模仿学习训练的流匹配策略继承了示范数据的局限性；要超越次优行为仍需强化学习微调。现有方法将确定性流转化为具有可学习噪声注入的随机微分方程，实现了探索性与可处理似然，但当示范数据已提供强先验时，这种仅依赖噪声的控制方式可能影响训练效率。我们观察到，通过评分函数（即对数密度梯度）调节漂移项，能够引导探索朝向高概率区域，从而提升稳定性。该评分函数可直接从速度场推导出闭式表达式，无需辅助网络。基于此，我们提出ScoRe-Flow——一种结合漂移调节与学习型方差预测的评分强化学习微调方法，实现对随机转移过程均值与方差的解耦控制。实验表明，在D4RL运动控制任务中，ScoRe-Flow比基于流的现有最优方法收敛速度快2.4倍；在Robomimic和Franka Kitchen操作任务中，成功率最高提升5.4%。

---

### 5. AffordGen: Generating Diverse Demonstrations for Generalizable Object Manipulation with Afford Correspondence

- **作者**: Jiawei Zhang, Kaizhe Hu, Yingqian Huang, Yuanchen Ju, Zhengrong Xue, Huazhe Xu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.10579v1)
- **发表日期**: 2026-04-12
- **匹配关键词**: object manipulation, affordance
- **arXiv**: [2604.10579v1](http://arxiv.org/abs/2604.10579v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 尽管现代模仿学习方法在机器人操作领域取得了显著进展，但其性能常因数据多样性不足而受限于几何形态变化。本研究提出的AffordGen框架通过结合强大的三维生成模型与视觉基础模型，利用大规模三维网格中有意义关键点的语义对应关系，生成全新的机器人操作轨迹，从而突破这一局限。该框架构建的大规模可供性感知数据集被用于训练鲁棒的闭环视觉运动策略，将可供性的语义泛化能力与端到端学习的反应鲁棒性相结合。仿真与真实环境实验表明，基于AffordGen训练的策略实现了高成功率，并能对完全未见过的物体进行零样本泛化，显著提升了机器人学习的数据效率。

---

