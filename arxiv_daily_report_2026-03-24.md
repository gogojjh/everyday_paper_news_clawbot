# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-03-24 09:35

**今日新增**: 19 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 5/19 篇提供

**🌟 Highlight**: 13 篇 | **📌 Poster**: 6 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. Does Peer Observation Help? Vision-Sharing Collaboration for Vision-Language Navigation

- **作者**: Qunchao Jin, Yiliao Song, Qi Wu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.20804v1)
- **发表日期**: 2026-03-21
- **匹配关键词**: exploration, navigation, VLN
- **arXiv**: [2603.20804v1](http://arxiv.org/abs/2603.20804v1)
- **📥 PDF**: 已下载至本地 (`2603.20804v1_Does_Peer_Observation_Help?_Vision-Sharing_Collaboration_for_Vision-Language_Navigation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉语言导航系统本质上受限于部分可观测性，因为智能体只能积累其亲自访问过的位置信息。随着多个机器人在共享环境中日益共存，一个自然的问题随之产生：在同一空间导航的智能体能否从彼此的观察中获益？本研究提出Co-VLN框架——一个极简且模型无关的系统化研究范式，旨在探究并发导航智能体间的同伴观察是否及如何提升视觉语言导航性能。当独立导航的智能体识别出共同经过的位置时，它们会交换结构化感知记忆，从而在不增加探索成本的前提下有效扩展每个智能体的感知范围。我们在R2R基准测试中通过两种代表性范式（基于学习的DUET和零样本MapGPT）验证了该框架，并开展大量分析性实验以系统揭示同伴观察共享在视觉语言导航中的内在机制。实验结果表明，启用视觉共享的模型在两种范式中均实现显著性能提升，为未来具身协同导航研究奠定了坚实基础。

---

### 2. ROI-Driven Foveated Attention for Unified Egocentric Representations in Vision-Language-Action Systems

- **作者**: Xinhai Sun, Xiang Shi, Menglin Zou, Wenlong Huang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.20668v1)
- **发表日期**: 2026-03-21
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2603.20668v1](http://arxiv.org/abs/2603.20668v1)
- **📥 PDF**: 已下载至本地 (`2603.20668v1_ROI-Driven_Foveated_Attention_for_Unified_Egocentric_Representations_in_Vision-Language-Action_Syste.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 具身人工智能系统的发展日益受到物理交互数据可用性与结构性的制约。尽管视觉-语言-动作模型近期取得进展，现有技术流程仍面临数据采集成本高、跨具身对齐能力有限、以及网络规模视觉数据向机器人控制迁移效果不佳等问题。

我们提出一种基于感兴趣区域的工程化工作流程，引入以自我为中心且几何基础的数据表征方法。通过正向运动学将末端执行器位姿投影至单一外部相机，我们实现了无需腕戴相机或多视角系统的运动对齐手部中心感兴趣区域提取。与直接对全帧图像进行降采样不同，本方法在尺寸调整前从原始图像中裁剪感兴趣区域，在保留全局上下文的同时，为接触关键区域维持了更高的局部信息密度。

我们构建了覆盖标定、同步、感兴趣区域生成、确定性边界处理及元数据管理的可复现技术流程。所得数据表征具备具身对齐与视角归一化特性，支持异构机器人间的数据复用。我们认为以自我为中心的感兴趣区域可作为可扩展数据采集与跨具身学习的实用数据抽象层，有效弥合网络级感知与机器人专属控制之间的鸿沟。

---

### 3. StageCraft: Execution Aware Mitigation of Distractor and Obstruction Failures in VLA Models

- **作者**: Kartikay Milind Pangaonkar, Prabin Rath, Omkar Patil, Nakul Gopalan
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.20659v1)
- **发表日期**: 2026-03-21
- **匹配关键词**: vision language action, VLA, vision language action model
- **arXiv**: [2603.20659v1](http://arxiv.org/abs/2603.20659v1)
- **📥 PDF**: 已下载至本地 (`2603.20659v1_StageCraft_Execution_Aware_Mitigation_of_Distractor_and_Obstruction_Failures_in_VLA_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 大规模文本与图像数据的预训练，结合多样化的机器人演示，已助力视觉语言动作模型（VLA）在新型任务、物体及场景中实现泛化。然而，当机器人工作空间存在干扰物或物理障碍等执行时阻碍时，这些模型仍易出现失误。现有策略改进方法通过对基础VLA进行微调以提升泛化能力，但在未见过的干扰场景中仍面临挑战。为解决此问题，本研究探讨了能否利用大规模视觉语言模型（VLM）的互联网级预训练能力来推理此类阻碍并缓解策略失效。为此，我们提出StageCraft——一种无需额外训练的方法，通过基于VLM的上下文推理来操控环境初始状态，从而提升预训练VLA策略的性能。StageCraft以策略执行视频和成功标签为输入，借助VLM的推理能力推断初始状态中哪些物体需要被操控以避免预期执行失败。该框架作为可扩展的即插即用模块，无需对底层策略施加额外约束，仅需少量策略执行样本即可运作。我们在涉及多种干扰物与障碍的三个现实任务领域中评估了结合StageCraft的先进VLA模型性能，结果显示绝对性能提升达40%。在RLBench仿真实验中，StageCraft能根据底层策略强度自适应调整干预程度，并通过增加上下文样本持续提升性能。StageCraft的实际效果视频可见于https://stagecraft-decorator.github.io/stagecraft/。

---

### 4. Towards Practical World Model-based Reinforcement Learning for Vision-Language-Action Models

- **作者**: Zhilong Zhang, Haoxiang Ren, Yihao Sun, Yifei Sheng, Haonan Wang, Haoxin Lin, Zhichao Wu, Pierre-Luc Bacon, Yang Yu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.20607v1)
- **发表日期**: 2026-03-21
- **匹配关键词**: VLA, vision-language-action, vision-language-action model
- **arXiv**: [2603.20607v1](http://arxiv.org/abs/2603.20607v1)
- **📥 PDF**: 已下载至本地 (`2603.20607v1_Towards_Practical_World_Model-based_Reinforcement_Learning_for_Vision-Language-Action_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型在机器人控制任务中展现出强大的泛化能力，但通过强化学习（RL）对其进行微调时，常受限于现实交互的高成本与安全风险。在交互式世界模型中训练VLA模型虽能规避这些问题，却引入了像素级世界建模、多视角一致性以及稀疏奖励下的误差累积等挑战。基于近期大语言多模态模型与基于模型的强化学习领域的研究进展，我们提出VLA-MBPO框架，以系统解决VLA微调中的上述难题。该框架包含三项核心设计：（1）采用统一多模态模型（UMM）实现高效数据驱动的世界建模；（2）通过交错视角解码机制确保多视角一致性；（3）设计分块级分支推演策略以抑制误差传播。理论分析与跨仿真及真实场景的实验表明，VLA-MBPO能显著提升策略性能与样本效率，验证了其在现实机器人部署中的鲁棒性与可扩展性。

---

### 5. Two Experts Are Better Than One Generalist: Decoupling Geometry and Appearance for Feed-Forward 3D Gaussian Splatting

- **作者**: Hwasik Jeong, Seungryong Lee, Gyeongjin Kang, Seungkwon Yang, Xiangyu Sun, Seungtae Nam, Eunbyung Park
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.21064v1)
- **发表日期**: 2026-03-22
- **匹配关键词**: 3D gaussian splatting, gaussian splatting
- **arXiv**: [2603.21064v1](http://arxiv.org/abs/2603.21064v1)
- **🔒 开源**: 未提及
- **中文摘要**: 无姿态前馈三维高斯溅射（3DGS）为快速三维建模开辟了新领域，能够从未校准的多视角图像中通过单次前向传递生成高质量的高斯表示。该领域的主流方法采用统一的单体架构，通常基于以几何为中心的三维基础模型，在单一网络中联合估计相机姿态并合成3DGS表示。尽管这种"一体化"设计在架构上较为简洁，但对于高保真度的3DGS生成可能并非最优选择，因为它们将几何推理与外观建模纠缠在共享表示中。本研究提出2Xplat——一种基于双专家设计的无姿态前馈3DGS框架，该框架明确将几何估计与高斯生成分离。专用几何专家首先预测相机姿态，随后将其显式传递给强大的外观专家以合成三维高斯。尽管该方案概念简洁且在先前研究中鲜有探索，但实践证明其极为有效。在不足5000次训练迭代中，所提出的双专家流程显著超越了先前的无姿态前馈3DGS方法，其性能与最先进的姿态已知方法相当。这些成果对当前主流的统一范式提出了挑战，并揭示了模块化设计原则在复杂三维几何估计与外观合成任务中的潜在优势。

---

### 6. SGAD-SLAM: Splatting Gaussians at Adjusted Depth for Better Radiance Fields in RGBD SLAM

- **作者**: Pengchong Hu, Zhizhong Han
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.21055v1)
- **发表日期**: 2026-03-22
- **匹配关键词**: 3D gaussian splatting, gaussian splatting
- **arXiv**: [2603.21055v1](http://arxiv.org/abs/2603.21055v1)
- **📥 PDF**: 已下载至本地 (`2603.21055v1_SGAD-SLAM_Splatting_Gaussians_at_Adjusted_Depth_for_Better_Radiance_Fields_in_RGBD_SLAM.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://machineperceptionlab.github.io/SGAD-SLAM-Project
- **中文摘要**: 3D高斯泼溅（3DGS）在RGBD SLAM领域取得了显著进展。现有方法通常采用3D高斯或视图绑定的3D高斯来表示跟踪与建图中的辐射场。然而，这些高斯模型在运动灵活性方面要么过于自由，要么过于受限，导致收敛速度缓慢或渲染质量有限。为解决这一问题，我们采用像素对齐的高斯模型，但允许每个高斯沿其光线调整位置以最大化渲染质量，即使通过简化高斯模型来提升系统可扩展性。为加速跟踪过程，我们将每个像素周围的深度分布建模为高斯分布，并利用这些分布实现每帧图像与3D场景的快速对齐。我们在广泛使用的基准测试中进行了评估，验证了设计方案的有效性，并在视角渲染、相机跟踪、运行时间和存储复杂度方面展现出相较于最新方法的优势。代码与视频请访问项目页面：https://machineperceptionlab.github.io/SGAD-SLAM-Project。

---

### 7. SpatialFly: Geometry-Guided Representation Alignment for UAV Vision-and-Language Navigation in Urban Environments

- **作者**: Wen Jiang, Kangyao Huang, Li Wang, Wang Xu, Wei Fan, Jinyuan Liu, Shaoyu Liu, Hanfang Liang, Hongwei Duan, Bin Xu, Xiangyang Ji
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.21046v1)
- **发表日期**: 2026-03-22
- **匹配关键词**: 3d reconstruction, exploration, 3D reconstruction, navigation, VLN, vision-and-language navigation
- **arXiv**: [2603.21046v1](http://arxiv.org/abs/2603.21046v1)
- **📥 PDF**: 已下载至本地 (`2603.21046v1_SpatialFly_Geometry-Guided_Representation_Alignment_for_UAV_Vision-and-Language_Navigation_in_Urban_.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 无人机在自主探索、灾害响应和基础设施巡检等应用中发挥着重要作用。然而，无人机在复杂三维环境中的视觉语言导航仍面临挑战。核心难点在于二维视觉感知与三维轨迹决策空间之间的结构表征不匹配，限制了空间推理能力。为此，我们提出SpatialFly——一种面向无人机视觉语言导航的几何引导空间表征框架。该框架基于RGB观测数据运行，无需显式三维重建，通过引入几何引导的二维表征对齐机制实现创新。具体而言，几何先验注入模块将全局结构线索融入二维语义标记，提供场景级几何引导；随后几何感知重参数化模块通过跨模态注意力将二维语义标记与三维几何标记对齐，并采用门控残差融合保持语义区分度。实验结果表明，SpatialFly在已见和未见环境中均持续优于当前最先进的无人机视觉语言导航基线模型，在未见完整场景分割测试中，相较于最强基线模型将导航误差降低4.03米，成功率提升1.27%。进一步的轨迹级分析表明，SpatialFly生成的轨迹具有更优的路径对齐度，且运动更平滑稳定。

---

### 8. Dreaming the Unseen: World Model-regularized Diffusion Policy for Out-of-Distribution Robustness

- **作者**: Ziou Hu, Xiangtong Yao, Yuan Meng, Zhenshan Bing, Alois Knoll
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.21017v1)
- **发表日期**: 2026-03-22
- **匹配关键词**: diffusion policy
- **arXiv**: [2603.21017v1](http://arxiv.org/abs/2603.21017v1)
- **📥 PDF**: 已下载至本地 (`2603.21017v1_Dreaming_the_Unseen_World_Model-regularized_Diffusion_Policy_for_Out-of-Distribution_Robustness.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 扩散策略在视觉运动控制方面表现出色，但在遭遇严重分布外扰动（如意外物体位移或视觉干扰）时往往会出现灾难性失效。为解决这一脆弱性问题，我们提出了梦想扩散策略框架，该框架通过共享的三维视觉编码器，将扩散世界模型深度整合至策略训练目标中。这种协同优化使策略具备了稳健的状态预测能力。当在推理过程中遭遇突发的分布外异常时，该框架能够检测到现实与想象的差异，主动舍弃受损的视觉流，转而依赖其内部"想象"（自回归预测的潜在动态）安全绕过干扰，在平稳回归物理现实之前生成想象轨迹。大量实验证明该框架具有卓越的抗干扰能力：在MetaWorld任务中实现73.8%的分布外成功率（无预测想象时仅为23.9%），在真实世界严重空间偏移条件下达到83.3%成功率（无预测想象时仅为3.3%）。作为压力测试，即使在初始化后完全依赖开环想象的情况下，该框架仍能保持76.7%的真实世界成功率。

---

### 9. Fast and Robust Deformable 3D Gaussian Splatting

- **作者**: Han Jiao, Jiakai Sun, Lei Zhao, Zhanjie Zhang, Wei Xing, Huaizhong Lin
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.20857v1)
- **发表日期**: 2026-03-21
- **匹配关键词**: 3D gaussian splatting, gaussian splatting
- **arXiv**: [2603.20857v1](http://arxiv.org/abs/2603.20857v1)
- **📥 PDF**: 已下载至本地 (`2603.20857v1_Fast_and_Robust_Deformable_3D_Gaussian_Splatting.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 3D高斯溅射在静态场景的新视角合成中展现出卓越的实时渲染能力与优越的视觉质量。基于这些优势，研究者们逐步将3D高斯技术拓展至动态场景重建领域。在众多技术路径中，基于变形场的方法展现出巨大潜力。这类方法在规范场中维护3D高斯属性，并借助变形场实现时序维度上的场变换。然而，现有方法常面临渲染速度欠佳、对初始点云依赖性强、暗光场景易陷局部最优等挑战。为突破这些局限，我们提出FRoG——一个高效鲁棒的高质量动态场景重建框架。FRoG通过融合逐高斯嵌入与由粗到细的时序嵌入策略，借助时序嵌入的早期融合机制实现渲染加速。此外，为增强对稀疏初始化的鲁棒性，我们创新性地提出深度-误差双引导采样策略，通过在低偏差初始位置向规范场注入新3D高斯，显著减轻变形场的优化负担，提升静态与动态区域的细节重建质量。进一步地，通过调控不透明度变化，我们有效缓解了暗光场景的局部最优问题，显著提升色彩保真度。综合实验结果表明，本方法在保持顶尖视觉质量的同时实现了渲染速度的显著提升。

---

### 10. RoboECC: Multi-Factor-Aware Edge-Cloud Collaborative Deployment for VLA Models

- **作者**: Zihao Zheng, Hangyu Cao, Jiayu Chen, Sicheng Tian, Chenyue Li, Maoliang Li, Xinhao Sun, Guojie Luo, Xiang Chen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.20711v1)
- **发表日期**: 2026-03-21
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2603.20711v1](http://arxiv.org/abs/2603.20711v1)
- **📥 PDF**: 已下载至本地 (`2603.20711v1_RoboECC_Multi-Factor-Aware_Edge-Cloud_Collaborative_Deployment_for_VLA_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型是具身智能领域的主流技术，但面临推理成本高昂的问题。边缘-云协同（ECC）部署通过减轻边缘设备计算压力来满足实时性需求，为此提供了有效的解决方案。然而，现有ECC框架对VLA模型存在两大适配挑战：（1）多样化的模型结构阻碍了最优ECC分割点的确定；（2）即使确定了最优分割点，网络带宽变化仍可能导致性能漂移。针对这些问题，我们提出了一种适用于各类VLA模型的新型ECC部署框架——RoboECC。具体而言，我们设计了模型-硬件协同感知的分割策略，以帮助寻找不同VLA模型的最优分割点。此外，我们提出了网络感知的部署调整方法，通过适应网络波动来维持最优性能。实验表明，RoboECC在仅产生2.55倍至2.62倍开销的情况下，最高可实现3.28倍的加速效果。

---

### 11. The Role and Relationship of Initialization and Densification in 3D Gaussian Splatting

- **作者**: Ivan Desiatov, Torsten Sattler
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.20714v1)
- **发表日期**: 2026-03-21
- **匹配关键词**: 3d reconstruction, 3D reconstruction, 3D gaussian splatting, gaussian splatting
- **arXiv**: [2603.20714v1](http://arxiv.org/abs/2603.20714v1)
- **📥 PDF**: 已下载至本地 (`2603.20714v1_The_Role_and_Relationship_of_Initialization_and_Densification_in_3D_Gaussian_Splatting.pdf`)
- **🔓 开源**: CODE
- **中文摘要**: 三维高斯溅射（3DGS）已成为实现场景照片级真实感三维重建的首选方法，因其能够高效且精确地从图像中恢复场景外观与几何结构。该方法通过一组三维高斯函数来表征场景，这些函数由其位置、空间范围及视角相关颜色参数化。从初始点云出发，3DGS通过优化高斯函数参数，以尽可能精确地重建一组训练图像。通常采用稀疏的运动恢复结构点云作为初始化基础。为获得稠密的高斯点云，3DGS方法依赖稠密化处理阶段。本文系统研究了稠密化与初始化之间的关联，通过构建新型基准测试框架，深入分析了不同类型初始化方案（稠密激光扫描、稠密多视角立体点云、稠密单目深度估计、稀疏SfM点云）与多种稠密化策略的组合效果。研究表明，现有稠密化方法未能充分利用稠密初始化优势，往往无法显著超越基于稀疏SfM初始化的重建效果。我们将公开此基准测试数据集。

---

### 12. GaussianPile: A Unified Sparse Gaussian Splatting Framework for Slice-based Volumetric Reconstruction

- **作者**: Di Kong, Yikai Wang, Wenjie Guo, Yifan Bu, Boya Zhang, Yuexin Duan, Xiawei Yue, Wenbiao Du, Yiman Zhong, Yuwen Chen, Cheng Ma
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.20611v1)
- **发表日期**: 2026-03-21
- **匹配关键词**: exploration, nerf, gaussian splatting, 3D gaussian splatting
- **arXiv**: [2603.20611v1](http://arxiv.org/abs/2603.20611v1)
- **📥 PDF**: 已下载至本地 (`2603.20611v1_GaussianPile_A_Unified_Sparse_Gaussian_Splatting_Framework_for_Slice-based_Volumetric_Reconstruction.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 基于切片的体成像技术应用广泛，它要求表征方法在保持内部结构以进行分析的同时实现高压缩率。为应对这一挑战，我们提出GaussianPile方法，将三维高斯泼溅与成像系统感知聚焦模型相结合。该方法包含三项关键创新：(i) 采用切片感知堆叠策略，通过各向异性三维高斯分布建模跨切片贡献；(ii) 设计可微分投影算子，编码成像采集系统的有限厚度点扩散函数；(iii) 构建紧凑编码与联合优化流程，同步实现高斯集合的重建与压缩。基于CUDA的设计方案在保持高斯基元压缩效率与实时渲染能力的同时，完整保留了高频内部体细节。在显微成像和超声数据集上的实验表明，该方法能有效降低存储与重建成本，维持诊断保真度，并支持快速二维可视化及三维体素化。实际应用中仅需3分钟即可获得高质量结果，较基于神经辐射场的方法提速最高达11倍，相比体素网格实现稳定16倍压缩，为可部署的切片体数据压缩与探索提供了实用路径。

---

### 13. RayMap3R: Inference-Time RayMap for Dynamic 3D Reconstruction

- **作者**: Feiran Wang, Zezhou Shang, Gaowen Liu, Yan Yan
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.20588v1)
- **发表日期**: 2026-03-21
- **匹配关键词**: 3d reconstruction, 3D reconstruction
- **arXiv**: [2603.20588v1](http://arxiv.org/abs/2603.20588v1)
- **📥 PDF**: 已下载至本地 (`2603.20588v1_RayMap3R_Inference-Time_RayMap_for_Dynamic_3D_Reconstruction.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 流式前馈三维重建技术能够从RGB图像中实时联合估计场景几何与相机位姿。然而，由于缺乏显式的动态推理机制，流式模型容易受到运动物体的干扰，导致重建伪影和轨迹漂移。本研究提出RayMap3R——一种无需训练的流式动态场景重建框架。我们观察到基于射线地图的预测存在静态场景偏好，这为动态识别提供了内在线索。基于此发现，我们构建了双分支推理机制：通过对比射线地图预测与图像预测来识别动态区域，并在记忆更新过程中抑制其干扰。进一步引入重置度量对齐和状态感知平滑技术，以保持度量一致性并稳定预测轨迹。在多个基准测试中，本方法在动态场景重建的流式方案中取得了最先进的性能表现。

---

## 📌 Poster

*其他相关研究*

---

### 1. Enhancing Vision-Based Policies with Omni-View and Cross-Modality Knowledge Distillation for Mobile Robots

- **作者**: Kai Li, Shiyu Zhao
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.20679v1)
- **发表日期**: 2026-03-21
- **匹配关键词**: navigation
- **arXiv**: [2603.20679v1](http://arxiv.org/abs/2603.20679v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 基于视觉的策略在机器人领域被广泛应用于操作和移动等任务。然而，在轻量级移动机器人上，这类策略面临场景迁移能力有限、机载计算资源受限以及传感器硬件成本的三重困境。为解决这些问题，我们提出一种知识蒸馏方法，将信息丰富且外观不变的全景深度策略知识迁移至轻量级单目策略中。该方法的核心思想是让学生模型不仅模仿专家动作，同时对齐全景深度教师模型的潜在嵌入表示。实验表明，全景与深度输入能有效提升场景迁移与导航性能，且所提出的蒸馏方法相较于仅模仿动作的策略，显著增强了单目视觉策略的表现。真实环境实验进一步验证了该方法的有效性和实用性。相关代码将公开释放。

---

### 2. E-SocialNav: Efficient Socially Compliant Navigation with Language Models

- **作者**: Ling Xiao, Daeun Song, Xuesu Xiao, Toshihiko Yamasaki
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.20664v1)
- **发表日期**: 2026-03-21
- **匹配关键词**: navigation
- **arXiv**: [2603.20664v1](http://arxiv.org/abs/2603.20664v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: CODE, GITHUB
  - 链接：https://github.com/Dr-LingXiao/ESocialNav.
- **中文摘要**: 语言模型在机器人导航领域的应用日益广泛；然而，现有基准测试主要关注导航成功率，对社会合规性的考量较为有限。此外，依赖大规模语言模型会引发效率问题——其庞大的计算开销导致响应速度降低、能耗增加，难以在资源受限的机器人平台上实现实时部署。本研究评估了GPT-4o与Claude在机器人导航中的社会合规性表现，并提出专为社会合规导航设计的高效语言模型E-SocialNav。尽管训练数据集规模相对较小，E-SocialNav在生成社会合规行为方面始终优于零样本基线模型。通过采用监督微调与直接偏好优化相结合的两阶段训练流程，该模型在文本语义与人类标注的相似度及动作准确性方面均表现出色。源代码已发布于https://github.com/Dr-LingXiao/ESocialNav。

---

### 3. CVT-Bench: Counterfactual Viewpoint Transformations Reveal Unstable Spatial Representations in Multimodal LLMs

- **作者**: Shanmukha Vellamcheti, Uday Kiran Kothapalli, Disharee Bhowmick, Sathyanarayanan N. Aakur
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.21114v1)
- **发表日期**: 2026-03-22
- **匹配关键词**: scene graph
- **arXiv**: [2603.21114v1](http://arxiv.org/abs/2603.21114v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 多模态大语言模型在单视角空间推理任务上表现出色，但其在反事实视角变化下能否保持稳定的空间状态表征仍不明确。我们构建了一个受控诊断基准，通过假设性相机环绕变换（无需重新渲染图像）来评估关系一致性。基于100个合成场景和6,000组关系查询，我们测量了视角一致性、360°循环一致性以及连续变换中的关系稳定性。尽管单视角准确率很高，当前最先进的多模态大语言模型在反事实视角变化下仍表现出系统性性能衰退，频繁违反循环一致性原则，且关系稳定性快速衰减。我们进一步评估了多种输入表征形式——视觉输入、文本边界框和结构化场景图，结果表明增强表征结构能有效提升稳定性。我们的研究揭示：单视角空间准确率会高估模型所构建空间表征的鲁棒性，而表征结构在反事实空间推理中起着关键作用。

---

### 4. Causally-Guided Diffusion for Stable Feature Selection

- **作者**: Arun Vignesh Malarkkan, Xinyuan Wang, Kunpeng Liu, Denghui Zhang, Yanjie Fu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.20930v1)
- **发表日期**: 2026-03-21
- **匹配关键词**: exploration
- **arXiv**: [2603.20930v1](http://arxiv.org/abs/2603.20930v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: CODE
- **中文摘要**: 特征选择是构建以数据为中心的稳健人工智能的基础，但现有方法大多在单一数据分布下优化预测性能。这往往导致选择出在分布变化时失效的伪相关特征。受因果不变性原理启发，我们从稳定性视角研究特征选择问题，提出了因果引导的稳定特征选择扩散模型。该模型将特征选择形式化为特征子集上的近似后验推断，其概率质量倾向于低预测误差与低跨环境方差。我们的框架融合了三个关键洞见：首先，将特征选择构建为稳定性感知的后验采样过程，其中因果不变性作为柔性归纳偏置而非显式因果发现；其次，训练扩散模型作为连续选择掩码的学习先验，结合奖励跨环境不变性的稳定性感知似然函数，该扩散先验能捕捉特征间的结构依赖关系，实现对组合爆炸的选择空间的可扩展探索；第三，执行结合扩散先验与稳定性目标的引导退火朗之万采样，获得可处理的、不确定性感知的后验推断，避免了离散优化并产生稳健的特征选择。我们在呈现分布偏移的开源真实数据集上评估该模型，在分类与回归任务中，相较于基于稀疏性、树模型及稳定性选择的基线方法，该模型始终选择出更稳定、可迁移的特征子集，从而获得更优的分布外性能与更强的选择鲁棒性。

---

### 5. Current state of the multi-agent multi-view experimental and digital twin rendezvous (MMEDR-Autonomous) framework

- **作者**: Logan Banker, Michael Wozniak, Mohanad Alameer, Smriti Nandan Paul, David Meisinger, Grant Baer, Trevor Hunting, Ryan Dunham, Jay Kamdar
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.20575v1)
- **发表日期**: 2026-03-21
- **匹配关键词**: navigation
- **arXiv**: [2603.20575v1](http://arxiv.org/abs/2603.20575v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 随着近地驻留空间物体的日益增多，在轨服务、碎片清除和轨道调整等应用领域对可靠技术的需求不断增长。交会对接作为此类任务的关键阶段，可通过提升自主性来降低操作复杂度与人工负荷。基于机器学习的方法可融入制导、导航与控制架构，构建鲁棒的交会对接框架。本研究提出的多智能体多视角实验与数字孪生交会自主框架，集成了基于学习的光学导航网络、正在开发中的强化学习制导方法以及硬件在环测试平台。导航系统采用轻量化单目姿态估计网络，通过多尺度特征融合技术，并利用真实图像增强数据进行训练以缓解域偏移问题。制导模块重点研究学习稳定性、奖励函数设计及任务相关约束下的系统化超参数调优。本文回顾了Clohessy-Wiltshire动力学中控制屏障函数的既有成果，为保障安全运行约束及指导MMEDR-Autonomous框架内非线性控制器设计提供理论基础。该框架目前正朝着多智能体交会场景的集成实验验证方向持续推进。

---

### 6. Scene Graph-guided SegCaptioning Transformer with Fine-grained Alignment for Controllable Video Segmentation and Captioning

- **作者**: Xu Zhang, Jin Yuan, BinHong Yang, Xuan Liu, Qianjun Zhang, Yuyi Wang, Zhiyong Li, Hanwang Zhang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.20887v1)
- **发表日期**: 2026-03-21
- **匹配关键词**: scene graph
- **arXiv**: [2603.20887v1](http://arxiv.org/abs/2603.20887v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: GITHUB
  - 链接：https://github.com/XuZhang1211/SG-FSCFormer.
- **中文摘要**: 近年来，多模态大模型的显著进展极大地弥合了不同模态间的表征鸿沟，推动了视频多模态理解技术的发展，该技术通过生成关联模态内容来增强用户对视频的理解。然而，现有视频多模态理解方法多聚焦于全局理解，用户交互能力有限。为此，我们提出了一项创新任务——可控视频分割与描述（SegCaptioning），允许用户通过特定提示（如对目标物体绘制边界框）来同步生成精确体现用户意图的关联掩码与描述文本。我们设计了一个创新框架——场景图引导的细粒度分割描述变换器（SG-FSCFormer），该框架集成提示引导时序图变换器，通过自适应提示适配器有效捕捉并表征用户意图，确保生成内容与用户需求高度契合。此外，模型引入细粒度掩码-语言解码器，采用多实体对比损失协同预测高质量的描述-掩码对，并实现每个掩码与其对应描述词元的细粒度对齐，从而深化用户对视频内容的理解。在两个基准数据集上的综合实验表明，SG-FSCFormer取得了卓越性能，能有效捕捉用户意图并生成符合用户需求的精准多模态输出。代码已开源：https://github.com/XuZhang1211/SG-FSCFormer。

---

