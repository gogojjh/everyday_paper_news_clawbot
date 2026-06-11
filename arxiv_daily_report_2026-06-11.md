# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-06-11 08:02

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 3/20 篇提供

**🌟 Highlight**: 20 篇 | **📌 Poster**: 0 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. WorldOlympiad: Can Your World Model Survive a Triathlon?

- **作者**: Yuke Zhao, Wangbo Zhao, Weijie Wang, Zeyu Zhang, Dakai An, Akide Liu, Yinghao Yu, Jiasheng Tang, Fan Wang, Wei Wang, Bohan Zhuang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.11129v1)
- **发表日期**: 2026-06-09
- **匹配关键词**: gaussian splatting
- **arXiv**: [2606.11129v1](http://arxiv.org/abs/2606.11129v1)
- **📥 PDF**: 已下载至本地 (`2606.11129v1_WorldOlympiad_Can_Your_World_Model_Survive_a_Triathlon?.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出了WorldOlympiad基准，用于从物理真实性、几何一致性和交互保真度三个维度诊断基于视频的世界模型。现有基准通常关注视觉质量、语义对齐或短期时间连贯性，但难以判断生成视频是否遵循物理规律、保持连贯的三维结构，以及能否在长时程中维持可控交互。为填补这一空白，WorldOlympiad将世界模型评估分解为三个互补维度：物理轨迹通过物体分割和多模态大语言模型评判机制，评估生成视频在力学、热现象和材料属性方面是否遵循可解释规则；几何轨迹利用高斯泼溅重建生成视频，评估结构一致性、跨视角连贯性和相机轨迹对齐度；交互轨迹则评估生成序列是否遵循复杂动作提示，并在连续视频片段间保持平滑连贯的过渡。WorldOlympiad进一步覆盖游戏、机器人和通用真实世界视频三大下游场景，囊括从交互控制、具身操作到开放域运动与相机动态的多样化挑战。这些轨迹与场景共同构成可扩展、可解释的评估体系，能够暴露超越通用视频质量的失效模式。针对当前最先进模型的实验表明，其在物理推理、三维一致性和长时程交互方面存在显著缺陷，凸显了为生成式世界模型建立更结构化评估协议的必要性。

---

### 2. AgniNav: Configuration-Driven Cross-Embodiment Local Planning for Robot Navigation

- **作者**: Tianhao Zang, Siwei Cheng, Haidong Huang, Shanze Wang, Wei Zhang
- **单位**: Eastern Institute of Technology, Ningbo, China; University of Science and Technology of China, Hefei, China; University of Nottingham, Nottingham, UK...
- **发表日期**: 2026-06-09
- **匹配关键词**: navigation, robot navigation
- **arXiv**: [2606.10903v1](http://arxiv.org/abs/2606.10903v1)
- **📥 PDF**: 已下载至本地 (`2606.10903v1_AgniNav_Configuration-Driven_Cross-Embodiment_Local_Planning_for_Robot_Navigation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 单目局部导航对轻量级机器人具有吸引力，但现有的基于视觉的策略通常将感知与特定本体、相机高度和足迹耦合，导致从轮式底盘到足式平台的迁移依赖于重新训练或主动深度硬件。本文提出AgniNav，一种配置驱动的局部导航框架，在碰撞包络层面标准化跨形态迁移。每个机器人通过可测量的四参数安全包络定义：碰撞相关高度、前部长度、后部长度和半宽度。高度参数调节图像到扫描网络的预测，从单目彩色图像生成一维碰撞相关伪激光扫描，而剩余足迹参数配置维度感知的局部规划器进行碰撞检测。训练使用从配对彩色深度数据生成的高度条件列最小扫描标签，使同一图像可监督不同安全包络，无需收集机器人特定数据。据我们所知，AgniNav是首个在共享碰撞包络配置上联合调节感知与规划的单目局部导航框架，实现跨轮式、四足和人形平台的零重训练部署。在Turtlebot2、Unitree Go2和Accelerated Evolution K1上的真实机器人实验中，分别达到39/40、18/20和18/20的成功率，碰撞次数分别为0/40、1/20和2/20，并在Jetson Orin上以30Hz频率运行。

---

### 3. GUIDE: Goal-Initialized Directional Understanding for End-to-End Visual Navigation

- **作者**: Liang Wang, Jin Jin, KanZhong Yao, YiBin Wu, Fangqiang Ding, Jin Wang, Jun Wu, Zhe Sun, Qiuguo Zhu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.10832v1)
- **发表日期**: 2026-06-09
- **匹配关键词**: navigation, visual navigation
- **arXiv**: [2606.10832v1](http://arxiv.org/abs/2606.10832v1)
- **📥 PDF**: 已下载至本地 (`2606.10832v1_GUIDE_Goal-Initialized_Directional_Understanding_for_End-to-End_Visual_Navigation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 基于学习的足式机器人视觉导航通常依赖层级状态估计提供的连续目标更新，以维持持久的方向参考。这种依赖性不仅增加了额外的感知与计算开销，也偏离了完全端到端的移动自主性。此外，在部分可观测条件下，策略容易学习短视行为，极易陷入死胡同和复杂结构布局。为解决这些局限，我们研究了目标初始化导航设定：目标仅在回合开始时提供一次，要求机器人基于内在空间记忆自主运行，无需外部模块后续更新目标。本文提出GUIDE——一种完全端到端的强化学习框架，旨在培养内在方向感知能力。具体而言，GUIDE包含空间锚点预测器，通过利用多频率本体感受历史提取自运动表征，从而维持导航所需的持久长时域空间上下文；同时，它利用原始深度流感知局部环境几何结构。我们在四足机器人的仿真与真实场景中评估了该框架。实验表明，GUIDE能够学习可靠的自运动与方向感知能力，使完全端到端部署的策略无需后续目标引导或先验地图，即可安全穿越密集杂乱环境与结构化迷宫。

---

### 4. ManiSplat: Manipulation Trajectory Synthesis from Monocular Video via Decoupled 3D Gaussian Splatting

- **作者**: Wenhao Hu, Haonan Zhou, Liu Liu, Yun Du, Xinjie Wang, Ziang Li, Zhizhong Su, Gaoang Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.10645v1)
- **发表日期**: 2026-06-09
- **匹配关键词**: 3D gaussian splatting, gaussian splatting, scene graph
- **arXiv**: [2606.10645v1](http://arxiv.org/abs/2606.10645v1)
- **📥 PDF**: 已下载至本地 (`2606.10645v1_ManiSplat_Manipulation_Trajectory_Synthesis_from_Monocular_Video_via_Decoupled_3D_Gaussian_Splatting.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 从真实观测中重建动态且可交互的三维场景，仍是计算机视觉与机器人领域的基础性挑战。尽管三维高斯泼溅技术的最新进展已实现高保真静态重建，但将其扩展至包含铰接式机械臂与可操作物体的交互环境时，复杂的接触交互与突变的位姿变化仍构成显著困难。为应对这些挑战，我们提出ManiSplat——一个可直接从单目自我中心视角的机器人视频中重建可控且解耦的高斯数字孪生的统一框架。该方法引入图结构解耦表示，将机器人、物体与背景分离为场景图中可独立优化的高斯子场。为确保稳定性，我们提出任务导向的时空对齐模块，利用操作任务固有的逻辑（在运动阶段与技能阶段间交替）构建精确的伪真实轨迹。最终，联合光度-几何优化确保重建场景在时间连贯性、物理一致性与仿真就绪性上达到要求。大量实验表明，本方法能以高保真度与可控性重建交互驱动的动态场景，有效支撑下游机器人任务与策略学习。

---

### 5. Dexterous Point Policy: Learning Point-based Dexterous Hand Policies from Human Demonstrations

- **作者**: Beomjun Kim, Seong Hyeon Park, Seunghoon Sim, Seungjun Moon, Sanghyeok Lee, Jinwoo Shin
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.10614v1)
- **发表日期**: 2026-06-09
- **匹配关键词**: tool use, VLA
- **arXiv**: [2606.10614v1](http://arxiv.org/abs/2606.10614v1)
- **📥 PDF**: 已下载至本地 (`2606.10614v1_Dexterous_Point_Policy_Learning_Point-based_Dexterous_Hand_Policies_from_Human_Demonstrations.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 基于人类示范视频预训练的机器人基础模型已展现出潜力，但当生成的策略部署到真实机器人上时，仍存在显著的具身性差距。常见的补救措施是在特定机器人的示范数据上微调这些模型。然而，机器人数据采集成本高昂且耗时，这在灵巧操作领域尤为突出——例如，仅通过遥操作多指手完成单个原子任务就可能需要数天时间。为解决这一问题，我们提出灵巧点策略（Dexterous Point Policy），该框架可直接从人类视频中学习灵巧操作策略，且无需任何机器人示范数据。我们的核心见解在于：统一的三维关键点表示在同时用于观测和动作时，能够弥合人类与机器人具身性之间的鸿沟。具体而言，我们从原始视频中提取任务相关物体和人类手部的三维关键点，并基于这些关键点训练自回归Transformer模型。我们观察到，在关键点层面（特别是手腕和指尖），人类与机器人的行为高度一致，从而实现了策略的直接迁移。在涵盖抓取放置与工具使用的一系列真实机器人任务中，灵巧点策略达到了75.0%的成功率，而当前最先进的VLA基线方法仅达1.0%。此外，我们的方法对未见场景（包括多物体环境和新型物体类别）展现出强大的泛化能力。

---

### 6. VeriSpace: Spatially Grounded Action Verification for Vision-Language-Action Models

- **作者**: Guiyu Zhao, Longteng Guo, Junyou Zhu, Jun Fu, Yanghong Mei, Bin Cao, Jie Jiang, Xingjian He, Jing Liu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.10568v1)
- **发表日期**: 2026-06-09
- **匹配关键词**: vision-language-action model, vision-language-action, VLA
- **arXiv**: [2606.10568v1](http://arxiv.org/abs/2606.10568v1)
- **📥 PDF**: 已下载至本地 (`2606.10568v1_VeriSpace_Spatially_Grounded_Action_Verification_for_Vision-Language-Action_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型在机器人操作任务中展现出巨大潜力，但其测试阶段的可靠性仍受限于单次动作预测——即使微小的动作误差也可能导致抓取失败、碰撞或任务进程错误。一个自然的替代方案是为VLA系统配备测试时验证机制，允许在执行前提出并评估多个候选动作。然而，可靠的动作验证极具挑战性，因为它不仅需要区分候选动作间细微的几何差异，还需评估该动作是否朝着任务目标取得有意义的进展。我们提出VeriSpace——一种面向VLA系统测试时动作选择的3D感知动作验证器。VeriSpace通过两个关键组件评估候选动作：双路径3D注入场景编码，构建同时保留视觉语义与显式3D几何结构的场景表征；空间锚定动作推理，通过推理任务相关的空间关系、几何有效性和预期目标进展来评估每个动作。这些组件协同作用，能够在保持与现有VLA策略完全兼容的同时，更可靠地区分那些细微但决定成败的候选动作。在公开基准测试和真实机器人操作任务上的实验表明，VeriSpace在分布内和分布外场景中均能持续提升底层VLA策略及现有验证方法的决策可靠性，带来显著性能增益。

---

### 7. Uncovering Vulnerability of Vision-Language-Action Models under Joint-Level Physical Faults

- **作者**: Minsoo Jo, Taeju Kwon, Junha Chun, Youngjoon Jeong, Taesup Kim
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.10501v1)
- **发表日期**: 2026-06-09
- **匹配关键词**: vision-language-action model, vision-language-action, VLA
- **arXiv**: [2606.10501v1](http://arxiv.org/abs/2606.10501v1)
- **📥 PDF**: 已下载至本地 (`2606.10501v1_Uncovering_Vulnerability_of_Vision-Language-Action_Models_under_Joint-Level_Physical_Faults.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 在真实机器人系统中部署视觉-语言-动作（VLA）模型时，不仅需要应对语义和感知层面的变化，还需处理改变动作物理实现方式的机体侧故障。真实机器人可能因执行器退化、硬件故障、安全限制、碰撞损伤或磨损导致的摩擦而产生关节级变化。这些故障至关重要，因为它们会改变策略的动作-运动接口，破坏指令动作、实际运动与后续观测之间已习得的闭环关系。本研究针对真实的关节级物理故障展开分析，发现当预测动作通过受扰动的机器人机体执行时，VLA模型存在脆弱性。分析揭示了关节依赖性效应，不同受影响关节的任务成功率呈现异质性退化。研究同时表明，性能下降不能仅归因于物理不可行性——诸如关节摩擦增加这类可行故障仍会显著降低成功率，并引发闭环执行失配。基于这些发现，我们提出关节级物理故障感知残差校准器（J-PARC），这是一种基于冻结VLA策略构建的轻量级残差校准框架。J-PARC通过近期关节动力学推断潜在关节故障模式，并基于该模式调节共享残差校准器，从而实现对故障关节的自适应动作修正。实验表明，J-PARC在保持无故障环境性能的同时，显著提升了关节级故障下的鲁棒性。

---

### 8. Act on What You See: Unlocking Safe Social Navigation in Vision-Language-Action Models

- **作者**: Qingzi Wang, Xiyang Wu, Guangyao Shi, Dianwei Chen, Xianfeng Yang, Dinesh Manocha
- **单位**: University of Maryland; University of Maryland; University of Southern California...
- **发表日期**: 2026-06-09
- **匹配关键词**: navigation, vision-language-action model, VLA, social navigation, vision-language-action
- **arXiv**: [2606.10495v1](http://arxiv.org/abs/2606.10495v1)
- **📥 PDF**: 已下载至本地 (`2606.10495v1_Act_on_What_You_See_Unlocking_Safe_Social_Navigation_in_Vision-Language-Action_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 安全社交导航要求机器人能够区分行人与普通障碍物，并在危险发生前做出反应。研究表明，预训练的视觉-语言-动作（VLA）模型已在其内部表征中编码了行人-物体区分及未来碰撞信号，但行为克隆方法未能将这些信号转化为符合社交规范的动作。为解决这一不匹配问题，我们提出SALSA——一种两阶段无标注后训练框架：（1）社交行为对齐将中间层社交特征桥接到动作头，并通过反事实人-物场景对训练打破视觉显著性捷径；（2）时间安全对齐提供自动生成的未来风险监督，实现预期性碰撞规避。在SCAND数据集及真实场景部署中，SALSA将近碰撞事件减少86.4%，社交反事实准确率从53%提升至93%，表明通过引导VLA策略利用其已具备的表征采取行动，可实现更安全的社交导航。这些结果证明，通过更好地对齐潜在表征与动作生成，预训练VLA策略可被适配用于更安全的社交导航。

---

### 9. GuideWalk: Learning Unified Autonomous Navigation and Locomotion for Humanoid Robots across Versatile Terrains

- **作者**: Haoxuan Han, Chen Chen, Linao Gong, Xin Yang, Hao Hu, Junhong Guo, Zhicheng He, Yao Su, Fenghua He
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.10449v1)
- **发表日期**: 2026-06-09
- **匹配关键词**: exploration, autonomous navigation, navigation, obstacle avoidance
- **arXiv**: [2606.10449v1](http://arxiv.org/abs/2606.10449v1)
- **📥 PDF**: 已下载至本地 (`2606.10449v1_GuideWalk_Learning_Unified_Autonomous_Navigation_and_Locomotion_for_Humanoid_Robots_across_Versatile.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 人形机器人已具备强大的运动能力，但在复杂地形上的可靠导航仍具挑战性，因为避障必须与动态可行的运动相协调。本文提出GuideWalk——一个统一端到端框架，将可通行性感知导航引导与地形自适应运动教师模型相结合，用于人形机器人导航。具体而言，我们引入一个提供显式速度引导的导航模块，将避障与地形条件解耦，从而实现在多样化环境中的鲁棒规划。我们提出一种复合教师蒸馏方案，将目标导向指令与动态一致的动作进行聚合，并蒸馏至单一策略中。为进一步提升鲁棒性，蒸馏后的策略通过强化学习与辅助行为克隆目标进行优化，该目标在保留理想教师行为的同时促进探索。实验表明，GuideWalk在保持稳定人形运动的同时，实现了稳定有效的导航。

---

### 10. A Practical Recipe Towards Improving Sim-and-Real Correlation for VLA Evaluation

- **作者**: Shuo Wang, Hanyuan Xu, Yingdong Hu, Fanqi Lin, Yang Gao
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.10366v1)
- **发表日期**: 2026-06-09
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2606.10366v1](http://arxiv.org/abs/2606.10366v1)
- **📥 PDF**: 已下载至本地 (`2606.10366v1_A_Practical_Recipe_Towards_Improving_Sim-and-Real_Correlation_for_VLA_Evaluation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 仿真已成为评估和改进视觉-语言-动作（VLA）策略的重要工具，为成本高昂的真实机器人评估提供了可扩展、可重复且可控的替代方案。近期仿真基准在真实感和多样性方面取得了显著进展，但这些平台尚未被广泛视为可靠的真实世界策略评估代理。本研究从仿真与真实相关性角度探讨该问题，系统性地跨多个仿真平台、VLA策略、任务及扰动因素展开研究，通过策略排序一致性、性能相关性及扰动失效模式三个维度，衡量仿真评估能否保持真实世界的结论。该分析使我们能够刻画现有仿真器的局限性，并识别哪些仿真信号与真实部署更一致。我们进一步探究用户应如何利用仿真改进策略，包括基于仿真微调的适用条件，以及后训练数据量对仿真-真实对齐的影响。总体而言，本研究为衡量、解读和提升仿真对VLA策略的有效性提供了统一框架，既为仿真器设计者提供指导，也为将仿真纳入策略开发流程的实践者提供参考。

---

### 11. SARM2: Multi-Task Stage Aware Reward Modeling for Self Improving Robotic Manipulation

- **作者**: Qianzhong Chen, Hau Zheng, Justin Yu, Suning Huang, Jiankai Sun, Ken Goldberg, Chuan Wen, Pieter Abbeel, Yide Shentu, Philipp Wu, Mac Schwager
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.10305v1)
- **发表日期**: 2026-06-09
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2606.10305v1](http://arxiv.org/abs/2606.10305v1)
- **📥 PDF**: 已下载至本地 (`2606.10305v1_SARM2_Multi-Task_Stage_Aware_Reward_Modeling_for_Self_Improving_Robotic_Manipulation.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://qianzhong-chen.github.io/sarm2.github.io/.
- **中文摘要**: 针对长时程操控任务的视觉-语言-动作（VLA）策略微调仍严重依赖行为克隆，这既需要昂贵的高质量演示数据，又使策略局限于演示分布。奖励模型可通过重新加权演示数据并为机器人在线强化学习提供密集监督来降低这种依赖性，但此类模型需具备密集性、准确性和通用性。现有方法存在不足：任务特定的分阶段感知模型虽准确但需逐任务标注，而通用视觉语言模型（VLM）奖励模型虽适用范围广却因粒度粗糙难以捕捉细粒度长时程进展。我们提出RM——一种多任务分阶段感知奖励模型，通过结合基于动作基元的分阶段估计器与多门控专家混合（MMoE）价值头，为跨操控任务生成密集的逐步奖励。基于RM，我们进一步提出SPIRAL（通过奖励对齐学习实现自我策略改进）——一种基于策略的奖励引导框架，利用低成本自主轨迹数据改进VLA策略。在10项任务基准测试中，RM将价值估计均方误差较最强基线降低80%；当应用于SPIRAL框架时，该模型在短裤折叠任务（成功率从58%提升至100%）和白板清洁任务（从50%提升至90%）中将任务成功率从约50%提升至近乎完美表现，证明高质量密集奖励是构建稳定机器人数据飞轮的关键。项目网站：https://qianzhong-chen.github.io/sarm2.github.io/。

---

### 12. Locomotion analysis of a quadruped interacting with the lunar granular surface

- **作者**: Yash J Vyas
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.10273v1)
- **发表日期**: 2026-06-09
- **匹配关键词**: exploration
- **arXiv**: [2606.10273v1](http://arxiv.org/abs/2606.10273v1)
- **📥 PDF**: 已下载至本地 (`2606.10273v1_Locomotion_analysis_of_a_quadruped_interacting_with_the_lunar_granular_surface.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 在复杂地形交互、能量及热约束等多重挑战下，将腿足机器人部署于地外环境面临诸多难题。针对月球探测四足机器人的有效机械设计，需审慎考量电机扭矩、能量消耗及运输成本。月球表面由颗粒状风化层构成，这种特性直接影响腿足机器人的运动性能。基于刚性接触假设训练的运动算法在应用于颗粒表面等软接触环境时效果不佳，可能导致失稳与轨迹跟踪偏差。本报告将月球风化层-机器人足端接触的物理模型应用于强化学习训练的运动仿真环境，通过对比刚性接触与软接触环境下训练的策略，分析步态及运动性能指标。研究表明，模拟风化层表面的软接触为基于强化学习的训练带来额外挑战，不仅产生性质迥异的步态特征，更显著增加了整体能量消耗。

---

### 13. What Matters in Orchestrating Robot Policies: A Systematic Study of Hierarchical VLA Agents

- **作者**: Jiaheng Hu, Mohit Shridhar, Caden Lu, Dhruv Shah, Hao-Tien Lewis Chiang, Jie Tan, Annie Xie
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.10267v1)
- **发表日期**: 2026-06-09
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2606.10267v1](http://arxiv.org/abs/2606.10267v1)
- **📥 PDF**: 已下载至本地 (`2606.10267v1_What_Matters_in_Orchestrating_Robot_Policies_A_Systematic_Study_of_Hierarchical_VLA_Agents.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 层次化视觉-语言-动作（Hi-VLA）系统通过利用高层VLM规划器将任务分解为语言子目标，并由底层VLA控制器执行，已成为复杂机器人操作领域一种有前景的范式。尽管近期取得了实证进展，但此类系统仍缺乏统一的设计原则：现有Hi-VLA系统在规划器与控制器的选择与连接方式、两者间的切换机制，以及规划器中观测与记忆的表示方法上存在差异。本文针对机器人操作中的Hi-VLA设计开展了系统性研究。我们基于选项式控制框架统一了具有代表性的Hi-VLA智能体，并在短时域、长时域及推理密集型任务中基准测试了核心设计选择。通过分析，我们提炼出构建Hi-VLA系统的实用原则，揭示了模型选择与接口机制如何共同影响系统性能。在仿真实验和真实ALOHA机器人实验中，应用这些原则所构建的系统在性能上显著优于平面VLA控制或简单层次化设计。总体而言，我们的研究为构建更强大、更鲁棒且更具原则性的层次化VLA智能体奠定了基础。更多信息与视频请访问 jiahenghu.github.io/hi-vla。

---

### 14. Flow Control: Steering Vision-Language-Action Models with Simple Real-Time Inputs

- **作者**: Jonathan C. Kao, Jason Chan, Andy Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.10180v1)
- **发表日期**: 2026-06-08
- **匹配关键词**: vision-language-action model, vision-language-action, VLA
- **arXiv**: [2606.10180v1](http://arxiv.org/abs/2606.10180v1)
- **📥 PDF**: 已下载至本地 (`2606.10180v1_Flow_Control_Steering_Vision-Language-Action_Models_with_Simple_Real-Time_Inputs.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出了视觉-语言-动作（VLA）模型的流控制方法，这是一种通过通用输入（如键盘）实时引导VLA动作的简单有效方式。该方法可直接使用，无需重新训练或微调VLA模型。它允许相对粗糙的用户输入引导VLA与用户意图对齐。VLA将这些输入转化为从训练阶段习得的VLA专家动作分布中采样的动作样本，从而生成高质量（符合动作专家分布）且高保真度（反映用户意图）的动作。我们证明流控制具有多项理想特性：（1）流控制能准确且灵敏地通过用户输入引导机器人动作；（2）对次优用户输入具有鲁棒性；（3）使用户能够引导VLA实现显著更高的成功率和更快的任务完成速度；（4）在流控制轨迹上微调VLA可提升自主策略性能。综合来看，这些成果为用户提供了一种简单直观的VLA动作引导方式，从而提升任务表现。

---

### 15. GHOST: Hierarchical Sub-Goal Policies for Generalizing Robot Manipulation

- **作者**: Sriram Krishna, Ben Eisner, Haotian Zhan, Ying Yuan, Haoyu Zhen, Chuang Gan, Shubham Tulsiani, David Held
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.10025v1)
- **发表日期**: 2026-06-08
- **匹配关键词**: diffusion policy
- **arXiv**: [2606.10025v1](http://arxiv.org/abs/2606.10025v1)
- **📥 PDF**: 已下载至本地 (`2606.10025v1_GHOST_Hierarchical_Sub-Goal_Policies_for_Generalizing_Robot_Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出GHOST框架，一种用于学习超越训练分布的视觉运动操控策略的框架。GHOST将控制分解为：(i) 高层策略，从多视角RGB-D观测中预测三维末端执行器位姿的分布作为下一子目标；(ii) 低层目标条件控制器，执行具体具身动作。为了将基于图像的策略与三维目标条件关联，我们引入了一个简单的空间接口，将预测目标投影到图像平面，并将其表示为末端执行器热力图。在一系列操控任务中，这种分层分解相比扁平化的扩散策略持续提升了性能与鲁棒性。此外，我们证明这种分层接口还能轻松融入人类演示，无需依赖（含噪声的）动作重定向。由于子目标在很大程度上与具身形态无关，我们利用人类视频训练高层策略以指定学习技能的应用与组合方式，同时保持低层策略仅基于机器人数据训练。这种层级结构使得仅需少量人类演示即可适应新物体和任务变化。

---

### 16. MemoryVLA++: Temporal Modeling via Memory and Imagination in Vision-Language-Action Models

- **作者**: Hao Shi, Weiye Li, Bin Xie, Yulin Wang, Renping Zhou, Tiancai Wang, Xiangyu Zhang, Ping Luo, Gao Huang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.09827v1)
- **发表日期**: 2026-06-08
- **匹配关键词**: vision-language-action model, vision-language-action, VLA
- **arXiv**: [2606.09827v1](http://arxiv.org/abs/2606.09827v1)
- **📥 PDF**: 已下载至本地 (`2606.09827v1_MemoryVLA++_Temporal_Modeling_via_Memory_and_Imagination_in_Vision-Language-Action_Models.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://shihao1895.github.io/MemoryVLA-PP-Web
- **中文摘要**: 时间建模对于机器人操作至关重要，因为有效控制既需要记忆过去的交互，也需要想象未来的状态。然而，大多数视觉-语言-动作（VLA）模型主要依赖当前观测，因此在长时域、时间依赖型任务中表现不佳。认知科学表明，人类依赖工作记忆缓冲短期上下文，依赖海马系统保存过去经历的情景记忆，并依赖内部模型想象未来可能的状态演化。受这些机制启发，我们提出MemoryVLA++，一个完整的时间建模框架，为VLA模型赋予记忆与想象能力以支持机器人操作。预训练的视觉-语言模型（VLM）将当前观测编码为感知与认知令牌，形成工作记忆。这些令牌查询感知-认知记忆库以检索相关历史上下文。该记忆库存储来自过去交互的低层细节与高层语义，并通过冗余感知整合进行更新。一个世界模型在去噪潜在空间中想象未来状态，并在记忆引导下整合这些想象潜在表示，形成完整的时间感知令牌。最终令牌条件化一个扩散动作专家，以预测时间一致的动作序列。我们在5个仿真基准测试和3类真实机器人任务（涵盖3种机器人）上进行了广泛实验，覆盖通用操作、长时域时间任务、鲁棒性与泛化能力。我们的方法在Libero、SimplerEnv、Mikasa-Robo、Calvin、Libero-Plus以及多种真实机器人任务上均取得强劲性能，验证了结合记忆与想象的完整时间建模的有效性。例如，在真实机器人上，该方法在通用任务、记忆依赖任务和想象依赖任务上分别获得+9%、+26%和+28%的性能提升。项目页面：https://shihao1895.github.io/MemoryVLA-PP-Web

---

### 17. Earth-OneVision: Extending Remote Sensing Multimodal Large Language Models to More Sensor Modalities and Tasks

- **作者**: Miaoxin Cai, Guanqun Wang, Wei Zhang, Guangyao Zhou, Yin Zhuang, Tong Zhang, Hao Wang, He Chen, Jun Li
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.10819v1)
- **发表日期**: 2026-06-09
- **匹配关键词**: VLA
- **arXiv**: [2606.10819v1](http://arxiv.org/abs/2606.10819v1)
- **📥 PDF**: 已下载至本地 (`2606.10819v1_Earth-OneVision_Extending_Remote_Sensing_Multimodal_Large_Language_Models_to_More_Sensor_Modalities_.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: RS-MLLMs能够实现对地球观测影像的自然语言理解与空间推理。然而，现有模型仅支持有限的传感器类型和任务，导致对地球的认知呈现碎片化，且跨模态地球科学知识尚未得到充分利用。本文提出Earth-OneVision，一个2B参数的RS-MLLM，在单一自回归框架内统一了六种传感器模态（即光学、SAR、红外、多光谱、时序和视频）以及跨9个任务类别的跨传感器融合。三个专用机制解决了三个瓶颈：全粒度视觉-语言对齐（FGVLA）将多层级视觉特征与多维语言空间对齐；空间-语言同构序列化（SLIS）将异构空间输出统一为自回归标记；渐进式跨模态适应（PCMA）将复合领域差距分解为顺序阶段，依次解决视角和成像物理差距。为支持联合训练，构建了MMRS-OneVision数据集，包含约3400万QA对，覆盖全部六种传感器模态及跨9个任务类别的跨传感器融合，规模远超现有遥感多模态指令数据集。仅凭2B参数，Earth-OneVision在广泛基准测试中取得具有竞争力或最优的结果，持续匹配或超越4B-72B的RS-MLLMs。其在光学视觉定位任务OPT-RSVG测试集上达到87.52%的P@0.5，在SAR VQA基准SARLANG-Bench上达到80.68%，超过7B模型7%以上；在多光谱分类任务BigEarthNet-MS测试集上实现75.74%的召回率，在跨模态推理基准EarthMind-Bench上达到81.94%的多选题准确率。

---

### 18. LIBERO-Occ: Evaluating and Improving Vision-Language-Action Models under Scene-Induced Occlusion via Viewpoint Imagination

- **作者**: Taishan Li, Jiwen Zhang, Siyuan Wang, Xuanjing Huang, Zhongyu Wei
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.10862v1)
- **发表日期**: 2026-06-09
- **匹配关键词**: vision-language-action model, vision-language-action, VLA
- **arXiv**: [2606.10862v1](http://arxiv.org/abs/2606.10862v1)
- **📥 PDF**: 已下载至本地 (`2606.10862v1_LIBERO-Occ_Evaluating_and_Improving_Vision-Language-Action_Models_under_Scene-Induced_Occlusion_via_.pdf`)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/litsh/Libero-Occ, https://github.com/litsh/Libero-Occ
- **中文摘要**: 视觉-语言-动作（VLA）模型在标准操作基准测试中表现出色，但大多数评估假设任务相关物体完全可见。这一假设在现实场景中往往不成立——遮挡使得操作过程仅能部分观测。本文研究作为VLA模型根本性挑战的**场景诱导遮挡**，并引入LIBERO的遮挡扩展版本**LIBERO-Occ**。实验表明，当前最先进的VLA模型在遮挡条件下性能显著下降。为解决该问题，我们提出**视点想象（VIM）**方法，该方法从被遮挡的主视角观测生成互补视角，并基于观测与想象的双重证据进行动作预测。VIM在无需部署额外摄像头的情况下，提升了模型在不同任务套件、遮挡类型及严重程度下的鲁棒性，表明视点想象是部分可观测操作中感知补全的有效机制。我们的基准测试及对应代码已开源：\href{https://github.com/litsh/Libero-Occ}{https://github.com/litsh/Libero-Occ}。

---

### 19. AgenticNav: Zero-Shot Vision-and-Language Navigation as a Tool-Calling Harness

- **作者**: Yijian Li, Changze Li, Hantian Shi, Jiaying Luo, Jiyuan Cai, Ming Yang, Tong Qin
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.10577v1)
- **发表日期**: 2026-06-09
- **匹配关键词**: navigation, vision-and-language navigation, VLN
- **arXiv**: [2606.10577v1](http://arxiv.org/abs/2606.10577v1)
- **📥 PDF**: 已下载至本地 (`2606.10577v1_AgenticNav_Zero-Shot_Vision-and-Language_Navigation_as_a_Tool-Calling_Harness.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 连续环境中的零样本视觉与语言导航（VLN-CE）近期随着大型视觉语言模型（VLM）的发展变得可行。然而，现有方法通常依赖学习得到的航点预测器来提出可导航动作，这严重限制了模型的动作空间，且未能有效利用深度输入。此外，记忆处理通常通过累积包含大量无关上下文的长文本或视觉历史记录，或通过检索跨场景经验来实现，这削弱了零样本设置的有效性。本文重新将零样本VLN-CE定义为VLM与环境之间的智能体接口，并提出AgenticNav——一种轻量级导航框架，将动作、深度和记忆作为可调用工具暴露给模型。动作工具允许VLM直接从RGB观测中选择目标像素，并将其转换为可执行运动，而非从预测航点中选取。深度通过按需像素深度工具暴露，使VLM仅在关键位置请求精确的度量距离。在记忆方面，AgenticNav提供紧凑的地图图像来总结历史轨迹，并配合召回工具使VLM能够选择性回顾过去的视觉观测，而不会过度占用提示上下文。在R2R-CE基准测试中，AgenticNav在相同VLM骨干网络下，于零样本方法中取得了新的最优性能（SOTA）。真实世界验证进一步凸显了其相比先前方法的零样本泛化能力。消融实验表明，我们的动作工具设计优于传统航点预测器，而深度工具与智能体记忆进一步提升了导航性能。

---

### 20. Envision4D: Envisioning Visual Futures via Feed-forward 4D Gaussian Splatting for Autonomous Driving

- **作者**: Qi Song, Yifei He, Chi Zhang, Zheng Fu, Xuhe Zhao, Mengmeng Yang, Kun Jiang, Rui Huang, Diange Yang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.10656v1)
- **发表日期**: 2026-06-09
- **匹配关键词**: gaussian splatting
- **arXiv**: [2606.10656v1](http://arxiv.org/abs/2606.10656v1)
- **📥 PDF**: 已下载至本地 (`2606.10656v1_Envision4D_Envisioning_Visual_Futures_via_Feed-forward_4D_Gaussian_Splatting_for_Autonomous_Driving.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 预测动态场景的未来演化对自动驾驶至关重要。然而，现有前馈范式主要针对插值任务设计。当扩展至未来外推时，这些方法在大位移场景下会产生鬼影伪影，且受限于简化的运动假设或严格的未来先验。为应对这些挑战，我们提出Envision4D——一种完全自监督的前馈框架，用于无位姿约束的未来外推。具体而言，我们引入未来位姿预测模块，通过迭代去噪过程推断未来相机参数。此外，为捕捉非线性动态，我们提出层内时序注意力机制，并采用条件运动提升方法，将高度不确定的外推过程转化为稳健的关系映射。最后，采用渐进式训练策略来稳定无监督运动学习，防止误差累积。大量实验表明，Envision4D实现了最优性能，在未来视角合成任务中显著超越现有方法。

---

