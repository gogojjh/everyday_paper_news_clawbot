# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-04-05 08:03

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 6/20 篇提供

**🏅 Oral**: 5 篇 | **🌟 Highlight**: 15 篇 | **📌 Poster**: 0 篇

---

## 🏅 Oral (Top recommendations)

*基于用户近期关注方向（world model/action generation；lifelong spatial memory/SLAM2.0；interaction/articulated/tactile）*

---

### 1. DriveDreamer-Policy: A Geometry-Grounded World-Action Model for Unified Generation and Planning

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2604.01765)
- **发表日期**: 
- **匹配关键词**: VLA, vision-language-action, motion planning
- **arXiv**: [2604.01765](https://arxiv.org/abs/2604.01765)
- **📥 PDF**: 已下载至本地 (`2604.01765_DriveDreamer-Policy_A_Geometry-Grounded_World-Action_Model_for_Unified_Generation_and_Planning.pdf`) | recent-focus score=11.50
- **🔒 开源**: 未提及
- **中文摘要**: arXiv:2604.01765v1 公告类型：新  
摘要：近年来，世界-动作模型（WAM）逐渐兴起，旨在连接视觉-语言-动作（VLA）模型与世界模型，统一其推理与指令跟随能力以及时空世界建模。然而，现有的WAM方法通常侧重于二维外观或潜在表示建模，几何基础较为有限——而这正是物理世界中具身系统运行的关键要素。本文提出DriveDreamer-Policy，一种统一的驾驶世界-动作模型，将深度生成、未来视频生成和运动规划集成于单一模块化架构中。该模型采用大型语言模型处理语言指令、多视角图像和动作，随后通过三个轻量级生成器分别生成深度、未来视频和动作。通过学习几何感知的世界表示，并在统一框架中利用该表示指导未来预测与规划，所提出的模型能够生成更连贯的想象未来和更明智的驾驶动作，同时保持模块化和可控延迟。在Navsim v1和v2基准测试上的实验表明，DriveDreamer-Policy在闭环规划和世界生成任务中均表现出色。具体而言，我们的模型在Navsim v1上达到89.2 PDMS，在Navsim v2上达到88.7 EPDMS，优于现有的基于世界模型的方法，同时生成更高质量的未来视频和深度预测。消融研究进一步表明，显式深度学习为视频想象提供了互补优势，并提升了规划的鲁棒性。

---

### 2. AffordTissue: Dense Affordance Prediction for Tool-Action Specific Tissue Interaction

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2604.01371)
- **发表日期**: 
- **匹配关键词**: affordance, vision-language-action model, vision-language-action
- **arXiv**: [2604.01371](https://arxiv.org/abs/2604.01371)
- **📥 PDF**: 已下载至本地 (`2604.01371_AffordTissue_Dense_Affordance_Prediction_for_Tool-Action_Specific_Tissue_Interaction.pdf`) | recent-focus score=8.50
- **🔒 开源**: 未提及
- **中文摘要**: arXiv:2604.01371v1 公告类型：新  
摘要：手术动作自动化在实现类外科医生灵巧控制方面进展迅速，主要得益于从演示学习和视觉-语言-动作模型的进步推动。尽管这些方法在桌面实验中已展现出成功，但将其转化为临床部署仍面临挑战：现有方法对器械在组织表面的交互位置预测能力有限，且缺乏显式的条件输入来确保工具动作特定的安全交互区域。为填补这一空白，我们提出了AffordTissue——一个多模态框架，用于在胆囊切除术中预测工具动作特定的组织可供性区域，并生成密集热图。我们的方法结合了时序视觉编码器（捕捉多视角下的工具运动和组织动态）、语言条件机制（实现对多样化器械-动作对的泛化）以及DiT风格解码器（用于密集可供性预测）。通过整理并标注来自103例胆囊切除术的15,638个视频片段，涵盖涉及四种器械（钩、抓钳、剪刀、夹钳）及其相关任务（解剖、抓持、夹闭、切割）的六种独特工具-动作对，我们建立了首个组织可供性基准测试。实验表明，相较于视觉-语言模型基线（Molmo-VLM的60.2像素ASSD对比我们的20.6像素ASSD），我们的方法实现了显著提升，证明针对特定任务设计的架构在密集手术可供性预测方面优于大规模基础模型。通过预测工具动作特定的组织可供性区域，AffordTissue为安全的手术自动化提供了显式空间推理，有望为实现针对适当组织区域的显式策略指导以及器械偏离预测安全区域时的早期安全停止机制提供关键支持。

---

### 3. UniDriveVLA: Unifying Understanding, Perception, and Action Planning for Autonomous Driving

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2604.02190)
- **发表日期**: 
- **匹配关键词**: vision-language-action model, VLA, vision-language-action
- **arXiv**: [2604.02190](https://arxiv.org/abs/2604.02190)
- **📥 PDF**: 已下载至本地 (`2604.02190_UniDriveVLA_Unifying_Understanding,_Perception,_and_Action_Planning_for_Autonomous_Driving.pdf`) | recent-focus score=8.00
- **🔓 开源**: GITHUB
  - 链接：https://github.com/xiaomi-research/unidrivevla
- **中文摘要**: arXiv:2604.02190v1 公告类型：新  
摘要：视觉-语言-行动（VLA）模型近期在自动驾驶领域崭露头角，其潜力在于利用丰富的世界知识提升驾驶系统的认知能力。然而，将此类模型适配于驾驶任务时，目前面临空间感知与语义推理之间的关键矛盾。这导致现有VLA系统不得不做出次优妥协：直接采用2D视觉语言模型会限制空间感知能力，而通过3D空间表征增强又往往会损害VLM原有的推理能力。我们认为，这一矛盾主要源于空间感知与语义推理在共享模型参数中的耦合优化。为突破此局限，我们提出UniDriveVLA——一个基于混合专家Transformer架构的统一驾驶视觉-语言-行动模型，通过专家解耦机制解决感知与推理的冲突。具体而言，该模型包含驾驶理解、场景感知和行动规划三个专家模块，通过掩码联合注意力机制进行协同工作。此外，我们结合稀疏感知范式与三阶段渐进式训练策略，在保持语义推理能力的同时提升空间感知性能。大量实验表明，UniDriveVLA在nuScenes数据集的开环评估和Bench2Drive的闭环评估中均达到最先进水平。更重要的是，该模型在感知、预测和理解等广泛任务中均表现出强大性能，包括3D检测、在线建图、运动预测及驾驶导向的视觉问答，彰显其作为自动驾驶统一模型的广泛适用性。代码与模型已发布于https://github.com/xiaomi-research/unidrivevla

---

### 4. UAV-Track VLA: Embodied Aerial Tracking via Vision-Language-Action Models

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2604.02241)
- **发表日期**: 
- **匹配关键词**: vision-language-action, vision-language-action model, VLA, visual tracking
- **arXiv**: [2604.02241](https://arxiv.org/abs/2604.02241)
- **📥 PDF**: 已下载至本地 (`2604.02241_UAV-Track_VLA_Embodied_Aerial_Tracking_via_Vision-Language-Action_Models.pdf`) | recent-focus score=7.00
- **🔓 开源**: GITHUB
  - 链接：https://github.com/Hub-Tian/UAV-Track
- **中文摘要**: arXiv:2604.02241v1 公告类型：新  
摘要：具身视觉跟踪对于无人机执行复杂现实任务至关重要。在具有复杂语义需求的动态城市场景中，视觉-语言-行动模型因其跨模态融合与连续动作生成能力展现出巨大潜力。为在此类环境中建立多模态跟踪基准，我们构建了专用评估基准及大规模数据集，涵盖超过89万帧画面、176项任务和85类不同目标。此外，为解决现有VLA模型中存在的时序特征冗余与空间几何先验缺失问题，我们提出改进型VLA跟踪模型UAV-Track VLA。该模型基于$\pi_{0.5}$架构，引入时序压缩网络以高效捕捉帧间动态特征，同时设计包含空间感知辅助定位头与流匹配动作专家的并行双分支解码器，实现跨模态特征解耦与细粒度连续动作生成。在CARLA仿真器中的系统实验验证了本方法优越的端到端性能：在极具挑战性的远距离行人跟踪任务中，UAV-Track VLA取得61.76%的成功率与269.65帧平均跟踪时长，显著超越现有基线模型；同时展现出对未见过环境的强零样本泛化能力，相比原始$\pi_{0.5}$模型单步推理延迟降低33.4%（至0.0571秒），可实现高效实时无人机控制。数据样本与演示视频详见：https://github.com/Hub-Tian/UAV-Track\_VLA。

---

### 5. Tex3D: Objects as Attack Surfaces via Adversarial 3D Textures for Vision-Language-Action Models

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2604.01618)
- **发表日期**: 
- **匹配关键词**: vision-language-action model, VLA, vision-language-action
- **arXiv**: [2604.01618](https://arxiv.org/abs/2604.01618)
- **📥 PDF**: 已下载至本地 (`2604.01618_Tex3D_Objects_as_Attack_Surfaces_via_Adversarial_3D_Textures_for_Vision-Language-Action_Models.pdf`) | recent-focus score=6.50
- **🔒 开源**: 未提及
- **中文摘要**: arXiv:2604.01618v1 公告类型：新  
摘要：视觉-语言-动作（VLA）模型在机器人操作任务中展现出强大性能，但其对物理可实现对抗攻击的鲁棒性仍待深入探索。现有研究通过语言扰动和二维视觉攻击揭示了系统脆弱性，但这些攻击面要么难以代表实际部署场景，要么在物理真实性上存在局限。相比之下，对抗性三维纹理构成了更具物理合理性和破坏性的威胁——它们能自然附着于被操作物体，且更易于在物理环境中部署。然而，将对抗性三维纹理引入VLA系统面临重大挑战：标准三维模拟器无法提供从VLA目标函数到物体外观的可微分优化路径，导致难以实现端到端优化。为此，我们提出前景-背景解耦技术，通过双渲染器对齐实现可微分纹理优化，同时保持原始模拟环境不变。为确保攻击在物理世界长时程、多视角场景中持续有效，我们进一步提出轨迹感知对抗优化方法，通过行为关键帧优先策略和基于顶点的参数化技术稳定优化过程。基于这些设计，我们构建了Tex3D框架——首个能在VLA模拟环境中实现三维对抗纹理端到端优化的系统。仿真与真实机器人实验表明，Tex3D能在多种操作任务中显著降低VLA模型性能，最高可实现96.7%的任务失败率。这些实证结果揭示了VLA系统对物理三维对抗攻击的关键脆弱性，凸显了鲁棒性感知训练的必要性。

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. UniRecGen: Unifying Multi-View 3D Reconstruction and Generation

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2604.01479)
- **发表日期**: 
- **匹配关键词**: 3D reconstruction, 3d reconstruction
- **arXiv**: [2604.01479](https://arxiv.org/abs/2604.01479)
- **📥 PDF**: 已下载至本地 (`2604.01479_UniRecGen_Unifying_Multi-View_3D_Reconstruction_and_Generation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: arXiv:2604.01479v1 公告类型：新  
摘要：稀疏视角三维建模体现了重建保真度与生成合理性之间的根本张力。前馈重建方法在效率和输入对齐方面表现出色，但往往缺乏结构完整性所需的全局先验。相反，基于扩散的生成方法能提供丰富的几何细节，却在多视角一致性上存在不足。我们提出了UniRecGen，这是一个将这两种范式整合到单一协作系统中的统一框架。为克服坐标空间、三维表示和训练目标之间的固有冲突，我们将两个模型对齐至共享的规范空间。我们采用解耦协作学习策略，在保持训练稳定性的同时，实现推理过程中的无缝协作。具体而言，重建模块经过调整以提供规范几何锚点，而扩散生成器则利用潜在增强条件机制来优化并完善几何结构。实验结果表明，UniRecGen在从稀疏观测中创建完整且一致的三维模型时，实现了卓越的保真度与鲁棒性，其性能优于现有方法。

---

### 2. F3DGS: Federated 3D Gaussian Splatting for Decentralized Multi-Agent World Modeling

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2604.01605)
- **发表日期**: 
- **匹配关键词**: 3D reconstruction, 3d reconstruction, 3D gaussian splatting, gaussian splatting, exploration
- **arXiv**: [2604.01605](https://arxiv.org/abs/2604.01605)
- **📥 PDF**: 已下载至本地 (`2604.01605_F3DGS_Federated_3D_Gaussian_Splatting_for_Decentralized_Multi-Agent_World_Modeling.pdf`)
- **🔓 开源**: CODE
- **中文摘要**: arXiv:2604.01605v1 公告类型：新  
摘要：本文提出F3DGS——一种用于去中心化多智能体三维重建的联邦式三维高斯溅射框架。现有3DGS流程假设所有观测数据均可集中访问，这限制了其在分布式机器人场景中的应用，因为智能体通常独立运行且集中式数据聚合可能受限。直接将集中式训练扩展至多智能体系统会引入通信开销与几何不一致性问题。F3DGS首先通过配准来自多个客户端的局部融合激光雷达点云构建共享几何支架，以初始化全局3DGS模型。在联邦优化过程中，高斯位置保持固定以确保几何对齐，各客户端仅更新外观相关属性（包括协方差、不透明度及球谐系数）。服务器采用可见性感知聚合机制，根据各客户端观测每个高斯的频率对其贡献进行加权，从而解决多智能体探索中固有的部分可观测性挑战。为评估去中心化重建效果，我们收集了包含同步激光雷达、RGB与IMU测量的多序列室内数据集。实验表明，F3DGS在实现跨智能体分布式优化的同时，达到了与集中式训练相当的重建质量。数据集、开发工具包及源代码将公开发布。

---

### 3. Lifting Unlabeled Internet-level Data for 3D Scene Understanding

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2604.01907)
- **发表日期**: 
- **匹配关键词**: navigation, VLN
- **arXiv**: [2604.01907](https://arxiv.org/abs/2604.01907)
- **📥 PDF**: 已下载至本地 (`2604.01907_Lifting_Unlabeled_Internet-level_Data_for_3D_Scene_Understanding.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: arXiv:2604.01907v1 公告类型：新  
摘要：带标注的三维场景数据稀缺且获取成本高昂，而互联网上存在大量易于获取的无标注视频。本文证明，通过精心设计的数据引擎，能够利用网络收集的无标注视频自动生成训练数据，结合人工标注数据集共同促进端到端模型在三维场景理解中的发展。我们识别并分析了自动化数据生成中的瓶颈问题，揭示了决定从无标注数据中学习效率与效果的关键因素。为验证该方法在不同感知粒度上的适用性，我们在三个任务上进行评估：涵盖低层感知（三维目标检测与实例分割）到高层推理（三维空间视觉问答与视觉语言导航）。使用生成数据训练的模型展现出强大的零样本性能，并在微调后获得进一步提升。这表明利用易于获取的网络数据作为提升场景理解系统能力的路径具有可行性。

---

### 4. Stop Wandering: Efficient Vision-Language Navigation via Metacognitive Reasoning

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2604.02318)
- **发表日期**: 
- **匹配关键词**: navigation, VLN, exploration
- **arXiv**: [2604.02318](https://arxiv.org/abs/2604.02318)
- **📥 PDF**: 已下载至本地 (`2604.02318_Stop_Wandering_Efficient_Vision-Language_Navigation_via_Metacognitive_Reasoning.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: arXiv:2604.02318v1 公告类型：交叉  
摘要：基于基础模型的免训练视觉语言导航（VLN）智能体能够遵循指令并探索三维环境。然而，现有方法依赖于贪婪的前沿选择与被动空间记忆，导致局部振荡和重复访问等低效行为。我们认为这源于元认知能力的缺失：智能体无法监控其探索进度、诊断策略失败或进行相应调整。为解决这一问题，我们提出MetaNav——一种集成了空间记忆、历史感知规划与反思校正的元认知导航智能体。空间记忆构建了持久的三维语义地图；历史感知规划通过惩罚重复访问提升效率；反思校正模块能检测停滞状态，并利用大语言模型生成指导未来前沿选择的修正规则。在GOAT-Bench、HM3D-OVON和A-EQA数据集上的实验表明，MetaNav实现了最先进的性能，同时将视觉语言模型查询量降低20.7%，证明元认知推理能显著提升导航的鲁棒性与效率。

---

### 5. SPAGS: Sparse-View Articulated Object Reconstruction from Single State via Planar Gaussian Splatting

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2511.17092)
- **发表日期**: 
- **匹配关键词**: 3D reconstruction, articulated object, 3d reconstruction, gaussian splatting
- **arXiv**: [2511.17092](https://arxiv.org/abs/2511.17092)
- **📥 PDF**: 已下载至本地 (`2511.17092_SPAGS_Sparse-View_Articulated_Object_Reconstruction_from_Single_State_via_Planar_Gaussian_Splatting.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: arXiv:2511.17092v3 公告类型：替换  
摘要：铰接物体在日常环境中无处不在，其三维重建在多个领域具有重要意义。然而，现有的铰接物体重建方法通常需要多阶段、多视角观测等高成本输入。为突破这些限制，我们提出了一种基于平面高斯溅射的类别无关铰接物体重建框架，该框架仅需使用单一状态下的稀疏视角RGB图像。具体而言，我们首先引入高斯信息场，从候选相机位姿中感知最优稀疏视角。为确保精确的几何保真度，我们将传统三维高斯约束为平面基元，从而促进准确的法向量和深度估计。随后，通过深度平滑性和少样本扩散先验的正则化，以由粗到精的方式优化平面高斯模型。此外，我们通过视觉提示利用视觉语言模型实现开放词汇的部件分割与关节参数估计。在合成数据集和真实数据集上的大量实验表明，本方法显著优于现有基线，实现了更优的部件级表面重建保真度。代码与数据详见补充材料。

---

### 6. GPA-VGGT:Adapting VGGT to Large Scale Localization by Self-Supervised Learning with Geometry and Physics Aware Loss

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2601.16885)
- **发表日期**: 
- **匹配关键词**: 3D reconstruction, 3d reconstruction
- **arXiv**: [2601.16885](https://arxiv.org/abs/2601.16885)
- **📥 PDF**: 已下载至本地 (`2601.16885_GPA-VGGTAdapting_VGGT_to_Large_Scale_Localization_by_Self-Supervised_Learning_with_Geometry_and_Phys.pdf`)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/X-yangfan/GPA-VGGT.
- **中文摘要**: arXiv:2601.16885v3 公告类型：替换  
摘要：基于Transformer的通用视觉几何框架在相机姿态估计和三维场景理解方面展现出优异性能。近期视觉几何基础Transformer（VGGT）模型的进展在相机姿态估计与三维重建任务中显示出巨大潜力。然而，这类模型通常依赖真实标注数据进行训练，在适应未标注及未见场景时面临挑战。本文提出一种自监督框架，利用未标注数据训练VGGT模型，从而提升其在大规模环境中的定位能力。为实现这一目标，我们将传统的成对几何关系扩展为序列级几何约束以进行自监督学习。具体而言，我们在每个序列中采样多帧源图像，并将其几何投影至不同目标帧，以此增强时序特征一致性。我们将物理光度一致性与几何约束构建为联合优化损失函数，从而规避对硬标签的依赖。通过该方法训练模型，不仅局部与全局跨视角注意力层能够有效捕捉潜在的多视角几何关系，相机参数头与深度估计头亦能实现协同优化。实验表明，该模型可在数百次迭代内收敛，并在大规模定位任务中取得显著性能提升。代码发布于https://github.com/X-yangfan/GPA-VGGT。

---

### 7. Think, Act, Build: An Agentic Framework with Vision Language Models for Zero-Shot 3D Visual Grounding

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2604.00528)
- **发表日期**: 
- **匹配关键词**: 3D reconstruction, 3d reconstruction
- **arXiv**: [2604.00528](https://arxiv.org/abs/2604.00528)
- **📥 PDF**: 已下载至本地 (`2604.00528_Think,_Act,_Build_An_Agentic_Framework_with_Vision_Language_Models_for_Zero-Shot_3D_Visual_Grounding.pdf`)
- **🔓 开源**: CODE
- **中文摘要**: arXiv:2604.00528v2 公告类型：替换  
摘要：三维视觉定位（3D-VG）旨在通过自然语言描述在三维场景中定位物体。尽管近期利用视觉语言模型（VLM）的进展探索了零样本可能性，但这些方法通常依赖于预处理的三维点云静态流程，本质上将定位任务简化为候选匹配。为突破这一局限，我们的核心思路是将任务解耦：利用二维VLM解析复杂空间语义，同时依靠确定性多视图几何实现三维结构实例化。基于这一洞见，我们提出“思考、行动、构建（TAB）”动态智能体框架，将3D-VG任务重构为直接在原始RGB-D流上运行的生成式二维到三维重建范式。具体而言，在专用3D-VG技能引导下，我们的VLM智能体动态调用视觉工具在二维帧序列中追踪并重建目标。关键创新在于，为克服严格VLM语义追踪导致的多视图覆盖缺失，我们提出语义锚定几何扩展机制：先在参考视频片段中锚定目标，再利用多视图几何将其空间位置传播至未观测帧。这使得智能体能够通过相机参数聚合多视图特征，“构建”目标的三维表征，直接将二维视觉线索映射为三维坐标。此外，为确保严谨评估，我们发现了现有基准中存在的参考歧义与类别错误等缺陷，并手动修正了错误查询。在ScanRefer和Nr3D数据集上的大量实验表明，本框架完全基于开源模型，显著超越先前零样本方法，甚至优于全监督基线模型。

---

### 8. LESV: Language Embedded Sparse Voxel Fusion for Open-Vocabulary 3D Scene Understanding

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2604.01388)
- **发表日期**: 
- **匹配关键词**: 3D gaussian splatting, gaussian splatting
- **arXiv**: [2604.01388](https://arxiv.org/abs/2604.01388)
- **📥 PDF**: 已下载至本地 (`2604.01388_LESV_Language_Embedded_Sparse_Voxel_Fusion_for_Open-Vocabulary_3D_Scene_Understanding.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: arXiv:2604.01388v1 公告类型：新  
摘要：开放词汇3D场景理解的最新进展主要依赖于3D高斯泼溅（3DGS）将视觉语言特征注册到3D空间中。然而，我们发现这些方法存在两个关键局限：一是由非结构化、重叠的高斯分布引起的空间模糊性，这迫使采用概率性特征注册；二是通过对象级掩码池化特征导致的多层次语义模糊，削弱了细粒度细节。为解决这些问题，我们提出了一种新颖框架，利用稀疏体素栅格化（SVRaster）作为结构化、互斥的几何表示。通过单目深度和法向先验对SVRaster进行正则化，我们建立了稳定的几何基础。这实现了确定性的、置信度感知的特征注册过程，并抑制了3DGS中常见的语义渗漏伪影。此外，我们通过利用基础模型AM-RADIO新兴的密集对齐特性，解决了多层次模糊问题，避免了分层训练方法的计算开销。我们的方法在开放词汇3D物体检索和点云理解基准测试中达到了最先进的性能，尤其在细粒度查询任务上表现突出，而传统注册方法通常在此类任务中失效。

---

### 9. Better Rigs, Not Bigger Networks: A Body Model Ablation for Gaussian Avatars

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2604.01447)
- **发表日期**: 
- **匹配关键词**: 3D gaussian splatting, gaussian splatting
- **arXiv**: [2604.01447](https://arxiv.org/abs/2604.01447)
- **📥 PDF**: 已下载至本地 (`2604.01447_Better_Rigs,_Not_Bigger_Networks_A_Body_Model_Ablation_for_Gaussian_Avatars.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: arXiv:2604.01447v1 公告类型：新  
摘要：近期基于SMPL构建的3D高斯溅射方法在持续提升整体训练架构复杂度的同时，实现了卓越的视觉保真度。我们证明这种复杂性大多是不必要的：通过采用经SAM-3D-Body估计的动量人体骨骼（MHR）替代SMPL，一个无需学习形变或姿态相关修正的极简流程，在PeopleSnapshot和ZJU-MoCap数据集上取得了当前最高的PSNR报告值，以及具有竞争力或更优的LPIPS与SSIM指标。为解耦姿态估计质量与人体模型表征能力的影响，我们进行了两项对照实验：将SAM-3D-Body网格转换为SMPL-X格式，并将原始数据集的SMPL姿态转换为MHR格式，两者均在相同条件下重新训练。这些实验证实，人体模型的表达能力一直是虚拟形象重建的主要瓶颈，其中网格表征能力与姿态估计质量共同对全流程性能提升产生实质性贡献。

---

### 10. Satellite-Free Training for Drone-View Geo-Localization

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2604.01581)
- **发表日期**: 
- **匹配关键词**: 3D gaussian splatting, gaussian splatting
- **arXiv**: [2604.01581](https://arxiv.org/abs/2604.01581)
- **📥 PDF**: 已下载至本地 (`2604.01581_Satellite-Free_Training_for_Drone-View_Geo-Localization.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: arXiv:2604.01581v1 公告类型：新  
摘要：无人机视角地理定位（DVGL）旨在通过无人机对某位置的观测，从参考库中检索出对应的地理标记卫星图块，从而在GPS受限环境中确定无人机的位置。现有方法多采用单张倾斜无人机图像作为观测表示，而本文提出的无卫星训练框架则针对多视角无人机序列设计，在跨视图检索前构建几何归一化的无人机端位置表征。现有方法在训练过程中依赖卫星图像，无论是通过配对监督还是无监督对齐，这在实际部署中若卫星数据不可用或受限时会受到限制。本文提出一种无卫星训练框架，通过三个阶段将无人机图像转换为跨视图兼容的表征：无人机端三维场景重建、基于几何的伪正射影像生成，以及用于检索的无卫星特征聚合。具体而言，我们首先利用三维高斯泼溅技术从多视角无人机图像重建稠密三维场景，并通过PCA引导的正射投影将重建几何投影为伪正射影像。该渲染阶段直接基于重建的场景几何进行，无需在渲染时获取相机参数。接着，我们通过轻量级几何引导修复技术优化这些正射影像，获得纹理完整的无人机端视图。最后，从生成的伪正射影像中提取DINOv3补丁特征，仅使用无人机数据学习Fisher向量聚合模型，并在测试时复用该模型对卫星图块进行编码以实现跨视图检索。在University-1652和SUES-200数据集上的实验结果表明，我们的无卫星训练框架显著优于无卫星泛化基线方法，并缩小了与使用卫星图像训练方法之间的性能差距。

---

### 11. Director: Instance-aware Gaussian Splatting for Dynamic Scene Modeling and Understanding

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2604.01678)
- **发表日期**: 
- **匹配关键词**: gaussian splatting
- **arXiv**: [2604.01678](https://arxiv.org/abs/2604.01678)
- **📥 PDF**: 已下载至本地 (`2604.01678_Director_Instance-aware_Gaussian_Splatting_for_Dynamic_Scene_Modeling_and_Understanding.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: arXiv:2604.01678v1 公告类型：新  
摘要：体视频旨在将动态场景建模为时间连贯的四维表示。尽管近期基于高斯分布的方法在渲染保真度方面取得了显著成果，但它们主要侧重于外观表现，而对实例级结构缺乏明确感知，这限制了在高度动态场景中的稳定跟踪与语义推理能力。本文提出Director——一种统一时空高斯表示方法，能够同时建模人体动作表现、高保真渲染与实例级语义。我们的核心洞见在于：嵌入实例一致的语义信息天然契合四维建模需求，既能实现更精确的场景解构，又能支持鲁棒的动态场景理解。为此，我们利用时间对齐的实例掩码和源自多模态大语言模型的语句嵌入，通过两个多层感知机解码器监督每个高斯点的可学习语义特征，从而构建语言对齐的四维表示并强化跨时间身份一致性。为提升时间稳定性，我们将二维光流与四维高斯表示相融合，通过微调运动参数实现可靠初始化并减少漂移误差。在训练过程中，我们进一步引入几何感知的符号距离场约束及增强表面连续性的正则化项，从而提升动态前景建模的时间连贯性。实验表明，Director在实现时间连贯四维重建的同时，能够同步完成实例分割与开放词汇查询任务。

---

### 12. FaCT-GS: Fast and Scalable CT Reconstruction with Gaussian Splatting

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2604.01844)
- **发表日期**: 
- **匹配关键词**: gaussian splatting
- **arXiv**: [2604.01844](https://arxiv.org/abs/2604.01844)
- **📥 PDF**: 已下载至本地 (`2604.01844_FaCT-GS_Fast_and_Scalable_CT_Reconstruction_with_Gaussian_Splatting.pdf`)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/PaPieta/fact-gs.
- **中文摘要**: arXiv:2604.01844v1 公告类型：新  
摘要：高斯泼溅（GS）已成为图像渲染的主导技术，并迅速被应用于X射线计算机断层扫描（CT）重建任务。然而，尽管其性能与许多先前方法相当甚至更优，但GS的优势通常不足以显著推动从成熟重建算法的转变。本文通过引入FaCT-GS框架，解决了基于GS方法中最突出的剩余局限性，实现了快速且灵活的CT重建。通过对体素化和光栅化流程的深度优化，我们的新方法比先前方法显著更快，并能良好适应投影和输出体积大小的变化。此外，改进的体素化技术能够快速将高斯分布拟合到现有体积数据上，这可以作为预热启动重建的先验信息，或仅作为一种替代的压缩表示方式。在标准的512x512投影上，FaCT-GS比当前最先进的GS CT重建方法快4倍以上，在2k投影上则快13倍以上。实现代码可在以下网址获取：https://github.com/PaPieta/fact-gs。

---

### 13. GS^2: Graph-based Spatial Distribution Optimization for Compact 3D Gaussian Splatting

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2604.01884)
- **发表日期**: 
- **匹配关键词**: 3D gaussian splatting, gaussian splatting
- **arXiv**: [2604.01884](https://arxiv.org/abs/2604.01884)
- **📥 PDF**: 已下载至本地 (`2604.01884_GS^2_Graph-based_Spatial_Distribution_Optimization_for_Compact_3D_Gaussian_Splatting.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: arXiv:2604.01884v1 公告类型：新  
摘要：3D高斯泼溅（3DGS）在新视角合成与实时渲染中展现出突破性性能。然而，其实际应用受限于海量高斯点带来的高内存消耗。现有许多基于剪枝的3DGS变体虽能降低内存占用，但往往损害空间一致性并可能导致渲染伪影。为解决这一问题，我们提出基于图结构的空间分布优化方法（GS^2），通过优化高斯点的空间分布来提升重建质量。具体而言，我们设计了基于证据下界的自适应致密化策略，可自动控制高斯点的增殖过程。同时提出透明度感知的渐进式剪枝策略，通过动态移除低透明度高斯点进一步降低内存消耗。此外，我们构建了基于图的特征编码模块，通过特征引导的点位移机制调整空间分布。大量实验表明，GS^2在实现紧凑高斯表示的同时，能提供更优的渲染质量。相较于原始3DGS，该方法仅需约12.5%的高斯点即可获得更高的峰值信噪比。在渲染质量与内存效率方面，GS^2均优于所有对比基线方法。

---

### 14. Resonance4D: Frequency-Domain Motion Supervision for Preset-Free Physical Parameter Learning in 4D Dynamic Physical Scene Simulation

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2604.01994)
- **发表日期**: 
- **匹配关键词**: 3D gaussian splatting, gaussian splatting
- **arXiv**: [2604.01994](https://arxiv.org/abs/2604.01994)
- **📥 PDF**: 已下载至本地 (`2604.01994_Resonance4D_Frequency-Domain_Motion_Supervision_for_Preset-Free_Physical_Parameter_Learning_in_4D_Dy.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: arXiv:2604.01994v1 公告类型：新  
摘要：基于静态3D场景的物理驱动4D动态仿真始终受限于一个被忽视的矛盾：可靠的运动监督通常依赖于在线视频扩散或光流管道，其计算成本远超仿真器本身。现有方法通过仅优化部分材料参数进一步简化逆向物理建模，限制了具有复杂材料和动态场景的真实感。我们提出Resonance4D，这是一个物理驱动的4D动态仿真框架，通过轻量级但物理表达性强的监督，将3D高斯泼溅与材料点法耦合。我们的核心洞见是：通过在互补域中联合约束运动，无需密集时间生成即可实现动态一致性。为此，我们引入双域运动监督（DMS），将局部变形的空间结构一致性与振荡及全局动态模式的频域谱一致性相结合，在保留物理意义运动线索的同时，显著降低训练成本和内存开销。为实现稳定的全参数物理恢复，我们进一步结合零样本文本提示分割与仿真引导初始化，自动将高斯分解为对象部件级区域，并支持全材料参数的联合优化。在合成场景和真实场景上的实验表明，Resonance4D在实现强物理保真度和运动一致性的同时，将峰值GPU内存从超过35GB降低至约20GB，使得在单张消费级GPU上实现高保真物理驱动4D仿真成为可能。

---

### 15. ProDiG: Progressive Diffusion-Guided Gaussian Splatting for Aerial to Ground Reconstruction

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2604.02003)
- **发表日期**: 
- **匹配关键词**: gaussian splatting
- **arXiv**: [2604.02003](https://arxiv.org/abs/2604.02003)
- **📥 PDF**: 已下载至本地 (`2604.02003_ProDiG_Progressive_Diffusion-Guided_Gaussian_Splatting_for_Aerial_to_Ground_Reconstruction.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: arXiv:2604.02003v1 公告类型：新  
摘要：仅从航拍图像生成地面视角和连贯的三维场地模型具有挑战性，原因在于视角变化极端、中间观测数据缺失以及尺度差异巨大。现有方法要么通过后处理优化渲染结果，但常产生几何不一致的产物；要么依赖多高度地面实况数据，而这类数据往往难以获取。高斯泼溅和基于扩散的优化方法能在小尺度变化下提升保真度，但在航拍到地面的巨大视角跨度中表现欠佳。为突破这些局限，我们提出了ProDiG（渐进式高度高斯泼溅）——一种扩散引导框架，通过渐进式优化将航拍三维表征逐步提升至地面级保真度。ProDiG通过合成中间高度视角，并利用几何感知因果注意力模块在每一阶段优化高斯表征，该模块将极线结构注入参考视角的扩散过程中。距离自适应高斯模块则根据相机距离动态调整高斯尺度与透明度，确保在大视角跨度下实现稳定重建。这些组件共同实现了无需额外地面实况视角的渐进式几何优化。在合成数据集与真实场景数据集上的大量实验表明，ProDiG能生成视觉逼真的地面渲染效果与连贯的三维几何结构，在视觉质量、几何一致性及对极端视角变化的鲁棒性方面显著优于现有方法。

---

