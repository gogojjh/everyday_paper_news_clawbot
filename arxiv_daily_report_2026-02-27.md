# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-02-27 08:02

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 6/20 篇提供

**🌟 Highlight**: 20 篇 | **📌 Poster**: 0 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. Are Foundation Models the Route to Full-Stack Transfer in Robotics?

- **作者**: Freek Stulp, Samuel Bustamante, João Silvério, Alin Albu-Schäffer, Jeannette Bohg, Shuran Song ⭐
  - **高亮作者**: Shuran Song
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.22001v1)
- **发表日期**: 2026-02-25
- **匹配关键词**: VLA
- **arXiv**: [2602.22001v1](http://arxiv.org/abs/2602.22001v1)
- **📥 PDF**: 已下载至本地 (`2602.22001v1_Are_Foundation_Models_the_Route_to_Full-Stack_Transfer_in_Robotics?.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 在人类与机器人领域，迁移学习发生在不同抽象层次——从高层次的语言迁移到低层次的运动技能迁移。本文系统梳理了基础模型与Transformer网络对这些不同层次迁移学习的影响，推动机器人技术比以往更接近"全栈迁移"的实现。从机器人迁移学习的视角审视大语言模型、视觉语言模型及视觉语言动作模型，使我们能够超越具体技术实现，聚焦迁移学习中反复出现的核心概念。我们还探讨了基础模型时代下机器人数据收集与迁移基准测试所面临的挑战。基础模型是否真能引领机器人实现全栈迁移？我们预期它们必将作为关键技术持续推动这一进程。

---

### 2. Humanizing Robot Gaze Shifts: A Framework for Natural Gaze Shifts in Humanoid Robots

- **作者**: Jingchao Wei, Jingkai Qin, Yuxiao Cao, Jingcheng Huang, Xiangrui Zeng, Min Li, Zhouping Yin
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.21983v1)
- **发表日期**: 2026-02-25
- **匹配关键词**: visual feedback, HRI
- **arXiv**: [2602.21983v1](http://arxiv.org/abs/2602.21983v1)
- **📥 PDF**: 已下载至本地 (`2602.21983v1_Humanizing_Robot_Gaze_Shifts_A_Framework_for_Natural_Gaze_Shifts_in_Humanoid_Robots.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 利用听觉与视觉反馈进行注意力重定向，是实现社交互动中自然视线转移的关键。然而，在开放场景的人机交互中，使人形机器人能够执行自然且符合情境的视线转移仍具挑战，因为这需要将认知注意力机制与仿生运动生成相结合。本研究提出机器人视线转移框架，将这两个组件整合为统一流程。该框架首先采用基于视觉-语言模型的视线推理管道，从多模态交互线索中推断符合情境的注视目标，确保与人类视线转移规律保持一致；其次引入条件向量量化变分自编码器模型，实现眼-头协调的视线转移运动生成，产生多样化且类人的视线转移行为。实验验证表明，该框架能有效复现类人的目标选择机制，并生成逼真、多样化的视线转移动作。

---

### 3. Dream-SLAM: Dreaming the Unseen for Active SLAM in Dynamic Environments

- **作者**: Xiangqi Meng, Pengxu Hou, Zhenjun Zhao, Javier Civera, Daniel Cremers, Hesheng Wang, Haoang Li ⭐
  - **高亮作者**: Daniel Cremers
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.21967v1)
- **发表日期**: 2026-02-25
- **匹配关键词**: localization and mapping, exploration, motion planning
- **arXiv**: [2602.21967v1](http://arxiv.org/abs/2602.21967v1)
- **📥 PDF**: 已下载至本地 (`2602.21967v1_Dream-SLAM_Dreaming_the_Unseen_for_Active_SLAM_in_Dynamic_Environments.pdf`)
- **🔓 开源**: CODE
- **中文摘要**: 除了同步定位与建图（SLAM）的核心任务外，主动SLAM还涉及生成机器人动作，以实现对未知环境的高效探索。然而，现有的主动SLAM流程主要受限于三个因素：首先，它们继承了所采用底层SLAM模块的固有局限；其次，其运动规划策略通常缺乏长远视野，偏向短视决策；第三，多数方法难以有效处理动态场景。为突破这些限制，本文提出了一种新颖的单目主动SLAM方法——Dream-SLAM，该方法基于对部分观测到的动态环境进行跨时空图像与语义合理结构的“梦境生成”。生成的跨时空图像将与实际观测数据融合，以降低噪声并弥补数据不完整性，从而实现更精确的相机姿态估计和更连贯的三维场景重建。此外，我们整合了“梦境生成”与观测得到的场景结构，以支持长时程规划，生成具有远见的轨迹，推动高效而全面的环境探索。在公开数据集及自采集数据集上的大量实验表明，Dream-SLAM在定位精度、建图质量与探索效率方面均优于现有先进方法。论文录用后源代码将公开提供。

---

### 4. Enhancing Cellular-enabled Collaborative Robots Planning through GNSS data for SAR Scenarios

- **作者**: Arnau Romero, Carmen Delgado, Jana Baguer, Raúl Suárez, Xavier Costa-Pérez
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.21899v1)
- **发表日期**: 2026-02-25
- **匹配关键词**: collaborative robot, exploration
- **arXiv**: [2602.21899v1](http://arxiv.org/abs/2602.21899v1)
- **📥 PDF**: 已下载至本地 (`2602.21899v1_Enhancing_Cellular-enabled_Collaborative_Robots_Planning_through_GNSS_data_for_SAR_Scenarios.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 基于蜂窝网络的协作机器人在搜救与应急响应中正变得至关重要。这些机器人高度依赖稳定的移动网络连接，在快速定位受困者、探索危险且难以进入的区域等任务中发挥着不可替代的作用。然而，其对电池供电的依赖以及对持续低延迟通信的需求，限制了其作业时间和移动性。为解决这一问题，并考虑到5G/6G网络不断演进的能力，我们提出了一种新型搜救框架，包含任务规划与任务执行两个阶段，并对机器人部署进行优化。通过综合考虑搜索区域大小、地形高程、机器人集群规模、通信影响的能耗特征、目标探索速率及响应时间等参数，我们的框架能够确定所需机器人的最小数量及其最优路径，以确保在移动网络上实现有效区域覆盖和及时的数据回传。研究结果揭示了轮式机器人与四足机器人在数量、探索面积和响应时间之间的权衡关系。此外，我们量化了地形高程数据对任务时间和能耗的影响，证明了将可能影响移动信号传播与连接的真实环境因素纳入搜救规划的优越性。该框架为利用新一代移动网络增强自主搜救行动提供了重要参考。

---

### 5. EndoDDC: Learning Sparse to Dense Reconstruction for Endoscopic Robotic Navigation via Diffusion Depth Completion

- **作者**: Yinheng Lin, Yiming Huang, Beilei Cui, Long Bai, Huxin Gao, Hongliang Ren, Jiewen Lai
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.21893v1)
- **发表日期**: 2026-02-25
- **匹配关键词**: 3D reconstruction, navigation, 3d reconstruction
- **arXiv**: [2602.21893v1](http://arxiv.org/abs/2602.21893v1)
- **📥 PDF**: 已下载至本地 (`2602.21893v1_EndoDDC_Learning_Sparse_to_Dense_Reconstruction_for_Endoscopic_Robotic_Navigation_via_Diffusion_Dept.pdf`)
- **🔓 开源**: CODE, GITHUB
  - 链接：https://github.com/yinheng-lin/EndoDDC.
- **中文摘要**: 精确的深度估计在内窥镜手术机器人导航中起着至关重要的作用，为三维重建和安全器械引导奠定了基础。预训练模型的微调高度依赖于带有精确深度标注的内窥镜手术数据集。虽然现有的自监督深度估计技术无需精确的深度标注，但其在纹理弱、光照多变环境中的性能会下降，导致重建稀疏且深度估计无效。利用稀疏深度图进行深度补全可以缓解这些问题并提高准确性。尽管深度补全技术在通用领域取得了进展，但其在内窥镜领域的应用仍然有限。为克服这些限制，我们提出了EndoDDC，一种内窥镜深度补全方法，该方法整合图像、稀疏深度信息与深度梯度特征，并通过扩散模型优化深度图，解决了内窥镜环境中纹理弱和光反射的问题。在两个公开可用的内窥镜数据集上进行的大量实验表明，我们的方法在深度准确性和鲁棒性方面均优于现有最先进模型。这证明了我们的方法在减少复杂内窥镜环境中视觉误差方面的潜力。我们的代码将在https://github.com/yinheng-lin/EndoDDC发布。

---

### 6. Joint-Aligned Latent Action: Towards Scalable VLA Pretraining in the Wild

- **作者**: Hao Luo, Ye Wang, Wanpeng Zhang, Haoqi Yuan, Yicheng Feng, Haiweng Xu, Sipeng Zheng, Zongqing Lu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.21736v1)
- **发表日期**: 2026-02-25
- **匹配关键词**: vision-language-action, VLA, vision-language-action model
- **arXiv**: [2602.21736v1](http://arxiv.org/abs/2602.21736v1)
- **📥 PDF**: 已下载至本地 (`2602.21736v1_Joint-Aligned_Latent_Action_Towards_Scalable_VLA_Pretraining_in_the_Wild.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 尽管已有进展，视觉-语言-动作模型（VLAs）仍受限于大规模多样化机器人数据的稀缺。人类操作视频虽提供了丰富的替代资源，但现有方法不得不在小规模精准标注数据集与海量追踪标签不可靠的野外视频之间做出取舍。我们提出JALA——一种学习联合对齐潜在动作的预训练框架。该方法绕过完整的视觉动态重建，转而学习与逆向动力学及真实动作双重对齐的预测性动作嵌入，从而构建出适用于异构人类数据学习的、具备状态转移感知与行为中心特性的潜在空间。我们通过UniHand-Mix数据集（包含750万视频片段，总时长超2000小时）融合实验室与野外视频素材，实现了该方法的规模化应用。实验表明，JALA在受控与非受控场景下均能生成更逼真的手部动作，显著提升了仿真与真实世界任务中的机器人操作性能。这些结果表明，联合对齐潜在动作为基于人类数据的VLA预训练提供了可扩展的路径。

---

### 7. DAGS-SLAM: Dynamic-Aware 3DGS SLAM via Spatiotemporal Motion Probability and Uncertainty-Aware Scheduling

- **作者**: Li Zhang, Yu-An Liu, Xijia Jiang, Conghao Huang, Danyang Li, Yanyong Zhang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.21644v1)
- **发表日期**: 2026-02-25
- **匹配关键词**: gaussian splatting, 3D gaussian splatting
- **arXiv**: [2602.21644v1](http://arxiv.org/abs/2602.21644v1)
- **📥 PDF**: 已下载至本地 (`2602.21644v1_DAGS-SLAM_Dynamic-Aware_3DGS_SLAM_via_Spatiotemporal_Motion_Probability_and_Uncertainty-Aware_Schedu.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 移动机器人与物联网设备需要在有限的计算与能耗预算下实现实时定位与密集重建。尽管三维高斯泼溅技术能够支持高效的密集SLAM系统，但动态物体与遮挡问题仍会降低跟踪与建图性能。现有动态3DGS-SLAM方案通常依赖计算量大的光流估计和逐帧分割，这在移动端部署中成本高昂，且在复杂光照条件下表现脆弱。本文提出DAGS-SLAM——一种动态感知的3DGS-SLAM系统，通过为每个高斯点维护时空运动概率状态，并借助不确定性感知调度器按需触发语义分析。该系统融合轻量级YOLO实例先验与几何线索来估计并时序更新运动概率，将运动概率传播至前端以实现动态感知的特征匹配选择，并通过运动概率引导的后端优化抑制动态伪影。在公开动态RGB-D基准测试上的实验表明，该系统在保持商用GPU实时吞吐量的同时，显著提升了重建质量与跟踪鲁棒性，通过减少语义调用次数实现了面向移动部署的实用化速度-精度平衡。

---

### 8. Self-Correcting VLA: Online Action Refinement via Sparse World Imagination

- **作者**: Chenyv Liu, Wentao Tan, Lei Zhu, Fengling Li, Jingjing Li, Guoli Yang, Heng Tao Shen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.21633v1)
- **发表日期**: 2026-02-25
- **匹配关键词**: VLA, vision-language-action, exploration
- **arXiv**: [2602.21633v1](http://arxiv.org/abs/2602.21633v1)
- **📥 PDF**: 已下载至本地 (`2602.21633v1_Self-Correcting_VLA_Online_Action_Refinement_via_Sparse_World_Imagination.pdf`)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/Kisaragi0/SC-VLA.
- **中文摘要**: 标准视觉-语言-动作（VLA）模型依赖拟合统计数据先验，限制了其对底层物理动态的稳健理解。强化学习通过探索增强物理基础，但通常依赖外部奖励信号，这些信号与智能体内部状态相互隔离。世界动作模型作为一种新兴范式，通过整合想象与控制实现预测性规划，但其依赖隐式上下文建模，缺乏明确的自我改进机制。为解决这些问题，我们提出自校正视觉-语言-动作模型（SC-VLA），通过稀疏想象内在引导动作优化，实现自我改进。我们首先设计稀疏世界想象模块，集成辅助预测头来预估当前任务进度与未来轨迹趋势，从而约束策略编码短期物理演化过程。随后引入在线动作优化模块，重塑基于进度的密集奖励，依据预测的稀疏未来状态调整轨迹方向。在仿真基准和真实场景的机器人操作任务评估中，SC-VLA实现了最先进的性能：相比最优基线方法，任务吞吐量最高，步骤数减少16%，成功率提升9%，真实世界实验性能增益达14%。代码已开源：https://github.com/Kisaragi0/SC-VLA。

---

### 9. ADM-DP: Adaptive Dynamic Modality Diffusion Policy through Vision-Tactile-Graph Fusion for Multi-Agent Manipulation

- **作者**: Enyi Wang, Wen Fan, Dandan Zhang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.21622v1)
- **发表日期**: 2026-02-25
- **匹配关键词**: diffusion policy
- **arXiv**: [2602.21622v1](http://arxiv.org/abs/2602.21622v1)
- **📥 PDF**: 已下载至本地 (`2602.21622v1_ADM-DP_Adaptive_Dynamic_Modality_Diffusion_Policy_through_Vision-Tactile-Graph_Fusion_for_Multi-Agen.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 多智能体机器人协同操作因需同时满足协调性、抓取稳定性及共享工作空间中的避碰要求而极具挑战。为应对这些挑战，我们提出自适应动态模态扩散策略（ADM-DP），该框架融合视觉、触觉及基于图结构（多智能体位姿）的模态实现协同控制。ADM-DP包含四项核心创新：首先，增强型视觉编码器通过特征线性调制（FiLM）融合RGB与点云特征以提升感知能力；其次，触觉引导抓取策略利用力敏电阻（FSR）反馈检测接触不足并触发抓取修正，从而增强抓取稳定性；第三，基于图的碰撞编码器利用多智能体共享的工具中心点（TCP）位置构建结构化运动学上下文，以保持空间感知并减少智能体间干扰；第四，自适应模态注意力机制（AMAM）根据任务场景动态调整模态权重，实现灵活融合。为提升可扩展性与模块化程度，采用解耦训练范式使智能体在共享空间信息的同时学习独立策略，在保持集体感知的同时降低智能体间相互依赖性。在七项多智能体任务测试中，ADM-DP相较前沿基线方法取得12-25%的性能提升。消融实验表明，该框架在需要多感官模态的任务中改进最为显著，验证了自适应融合策略的有效性，并证明其对多样化操作场景的鲁棒性。

---

### 10. LiLo-VLA: Compositional Long-Horizon Manipulation via Linked Object-Centric Policies

- **作者**: Yue Yang, Shuo Cheng, Yu Fang, Homanga Bharadhwaj, Mingyu Ding, Gedas Bertasius, Daniel Szafir
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.21531v1)
- **发表日期**: 2026-02-25
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2602.21531v1](http://arxiv.org/abs/2602.21531v1)
- **📥 PDF**: 已下载至本地 (`2602.21531v1_LiLo-VLA_Compositional_Long-Horizon_Manipulation_via_Linked_Object-Centric_Policies.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://yy-gx.github.io/LiLo-VLA/.
- **中文摘要**: 通用机器人必须掌握长时程操作，这类任务涉及在非结构化环境中进行多次运动结构变化（例如装配或拆卸物体）。虽然视觉-语言-动作模型具备掌握多样化原子技能的潜力，但它们在技能序列组合的复杂性上存在困难，且容易因环境敏感性引发连锁故障。为应对这些挑战，我们提出LiLo-VLA（关联局部视觉-语言-动作模型）——一个能够零样本泛化至全新长时程任务的模块化框架，且无需针对这些任务进行专门训练。我们的方法将运输与交互解耦：抵达模块负责全局运动，而交互模块采用以对象为中心的视觉-语言-动作模型来处理独立的目标物体，确保对无关视觉特征的鲁棒性及空间配置的不变性。关键在于，这种模块化设计通过动态重规划与技能复用实现了稳健的故障恢复，有效缓解了端到端方法中常见的连锁错误。我们构建了一个包含21项任务的仿真基准测试集，涵盖两大挑战性场景：LIBERO-Long++与Ultra-Long。在仿真测试中，LiLo-VLA实现了69%的平均成功率，较Pi0.5提升41%，较OpenVLA-OFT提升67%。此外，在8项真实世界长时程任务评估中，该系统达到85%的平均成功率。项目主页：https://yy-gx.github.io/LiLo-VLA/。

---

### 11. VLA Knows Its Limits

- **作者**: Haoxuan Wang, Gengyu Zhang, Yan Yan, Ramana Rao Kompella, Gaowen Liu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.21445v1)
- **发表日期**: 2026-02-24
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2602.21445v1](http://arxiv.org/abs/2602.21445v1)
- **📥 PDF**: 已下载至本地 (`2602.21445v1_VLA_Knows_Its_Limits.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 动作分块已成为基于流程的视觉-语言-动作模型的标准实践。然而，执行范围——即从每个预测块中执行的动作数量——的影响与选择仍未得到充分探索。本研究首先证明，改变执行范围会导致显著的性能差异：随着范围增大，性能先提升后下降。为探究原因，我们分析了基于流程的视觉-语言-动作模型中的交叉注意力与自注意力权重，揭示出两个关键现象：（一）块内动作对视觉语言标记的注意力模式固定，限制了环境变化的适应性；（二）起始与终止动作标记作为稳定锚点，形成潜在中心，中间动作围绕其组织。基于这些发现，我们将动作自注意力权重解释为模型预测极限的代理指标，并提出AutoHorizon——首个在测试时动态估计每个预测动作块执行范围的方法，以适应不断变化的感知条件。在模拟与真实机器人操作任务中，AutoHorizon表现出色，计算开销可忽略不计，并能泛化至多种任务及基于流程的模型。

---

### 12. Efficient Hierarchical Any-Angle Path Planning on Multi-Resolution 3D Grids

- **作者**: Victor Reijgwart, Cesar Cadena, Roland Siegwart, Lionel Ott ⭐
  - **高亮作者**: Cesar Cadena, Roland Siegwart
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.21174v1)
- **发表日期**: 2026-02-24
- **匹配关键词**: path planning, navigation
- **arXiv**: [2602.21174v1](http://arxiv.org/abs/2602.21174v1)
- **📥 PDF**: 已下载至本地 (`2602.21174v1_Efficient_Hierarchical_Any-Angle_Path_Planning_on_Multi-Resolution_3D_Grids.pdf`)
- **🔓 开源**: CODE
- **中文摘要**: 分层多分辨率体素映射方法因其能高效捕捉环境的占用与连通性信息，被广泛应用于大型复杂环境的表征。然而，当前广泛使用的路径规划方法（如采样法和轨迹优化法）并未充分利用这种显式的连通性信息，而基于搜索的方法（如A*算法）在大规模高分辨率地图中面临可扩展性问题。在许多应用场景中，欧几里得最短路径构成导航系统的基础。针对这类应用，任意角度规划方法通过连接障碍物顶点形成直线段来寻找最优路径，提供了简洁高效的解决方案。本文提出一种兼具任意角度规划器最优性与完备性的方法，通过利用多分辨率表征克服了基于搜索方法普遍存在的计算可处理性问题。在真实与合成环境中的大量实验表明，所提方法在求解质量与速度上均表现优异，甚至超越了基于采样的方法。本框架已开源，以促进机器人学与规划领域基于本研究开展进一步探索。

---

### 13. ActionReasoning: Robot Action Reasoning in 3D Space with LLM for Robotic Brick Stacking

- **作者**: Guangming Wang, Qizhen Ying, Yixiong Jing, Olaf Wysocki, Brian Sheil
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.21161v1)
- **发表日期**: 2026-02-24
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2602.21161v1](http://arxiv.org/abs/2602.21161v1)
- **📥 PDF**: 已下载至本地 (`2602.21161v1_ActionReasoning_Robot_Action_Reasoning_in_3D_Space_with_LLM_for_Robotic_Brick_Stacking.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 经典机器人系统通常依赖为受限环境设计的定制规划器。这些系统在受限环境中虽有效，但缺乏泛化能力，限制了具身人工智能和通用机器人的可扩展性。近年来数据驱动的视觉-语言-动作方法试图从大规模仿真和现实数据中学习策略。然而物理世界的连续动作空间远超语言符号的表征能力，仅靠扩展数据能否实现通用机器人智能尚不明确。为填补这一空白，我们提出ActionReasoning框架——一种基于大语言模型的显式动作推理系统，可为机器人操作生成符合物理规律且具有先验引导的决策。该框架利用大语言模型中已编码的物理先验与现实世界知识，并通过多智能体架构进行组织。我们在积木堆叠这一可验证案例中实例化了该框架，其中假设环境状态已被精确测量。环境状态经序列化后输入多智能体大语言模型框架，生成具有物理感知的动作规划。实验表明，所提出的多智能体大语言模型框架能实现稳定的积木摆放，同时将开发重心从底层领域特定编码转向高层工具调用与提示工程，凸显了其广泛泛化的潜力。本研究通过将物理推理与大语言模型相结合，为机器人操作中感知与执行的衔接提供了一种前景广阔的新途径。

---

### 14. HALO: A Unified Vision-Language-Action Model for Embodied Multimodal Chain-of-Thought Reasoning

- **作者**: Quanxin Shou, Fangqi Zhu, Shawn Chen, Puxin Yan, Zhengyang Yan, Yikun Miao, Xiaoyi Pang, Zicong Hong, Ruikai Shi, Hao Huang, Jie Zhang, Song Guo
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.21157v1)
- **发表日期**: 2026-02-24
- **匹配关键词**: vision-language-action, VLA, vision-language-action model
- **arXiv**: [2602.21157v1](http://arxiv.org/abs/2602.21157v1)
- **📥 PDF**: 已下载至本地 (`2602.21157v1_HALO_A_Unified_Vision-Language-Action_Model_for_Embodied_Multimodal_Chain-of-Thought_Reasoning.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型在机器人操作任务中展现出强大性能，但在长时程或分布外场景中常因缺乏显式的多模态推理机制以及对动作引发环境演变的预判能力而表现受限。近期研究尝试在VLA模型中引入文本思维链或视觉子目标预测以增强推理能力，但仍未能构建统一的人类式推理框架来实现文本推理、视觉前瞻与动作预测的协同。为此，我们提出HALO模型——一个支持具身多模态思维链（EM-CoT）推理的统一VLA框架，通过文本任务推理、细粒度视觉子目标预测及EM-CoT增强动作预测的序列化流程实现推理。我们采用混合专家Transformer架构实例化HALO，将语义推理、视觉前瞻与动作预测解耦至专用专家模块，同时保持跨模块的无缝协作。为实现大规模训练，我们开发了自动化流水线合成EM-CoT训练数据，并设计了精细化的训练方案。大量实验表明：（1）HALO在仿真与真实环境中均取得卓越性能，在RoboTwin基准测试中超越基线策略π_0达34.1%；（2）训练方案与EM-CoT设计的所有组件均能提升任务成功率；（3）在激进未见环境随机化条件下，HALO通过EM-CoT推理展现出强大的泛化能力。

---

### 15. Event-Aided Sharp Radiance Field Reconstruction for Fast-Flying Drones

- **作者**: Rong Zou, Marco Cannici, Davide Scaramuzza ⭐
  - **高亮作者**: Davide Scaramuzza
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.21101v1)
- **发表日期**: 2026-02-24
- **匹配关键词**: 3d reconstruction, neural radiance field, nerf, 3D reconstruction, exploration
- **arXiv**: [2602.21101v1](http://arxiv.org/abs/2602.21101v1)
- **📥 PDF**: 已下载至本地 (`2602.21101v1_Event-Aided_Sharp_Radiance_Field_Reconstruction_for_Fast-Flying_Drones.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 在电池续航有限的条件下，高速飞行机器人有望实现快速巡检，在基础设施检查、地形勘探及搜救等领域具有直接应用价值。然而高速飞行会导致图像出现严重运动模糊，并引发位姿估计的显著漂移与噪声，这使得神经辐射场（NeRF）的稠密三维重建面临特殊挑战，因为该方法对此类退化现象极为敏感。本研究提出一种统一框架，通过融合异步事件流与运动模糊图像帧，实现从敏捷无人机飞行中重建高保真辐射场。通过将事件-图像融合嵌入NeRF优化过程，并联合利用事件与图像模态精化基于事件的视觉惯性里程计先验信息，本方法无需真实轨迹监督即可重建清晰辐射场与精确相机轨迹。我们在合成数据与高速飞行无人机采集的真实场景序列上验证了该方法的有效性。即使在无人机高速动态飞行导致RGB图像帧严重运动模糊、位姿先验信息不可靠的情况下，本方法仍能重建高保真辐射场并保留精细场景细节，在真实数据上相比现有最优方法实现超过50%的性能提升。

---

### 16. Notes-to-Self: Scratchpad Augmented VLAs for Memory Dependent Manipulation Tasks

- **作者**: Sanjay Haresh, Daniel Dijkman, Apratim Bhattacharyya, Roland Memisevic
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.21013v1)
- **发表日期**: 2026-02-24
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2602.21013v1](http://arxiv.org/abs/2602.21013v1)
- **📥 PDF**: 已下载至本地 (`2602.21013v1_Notes-to-Self_Scratchpad_Augmented_VLAs_for_Memory_Dependent_Manipulation_Tasks.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 许多灵巧操作任务本质上具有非马尔可夫特性，然而在近期兴起的视觉-语言-动作范式研究中，这一事实却鲜有关注。尽管现有VLA模型成功地将互联网规模的语义理解引入机器人领域，但它们主要是"无状态"的，难以应对依赖记忆的长时程任务。本研究探索通过引入语言草稿本为VLA模型赋予时空记忆能力。该草稿本能够记录任务特定信息（如物体位置），使模型得以追踪任务计划并监控子目标完成进度。我们在ClevrSkills环境中的记忆依赖任务子集、MemoryBench测试平台以及具有挑战性的真实世界抓放任务上评估该方法。实验表明，语言草稿本的引入显著提升了非循环模型与循环模型在这些任务上的泛化性能。

---

### 17. Task-oriented grasping for dexterous robots using postural synergies and reinforcement learning

- **作者**: Dimitrios Dimou, José Santos-Victor, Plinio Moreno
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.20915v1)
- **发表日期**: 2026-02-24
- **匹配关键词**: exploration
- **arXiv**: [2602.20915v1](http://arxiv.org/abs/2602.20915v1)
- **📥 PDF**: 已下载至本地 (`2602.20915v1_Task-oriented_grasping_for_dexterous_robots_using_postural_synergies_and_reinforcement_learning.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 本文针对仿人机器人的任务导向抓取问题展开研究，重点探讨如何使其符合人类社交规范并满足特定任务需求。现有方法虽采用多种开环与闭环控制策略，但缺乏能够同时抓取多个物体并兼顾下游任务约束的端到端解决方案。我们提出一种基于强化学习的任务导向抓取增强方法，以智能体的抓取后意图为优先考量。通过从ContactPose数据集中提取人类抓取偏好，并基于变分自编码器训练手部协同模型以模仿参与者的抓取动作，我们构建了能够同时抓取多个物体且兼顾不同任务特定抓取后意图的智能体训练体系。通过将人类抓取行为的数据驱动洞察与强化学习提供的探索式学习相结合，我们得以开发出具备情境感知操作能力的仿人机器人，为人本环境中的协同作业提供技术支持。

---

### 18. World Guidance: World Modeling in Condition Space for Action Generation

- **作者**: Yue Su, Sijin Chen, Haixin Shi, Mingyu Liu, Zhengshen Zhang, Ningyuan Huang, Weiheng Zhong, Zhengbang Zhu, Yuxiao Liu, Xihui Liu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.22010v1)
- **发表日期**: 2026-02-25
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2602.22010v1](http://arxiv.org/abs/2602.22010v1)
- **📥 PDF**: 已下载至本地 (`2602.22010v1_World_Guidance_World_Modeling_in_Condition_Space_for_Action_Generation.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://selen-suyue.github.io/WoGNet/
- **中文摘要**: 利用未来观测建模来促进动作生成，为提升视觉-语言-动作（VLA）模型能力提供了前景广阔的研究路径。然而，现有方法难以在维持高效、可预测的未来表征与保留足够细粒度信息以指导精确动作生成之间取得平衡。针对这一局限，我们提出WoG（世界引导）框架，通过将未来观测注入动作推理流程，将其映射为紧凑的条件表征。随后训练VLA模型同步预测这些压缩条件与未来动作，从而在条件空间内实现面向动作推理的有效世界建模。实验表明，对此条件空间的建模与预测不仅能促进细粒度动作生成，还展现出卓越的泛化能力，并能从海量人类操作视频中高效学习。在仿真与真实环境中的大量实验验证了本方法显著优于现有基于未来预测的方法。项目页面详见：https://selen-suyue.github.io/WoGNet/

---

### 19. Geometry-as-context: Modulating Explicit 3D in Scene-consistent Video Generation to Geometry Context

- **作者**: JiaKui Hu, Jialun Liu, Liying Yang, Xinliang Zhang, Kaiwen Li, Shuang Zeng, Yuanwei Li, Haibin Huang, Chi Zhang, Yanye Lu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.21929v1)
- **发表日期**: 2026-02-25
- **匹配关键词**: 3D reconstruction, 3d reconstruction
- **arXiv**: [2602.21929v1](http://arxiv.org/abs/2602.21929v1)
- **📥 PDF**: 已下载至本地 (`2602.21929v1_Geometry-as-context_Modulating_Explicit_3D_in_Scene-consistent_Video_Generation_to_Geometry_Context.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 场景一致性视频生成旨在根据相机轨迹创建探索三维场景的视频。先前方法依赖带有外部记忆的视频生成模型来保持一致性，或采用迭代式三维重建与修复技术，这些方法在推理过程中会因中间输出错误、不可微分流程及模型分离等问题导致误差累积。为突破这些局限，我们提出"几何作为上下文"方法。该方法通过自回归相机控制视频生成模型迭代执行以下步骤：(1) 估计当前视角下三维重建所需的几何信息，(2)模拟并还原三维场景渲染的新视角图像。在此多任务框架下，我们开发了相机门控注意力模块，以增强模型有效利用相机位姿的能力。在训练阶段，系统利用文本上下文判断应生成几何图像还是RGB图像。为确保模型在推理阶段仅生成RGB输出，我们在交错排列的文本-图像-几何训练序列中随机丢弃几何上下文。该方法已在单向及往返轨迹的场景视频生成任务中得到验证，结果表明其在保持场景一致性和相机控制方面优于现有方法。

---

### 20. Joint Shadow Generation and Relighting via Light-Geometry Interaction Maps

- **作者**: Shan Wang, Peixia Li, Chenchen Xu, Ziang Cheng, Jiayu Yang, Hongdong Li, Pulak Purkait
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.21820v1)
- **发表日期**: 2026-02-25
- **匹配关键词**: 3D reconstruction, 3d reconstruction
- **arXiv**: [2602.21820v1](http://arxiv.org/abs/2602.21820v1)
- **📥 PDF**: 已下载至本地 (`2602.21820v1_Joint_Shadow_Generation_and_Relighting_via_Light-Geometry_Interaction_Maps.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出光几何交互图这一新型表征方法，通过单目深度信息编码光感知遮挡关系。与需要完整三维重建的光线追踪技术不同，光几何交互图能够基于现成的2.5维深度图预测，可靠且精确地捕捉关键的光影交互作用。该方法将光照方向与几何结构显式关联，为生成模型提供了受物理学启发的约束先验。缺乏此类先验的模型常会产生悬浮阴影、光照不一致及不合理阴影几何等问题。基于此表征，我们构建了阴影生成与重照明的联合处理流程——突破以往将二者视为独立任务的局限——捕捉光照与阴影的内在耦合关系，这对建模间接光照效应至关重要。通过将光几何交互图嵌入桥接匹配生成架构，我们有效降低了歧义性并强化了物理一致的光影推理。为支持高效训练，我们构建了首个面向联合阴影与重照明任务的大规模基准数据集，涵盖反射、透明材质及复杂互反射现象。实验表明，该方法在合成图像与真实图像上均实现了真实感与一致性的显著提升。光几何交互图由此搭建起几何渲染与生成建模的桥梁，为实现高效且物理一致的阴影生成与重照明提供了新途径。

---

