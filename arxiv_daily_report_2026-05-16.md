# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-05-16 08:02

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 3/20 篇提供

**🌟 Highlight**: 12 篇 | **📌 Poster**: 8 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. Hand-in-the-Loop: Improving Dexterous VLA via Seamless Interventional Correction

- **作者**: Zhuohang Li, Liqun Huang, Wei Xu, Zhengming Zhu, Nie Lin, Xiao Ma, Xinjun Sheng, Ruoshi Wen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.15157v1)
- **发表日期**: 2026-05-14
- **匹配关键词**: vision-language-action, VLA, tool use
- **arXiv**: [2605.15157v1](http://arxiv.org/abs/2605.15157v1)
- **📥 PDF**: 已下载至本地 (`2605.15157v1_Hand-in-the-Loop_Improving_Dexterous_VLA_via_Seamless_Interventional_Correction.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型在灵巧操作中容易产生累积误差，高维动作空间和富含接触的动力学特性会放大长期任务中小策略偏差的影响。交互式模仿学习（IIL）虽能通过人类接管数据优化策略，但在高自由度（DoF）机器人手上应用仍面临挑战——人类遥操作与策略执行在接管时刻存在指令不匹配，导致机器人手部构型突变（即"手势跳跃"）。我们提出"手在环中"（HandITL）无缝人机交互干预方法，通过融合人类修正意图与自主策略执行，避免双手灵巧操作中的手势跳跃。与直接遥操作接管相比，HandITL将接管抖动降低99.8%，并保持接管后稳健操作能力，抓取失败率降低87.5%，平均完成时间缩短19.1%。我们在需要双手协调、工具使用及细粒度长程操作的任务中验证了HandITL。当用于收集策略优化的干预数据时，基于HandITL训练的策略在三个长程灵巧任务上的平均性能比使用标准遥操作数据训练的策略提升19%。

---

### 2. Evo-Depth: A Lightweight Depth-Enhanced Vision-Language-Action Model

- **作者**: Tao Lin, Yuxin Du, Jiting Liu, Nuobei Zhu, Yunhe Li, Yuqian Fu, Yinxinyu Chen, Hongyi Cai, Zewei Ye, Bing Cheng, Kai Ye, Yiran Mao, Yilei Zhong, MingKang Dong, Junchi Yan, Gen Li, Bo Zhao
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.14950v1)
- **发表日期**: 2026-05-14
- **匹配关键词**: vision-language-action model, vision-language-action, VLA
- **arXiv**: [2605.14950v1](http://arxiv.org/abs/2605.14950v1)
- **📥 PDF**: 已下载至本地 (`2605.14950v1_Evo-Depth_A_Lightweight_Depth-Enhanced_Vision-Language-Action_Model.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作模型通过统一感知、语言理解和动作生成，已成为机器人操作领域一种有前景的范式。然而，这类模型在需要精确空间理解的场景中仍面临挑战，因为当前的VLA模型主要依赖缺乏深度信息和详细空间关系的二维视觉表征。虽然近期研究通过引入深度图或点云等显式三维输入来解决该问题，但这往往增加了系统复杂度，需要额外传感器，并且容易受到感知噪声和重建误差的影响。另一类工作尝试从RGB观测中直接进行隐式三维感知空间建模而无需额外传感器，但通常依赖大型几何基础模型，导致训练和部署成本较高。为应对这些挑战，我们提出Evo-Depth——一种轻量级深度增强型VLA框架，可在不依赖额外传感硬件或牺牲部署效率的前提下提升空间操作能力。Evo-Depth采用轻量级隐式深度编码模块，从多视角RGB图像中提取紧凑深度特征，并通过空间增强模块中的深度感知调制将其融入视觉-语言表征，实现高效的空间语义增强。此外，我们引入渐进对齐训练策略，使增强后的深度表征与下游动作学习相适配。仅需0.9B参数，Evo-Depth便在四个仿真基准测试中取得卓越性能。在真实世界实验中，Evo-Depth在获得最高平均成功率的同时，还展现出最小的模型尺寸、最低的GPU内存占用以及最高的推理频率。

---

### 3. IntentVLA: Short-Horizon Intent Modeling for Aliased Robot Manipulation

- **作者**: Shijie Lian, Bin Yu, Xiaopeng Lin, Zhaolong Shen, Laurence Tianruo Yang, Yurun Jin, Haishan Liu, Changti Wu, Hang Yuan, Cong Huang, Kai Chen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.14712v1)
- **发表日期**: 2026-05-14
- **匹配关键词**: VLA
- **arXiv**: [2605.14712v1](http://arxiv.org/abs/2605.14712v1)
- **📥 PDF**: 已下载至本地 (`2605.14712v1_IntentVLA_Short-Horizon_Intent_Modeling_for_Aliased_Robot_Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 机器人模仿数据通常是多模态的：相似的视觉-语言观测可能对应不同的动作片段，因为人类演示者会基于不同的短期意图、任务阶段或近期上下文采取行动。现有的帧条件化VLA策略仅根据当前观测和指令推断每个动作片段，因此在部分可观测性条件下，它们可能在相邻的重新规划步骤中重新采样不同的意图，导致片段间冲突和执行不稳定。我们提出IntentVLA，一种历史条件化的VLA框架，将近期视觉观测编码为紧凑的短期意图表示，并利用该表示来条件化片段生成。我们进一步引入AliasBench，一个基于RoboTwin2的12任务歧义感知基准，包含匹配的训练数据和评估环境，以隔离短期观测歧义。在AliasBench、SimplerEnv、LIBERO和RoboCasa上，IntentVLA提升了滚动稳定性，并优于强VLA基线。

---

### 4. CalibAnyView: Beyond Single-View Camera Calibration in the Wild

- **作者**: Boying Li, Cheng Zhang, Weirong Chen, Daniel Cremers, Ian Reid, Hamid Rezatofighi ⭐
  - **高亮作者**: Daniel Cremers
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.14615v1)
- **发表日期**: 2026-05-14
- **匹配关键词**: 3d reconstruction, 3D reconstruction
- **arXiv**: [2605.14615v1](http://arxiv.org/abs/2605.14615v1)
- **📥 PDF**: 已下载至本地 (`2605.14615v1_CalibAnyView_Beyond_Single-View_Camera_Calibration_in_the_Wild.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 相机标定是实现可靠几何感知的基本前提，但传统方法依赖受控采集环境，难以应用于自然场景图像。近年来基于学习的方法在单视图标定中展现出良好效果，但本质上忽略了多视图间的几何一致性。我们提出CalibAnyView统一框架，通过显式建模跨视图几何一致性，支持任意数量输入视图（N≥1）。为此，我们构建了覆盖多种真实场景的大规模多视图视频数据集，包含多种相机模型、动态场景、真实运动轨迹及异构镜头畸变。基于该数据集，我们开发了多视图Transformer以预测密集透视场，并将其集成至几何优化框架中，联合估计相机内参和重力方向。大量实验表明，CalibAnyView持续优于现有最优方法，在单视图设置下展现出强鲁棒性，且随多视图推理性能进一步提升，为野外三维重建和机器人感知等下游任务提供了可靠基础。

---

### 5. FrameSkip: Learning from Fewer but More Informative Frames in VLA Training

- **作者**: Bin Yu, Shijie Lian, Xiaopeng Lin, Zhaolong Shen, Yuliang Wei, Changti Wu, Hang Yuan, Haishan Liu, Bailing Wang, Cong Huang, Kai Chen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.13757v1)
- **发表日期**: 2026-05-13
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2605.13757v1](http://arxiv.org/abs/2605.13757v1)
- **📥 PDF**: 已下载至本地 (`2605.13757v1_FrameSkip_Learning_from_Fewer_but_More_Informative_Frames_in_VLA_Training.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）策略通常通过遥操作采集的密集机器人演示轨迹进行训练，其采样方式是将每一帧记录数据视为提供同等有效的监督信号。我们认为这种惯例造成了时间维度的监督失衡：长段低变化片段主导了训练数据流，而操作关键过渡阶段（如对齐、接触、抓取和释放）却仅稀疏出现。为此，我们提出FrameSkip——一种数据层帧选择框架，通过动作变化度、视觉-动作一致性、任务进度先验和夹爪过渡保留度对轨迹帧进行评分，并在目标保留率下将训练样本重新映射至高重要性帧。由于FrameSkip仅在数据加载器层面运作，因此无需改变VLA架构、动作头、训练目标及推理流程。在RoboCasa-GR1、SimplerEnv和LIBERO基准测试中，FrameSkip相较于全帧训练及简单帧选择变体，实现了更优的成功率-保留率权衡：在三个基准测试中宏观平均成功率达76.15%（全帧训练为66.50%），同时主设置下仅保留20%独特帧的压缩轨迹视图。

---

### 6. LEXI-SG: Monocular 3D Scene Graph Mapping with Room-Guided Feed-Forward Reconstruction

- **作者**: Christina Kassab, Hyeonjae Gil, Matías Mattamala, Ayoung Kim, Maurice Fallon ⭐
  - **高亮作者**: Maurice Fallon
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.13741v1)
- **发表日期**: 2026-05-13
- **匹配关键词**: navigation, semantic scene graph, robot navigation, scene graph
- **arXiv**: [2605.13741v1](http://arxiv.org/abs/2605.13741v1)
- **📥 PDF**: 已下载至本地 (`2605.13741v1_LEXI-SG_Monocular_3D_Scene_Graph_Mapping_with_Room-Guided_Feed-Forward_Reconstruction.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://ori-drs.github.io/lexisg-web/.
- **中文摘要**: 场景图正逐渐成为机器人导航的标准表示方法，能够提供层次化的几何与语义场景理解。然而，现有场景图建图方法大多依赖深度相机或激光雷达传感器。本研究提出LEXI-SG——首个仅使用RGB相机输入、面向开放词汇三维场景图的密集单目视觉建图系统。我们的方法利用开放词汇基础模型的语义先验将场景划分为不同房间，并将前馈重建过程延迟至每个房间被完全观测时——从而在避免滑动窗口尺度不一致问题的同时实现可扩展的密集建图。我们提出基于房间的因子图框架，在保持局部地图一致性的同时实现房间重建的全局对齐，并自然构建语义场景图的层次结构。在每个房间内，我们进一步支持开放词汇的物体分割与追踪。我们在Habitat-Matterport 3D室内场景及自采集的自我中心办公序列上验证了LEXI-SG的性能，并与现有前馈SLAM方法及主流场景图基线进行了对比评估。实验表明，本方法在轨迹估计与密集重建方面表现更优，同时在开放词汇分割任务中具有竞争力。LEXI-SG证明，仅凭单目RGB即可实现精确、可扩展的开放词汇三维场景图。项目页面与办公序列详见：https://ori-drs.github.io/lexisg-web/。

---

### 7. Robot Squid Game: Quadrupedal Locomotion for Traversing Narrow Tunnels

- **作者**: Amir Hossain Raj, Dibyendu Das, Xuesu Xiao
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.13665v1)
- **发表日期**: 2026-05-13
- **匹配关键词**: navigation
- **arXiv**: [2605.13665v1](http://arxiv.org/abs/2605.13665v1)
- **📥 PDF**: 已下载至本地 (`2605.13665v1_Robot_Squid_Game_Quadrupedal_Locomotion_for_Traversing_Narrow_Tunnels.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 四足机器人在搜索救援、基础设施巡检等关键任务中展现出穿越复杂地形的卓越潜力。然而，在隧道、洞穴及坍塌结构等受限三维环境中的自主通行仍面临重大挑战。现有方法常受困于僵化的步态模式、对多样化几何结构的适应能力有限，以及过度依赖简化的环境假设。本文提出一种结合程序化环境生成与策略蒸馏的强化学习框架，使机器人能够在各类隧道构型中实现稳健运动。该方法采用师生训练范式：基于程序化生成隧道几何结构的专家策略，将其知识迁移至统一的学徒策略。这种策略无需在端到端强化学习训练中进行复杂的奖励塑形，通过将复杂任务分解为更易学习的子模块来简化训练流程。通过在训练中合成多样化隧道结构，并将导航策略蒸馏为可泛化的统一策略，本方法在传统方法失效的复杂空间约束下实现了持续穿越能力。仿真与实物实验均证明，该方法能使四足机器人成功穿越具有挑战性的受限隧道环境。

---

### 8. Guide, Think, Act: Interactive Embodied Reasoning in Vision-Language-Action Models

- **作者**: Yiran Ling, Qing Lian, Jinghang Li, Qing Jiang, Tianming Zhang, Xiaoke Jiang, Chuanxiu Liu, Jie Liu, Lei Zhang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.13632v1)
- **发表日期**: 2026-05-13
- **匹配关键词**: vision-language-action model, affordance, vision-language-action, VLA
- **arXiv**: [2605.13632v1](http://arxiv.org/abs/2605.13632v1)
- **📥 PDF**: 已下载至本地 (`2605.13632v1_Guide,_Think,_Act_Interactive_Embodied_Reasoning_in_Vision-Language-Action_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 本文提出GTA-VLA（引导、思考、行动）框架，这是一种交互式视觉-语言-动作（VLA）框架，通过允许用户使用显式视觉线索引导机器人策略，实现空间可操控的具身推理。现有VLA模型学习从多模态观测到机器人动作的直接"感知-行动"映射。虽然这类紧密耦合的策略在训练分布内表现有效，但在域外偏移下较为脆弱，且发生故障时难以修正。尽管近期具身思维链方法暴露了中间推理过程，但仍缺乏融入人类空间引导的机制，限制了其解决视觉歧义或从错误中恢复的能力。为填补这一空白，本框架允许用户可选地使用空间先验（如可操作点、边界框和轨迹）引导策略，后续推理过程可直接基于这些输入进行条件化。基于这些输入，模型生成统一的时空视觉思维链，将外部引导与内部任务规划相结合，使人类视觉意图与自主决策对齐。为便于实际部署，我们进一步将推理模块与轻量级反应式动作头耦合，实现高效动作执行。大量实验证明了该方法的有效性。在域内SimplerEnv WidowX基准测试中，本框架实现了81.2%的最优成功率。面对域外视觉偏移和空间歧义时，单次视觉交互即可显著提升任务成功率，凸显了交互式推理在具身控制故障恢复中的价值。项目详情请见：https://signalispupupu.github.io/GTA-VLA_ProjPage/

---

### 9. AttenA+: Rectifying Action Inequality in Robotic Foundation Models

- **作者**: Daojie Peng, Fulong Ma, Jiahang Cao, Qiang Zhang, Xupeng Xie, Jian Guo, Ping Luo, Andrew F. Luo, Boyu Zhou, Jun Ma
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.13548v1)
- **发表日期**: 2026-05-13
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2605.13548v1](http://arxiv.org/abs/2605.13548v1)
- **📥 PDF**: 已下载至本地 (`2605.13548v1_AttenA+_Rectifying_Action_Inequality_in_Robotic_Foundation_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 现有的机器人基础模型虽然功能强大，但都隐含着一个时间同质性的假设：在优化过程中将所有动作视为同等重要。这种从语言建模继承而来的"扁平化"训练范式，对操作任务中潜在的物理层级结构视而不见。实际上，机器人轨迹本质上是异质的——低速段往往通过高精度交互决定任务成败，而高速运动则充当容错性过渡。这种统一损失权重与物理关键性之间的错位，从根本上限制了当前视觉-语言-动作模型（VLA）和世界动作模型（WAM）在复杂长程任务中的性能。为解决这一问题，我们提出AttenA+——一个与架构无关的框架，通过速度驱动的动作注意力机制优先关注运动学关键片段。基于逆速度场重新加权训练目标后，AttenA+自然地将模型学习能力与操作任务的物理需求对齐。作为即插即用的增强模块，AttenA+无需修改结构或增加参数即可集成到现有骨干网络中。大量实验表明，AttenA+显著提升了当前最优模型的上限：在Libero基准测试中将OpenVLA-OFT提升至98.6%（+1.5%），在RoboTwin 2.0上将FastWAM推至92.4%（+0.6%）。在Franka机械臂上的真实世界验证进一步展示了其鲁棒性和跨任务泛化能力。我们的工作表明，挖掘动作序列的内在结构先验，为标准的扩展定律提供了高效且具有物理感知的补充，为通用机器人控制开辟了新路径。

---

### 10. CUBic: Coordinated Unified Bimanual Perception and Control Framework

- **作者**: Xingyu Wang, Pengxiang Ding, Jingkai Xu, Donglin Wang, Zhaoxin Fan
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.13452v1)
- **发表日期**: 2026-05-13
- **匹配关键词**: diffusion policy, bimanual manipulation
- **arXiv**: [2605.13452v1](http://arxiv.org/abs/2605.13452v1)
- **📥 PDF**: 已下载至本地 (`2605.13452v1_CUBic_Coordinated_Unified_Bimanual_Perception_and_Control_Framework.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 近期，视觉运动策略学习的进展使机器人能够直接从视觉输入进行控制。然而，将这种端到端学习从单臂操作扩展到双臂操作仍具挑战性，因为双臂既需要独立感知，又需要协调交互。现有方法通常偏向某一侧——要么解耦双臂以避免干扰，要么强制双臂强耦合以实现协调——因此缺乏统一的处理方式。我们提出CUBic，一个协调统一的双臂感知与控制框架，将双臂协调重新定义为统一的感知建模问题。CUBic学习一种连接感知与控制的共享标记化表示，其中独立性与协调性从结构本身内在地涌现，而非依赖人为设计的耦合。我们的方法整合了三个组件：单向感知聚合、通过两个共享映射码本实现的双向感知协调，以及统一的感知到控制扩散策略。在RoboTwin基准上的大量实验表明，CUBic持续超越标准基线，在协调准确率和任务成功率上相较于最先进的视觉运动基线取得了显著提升。

---

### 11. Asymptotically Optimal Ergodic Coverage on Generalized Motion Fields

- **作者**: Christian Hughes, Yilang Liu, Yanis Lahrach, Julia Engdahl, Houston Warren, Darrick Lee, Fabio Ramos, Travis Miles, Ian Abraham
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.13442v1)
- **发表日期**: 2026-05-13
- **匹配关键词**: exploration, path planning
- **arXiv**: [2605.13442v1](http://arxiv.org/abs/2605.13442v1)
- **📥 PDF**: 已下载至本地 (`2605.13442v1_Asymptotically_Optimal_Ergodic_Coverage_on_Generalized_Motion_Fields.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 在偏远和极端环境中的自主机器人探索，使科学家能够模拟由连续变形流场描述的复杂输运现象和集体行为。尽管这些环境天然被建模为时变区域，但大多数自适应探索方法假设静态环境，无法提供充分的覆盖或满足任何形式化保证。这在海洋学中尤为突出——自主水下系统（UxS）对计算和载荷有严格限制，需要路径规划方法在开环和欠驱动条件下生成稳健的数据采集策略。

为解决上述问题，本研究提出将自适应搜索建模为遍历覆盖问题，并研究在具有流致动力学的演化域中，从遍历意义上验证覆盖性能的方法。我们扩展了近期将最大均值差异（MMD）作为函数遍历度量的研究成果，推导出显式考虑域演化的流自适应覆盖目标函数。研究表明，该方法在环境流场中保留了遍历覆盖保证，并通过整合环境动力学，在欠驱动甚至开环规划场景中实现高效探索。实验验证了该方法可泛化至包括海洋探索、人类与牲畜运动追踪在内的多种时空过程。基于空中和足式机器人平台的物理实验进一步证实，该方法能在非凸、受限流场环境中，在满足机器人动力学约束的前提下实现遍历覆盖。

---

### 12. RotVLA: Rotational Latent Action for Vision-Language-Action Model

- **作者**: Qiwei Li, Xicheng Gong, Xinghang Li, Peiyan Li, Quanyun Zhou, Hangjun Ye, Jiahuan Zhou, Yadong Mu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.13403v1)
- **发表日期**: 2026-05-13
- **匹配关键词**: vision-language-action model, vision-language-action, VLA
- **arXiv**: [2605.13403v1](http://arxiv.org/abs/2605.13403v1)
- **📥 PDF**: 已下载至本地 (`2605.13403v1_RotVLA_Rotational_Latent_Action_for_Vision-Language-Action_Model.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 潜在动作模型（LAMs）已成为视觉-语言-动作（VLA）模型预训练中处理异构数据集的有效范式，能够跨实体提供统一的动作空间。然而，现有LAMs通常依赖离散量化编码-解码流程，这可能导致帧重建行为琐碎、表征能力受限，且缺乏具有物理意义的结构。我们提出RotVLA，一种基于连续旋转潜在动作表征的VLA框架。潜在动作被建模为SO(n)群元素，具备连续性、组合性以及与真实世界动作动态对齐的结构化几何特性。三重帧学习框架进一步强化了有意义的时序动态，同时避免退化。RotVLA由视觉语言模型（VLM）主干网络和流匹配动作头组成，在大规模跨实体机器人数据集和人类视频上通过潜在动作监督进行预训练。在下游机器人控制中，流匹配头被扩展为统一动作专家，联合去噪潜在动作和机器人动作。其中，潜在动作作为潜在规划器，提供约束动作生成的高层引导。仅凭1.7B参数和1700+小时预训练数据，RotVLA在LIBERO上达到98.2%的准确率，在RoboTwin2.0的干净和随机设置下分别达到89.6%和88.5%。在真实世界的操作任务中，它也展现出强劲性能，持续优于现有VLA模型。

---

## 📌 Poster

*其他相关研究*

---

### 1. SOCC-ICP: Semantics-Assisted Odometry based on Occupancy Grids and ICP

- **作者**: Johannes Scherer, Sebastian Hirt, Henri Meeß
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.15074v1)
- **发表日期**: 2026-05-14
- **匹配关键词**: motion planning
- **arXiv**: [2605.15074v1](http://arxiv.org/abs/2605.15074v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 在未知环境中实现可靠的位姿估计是自主系统的一项基本能力。现有的激光雷达里程计方法通常采用基于点、面元或正态分布变换的地图表示，这与下游任务（如运动规划）中常用的语义占据网格存在显著差异。我们提出SOCC-ICP——一种语义辅助的里程计框架，可联合执行语义占据网格建图与激光雷达扫描配准。每个地图体素编码几何与语义统计信息，能够根据局部平面性自适应地执行点到点或点到平面的迭代最近点算法。此外，占据网格通过基于射线投射的自由空间更新自然地过滤动态物体。在多种评估场景中，SOCC-ICP的性能与最先进的激光雷达里程计相当，且即使在缺乏语义线索的几何退化环境中仍保持鲁棒性。当语义标签可用时，将其集成到地图构建、降采样和对应点加权中可进一步提升精度。通过将里程计与语义占据网格建图统一于单一表示中，SOCC-ICP消除了冗余的地图结构，并直接提供适用于下游机器人应用的地图。

---

### 2. Chrono-Gymnasium: An Open-Source, Gymnasium-Compatible Distributed Simulation Framework

- **作者**: Bocheng Zou, Harry Zhang, Khailanii Slaton, Jingquan Wang, Derrick Ruan, Huzaifa Mustafa Unjhawala, Radu Serban, Dan Negrut
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.14911v1)
- **发表日期**: 2026-05-14
- **匹配关键词**: navigation
- **arXiv**: [2605.14911v1](http://arxiv.org/abs/2605.14911v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: CODE
- **中文摘要**: 高保真物理仿真对于弥合机器人及复杂机械系统中仿真与现实的差距至关重要。然而，高保真引擎的计算开销往往限制了其在强化学习（RL）和全局优化等数据密集型任务中的应用。我们提出Chrono-Gymnasium，这是一个分布式计算框架，能够将Project Chrono的高保真多体动力学计算扩展至大规模计算集群。该框架基于Ray构建，提供标准化的Gymnasium接口，既支持与现代机器学习库的无缝集成，又内置了用于分布式执行的同步与消息传递原语。我们通过两个典型案例验证了该框架的能力：（1）在复杂地形中训练自主机器人导航的强化学习智能体；（2）通过贝叶斯优化行星着陆器的设计参数以确保着陆稳定性。实验结果表明，Chrono-Gymnasium在保持物理精度的前提下减少了高保真仿真的实际运行时间，为复杂机器人系统的设计与控制提供了可扩展的解决方案。

---

### 3. Let Robots Feel Your Touch: Visuo-Tactile Cortical Alignment for Embodied Mirror Resonance

- **作者**: Tianfang Zhu, Ning An, Rui Wang, Jiasi Gao, Qingming Luo, Anan Li, Guyue Zhou
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.14571v1)
- **发表日期**: 2026-05-14
- **匹配关键词**: human-robot interaction
- **arXiv**: [2605.14571v1](http://arxiv.org/abs/2605.14571v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: GITHUB
  - 链接：https://github.com/fun0515/Mirror-Touch-Net.
- **中文摘要**: 观察他人身体上的触觉可以引发观察者相应的触觉感受，这种现象被称为镜像触觉，它支撑着共情与社会感知。这种视觉-触觉共振被认为依赖于视觉皮层与体感皮层之间的结构对应关系，然而机器人系统缺乏实现这一原理的计算框架。在此，我们证明皮层对应关系可被操作化，赋予机器人镜像触觉能力。我们提出了镜像触觉网络（Mirror Touch Net），通过多层次约束实现视觉表征与触觉表征之间的语义对齐、分布对齐与几何对齐，从而能够从RGB图像预测机器人手上1140个触觉单元的毫米级触觉信号。流形分析表明，这些约束将视觉表征重塑为与触觉流形一致的几何结构，降低了跨模态映射的复杂性。将该对齐框架扩展至人手跨域观察，可实现触觉预测及对观察到的他人触觉的反射性响应。我们的研究结果将视觉-触觉共振的神经原理与机器人感知联系起来，为预期性触觉和共情型人机交互提供了可解释的路径。代码已开源：https://github.com/fun0515/Mirror-Touch-Net。

---

### 4. When Robots Do the Chores: A Benchmark and Agent for Long-Horizon Household Task Execution

- **作者**: Zilin Zhu, Longteng Guo, Yanghong Mei, Bowen Pang, Zongxun Zhang, Xingjian He, Ruyi Ji, Jing Liu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.14504v1)
- **发表日期**: 2026-05-14
- **匹配关键词**: navigation
- **arXiv**: [2605.14504v1](http://arxiv.org/abs/2605.14504v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 长时域家庭任务要求强大的高层规划与持续推理能力，而现有具身智能基准测试大多聚焦于短时域导航或操作任务，且依赖固定任务类别，忽视了这一关键维度。为此，我们提出LongAct基准测试，旨在评估通过自由形式指令指定的长时域家庭任务中的规划级自主性。通过剥离具身特性相关的底层控制，LongAct聚焦于高层认知能力，包括指令理解、依赖管理、记忆维护与自适应规划。我们进一步提出HoloMind——一种基于视觉语言模型（VLM）的智能体，其核心包含基于有向无环图（DAG）的长时域分层规划器、用于持久世界建模的多模态空间记忆、用于经验复用的情景记忆，以及用于反思性监督的全局评判器。基于GPT-5与Qwen3-VL模型的实验表明，HoloMind在显著提升长时域任务性能的同时，降低了对模型规模的依赖。即便最先进的模型也仅能达到59%的目标完成率与16%的全任务成功率，这凸显了LongAct的挑战性，以及具身智能体在长时域规划能力上的迫切需求。

---

### 5. Coding Agent Is Good As World Simulator

- **作者**: Hongyu Wang, Jingquan Wang, Bocheng Zou, Radu Serban, Dan Negrut
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.14398v1)
- **发表日期**: 2026-05-14
- **匹配关键词**: visual feedback
- **arXiv**: [2605.14398v1](http://arxiv.org/abs/2605.14398v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 世界模型已成为构建交互式仿真环境的一种强大范式，近期基于视频的方法在生成视觉上合理的动态过程方面取得了显著进展。然而，由于这些模型通常从视频中推断动态过程并以潜在状态表示，它们并未明确施加物理约束。因此，生成的视频推演在物理上并不合理，会出现接触不稳定、形状扭曲或运动不一致等问题。本文提出了一种基于智能体框架的方法，通过可执行的仿真代码构建基于物理的世界模型。该框架协调了规划、代码生成、视觉审查和物理分析等智能体。规划智能体将自然语言提示转换为结构化的场景规划，代码智能体将其实现为可执行的仿真代码，视觉审查智能体提供视觉反馈，而物理分析智能体则检查物理一致性。代码会根据反馈进行迭代修正，直至仿真结果满足提示要求及物理约束。实验结果表明，我们的框架在物理准确性、指令忠实度和视觉质量方面均优于先进的基于视频的模型，可应用于驾驶仿真和具身机器人任务等多种场景。

---

### 6. Analogical Trajectory Transfer

- **作者**: Junho Kim, Eun Sun Lee, Gwangtak Bae, Seunggu Kang, Young Min Kim
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.14393v1)
- **发表日期**: 2026-05-14
- **匹配关键词**: scene graph
- **arXiv**: [2605.14393v1](http://arxiv.org/abs/2605.14393v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 我们研究类比轨迹迁移，其目标是将一个3D环境中的运动轨迹迁移至另一个环境中语义相似的位置。这种能力将使机器能够进行类比空间推理，可应用于增强现实/虚拟现实（AR/VR）共在、内容创作和机器人技术。然而，即使语义相似的场景在物体放置、尺度和布局上仍可能存在显著差异，因此简单的语义匹配会导致碰撞或几何畸变。此外，由于映射必须在不撕裂轨迹或引发碰撞的前提下保持语义和功能性，寻找每个轨迹点应迁移到的位置具有巨大的搜索空间。我们的关键洞察是将问题分解为空间分离的子问题，并通过合并其解决方案来生成语义一致且空间连贯的迁移结果。具体而言，我们将场景划分为以物体为中心的聚类，并利用编码物体与开放空间布局上下文信息的3D基础模型特征，通过分层平滑映射预测来估计跨场景映射。随后，我们将各聚类映射组合成初始迁移结果，并通过优化消除碰撞与畸变，最终获得空间连贯的轨迹。我们的方法无需训练，运行时间仅约0.6秒，且性能优于基于大语言模型（LLM）、视觉语言模型（VLM）和场景图匹配的基线方法。我们进一步展示了该方法在虚拟共在、多轨迹迁移、相机迁移以及人机运动迁移中的应用，这表明了我们的工作对AR/VR和机器人领域的广泛适用性。

---

### 7. Towards Real-Time Autonomous Navigation: Transformer-Based Catheter Tip Tracking in Fluoroscopy

- **作者**: Harry Robertshaw, Yanghe Hao, Weiyuan Deng, Benjamin Jackson, S. M. Hadi Sadati, Nikola Fischer, Tom Vercauteren, Alejandro Granados, Thomas C. Booth
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.14253v1)
- **发表日期**: 2026-05-14
- **匹配关键词**: navigation, autonomous navigation
- **arXiv**: [2605.14253v1](http://arxiv.org/abs/2605.14253v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 目的：机械取栓术（MT）可改善卒中预后，但受限于局部治疗可及性不足。基于强化学习（RL）的机器人系统可通过自主导航缓解这一挑战，但现有RL方法需实时追踪器械尖端坐标。本文旨在开发并评估一种透视引导下的实时导管尖端追踪流程，以解决低对比度、噪声及器械遮挡等难题。方法：设计多线程处理流程，包含帧读取、预处理、推理及后处理模块。采用U-Net、U-Net+Transformer及SegFormer等深度学习分割模型，基于二分类与三分类方案进行训练与基准测试。后处理包含两步组件滤波、单像素中轴骨架化及带轮廓回退的贪婪弧长路径追踪。结果：在人工标注的中等复杂度透视视频数据中，二分类SegFormer模型平均绝对误差为4.44 mm，优于U-Net（4.60 mm）、U-Net+Transformer（6.20 mm）及所有三分类模型（5.19-7.74 mm）。在分割基准测试中，本系统在三分割任务中的Dice评分较现有最优CathAction方法提升达5%。结论：结果表明，所提出的多线程追踪框架在复杂成像条件下保持稳定性能，超越既往基准，为基于RL的自主MT导航提供了可靠高效的基础。

---

### 8. Safety-Constrained Reinforcement Learning with Post-Training Reachability Verification for Robot Navigation

- **作者**: Qisong He, Xinmiao Huang, Jinwei Hu, Zhuoyun Li, Yi Dong, Changshun Wu, Xiaowei Huang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.14174v1)
- **发表日期**: 2026-05-13
- **匹配关键词**: navigation, robot navigation
- **arXiv**: [2605.14174v1](http://arxiv.org/abs/2605.14174v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 移动机器人安全导航要求策略在杂乱环境的高后果感知不确定性下仍保持可靠。然而，现有大多数安全强化学习方法通过平均累积成本评估安全性，这类指标可能掩盖危险的尾部风险行为。为此，我们提出一个框架：在离策略TD3骨干网络上通过条件风险价值约束优化训练风险敏感策略，并在训练后通过神经网络可达性验证评估其安全裕度。训练阶段，策略在累积成本的条件风险价值约束下进行优化，从而提升对高成本尾部结果的敏感性，而非仅关注平均行为。训练完成后，我们利用泰勒模型分析计算有界观测不确定性下的动作可达集，得到安全率指标——该指标量化评估状态下策略可达动作集保持在预设安全裕度内的状态比例。关键发现是：经条件风险价值约束训练的策略在评估状态下能保持更大的障碍物安全裕度，这使得它们更易于通过形式化可达性验证。在十个导航场景和六个基线方法的实验中，我们的方法实现了98.3%的成功率，在所有对比方法中获得最高安全验证率，同时揭示了平均成本排序与基于可达性的安全排序可能产生分歧。这表明可达性验证能捕捉到仅凭经验成本指标无法识别的风险。我们进一步在实体Clearpath Jackal机器人上验证了该方法，成功实现了仿真到现实的迁移。

---

