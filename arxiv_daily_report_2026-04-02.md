# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-04-02 08:10

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 4/20 篇提供

**🌟 Highlight**: 9 篇 | **📌 Poster**: 11 篇

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
- **中文摘要**: 视觉语言动作（VLA）模型的发展因预训练视觉语言模型（VLM）的推动而显著加速。然而，现有大多数端到端VLA模型主要将VLM视为多模态编码器，直接将视觉语言特征映射为低层动作。这种范式未能充分利用VLM在高层决策中的潜力，并导致训练不稳定，常常削弱其丰富的语义表征能力。为解决这些局限，我们提出了DIAL框架，通过可微分潜在意图瓶颈桥接高层决策与低层运动执行。具体而言，基于VLM的System-2在VLM原生特征空间内合成潜在视觉前瞻，实现潜在世界建模；这种前瞻显式编码意图并构成结构化瓶颈。随后，轻量级System-1策略通过潜在逆动力学，将预测意图与当前观测共同解码为精确的机器人动作。为确保优化稳定性，我们采用两阶段训练范式：解耦预热阶段中，System-2学习在统一特征空间内预测潜在未来状态，而System-1在真实未来状态引导下学习运动控制；随后进行无缝的端到端联合优化。这使得动作感知梯度能以受控方式优化VLM骨干网络，同时保留预训练知识。在RoboCasa GR1桌面基准测试中的大量实验表明，DIAL实现了新的最优性能，仅需先前方法十分之一的演示数据即可获得更优表现。此外，通过利用异构人类演示数据，DIAL学习了物理基础的操作先验知识，并在人形机器人实际部署中，对未见物体和新配置展现出强大的零样本泛化能力。

---

### 2. CLaD: Planning with Grounded Foresight via Cross-Modal Latent Dynamics

- **作者**: Andrew Jeong, Jaemin Kim, Sebin Lee, Sung-Eui Yoon
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.29409v1)
- **发表日期**: 2026-03-31
- **匹配关键词**: diffusion policy, VLA
- **arXiv**: [2603.29409v1](http://arxiv.org/abs/2603.29409v1)
- **📥 PDF**: 已下载至本地 (`2603.29409v1_CLaD_Planning_with_Grounded_Foresight_via_Cross-Modal_Latent_Dynamics.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 机器人操作涉及运动学与语义状态的转换，这两种转换通过底层动作天然耦合。然而，现有方法仅在语义空间或潜在空间中进行规划，未能显式对齐这两种跨模态转换。为此，我们提出CLaD框架，通过非对称交叉注意力机制建模本体感知状态与语义状态在动作作用下的协同演化过程，使运动学转换能够查询语义转换。CLA采用指数移动平均目标编码器和辅助重构损失的自监督目标来预测基于观测状态的潜在前瞻，既防止表征坍缩又将预测锚定于可观测状态。通过观测信息调制的前瞻预测被用于条件扩散策略的动作生成。在LIBERO-LONG基准测试中，CLaD以显著更少的参数量实现94.7%的成功率，性能与大型视觉语言动作模型相当。

---

### 3. Efficient Camera Pose Augmentation for View Generalization in Robotic Policy Learning

- **作者**: Sen Wang, Huaiyi Dong, Jingyi Tian, Jiayi Li, Zhuo Yang, Tongtong Cao, Anlin Chen, Shuang Wu, Le Wang, Sanping Zhou
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.29192v1)
- **发表日期**: 2026-03-31
- **匹配关键词**: gaussian splatting, 3D gaussian splatting
- **arXiv**: [2603.29192v1](http://arxiv.org/abs/2603.29192v1)
- **📥 PDF**: 已下载至本地 (`2603.29192v1_Efficient_Camera_Pose_Augmentation_for_View_Generalization_in_Robotic_Policy_Learning.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 当前以二维为中心的视觉运动策略在新视角泛化方面存在明显不足，因其对静态观测的依赖阻碍了在未见视角下保持动作映射的一致性。为此，我们提出GenSplat——一种前馈式三维高斯溅射框架，通过新颖视角渲染促进视角泛化的策略学习。GenSplat采用置换等变架构，仅需单次前向传播即可从稀疏、未校准的输入中重建高保真三维场景。为确保结构完整性，我们设计了一种三维先验蒸馏策略，对三维高斯溅射优化过程进行正则化，避免纯光度监督中常见的几何塌陷问题。通过从这些稳定的三维表征中渲染多样化的合成视角，我们在训练过程中系统性地扩展了观测流形。这种增强迫使策略将其决策建立在底层三维结构之上，从而确保在基线方法严重失效的剧烈空间扰动下仍能实现鲁棒执行。

---

### 4. LatentPilot: Scene-Aware Vision-and-Language Navigation by Dreaming Ahead with Latent Visual Reasoning

- **作者**: Haihong Hao, Lei Chen, Mingfei Han, Changlin Li, Dong An, Yuqiang Yang, Zhihui Li, Xiaojun Chang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.29165v1)
- **发表日期**: 2026-03-31
- **匹配关键词**: VLN, vision-and-language navigation, navigation
- **arXiv**: [2603.29165v1](http://arxiv.org/abs/2603.29165v1)
- **📥 PDF**: 已下载至本地 (`2603.29165v1_LatentPilot_Scene-Aware_Vision-and-Language_Navigation_by_Dreaming_Ahead_with_Latent_Visual_Reasonin.pdf`)
- **🔓 开源**: PROJECT_PAGE
- **中文摘要**: 现有视觉语言导航模型主要基于过去和当前的视觉观察进行推理，而很大程度上忽略了由动作引发的未来视觉动态变化。这导致它们往往缺乏对动作与视觉世界变化之间因果关系的有效理解，从而限制了稳健的决策能力。相比之下，人类能够利用动作动态因果关系来想象近期未来，这增强了对环境的理解并优化了导航选择。受此能力启发，我们提出LatentPilot这一新范式，该范式在训练阶段利用未来观察作为宝贵数据源来学习动作条件化的视觉动态，同时在推理阶段无需访问未来帧。具体而言，我们设计了一种飞轮式训练机制：通过迭代收集在线策略轨迹并重新训练模型以更好地匹配智能体行为分布，当智能体偏离过度时触发专家接管机制。LatentPilot进一步在无显式监督的情况下学习视觉潜在标记；这些潜在标记在连续潜在空间中进行全局注意力计算，并跨步骤传递，既作为当前输出又作为下一时间步的输入，从而使智能体能够预演未来并推理动作将如何影响后续观察。在R2R-CE、RxR-CE和R2R-PE基准测试中取得了新的最优结果，跨多样环境的真实机器人测试也验证了LatentPilot对场景中环境-动作动态关系的卓越理解能力。项目页面：https://abdd.top/latentpilot/

---

### 5. FocusVLA: Focused Visual Utilization for Vision-Language-Action Models

- **作者**: Yichi Zhang, Weihao Yuan, Yizhuo Zhang, Xidong Zhang, Jia Wan
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.28740v1)
- **发表日期**: 2026-03-30
- **匹配关键词**: vision-language-action model, VLA, vision-language-action
- **arXiv**: [2603.28740v1](http://arxiv.org/abs/2603.28740v1)
- **📥 PDF**: 已下载至本地 (`2603.28740v1_FocusVLA_Focused_Visual_Utilization_for_Vision-Language-Action_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作模型通过将策略建立在丰富的视觉-语言信息基础上，提升了动作生成能力。然而，当前自回归策略面临三大瓶颈：(1) 架构偏差导致模型忽视视觉细节，(2) 过多的视觉标记使注意力难以聚焦关键区域，(3) 任务无关的视觉信息引入显著噪声——这些问题共同严重影响了动作生成质量。本文研究如何有效利用不同视觉表征进行动作生成。为此，我们首先通过实证验证了上述问题，并证明视觉-语言-动作模型的性能主要受限于视觉信息的利用方式，而非视觉表征的质量。基于这些发现，我们提出FocusVLA这一新范式，通过引导模型关注任务相关的视觉区域，有效建立视觉到动作的桥梁。具体而言，我们首先提出模态级联注意力机制以消除捷径路径，从而强制视觉-语言-动作模型依赖任务相关的视觉细节进行动作生成。此外，我们提出聚焦注意力机制，动态选择任务相关的视觉区块以控制信息量，同时显式调节其影响以抑制任务无关噪声。在模拟与真实机器人基准测试中的大量实验表明，FocusVLA不仅能有效利用视觉细节执行灵巧操作，还能显著提升多种任务的性能表现并加速收敛过程。

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
- **中文摘要**: 机器人建图系统通常基于机器人自身的传感器和摄像头构建度量语义场景表征。然而，这种"第一人称"地图会受限于机器人的物理形态或技能配置，可能导致环境中的许多方面未被探索。例如，机器人可能无法打开抽屉或接触壁柜。从这个意义上说，地图表征并不完整，需要能力更强的机器人来填补空白。我们通过利用人类佩戴Project Aria眼镜自然探索场景时捕获的自我中心数据来缩小现有方法的盲区，为将人类对可动部件的认知直接迁移至任何可部署机器人提供了途径。实验证明，通过简单启发式方法，我们能够利用自我中心数据重建可动物体部件的模型，其质量可与基于其他输入模态的最先进方法相媲美。我们还展示了如何将这些模型整合到三维场景图表征中，从而提升对物体动态及物体-容器关系的理解。最后，我们通过波士顿动力Spot机器人执行移动操作任务的应用案例，证明这些可动三维场景图能增强机器人能力——仅以三维场景图为输入，机器人即可成功定位并取出隐藏的目标物品。

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
- **中文摘要**: 开放词汇目标导航（OVON）要求具身智能体在未知环境中定位语言指定的目标。现有零样本方法通常在局部观测下对密集边界点进行推理，导致路径选择不稳定、重复访问和无效动作开销。本文提出DRIVE-Nav结构化框架，该框架围绕持久性方向而非原始边界组织探索。通过更完整地检查已遇到的方向，并将后续决策限制在前向240度视野范围内仍相关的方向上，DRIVE-Nav减少了冗余访问并提升了路径效率。该框架从加权快速行进法（FMM）路径中提取并追踪方向候选，维护代表性视角进行语义检查，结合视觉语言引导的提示增强与跨帧验证以提高定位可靠性。在HM3D-OVON、HM3Dv2和MP3D数据集上的实验表明，该方法在整体性能与路径效率方面均有显著提升。在HM3D-OVON任务中，DRIVE-Nav实现了50.2%的成功率（SR）和32.6%的路径长度加权成功率（SPL），较先前最佳方法分别提升1.9% SR和5.6% SPL。该方法同时在HM3Dv2和MP3D数据集上取得最优SPL指标，并成功迁移至实体人形机器人平台。实际场景部署验证了其有效性。项目页面：https://coolmaoguo.github.io/drive-nav-page/

---

### 8. ManipArena: Comprehensive Real-world Evaluation of Reasoning-Oriented Generalist Robot Manipulation

- **作者**: Yu Sun, Meng Cao, Ping Yang, Rongtao Xu, Yunxiao Yan, Runze Xu, Liang Ma, Roy Gan, Andy Zhai, Qingxuan Chen, Zunnan Xu, Hao Wang, Jincheng Yu, Lucy Liang, Qian Wang, Ivan Laptev, Ian D Reid, Xiaodan Liang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.28545v1)
- **发表日期**: 2026-03-30
- **匹配关键词**: mobile manipulation, VLA, vision-language-action
- **arXiv**: [2603.28545v1](http://arxiv.org/abs/2603.28545v1)
- **📥 PDF**: 已下载至本地 (`2603.28545v1_ManipArena_Comprehensive_Real-world_Evaluation_of_Reasoning-Oriented_Generalist_Robot_Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作模型与世界模型已成为通用机器人智能领域备受关注的研究范式，但其发展受限于缺乏能够反映真实世界部署需求的可靠评估体系。现有基准测试大多以仿真环境为核心，虽具备可控性优势，却难以捕捉由感知噪声、复杂接触动力学、硬件约束及系统延迟等因素造成的现实鸿沟。此外，分散在不同机器人平台上的现实世界评估导致公平性与可复现性难以保障。为应对这些挑战，我们提出ManipArena标准化评估框架，旨在构建仿真与真实执行的桥梁。该框架包含20类多样化任务与10,812条专家示范轨迹，重点关注需要语义与空间推理的认知型操作任务，通过受控分布外设置支持多层级泛化能力评估，并突破桌面场景局限引入长时程移动操作。该体系进一步提供丰富的传感诊断数据（包括底层运动信号），以及通过高精度三维扫描构建的同步虚实环境。这些特性共同为视觉-语言-动作模型与世界模型方法提供了公平、真实且可复现的评估方案，为具身智能系统的诊断与演进奠定了可扩展的基础。

---

### 9. Tele-Catch: Adaptive Teleoperation for Dexterous Dynamic 3D Object Catching

- **作者**: Weiguang Zhao, Junting Dong, Rui Zhang, Kailin Li, Qin Zhao, Kaizhu Huang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.28427v1)
- **发表日期**: 2026-03-30
- **匹配关键词**: diffusion policy
- **arXiv**: [2603.28427v1](http://arxiv.org/abs/2603.28427v1)
- **📥 PDF**: 已下载至本地 (`2603.28427v1_Tele-Catch_Adaptive_Teleoperation_for_Dexterous_Dynamic_3D_Object_Catching.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 遥操作是将人类灵巧性转移至机器人的关键范式，但现有研究多聚焦于初始静止物体的抓取或操控任务。动态物体捕捉——即物体在接触前处于运动状态——仍属探索不足的领域。纯遥操作常因时机、位姿与施力误差在此类任务中失效，这凸显了需要将人类指令与自主策略相结合的共享控制机制。为此，我们提出Tele-Catch动态捕捉灵巧手遥操作系统框架。其核心是设计了动态感知自适应融合机制DAIM，通过将基于数据手套的遥操作信号融入扩散策略去噪过程实现共享控制，该机制能依据交互物体状态自适应调节控制策略。为提升策略鲁棒性，我们提出DP-U3R方法，将点云观测中提取的无监督几何表征融入扩散策略学习，实现几何感知决策。大量实验表明，Tele-Catch在动态捕捉任务中显著提升了精度与鲁棒性，同时在不同灵巧手构型及未见物体类别上均展现出持续的性能增益。

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
- **中文摘要**: 聚合编程是一种基于场的协调范式，经过十余年的探索，已在传感器网络、机器人技术和物联网等多个领域成功应用，并实现了多种编程语言版本，如Protelis、ScaFi（Scala）和FCPP（C++）。近期研究方向将机器学习与聚合计算相结合，旨在支持大规模分布式学习，并为实现学习算法提供新的抽象层。然而，现有实现并未面向数据科学从业者——他们主要使用Python这一数据科学与机器学习领域的事实标准语言，该语言拥有丰富成熟的生态系统。Python在其他应用场景（如教育及机器人技术领域，例如通过ROS系统）同样具备优势。为填补这一空白，我们推出了Phyelds——一个用于聚合编程的Python库。Phyelds完整实现了场演算计算模型，同时保持轻量化设计，提供符合Python风格的API架构，旨在与Python机器学习生态系统无缝集成。本文阐述了Phyelds的设计与实现，并通过从经典聚合计算模式到联邦学习协调，再到与广泛使用的多智能体强化学习模拟器的集成案例，展示了其跨领域应用的广泛适应性。

---

### 2. Reconfiguration of supernumerary robotic limbs for human augmentation

- **作者**: Mustafa Mete, Anastasia Bolotnikova, Alexander Schuessler, Jamie Paik
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.29808v1)
- **发表日期**: 2026-03-31
- **匹配关键词**: human-robot collaboration
- **arXiv**: [2603.29808v1](http://arxiv.org/abs/2603.29808v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 可穿戴机器人旨在通过个性化交互，无缝适应人类及其所处环境。现有的超数机器人肢体通过增加额外肢体来增强人类物理能力，但迄今主要针对结构化工业场景中的特定任务开发，限制了其在动态非结构化环境中的适应性。本文提出一种基于人类增强定量分析的新型可重构SRL框架，以指导开发适用于多样化场景的适应性更强的SRL系统。该框架揭示了SRL配置如何影响工作空间扩展与人机协作。我们定义了人类增强比率来评估协作空间、可见扩展工作空间及不可见扩展工作空间，从而为特定任务系统化选择SRL的布局、形态和自主性。运用这些指标，我们展示了定量增强分析如何指导SRL的重构与控制，以更好地匹配任务需求。通过由折纸启发的模块化元件构成的可重构SRL实验，我们验证了所提方法的有效性。研究结果表明，基于定量人类增强分析的可重构SRL，为日常环境中提供适应性人类增强与辅助开辟了新视角。

---

### 3. SafeDMPs: Integrating Formal Safety with DMPs for Adaptive HRI

- **作者**: Soumyodipta Nath, Pranav Tiwari, Ravi Prakash
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.29708v1)
- **发表日期**: 2026-03-31
- **匹配关键词**: collaborative robot, HRI
- **arXiv**: [2603.29708v1](http://arxiv.org/abs/2603.29708v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 在人类中心环境中运行的机器人必须既具备抗干扰的鲁棒性，又能确保可证明的防碰撞安全性。如何同时高效地实现这两个特性仍是核心挑战。动态运动基元（DMPs）虽具有内在稳定性并能通过单次演示实现泛化，但缺乏形式化的安全保障。相反，控制屏障函数（CBFs）等形式化方法虽能提供可证明的安全性，却常依赖计算密集的实时优化，难以应用于高频控制场景。本文提出的SafeDMPs框架创新性地解决了这一矛盾。我们将DMPs的闭式求解效率与动态鲁棒性，同基于时空管道（STTs）推导出的可证明安全、非优化型控制律相结合。这种协同机制不仅能生成抗干扰且适应新目标的运动轨迹，还能确保规避静态与动态障碍物。针对传统需要在线优化求解的问题，本方法实现了闭式解。在七自由度机械臂上的实验表明，SafeDMPs相比基于优化的基准方法在速度上提升数个数量级，且精度更高，为实时、安全、协作的机器人系统提供了理想解决方案。

---

### 4. RAAP: Retrieval-Augmented Affordance Prediction with Cross-Image Action Alignment

- **作者**: Qiyuan Zhuang, He-Yang Xu, Yijun Wang, Xin-Yang Zhao, Yang-Yang Li, Xiu-Shen Wei
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.29419v1)
- **发表日期**: 2026-03-31
- **匹配关键词**: affordance
- **arXiv**: [2603.29419v1](http://arxiv.org/abs/2603.29419v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: GITHUB, PROJECT_PAGE
  - 链接：https://github.com/SEU-VIPGroup/RAAP.
- **中文摘要**: 理解物体可供性是使机器人能够在多样化和非结构化环境中进行有目的、细粒度交互的关键。然而，现有方法要么依赖检索机制——由于数据稀疏性和覆盖范围不足而显得脆弱，要么依赖大规模模型——在应用于未见类别时经常出现接触点定位错误和接触后动作预测偏差，从而阻碍了鲁棒的泛化能力。我们提出检索增强可供性预测框架，该框架将可供性检索与基于对齐的学习相统一。通过解耦静态接触点定位与动态动作方向预测，RAAP通过稠密对应关系迁移接触点，并借助检索增强对齐模型预测动作方向——该模型采用双权重注意力机制整合多参考信息。在DROID和HOI4D数据集的紧凑子集上训练（每个任务仅需数十个样本），RAAP在未见物体和类别上均表现出稳定性能，并在仿真环境与现实世界中实现了零样本机器人操作。项目网站：https://github.com/SEU-VIPGroup/RAAP。

---

### 5. Learning Semantic Priorities for Autonomous Target Search

- **作者**: Max Lodel, Nils Wilde, Robert Babuška, Javier Alonso-Mora
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.29391v1)
- **发表日期**: 2026-03-31
- **匹配关键词**: exploration
- **arXiv**: [2603.29391v1](http://arxiv.org/abs/2603.29391v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 在机器人搜救任务中，利用语义特征能够提升未知环境下目标搜索的效率。当前的目标搜索方法依赖于对相似领域大规模数据集的训练，这限制了其在不同环境中的适应性。然而，人类专家具备关于语义关系的高层次知识，这些知识对于在多样且先前未见的环境中有效引导机器人进行目标搜索任务至关重要。本文提出一种目标搜索方法，该方法利用专家输入来训练语义优先级模型。通过将学习到的优先级应用于基于组合优化的前沿探索规划器，我们的方法实现了由语义特征驱动的高效目标搜索，同时确保了鲁棒性和完全覆盖。所提出的语义优先级模型通过多个模拟专家指导目标搜索的合成数据集进行训练。在先前未见的环境中的仿真测试表明，与覆盖驱动探索规划器相比，我们的方法始终能够实现更快的目标恢复。

---

### 6. Kernel-SDF: An Open-Source Library for Real-Time Signed Distance Function Estimation using Kernel Regression

- **作者**: Zhirui Dai, Tianxing Fan, Mani Amani, Jaemin Seo, Ki Myung Brian Lee, Hyondong Oh, Nikolay Atanasov
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.29227v1)
- **发表日期**: 2026-03-31
- **匹配关键词**: motion planning, navigation
- **arXiv**: [2603.29227v1](http://arxiv.org/abs/2603.29227v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: CODE
- **中文摘要**: 准确高效的环境表征对于运动规划、操作与导航等机器人应用至关重要。有符号距离函数（SDF）已成为编码障碍物边界距离的强大表征方法，能够支持高效的碰撞检测与轨迹优化技术。然而，现有SDF重建方法在处理流式传感器数据的大规模不确定性感知SDF估计时存在局限：基于体素的方法受限于固定分辨率且缺乏不确定性量化，神经网络方法需要大量训练时间，而高斯过程（GP）方法则在可扩展性、符号估计和不确定性校准方面面临挑战。本文开发了开源库Kernel-SDF，采用核回归方法实现具有校准不确定性量化的实时SDF学习。该方法包含通过核回归学习连续占据场的前端模块，以及利用前端表面边界样本通过GP回归估计精确SDF的后端模块。Kernel-SDF能够实时提供精确的SDF值、SDF梯度、SDF不确定性和网格构建功能。评估结果表明，与现有方法相比，Kernel-SDF在保持实时性能的同时实现了更高的精度，适用于各类需要可靠不确定性感知几何信息的机器人应用场景。

---

### 7. Why That Robot? A Qualitative Analysis of Justification Strategies for Robot Color Selection Across Occupational Contexts

- **作者**: Jiangen He, Wanqi Zhang, Jessica K. Barfield
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.28919v1)
- **发表日期**: 2026-03-30
- **匹配关键词**: human-robot interaction, HRI
- **arXiv**: [2603.28919v1](http://arxiv.org/abs/2603.28919v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 随着机器人日益融入劳动力市场，人机交互领域必须解决隐性社会偏见如何影响用户偏好的问题。本文研究了用户如何合理化他们在不同职业场景下对肤色和拟人化特征各异的机器人的选择。通过对1,038名参与者提供的4,146条开放式理由进行定性分析，我们绘制了四种专业情境下驱动机器人颜色选择的推理框架。通过人机共识验证（κ=0.73），我们开发并验证了一个多维度的综合编码体系。研究结果表明，虽然功利主义的"功能论"是主导的合理化策略（52%），但参与者系统性地调整这些实用理由，以符合既有的种族与职业刻板印象。此外，我们发现偏见常在意识合理化层面之下运作：接触种族刻板印象暗示会显著改变参与者的颜色选择，但其口头解释仍被标准的情感或任务相关推理所掩盖。研究还发现人口背景显著影响合理化策略，且机器人形态强烈调节颜色解读。具体而言，当机器人高度拟人化时，用户会逐渐从功能性推理转向"以机器为中心"的去种族化解释。基于这些实证结果，我们提出了可操作的设计建议，以帮助减少未来劳动力机器人对社会偏见的延续。

---

### 8. Bootstrap Perception Under Hardware Depth Failure for Indoor Robot Navigation

- **作者**: Nishant Pushparaju, Vivek Mattam, Aliasghar Arab
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.28890v1)
- **发表日期**: 2026-03-30
- **匹配关键词**: robot navigation, navigation
- **arXiv**: [2603.28890v1](http://arxiv.org/abs/2603.28890v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出一种在硬件深度失效情况下的室内机器人导航自举感知系统。在走廊环境中，飞行时间相机在反光表面会损失高达78%的深度像素，而仅靠二维激光雷达无法感知扫描平面上方的障碍物。本系统利用这种失效的自参照特性：传感器存留的有效像素可将学习型单目深度校准至公制尺度，从而实现无需外部数据的自主补全。该架构构建了失效感知的层级化传感体系，在传感器正常时保持保守策略，在失效时进行填补：激光雷达始终作为几何基准锚点，硬件深度数据在有效区域予以保留，学习型深度仅在需要时介入。在走廊环境与动态行人场景评估中，选择性融合策略使代价地图的障碍物覆盖率较单一激光雷达提升55-110%。经蒸馏的紧凑学生模型在Jetson Orin Nano平台上以218帧/秒运行，在闭环仿真中实现9/10的导航成功率且零碰撞，以基础模型极小部分的计算成本达到了真实深度基准线的性能水平。

---

### 9. Serialized Red-Green-Gray: Quicker Heuristic Validation of Edges in Dynamic Roadmap Graphs

- **作者**: Yulie Arad, Stav Ashur, Marta Markowicz, James D. Motes, Marco Morales, Nancy M. Amato
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.28674v1)
- **发表日期**: 2026-03-30
- **匹配关键词**: motion planning
- **arXiv**: [2603.28674v1](http://arxiv.org/abs/2603.28674v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 在动态环境（如机器人仓库）中进行运动规划时，需要快速适应障碍物位姿的频繁变化。传统的基于路线图的方法在此类场景中面临挑战，它们要么依赖低效的路线图重建，要么需要通过昂贵的碰撞检测来更新现有路线图。为解决这些问题，我们提出了红-绿-灰（RGG）框架，该方法基于SPITE算法，通过保守几何近似将路线图边快速分类为无效（红）、有效（绿）或不确定（灰）。序列化RGG通过批量序列化与向量化实现了高性能变体，支持高效的GPU加速。实验结果表明，RGG能有效减少需要完全验证的未知边数量，而SerRGG相比顺序执行方案实现了2-9倍的加速。这种几何精度与计算速度的结合，使SerRGG在时间敏感的机器人应用中具有显著优势。

---

### 10. EBuddy: a workflow orchestrator for industrial human-machine collaboration

- **作者**: Michele Banfi, Rocco Felici, Stefano Baraldo, Oliver Avram, Anna Valente
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.28579v1)
- **发表日期**: 2026-03-30
- **匹配关键词**: human-robot collaboration, collaborative robot
- **arXiv**: [2603.28579v1](http://arxiv.org/abs/2603.28579v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 本文介绍EBuddy——一种面向工业环境中自然人机协作的语音引导工作流协调系统。该系统针对工具密集型工作流中的常见瓶颈：专家经验虽有效但难以规模化推广，且当操作流程在不同人员和作业时段临时重构时，执行质量往往下降。EBuddy将专家实践转化为有限状态机驱动的应用程序，在运行时提供可解释的决策框架（当前状态与允许操作），使语音请求能在状态约束下被准确解析，同时系统执行并监控相应的工具交互。通过模块化工作流组件，EBuddy协调包括图形界面软件和协作机器人在内的异构资源，借助自动语音识别与意图理解技术实现全语音交互。在基于人机协作的定向能量沉积叶轮叶片检测与修复准备工业试点中，该系统在人员培训、三维扫描处理及修复程序生成等全流程环节显著缩短作业时间，同时保持操作可重复性并降低人员工作负荷。

---

### 11. A Foldable and Agile Soft Electromagnetic Robot for Multimodal Navigation in Confined and Unstructured Environments

- **作者**: Zhihao Lv, Xiaoyong Zhang, Mengfan Zhang, Xiaoyu Song, Xingyue Liu, Yide Liu, Shaoxing Qu, Guoyong Mao
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.28362v1)
- **发表日期**: 2026-03-30
- **匹配关键词**: navigation
- **arXiv**: [2603.28362v1](http://arxiv.org/abs/2603.28362v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 多模态运动对动物在非结构化野生环境中的适应性至关重要。同样，在具有粘弹性黏液、复杂皱襞及贲门等狭窄括约肌特征的人类胃肠道中，多模态运动对于执行任务的小型软体机器人也极为重要。本文提出一种小型紧凑、可折叠且坚固的软体电磁机器人（M-SEMR），其具备九种以上运动模式，专为此类场景设计。该机器人采用六辐弹性体结构，内部嵌有液态金属通道，在静磁场中通过拉普拉斯力驱动，能够在不同运动模式间实现快速切换（<0.35秒）。它展现出卓越的敏捷性，包括高速滚动（818毫米/秒，26体长/秒）、全向爬行、跳跃和游泳。特别值得注意的是，该机器人可通过折叠将体积缩小79%，从而穿越狭窄空间。我们进一步验证了其在复杂地形上的导航能力，包括离散障碍物、粘弹性明胶表面、粘性流体及模拟生物组织。该系统为开发面向未来生物医学应用的高机动性软体机器人提供了一种通用策略。

---

