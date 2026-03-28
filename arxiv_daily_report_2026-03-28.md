# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-03-28 08:04

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 6/20 篇提供

**🌟 Highlight**: 20 篇 | **📌 Poster**: 0 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. SoftMimicGen: A Data Generation System for Scalable Robot Learning in Deformable Object Manipulation

- **作者**: Masoud Moghani, Mahdi Azizian, Animesh Garg, Yuke Zhu, Sean Huver, Ajay Mandlekar ⭐
  - **高亮作者**: Yuke Zhu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.25725v1)
- **发表日期**: 2026-03-26
- **匹配关键词**: object manipulation
- **arXiv**: [2603.25725v1](http://arxiv.org/abs/2603.25725v1)
- **📥 PDF**: 已下载至本地 (`2603.25725v1_SoftMimicGen_A_Data_Generation_System_for_Scalable_Robot_Learning_in_Deformable_Object_Manipulation.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://softmimicgen.github.io
- **中文摘要**: 大规模机器人数据集已促进了多种机器人操作技能的学习，但由于需要耗费大量人力、时间和成本，这些数据集的收集与扩展仍面临困难。仿真与合成数据生成已被证明是满足数据需求的有效替代方案，特别是近期研究表明此类合成数据集能显著减少对真实世界数据的需求，并促进对真实演示中未见过的新场景的泛化能力。然而，这一范式目前主要局限于易于模拟的刚体任务。可变形物体操作在真实世界操作中占据重要部分，却仍是阻碍合成仿真数据范式进一步推广的关键缺口。本文提出SoftMimicGen——一个面向可变形物体操作任务的自动化数据生成流程。我们构建了一套高保真仿真环境，涵盖多种可变形物体（毛绒玩具、绳索、纸巾、毛巾）和操作行为（高精度穿线、动态挥动、折叠、抓取放置），并适配四种机器人形态：单臂机械手、双臂机械手、人形机器人和手术机器人。我们应用SoftMimicGen在任务套件中生成数据集，基于数据训练高性能策略，并对数据生成系统进行系统性分析。项目网站：\href{https://softmimicgen.github.io}{softmimicgen.github.io}。

---

### 2. Fast-dVLA: Accelerating Discrete Diffusion VLA to Real-Time Performance

- **作者**: Wenxuan Song, Jiayi Chen, Shuai Chen, Jingbo Wang, Pengxiang Ding, Han Zhao, Yikai Qin, Xinhu Zheng, Donglin Wang, Yan Wang, Haoang Li
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.25661v1)
- **发表日期**: 2026-03-26
- **匹配关键词**: VLA, HRI
- **arXiv**: [2603.25661v1](http://arxiv.org/abs/2603.25661v1)
- **📥 PDF**: 已下载至本地 (`2603.25661v1_Fast-dVLA_Accelerating_Discrete_Diffusion_VLA_to_Real-Time_Performance.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://chris1220313648.github.io/Fast-dVLA/
- **中文摘要**: 本文提出一种新方法，以解决预训练视觉语言动作模型在标准监督微调过程中常难以有效提升性能并降低适应成本的问题。现有部分采用辅助训练目标的高级微调方法虽能提升性能并减少收敛步数，但通常会因辅助任务带来的额外损失而产生显著计算开销。为在保持标准监督微调简洁性的同时实现辅助训练的能力增强效果，我们将辅助任务训练在参数空间中的两个目标——即增强通用能力与拟合任务特定动作分布——进行解耦处理。为实现这一目标，我们仅需通过两种不同训练策略使模型在小规模任务集上收敛，所得模型参数的差异即可解释为辅助任务提供的能力向量。这些向量随后与预训练参数融合，形成能力增强的元模型。此外，当标准监督微调辅以轻量级正交正则化损失时，融合模型能以更低计算开销达到与辅助微调基线相当的性能水平。实验结果表明，该方法在多样化机器人任务中均表现出显著有效性。项目页面：https://chris1220313648.github.io/Fast-dVLA/

---

### 3. Towards Embodied AI with MuscleMimic: Unlocking full-body musculoskeletal motor learning at scale

- **作者**: Chengkun Li, Cheryl Wang, Bianca Ziliotto, Merkourios Simos, Jozsef Kovecses, Guillaume Durandau, Alexander Mathis
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.25544v1)
- **发表日期**: 2026-03-26
- **匹配关键词**: bimanual manipulation
- **arXiv**: [2603.25544v1](http://arxiv.org/abs/2603.25544v1)
- **📥 PDF**: 已下载至本地 (`2603.25544v1_Towards_Embodied_AI_with_MuscleMimic_Unlocking_full-body_musculoskeletal_motor_learning_at_scale.pdf`)
- **🔓 开源**: CODE, GITHUB
  - 链接：https://github.com/amathislab/musclemimic
- **中文摘要**: 学习肌肉驱动骨骼肌模型运动控制的难点在于生物力学精确模拟的计算成本高昂，且经过验证的开放式全身模型稀缺。本文提出MuscleMimic——一个基于生理真实肌肉驱动人形体的可扩展运动模仿学习开源框架。该框架提供两个经过验证的骨骼肌实体：用于双手操作的固定躯干上半身模型（126块肌肉）和用于全身运动的完整人体模型（416块肌肉），并配备运动重定向流程，可将SMPL格式动作捕捉数据映射至骨骼肌结构，同时保持运动学与动力学一致性。通过大规模并行GPU模拟，该框架相比先前基于CPU的方法实现了数量级训练加速，同时保持全面碰撞处理能力，使得单一通用策略能在数日内完成数百种多样化动作的训练。所得策略能在完整肌肉控制下精准复现广泛的人类动作谱系，并可在数小时内针对新动作进行微调。基于实验步行与跑步数据的生物力学验证显示，关节运动学具有高度一致性（平均相关系数r=0.90），而肌肉激活分析则揭示了仅通过运动学模仿实现生理真实性的潜力与根本挑战。通过降低骨骼肌模拟的计算与数据门槛，MuscleMimic支持跨多样化动态运动的系统性模型验证，并促进神经肌肉控制研究的广泛参与。代码、模型、检查点及重定向数据集详见：https://github.com/amathislab/musclemimic

---

### 4. LILAC: Language-Conditioned Object-Centric Optical Flow for Open-Loop Trajectory Generation

- **作者**: Motonari Kambara, Koki Seno, Tomoya Kaichi, Yanan Wang, Komei Sugiura
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.25481v1)
- **发表日期**: 2026-03-26
- **匹配关键词**: vision-language-action model, object manipulation, VLA, vision-language-action
- **arXiv**: [2603.25481v1](http://arxiv.org/abs/2603.25481v1)
- **📥 PDF**: 已下载至本地 (`2603.25481v1_LILAC_Language-Conditioned_Object-Centric_Optical_Flow_for_Open-Loop_Trajectory_Generation.pdf`)
- **🔓 开源**: PROJECT_PAGE
- **中文摘要**: 我们提出了一种基于流轨迹生成的语言条件机器人操控方法，该方法能够利用人类操作视频和网络视频进行训练，仅需极少量的实体适配数据。这项任务具有挑战性，因为从操作前图像和自然语言指令生成物体轨迹需要实现指令与运动流的精准对齐。为解决这一难题，我们提出了基于流的语言指令引导开环动作生成器（LILAC）。这个基于流的视觉-语言-动作模型通过RGB图像和自然语言指令生成以物体为中心的二维光流，并将光流转换为六自由度机械臂轨迹。LILAC包含两个核心组件：语义对齐损失函数——通过强化语言条件约束来生成与指令对齐的光流；提示条件跨模态适配器——将学习到的视觉提示与图像文本特征对齐，为光流生成提供丰富线索。实验表明，我们的方法在多个基准测试中的光流生成质量优于现有方法。此外，在使用自由格式指令的实体物体操控实验中，LILAC相比现有方法展现出更高的任务成功率。项目页面详见 https://lilac-75srg.kinsta.page/。

---

### 5. MMaDA-VLA: Large Diffusion Vision-Language-Action Model with Unified Multi-Modal Instruction and Generation

- **作者**: Yang Liu, Pengxiang Ding, Tengyue Jiang, Xudong Wang, Wenxuan Song, Minghui Lin, Han Zhao, Hongyin Zhang, Zifeng Zhuang, Wei Zhao, Siteng Huang, Jinkui Shi, Donglin Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.25406v1)
- **发表日期**: 2026-03-26
- **匹配关键词**: vision-language-action model, VLA, vision-language-action
- **arXiv**: [2603.25406v1](http://arxiv.org/abs/2603.25406v1)
- **📥 PDF**: 已下载至本地 (`2603.25406v1_MMaDA-VLA_Large_Diffusion_Vision-Language-Action_Model_with_Unified_Multi-Modal_Instruction_and_Gene.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型旨在通过视觉观察和自然语言指令控制机器人执行操作任务。然而，现有的分层与自回归范式常伴随架构冗余、时序不一致性及长时程误差累积等问题，且缺乏无需额外模块即可捕捉环境动态的机制。为此，我们提出MMaDA-VLA——一个完全原生的预训练大型扩散VLA模型，将多模态理解与生成统一于单一框架。其核心创新在于原生离散扩散建模方法：将语言、图像及连续机器人控制嵌入统一离散标记空间，通过掩码标记去噪训练单一主干网络，实现未来目标观测与动作片段的并行生成。迭代去噪机制支持全局无序优化，在提升长时程一致性的同时，使动作生成基于预测的未来视觉结果，无需辅助世界模型。在仿真基准测试和实际任务中的实验表明，该方法达到最先进性能：在LIBERO基准上取得98.0%的平均成功率，在CALVIN基准上实现4.78的平均任务长度。

---

### 6. LaMP: Learning Vision-Language-Action Policies with 3D Scene Flow as Latent Motion Prior

- **作者**: Xinkai Wang, Chenyi Wang, Yifu Xu, Mingzhe Ye, Fu-Cheng Zhang, Jialin Tian, Xinyu Zhan, Lifeng Zhu, Cewu Lu, Lixin Yang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.25399v1)
- **发表日期**: 2026-03-26
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2603.25399v1](http://arxiv.org/abs/2603.25399v1)
- **📥 PDF**: 已下载至本地 (`2603.25399v1_LaMP_Learning_Vision-Language-Action_Policies_with_3D_Scene_Flow_as_Latent_Motion_Prior.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://summerwxk.github.io/lamp-project-page/.
- **中文摘要**: 我们提出\textbf{LaMP}——一种双专家视觉-语言-动作框架，它将稠密三维场景流作为机器人操作的潜在运动先验进行嵌入。现有VLA模型直接从二维语义视觉特征回归动作，迫使它们隐式学习复杂的三维物理交互。这种隐式学习策略在陌生空间动态下性能会下降。LaMP通过门控交叉注意力将流匹配的\emph{运动专家}与策略预测的\emph{动作专家}对齐，从而解决这一局限。具体而言，运动专家生成单步部分去噪的三维场景流，其隐藏状态在不进行完整多步重建的情况下为动作专家提供条件。我们在LIBERO、LIBERO-Plus和SimplerEnv-WidowX仿真基准以及真实世界实验中评估LaMP。在相同训练预算下，LaMP在LIBERO、LIBERO-Plus和SimplerEnv-WidowX基准测试中始终优于现有VLA基线，取得了目前报道的最高平均成功率。在LIBERO-Plus分布外扰动测试中，LaMP展现出更强的鲁棒性，较先前最强基线平均提升9.7%。项目页面详见https://summerwxk.github.io/lamp-project-page/。

---

### 7. IntentReact: Guiding Reactive Object-Centric Navigation via Topological Intent

- **作者**: Yanmei Jiao, Anpeng Lu, Wenhan Hu, Rong Xiong, Yue Wang, Huajin Tang, Wen-an Zhang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.25382v1)
- **发表日期**: 2026-03-26
- **匹配关键词**: navigation, visual navigation
- **arXiv**: [2603.25382v1](http://arxiv.org/abs/2603.25382v1)
- **📥 PDF**: 已下载至本地 (`2603.25382v1_IntentReact_Guiding_Reactive_Object-Centric_Navigation_via_Topological_Intent.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 物体目标视觉导航要求机器人能够理解语义结构并在部分可观测条件下有效行动。基于物体级拓扑地图的最新方法实现了无需密集几何重建的长距离导航，但其执行仍受限于全局拓扑引导与局部感知驱动控制之间的鸿沟。具体而言，局部决策仅基于当前以自我为中心的观测，无法获取机器人视野范围外的信息。这导致机器人即使初始朝向偏离目标，仍可能持续沿当前方向行进，朝着无法缩短全局拓扑距离的方向移动。本研究提出IntentReact框架——一种以意图为条件的物体中心导航系统，通过在全局拓扑规划与反应式物体中心控制之间建立紧凑接口。我们的方法将全局拓扑引导编码为低维方向信号（称为意图），该信号通过调节学习型航点预测策略，使导航偏向拓扑一致的前进方向。这种设计使机器人能在局部观测产生误导时迅速调整方向，引导运动朝着缩短全局拓扑距离的方向发展，同时保持物体中心控制的反应性与鲁棒性。通过大量实验评估，本框架相较于现有物体中心导航方法，在导航成功率与执行质量方面均展现出显著提升。

---

### 8. SafeGuard ASF: SR Agentic Humanoid Robot System for Autonomous Industrial Safety

- **作者**: Thanh Nguyen Canh, Thang Tran Viet, Thanh Tuan Tran, Ben Wei Lim
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.25353v1)
- **发表日期**: 2026-03-26
- **匹配关键词**: obstacle avoidance
- **arXiv**: [2603.25353v1](http://arxiv.org/abs/2603.25353v1)
- **📥 PDF**: 已下载至本地 (`2603.25353v1_SafeGuard_ASF_SR_Agentic_Humanoid_Robot_System_for_Autonomous_Industrial_Safety.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 随着无需人员值守的"黑灯工厂"兴起，工业场景亟需能够检测并应对多种危险类型的自主安全系统。本文提出SafeGuard ASF（智能体化安防集群）框架，通过部署人形机器人实现工业环境自主危险检测。该系统在宇树G1人形机器人平台上整合了多模态感知（RGB-D成像）、基于ReAct架构的智能体推理框架以及学习型运动策略。我们针对三类典型危险场景展开研究：火灾烟雾检测、管道异常温度监测和限制区域入侵检测。感知模块在127毫秒延迟下实现94.2%平均精度（mAP）的火灾烟雾检测性能。通过宇树强化学习实验室平台采用PPO算法，我们训练了包括舞蹈动作追踪与速度控制在内的多种运动策略，在8万次训练迭代内实现稳定收敛。该系统在仿真与真实环境中均通过验证，展现出自主巡逻、基于视觉感知的人员检测及避障能力。所提出的ToolOrchestra行动框架通过感知、推理与执行工具的协同，实现了结构化决策流程。

---

### 9. ThermoAct:Thermal-Aware Vision-Language-Action Models for Robotic Perception and Decision-Making

- **作者**: Young-Chae Son, Dae-Kwan Ko, Yoon-Ji Choi, Soo-Chul Lim
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.25044v1)
- **发表日期**: 2026-03-26
- **匹配关键词**: vision-language-action model, vision-language-action, VLA, human-robot collaboration
- **arXiv**: [2603.25044v1](http://arxiv.org/abs/2603.25044v1)
- **📥 PDF**: 已下载至本地 (`2603.25044v1_ThermoActThermal-Aware_Vision-Language-Action_Models_for_Robotic_Perception_and_Decision-Making.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 在近期的人机协作环境中，研究者日益关注整合视觉信息之外的多样化传感器数据，以实现更安全、更智能的任务执行。尽管热成像数据对于提升机器人安全性与操作效率具有关键作用，但在先前研究中其整合应用相对被忽视。本文提出一种融合热成像信息的新型视觉-语言-动作框架用于机器人任务执行。该系统利用视觉语言模型作为高层规划器，解析复杂自然语言指令并将其分解为简单子任务，从而为复杂操作实现高效数据收集与鲁棒推理。与传统仅依赖视觉数据的方法不同，本方案通过整合热成像信息，使机器人能够感知物理特性并主动保障环境安全。真实任务场景中的实验结果验证了所提框架的可行性，表明相较于现有视觉系统，该框架有望提升任务成功率与安全性。

---

### 10. Beyond Attention Magnitude: Leveraging Inter-layer Rank Consistency for Efficient Vision-Language-Action Models

- **作者**: Peiju Liu, Jinming Liu, Xipeng Qiu, Xuanjing Huang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.24941v1)
- **发表日期**: 2026-03-26
- **匹配关键词**: vision-language-action model, VLA, vision-language-action
- **arXiv**: [2603.24941v1](http://arxiv.org/abs/2603.24941v1)
- **📥 PDF**: 已下载至本地 (`2603.24941v1_Beyond_Attention_Magnitude_Leveraging_Inter-layer_Rank_Consistency_for_Efficient_Vision-Language-Act.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型在机器人操作任务中表现出色，但由于需要处理密集的视觉标记，其推理延迟问题显著。现有的标记缩减方法主要依赖注意力权重作为静态选择依据。本研究对这一假设提出挑战，揭示了高注意力标记具有任务依赖性，甚至可能降低策略性能。为解决这一问题，我们提出了**TIES**（基于τ引导的层间高效选择框架），这是一个通过层间标记排序一致性引导的动态框架。通过自适应平衡注意力权重与排序一致性，TIES能在无需额外训练的情况下实现鲁棒的标记选择。在CogACT + SIMPLER基准测试中，TIES将平均成功率提升6%，同时减少78%的标记使用量，并在不同解码器和基准测试中展现出强大的泛化能力。

---

### 11. SABER: A Stealthy Agentic Black-Box Attack Framework for Vision-Language-Action Models

- **作者**: Xiyang Wu, Guangyao Shi, Qingzi Wang, Zongxia Li, Amrit Singh Bedi, Dinesh Manocha
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.24935v1)
- **发表日期**: 2026-03-26
- **匹配关键词**: vision-language-action model, VLA, vision-language-action
- **arXiv**: [2603.24935v1](http://arxiv.org/abs/2603.24935v1)
- **📥 PDF**: 已下载至本地 (`2603.24935v1_SABER_A_Stealthy_Agentic_Black-Box_Attack_Framework_for_Vision-Language-Action_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型使机器人能够遵循基于视觉观察的自然语言指令，但指令通道也引入了一个关键漏洞：微小的文本扰动可能改变下游机器人行为。因此，系统性鲁棒性评估需要一个能够跨不同VLA模型生成最小化但有效指令编辑的黑盒攻击器。为此，我们提出SABER——一种以智能体为中心的方法，用于在有限编辑预算下自动生成针对VLA模型的指令对抗攻击。SABER采用GRPO训练的ReAct攻击器，在有限编辑预算下使用字符级、词元级和提示级工具生成微小且合理的对抗性指令编辑，从而引发目标行为退化，包括任务失败、执行时间过长及约束违反增加。在涵盖六个前沿VLA模型的LIBERO基准测试中，SABER将任务成功率降低20.6%，动作序列长度增加55%，约束违反率提升33%，同时相较于基于GPT的强基线方法，工具调用次数减少21.1%，字符编辑量降低54.7%。这些结果表明，微小且合理的指令编辑足以显著削弱机器人执行性能，而智能化的黑盒流程为红队测试机器人基础模型提供了一种实用、可扩展且自适应的解决方案。

---

### 12. FODMP: Fast One-Step Diffusion of Movement Primitives Generation for Time-Dependent Robot Actions

- **作者**: Xirui Shi, Arya Ebrahimi, Yi Hu, Jun Jin
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.24806v1)
- **发表日期**: 2026-03-25
- **匹配关键词**: diffusion policy
- **arXiv**: [2603.24806v1](http://arxiv.org/abs/2603.24806v1)
- **📥 PDF**: 已下载至本地 (`2603.24806v1_FODMP_Fast_One-Step_Diffusion_of_Movement_Primitives_Generation_for_Time-Dependent_Robot_Actions.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 扩散模型在机器人学习中的应用日益广泛，但现有设计面临明显的权衡困境。动作分块扩散策略（如ManiCM）虽运行速度快，却只能预测短时运动片段。这使得它们具备快速反应能力，但无法捕捉具有时间依赖性的运动基元，例如遵循类似弹簧阻尼器行为、内置加速与减速动态特性的运动模式。近期提出的运动基元扩散（MPD）通过概率动态运动基元（ProDMPs）参数化完整轨迹，部分解决了这一局限，从而能够生成具有时间结构性的运动。然而，MPD将运动解码器直接整合到多步扩散过程中，导致推理延迟过高，限制了其在实时控制场景中的应用。我们提出FODMP（快速单步运动基元扩散）——一种将扩散模型蒸馏至ProDMPs轨迹参数空间，并通过单步解码器生成运动的新框架。FODMP在保持运动基元时间结构的同时，通过单步一致性蒸馏消除了推理瓶颈，使机器人能够以高推理速度执行时间依赖性基元，适用于基于视觉的闭环控制。在标准操作基准测试（MetaWorld、ManiSkill）中，FODMP的运行速度比MPD快10倍，比动作分块扩散策略快7倍，同时达到或超越其成功率。除速度优势外，通过生成快速加减速运动基元，FODMP使机器人能够拦截并安全接住高速飞行的球体，而动作分块扩散策略和MPD因响应过慢无法实现实时拦截。

---

### 13. TAG: Target-Agnostic Guidance for Stable Object-Centric Inference in Vision-Language-Action Models

- **作者**: Jiaying Zhou, Zhihao Zhan, Ruifeng Zhai, Qinhan Lyu, Hao Liu, Keze Wang, Liang Lin, Guangrun Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.24584v1)
- **发表日期**: 2026-03-25
- **匹配关键词**: vision-language-action model, VLA, vision-language-action
- **arXiv**: [2603.24584v1](http://arxiv.org/abs/2603.24584v1)
- **📥 PDF**: 已下载至本地 (`2603.24584v1_TAG_Target-Agnostic_Guidance_for_Stable_Object-Centric_Inference_in_Vision-Language-Action_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）策略在将语言指令和视觉观察映射为机器人动作方面取得了显著进展，但在存在干扰物的杂乱场景中，其可靠性会下降。通过分析失败案例，我们发现许多错误并非源于不可行的运动，而是由实例级定位失败引起的：策略常常生成看似合理的抓取轨迹，但最终落点略微偏离目标，甚至落在错误的物体实例上。为解决这一问题，我们提出了TAG（目标无关引导），这是一种简单的推理时引导机制，旨在明确减少VLA策略中由干扰物和外观引起的偏差。受无分类器引导（CFG）的启发，TAG对比了原始观察和物体擦除观察下的策略预测，并将它们的差异用作残差引导信号，以增强物体证据在决策过程中的影响。TAG无需修改策略架构，只需对现有VLA策略进行极少的训练和推理调整即可集成。我们在标准操作基准测试（包括LIBERO、LIBERO-Plus和VLABench）上评估了TAG，结果显示它在杂乱环境下持续提升了鲁棒性，并减少了接近失误和错误物体执行的情况。

---

### 14. EndoVGGT: GNN-Enhanced Depth Estimation for Surgical 3D Reconstruction

- **作者**: Falong Fan, Yi Xie, Arnis Lektauers, Bo Liu, Jerzy Rozenblit
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.24577v1)
- **发表日期**: 2026-03-25
- **匹配关键词**: nerf, 3D reconstruction, 3d reconstruction
- **arXiv**: [2603.24577v1](http://arxiv.org/abs/2603.24577v1)
- **📥 PDF**: 已下载至本地 (`2603.24577v1_EndoVGGT_GNN-Enhanced_Depth_Estimation_for_Surgical_3D_Reconstruction.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 可变形软组织的精确三维重建对于手术机器人感知至关重要。然而，低纹理表面、镜面高光和器械遮挡常导致几何连续性断裂，这对现有固定拓扑方法构成挑战。为此，我们提出以几何为中心的EndoVGGT框架，其配备的形变感知图注意力模块能够动态构建特征空间语义图，替代传统静态空间邻域方法，从而捕捉相干组织区域间的长程关联。该机制实现了结构信息在遮挡区域的鲁棒传播，强化全局一致性并提升非刚性形变恢复能力。在SCARED数据集上的大量实验表明，本方法显著提升重建保真度，PSNR指标较现有最优方法提高24.6%，SSIM指标提升9.1%。关键的是，EndoVGGT在未见过的SCARED和EndoNeRF数据集上展现出强大的零样本跨域泛化能力，证实了形变感知图注意力模块能够学习领域无关的几何先验。这些结果凸显了动态特征空间建模在实现稳定手术三维重建中的有效性。

---

### 15. Design, Modelling and Characterisation of a Miniature Fibre-Reinforced Soft Bending Actuator for Endoluminal Interventions

- **作者**: Xiangyi Tan, Aoife McDonald-Bowyer, Danail Stoyanov, Agostino Stilli
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.24461v1)
- **发表日期**: 2026-03-25
- **匹配关键词**: VLA
- **arXiv**: [2603.24461v1](http://arxiv.org/abs/2603.24461v1)
- **📥 PDF**: 已下载至本地 (`2603.24461v1_Design,_Modelling_and_Characterisation_of_a_Miniature_Fibre-Reinforced_Soft_Bending_Actuator_for_End.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 微型软体气动执行器对于在高度受限的解剖路径内进行机器人介入至关重要。本研究提出了一种厘米级纤维增强软体执行器的设计与验证方案，该执行器可集成于自然腔道介入诊疗的腔内机器人平台。通过采用嵌入式凯夫拉纤维增强的单腔体结构设计，在保持密封完整性的同时实现了曲率最大化；采用多阶段多硬度硅胶浇铸工艺制造，并基于实验参数化的超弹性材料模型与嵌入式梁增强结构，通过高精度Abaqus有限元模型进行了验证。该半圆柱形执行器外径为18毫米，长度为37.5毫米。研究对比了单螺旋与双螺旋缠绕构型、纤维螺距及纤维密度的影响，最终优化的100SH构型在实验中实现202.9°弯曲角度，仿真结果达297.6°，结构稳定性在100千帕压力下保持良好，纤维增强层有效抑制了径向膨胀。工作空间评估证实其符合目标设备的集成要求，表明纤维增强策略可在厘米尺度有效转化并保持执行器性能。

---

### 16. 3D-Mix for VLA: A Plug-and-Play Module for Integrating VGGT-based 3D Information into Vision-Language-Action Models

- **作者**: Bin Yu, Shijie Lian, Xiaopeng Lin, Zhaolong Shen, Yuliang Wei, Haishan Liu, Changti Wu, Hang Yuan, Bailing Wang, Cong Huang, Kai Chen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.24393v1)
- **发表日期**: 2026-03-25
- **匹配关键词**: vision-language-action model, VLA, vision-language-action
- **arXiv**: [2603.24393v1](http://arxiv.org/abs/2603.24393v1)
- **📥 PDF**: 已下载至本地 (`2603.24393v1_3D-Mix_for_VLA_A_Plug-and-Play_Module_for_Integrating_VGGT-based_3D_Information_into_Vision-Language.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型利用多模态大语言模型（MLLMs）实现机器人控制，但近期研究表明，由于主要基于二维数据进行训练，MLLMs的空间智能表现有限，导致在操作任务中三维感知能力不足。虽然现有方法通过引入VGGT等专用三维视觉模型来增强空间理解能力，但这些方法采用多样化的集成机制且缺乏系统性研究，导致最优融合策略尚不明确。我们通过系统性预研，在标准化基准上比较了九种VGGT集成方案，发现基于任务上下文自适应平衡二维语义特征与三维几何特征的语义门控融合机制，在预研评估的九种融合方案中取得了最优性能。我们提出即插即用模块3D-Mix，该模块可无缝集成至多种VLA架构（GR00T型与$π$型）中，无需修改现有MLLM或动作专家组件。在SIMPLER和LIBERO基准上对六个MLLM系列（九种模型变体，参数量2B-8B）的实验表明，3D-Mix能带来稳定的性能提升：在九种GR00T型变体上，域外（OOD）SIMPLER基准平均提升达+7.0%，为增强VLA系统空间智能提供了理论完备的解决方案。

---

### 17. Less Gaussians, Texture More: 4K Feed-Forward Textured Splatting

- **作者**: Yixing Lao, Xuyang Bai, Xiaoyang Wu, Nuoyuan Yan, Zixin Luo, Tian Fang, Jean-Daniel Nahmias, Yanghai Tsin, Shiwei Li, Hengshuang Zhao
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.25745v1)
- **发表日期**: 2026-03-26
- **匹配关键词**: 3D gaussian splatting, gaussian splatting
- **arXiv**: [2603.25745v1](http://arxiv.org/abs/2603.25745v1)
- **📥 PDF**: 已下载至本地 (`2603.25745v1_Less_Gaussians,_Texture_More_4K_Feed-Forward_Textured_Splatting.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://yxlao.github.io/lgtm/
- **中文摘要**: 现有前馈式3D高斯泼溅方法通过预测像素对齐的图元，导致图元数量随分辨率提升呈二次增长。这一根本性局限制约了方法的可扩展性，使得4K等高分辨率合成难以实现。本文提出LGTM（更少高斯、更多纹理）框架，通过预测紧凑型高斯图元并配合逐图元纹理映射，成功突破分辨率缩放瓶颈。该方法将几何复杂度与渲染分辨率解耦，首次在前馈式框架中实现了无需逐场景优化的高保真4K新视角合成，同时显著减少了高斯图元的使用量。项目主页：https://yxlao.github.io/lgtm/

---

### 18. Vega: Learning to Drive with Natural Language Instructions

- **作者**: Sicheng Zuo, Yuxuan Li, Wenzhao Zheng, Zheng Zhu, Jie Zhou, Jiwen Lu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.25741v1)
- **发表日期**: 2026-03-26
- **匹配关键词**: vision-language-action model, vision-language-action
- **arXiv**: [2603.25741v1](http://arxiv.org/abs/2603.25741v1)
- **📥 PDF**: 已下载至本地 (`2603.25741v1_Vega_Learning_to_Drive_with_Natural_Language_Instructions.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-行动模型通过将语言融入决策过程，重塑了自动驾驶领域。然而，现有研究大多仅将语言模态用于场景描述或推理，缺乏遵循多样化用户指令以实现个性化驾驶的灵活性。为此，我们首先构建了一个大规模驾驶数据集（InstructScene），包含约10万个场景，每个场景都标注了多样化的驾驶指令及对应轨迹。随后，我们提出了一种统一的视觉-语言-世界-行动模型Vega，用于基于指令的生成与规划。我们采用自回归范式处理视觉输入（视觉）和语言指令（语言），并运用扩散范式生成未来预测（世界建模）和轨迹（行动）。通过联合注意力机制实现多模态间的交互，并为不同模态设计独立投影层以增强模型能力。大量实验表明，我们的方法不仅在规划性能上表现卓越，还展现出强大的指令遵循能力，为更智能、个性化的驾驶系统开辟了新路径。

---

### 19. Accurate Surface and Reflectance Modelling from 3D Radar Data with Neural Radiance Fields

- **作者**: Judith Treffler, Vladimír Kubelka, Henrik Andreasson, Martin Magnusson
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.25623v1)
- **发表日期**: 2026-03-26
- **匹配关键词**: implicit representation, neural radiance field
- **arXiv**: [2603.25623v1](http://arxiv.org/abs/2603.25623v1)
- **📥 PDF**: 已下载至本地 (`2603.25623v1_Accurate_Surface_and_Reflectance_Modelling_from_3D_Radar_Data_with_Neural_Radiance_Fields.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 稳健的场景表征对于自主系统在低能见度挑战环境中安全运行至关重要。雷达因其对雾、烟、尘等环境干扰的强抗扰性，在此类条件下较相机与激光雷达具有明显优势。然而雷达数据本身具有稀疏性与噪声特性，使得可靠的3D表面重建面临挑战。为解决这些问题，我们提出一种基于神经隐式表达的雷达点云三维建图方法，该方法能够联合建模场景几何结构与视角相关的雷达反射强度。我们采用内存高效的混合特征编码技术，通过学习连续有向距离场实现表面重建，同时捕捉雷达特有的反射特性。实验表明，相较于现有应用于雷达数据的激光雷达重建方法，本方法能生成更平滑、更精确的三维表面重建结果，并能重构视角相关的雷达反射强度。研究还发现，当输入点云趋于稀疏时，相较于传统显式有向距离场与网格化技术，神经隐式表征能呈现更真实的表面细节。

---

### 20. Drive My Way: Preference Alignment of Vision-Language-Action Model for Personalized Driving

- **作者**: Zehao Wang, Huaide Jiang, Shuaiwu Dong, Yuping Wang, Hang Qiu, Jiachen Li
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.25740v1)
- **发表日期**: 2026-03-26
- **匹配关键词**: vision-language-action model, VLA, vision-language-action
- **arXiv**: [2603.25740v1](http://arxiv.org/abs/2603.25740v1)
- **📥 PDF**: 已下载至本地 (`2603.25740v1_Drive_My_Way_Preference_Alignment_of_Vision-Language-Action_Model_for_Personalized_Driving.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 人类驾驶行为具有天然的个性化特征，既受长期习惯塑造，又受短期意图影响。不同个体在加速、制动、并线、让行、超车等场景中均表现出差异性。然而，现有的端到端自动驾驶系统要么优化通用目标，要么依赖固定驾驶模式，缺乏适应个体偏好或解析自然语言意图的能力。为填补这一空白，我们提出"Drive My Way"（DMW）个性化视觉-语言-动作驾驶框架，该系统既能适应用户长期驾驶习惯，又能响应实时用户指令。DMW通过我们在多驾驶员、多场景条件下收集的个性化驾驶数据集学习用户嵌入表征，并在规划过程中以此嵌入作为策略条件，同时通过自然语言指令提供额外的短期引导。在Bench2Drive基准测试中的闭环评估表明，DMW显著提升了驾驶风格指令适应能力；用户研究证实其生成行为可被识别为对应驾驶员的个人风格，凸显个性化作为人本自动驾驶核心能力的价值。相关数据与代码已发布于https://dmw-cvpr.github.io/。

---

