# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-05-15 08:02

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 4/20 篇提供

**🌟 Highlight**: 18 篇 | **📌 Poster**: 2 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. FrameSkip: Learning from Fewer but More Informative Frames in VLA Training

- **作者**: Bin Yu, Shijie Lian, Xiaopeng Lin, Zhaolong Shen, Yuliang Wei, Changti Wu, Hang Yuan, Haishan Liu, Bailing Wang, Cong Huang, Kai Chen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.13757v1)
- **发表日期**: 2026-05-13
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2605.13757v1](http://arxiv.org/abs/2605.13757v1)
- **📥 PDF**: 已下载至本地 (`2605.13757v1_FrameSkip_Learning_from_Fewer_but_More_Informative_Frames_in_VLA_Training.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）策略通常通过遥操作采集的密集机器人演示轨迹进行训练，其训练方式是对每一帧记录进行等权重采样。我们认为这种惯例造成了时间维度的监督不平衡：长时间的低变化片段主导了训练流，而操作关键性过渡（如对齐、接触、抓取和释放）却仅稀疏出现。为此，我们提出FrameSkip——一种数据层帧选择框架，通过动作变化度、视觉-动作一致性、任务进度先验和夹爪过渡保留性对轨迹帧进行评分，并在目标保留率下将训练样本重新映射至高重要性帧。由于FrameSkip仅在数据加载器中运行，因此不改变VLA架构、动作头、训练目标和推理流程。在RoboCasa-GR1、SimplerEnv和LIBERO基准测试中，FrameSkip相较于全帧训练及简单帧选择变体，在成功保留权衡上取得更优表现：在三个基准测试中实现76.15%的宏观平均成功率（全帧训练为66.50%），同时主设置下仅保留20%独特帧的压缩轨迹视图。

---

### 2. LEXI-SG: Monocular 3D Scene Graph Mapping with Room-Guided Feed-Forward Reconstruction

- **作者**: Christina Kassab, Hyeonjae Gil, Matías Mattamala, Ayoung Kim, Maurice Fallon ⭐
  - **高亮作者**: Maurice Fallon
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.13741v1)
- **发表日期**: 2026-05-13
- **匹配关键词**: scene graph, robot navigation, semantic scene graph, navigation
- **arXiv**: [2605.13741v1](http://arxiv.org/abs/2605.13741v1)
- **📥 PDF**: 已下载至本地 (`2605.13741v1_LEXI-SG_Monocular_3D_Scene_Graph_Mapping_with_Room-Guided_Feed-Forward_Reconstruction.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://ori-drs.github.io/lexisg-web/.
- **中文摘要**: 场景图正成为机器人导航的标准表示方法，能够提供层次化的几何与语义场景理解。然而，现有场景图建图方法大多依赖深度相机或激光雷达传感器。本研究提出LEXI-SG——首个仅使用RGB相机输入即可实现开放词汇3D场景图的稠密单目视觉建图系统。该方法利用开放词汇基础模型的语义先验将场景划分为不同房间，并将前馈重建延迟至每个房间被完整观测时——从而在避免滑动窗口尺度不一致问题的同时实现可扩展的稠密建图。我们提出基于房间的因子图框架，在保持局部地图一致性的同时全局对齐房间重建结果，并自然构建语义场景图的层次结构。在每个房间内，我们进一步支持开放词汇的物体分割与追踪。我们在Habitat-Matterport 3D室内场景及自采集的第一人称办公室序列上验证了LEXI-SG的性能，并与现有前馈SLAM方法及经典场景图基线进行了对比评估。实验表明，本方法在轨迹估计与稠密重建方面表现更优，同时在开放词汇分割任务中具有竞争力。LEXI-SG证明：仅凭单目RGB输入即可实现精确、可扩展的开放词汇3D场景图。项目主页及办公室序列详见：https://ori-drs.github.io/lexisg-web/。

---

### 3. Robot Squid Game: Quadrupedal Locomotion for Traversing Narrow Tunnels

- **作者**: Amir Hossain Raj, Dibyendu Das, Xuesu Xiao
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.13665v1)
- **发表日期**: 2026-05-13
- **匹配关键词**: navigation
- **arXiv**: [2605.13665v1](http://arxiv.org/abs/2605.13665v1)
- **📥 PDF**: 已下载至本地 (`2605.13665v1_Robot_Squid_Game_Quadrupedal_Locomotion_for_Traversing_Narrow_Tunnels.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 四足机器人在搜救任务和基础设施检查等关键应用中展现出穿越复杂地形的卓越潜力。然而，在隧道、洞穴和坍塌结构等受限三维环境中的自主穿越仍是一项重大挑战。现有方法常受限于僵化的步态模式、对多样化几何结构的适应性不足，以及过度简化的环境假设。本文提出一种结合程序化环境生成与策略蒸馏的强化学习框架，使机器人能够在各种隧道构型中实现稳健运动。我们的方法采用师生训练范式：在程序化生成的隧道几何结构中训练的专业化专家策略，将其知识迁移至统一的通用学生策略。该策略无需在端到端强化学习训练中进行复杂的奖励塑形，通过将复杂任务分解为更易学习的子模块来简化训练流程。通过在训练中合成多样化隧道结构并将导航策略蒸馏为可泛化策略，我们的方法在传统方法失效的复杂空间约束下实现了持续穿越。仿真与真实世界实验均证明，该方法能使四足机器人成功穿越具有挑战性的受限隧道环境。

---

### 4. Guide, Think, Act: Interactive Embodied Reasoning in Vision-Language-Action Models

- **作者**: Yiran Ling, Qing Lian, Jinghang Li, Qing Jiang, Tianming Zhang, Xiaoke Jiang, Chuanxiu Liu, Jie Liu, Lei Zhang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.13632v1)
- **发表日期**: 2026-05-13
- **匹配关键词**: vision-language-action model, affordance, VLA, vision-language-action
- **arXiv**: [2605.13632v1](http://arxiv.org/abs/2605.13632v1)
- **📥 PDF**: 已下载至本地 (`2605.13632v1_Guide,_Think,_Act_Interactive_Embodied_Reasoning_in_Vision-Language-Action_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 本文提出GTA-VLA（引导-思考-行动）框架，这是一种交互式视觉-语言-动作（VLA）框架，通过允许用户使用显式视觉线索引导机器人策略，实现空间可操控的具体推理。现有VLA模型学习从多模态观测到机器人动作的直接"感知-行动"映射。虽然这种紧密耦合的策略在训练分布内有效，但在域外偏移下表现脆弱，且当失败发生时难以修正。尽管近期具体思维链方法暴露了中间推理过程，但仍缺乏融入人类空间引导的机制，限制了其解决视觉歧义或从错误中恢复的能力。为弥补这一缺口，本框架允许用户可选地使用空间先验（如功能点、边界框和轨迹）引导策略，后续推理过程可直接基于这些输入。基于这些输入，模型生成统一的空间-视觉思维链，将外部引导与内部任务规划相结合，使人类视觉意图与自主决策对齐。为便于实际部署，我们进一步将推理模块与轻量级反应式动作头耦合，实现高效动作执行。大量实验证明了该方法的有效性。在域内SimplerEnv WidowX基准测试中，本框架实现了81.2%的最优成功率。在域外视觉偏移和空间歧义场景下，单次视觉交互即可显著提升任务成功率，凸显了交互式推理在具体控制中实现失败恢复的价值。项目详情请见：https://signalispupupu.github.io/GTA-VLA_ProjPage/

---

### 5. AttenA+: Rectifying Action Inequality in Robotic Foundation Models

- **作者**: Daojie Peng, Fulong Ma, Jiahang Cao, Qiang Zhang, Xupeng Xie, Jian Guo, Ping Luo, Andrew F. Luo, Boyu Zhou, Jun Ma
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.13548v1)
- **发表日期**: 2026-05-13
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2605.13548v1](http://arxiv.org/abs/2605.13548v1)
- **📥 PDF**: 已下载至本地 (`2605.13548v1_AttenA+_Rectifying_Action_Inequality_in_Robotic_Foundation_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 现有的机器人基础模型虽然功能强大，但都隐含着一个时间同质性的假设：在优化过程中将所有动作视为同等重要。这种从语言模型继承而来的"扁平化"训练范式，对操作任务中固有的物理层级结构视而不见。实际上，机器人轨迹本质上是异质的——低速运动段往往通过高精度交互决定任务成败，而高速运动段则作为容错性过渡存在。这种均匀损失权重与物理关键性之间的错位，从根本上限制了当前视觉-语言-动作模型和世界-动作模型在复杂长时域任务中的性能。为解决这一问题，我们提出AttenA+——一个与架构无关的框架，通过速度驱动的动作注意力机制优先关注运动学关键片段。通过基于逆速度场重新加权训练目标，AttenA+自然地将模型学习能力与操作任务的物理需求对齐。作为即插即用的增强模块，AttenA+无需修改结构或增加参数即可集成到现有骨干网络中。大量实验表明，AttenA+显著提升了当前最优模型的性能上限：在Libero基准测试中将OpenVLA-OFT提升至98.6%（+1.5%），在RoboTwin 2.0上将FastWAM推至92.4%（+0.6%）。在Franka机械臂上的真实世界验证进一步展示了其鲁棒性与跨任务泛化能力。我们的研究表明，挖掘动作序列的内在结构先验，为标准的扩展定律提供了高效且具有物理感知的补充，为通用机器人控制开辟了新路径。

---

### 6. CUBic: Coordinated Unified Bimanual Perception and Control Framework

- **作者**: Xingyu Wang, Pengxiang Ding, Jingkai Xu, Donglin Wang, Zhaoxin Fan
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.13452v1)
- **发表日期**: 2026-05-13
- **匹配关键词**: bimanual manipulation, diffusion policy
- **arXiv**: [2605.13452v1](http://arxiv.org/abs/2605.13452v1)
- **📥 PDF**: 已下载至本地 (`2605.13452v1_CUBic_Coordinated_Unified_Bimanual_Perception_and_Control_Framework.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 近期，视觉运动策略学习的进展使机器人能够直接从视觉输入执行控制。然而，将这种端到端学习从单臂操作扩展到双臂操作仍具挑战性，原因在于双臂既需要独立感知，又需要协调交互。现有方法通常偏向某一侧——要么解耦双臂以避免干扰，要么通过强跨臂耦合实现协调——因此缺乏统一的处理方式。我们提出CUBic，一种用于双臂感知与控制的协调统一框架，将双臂协调重新定义为统一的感知建模问题。CUBic学习一种连接感知与控制的共享标记化表征，其中独立性与协调性从结构本身内在涌现，而非依赖人工设计的耦合。我们的方法整合了三个组件：单向感知聚合、通过两个共享映射码本实现的双向感知协调，以及统一的感知到控制扩散策略。在RoboTwin基准上的大量实验表明，CUBic持续超越标准基线，在协调精度和任务成功率上相较于最先进的视觉运动基线取得了显著提升。

---

### 7. Asymptotically Optimal Ergodic Coverage on Generalized Motion Fields

- **作者**: Christian Hughes, Yilang Liu, Yanis Lahrach, Julia Engdahl, Houston Warren, Darrick Lee, Fabio Ramos, Travis Miles, Ian Abraham
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.13442v1)
- **发表日期**: 2026-05-13
- **匹配关键词**: path planning, exploration
- **arXiv**: [2605.13442v1](http://arxiv.org/abs/2605.13442v1)
- **📥 PDF**: 已下载至本地 (`2605.13442v1_Asymptotically_Optimal_Ergodic_Coverage_on_Generalized_Motion_Fields.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 在偏远和极端环境中的自主机器人探索，使科学家能够模拟由连续变形流场描述的复杂输运现象和集体行为。尽管这些环境自然被建模为时变域，但大多数自适应探索方法假设静态环境，无法提供充分的覆盖或满足任何形式保证。这在海洋学中尤为突出，自主水下系统（UxS）对计算和载荷有高度限制，需要路径规划方法在开环和欠驱动条件下产生稳健的数据收集策略。

为解决上述问题，本文提出将自适应搜索建模为遍历覆盖问题，并研究在具有流致动力学的演化域上，从遍历意义上认证覆盖性能。我们扩展了近期将最大均值差异（MMD）作为函数遍历度量的工作，推导出一种流自适应公式，明确将域演化纳入覆盖目标。研究表明，该方法在环境流中保留了遍历覆盖保证，并通过整合环境动力学，在欠驱动甚至开环规划场景中实现有效探索。实验验证了该方法能泛化至包括海洋探索、人类及牲畜运动追踪在内的多种时空过程。基于空中和腿式机器人平台的物理实验证实，我们能在非凸、受限流环境中，在尊重机器人动力学的同时实现遍历覆盖。

---

### 8. RotVLA: Rotational Latent Action for Vision-Language-Action Model

- **作者**: Qiwei Li, Xicheng Gong, Xinghang Li, Peiyan Li, Quanyun Zhou, Hangjun Ye, Jiahuan Zhou, Yadong Mu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.13403v1)
- **发表日期**: 2026-05-13
- **匹配关键词**: vision-language-action model, VLA, vision-language-action
- **arXiv**: [2605.13403v1](http://arxiv.org/abs/2605.13403v1)
- **📥 PDF**: 已下载至本地 (`2605.13403v1_RotVLA_Rotational_Latent_Action_for_Vision-Language-Action_Model.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 潜在动作模型（LAMs）已成为视觉-语言-动作（VLA）模型预训练中处理异构数据集的有效范式，能够跨不同实体提供统一的动作空间。然而，现有LAMs通常依赖离散量化编码-解码流程，这可能导致帧重建行为琐碎、表征能力受限以及缺乏物理意义的结构。我们提出RotVLA，一种基于连续旋转潜在动作表征的VLA框架。潜在动作被建模为SO(n)群元素，具备连续性、组合性以及与真实世界动作动力学对齐的结构化几何特性。三重帧学习框架进一步强化了有意义的时序动态，同时避免退化。RotVLA由视觉语言模型（VLM）主干网络和流匹配动作头组成，在大规模跨实体机器人数据集和人类视频上通过潜在动作监督进行预训练。在下游机器人控制中，流匹配头被扩展为统一动作专家，联合去噪潜在动作和机器人动作。其中，潜在动作作为潜在规划器，提供高层引导以约束动作生成。仅凭1.7B参数和1700+小时预训练数据，RotVLA在LIBERO上达到98.2%的准确率，在RoboTwin2.0的干净和随机设置下分别达到89.6%和88.5%。在真实世界的操作任务中，它也展现出强大性能，持续优于现有VLA模型。

---

### 9. BlockVLA: Accelerating Autoregressive VLA via Block Diffusion Finetuning

- **作者**: Ruiheng Wang, Shuanghao Bai, Haoran Zhang, Badong Chen, Xiangyu Xu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.13382v1)
- **发表日期**: 2026-05-13
- **匹配关键词**: VLA, diffusion-based policy, diffusion policy, vision-language-action
- **arXiv**: [2605.13382v1](http://arxiv.org/abs/2605.13382v1)
- **📥 PDF**: 已下载至本地 (`2605.13382v1_BlockVLA_Accelerating_Autoregressive_VLA_via_Block_Diffusion_Finetuning.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 尽管自回归（AR）视觉-语言-动作（VLA）模型在机器人任务中展现出强大的推理能力，但其顺序解码过程通常会导致高推理延迟，并在长期执行过程中可能加剧误差累积。离散扩散语言模型（dLLMs）通过并行令牌精炼提供了一种有前景的替代方案，但它们在机器人领域的实际部署仍受到重复去噪函数评估（NFEs）以及标准KV缓存难以直接应用于双向迭代解码的限制。为弥合这些范式之间的差距，我们提出BlockVLA框架，该框架通过块扩散范式将预训练的AR骨干网络适配为高效的离散扩散策略。BlockVLA在块级别保持自回归依赖关系，同时支持每个块内的并行去噪，从而将全局因果一致性与局部并行生成相结合。这种设计使得已完成块的KV缓存前缀可复用，降低了迭代去噪的有效成本，并为从AR预训练到基于扩散的策略微调提供了更平滑的过渡。我们在LIBERO和SimplerEnv基准上进行了广泛评估。实验结果表明，我们的BlockVLA相比标准离散扩散基线实现了3.3倍的推理加速。此外，我们的模型展现出更优的训练效率，成功率收敛速度显著快于基线模型，这一优势在复杂、长期任务中尤为突出——BlockVLA在训练早期即取得了显著的性能提升。本工作将块扩散确立为大规模预训练AR模型与高效、高频实时机器人控制之间的稳健桥梁。

---

### 10. What Limits Vision-and-Language Navigation ?

- **作者**: Yunheng Wang, Yuetong Fang, Taowen Wang, Lusong Li, Kun Liu, Junzhe Xu, Zizhao Yuan, Yixiao Feng, Jiaxi Zhang, Wei Lu, Zecui Zeng, Renjing Xu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.13328v1)
- **发表日期**: 2026-05-13
- **匹配关键词**: VLN, navigation, vision-and-language navigation, vision-language-action
- **arXiv**: [2605.13328v1](http://arxiv.org/abs/2605.13328v1)
- **📥 PDF**: 已下载至本地 (`2605.13328v1_What_Limits_Vision-and-Language_Navigation_?.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://yunheng-wang.github.io/stereonav-public.github.io.
- **中文摘要**: 视觉与语言导航（VLN）是具身智能的基石。然而，当前智能体在从仿真环境迁移到现实世界部署时，常因感知不稳定性（如光照变化和运动模糊）以及指令描述不充分而出现显著性能下降。尽管现有方法试图通过扩大模型规模和训练数据来弥合这一差距，但我们认为瓶颈在于缺乏鲁棒的空间定位能力和跨领域先验知识。本文提出StereoNav——一个鲁棒的视觉-语言-动作框架，旨在增强现实世界中的导航一致性。为解决合成训练与物理执行之间的固有鸿沟，我们引入目标位置先验作为持久桥梁。这些先验提供跨领域保持不变的稳定视觉引导，即使在指令模糊时也能有效锚定智能体。此外，为缓解运动模糊和光照变化等视觉干扰，StereoNav利用立体视觉构建语义与几何的统一表征，通过增强深度感知实现精确动作预测。在R2R-CE和RxR-CE上的大量实验表明，StereoNav在自中心RGB任务中达到了最优性能，SR和SPL分数分别达到81.1%和68.3%、67.5%和52.0%，同时使用的参数量和训练数据远少于此前基于规模扩展的方法。更重要的是，现实世界机器人部署证实，StereoNav在复杂非结构化环境中显著提升了导航可靠性。项目页面：https://yunheng-wang.github.io/stereonav-public.github.io。

---

### 11. HCSG: Human-Centric Semantic-Geometric Reasoning for Vision-Language Navigation

- **作者**: Haoxuan Xu, Tianfu Li, Wenbo Chen, Yi Liu, Jin Wu, Huashuo Lei, Yunfan Lou, Lujia Wang, Hesheng Wang, Haoang Li
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.13321v1)
- **发表日期**: 2026-05-13
- **匹配关键词**: VLN, navigation
- **arXiv**: [2605.13321v1](http://arxiv.org/abs/2605.13321v1)
- **📥 PDF**: 已下载至本地 (`2605.13321v1_HCSG_Human-Centric_Semantic-Geometric_Reasoning_for_Vision-Language_Navigation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉语言导航（VLN）通过扩展数据和模型容量取得了显著进展。然而，静态环境的假设在真实室内场景中难以成立——机器人不可避免地会遇到动态行人。现有的人感知方法通常仅基于隐式视觉线索将人视为移动障碍物，缺乏解读人类意图或维护社会规范所需的显式推理能力。为此，我们提出HCSG——首个以人为中心的VLN框架。该框架为动态人机环境中的安全、社会智能导航提供了坚实基础，将范式从被动避障转向主动理解人类行为。具体而言，HCSG引入统一的人类理解模块，协同实现两大核心能力：(i) 几何预测——预测人体姿态与轨迹以预判未来运动动态；(ii) 语义解析——利用视觉语言模型（VLM）生成人类行为与意图的自然语言描述。这些语义-几何表征被融合到智能体的拓扑地图中，用于指令条件规划。此外，我们引入社交距离损失函数以强制遵循社会规范的交互距离。在HA-VLNCE基准上的大量实验表明，HCSG显著优于现有最先进方法，成功率达14%的提升，碰撞率降低34%。项目主页：https://haoxuanxu1024.github.io/HCSG/。

---

### 12. Towards Long-horizon Embodied Agents with Tool-Aligned Vision-Language-Action Models

- **作者**: Zixing Lei, Changxing Liu, Yichen Xiong, Minhao Xiong, Yuanzhuo Ding, Zhipeng Zhang, Weixin Li, Siheng Chen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.13119v1)
- **发表日期**: 2026-05-13
- **匹配关键词**: vision-language-action model, VLA, vision-language-action
- **arXiv**: [2605.13119v1](http://arxiv.org/abs/2605.13119v1)
- **📥 PDF**: 已下载至本地 (`2605.13119v1_Towards_Long-horizon_Embodied_Agents_with_Tool-Aligned_Vision-Language-Action_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型是有效的机器人动作执行器，但由于需要同时承担扩展闭环规划与多样化物理操作的双重负担，它们在长时域任务中仍存在局限性。为此，我们提出"VLA即工具"策略，通过将任务负担分配给高层视觉语言模型（VLM）智能体进行时序推理，并配备一系列专用VLA工具执行多样化局部物理操作。VLM负责场景分析、全局规划与恢复操作，而每个VLA工具执行有界子任务。为在长时域任务中实现智能体规划与VLA工具执行的紧密耦合，我们引入VLA工具族接口，该接口提供显式工具选择与执行进度反馈机制，可在无需持续轮询智能体的情况下实现高效的事件触发式重规划。为获得能忠实遵循智能体调用的多样化专用VLA工具，我们进一步提出工具对齐后训练（TAPT）方法，该方法构建调用对齐训练单元以增强指令跟随能力，并采用工具族残差适配器实现高效工具专业化。实验表明，VLA即工具策略在LIBERO-Long和RoboTwin基准上分别将π₀.₅的成功率提升4.8和23.1个百分点，并通过无偏率指标将调用保真度提升15.0个百分点。代码将开源。

---

### 13. What to Ignore, What to React: Visually Robust RL Fine-Tuning of VLA Models

- **作者**: Yuanfang Peng, Jingjing Fu, Chuheng Zhang, Li Zhao, Jiang Bian, Mingyu Liu, Ling Zhang, Jun Zhang, Rui Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.13105v1)
- **发表日期**: 2026-05-13
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2605.13105v1](http://arxiv.org/abs/2605.13105v1)
- **📥 PDF**: 已下载至本地 (`2605.13105v1_What_to_Ignore,_What_to_React_Visually_Robust_RL_Fine-Tuning_of_VLA_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 强化学习（RL）微调在机器人操作领域的视觉-语言-动作（VLA）模型中展现出潜力，但部署时的视觉变化带来了实际挑战。一个关键难点在于：标准任务奖励虽能监督任务成功与否，却难以区分视觉变化是否与任务无关，或是否改变了操作所需的行为。为此，我们提出PAIR-VLA（面向视觉鲁棒VLA的成对动作不变性与敏感性框架），这是一种RL微调框架，通过在PPO优化过程中增加两个针对成对视觉变体的辅助目标来解决该问题：一个不变性项，用于缩小任务保持对（如不同干扰物）的动作分布差异；一个敏感性目标，鼓励任务改变对（如目标物体处于不同姿态）产生可分离的动作分布。这些目标共同将视觉变体从单纯的观测多样性转化为RL微调过程中对策略响应的行为级指导。我们在ManiSkill3平台上，基于两种代表性VLA架构（OpenVLA和π₀.₅），在包含未见干扰物、纹理变化、目标物体姿态变化、视角偏移和光照变化等多种分布外视觉偏移场景下进行评估。我们的方法持续优于标准PPO，在π₀.₅和OpenVLA上分别实现平均16.62%和9.10%的性能提升。值得注意的是，消融实验进一步揭示了跨视觉偏移的泛化能力：从干扰物和纹理变体学习到的不变性指导可迁移至目标姿态和光照变化场景，而在目标姿态变体上增加敏感性指导则进一步提升了对抗干扰偏移的鲁棒性，凸显了行为级RL指导的更广泛可迁移性。

---

### 14. SafeManip: A Property-Driven Benchmark for Temporal Safety Evaluation in Robotic Manipulation

- **作者**: Chengyue Huang, Khang Vo Huynh, Sebastian Elbaum, Zsolt Kira, Lu Feng
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.12386v1)
- **发表日期**: 2026-05-12
- **匹配关键词**: vision-language-action
- **arXiv**: [2605.12386v1](http://arxiv.org/abs/2605.12386v1)
- **📥 PDF**: 已下载至本地 (`2605.12386v1_SafeManip_A_Property-Driven_Benchmark_for_Temporal_Safety_Evaluation_in_Robotic_Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 机器人操作通常通过任务成功来评估，但成功完成并不能保证安全执行。许多安全故障是时序性的：机器人在接触污染后触碰清洁表面，或在物体完全进入容器前释放物体。我们提出SafeManip，一个基于属性的基准测试，用于显式评估机器人操作中的时序安全属性，超越了以往主要关注任务完成或单步状态约束违反的评估方法。SafeManip利用有限迹线性时序逻辑（LTLf）定义了可复用的安全模板，将观测到的执行轨迹映射为符号谓词迹，并通过基于LTLf的监控器进行评估。其属性套件涵盖八类操作安全：碰撞与接触安全、抓取稳定性、释放稳定性、交叉污染、动作启动、机构恢复、物体包容及封闭空间访问。模板可通过任务特定对象、夹具、区域或技能进行实例化，使相同安全规范能泛化至不同任务与环境。我们在50个RoboCasa365家庭任务中，对包括$π_0$、$π_{0.5}$、GR00T及其训练变体在内的六种视觉-语言-动作策略进行了评估。结果表明，即使强模型也常表现出不安全行为。任务成功率的提升并不能可靠转化为更安全的执行：许多成功执行轨迹仍存在安全隐患，而更长时域或更复杂任务则暴露出更多违规行为。SafeManip为诊断时序安全故障及衡量超越任务完成的安全成功提供了可复用的评估层。

---

### 15. GuidedVLA: Specifying Task-Relevant Factors via Plug-and-Play Action Attention Specialization

- **作者**: Xiaosong Jia, Bowen Yang, Zuhao Ge, Xian Nie, Yuchen Zhou, Cunxin Fan, Yufeng Li, Yilin Chai, Chao Jing, Zijian Liang, Qingwen Bu, Haidong Cao, Chao Wu, Qifeng Li, Zhenjie Yang, Chenhe Zhang, Hongyang Li, Zuxuan Wu, Junchi Yan, Yu-Gang Jiang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.12369v1)
- **发表日期**: 2026-05-12
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2605.12369v1](http://arxiv.org/abs/2605.12369v1)
- **📥 PDF**: 已下载至本地 (`2605.12369v1_GuidedVLA_Specifying_Task-Relevant_Factors_via_Plug-and-Play_Action_Attention_Specialization.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型旨在通过将动作作为模态融入强大的视觉-语言模型（VLM）中，实现通用的机器人学习。现有VLA模型依赖端到端监督来隐式地使动作解码过程学习任务相关特征。然而，缺乏显式引导时，这些模型往往过度拟合虚假相关性（如视觉捷径或环境噪声），从而限制了其泛化能力。本文提出GuidedVLA框架，旨在手动引导动作生成聚焦于任务相关因素。核心思路是将动作解码器视为功能组件的集合，而非单一学习器——通过手动定义的辅助信号监督各个注意力头，使其捕获不同因素。作为初步研究，我们以三种专用注意力头实例化该范式：物体定位、空间几何与时序技能逻辑。在仿真与真实机器人实验中，相比强基线VLA模型，GuidedVLA在领域内与领域外场景中均提升了成功率。最后，我们证明这些专用因素的质量与任务性能正相关，且该机制能产生解耦的高质量特征。研究结果表明，显式引导动作解码器学习是构建更鲁棒、更通用的VLA模型的有前景方向。

---

### 16. SI-Diff: A Framework for Learning Search and High-Precision Insertion with a Force-Domain Diffusion Policy

- **作者**: Yibo Liu, Stanko Oparnica, Simon Shewchun-Jakaitis, Guoyi Fu, Jie Wang, Jun Yang, Anand Jagannathan, Tony Hong-Yau Lo
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.12247v1)
- **发表日期**: 2026-05-12
- **匹配关键词**: diffusion policy
- **arXiv**: [2605.12247v1](http://arxiv.org/abs/2605.12247v1)
- **📥 PDF**: 已下载至本地 (`2605.12247v1_SI-Diff_A_Framework_for_Learning_Search_and_High-Precision_Insertion_with_a_Force-Domain_Diffusion_P.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 接触丰富的装配是机器人技术的基础，但由于相对位姿的不确定性（例如轴孔任务中的错位和小间隙），这一任务面临重大挑战。现有方法通常将搜索与高精度插入分开处理，因为这两类任务涉及不同的动作模式。然而，在不切换模型或权重的情况下，在单一模型中同时支持这两类任务，对于智能装配系统而言是理想的目标。在本工作中，我们提出SI-Diff框架，通过力域扩散策略同时学习搜索与高精度插入。为此，我们引入了一种新的模式调节机制，使策略能够在单一框架下捕捉不同的动作行为。此外，我们开发了一种新的搜索教师策略，能够生成多样化的轨迹。通过基于教师策略提供的成功且高效的演示进行训练，模型学会了从触觉和末端执行器速度观测到有效动作行为的映射。我们进行了充分的实验，结果表明，与最先进的基线方法TacDiffusion相比，SI-Diff将x-y方向错位的容忍度从2毫米提升至5毫米，同时展现出对未见形状的强零样本迁移能力。

---

### 17. TMRL: Diffusion Timestep-Modulated Pretraining Enables Exploration for Efficient Policy Finetuning

- **作者**: Matthew M. Hong, Jesse Zhang, Anusha Nagabandi, Abhishek Gupta
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.12236v1)
- **发表日期**: 2026-05-12
- **匹配关键词**: VLA, exploration
- **arXiv**: [2605.12236v1](http://arxiv.org/abs/2605.12236v1)
- **📥 PDF**: 已下载至本地 (`2605.12236v1_TMRL_Diffusion_Timestep-Modulated_Pretraining_Enables_Exploration_for_Efficient_Policy_Finetuning.pdf`)
- **🔓 开源**: CODE
  - 链接：https://weirdlabuw.github.io/tmrl/.
- **中文摘要**: 基于强化学习（RL）微调预训练机器人策略时，常会继承行为克隆（BC）预训练引入的瓶颈——BC生成的狭窄动作分布缺乏下游探索所需的覆盖范围。我们提出统一框架，通过桥接BC预训练与RL微调，实现高效机器人策略微调所需的探索能力。我们的预训练方法——上下文平滑预训练（CSP）——将前向扩散噪声注入策略输入，在精确模仿与广泛动作覆盖之间构建连续谱系。随后通过时间步调制强化学习（TMRL）微调预训练策略，该方法训练智能体在微调过程中通过调节扩散时间步动态调整该条件，从而实现对探索的显式控制。该方法可无缝集成任意策略输入（如状态、3D点云或基于图像的VLA策略），实验表明TMRL能提升RL微调的样本效率。值得注意的是，TMRL可在1小时内完成复杂操作任务的真实世界微调。视频与代码详见https://weirdlabuw.github.io/tmrl/。

---

### 18. TriBand-BEV: Real-Time LiDAR-Only 3D Pedestrian Detection via Height-Aware BEV and High-Resolution Feature Fusion

- **作者**: Mohammad Khoshkdahan, Alexey Vinel
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.12220v1)
- **发表日期**: 2026-05-12
- **匹配关键词**: 3d reconstruction, 3D reconstruction
- **arXiv**: [2605.12220v1](http://arxiv.org/abs/2605.12220v1)
- **📥 PDF**: 已下载至本地 (`2605.12220v1_TriBand-BEV_Real-Time_LiDAR-Only_3D_Pedestrian_Detection_via_Height-Aware_BEV_and_High-Resolution_Fe.pdf`)
- **🔓 开源**: CODE
- **中文摘要**: 安全自主智能体与移动机器人需要快速实时的3D感知能力，尤其针对行人等弱势道路使用者（VRU）。我们提出一种新型鸟瞰图（BEV）编码方法，将完整的3D激光雷达点云映射为包含三个高度带的轻量级2D BEV张量。通过将3D检测显式重构为2D检测问题，再从BEV输出重建3D边界框，单个网络即可一次性检测汽车、行人和骑行者。主干网络在深层阶段采用区域注意力机制，P1至P4层级间的双向颈部网络融合上下文与细节信息，检测头通过分布聚焦学习预测侧向偏移的定向边界框，并采用旋转IoU损失函数。训练过程中应用垂直方向的小区间重分箱与通道空间的适度反射抖动增强，以防止过拟合记忆。在3D重建阶段，采用四分位距（IQR）滤波器去除噪声和离群点云。在KITTI数据集上，TriBand-BEV在单张消费级GPU上以49 FPS的速度，对行人检测的简单/中等/困难场景分别达到58.7%/52.6%/47.2%的BEV AP值，超越Complex-YOLO方法，分别提升12.6%、7.5%和3.1%。定性场景显示该方法在遮挡条件下仍能稳定检测。整个流程紧凑高效，可直接部署于实时机器人系统。我们的源代码已在GitHub上公开。

---

## 📌 Poster

*其他相关研究*

---

### 1. RoboEvolve: Co-Evolving Planner-Simulator for Robotic Manipulation with Limited Data

- **作者**: Harold Haodong Chen, Sirui Chen, Yingjie Xu, Wenhang Ge, Ying-Cong Chen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.13775v1)
- **发表日期**: 2026-05-13
- **匹配关键词**: exploration
- **arXiv**: [2605.13775v1](http://arxiv.org/abs/2605.13775v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 机器人操作的可扩展性从根本上受限于任务对齐的物理交互数据的稀缺性。尽管视觉语言模型（VLMs）和视频生成模型（VGMs）在自主数据合成方面具有潜力，但它们分别存在语义-空间错位和物理幻觉的问题。为弥合这一差距，我们提出了RoboEvolve，一个将VLM规划器与VGM模拟器耦合为相互强化的协同进化循环的新型框架。该框架仅基于无标注的种子图像运行，利用受认知启发的双阶段机制：（i）日间探索阶段通过语义控制的多粒度奖励促进基于物理的行为发现，以及（ii）夜间巩固阶段挖掘"近似失败"案例以稳定策略优化。在自主渐进式课程引导下，系统自然地从简单原子动作扩展到复杂任务。大量实验表明，RoboEvolve（I）实现了卓越的有效性，使基础规划器性能提升30个绝对百分点，模拟器成功率平均提高48%；（II）展现出极致的数效率，仅需500个无标注种子即可超越全监督基线——数据量减少50倍；（III）展示了稳健的持续学习能力，且无灾难性遗忘问题。

---

### 2. Manipulation Planning for Construction Activities with Repetitive Tasks

- **作者**: Wangyi Liu, Dasharadhan Mahalingam, Fanru Gao, Ci-Jyun Liang, Nilanjan Chakraborty
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.13754v1)
- **发表日期**: 2026-05-13
- **匹配关键词**: object manipulation
- **arXiv**: [2605.13754v1](http://arxiv.org/abs/2605.13754v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 本文研究了执行由重复性任务组成的建筑活动（例如砌墙或安装天花板瓷砖）所需的操作技能获取问题。我们的方法是在虚拟现实环境中搭建模拟建筑活动场景，用户可在此环境中演示执行建筑活动所需的对象操作技能。随后，我们利用运动的螺旋几何特性，将演示运动近似为一系列恒定螺旋运动序列。为执行建筑活动，我们先生成操作任务实例序列，再通过螺旋线性插值和解析运动速率控制计算每个实例对应的关节空间运动规划。我们通过执行两项代表性建筑任务（砌砖墙与安装多块天花板瓷砖）来评估该框架。每项任务仅需一次演示：砖块的拾取-放置动作演示与单块天花板瓷砖的安装演示。在仿真与硬件环境下使用七自由度机器人进行的实验表明，即使仅提供单次演示，该方法也能稳健泛化至任意长度、包含重复动作且要求精度的建筑活动。例如，通过演示将一块砖叠放在另一块砖上的单一操作，即可构建任意布局与长度的墙体。

---

