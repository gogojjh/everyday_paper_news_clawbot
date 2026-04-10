# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-04-10 08:03

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 3/20 篇提供

**🌟 Highlight**: 10 篇 | **📌 Poster**: 10 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. Mem3R: Streaming 3D Reconstruction with Hybrid Memory via Test-Time Training

- **作者**: Changkun Liu, Jiezhi Yang, Zeman Li, Yuan Deng, Jiancong Guo, Luca Ballan
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.07279v1)
- **发表日期**: 2026-04-08
- **匹配关键词**: 3d reconstruction, 3D reconstruction
- **arXiv**: [2604.07279v1](http://arxiv.org/abs/2604.07279v1)
- **📥 PDF**: 已下载至本地 (`2604.07279v1_Mem3R_Streaming_3D_Reconstruction_with_Hybrid_Memory_via_Test-Time_Training.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://lck666666.github.io/Mem3R/
- **中文摘要**: 流式三维感知技术特别适用于机器人和增强现实领域，这些场景需要高效且连贯地处理长时视觉流。近期出现的循环模型通过维持固定大小的状态并实现线性时间推理，提供了有前景的解决方案，但由于压缩潜在记忆的容量有限，这些模型在长序列中常面临漂移累积和时间遗忘问题。我们提出Mem3R——一种采用混合记忆设计的流式三维重建模型，通过将相机跟踪与几何映射解耦来提升长序列的时间一致性。在相机跟踪方面，Mem3R采用由轻量级多层感知机实现的隐式快速权重记忆，并通过测试时训练进行更新。在几何映射方面，Mem3R维持基于令牌的显式固定大小状态。与CUT3R相比，该设计不仅显著提升了长序列性能，还将模型参数量从7.93亿减少至6.44亿。Mem3R兼容为CUT3R开发的现有即插即用状态更新策略，特别是与TTT3R集成后，在500至1000帧序列上可将绝对轨迹误差较基础实现降低达39%。这些改进同样延伸至其他下游任务，包括视频深度估计和三维重建，同时保持恒定的GPU内存使用量和相当的推理吞吐量。项目页面：https://lck666666.github.io/Mem3R/

---

### 2. RichMap: A Reachability Map Balancing Precision, Efficiency, and Flexibility for Rich Robot Manipulation Tasks

- **作者**: Yupu Lu, Yuxiang Ma, Jia Pan
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.06778v1)
- **发表日期**: 2026-04-08
- **匹配关键词**: diffusion policy
- **arXiv**: [2604.06778v1](http://arxiv.org/abs/2604.06778v1)
- **📥 PDF**: 已下载至本地 (`2604.06778v1_RichMap_A_Reachability_Map_Balancing_Precision,_Efficiency,_and_Flexibility_for_Rich_Robot_Manipulat.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 本文提出RichMap，一种高精度可达性地图表示方法，旨在为多样化机器人操作任务平衡效率与灵活性。通过优化经典的网格化结构，我们提出一种精简方法，在保持结构灵活性的同时，其性能接近紧凑型地图形式（如RM4D）。该方法利用$\mathbb{S}^2$（或$SO(3)$）的理论容量边界确保严格覆盖，并采用异步流水线实现高效构建。我们通过综合指标验证地图性能，追求高预测准确率（$>98\%$）、低误报率（$1\sim2\%$）与快速批量查询能力（$\sim$15 $μ$s/查询）。我们将框架应用扩展至通过最大均值差异（MMD）度量量化机器人工作空间相似性，并展示基于能量的扩散策略迁移引导方法，在方块推动实验中实现跨实体场景最高达$26\%$的性能提升。

---

### 3. Designing Privacy-Preserving Visual Perception for Robot Navigation Based on User Privacy Preferences

- **作者**: Xuying Huang, Sicong Pan, Delphine Reinhardt, Maren Bennewitz
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.06382v1)
- **发表日期**: 2026-04-07
- **匹配关键词**: robot navigation, navigation, visual navigation
- **arXiv**: [2604.06382v1](http://arxiv.org/abs/2604.06382v1)
- **📥 PDF**: 已下载至本地 (`2604.06382v1_Designing_Privacy-Preserving_Visual_Perception_for_Robot_Navigation_Based_on_User_Privacy_Preference.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉导航是移动服务机器人的一项基本能力，然而实现此类导航所需搭载的摄像头可能采集涉及隐私的敏感信息，引发用户对隐私保护的担忧。现有面向隐私保护的导航视觉感知方法多从技术角度出发，较少基于用户隐私偏好进行设计。本研究提出一种以用户为中心的设计方法，用于开发机器人导航中的隐私保护视觉感知系统。为探究用户隐私偏好如何指导此类设计，我们开展了两项用户调研。结果显示：用户更倾向于采用隐私保护型视觉抽象化处理及采集端低分辨率保护机制；其偏好的RGB分辨率既取决于期望的隐私保护等级，也与导航过程中机器人的接近程度相关。基于这些发现，我们进一步推导出适用于隐私保护型机器人视觉导航的用户可配置距离-分辨率隐私策略。

---

### 4. BiCoord: A Bimanual Manipulation Benchmark towards Long-Horizon Spatial-Temporal Coordination

- **作者**: Xingyu Peng, Chen Gao, Liankai Jin, Annan Li, Si Liu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.05831v1)
- **发表日期**: 2026-04-07
- **匹配关键词**: bimanual manipulation, VLA
- **arXiv**: [2604.05831v1](http://arxiv.org/abs/2604.05831v1)
- **📥 PDF**: 已下载至本地 (`2604.05831v1_BiCoord_A_Bimanual_Manipulation_Benchmark_towards_Long-Horizon_Spatial-Temporal_Coordination.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 双手操作，即协调使用两个机械臂完成任务，对实现机器人领域人类水平的灵巧性至关重要。近期仿真基准（如RoboTwin和RLBench2）推动了数据驱动的双手操作学习研究。然而，现有任务多为短时程且协调松散，未能捕捉现实世界中双手行为固有的时空耦合特性。为填补这一空白，我们提出了BiCoord——一个面向长时程紧密协调双手操作的基准测试平台。该平台包含多种需要持续臂间依赖性和跨多子目标动态角色交换的任务。同时，我们设计了一套从时间、空间及时空维度评估协调性的量化指标，实现了对双手协作的系统化度量。实验结果表明，代表性操作策略（如DP、RDT、Pi0和OpenVLA-OFT）在长时程高度耦合任务中表现欠佳，揭示了实现长时程紧密协调任务面临的根本性挑战。我们期待BiCoord能为长时程协作操作研究奠定基础，并启发未来面向协调感知的机器人学习研究。所有数据集、代码及补充材料可通过https://buaa-colalab.github.io/BiCoord/获取。

---

### 5. Rectified Schrödinger Bridge Matching for Few-Step Visual Navigation

- **作者**: Wuyang Luan, Junhui Li, Weiguang Zhao, Wenjian Zhang, Tieru Wu, Rui Ma
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.05673v1)
- **发表日期**: 2026-04-07
- **匹配关键词**: navigation, visual navigation
- **arXiv**: [2604.05673v1](http://arxiv.org/abs/2604.05673v1)
- **📥 PDF**: 已下载至本地 (`2604.05673v1_Rectified_Schrödinger_Bridge_Matching_for_Few-Step_Visual_Navigation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉导航是具身人工智能的核心挑战，要求自主智能体将高维感知观测转化为连续、长程的动作轨迹。虽然基于扩散模型和薛定谔桥的生成策略能有效捕捉多模态动作分布，但由于高方差随机传输特性，它们需要数十个积分步骤，这对实时机器人控制构成了关键障碍。我们提出修正型薛定谔桥匹配框架，该框架利用标准薛定谔桥（$\varepsilon=1$，最大熵传输）与确定性最优传输（$\varepsilon\to 0$，如条件流匹配）之间共享的速度场结构，通过单一熵正则化参数$\varepsilon$进行调控。我们证明了两项关键结论：（1）条件速度场的函数形式在整个$\varepsilon$谱系中保持不变（速度结构不变性），使得单一网络可适用于所有正则化强度；（2）降低$\varepsilon$值能线性减少条件速度方差，从而实现更稳定的粗步长常微分方程积分。通过锚定于缩短传输距离的学习型条件先验，RSBM在中等$\varepsilon$值下运行，平衡了多模态覆盖与路径平直度。实验表明，标准桥方法需要$\geq 10$步才能收敛，而RSBM仅用3个积分步骤就实现了超过94%的余弦相似度和92%的成功率——无需蒸馏或多阶段训练——显著缩小了高保真生成策略与具身人工智能低延迟需求之间的差距。

---

### 6. A1: A Fully Transparent Open-Source, Adaptive and Efficient Truncated Vision-Language-Action Model

- **作者**: Kaidong Zhang, Jian Zhang, Rongtao Xu, Yu Sun, Shuoshuo Xue, Youpeng Wen, Xiaoyu Guo, Minghao Guo, Weijia Liufu, Liu Zihou, Kangyi Ji, Yangsong Zhang, Jiarun Zhu, Jingzhi Liu, Zihang Li, Ruiyi Chen, Meng Cao, Jingming Zhang, Shen Zhao, Xiaojun Chang, Feng Zheng, Ivan Laptev, Xiaodan Liang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.05672v2)
- **发表日期**: 2026-04-07
- **匹配关键词**: VLA, vision-language-action, vision-language-action model, affordance
- **arXiv**: [2604.05672v2](http://arxiv.org/abs/2604.05672v2)
- **📥 PDF**: 已下载至本地 (`2604.05672v2_A1_A_Fully_Transparent_Open-Source,_Adaptive_and_Efficient_Truncated_Vision-Language-Action_Model.pdf`)
- **🔓 开源**: CODE
- **中文摘要**: 视觉-语言-动作（VLA）模型已成为开放世界机器人操作的重要范式，但其实际部署常受成本限制：十亿级参数的视觉语言模型主干与基于迭代扩散/流的动作生成模块会带来高延迟与计算负担，导致在通用硬件上实现实时控制的成本高昂。我们提出A1框架——一个完全开源透明的VLA系统，旨在实现低成本、高吞吐量的推理，同时保持操作成功率。该方法利用预训练的视觉语言模型为动作生成提供隐式功能先验。我们完整开源训练体系（训练代码、数据及处理流程、中间检查点与评估脚本），确保端到端的可复现性。A1不仅优化视觉语言模型，更通过引入预算感知的自适应推理机制协同加速主干网络与动作生成模块：通过监控中间层动作一致性实现早期终止，并提出跨层截断流匹配方法，在层间预热去噪过程，从而以显著更少的有效去噪迭代生成精确动作。在仿真基准测试（LIBERO、VLABench）与实体机器人（Franka、AgiBot）实验中，A1在保持最优成功率的同时大幅降低推理成本（流匹配推理单回合延迟降低最高达72%，主干计算量减少最高达76.6%且性能损失微小）。在RoboChallenge测试中，A1以29.00%的平均成功率超越基线模型，包括pi0（28.33%）、X-VLA（21.33%）和RDT-1B（15.00%）。

---

### 7. SnapFlow: One-Step Action Generation for Flow-Matching VLAs via Progressive Self-Distillation

- **作者**: Wuyang Luan, Junhui Li, Weiguang Zhao, Wenjian Zhang, Tieru Wu, Rui Ma
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.05656v1)
- **发表日期**: 2026-04-07
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2604.05656v1](http://arxiv.org/abs/2604.05656v1)
- **📥 PDF**: 已下载至本地 (`2604.05656v1_SnapFlow_One-Step_Action_Generation_for_Flow-Matching_VLAs_via_Progressive_Self-Distillation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 基于流匹配的视觉-语言-动作模型（如pi0、pi0.5和SmolVLA）在通用机器人操作领域已达到最先进水平，但其迭代去噪过程（通常需10步ODE计算）会带来显著延迟：在现代GPU上，仅去噪步骤就占端到端推理时间的80%。若简单减少步数会导致不可靠结果——由于速度场未针对单步跳跃进行校准，多数任务成功率会下降。我们提出SnapFlow，一种即插即用的自蒸馏方法，可将流匹配VLA模型的多步去噪压缩为单次前向传播（1-NFE）。该方法混合标准流匹配样本与一致性样本，后者的目标值通过模型自身边缘速度预测计算出的两步欧拉捷径速度生成，从理论上避免了条件速度引起的轨迹漂移问题。通过零初始化目标时间嵌入技术，网络可在单一架构内切换局部速度估计与全局单步生成模式。SnapFlow无需外部教师模型、不改变网络架构，在单GPU上仅需约12小时训练。我们在参数规模相差6倍的两种VLA架构上使用相同超参数进行验证：对于pi0.5（30亿参数）在四个LIBERO测试集（40项任务、400个场景）中，SnapFlow平均成功率高达98.75%——与10步教师模型的97.75%持平并略有超越——同时去噪速度提升9.6倍，端到端延迟从274毫秒降至83毫秒；在SmolVLA（5亿参数）上，该方法在实现3.56倍端到端加速的同时将均方误差降低8.3%。针对长时序任务的行动步数扫描实验表明，SnapFlow在不同执行时域均保持优势：当n_act=5时达到93%成功率，而基线模型仅达90%。该方法与层蒸馏及令牌剪枝技术正交，可实现组合式加速效果。

---

### 8. FunRec: Reconstructing Functional 3D Scenes from Egocentric Interaction Videos

- **作者**: Alexandros Delitzas, Chenyangguang Zhang, Alexey Gavryushin, Tommaso Di Mario, Boyang Sun, Rishabh Dabral, Leonidas Guibas, Christian Theobalt, Marc Pollefeys, Francis Engelmann, Daniel Barath ⭐
  - **高亮作者**: Marc Pollefeys
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.05621v1)
- **发表日期**: 2026-04-07
- **匹配关键词**: affordance
- **arXiv**: [2604.05621v1](http://arxiv.org/abs/2604.05621v1)
- **📥 PDF**: 已下载至本地 (`2604.05621v1_FunRec_Reconstructing_Functional_3D_Scenes_from_Egocentric_Interaction_Videos.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出FunRec方法，该方法能够直接从第一人称视角的RGB-D交互视频中重建室内场景的功能性三维数字孪生。与现有依赖受控环境、多状态采集或CAD先验知识的关节重建方法不同，FunRec直接基于真实世界的人类交互序列进行可交互三维场景重建。该方法能自动发现关节部件，估算其运动学参数，追踪三维运动轨迹，并在规范空间中重建静态与动态几何结构，最终生成兼容仿真模拟的网格模型。在全新构建的真实与模拟基准测试中，FunRec以前所未有的优势超越现有方法：部件分割任务中mIoU指标提升高达50%，关节与姿态误差降低5-10倍，重建精度显著提高。我们进一步展示了该方法在仿真系统URDF/USD导出、手部引导的功用映射以及机器人-场景交互等领域的应用潜力。

---

### 9. Grounding Hierarchical Vision-Language-Action Models Through Explicit Language-Action Alignment

- **作者**: Theodor Wulff, Federico Tavella, Rahul Singh Maharjan, Manith Adikari, Angelo Cangelosi
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.05614v1)
- **发表日期**: 2026-04-07
- **匹配关键词**: VLA, vision-language-action, vision-language-action model, human-robot collaboration
- **arXiv**: [2604.05614v1](http://arxiv.org/abs/2604.05614v1)
- **📥 PDF**: 已下载至本地 (`2604.05614v1_Grounding_Hierarchical_Vision-Language-Action_Models_Through_Explicit_Language-Action_Alignment.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 实现机器人透明度是迈向有效人机协作的关键一步。为达到透明化，机器人的自然语言交流必须与其行为保持一致，并明确植根于任务与环境之中。现有的分层视觉-语言-动作模型能够生成语言描述（例如通过思维链）并执行底层动作，但当前研究未在训练过程中考虑这些模态间的显式对齐。为填补这一关键空白，我们提出了一种新颖的训练框架，该框架将分层视觉-语言-动作模型的子任务描述显式地锚定在视觉观察与动作空间中。我们的框架采用对比模型来评估生成语言与对应动作轨迹之间的对齐程度，通过直接对不同语言-轨迹配对进行对齐度排序，使我们能够通过离线偏好学习优化分层视觉-语言-动作模型的语义锚定。我们将该框架应用于LanguageTable数据集——一个包含人类语言标注轨迹的基准数据集，在建立强大基准模型的同时，为多模态锚定表征提供了关键洞见。该模型实现了与全监督微调相当的性能，同时最大程度减少了对高成本数据标注的需求。

---

### 10. Uncovering Linguistic Fragility in Vision-Language-Action Models via Diversity-Aware Red Teaming

- **作者**: Baoshun Tong, Haoran He, Ling Pan, Yang Liu, Liang Lin
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.05595v1)
- **发表日期**: 2026-04-07
- **匹配关键词**: VLA, vision-language-action, vision-language-action model
- **arXiv**: [2604.05595v1](http://arxiv.org/abs/2604.05595v1)
- **📥 PDF**: 已下载至本地 (`2604.05595v1_Uncovering_Linguistic_Fragility_in_Vision-Language-Action_Models_via_Diversity-Aware_Red_Teaming.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型在机器人操作领域取得了显著成功。然而，其对语言细微差异的鲁棒性仍是一个关键且尚未深入探索的安全问题，给实际部署带来了重大安全风险。红队测试（即识别可能引发灾难性行为的环境场景）是确保具身人工智能代理安全部署的重要环节。强化学习（RL）已成为自动化红队测试中一种有前景的方法，旨在揭示这些潜在漏洞。然而，基于强化学习的标准对抗方法因其奖励最大化的特性，常陷入严重的模式坍塌问题——倾向于收敛到一组狭窄的、琐碎或重复的故障模式，无法全面揭示有意义的风险图景。为弥补这一不足，我们提出了一种新颖的**多样性感知具身红队测试框架**，旨在暴露VLA模型面对语言变异的脆弱性。该框架基于对统一策略的评估，能够生成多样化的挑战性指令，同时通过物理模拟器中的执行失败率来确保攻击有效性。我们在多个机器人基准测试中，针对包括$π_0$和OpenVLA在内的两种先进VLA模型进行了广泛实验。结果表明，我们的方法能持续发现更广泛且更有效的对抗性指令，将平均任务成功率从93.33%降至5.85%，这为压力测试VLA代理提供了一种可扩展的方法，有助于在实际部署前暴露关键的安全盲点。

---

## 📌 Poster

*其他相关研究*

---

### 1. TAMEn: Tactile-Aware Manipulation Engine for Closed-Loop Data Collection in Contact-Rich Tasks

- **作者**: Longyan Wu, Jieji Ren, Chenghang Jiang, Junxi Zhou, Shijia Peng, Ran Huang, Guoying Gu, Li Chen, Hongyang Li
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.07335v1)
- **发表日期**: 2026-04-08
- **匹配关键词**: bimanual manipulation
- **arXiv**: [2604.07335v1](http://arxiv.org/abs/2604.07335v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: CODE
- **中文摘要**: 手持式采集范式为机器人操作的大规模演示数据收集提供了高效直观的途径。然而，通过此类方法实现接触密集型的双手操作仍面临关键挑战，硬件适应性与数据有效性成为主要制约因素。现有硬件设计多局限于特定夹爪结构，且常在追踪精度与便携性之间难以兼顾。此外，演示过程中缺乏在线可行性校验导致动作复现性较差。更重要的是，当前手持式系统难以在机器人执行过程中采集交互式纠偏数据，缺乏鲁棒策略优化所需的真实触觉信息。为突破这些局限，我们提出触觉感知操作引擎TAMEn，实现接触密集型任务的闭环数据采集。该系统采用跨形态可穿戴接口设计，可快速适配异构夹爪。为平衡数据质量与环境多样性，我们构建了双模态采集流程：精度模式借助动作捕捉技术实现高保真演示，便携模式则利用基于VR的追踪技术实现野外环境采集与触觉可视化纠偏遥操作。基于此硬件平台，我们将大规模触觉预训练、任务特异性双手演示以及人机协同纠偏数据整合为金字塔结构的数据体系，实现闭环策略优化。实验表明，我们的可行性感知流程显著提升了演示动作复现率，所提出的视觉-触觉学习框架将多种双手操作任务的成功率从34%提升至75%。我们同步开源硬件方案与数据集，以促进研究可复现性并推动视觉-触觉操作领域的发展。

---

### 2. Robust Quadruped Locomotion via Evolutionary Reinforcement Learning

- **作者**: Brian McAteer, Karl Mason
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.07224v1)
- **发表日期**: 2026-04-08
- **匹配关键词**: exploration
- **arXiv**: [2604.07224v1](http://arxiv.org/abs/2604.07224v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 深度强化学习在四足机器人运动控制领域近期取得显著进展，但仿真环境中训练的策略在环境变化时往往难以迁移。进化强化学习通过将基于梯度的策略优化与群体驱动探索相结合，旨在突破这一局限。本研究在模拟行走任务中评估了四种方法：DDPG、TD3以及两种基于交叉熵的变体CEM-DDPG和CEM-TD3。所有智能体均在平坦地形训练，随后在训练地形和未接触过的崎岖地形进行测试。在平坦地面测试中，TD3在标准深度强化学习基线方法中表现最佳，平均奖励达5927.26；而CEM-TD3在训练与评估阶段获得最高综合奖励17611.41。在崎岖地形迁移测试中，深度强化学习方法性能急剧下降：DDPG获得-1016.32奖励，TD3获得-99.73奖励，而进化变体则保持了大部分性能。CEM-TD3以19574.33的平均奖励记录展现出最强的迁移能力。这些发现表明，融入进化搜索能有效减少运动控制任务中的过拟合现象，提升策略鲁棒性，尤其在部署环境与训练条件存在差异时效果更为显著。

---

### 3. Flow Motion Policy: Manipulator Motion Planning with Flow Matching Models

- **作者**: Davood Soleymanzadeh, Xiao Liang, Minghui Zheng
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.07084v1)
- **发表日期**: 2026-04-08
- **匹配关键词**: motion planning
- **arXiv**: [2604.07084v1](http://arxiv.org/abs/2604.07084v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 开环端到端神经运动规划器近期被提出，用于改进机器人机械臂的运动规划。这些方法能够直接从传感器观测进行规划，无需在规划过程中依赖特权碰撞检测器。然而，现有方法在多次运行中通常仅为给定工作空间生成单一轨迹，且未能利用其开环结构进行推理时优化。为突破这一局限，我们提出流运动策略——一种面向机器人机械臂的开环端到端神经运动规划器，该方法通过流匹配技术的随机生成框架捕捉规划数据固有的多模态特性。通过对可行路径分布进行建模，流运动策略实现了高效的推理时N选优采样。该方法可生成多条端到端候选路径，在规划后评估其碰撞状态，并执行首个无碰撞解。我们将流运动策略与代表性采样基及神经运动规划方法进行基准测试。评估结果表明，流运动策略显著提升了规划成功率与效率，验证了随机生成策略在端到端运动规划及推理时优化中的有效性。实验评估视频可通过此\href{https://zh.engr.tamu.edu/wp-content/uploads/sites/310/2026/03/FMP-Website.mp4}{链接}观看。

---

### 4. Auditing Demographic Bias in Facial Landmark Detection for Fair Human-Robot Interaction

- **作者**: Pablo Parte, Roberto Valle, José M. Buenaposada, Luis Baumela
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.06961v1)
- **发表日期**: 2026-04-08
- **匹配关键词**: human-robot interaction, HRI
- **arXiv**: [2604.06961v1](http://arxiv.org/abs/2604.06961v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 人机交互中的公平性关键取决于使机器人能够解读人类行为的感知模型的可靠性。尽管人口统计学偏见在高级面部分析任务中已被广泛研究，但其在面部关键点检测中的存在尚未得到探索。本文对该任务中的人口统计学偏见进行了系统性审查，分析了年龄、性别和种族偏见。为此，我们引入了一种受控统计方法，以将人口统计学效应与混淆视觉因素区分开来。对标准代表性模型的评估表明，混淆视觉因素——特别是头部姿态和图像分辨率——的影响远超人口统计学属性。值得注意的是，在考虑这些混淆因素后，我们发现跨性别和种族的性能差异消失。然而，我们识别出统计学上显著的年龄相关效应，对年长个体观察到更高的偏见。这表明公平性问题甚至可能在低级视觉组件中出现，并可能通过人机交互流程传播，对弱势群体造成不成比例的影响。我们认为，审查并纠正此类偏见是构建可信且公平的机器人感知系统的必要步骤。

---

### 5. Exploiting Aggregate Programming in a Multi-Robot Service Prototype

- **作者**: Giorgio Audrito, Andrea Basso, Daniele Bortoluzzi, Ferruccio Damiani, Giordano Scarso, Gianluca Torta
- **单位**: Dipartimento di Informatica, Universita' di Torino; MITO Technology; Dipartimento di Informatica, Universita' di Torino...
- **发表日期**: 2026-04-08
- **匹配关键词**: exploration
- **arXiv**: [2604.06876v1](http://arxiv.org/abs/2604.06876v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 多机器人系统在医疗、勘探及救援任务等多样化应用领域中正变得日益重要。然而，构建此类系统仍面临重大挑战，因为它不仅需要协调分布式（多智能体）系统固有的复杂性，还需应对机器人物理特性及其所处环境带来的额外难题。近年来，聚合编程作为一种基于邻近通信的弹性分布式系统工程方法崭露头角，并已获得多个实用框架的有力支持。本文提出了一种多机器人服务系统的原型设计，该原型采用聚合编程方法进行协调软件的设计与实现。该原型已通过仿真实验及大学图书馆的实际测试得到验证。

---

### 6. Train-Small Deploy-Large: Leveraging Diffusion-Based Multi-Robot Planning

- **作者**: Siddharth Singh, Soumee Guha, Qing Chang, Scott Acton
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.06598v1)
- **发表日期**: 2026-04-08
- **匹配关键词**: path planning
- **arXiv**: [2604.06598v1](http://arxiv.org/abs/2604.06598v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 基于学习的多机器人路径规划方法在扩展或适应变化方面存在困难，特别是在部署过程中机器人数量发生变化时。现有方法大多针对固定数量的机器人进行训练，在测试时或许能容忍数量减少，但当数量增加时通常无法有效应对。此外，为更多智能体训练此类方法既耗时又计算成本高昂。然而，分析方法在计算扩展或处理环境动态变化方面也存在挑战。本研究提出利用基于扩散模型的规划器，该规划器能够处理动态变化的智能体数量。我们的方法在有限数量的智能体上进行训练，并在部署时能有效泛化至更多智能体。结果表明，通过将基于单一共享扩散模型的规划器与专用的智能体间注意力计算及时间卷积相结合，能够实现"训练小规模、部署大规模"的高精度范式。我们在多种场景下验证了该方法，并与现有的多智能体强化学习技术及基于启发式控制的方法进行了性能比较。

---

### 7. BiDexGrasp: Coordinated Bimanual Dexterous Grasps across Object Geometries and Sizes

- **作者**: Mu Lin, Yi-Lin Wei, Jiaxuan Chen, Yuhao Lin, Shuoyu Chen, Jiangran Lyu, Jiayi Chen, Yansong Tang, He Wang, Wei-Shi Zheng
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.06589v1)
- **发表日期**: 2026-04-08
- **匹配关键词**: dexterous grasping, grasp synthesis
- **arXiv**: [2604.06589v1](http://arxiv.org/abs/2604.06589v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 双手灵巧抓取是机器人学中一个基础且前景广阔的领域，但其发展因缺乏全面数据集和强大生成模型而受限。本研究提出BiDexGrasp系统，包含大规模双手灵巧抓取数据集与新型生成模型。在数据集构建方面，我们设计了一种创新的双手抓取合成流程，通过高效区域化抓取初始化与解耦力闭合抓取优化的两阶段合成策略，系统性地解决高维双手抓取标注难题，成功构建了涵盖6351个尺寸在30-80厘米的多样化物体、包含970万条标注抓取数据的大规模数据集。基于此数据集，我们进一步提出双手协调与几何尺寸自适应的灵巧抓取生成框架，其核心创新在于双手协调模块与几何尺寸自适应抓取生成策略，能够在未见物体上生成协调且高质量的抓取方案。在仿真环境与真实场景中的大量实验证明，我们提出的数据合成流程与生成框架均展现出卓越性能。

---

### 8. Learning-Guided Force-Feedback Model Predictive Control with Obstacle Avoidance for Robotic Deburring

- **作者**: Krzysztof Wojciechowski, Ege Gursoy, Arthur Haffemayer, Sebastien Kleff, Vincent Bonnet, Florent Lamiraux, Nicolas Mansard
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.06133v1)
- **发表日期**: 2026-04-07
- **匹配关键词**: obstacle avoidance
- **arXiv**: [2604.06133v1](http://arxiv.org/abs/2604.06133v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 模型预测控制（MPC）在扭矩控制机器人领域应用广泛，但传统方法常忽略实时力反馈，且在碰撞约束下的密集接触工业任务中表现不佳。特别是去毛刺作业，需要在复杂构型下实现精确工具插入、稳定力控以及无碰撞圆周运动，这已超出标准MPC流程的能力范围。我们提出一种融合力反馈MPC与基于扩散的运动先验框架来解决这些挑战。扩散模型作为运动策略的记忆库，为多任务场景提供鲁棒的初始化与自适应能力，而MPC则通过显式力跟踪、扭矩可行性与碰撞规避确保安全执行。我们在执行工业去毛刺任务的扭矩控制机械臂上验证了该方法。实验表明，即使在难以触及的构型和障碍物约束下，系统仍能实现可靠的工具插入、精确法向力跟踪及圆周去毛刺运动。据我们所知，这是首次将扩散运动先验与力反馈MPC相结合，用于具有碰撞感知的密集接触工业任务。

---

### 9. Intuitive Human-Robot Interaction: Development and Evaluation of a Gesture-Based User Interface for Object Selection

- **作者**: Bijan Kavousian, Oliver Petrovic, Werner Herfs
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.06073v1)
- **发表日期**: 2026-04-07
- **匹配关键词**: human-robot interaction
- **arXiv**: [2604.06073v1](http://arxiv.org/abs/2604.06073v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 手势是人类之间自然的交流方式，也可用于人机交互。本研究提出了一种基于手势的用户界面，通过指向与点击动作实现目标选择。一项包含20名参与者的实验评估了该系统的准确性与选择耗时，结果证明了其在提升协作效率方面的潜力。

---

### 10. Dialogue based Interactive Explanations for Safety Decisions in Human Robot Collaboration

- **作者**: Yifan Xu, Xiao Zhan, Akilu Yunusa Kaltungo, Ming Shan Ng, Tsukasa Ishizawa, Kota Fujimoto, Clara Cheung
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.05896v1)
- **发表日期**: 2026-04-07
- **匹配关键词**: exploration
- **arXiv**: [2604.05896v1](http://arxiv.org/abs/2604.05896v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 随着机器人在共享安全关键环境中日益广泛应用，仅确保安全行为已不足够——机器人还必须使其安全决策对人类协作者具有可理解性。在人机协作（HRC）场景中，诸如停止或切换模式等行为通常由内部安全约束触发，而这些约束对现场工作人员往往是不透明的。本文提出一种基于对话的交互式安全决策解释框架，该方法将解释过程与基于约束的安全评估紧密结合，使对话建立在与行为选择机制相同的状态和约束表征基础上。解释内容直接源自记录在案的决策轨迹，使用户能够就安全干预措施提出因果性（"为什么？"）、对比性（"为什么不？"）及反事实（"如果…会怎样？"）三类查询。反事实推理在固定且经过认证的安全参数范围内进行有界评估，确保交互式探索不会削弱操作安全保障。我们将该框架应用于建筑机器人场景，并通过结构化操作轨迹展示具备约束感知的对话如何阐明安全干预机制并支持协同任务恢复。通过将解释视为安全控制的操作接口，本研究为HRC领域交互式安全感知自主系统的设计提供了新的理论视角。

---

