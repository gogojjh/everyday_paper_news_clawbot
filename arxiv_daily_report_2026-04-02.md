# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-04-02 08:11

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 6/20 篇提供

**🌟 Highlight**: 16 篇 | **📌 Poster**: 4 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. DIAL: Decoupling Intent and Action via Latent World Modeling for End-to-End VLA

- **作者**: Yi Chen, Yuying Ge, Hui Zhou, Mingyu Ding, Yixiao Ge, Xihui Liu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.29844v1)
- **发表日期**: 2026-03-31
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2603.29844v1](http://arxiv.org/abs/2603.29844v1)
- **📥 PDF**: 已下载至本地 (`2603.29844v1_DIAL_Decoupling_Intent_and_Action_via_Latent_World_Modeling_for_End-to-End_VLA.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉语言模型（VLM）的预训练显著加速了视觉-语言-动作（VLA）模型的发展。然而，现有大多数端到端VLA模型主要将VLM视为多模态编码器，直接将视觉-语言特征映射为底层动作。这种范式未能充分利用VLM在高层决策中的潜力，并导致训练不稳定，常常削弱其丰富的语义表征能力。为突破这些局限，我们提出了DIAL框架，通过可微分的潜在意图瓶颈桥接高层决策与底层运动执行。具体而言，基于VLM的System-2在VLM原生特征空间内合成潜在视觉前瞻，实现潜在世界建模；这种前瞻显式编码意图并构成结构化瓶颈。随后，轻量级System-1策略通过潜在逆动力学，将预测意图与当前观测共同解码为精确的机器人动作。为确保优化稳定性，我们采用两阶段训练范式：解耦预热阶段中，System-2学习在统一特征空间内预测潜在未来状态，而System-1在真实未来状态引导下学习运动控制；随后进行无缝的端到端联合优化。该方法使动作感知梯度能以受控方式优化VLM主干网络，同时保留预训练知识。在RoboCasa GR1桌面基准测试中的大量实验表明，DIAL以仅需先前方法十分之一的示范数据量实现了最优性能，确立了新的技术标杆。此外，通过融合异构人类示范数据，DIAL学习了物理可验证的操作先验知识，并在人形机器人实际部署中，对未见物体及新场景配置展现出强大的零样本泛化能力。

---

### 2. CLaD: Planning with Grounded Foresight via Cross-Modal Latent Dynamics

- **作者**: Andrew Jeong, Jaemin Kim, Sebin Lee, Sung-Eui Yoon
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.29409v1)
- **发表日期**: 2026-03-31
- **匹配关键词**: diffusion policy, VLA
- **arXiv**: [2603.29409v1](http://arxiv.org/abs/2603.29409v1)
- **📥 PDF**: 已下载至本地 (`2603.29409v1_CLaD_Planning_with_Grounded_Foresight_via_Cross-Modal_Latent_Dynamics.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 机器人操作涉及运动学与语义状态的转换，这两种转换通过底层动作天然耦合。然而，现有方法仅在语义空间或潜在空间中进行规划，未能显式对齐这两种跨模态转换。为此，我们提出CLaD框架，通过非对称交叉注意力机制建模本体感知状态与语义状态在动作作用下的协同演化过程，使运动学转换能够查询语义转换。CLA采用指数移动平均目标编码器和辅助重建损失的自监督目标来预测基于现实的潜在状态前瞻，既防止表征坍缩，又将预测锚定于可观测状态。通过观测信息调制的前瞻状态被用于条件化扩散策略以生成动作。在LIBERO-LONG基准测试中，CLaD以显著更少的参数量实现94.7%的成功率，性能与大型视觉语言动作模型相当。

---

### 3. Efficient Camera Pose Augmentation for View Generalization in Robotic Policy Learning

- **作者**: Sen Wang, Huaiyi Dong, Jingyi Tian, Jiayi Li, Zhuo Yang, Tongtong Cao, Anlin Chen, Shuang Wu, Le Wang, Sanping Zhou
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.29192v1)
- **发表日期**: 2026-03-31
- **匹配关键词**: gaussian splatting, 3D gaussian splatting
- **arXiv**: [2603.29192v1](http://arxiv.org/abs/2603.29192v1)
- **📥 PDF**: 已下载至本地 (`2603.29192v1_Efficient_Camera_Pose_Augmentation_for_View_Generalization_in_Robotic_Policy_Learning.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 当前以二维为中心的视觉运动策略在新视角泛化方面存在明显不足，因其对静态观测的依赖阻碍了在未见视角下保持动作映射的一致性。为此，我们提出GenSplat——一种前馈式三维高斯溅射框架，通过新颖视角渲染促进视角泛化的策略学习。GenSplat采用置换等变架构，在单次前向传播中从稀疏未校准输入重建高保真三维场景。为确保结构完整性，我们设计了三维先验蒸馏策略，对三维高斯溅射优化过程进行正则化，避免纯光度监督中常见的几何塌陷问题。通过从这些稳定的三维表征中渲染多样化合成视角，我们在训练过程中系统性地扩展了观测流形。这种增强迫使策略将其决策建立在底层三维结构之上，从而确保在基线方法严重失效的剧烈空间扰动下仍能实现鲁棒执行。

---

### 4. LatentPilot: Scene-Aware Vision-and-Language Navigation by Dreaming Ahead with Latent Visual Reasoning

- **作者**: Haihong Hao, Lei Chen, Mingfei Han, Changlin Li, Dong An, Yuqiang Yang, Zhihui Li, Xiaojun Chang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.29165v1)
- **发表日期**: 2026-03-31
- **匹配关键词**: vision-and-language navigation, VLN, navigation
- **arXiv**: [2603.29165v1](http://arxiv.org/abs/2603.29165v1)
- **📥 PDF**: 已下载至本地 (`2603.29165v1_LatentPilot_Scene-Aware_Vision-and-Language_Navigation_by_Dreaming_Ahead_with_Latent_Visual_Reasonin.pdf`)
- **🔓 开源**: PROJECT_PAGE
- **中文摘要**: 现有视觉语言导航模型主要基于过去和当前的视觉观测进行推理，而基本忽略了由动作引发的未来视觉动态变化。这导致它们往往难以有效理解动作与视觉世界变化之间的因果关系，从而限制了稳健的决策能力。相比之下，人类能够利用动作动态因果关系来想象近期未来，这增强了对环境的理解并优化了导航选择。受此能力启发，我们提出LatentPilot这一新范式，该范式在训练阶段利用未来观测作为宝贵数据源来学习动作条件化的视觉动态，同时在推理阶段无需访问未来帧。具体而言，我们设计了一种飞轮式训练机制：通过迭代收集在线策略轨迹并重新训练模型以更好地匹配智能体行为分布，当智能体偏离过度时触发专家接管机制。LatentPilot进一步在无显式监督的情况下学习视觉潜在标记；这些潜在标记在连续潜在空间中进行全局注意力计算，并跨步骤传递，既作为当前输出又作为下一时刻输入，从而使智能体能够预演未来并推理动作将如何影响后续观测。在R2R-CE、RxR-CE和R2R-PE基准测试中取得新的最优性能，跨多样环境的真实机器人测试验证了LatentPilot对场景中环境-动作动态关系的卓越理解能力。项目页面：https://abdd.top/latentpilot/

---

### 5. FocusVLA: Focused Visual Utilization for Vision-Language-Action Models

- **作者**: Yichi Zhang, Weihao Yuan, Yizhuo Zhang, Xidong Zhang, Jia Wan
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.28740v1)
- **发表日期**: 2026-03-30
- **匹配关键词**: vision-language-action model, VLA, vision-language-action
- **arXiv**: [2603.28740v1](http://arxiv.org/abs/2603.28740v1)
- **📥 PDF**: 已下载至本地 (`2603.28740v1_FocusVLA_Focused_Visual_Utilization_for_Vision-Language-Action_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作模型通过将策略建立在丰富的视觉-语言信息之上，提升了动作生成的质量。然而，当前的自回归策略面临三个瓶颈：(1) 架构偏差导致模型忽视视觉细节，(2) 过多的视觉标记使注意力难以聚焦于正确区域，(3) 任务无关的视觉信息引入大量噪声——这些问题共同严重影响了动作生成的质量。本文研究了如何有效利用不同视觉表征进行动作生成。为此，我们首先通过实验验证了上述问题，并证明视觉-语言-动作模型的性能主要受限于视觉信息的利用方式，而非视觉表征的质量。基于这些发现，我们提出了FocusVLA这一新范式，通过引导模型关注任务相关的视觉区域，有效连接视觉与动作。具体而言，我们首先提出模态级联注意力机制以消除捷径路径，从而迫使视觉-语言-动作模型依赖任务相关的视觉细节生成动作。此外，我们提出聚焦注意力机制，动态选择任务相关的视觉片段以控制信息量，同时显式调节其影响以抑制任务无关的噪声。在模拟和真实机器人基准测试上的大量实验表明，FocusVLA不仅能有效利用视觉细节执行灵巧操作，还能显著提升多种任务的性能并加速收敛过程。

---

### 6. Pandora: Articulated 3D Scene Graphs from Egocentric Vision

- **作者**: Alan Yu, Yun Chang, Christopher Xie, Luca Carlone ⭐
  - **高亮作者**: Luca Carlone
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.28732v1)
- **发表日期**: 2026-03-30
- **匹配关键词**: mobile manipulation, scene graph
- **arXiv**: [2603.28732v1](http://arxiv.org/abs/2603.28732v1)
- **📥 PDF**: 已下载至本地 (`2603.28732v1_Pandora_Articulated_3D_Scene_Graphs_from_Egocentric_Vision.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 机器人建图系统通常基于机器人自身的传感器和摄像头构建度量-语义场景表征。然而，这种"第一人称"地图因机器人本体结构或技能限制而存在固有缺陷，可能导致环境中的许多方面未被探索。例如，机器人可能无法打开抽屉或触及壁柜。从这个意义上说，地图表征并不完整，需要能力更强的机器人来填补空白。我们通过利用人类佩戴Project Aria眼镜自然探索场景时捕获的自我中心数据来缩小现有方法的盲区，为将人类对可动部件的认知直接迁移至任何可部署机器人提供了途径。实验证明，通过简单启发式方法，利用自我中心数据重建的可动部件模型质量可与基于其他输入模态的最先进方法相媲美。我们还展示了如何将这些模型整合到3D场景图表征中，从而提升对物体动态及物体-容器关系的理解。最后，我们通过波士顿动力Spot机器人执行移动操控任务的案例，验证了这些可动3D场景图能增强机器人能力——仅以3D场景图为输入，机器人即可成功定位并取出隐藏的目标物品。

---

### 7. DRIVE-Nav: Directional Reasoning, Inspection, and Verification for Efficient Open-Vocabulary Navigation

- **作者**: Maoguo Gao, Zejun Zhu, Zhiming Sun, Zhengwei Ma, Longze Yuan, Zhongjing Ma, Zhigang Gao, Jinhui Zhang, Suli Zou
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.28691v1)
- **发表日期**: 2026-03-30
- **匹配关键词**: exploration, navigation
- **arXiv**: [2603.28691v1](http://arxiv.org/abs/2603.28691v1)
- **📥 PDF**: 已下载至本地 (`2603.28691v1_DRIVE-Nav_Directional_Reasoning,_Inspection,_and_Verification_for_Efficient_Open-Vocabulary_Navigati.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://coolmaoguo.github.io/drive-nav-page/
- **中文摘要**: 开放词汇目标导航（OVON）要求具身智能体在未知环境中定位语言指定的目标。现有零样本方法通常在局部观测下对密集边界点进行推理，导致路径选择不稳定、重复访问和无效动作开销。本文提出DRIVE-Nav结构化框架，该框架围绕持久性方向而非原始边界组织探索。通过更完整地检查已遇到的方向，并将后续决策限制在前向240度视野范围内仍相关的方向上，DRIVE-Nav减少了冗余访问并提升了路径效率。该框架从加权快速行进法（FMM）路径中提取并追踪方向候选，维护代表性视角进行语义检查，结合视觉语言引导的提示增强与跨帧验证以提高语义定位可靠性。在HM3D-OVON、HM3Dv2和MP3D数据集上的实验表明，该方法在整体性能与路径效率方面均取得显著提升。在HM3D-OVON数据集上，DRIVE-Nav实现了50.2%的成功率（SR）和32.6%的路径长度加权成功率（SPL），较先前最佳方法分别提升1.9% SR和5.6% SPL。该方法同时在HM3Dv2和MP3D数据集上取得最优SPL指标，并可迁移至实体人形机器人平台。实际场景部署验证了其有效性。项目页面：https://coolmaoguo.github.io/drive-nav-page/

---

### 8. ManipArena: Comprehensive Real-world Evaluation of Reasoning-Oriented Generalist Robot Manipulation

- **作者**: Yu Sun, Meng Cao, Ping Yang, Rongtao Xu, Yunxiao Yan, Runze Xu, Liang Ma, Roy Gan, Andy Zhai, Qingxuan Chen, Zunnan Xu, Hao Wang, Jincheng Yu, Lucy Liang, Qian Wang, Ivan Laptev, Ian D Reid, Xiaodan Liang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.28545v1)
- **发表日期**: 2026-03-30
- **匹配关键词**: mobile manipulation, VLA, vision-language-action
- **arXiv**: [2603.28545v1](http://arxiv.org/abs/2603.28545v1)
- **📥 PDF**: 已下载至本地 (`2603.28545v1_ManipArena_Comprehensive_Real-world_Evaluation_of_Reasoning-Oriented_Generalist_Robot_Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作模型与世界模型已成为通用机器人智能领域备受关注的研究范式，但其发展因缺乏反映真实部署场景的可靠评估标准而受限。现有基准测试大多以仿真环境为核心，虽具备可控性优势，却难以捕捉由感知噪声、复杂接触动力学、硬件限制及系统延迟导致的现实鸿沟。此外，分散在不同机器人平台上的现实世界评估阻碍了公平可复现的比较研究。为应对这些挑战，我们提出ManipArena标准化评估框架，旨在构建仿真与真实执行的桥梁。该框架涵盖20类多样化任务与10,812条专家示范轨迹，聚焦需要语义与空间推理的认知型操作任务，通过受控分布外设置支持多层次泛化能力评估，并突破桌面场景局限纳入长时程移动操作任务。该框架进一步提供丰富的传感诊断数据（包括底层运动信号），以及通过高精度三维扫描构建的同步虚实环境。这些特性共同为视觉-语言-动作模型与世界模型方法提供了公平、真实且可复现的评估体系，为具身智能系统的诊断与演进奠定了可扩展的基础。

---

### 9. Tele-Catch: Adaptive Teleoperation for Dexterous Dynamic 3D Object Catching

- **作者**: Weiguang Zhao, Junting Dong, Rui Zhang, Kailin Li, Qin Zhao, Kaizhu Huang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.28427v1)
- **发表日期**: 2026-03-30
- **匹配关键词**: diffusion policy
- **arXiv**: [2603.28427v1](http://arxiv.org/abs/2603.28427v1)
- **📥 PDF**: 已下载至本地 (`2603.28427v1_Tele-Catch_Adaptive_Teleoperation_for_Dexterous_Dynamic_3D_Object_Catching.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 遥操作是将人类灵巧性转移至机器人的关键范式，然而现有研究多聚焦于初始静止的物体操作，如抓取或操控。动态物体捕捉——即物体在接触前处于运动状态的任务——仍缺乏深入探索。纯遥操作在此类任务中常因时机、姿态和力控误差而失败，凸显了需要将人类输入与自主策略相结合的分级自主控制机制。为此，我们提出Tele-Catch，一个面向动态物体捕捉的灵巧手遥操作系统框架。其核心是DAIM机制，该动态感知自适应集成系统通过将基于数据手套的遥操作信号融入扩散策略去噪过程，实现了人机协同的分级自主控制，并能根据交互物体状态自适应调节控制策略。为提升策略鲁棒性，我们提出DP-U3R方法，将点云观测中无监督几何表征融入扩散策略学习，实现几何感知的决策制定。大量实验表明，Tele-Catch在动态捕捉任务中显著提升了精度与鲁棒性，同时在不同灵巧手形态及未见过的物体类别上均展现出持续的性能增益。

---

### 10. OmniRoam: World Wandering via Long-Horizon Panoramic Video Generation

- **作者**: Yuheng Liu, Xin Lin, Xinke Li, Baihan Yang, Chen Wang, Kalyan Sunkavalli, Yannick Hold-Geoffroy, Hao Tan, Kai Zhang, Xiaohui Xie, Zifan Shi, Yiwei Hu ⭐
  - **高亮作者**: Chen Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.30045v1)
- **发表日期**: 2026-03-31
- **匹配关键词**: 3D reconstruction, 3d reconstruction
- **arXiv**: [2603.30045v1](http://arxiv.org/abs/2603.30045v1)
- **📥 PDF**: 已下载至本地 (`2603.30045v1_OmniRoam_World_Wandering_via_Long-Horizon_Panoramic_Video_Generation.pdf`)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/yuhengliu02/OmniRoam.
- **中文摘要**: 近年来，利用视频生成模型进行场景建模的研究兴趣日益增长。然而，现有方法大多依赖透视视频模型，仅能合成场景的有限观测视角，导致完整性与全局一致性问题。我们提出OmniRoam——一个可控的全景视频生成框架，该框架充分利用全景表征在单帧场景覆盖上的丰富性及其固有的长时空间与时间一致性，实现了长时程场景漫游。我们的框架首先通过预览阶段，利用轨迹控制视频生成模型从给定输入图像或视频快速生成场景概览；随后在优化阶段，将该视频进行时间延伸与空间上采样，生成长时程、高分辨率的视频，从而实现高保真度的虚拟世界漫游。为训练模型，我们构建了两个包含合成与实拍视频的全景视频数据集。实验表明，无论在定性还是定量评估中，我们的框架在视觉质量、可控性及长时场景一致性方面均持续优于现有先进方法。我们进一步展示了该框架的多种扩展应用，包括实时视频生成与三维重建。代码已开源：https://github.com/yuhengliu02/OmniRoam。

---

### 11. GRVS: a Generalizable and Recurrent Approach to Monocular Dynamic View Synthesis

- **作者**: Thomas Tanay, Mohammed Brahimi, Michal Nazarczuk, Qingwen Zhang, Sibi Catley-Chandar, Arthur Moreau, Zhensong Zhang, Eduardo Pérez-Pellitero
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.29734v1)
- **发表日期**: 2026-03-31
- **匹配关键词**: gaussian splatting
- **arXiv**: [2603.29734v1](http://arxiv.org/abs/2603.29734v1)
- **📥 PDF**: 已下载至本地 (`2603.29734v1_GRVS_a_Generalizable_and_Recurrent_Approach_to_Monocular_Dynamic_View_Synthesis.pdf`)
- **🔓 开源**: MODEL
- **中文摘要**: 从动态场景的单目视频中合成新视角仍是一个具有挑战性的问题。基于显式运动先验优化4D表示的场景特定方法在高度动态区域往往失效，因为这些区域难以利用多视角信息。而将相机控制集成到大型预训练模型中的扩散方法虽能生成视觉上合理的视频，却常出现静态与动态区域间的几何不一致性。这两类方法都需要大量计算资源。基于通用化静态新视角合成模型的成功经验，我们将其框架适配于动态输入，并提出包含两个关键组件的新模型：(1) 实现输入与目标视频间无界异步映射的循环机制；(2) 通过对动态输入进行高效平面扫描，解耦相机与场景运动，实现精细的六自由度相机控制。我们在UCSD数据集和Kubric-4D-dyn数据集上训练并评估模型——后者是新型单目动态数据集，其序列更长、分辨率更高，且场景动态比现有数据集更复杂。实验表明，在重建静态与动态区域的精细几何细节方面，我们的模型优于四种基于高斯泼溅的场景特定方法以及两种基于扩散的方法。

---

### 12. AA-Splat: Anti-Aliased Feed-forward Gaussian Splatting

- **作者**: Taewoo Suh, Sungpyo Kim, Jongmin Park, Munchurl Kim
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.29394v1)
- **发表日期**: 2026-03-31
- **匹配关键词**: gaussian splatting, 3D gaussian splatting, 3D reconstruction, 3d reconstruction
- **arXiv**: [2603.29394v1](http://arxiv.org/abs/2603.29394v1)
- **📥 PDF**: 已下载至本地 (`2603.29394v1_AA-Splat_Anti-Aliased_Feed-forward_Gaussian_Splatting.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 前馈式三维高斯溅射（FF-3DGS）已成为稀疏视角三维重建与新视角合成（NVS）领域快速且鲁棒的解决方案。然而，现有FF-3DGS方法基于不正确的屏幕空间扩张滤波器，在分布外采样率下渲染时会产生严重伪影。我们首次提出名为AA-Splat的FF-3DGS模型，实现在任意分辨率下的鲁棒抗锯齿渲染。AA-Splat采用不透明度平衡的带限设计，该设计融合两大核心组件：通过三维带限后置滤波器将多视角最大频率约束整合至前馈重建流程，有效对三维场景表征进行带限处理并消除退化高斯分布；采用不透明度平衡机制无缝集成所有像素对齐的高斯基元至渲染流程，补偿扩张后高斯基元间重叠度的增加。实验表明，在4倍至1/4倍的所有分辨率范围内，AA-Splat相较于前沿基线方法DepthSplat，其新视角合成性能平均获得5.4~7.5dB的峰值信噪比提升。相关代码将公开提供。

---

### 13. MotionScale: Reconstructing Appearance, Geometry, and Motion of Dynamic Scenes with Scalable 4D Gaussian Splatting

- **作者**: Haoran Zhou, Gim Hee Lee
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.29296v1)
- **发表日期**: 2026-03-31
- **匹配关键词**: gaussian splatting, neural rendering
- **arXiv**: [2603.29296v1](http://arxiv.org/abs/2603.29296v1)
- **📥 PDF**: 已下载至本地 (`2603.29296v1_MotionScale_Reconstructing_Appearance,_Geometry,_and_Motion_of_Dynamic_Scenes_with_Scalable_4D_Gauss.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://hrzhou2.github.io/motion-scale-web/.
- **中文摘要**: 从单目视频中实现动态4D场景的真实重建对于理解物理世界至关重要。尽管神经渲染领域近期取得进展，现有方法在复杂环境中仍难以恢复精确的3D几何结构和时间一致的运动轨迹。为应对这些挑战，我们提出MotionScale——一种4D高斯泼溅框架，该框架能高效扩展至大场景与长时序，同时保持高保真的结构与运动一致性。我们的方法核心在于通过集群中心基变换参数化的可扩展运动场，该运动场能自适应扩展以捕捉多样且持续演变的运动模式。为确保长时间序列的稳健重建，我们引入包含两个解耦传播阶段的渐进式优化策略：1）背景扩展阶段，适应新可见区域、优化相机位姿并显式建模瞬态阴影；2）前景传播阶段，通过专门的三阶段精修流程强化运动一致性。在具有挑战性的真实场景基准测试中，大量实验表明MotionScale在重建质量和时序稳定性方面均显著优于现有先进方法。项目页面：https://hrzhou2.github.io/motion-scale-web/。

---

### 14. LightHarmony3D: Harmonizing Illumination and Shadows for Object Insertion in 3D Gaussian Splatting

- **作者**: Tianyu Huang, Zhenyang Ren, Zhenchen Wan, Jiyang Zheng, Wenjie Wang, Runnan Chen, Mingming Gong, Tongliang Liu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.29209v1)
- **发表日期**: 2026-03-31
- **匹配关键词**: gaussian splatting, 3D gaussian splatting
- **arXiv**: [2603.29209v1](http://arxiv.org/abs/2603.29209v1)
- **📥 PDF**: 已下载至本地 (`2603.29209v1_LightHarmony3D_Harmonizing_Illumination_and_Shadows_for_Object_Insertion_in_3D_Gaussian_Splatting.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 三维高斯溅射（3DGS）能够实现对场景几何与外观的高保真重建。基于这一能力，将外部网格对象插入重建的3DGS场景中，可为增强现实/虚拟现实（AR/VR）、虚拟场景布置及数字内容创作等沉浸式应用实现交互式编辑与内容增强。然而，为网格插入实现物理一致的光照与阴影仍具挑战性，因为这需要精确的场景光照估计与多视角一致渲染。针对这一挑战，我们提出了LightHarmony3D——一个在3DGS场景中实现光照一致网格插入的创新框架。该方法的核心理念是我们提出的生成模块，该模块通过单次前向传播即可在插入位置预测完整的360度高动态范围环境贴图。通过利用生成先验而非迭代优化，我们的方法能高效捕捉场景主导光照，为插入网格提供基于物理原理的着色与阴影效果，同时保持多视角一致性。此外，我们首次针对3DGS中的网格插入任务构建了专用基准测试集，为评估光照一致性与照片真实感提供了标准化框架。在多个真实世界重建数据集上的大量实验表明，LightHarmony3D在真实感与多视角一致性方面均达到了当前最优水平。

---

### 15. Hierarchical Visual Relocalization with Nearest View Synthesis from Feature Gaussian Splatting

- **作者**: Huaqi Tao, Bingxi Liu, Guangcheng Chen, Fulin Tang, Li He, Hong Zhang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.29185v1)
- **发表日期**: 2026-03-31
- **匹配关键词**: visual relocalization, gaussian splatting
- **arXiv**: [2603.29185v1](http://arxiv.org/abs/2603.29185v1)
- **📥 PDF**: 已下载至本地 (`2603.29185v1_Hierarchical_Visual_Relocalization_with_Nearest_View_Synthesis_from_Feature_Gaussian_Splatting.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉重定位是三维计算机视觉领域的一项基础任务，旨在估计相机重新访问已知场景时的位姿。虽然基于点的分层重定位方法展现出良好的可扩展性和效率，但其常受限于稀疏的图像观测和薄弱的特征匹配能力。本研究提出SplatHLoc——一种采用特征高斯溅射作为场景表征的新型分层视觉重定位框架。针对数据库图像稀疏性问题，我们提出自适应视角检索方法，通过合成与查询视角更契合的虚拟候选视角，提升初始位姿估计精度。在特征匹配方面，我们发现高斯渲染特征与图像直接提取的特征在两级匹配过程中各具优势：前者在粗匹配阶段表现更佳，后者在精匹配阶段更为有效。因此，我们引入混合特征匹配策略，实现更精准高效的位姿估计。在室内外数据集上的大量实验表明，SplatHLoc显著提升了视觉重定位的鲁棒性，创造了新的性能标杆。

---

### 16. Gleanmer: A 6 mW SoC for Real-Time 3D Gaussian Occupancy Mapping

- **作者**: Zih-Sing Fu, Peter Zhi Xuan Li, Sertac Karaman, Vivienne Sze
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.29005v1)
- **发表日期**: 2026-03-30
- **匹配关键词**: autonomous navigation, navigation
- **arXiv**: [2603.29005v1](http://arxiv.org/abs/2603.29005v1)
- **📥 PDF**: 已下载至本地 (`2603.29005v1_Gleanmer_A_6_mW_SoC_for_Real-Time_3D_Gaussian_Occupancy_Mapping.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 高保真三维占据地图对许多边缘应用（如增强现实/虚拟现实和自主导航）至关重要，但受限于功耗约束。我们提出了Gleanmer，这是一款搭载专用加速器的片上系统（SoC），用于支持基于高斯模型的三维占据地图GMMap。通过对紧凑高斯模型进行直接计算与高效重用的算法-硬件协同优化，Gleanmer将地图构建与查询能耗分别降低最高达63%和81%。采用高斯近似计算使加速器面积减少38%。基于16纳米CMOS工艺，Gleanmer在构建地图时能以超过88帧/秒的实时速度处理640x480分辨率图像，在查询地图时每秒可处理超过54万个坐标点。据我们所知，Gleanmer是首款能在6毫瓦功耗下为边缘应用实现实时三维占据地图构建的已量产片上系统。

---

## 📌 Poster

*其他相关研究*

---

### 1. Phyelds: A Pythonic Framework for Aggregate Computing

- **作者**: Gianluca Aguzzi, Davide Domini, Nicolas Farabegoli, Mirko Viroli
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.29999v1)
- **发表日期**: 2026-03-31
- **匹配关键词**: exploration
- **arXiv**: [2603.29999v1](http://arxiv.org/abs/2603.29999v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 聚合编程是一种基于场的协调范式，经过十余年的探索，已在传感器网络、机器人技术和物联网等多个领域成功应用，并实现了多种编程语言版本，如Protelis、ScaFi（Scala）和FCPP（C++）。近期研究方向将机器学习与聚合计算相结合，旨在支持大规模分布式学习，并为实现学习算法提供新的抽象层。然而，现有实现并未面向数据科学从业者——他们主要使用Python这一数据科学与机器学习领域的事实标准语言，该语言拥有丰富成熟的生态系统。Python在其他应用场景中也具有优势，例如教育领域和机器人技术（如通过ROS系统）。为填补这一空白，我们推出了Phyelds——一个用于聚合编程的Python库。Phyelds完整实现了场演算计算模型，同时保持轻量化特性，提供符合Python风格的API架构，专为与Python机器学习生态系统无缝集成而设计。本文阐述了Phyelds的设计与实现，并通过从经典聚合计算模式到联邦学习协调，再到与广泛使用的多智能体强化学习模拟器的集成案例，展示了其跨领域应用的广泛适应性。

---

### 2. Reconfiguration of supernumerary robotic limbs for human augmentation

- **作者**: Mustafa Mete, Anastasia Bolotnikova, Alexander Schuessler, Jamie Paik
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.29808v1)
- **发表日期**: 2026-03-31
- **匹配关键词**: human-robot collaboration
- **arXiv**: [2603.29808v1](http://arxiv.org/abs/2603.29808v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 可穿戴机器人旨在通过个性化交互，无缝适应人类及其所处环境。现有的超数机器人肢体（SRL）通过增加额外肢体来增强人类的身体能力，但迄今为止主要针对结构化工业环境中的特定任务应用而开发，限制了其在动态和非结构化环境中的适应性。本文提出了一种基于人类增强定量分析的新型可重构SRL框架，以指导开发适用于多样化场景的更具适应性的SRL。该框架揭示了SRL配置如何影响工作空间扩展和人机协作。我们定义了人类增强比率来评估协作工作空间、可见扩展工作空间和非可见扩展工作空间，从而能够系统地为特定任务选择SRL的放置位置、形态和自主性。利用这些指标，我们展示了定量增强分析如何指导SRL的重构与控制，以更好地匹配任务需求。我们通过一个由折纸启发的模块化元件构成的可重构SRL实验验证了所提出的方法。结果表明，基于定量人类增强分析的可重构SRL为日常环境中提供适应性人类增强和辅助提供了新的视角。

---

### 3. SafeDMPs: Integrating Formal Safety with DMPs for Adaptive HRI

- **作者**: Soumyodipta Nath, Pranav Tiwari, Ravi Prakash
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.29708v1)
- **发表日期**: 2026-03-31
- **匹配关键词**: HRI, collaborative robot
- **arXiv**: [2603.29708v1](http://arxiv.org/abs/2603.29708v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 在人类中心环境中运行的机器人必须既具备抗干扰的鲁棒性，又能提供可证明的防碰撞安全性。如何同时高效实现这两大特性仍是核心挑战。动态运动基元（DMPs）虽具备固有稳定性并能通过单次演示实现泛化，但缺乏形式化的安全保障。相反，控制屏障函数（CBFs）等形式化方法虽能提供可证明的安全性，却常依赖计算密集的实时优化，难以应用于高频控制场景。本文提出的SafeDMPs创新框架解决了这一矛盾。我们将DMPs的闭式求解效率与动态鲁棒性，同基于时空管道（STTs）推导出的可证明安全、非优化控制律相结合。这种协同机制不仅能生成抗干扰且适应新目标的运动轨迹，还能确保规避静态与动态障碍物。针对传统需要在线优化求解的问题，本方法实现了闭式解。在七自由度机械臂上的实验结果表明，SafeDMPs相比基于优化的基准方法在速度上提升数个数量级，且精度更高，为实时、安全、协作的机器人系统提供了理想解决方案。

---

### 4. RAAP: Retrieval-Augmented Affordance Prediction with Cross-Image Action Alignment

- **作者**: Qiyuan Zhuang, He-Yang Xu, Yijun Wang, Xin-Yang Zhao, Yang-Yang Li, Xiu-Shen Wei
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.29419v1)
- **发表日期**: 2026-03-31
- **匹配关键词**: affordance
- **arXiv**: [2603.29419v1](http://arxiv.org/abs/2603.29419v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: PROJECT_PAGE, GITHUB
  - 链接：https://github.com/SEU-VIPGroup/RAAP.
- **中文摘要**: 理解物体可供性是使机器人能够在多样化和非结构化环境中进行有目的、细粒度交互的关键。然而，现有方法要么依赖检索机制——由于数据稀疏性和覆盖范围不足而显得脆弱，要么依赖大规模模型——在应用于未见类别时经常错误定位接触点并误判接触后动作，从而阻碍了稳健的泛化能力。我们提出检索增强可供性预测框架，该框架通过基于对齐的学习统一了可供性检索机制。通过解耦静态接触点定位与动态动作方向预测，RAAP利用密集对应关系迁移接触点，并通过检索增强对齐模型预测动作方向——该模型采用双重加权注意力机制整合多组参考信息。在DROID和HOI4D数据集的紧凑子集上训练（每任务仅需数十个样本），RAAP在未见物体和类别上均表现出稳定性能，并在仿真环境与真实世界中实现了零样本机器人操作。项目网站：https://github.com/SEU-VIPGroup/RAAP。

---

