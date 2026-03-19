# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-03-19 08:06

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 1/20 篇提供

**🌟 Highlight**: 20 篇 | **📌 Poster**: 0 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. vAccSOL: Efficient and Transparent AI Vision Offloading for Mobile Robots

- **作者**: Adam Zahir, Michele Gucciardom Falk Selker, Anastasios Nanos, Kostis Papazafeiropoulos, Carlos J. Bernardos, Nicolas Weber, Roberto Gonzalez
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.16685v1)
- **发表日期**: 2026-03-17
- **匹配关键词**: navigation
- **arXiv**: [2603.16685v1](http://arxiv.org/abs/2603.16685v1)
- **📥 PDF**: 已下载至本地 (`2603.16685v1_vAccSOL_Efficient_and_Transparent_AI_Vision_Offloading_for_Mobile_Robots.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 移动机器人正越来越多地应用于巡检、巡逻和搜救任务，其依赖计算机视觉实现环境感知、自主导航与决策。然而，由于计算资源有限且能耗约束严格，在机器人本体执行现代视觉任务面临巨大挑战。虽然部分平台配备了嵌入式加速器，但这些硬件通常绑定专有软件栈，导致用户自定义任务只能在资源受限的配套计算机上运行。

我们提出vAccSOL框架，旨在为异构机器人及边缘平台提供高效透明的AI视觉任务执行方案。该框架整合两大核心组件：一是SOL神经网络编译器，可生成依赖极简的优化推理库；二是vAccel轻量级执行框架，能够透明调度推理任务至机器人本地或邻近边缘基础设施。这种组合实现了硬件优化推理与灵活任务部署，且无需修改机器人应用程序。

我们在真实测试环境中对vAccSOL进行评估，使用商用四足机器人和涵盖图像分类、视频分类及语义分割的十二个深度学习模型。与PyTorch编译器基准相比，SOL实现了相当或更优的推理性能。通过边缘卸载机制，vAccSOL较PyTorch方案将机器人端功耗降低最高达80%，边缘端功耗降低最高达60%，同时将视觉处理流水线帧率提升最高达24倍，显著延长了电池供电机器人的持续运行时间。

---

### 2. LIMBERO: A Limbed Climbing Exploration Robot Toward Traveling on Rocky Cliffs

- **作者**: Kentaro Uno, Masazumi Imai, Kazuki Takada, Teruhiro Kataonami, Yudai Matsuura, Antonin Ringeval-Meusnier, Keita Nagaoka, Mikio Eguchi, Ryo Nishibe, Kazuya Yoshida
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.16531v1)
- **发表日期**: 2026-03-17
- **匹配关键词**: exploration
- **arXiv**: [2603.16531v1](http://arxiv.org/abs/2603.16531v1)
- **📥 PDF**: 已下载至本地 (`2603.16531v1_LIMBERO_A_Limbed_Climbing_Exploration_Robot_Toward_Traveling_on_Rocky_Cliffs.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 在月球与行星探测任务中，足式机器人作为传统轮式机器人的重要补充方案受到广泛关注，后者在崎岖不平的地形中行进能力有限。为实现在极端不规则和陡峭倾斜表面的移动，配备足端抓握机构的仿生攀爬机器人展现出巨大潜力。本文提出LIMBERO——一款采用脊柱式抓握机构的10公斤级四足攀爬机器人，能够在复杂陡峭地形实现稳定移动与攀爬。我们首先介绍一种新型抓握机构设计，其通过单电机驱动实现指节闭合与脊柱钩爪运动的联动机制，在轻量化设计（525克）前提下实现了卓越抓握性能（>150 N）。进一步开发了高效算法，可在连续粗糙地形上可视化基于几何特征的抓握可行性指数。最终将这些组件集成至LIMBERO系统，并在1G重力条件下成功演示了其攀爬陡峭岩石表面的能力，这是同尺度足式攀爬机器人首次实现此类突破。

---

### 3. Encoding Predictability and Legibility for Style-Conditioned Diffusion Policy

- **作者**: Adrien Jacquet Crétides, Mouad Abrini, Hamed Rahimi, Mohamed Chetouani
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.16368v1)
- **发表日期**: 2026-03-17
- **匹配关键词**: human-robot collaboration, navigation, diffusion policy
- **arXiv**: [2603.16368v1](http://arxiv.org/abs/2603.16368v1)
- **📥 PDF**: 已下载至本地 (`2603.16368v1_Encoding_Predictability_and_Legibility_for_Style-Conditioned_Diffusion_Policy.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 在人与机器人协作中，如何在效率与动作透明度之间取得平衡是一个核心挑战，因为高度表现力的动作往往会带来不必要的时间和能量消耗。在协作环境中，动作的可读性有助于人类观察者更好地理解机器人的行为，从而提升安全性和信任度。然而，这些行为会导致轨迹偏离最优状态并显得夸张，在机器人目标已十分明确的低模糊性场景中显得冗余。为解决这一权衡问题，我们提出了风格条件扩散策略（SCDP），这是一个模块化框架，能够根据环境配置，约束预训练扩散模型生成具有可读性或高效性的轨迹。我们的方法采用后训练流程，冻结基础策略，同时训练轻量级场景编码器和条件预测器来调节扩散过程。在推理阶段，模糊性检测模块会激活相应的条件设置：仅在目标模糊时优先采用表现力强的动作，否则回归高效路径。我们在操作与导航任务中对SCDP进行了评估，结果表明，该方法能在模糊场景中增强动作可读性，同时在无需可读性时保持最优效率，且无需重新训练基础策略。

---

### 4. OGScene3D: Incremental Open-Vocabulary 3D Gaussian Scene Graph Mapping for Scene Understanding

- **作者**: Siting Zhu, Ziyun Lu, Guangming Wang, Chenguang Huang, Yongbo Chen, I-Ming Chen, Wolfram Burgard, Hesheng Wang ⭐
  - **高亮作者**: Wolfram Burgard
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.16301v1)
- **发表日期**: 2026-03-17
- **匹配关键词**: scene graph, navigation, navigation and manipulation
- **arXiv**: [2603.16301v1](http://arxiv.org/abs/2603.16301v1)
- **📥 PDF**: 已下载至本地 (`2603.16301v1_OGScene3D_Incremental_Open-Vocabulary_3D_Gaussian_Scene_Graph_Mapping_for_Scene_Understanding.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 开放词汇场景理解对机器人应用至关重要，它使机器人能够理解复杂的三维环境上下文，并支持导航、操作等多种下游任务。然而，现有方法需要预先构建完整的三维语义地图来构建场景图以实现场景理解，这限制了它们在机器人逐步探索环境场景中的适用性。为解决这一挑战，我们提出了OGScene3D系统——一种能够逐步实现精确三维语义建图与场景图构建的开放词汇场景理解系统。该系统采用基于置信度的高斯语义表示方法，联合建模语义预测及其可靠性，从而实现鲁棒的场景建模。基于此表示方法，我们提出分层三维语义优化策略，通过建立局部对应关系与全局优化实现语义一致性，进而构建全局一致的语义地图。此外，我们设计了长期全局优化方法，利用历史观测的时间记忆增强语义预测能力。该方法通过融合二维-三维语义一致性与高斯渲染贡献度，持续优化对整个场景的语义理解。更进一步，我们开发了渐进式图构建方法，能够动态创建并更新节点及语义关系，实现三维场景图的持续更新。在广泛使用的数据集和真实场景中进行的大量实验，验证了我们的OGScene3D系统在开放词汇场景理解方面的有效性。

---

### 5. MG-Grasp: Metric-Scale Geometric 6-DoF Grasping Framework with Sparse RGB Observations

- **作者**: Kangxu Wang, Siang Chen, Chenxing Jiang, Shaojie Shen, Yixiang Dai, Guijin Wang ⭐
  - **高亮作者**: Shaojie Shen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.16270v1)
- **发表日期**: 2026-03-17
- **匹配关键词**: grasp detection, 6-DoF grasping
- **arXiv**: [2603.16270v1](http://arxiv.org/abs/2603.16270v1)
- **📥 PDF**: 已下载至本地 (`2603.16270v1_MG-Grasp_Metric-Scale_Geometric_6-DoF_Grasping_Framework_with_Sparse_RGB_Observations.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 单视角RGB-D抓取检测仍是六自由度机器人抓取系统的常见选择，该方法通常需要深度传感器。尽管近期已出现仅使用RGB的六自由度抓取方法，但其不精确的几何表征无法直接适用于物理可靠的机器人操作，从而阻碍了可靠抓取姿态的生成。为突破这些局限，我们提出MG-Grasp——一种新型的无深度六自由度抓取框架，能够实现高质量物体抓取。该方法利用具备相机内外参数的双视角三维基础模型，从稀疏RGB图像重建公制尺度且多视角一致的高密度点云，并生成稳定的六自由度抓取姿态。在GraspNet-10亿数据集及真实场景中的实验表明，MG-Grasp在基于RGB的六自由度抓取方法中达到了最先进的抓取性能。

---

### 6. Enabling Dynamic Tracking in Vision-Language-Action Models via Time-Discrete and Time-Continuous Velocity Feedforward

- **作者**: Johannes Hechtl, Philipp Schmitt, Georg von Wichert, Wolfram Burgard ⭐
  - **高亮作者**: Wolfram Burgard
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.16218v1)
- **发表日期**: 2026-03-17
- **匹配关键词**: vision-language-action model, vision-language-action, VLA
- **arXiv**: [2603.16218v1](http://arxiv.org/abs/2603.16218v1)
- **📥 PDF**: 已下载至本地 (`2603.16218v1_Enabling_Dynamic_Tracking_in_Vision-Language-Action_Models_via_Time-Discrete_and_Time-Continuous_Vel.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 尽管视觉-语言-动作（VLA）模型在机器人操作领域展现出巨大潜力，但由于顺应性与响应性之间的固有矛盾，其在刚性工业机器人上的部署仍面临挑战。标准的行为克隆方法以低频预测离散位姿，忽略了底层顺应控制器通常使用的速度和加速度前馈项。这需要依赖高刚度实现精确跟踪，从而牺牲了安全接触动态。本文论证了将速度前馈项整合到VLA策略中以解决这一矛盾的重要性。我们提出两种从VLA模型中提取速度目标的方法：一是作为现有模型高效桥梁的时间离散有限差分近似法，二是能原生生成$C^2$连续轨迹以适应高频控制的连续三次B样条动作空间。关键在于，这两种方法均严格遵循模型无关原则，兼容任何标准动作分块架构，仅需对遥操作、数据处理及底层控制器进行调整。我们微调了$π_{0.5}$模型，并在高要求的接触密集型立方体入孔任务中评估了两种方法。结果表明：通过有限差分法整合速度前馈项可显著提升任务执行速度，而连续B样条方法在保持高整体成功率的同时，为生成更平滑的高阶导数提供了基础，且不损害顺应性。

---

### 7. Towards the Vision-Sound-Language-Action Paradigm: The HEAR Framework for Sound-Centric Manipulation

- **作者**: Chang Nie, Tianchen Deng, Guangming Wang, Zhe Liu, Hesheng Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.16086v1)
- **发表日期**: 2026-03-17
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2603.16086v1](http://arxiv.org/abs/2603.16086v1)
- **📥 PDF**: 已下载至本地 (`2603.16086v1_Towards_the_Vision-Sound-Language-Action_Paradigm_The_HEAR_Framework_for_Sound-Centric_Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 尽管当前的视觉-语言-动作（VLA）模型已开始融入音频信息，但它们通常将声音视为静态的预执行提示，或仅关注人类语音。这导致在实时以声音为中心的操作中存在显著空白——在任务执行过程中，转瞬即逝的环境声学信息本可为状态验证提供关键依据。由于低频更新或系统延迟，关键声音极易被遗漏。而采用开环执行的动作分块机制进一步加剧了这一问题，形成了"盲执行区间"：在离散的音频观测窗口之间，声学事件会完全丢失。认识到持续听觉感知的必要性，我们正式提出视觉-声音-语言-动作（VSLA）作为连续控制范式，该范式在延迟决策循环中整合视觉、流式音频、语言及本体感知的协同条件。

作为具体实现，我们推出HEAR框架，该VSLA架构包含四个核心组件：（1）流式历史化模块，通过紧凑的因果音频上下文跨越执行间隙；（2）基于全能基础模型改造的多感官推理模块；（3）作为音频世界模型的演进器，通过预测近期音频编码学习时序动态；（4）采用流匹配技术的执行策略，生成平滑的动作序列。针对VSLA预训练数据与评估体系的稀缺性，我们构建了OpenX-Sound预训练数据集，并首创具有严格因果时序规则的声学操作基准测试HEAR-Bench。实验表明，稳健的声学中心化操作必须依赖因果持续性机制与显式时序学习。该框架为具身智能体的多感官基础模型发展迈出实践性一步，使机器人能够感知动态环境并实现交互。代码与演示视频详见https://hear.irmv.top。

---

### 8. Enhancing Linguistic Generalization of VLA: Fine-Tuning OpenVLA via Synthetic Instruction Augmentation

- **作者**: Dongik Shin
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.16044v1)
- **发表日期**: 2026-03-17
- **匹配关键词**: vision-language-action model, vision-language-action, VLA
- **arXiv**: [2603.16044v1](http://arxiv.org/abs/2603.16044v1)
- **📥 PDF**: 已下载至本地 (`2603.16044v1_Enhancing_Linguistic_Generalization_of_VLA_Fine-Tuning_OpenVLA_via_Synthetic_Instruction_Augmentatio.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 泛化能力仍然是具身人工智能的核心挑战，因为机器人必须适应多样化环境。尽管OpenVLA通过大规模预训练成为视觉-语言-动作模型的性能标杆，但在面对全新环境时其零样本性能仍存在局限。本文提出一种参数高效的微调策略，通过为Bridge Dataset V2合成通用指令集来增强OpenVLA的语言泛化能力。研究利用大语言模型为现有轨迹生成大量语义等价但结构多样的指令。实验中采用低秩自适应方法对增强后的指令-动作对进行微调，使模型能够弥合复杂自然语言意图与机器人动作之间的鸿沟。结果表明，经低秩自适应增强的模型展现出更强的鲁棒性，这证明丰富专业数据集的语言空间对于具身智能体至关重要。

---

### 9. ExpertGen: Scalable Sim-to-Real Expert Policy Learning from Imperfect Behavior Priors

- **作者**: Zifan Xu, Ran Gong, Maria Vittoria Minniti, Ahmet Salih Gundogdu, Eric Rosen, Kausik Sivakumar, Riedana Yan, Zixing Wang, Di Deng, Peter Stone, Xiaohan Zhang, Karl Schmeckpeper
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.15956v1)
- **发表日期**: 2026-03-16
- **匹配关键词**: exploration, diffusion policy
- **arXiv**: [2603.15956v1](http://arxiv.org/abs/2603.15956v1)
- **📥 PDF**: 已下载至本地 (`2603.15956v1_ExpertGen_Scalable_Sim-to-Real_Expert_Policy_Learning_from_Imperfect_Behavior_Priors.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 学习具有泛化性和鲁棒性的行为克隆策略需要大量高质量的机器人数据。虽然人类演示（例如通过遥操作）是专家行为的标准来源，但在现实世界中大规模获取此类数据成本极高。本文提出ExpertGen框架，通过在仿真环境中自动化学习专家策略，实现可扩展的仿真到现实迁移。该框架首先利用基于不完美演示训练的扩散策略初始化行为先验，这些演示可由大语言模型合成或由人类提供。随后通过强化学习优化扩散模型的初始噪声（同时保持原始策略冻结），引导该先验实现高任务成功率。通过冻结预训练的扩散策略，ExpertGen将探索范围规范在安全、类人的行为流形内，同时仅需稀疏奖励即可实现高效学习。在具有挑战性的操作基准测试中，实证评估表明ExpertGen无需奖励工程即可稳定生成高质量专家策略。在工业装配任务中达到90.5%的整体成功率，在长时序操作任务中获得85%的整体成功率，优于所有基线方法。所得策略展现出灵巧的控制能力，并能适应不同初始配置和故障状态的鲁棒性。为验证仿真到现实的迁移效果，基于状态学习的专家策略通过DAgger方法进一步蒸馏为视觉运动策略，并成功部署在真实机器人硬件上。

---

### 10. M^3: Dense Matching Meets Multi-View Foundation Models for Monocular Gaussian Splatting SLAM

- **作者**: Kerui Ren, Guanghao Li, Changjian Jiang, Yingxiang Xu, Tao Lu, Linning Xu, Junting Dong, Jiangmiao Pang, Mulin Yu, Bo Dai
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.16844v1)
- **发表日期**: 2026-03-17
- **匹配关键词**: gaussian splatting
- **arXiv**: [2603.16844v1](http://arxiv.org/abs/2603.16844v1)
- **📥 PDF**: 已下载至本地 (`2603.16844v1_M^3_Dense_Matching_Meets_Multi-View_Foundation_Models_for_Monocular_Gaussian_Splatting_SLAM.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 从未标定的单目视频流进行实时三维重建仍具挑战性，因其需要在动态环境中同时实现高精度位姿估计与高效在线优化。虽然将三维基础模型与SLAM框架结合是前景广阔的范式，但关键瓶颈依然存在：多数多视角基础模型以前馈方式估计位姿，产生的像素级对应关系缺乏严格几何优化所需的精度。为此，我们提出M^3模型，通过为多视角基础模型增设专用匹配头来获取细粒度密集对应关系，并将其集成至鲁棒的单目高斯溅射SLAM系统中。M^3进一步引入动态区域抑制与跨推理内参对齐机制，显著提升了跟踪稳定性。在多样化室内外基准测试中的大量实验表明，该方法在位姿估计与场景重建精度上均达到最先进水平。值得注意的是，在ScanNet++数据集上，M^3的绝对轨迹误差均方根较VGGT-SLAM 2.0降低64.3%，峰值信噪比指标较ARTDECO提升2.11 dB。

---

### 11. WildDepth: A Multimodal Dataset for 3D Wildlife Perception and Depth Estimation

- **作者**: Muhammad Aamir, Naoya Muramatsu, Sangyun Shin, Matthew Wijers, Jiaxing Jhong, Xinyu Hou, Amir Patel, Andrew Markham
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.16816v1)
- **发表日期**: 2026-03-17
- **匹配关键词**: 3d reconstruction, 3D reconstruction
- **arXiv**: [2603.16816v1](http://arxiv.org/abs/2603.16816v1)
- **📥 PDF**: 已下载至本地 (`2603.16816v1_WildDepth_A_Multimodal_Dataset_for_3D_Wildlife_Perception_and_Depth_Estimation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 深度估计与三维重建作为计算机视觉的核心课题已被广泛研究。从车辆等几何形状相对简单的刚性物体起步，研究范围已扩展至涵盖包括人类和动物等具有挑战性的可变形物体在内的通用对象。然而针对动物对象，现有模型大多基于无度量尺度的数据集进行训练，这类数据集虽能验证纯图像模型的性能，却存在局限。为此我们提出WildDepth——一个面向从家养到野外环境多类别动物的多模态数据集与基准测试套件，包含同步采集的RGB图像与激光雷达数据，可用于深度估计、行为检测及三维重建任务。实验结果表明，多模态数据的使用将深度估计的均方根误差可靠性提升达10%，而RGB-激光雷达融合技术使三维重建的倒角距离保真度提高12%。通过开源WildDepth数据集及其基准测试体系，我们旨在推动建立能够跨领域泛化的鲁棒多模态感知系统。

---

### 12. World Reconstruction From Inconsistent Views

- **作者**: Lukas Höllein, Matthias Nießner
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.16736v1)
- **发表日期**: 2026-03-17
- **匹配关键词**: 3d reconstruction, 3D reconstruction
- **arXiv**: [2603.16736v1](http://arxiv.org/abs/2603.16736v1)
- **📥 PDF**: 已下载至本地 (`2603.16736v1_World_Reconstruction_From_Inconsistent_Views.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视频扩散模型能够生成高质量且多样化的动态场景，但输出序列中的单帧画面往往缺乏三维一致性，这给三维世界的重建带来了困难。为此，我们提出一种新方法，通过将视频帧非刚性对齐至全局一致的坐标系框架来处理这些不一致性问题，从而生成清晰细致的点云重建结果。首先，我们利用几何基础模型将每帧图像提升为像素级三维点云，但由于前述不一致性，这些点云包含未对齐的表面。随后，我们提出一种定制化的非刚性迭代帧到模型ICP算法，实现所有帧间的初始对齐，再通过全局优化进一步锐化点云。最后，我们将该点云作为三维重建的初始化条件，并提出一种新颖的反向形变渲染损失函数，从而从不一致的视角中创建出高质量、可探索的三维环境。实验表明，我们的三维场景在质量上优于基线方法，成功将视频模型转化为具有三维一致性的世界生成器。

---

### 13. Fast-WAM: Do World Action Models Need Test-time Future Imagination?

- **作者**: Tianyuan Yuan, Zibin Dong, Yicheng Liu, Hang Zhao
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.16666v1)
- **发表日期**: 2026-03-17
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2603.16666v1](http://arxiv.org/abs/2603.16666v1)
- **📥 PDF**: 已下载至本地 (`2603.16666v1_Fast-WAM_Do_World_Action_Models_Need_Test-time_Future_Imagination?.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://yuantianyuan01.github.io/FastWAM/
- **中文摘要**: 世界行动模型（WAMs）作为具身控制中视觉-语言-行动（VLA）模型的一种有前景的替代方案崭露头角，因为它们明确建模了视觉观察在行动下可能如何演变。现有的大多数WAM遵循“想象后执行”范式，通过迭代视频去噪在测试时产生显著延迟，但尚不清楚显式的未来想象是否对强大的行动性能真正必要。本文探讨WAM在测试时是否需要显式的未来想象，或者其优势是否主要源于训练期间的视频建模。通过提出\textbf{Fast-WAM}——一种在训练时保留视频协同训练但在测试时跳过未来预测的WAM架构，我们解耦了训练中视频建模与推理中显式未来生成的作用。我们进一步实例化了几种Fast-WAM变体，以对这两个因素进行受控比较。在这些变体中，我们发现Fast-WAM与“想象后执行”变体保持竞争力，而去除视频协同训练则会导致性能大幅下降。实证表明，Fast-WAM在仿真基准（LIBERO和RoboTwin）和现实世界任务中均取得了与最先进方法相媲美的结果，且无需具身预训练。它以190毫秒的延迟实时运行，比现有的“想象后执行”WAM快4倍以上。这些结果表明，WAM中视频预测的主要价值可能在于提升训练期间的世界表征，而非在测试时生成未来观察。项目页面：https://yuantianyuan01.github.io/FastWAM/

---

### 14. Rethinking Pose Refinement in 3D Gaussian Splatting under Pose Prior and Geometric Uncertainty

- **作者**: Mangyu Kong, Jaewon Lee, Seongwon Lee, Euntai Kim
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.16538v1)
- **发表日期**: 2026-03-17
- **匹配关键词**: 3D gaussian splatting, gaussian splatting
- **arXiv**: [2603.16538v1](http://arxiv.org/abs/2603.16538v1)
- **📥 PDF**: 已下载至本地 (`2603.16538v1_Rethinking_Pose_Refinement_in_3D_Gaussian_Splatting_under_Pose_Prior_and_Geometric_Uncertainty.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 三维高斯泼溅（3DGS）作为一种强大的场景表示方法，近年来崭露头角，并越来越多地应用于视觉定位与姿态优化领域。然而，尽管其具备高质量的可微分渲染能力，基于3DGS的姿态优化鲁棒性仍高度依赖于初始相机姿态与重建几何结构的准确性。本研究深入探讨了这些局限性，并识别出两大不确定性来源：（一）姿态先验不确定性，通常源于回归或检索模型输出的单一确定性估计；（二）几何不确定性，由3DGS重建过程中的缺陷引发，这类误差会进一步传播至PnP求解器中。即使渲染外观仍具合理性，此类不确定性仍可能导致重投影几何结构扭曲并破坏优化过程的稳定性。为应对这些不确定性，我们提出了一种结合蒙特卡洛姿态采样与基于费舍尔信息的PnP优化的重定位框架。该方法显式地兼顾姿态与几何不确定性，且无需重新训练或额外监督。在多样化的室内外基准测试中，我们的方法持续提升了定位精度，并显著增强了在姿态与深度噪声干扰下的稳定性。

---

### 15. GAP-MLLM: Geometry-Aligned Pre-training for Activating 3D Spatial Perception in Multimodal Large Language Models

- **作者**: Jiaxin Zhang, Junjun Jiang, Haijie Li, Youyu Chen, Kui Jiang, Dave Zhenyu Chen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.16461v1)
- **发表日期**: 2026-03-17
- **匹配关键词**: 3d reconstruction, 3D reconstruction
- **arXiv**: [2603.16461v1](http://arxiv.org/abs/2603.16461v1)
- **📥 PDF**: 已下载至本地 (`2603.16461v1_GAP-MLLM_Geometry-Aligned_Pre-training_for_Activating_3D_Spatial_Perception_in_Multimodal_Large_Lang.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 多模态大语言模型（MLLMs）在纯RGB输入条件下展现出卓越的语义推理能力，但在三维空间感知方面存在明显不足。尽管现有方法通过三维重建模型获取隐式几何先验，但与使用显式三维数据的方法相比，基于图像的方法仍存在显著性能差距。我们认为这种差距并非源于几何先验不足，而是训练范式错配所致：以文本为主导的微调策略未能有效激活MLLMs内部的几何表征能力。现有方案通常采用简单的特征拼接方式，并在缺乏几何特异性监督的情况下直接优化下游任务，导致结构信息利用不充分。为突破这一局限，我们提出GAP-MLLM——一种几何对齐预训练范式，在下游任务适配前显式激活结构感知能力。具体而言，我们设计了视觉提示联合任务，强制MLLMs在预测语义标签的同时生成稀疏点云图，从而强化几何感知。此外，我们构建了具有令牌级门控机制的多层级渐进融合模块，实现几何先验的自适应融合而不抑制语义推理。大量实验表明，GAP-MLLM显著提升了几何特征融合效果，在三维视觉定位、三维密集描述生成和三维视频目标检测任务中均取得持续性能提升。

---

### 16. SignNav: Leveraging Signage for Semantic Visual Navigation in Large-Scale Indoor Environments

- **作者**: Jian Sun, Yuming Huang, He Li, Shuqi Xiao, Shenyan Guo, Maani Ghaffari, Qingbiao Li, Chengzhong Xu, Hui Kong
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.16166v1)
- **发表日期**: 2026-03-17
- **匹配关键词**: visual navigation, navigation
- **arXiv**: [2603.16166v1](http://arxiv.org/abs/2603.16166v1)
- **📥 PDF**: 已下载至本地 (`2603.16166v1_SignNav_Leveraging_Signage_for_Semantic_Visual_Navigation_in_Large-Scale_Indoor_Environments.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 人类通常利用标识牌提供的语义提示，在大型室内环境（如医院和机场航站楼）中导航至目的地。然而，在具身导航领域，这一能力尚未得到充分探索。本文提出了一种新颖的具身导航任务——SignNav，要求智能体能够解读标识牌的语义提示，并根据当前观察推理后续行动。为促进该领域研究，我们构建了LSI数据集，用于训练和评估各类SignNav智能体。大型室内环境中动态变化的语义提示与稀疏分布的标识牌对SignNav任务构成了显著挑战。为解决这些挑战，我们提出了时空感知Transformer模型（START）进行端到端决策。空间感知模块将标识牌的语义提示映射到物理世界，而时间感知模块则捕捉历史状态与当前观察之间的长程依赖关系。通过采用数据集聚合（DAgger）的两阶段训练策略，我们的方法在未见验证集上取得了80%的成功率和0.74的NDTW分数，达到最先进水平。实际部署进一步证明了该方法在无预设地图的物理环境中的实用性。

---

### 17. Safety Case Patterns for VLA-based driving systems: Insights from SimLingo

- **作者**: Gerhard Yu, Fuyuki Ishikawa, Oluwafemi Odu, Alvine Boaye Belle
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.16013v1)
- **发表日期**: 2026-03-16
- **匹配关键词**: VLA, vision-language-action, navigation
- **arXiv**: [2603.16013v1](http://arxiv.org/abs/2603.16013v1)
- **📥 PDF**: 已下载至本地 (`2603.16013v1_Safety_Case_Patterns_for_VLA-based_driving_systems_Insights_from_SimLingo.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 基于视觉-语言-动作（VLA）的驾驶系统代表了自动驾驶领域的重要范式转变，通过融合交通场景理解、语言解析与动作生成，这类系统能够实现更灵活、自适应且可响应指令的驾驶行为。然而，尽管这类系统正被日益广泛地采用，并具备支持社会责任型自动驾驶及理解人类高层指令的潜力，它们仍可能表现出新型危险行为。例如，在多模态控制回路中引入自然语言输入（如用户指令或导航指令），可能导致不可预测且不安全的行为，危及车内乘员与行人安全。因此，确保此类系统的安全性对于建立其运行信任至关重要。为此，我们提出了一种名为RAISE的新型安全案例设计方法。该方法针对基于指令的驾驶系统（如VLA驾驶系统）引入了定制化新模式，扩展了危险分析与风险评估（HARA）框架以细化安全场景及其预期结果，并提供了构建VLA驾驶系统安全案例的设计技术。通过SimLingo平台的案例研究，我们展示了如何运用该方法为这类新兴自动驾驶系统构建严谨的、基于证据的安全声明。

---

### 18. Robust Dynamic Object Detection in Cluttered Indoor Scenes via Learned Spatiotemporal Cues

- **作者**: Juan Rached, Yixuan Jia, Kota Kondo, Jonathan P. How ⭐
  - **高亮作者**: Jonathan P. How
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.15826v1)
- **发表日期**: 2026-03-16
- **匹配关键词**: autonomous navigation, navigation
- **arXiv**: [2603.15826v1](http://arxiv.org/abs/2603.15826v1)
- **📥 PDF**: 已下载至本地 (`2603.15826v1_Robust_Dynamic_Object_Detection_in_Cluttered_Indoor_Scenes_via_Learned_Spatiotemporal_Cues.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 在复杂环境中实现可靠的动态物体检测，仍然是自主导航面临的关键挑战。依赖聚类和启发式滤波的纯几何激光雷达流程，在动态障碍物紧贴静态结构移动或仅被部分观测时，常出现漏检问题。视觉增强方法虽能提供语义线索，但受限于封闭集检测器和相机视场约束，对新型障碍物及视锥外事件的鲁棒性不足。本研究提出一种纯激光雷达框架，将基于时序占据网格的运动分割与学习的鸟瞰图动态先验信息相融合。该融合模块优先采用可用的三维检测结果，同时利用学习的动态网格恢复因邻近干扰导致的漏检。通过运动捕捉真值实验验证，本方法在高度杂乱环境中相比现有最优技术，召回率提升28.67%，F1分数提高18.50%，同时保持相当的检测精度与位置误差。

---

### 19. Trajectory-Diversity-Driven Robust Vision-and-Language Navigation

- **作者**: Jiangyang Li, Cong Wan, SongLin Dong, Chenhao Ding, Qiang Wang, Zhiheng Ma, Yihong Gong
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.15370v1)
- **发表日期**: 2026-03-16
- **匹配关键词**: vision-and-language navigation, VLN, navigation
- **arXiv**: [2603.15370v1](http://arxiv.org/abs/2603.15370v1)
- **📥 PDF**: 已下载至本地 (`2603.15370v1_Trajectory-Diversity-Driven_Robust_Vision-and-Language_Navigation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉语言导航任务要求智能体根据自然语言指令在逼真环境中进行导航。现有方法主要依赖模仿学习，存在泛化能力有限且对执行扰动鲁棒性较差的问题。本文提出NavGRPO强化学习框架，通过组内相对策略优化学习目标导向的导航策略。该方法通过探索多样化轨迹并利用组内性能比较进行优化，使智能体能够识别专家路径之外的有效策略，且无需额外价值网络支持。基于ScaleVLN构建的NavGRPO在R2R和REVERIE基准测试中展现出卓越的鲁棒性，在未见环境中分别实现+3.0%和+1.71%的SPL提升。在极端早期扰动条件下，本方法较基线模型获得+14.89%的SPL增益，证实目标导向的强化学习训练能构建显著更鲁棒的导航策略。代码与模型将开源发布。

---

### 20. NavGSim: High-Fidelity Gaussian Splatting Simulator for Large-Scale Navigation

- **作者**: Jiahang Liu, Yuanxing Duan, Jiazhao Zhang, Minghan Li, Shaoan Wang, Zhizheng Zhang, He Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.15186v1)
- **发表日期**: 2026-03-16
- **匹配关键词**: gaussian splatting, vision-language-action, VLA, 3D gaussian splatting, navigation
- **arXiv**: [2603.15186v1](http://arxiv.org/abs/2603.15186v1)
- **📥 PDF**: 已下载至本地 (`2603.15186v1_NavGSim_High-Fidelity_Gaussian_Splatting_Simulator_for_Large-Scale_Navigation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 为机器人模拟真实环境被广泛认为是机器人学习领域的关键挑战，尤其在渲染和物理仿真方面。这一挑战在导航任务中尤为突出，因为轨迹常常跨越多个房间甚至整层楼宇。本研究提出NavGSim——一个基于高斯泼溅技术的仿真器，专门用于生成高保真度的大规模导航环境。NavGSim依托分层式3D高斯泼溅框架，能够在数百平方米的广阔场景中实现照片级真实感渲染。为模拟导航碰撞，我们创新性地引入基于高斯泼溅的切片技术，可直接从重建的高斯模型中提取可通行区域。此外，为提升易用性，我们提供支持多GPU开发的完整NavGSim应用程序接口，包含自定义场景重建、机器人配置、策略训练与评估等工具集。为验证NavGSim的有效性，我们使用从该仿真器采集的轨迹训练视觉-语言-动作模型，并在仿真环境与真实场景中评估其性能。实验结果表明，NavGSim显著增强了VLA模型对场景的理解能力，使策略能够有效处理多样化的导航查询。

---

