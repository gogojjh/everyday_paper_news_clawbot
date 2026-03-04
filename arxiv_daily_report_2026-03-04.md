# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-03-04 08:04

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 2/20 篇提供

**🌟 Highlight**: 20 篇 | **📌 Poster**: 0 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. OnlineX: Unified Online 3D Reconstruction and Understanding with Active-to-Stable State Evolution

- **作者**: Chong Xia, Fangfu Liu, Yule Wang, Yize Pang, Yueqi Duan
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.02134v1)
- **发表日期**: 2026-03-02
- **匹配关键词**: gaussian splatting, 3D reconstruction, 3d reconstruction, 3D gaussian splatting
- **arXiv**: [2603.02134v1](http://arxiv.org/abs/2603.02134v1)
- **📥 PDF**: 已下载至本地 (`2603.02134v1_OnlineX_Unified_Online_3D_Reconstruction_and_Understanding_with_Active-to-Stable_State_Evolution.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 通用化三维高斯泼溅技术的最新进展使得三维场景重建能在数秒内完成，无需逐场景优化。然而，现有方法主要遵循离线重建范式，缺乏连续重建能力，这限制了其在机器人、VR/AR等在线场景中的应用。本文提出OnlineX框架，这是一种仅通过流式图像就能在线重建三维视觉外观与语言场的前馈式系统。在线建模的核心挑战在于累积漂移问题，其根源在于记忆状态的两种对立角色之间的根本冲突：一方面需要作为活跃状态持续更新以捕捉高频局部几何特征，另一方面又需作为稳定状态保守地积累并保持长期全局结构。为解决这一矛盾，我们提出解耦式"活跃-稳定"状态演化范式。该框架将记忆状态解耦为专用活跃状态与持久稳定状态，再将前者的信息融合至后者，从而实现细节保真与结构稳定的双重目标。此外，我们联合建模视觉外观与语言场，并引入隐式高斯融合模块以提升重建质量。在主流数据集上的实验表明，本方法在新视角合成与语义理解任务中持续优于现有技术，在不同长度的输入序列上均展现出鲁棒性能，并具备实时推理速度。

---

### 2. Closed-Loop Action Chunks with Dynamic Corrections for Training-Free Diffusion Policy

- **作者**: Pengyuan Wu, Pingrui Zhang, Zhigang Wang, Dong Wang, Bin Zhao, Xuelong Li
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.01953v1)
- **发表日期**: 2026-03-02
- **匹配关键词**: diffusion policy
- **arXiv**: [2603.01953v1](http://arxiv.org/abs/2603.01953v1)
- **📥 PDF**: 已下载至本地 (`2603.01953v1_Closed-Loop_Action_Chunks_with_Dynamic_Corrections_for_Training-Free_Diffusion_Policy.pdf`)
- **🔓 开源**: GITHUB, PROJECT_PAGE
  - 链接：https://github.com/wupengyuan/dcdp
- **中文摘要**: 基于扩散的策略在机器人操作中取得了显著成果，但在动态场景中往往难以快速适应，导致响应延迟或任务失败。我们提出DCDP——一种动态闭环扩散策略框架，该框架将分块动作生成与实时校正相结合。DCDP通过集成自监督动态特征编码器、交叉注意力融合机制及非对称动作编码器-解码器，在执行动作前注入环境动态信息，实现实时闭环动作校正，从而增强系统在动态场景中的适应性。在动态PushT仿真实验中，DCDP在不重新训练的情况下将适应性提升19%，同时仅需增加5%的计算开销。其模块化设计支持即插即用集成，在包括真实世界操作任务在内的动态机器人场景中，既能保持时间连贯性又能实现实时响应。项目页面位于：https://github.com/wupengyuan/dcdp

---

### 3. SaferPath: Hierarchical Visual Navigation with Learned Guidance and Safety-Constrained Control

- **作者**: Lingjie Zhang, Zeyu Jiang, Changhao Chen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.01898v1)
- **发表日期**: 2026-03-02
- **匹配关键词**: navigation, visual navigation
- **arXiv**: [2603.01898v1](http://arxiv.org/abs/2603.01898v1)
- **📥 PDF**: 已下载至本地 (`2603.01898v1_SaferPath_Hierarchical_Visual_Navigation_with_Learned_Guidance_and_Safety-Constrained_Control.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉导航是移动机器人的核心能力，然而基于端到端学习的方法在未知、杂乱或狭窄环境中常面临泛化性与安全性挑战。这些局限在密集室内场景中尤为突出，碰撞风险高且端到端模型易失效。为此，我们提出SaferPath——一种分层式视觉导航框架，该框架利用现有端到端模型的学习引导，并通过安全约束优化控制模块进行轨迹优化。SaferPath将视觉观测转换为可通行区域地图，并采用模型预测斯坦因变分进化策略（MP-SVES）优化引导轨迹，仅需数次迭代即可高效生成安全轨迹。优化后的轨迹由模型预测控制器跟踪，确保在复杂环境中的鲁棒导航。通过在未知障碍物、密集非结构化空间及狭窄走廊场景中的大量实验证明，SaferPath能持续提升成功率并降低碰撞率，其性能优于ViNT、NoMaD等代表性基线方法，实现了在挑战性现实场景中的安全导航。

---

### 4. Tiny-DroNeRF: Tiny Neural Radiance Fields aboard Federated Learning-enabled Nano-drones

- **作者**: Ilenia Carboni, Elia Cereda, Lorenzo Lamberti, Daniele Malpetti, Francesco Conti, Daniele Palossi
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.01850v1)
- **发表日期**: 2026-03-02
- **匹配关键词**: motion planning, 3d reconstruction, nerf, 3D reconstruction, neural radiance field
- **arXiv**: [2603.01850v1](http://arxiv.org/abs/2603.01850v1)
- **📥 PDF**: 已下载至本地 (`2603.01850v1_Tiny-DroNeRF_Tiny_Neural_Radiance_Fields_aboard_Federated_Learning-enabled_Nano-drones.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 重量不足30克的纳米级飞行机器人凭借其敏捷性与紧凑形态，可在工业检测、搜救任务等场景中自主探索复杂狭窄环境。然而微型化设计也导致其资源极度受限：搭载的微控制器单元（MCU）功耗低于100毫瓦，算力峰值约100 GOps/s，内存容量远低于100 MB。尽管存在这些严格约束，我们仍致力于在纳米无人机上实现复杂的视觉任务，例如密集三维场景重建——这是空间感知与运动规划等核心能力的基础关键技术。

当前最优的三维重建方法依赖神经辐射场（NeRF）模型，这类模型通常需要GB级内存与大规模计算能力，往往由功耗数百瓦的高端GPU支持。本研究提出Tiny-DroNeRF轻量化NeRF模型：基于Instant-NGP框架进行优化，专为搭载于纳米无人机的GAP9超低功耗MCU设计。我们进一步通过协同联邦学习方案增强系统性能，将模型训练任务分布式部署于多架纳米无人机。实验结果表明，Tiny-DroNeRF在保持重建精度仅下降5.7 dB的前提下，相较Instant-NGP实现了96%的内存占用缩减。联邦学习机制使模型能够处理单架无人机内存无法容纳的海量训练数据，从而提升整体重建精度。本研究首次在超低功耗MCU上实现了NeRF训练与纳米无人机联邦学习的融合创新。

---

### 5. MVR: Multi-view Video Reward Shaping for Reinforcement Learning

- **作者**: Lirui Luo, Guoxi Zhang, Hongming Xu, Yaodong Yang, Cong Fang, Qing Li
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.01694v1)
- **发表日期**: 2026-03-02
- **匹配关键词**: visual feedback
- **arXiv**: [2603.01694v1](http://arxiv.org/abs/2603.01694v1)
- **📥 PDF**: 已下载至本地 (`2603.01694v1_MVR_Multi-view_Video_Reward_Shaping_for_Reinforcement_Learning.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 奖励设计对于通过强化学习解决复杂任务至关重要。近期研究探索利用视觉语言模型（VLM）生成的图像-文本相似度，通过视觉反馈增强任务奖励。常见做法是将VLM评分与任务或成功奖励线性叠加而不进行显式塑形，这可能改变最优策略。此外，这类方法通常依赖单一静态图像，难以处理那些期望行为涉及跨越多个视觉差异状态的复杂动态运动的任务。单一视角还可能遮蔽智能体行为的关键方面。为解决这些问题，本文提出多视角视频奖励塑形框架（MVR），该框架利用多视角拍摄的视频建模状态与目标任务的相关性。MVR通过冻结预训练VLM提取的视频-文本相似度，学习状态相关性函数，从而缓解基于图像方法对特定静态姿态的固有偏差。此外，我们提出一种状态依赖的奖励塑形公式，将任务特定奖励与基于VLM的指导相结合，一旦达成期望运动模式即自动减弱VLM引导的影响。通过在HumanoidBench的复杂人形运动任务和MetaWorld的操作任务上进行大量实验，我们验证了所提框架的有效性，并通过消融研究证实了设计选择的合理性。

---

### 6. KERV: Kinematic-Rectified Speculative Decoding for Embodied VLA Models

- **作者**: Zihao Zheng, Zhihao Mao, Maoliang Li, Jiayu Chen, Xinhao Sun, Zhaobo Zhang, Donggang Cao, Hong Mei, Xiang Chen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.01581v1)
- **发表日期**: 2026-03-02
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2603.01581v1](http://arxiv.org/abs/2603.01581v1)
- **📥 PDF**: 已下载至本地 (`2603.01581v1_KERV_Kinematic-Rectified_Speculative_Decoding_for_Embodied_VLA_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型构建了基于令牌域的机器人控制范式，但其运行速度较慢。推测解码（SD）是一种能够提升推理速度的优化策略。将VLA与SD结合时出现两个关键问题：首先，SD依赖重新推理来处理令牌错误，计算成本高昂；其次，为减少令牌错误，SD中的接受阈值需要仔细调整。现有研究未能有效解决上述两个问题。同时，作为人工智能与物理世界之间的桥梁，现有具身智能研究忽视了机器人运动学的应用。为解决这些问题，我们创新性地将令牌域VLA模型与运动学域预测相结合用于SD，提出了一种名为KERV的运动学修正SD框架。我们采用基于运动学的卡尔曼滤波器来预测动作并补偿SD误差，从而避免昂贵的重新推理。此外，我们设计了一种基于运动学的调整策略来动态修正接受阈值，解决了阈值确定的难题。在不同任务和环境中的实验结果表明，KERV在几乎不损失成功率的情况下实现了27%~37%的加速。

---

### 7. ATA: Bridging Implicit Reasoning with Attention-Guided and Action-Guided Inference for Vision-Language Action Models

- **作者**: Cheng Yang, Jianhao Jiao, Lingyi Huang, Jinqi Xiao, Zhexiang Tang, Yu Gong, Yibiao Ying, Yang Sui, Jintian Lin, Wen Huang, Bo Yuan
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.01490v1)
- **发表日期**: 2026-03-02
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2603.01490v1](http://arxiv.org/abs/2603.01490v1)
- **📥 PDF**: 已下载至本地 (`2603.01490v1_ATA_Bridging_Implicit_Reasoning_with_Attention-Guided_and_Action-Guided_Inference_for_Vision-Languag.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型依赖当前观察（包括图像、语言指令和机器人状态）来预测动作并完成任务。虽然精确的视觉感知对于准确的动作预测与执行至关重要，但近期研究尝试通过在推理过程中引入显式推理来进一步提升性能。然而，这类方法面临显著局限：它们往往依赖思维链式标注等数据密集型资源将任务分解为逐步推理，且多数情况下需要额外的视觉定位标注（如边界框或掩码）来突出相关图像区域。此外，这些方法涉及耗时的数据集构建、标注和重新训练，最终导致推理序列延长、效率降低。为应对这些挑战，我们提出ATA——一种无需训练的新型框架，通过互补的注意力引导与动作引导策略将隐式推理引入VLA推理过程。与思维链或显式视觉定位方法不同，ATA通过将注意力图与基于动作的兴趣区域（RoI）相结合，以隐式形式实现推理，从而自适应优化视觉输入，无需额外训练或标注。ATA是一种即插即用的VLA隐式推理方法，轻量而高效。大量实验表明，该方法在保持甚至提升推理效率的同时，能持续提高任务成功率与鲁棒性。

---

### 8. SFCo-Nav: Efficient Zero-Shot Visual Language Navigation via Collaboration of Slow LLM and Fast Attributed Graph Alignment

- **作者**: Chaoran Xiong, Litao Wei, Xinhao Hu, Kehui Ma, Ziyi Xia, Zixin Jiang, Zhen Sun, Ling Pei
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.01477v1)
- **发表日期**: 2026-03-02
- **匹配关键词**: navigation, VLN
- **arXiv**: [2603.01477v1](http://arxiv.org/abs/2603.01477v1)
- **📥 PDF**: 已下载至本地 (`2603.01477v1_SFCo-Nav_Efficient_Zero-Shot_Visual_Language_Navigation_via_Collaboration_of_Slow_LLM_and_Fast_Attri.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 大型视觉语言模型（VLM）与大型语言模型（LLM）的最新进展，使得视觉语言导航（VLN）任务能够采用零样本方法实现，即智能体仅通过第一人称感知与推理来遵循自然语言指令进行导航。然而，现有零样本方法通常构建简单的观测图并在其上执行逐步骤的VLM-LLM推理，导致高延迟与计算成本，限制了实时部署能力。为此，我们提出SFCo-Nav——一种受慢-快认知协作机制启发的高效零样本VLN框架。该框架整合了三个核心模块：1）基于慢速LLM的规划器，生成与想象物体图关联的层级化子目标策略链；2）快速反应式导航器，用于实时构建物体图并执行子目标；3）轻量级异步慢-快桥接模块，通过对齐结构化属性想象图与感知图来估计导航置信度，仅在必要时触发慢速LLM规划器。据我们所知，SFCo-Nav是首个支持基于内部置信度异步触发LLM的慢-快协作零样本VLN系统。在公开R2R与REVERIE基准测试中，SFCo-Nav达到或超越了现有零样本VLN最优成功率，同时将单轨迹总token消耗降低超50%，运行速度提升3.5倍以上。最后，我们在酒店场景的四足机器人上验证了SFCo-Nav，展示了其在室内环境中的高效性与实用价值。

---

### 9. Mean-Flow based One-Step Vision-Language-Action

- **作者**: Yang Chen, Xiaoguang Ma, Bin Zhao
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.01469v1)
- **发表日期**: 2026-03-02
- **匹配关键词**: VLA, vision-language-action, diffusion policy
- **arXiv**: [2603.01469v1](http://arxiv.org/abs/2603.01469v1)
- **📥 PDF**: 已下载至本地 (`2603.01469v1_Mean-Flow_based_One-Step_Vision-Language-Action.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 基于流匹配的视觉-语言-动作框架近期取得显著进展，在生成高频动作片段方面展现出突出优势，尤其适用于高精度机器人操作任务。然而，这些成果在实际应用中受限于较长的生成延迟，这源于固有的迭代采样需求与架构限制。为突破这一关键瓶颈，我们提出基于均值流的单步视觉-语言-动作方法。具体而言，我们解决了动作生成过程中由噪声引发的问题，从而消除了传统流匹配方法固有的连续性约束。这显著提升了生成效率，实现了单步动作生成。真实机器人实验表明，所提出的基于均值流的单步视觉-语言-动作方法的生成速度分别达到SmolVLA的8.7倍和Diffusion Policy的83.9倍。这些结果充分证明了其作为视觉-语言-动作机器人操作高效核心框架的巨大潜力。

---

### 10. Non-Markovian Long-Horizon Robot Manipulation via Keyframe Chaining

- **作者**: Yipeng Chen, Wentao Tan, Lei Zhu, Fengling Li, Jingjing Li, Guoli Yang, Heng Tao Shen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.01465v1)
- **发表日期**: 2026-03-02
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2603.01465v1](http://arxiv.org/abs/2603.01465v1)
- **📥 PDF**: 已下载至本地 (`2603.01465v1_Non-Markovian_Long-Horizon_Robot_Manipulation_via_Keyframe_Chaining.pdf`)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/cytoplastm/KC-VLA.
- **中文摘要**: 现有的视觉-语言-动作（VLA）模型由于过度依赖即时观测，往往难以泛化到长时程任务中。尽管近期研究通过引入检索机制或扩展上下文窗口来处理流程性任务，但这些方法通常难以捕捉非马尔可夫依赖关系——即最优动作仅依赖于特定历史状态而非当前观测。为解决这一问题，我们提出了关键帧链式VLA框架，通过提取并链接关键历史帧来建模长时程依赖关系。具体而言，我们设计了一种自动关键帧选择器，通过学习判别性嵌入空间来有效识别不同的状态转移。为捕捉任务关键信息，我们开发了进度感知查询机制，根据历史帧与当前执行阶段的时间相关性进行动态检索。这些选定的关键帧以交错视觉标记的形式整合到VLA模型中，显式地将策略锚定在长时程时间上下文中。最后，我们在ManiSkill仿真平台上构建了包含四项非马尔可夫操作任务的测试集以评估任务成功率。实验结果表明，我们的方法在具有长时程时间依赖特性的机器人操作任务中取得了优越性能。代码已开源：https://github.com/cytoplastm/KC-VLA。

---

### 11. riMESA: Consensus ADMM for Real-World Collaborative SLAM

- **作者**: Daniel McGann, Michael Kaess ⭐
  - **高亮作者**: Michael Kaess
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.01178v1)
- **发表日期**: 2026-03-01
- **匹配关键词**: navigation, localization and mapping
- **arXiv**: [2603.01178v1](http://arxiv.org/abs/2603.01178v1)
- **📥 PDF**: 已下载至本地 (`2603.01178v1_riMESA_Consensus_ADMM_for_Real-World_Collaborative_SLAM.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 协作同步定位与建图（C-SLAM）是多机器人团队实现规划与导航等下游任务的基础能力。然而，现有解决该问题的C-SLAM后端算法难以应对实际部署中的现实挑战（如通信限制、异常测量和在线操作需求）。本文提出鲁棒增量流形边缘可分离交替方向乘子法（riMESA）——一种具备抗异常值能力、适应有限通信环境、能实时计算多机器人团队精确状态估计的鲁棒增量分布式C-SLAM后端算法。通过riMESA的研发，我们更广泛地论证了共识交替方向乘子法因其灵活性、精确性和快速收敛特性，可作为机器人分布式优化任务（如C-SLAM）的理论基础。本研究最后通过合成与真实C-SLAM数据，在不同C-SLAM场景和通信网络条件下对riMESA进行深入评估。实验表明，riMESA能适应多种条件生成精确状态估计，实现实时运算，并在真实数据集上以超过现有方法7倍的精度优势显著优于先前研究成果。

---

### 12. A Deployable Bio-inspired Compliant Leg Design for Enhanced Leaping in Quadruped Robots

- **作者**: Yiyang Chen, Yuxin Liu, Jinzheng Zhou, Fanxin Wang, Qinglei Bu, Jie Sun, Yikun Cheng
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.01128v1)
- **发表日期**: 2026-03-01
- **匹配关键词**: navigation
- **arXiv**: [2603.01128v1](http://arxiv.org/abs/2603.01128v1)
- **📥 PDF**: 已下载至本地 (`2603.01128v1_A_Deployable_Bio-inspired_Compliant_Leg_Design_for_Enhanced_Leaping_in_Quadruped_Robots.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 四足机器人在工业巡检、灾难搜救等应用场景中日益重要，这些场景要求机器人具备更强的敏捷性与越障能力。然而，现有平台常因电机峰值功率不足而难以实现爆发性跳跃，制约了其性能表现。为解决这一问题，本文受沫蝉腿部储能机制启发，提出一种仿生设计方法。我们采用具有轻质内部晶格结构的特种3D打印弹性材料——聚醚嵌段酰胺（PEBA），设计出可展开式柔性腿（DCL）。该结构模拟生物肌腱功能，在机器人下蹲阶段储存弹性势能，并在起跳瞬间快速释放以增强电机输出。所提出的机械设计显著提升了机器人的垂直跳跃能力，通过有限元分析与实验验证，垂直跳跃高度相对性能提升了17.1%。

---

### 13. Pro-HOI: Perceptive Root-guided Humanoid-Object Interaction

- **作者**: Yuhang Lin, Jiyuan Shi, Dewei Wang, Jipeng Kong, Yong Liu, Chenjia Bai, Xuelong Li
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.01126v1)
- **发表日期**: 2026-03-01
- **匹配关键词**: navigation
- **arXiv**: [2603.01126v1](http://arxiv.org/abs/2603.01126v1)
- **📥 PDF**: 已下载至本地 (`2603.01126v1_Pro-HOI_Perceptive_Root-guided_Humanoid-Object_Interaction.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 实现可靠的人形机器人-物体交互任务面临两大障碍：缺乏通用控制接口与鲁棒的闭环感知机制。本研究提出感知式根轨迹引导人形机器人-物体交互框架Pro-HOI，这是一个适用于鲁棒性人形机器人移动操作任务的通用化框架。首先，我们采集适用于现实场景部署的箱体搬运运动数据，并通过符号距离场损失函数优化运动穿透伪影。其次，我们设计了一种创新的训练框架：在策略训练中引入期望根轨迹作为条件约束，同时将参考运动数据专用于奖励函数构建。该设计不仅无需复杂奖励函数调参，还将根轨迹确立为高层规划器的通用接口，实现导航与移动操作的同步执行。此外，为确保操作可靠性，我们整合了持续性物体状态估计模块。通过实时检测与数字孪生系统的融合，该模块使机器人能够自主检测物体滑移并触发重新抓取动作。在宇树G1机器人上的实证验证表明，Pro-HOI在泛化能力与鲁棒性方面显著优于基线方法，能够在复杂现实场景中实现可靠的长时程任务执行。

---

### 14. Compact Task-Aligned Imitation Learning for Laboratory Automation

- **作者**: Kanata Suzuki, Hanon Nakamurama, Kana Miyamoto, Tetsuya Ogata
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.01110v1)
- **发表日期**: 2026-03-01
- **匹配关键词**: diffusion-based policy
- **arXiv**: [2603.01110v1](http://arxiv.org/abs/2603.01110v1)
- **📥 PDF**: 已下载至本地 (`2603.01110v1_Compact_Task-Aligned_Imitation_Learning_for_Laboratory_Automation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 传统机器人实验室自动化技术高度依赖精心设计的运动流程和特定任务硬件接口，导致设计成本高昂且灵活性受限。虽然近期模仿学习技术能够生成通用机器人行为，但其庞大的模型规模通常需要高性能计算资源，限制了在实际实验室环境中的应用。本研究提出了一种基于小型基础模型的紧凑型模仿学习框架用于实验室自动化。所提出的TVF-DiT方法通过紧凑适配器将自监督视觉基础模型与视觉语言模型对齐，并将其与基于扩散变换器的动作专家模块集成。整个模型参数量少于5亿，可在低显存GPU上实现推理。在三个真实实验室任务（试管清洗、试管排列和粉末转移）上的实验表明，该方法平均成功率达86.6%，显著优于其他轻量级基线模型。进一步研究发现，详细的任务提示能有效提升视觉语言对齐效果和任务性能。这些结果表明，当小型基础模型与基于扩散的策略学习经过适当对齐和集成后，能够在有限计算资源下有效支持实际实验室自动化应用。

---

### 15. LiftAvatar: Kinematic-Space Completion for Expression-Controlled 3D Gaussian Avatar Animation

- **作者**: Hualiang Wei, Shunran Jia, Jialun Liu, Wenhui Li
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.02129v1)
- **发表日期**: 2026-03-02
- **匹配关键词**: gaussian splatting, 3D gaussian splatting
- **arXiv**: [2603.02129v1](http://arxiv.org/abs/2603.02129v1)
- **📥 PDF**: 已下载至本地 (`2603.02129v1_LiftAvatar_Kinematic-Space_Completion_for_Expression-Controlled_3D_Gaussian_Avatar_Animation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出LiftAvatar，这是一种新范式，通过补全运动学空间（如面部表情与头部姿态）中的稀疏单目观测数据，并利用补全后的信号驱动高保真数字人生成。LiftAvatar是一个细粒度、表情可控的大规模视频扩散Transformer模型，能够基于单张或多张参考图像合成高质量、时序连贯的表情序列。其核心思想是将不完整的输入数据提升为更丰富的运动学表征，从而增强下游三维数字人流程的重建与动画效果。为此，我们引入（1）多粒度表情控制方案，将光影图与表情系数相结合以实现精准稳定的驱动；（2）多参考帧条件机制，聚合多帧图像的互补信息，确保强烈的三维一致性与可控性。作为即插即用的增强模块，LiftAvatar直接解决了日常单目视频中因运动学线索稀疏导致的基于三维高斯溅射数字人表现力受限和重建伪影问题。通过将不完整观测扩展为多样化的姿态-表情组合，LiftAvatar还能实现从大规模视频生成模型到三维流程的有效先验知识蒸馏，带来显著性能提升。大量实验表明，LiftAvatar能持续提升前沿三维数字人方法的动画质量与量化指标，尤其在极端、未见过的表情条件下表现突出。

---

### 16. $π$-StepNFT: Wider Space Needs Finer Steps in Online RL for Flow-based VLAs

- **作者**: Siting Wang, Xiaofeng Wang, Zheng Zhu, Minnan Pei, Xinyu Cui, Cheng Deng, Jian Zhao, Guan Huang, Haifeng Zhang, Jun Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.02083v1)
- **发表日期**: 2026-03-02
- **匹配关键词**: VLA, exploration, vision-language-action
- **arXiv**: [2603.02083v1](http://arxiv.org/abs/2603.02083v1)
- **📥 PDF**: 已下载至本地 (`2603.02083v1_$π$-StepNFT_Wider_Space_Needs_Finer_Steps_in_Online_RL_for_Flow-based_VLAs.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 基于流的视觉-语言-动作模型在具身控制方面表现出色，但在多步采样过程中存在难以处理的似然性问题，阻碍了在线强化学习的应用。我们提出\textbf{\textit{$\boldsymbolπ$-StepNFT}}（逐步负感知微调框架），这是一种无需评论家网络和似然计算的创新方法，每个优化步骤仅需单次前向传播，并完全摒弃了辅助价值网络。我们发现，更广阔的探索空间需要更精细的逐步指导来实现对齐。实验表明，$π$-StepNFT在LIBERO基准上展现出具有竞争力的少样本鲁棒性，释放了模型的潜在能力。此外，该方法在ManiSkill任务中实现了卓越的泛化性能，通过避免对多模态特征的过拟合，在分布外场景中超越了基于价值函数的基线模型。这一特性为复杂现实世界应用提供了可扩展的解决方案。

---

### 17. WorldStereo: Bridging Camera-Guided Video Generation and Scene Reconstruction via 3D Geometric Memories

- **作者**: Yisu Zhang, Chenjie Cao, Tengfei Wang, Xuhui Zuo, Junta Wu, Jianke Zhu, Chunchao Guo
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.02049v1)
- **发表日期**: 2026-03-02
- **匹配关键词**: 3D reconstruction, 3d reconstruction
- **arXiv**: [2603.02049v1](http://arxiv.org/abs/2603.02049v1)
- **📥 PDF**: 已下载至本地 (`2603.02049v1_WorldStereo_Bridging_Camera-Guided_Video_Generation_and_Scene_Reconstruction_via_3D_Geometric_Memori.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 基础视频扩散模型（VDM）近期取得显著进展。然而，尽管生成视频的视觉质量令人瞩目，但由于相机可控性有限以及从不同相机轨迹观察时生成内容存在不一致性，从这些输出中重建一致的三维场景仍具挑战性。本文提出WorldStereo——一种通过两个专用几何记忆模块连接相机引导视频生成与三维重建的创新框架。具体而言，全局几何记忆模块通过增量更新的点云实现精确相机控制，同时注入粗粒度结构先验。此外，空间立体记忆模块利用三维对应关系约束模型的注意力感受野，使其能聚焦于记忆库中的细粒度细节。这些组件使WorldStereo能够在精确相机控制下生成多视角一致的视频，从而促进高质量三维重建。得益于基于分布匹配的蒸馏VDM主干网络无需联合训练，采用灵活控制分支的WorldStereo展现出卓越效率。在相机引导视频生成和三维重建基准测试中的大量实验证明了我们方法的有效性。值得注意的是，WorldStereo可作为强大的世界模型，以高保真三维结果处理多样化场景生成任务（无论是从透视图像还是全景图像开始）。相关模型将予以开源。

---

### 18. LaST-VLA: Thinking in Latent Spatio-Temporal Space for Vision-Language-Action in Autonomous Driving

- **作者**: Yuechen Luo, Fang Li, Shaoqing Xu, Yang Ji, Zehan Zhang, Bing Wang, Yuannan Shen, Jianwei Cui, Long Chen, Guang Chen, Hangjun Ye, Zhi-Xin Yang, Fuxi Wen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.01928v1)
- **发表日期**: 2026-03-02
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2603.01928v1](http://arxiv.org/abs/2603.01928v1)
- **📥 PDF**: 已下载至本地 (`2603.01928v1_LaST-VLA_Thinking_in_Latent_Spatio-Temporal_Space_for_Vision-Language-Action_in_Autonomous_Driving.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 尽管视觉-语言-动作模型通过统一感知与规划革新了自动驾驶领域，但其对显式文本思维链的依赖导致了语义感知解耦与感知符号冲突。近期研究转向潜在推理机制，试图通过在连续隐空间中进行思考来绕过这些瓶颈。然而，由于缺乏显式的中间约束，标准潜在思维链往往表现为脱离物理规律的抽象表征。为此，我们提出潜在时空视觉-语言-动作模型——一种将推理范式从离散符号处理转向物理基础潜在时空思维链的框架。通过实施双特征对齐机制，我们将三维基础模型的几何约束与世界模型的动态预见能力直接蒸馏至潜在空间。配合从特征对齐逐步过渡到轨迹生成的渐进式监督微调训练策略，并采用分组相对策略优化的强化学习方法进行精细化调整，以确保安全性与规则遵从性。该方法在NAVSIM v1数据集上创下91.3%的规划决策匹配度新纪录，在NAVSIM v2数据集上达到87.1%的增强规划决策匹配度，同时在SURDS和NuDynamics基准测试中展现出卓越的时空推理能力。

---

### 19. Affine Correspondences in Stereo Vision: Theory, Practice, and Limitations

- **作者**: Levente Hajder
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.01836v1)
- **发表日期**: 2026-03-02
- **匹配关键词**: 3D reconstruction, 3d reconstruction
- **arXiv**: [2603.01836v1](http://arxiv.org/abs/2603.01836v1)
- **📥 PDF**: 已下载至本地 (`2603.01836v1_Affine_Correspondences_in_Stereo_Vision_Theory,_Practice,_and_Limitations.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 仿射变换在立体视觉领域近期得到了应用，其可广泛运用于各类计算机视觉任务，例如表面法向量估计、单应性矩阵计算以及基础矩阵与本质矩阵的求解。通过仿射对应关系甚至能够实现完整的三维重建。本文首先系统阐述仿射变换与对极几何的基本原理，继而深入探究变换精度对三维重建质量的影响机制。此外，我们创新性地提出基于对应图像方向估计局部仿射变换的方法，并充分利用待处理图像对相关的基础矩阵。研究通过合成数据与真实场景的定量评估，以重建表面法向量的精度作为衡量标准。针对真实场景评估，专门构建了包含三组正交棋盘格平面的特殊标定物。定量分析表明，在现实测试案例中表面法向量的估计误差约为数度。研究还针对特殊立体构型与平面方位进行了详细评估。

---

### 20. Neural Implicit Action Fields: From Discrete Waypoints to Continuous Functions for Vision-Language-Action Models

- **作者**: Haoyun Liu, Jianzhuang Zhao, Xinyuan Chang, Tianle Shi, Chuanzhang Meng, Jiayuan Tan, Feng Xiong, Tong Lin, Dongjie Huo, Mu Xu, SongLin Dong, Zhiheng Ma, Yihong Gong, Sheng Zhong
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.01766v1)
- **发表日期**: 2026-03-02
- **匹配关键词**: VLA, vision-language-action, vision-language-action model
- **arXiv**: [2603.01766v1](http://arxiv.org/abs/2603.01766v1)
- **📥 PDF**: 已下载至本地 (`2603.01766v1_Neural_Implicit_Action_Fields_From_Discrete_Waypoints_to_Continuous_Functions_for_Vision-Language-Ac.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 尽管视觉-语言-动作（VLA）模型发展迅速，但当前主流的离散路径点预测范式与物理运动固有的连续性存在根本性错位。这种离散化方法强制采用固定采样率，缺乏高阶可微性，并引入量化伪影，从而阻碍了精确、柔顺的交互。我们提出神经隐式动作场（NIAF），通过将动作预测从离散路径点重构为连续动作函数回归，实现了范式转变。NIAF利用多模态大语言模型作为可学习运动先验的分层频谱调制器，将无限分辨率的轨迹合成为连续时间流形。这种表述实现了解析可微性，允许对速度、加速度和加加速度进行显式监督，从而确保数学一致性和物理合理性。我们的方法在CALVIN和LIBERO基准测试中，针对不同骨干网络均取得了最先进的结果。此外，真实世界实验表明，NIAF能够实现稳定的阻抗控制，弥合了高层语义理解与底层动态执行之间的鸿沟。

---

