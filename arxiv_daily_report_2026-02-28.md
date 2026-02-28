# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-02-28 08:03

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 7/20 篇提供

**🌟 Highlight**: 20 篇 | **📌 Poster**: 0 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. UniScale: Unified Scale-Aware 3D Reconstruction for Multi-View Understanding via Prior Injection for Robotic Perception

- **作者**: Mohammad Mahdavian, Gordon Tan, Binbin Xu, Yuan Ren, Dongfeng Bai, Bingbing Liu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.23224v1)
- **发表日期**: 2026-02-26
- **匹配关键词**: navigation, 3d reconstruction, 3D reconstruction
- **arXiv**: [2602.23224v1](http://arxiv.org/abs/2602.23224v1)
- **📥 PDF**: 已下载至本地 (`2602.23224v1_UniScale_Unified_Scale-Aware_3D_Reconstruction_for_Multi-View_Understanding_via_Prior_Injection_for_.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出UniScale——一个面向机器人应用、具备统一尺度感知的多视角三维重建框架，该框架通过模块化语义感知设计灵活整合几何先验。在基于视觉的机器人导航中，从原始图像序列中准确提取环境结构对下游任务至关重要。UniScale通过单一前馈网络应对这一挑战，该网络能够从多视角图像中联合估计相机内外参数、尺度不变深度图与点云图以及场景的度量尺度，并可在获得辅助几何先验时选择性融合。通过将全局上下文推理与相机感知特征表示相结合，UniScale能够恢复场景的度量尺度。在相机内参已知的机器人应用场景中，可便捷融入该信息以提升性能；若同时获得相机位姿，则可实现额外增益。这种协同设计使得单一统一模型能够实现鲁棒的度量感知三维重建。值得注意的是，UniScale无需从头训练，可直接利用预训练模型中蕴含的、未采用几何编码策略的世界先验，这使其特别适合资源受限的机器人团队。我们在多个基准测试中评估UniScale，结果表明其在不同环境中均表现出强大的泛化能力和稳定的性能。论文录用后我们将公开实现代码。

---

### 2. Latent Gaussian Splatting for 4D Panoptic Occupancy Tracking

- **作者**: Maximilian Luz, Rohit Mohan, Thomas Nürnberg, Yakov Miron, Daniele Cattaneo, Abhinav Valada
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.23172v1)
- **发表日期**: 2026-02-26
- **匹配关键词**: gaussian splatting
- **arXiv**: [2602.23172v1](http://arxiv.org/abs/2602.23172v1)
- **📥 PDF**: 已下载至本地 (`2602.23172v1_Latent_Gaussian_Splatting_for_4D_Panoptic_Occupancy_Tracking.pdf`)
- **🔓 开源**: CODE
- **中文摘要**: 捕捉四维时空环境对于机器人在动态环境中安全可靠运行至关重要。然而，现有方法大多仅解决单方面问题：要么通过边界框提供粗略的几何追踪，要么提供缺乏明确时间关联的详细三维结构（如基于体素的占据表示）。本研究提出基于潜在高斯泼溅的四维全景占据追踪方法（LaGS），将时空场景理解推向整体化发展方向。该方法融合了基于摄像头的端到端追踪与基于掩码的多视角全景占据预测，并通过创新的潜在高斯泼溅技术，有效解决了多视角信息向三维体素网格高效聚合的关键挑战。具体而言，我们首先将观测数据融合为三维高斯分布，以此作为三维场景的稀疏点中心潜在表征，随后将聚合特征泼溅至三维体素网格，并通过基于掩码的分割头进行解码。我们在Occ3D nuScenes和Waymo数据集上评估LaGS，在四维全景占据追踪任务中取得了最先进的性能表现。代码已开源：https://lags.cs.uni-freiburg.de/。

---

### 3. DySL-VLA: Efficient Vision-Language-Action Model Inference via Dynamic-Static Layer-Skipping for Robot Manipulation

- **作者**: Zebin Yang, Yijiahao Qi, Tong Xie, Bo Yu, Shaoshan Liu, Meng Li
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.22896v1)
- **发表日期**: 2026-02-26
- **匹配关键词**: VLA, vision-language-action, vision-language-action model
- **arXiv**: [2602.22896v1](http://arxiv.org/abs/2602.22896v1)
- **📥 PDF**: 已下载至本地 (`2602.22896v1_DySL-VLA_Efficient_Vision-Language-Action_Model_Inference_via_Dynamic-Static_Layer-Skipping_for_Robo.pdf`)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/PKU-SEC-Lab/DYSL_VLA.
- **中文摘要**: 视觉-语言-动作（VLA）模型通过融合语言模型的推理能力与视觉模型的三维理解能力，在机器人操作等任务中展现出卓越性能。然而，其高昂的计算成本仍是实际应用中实现实时性能的主要障碍。我们观察到，任务中的动作具有不同程度的重要性：关键步骤需要高精度执行，而次要步骤则可容忍更大误差。基于这一发现，我们提出DySL-VLA框架，通过根据动作重要性动态跳过VLA层来降低计算成本。DySL-VLA将其网络层分为两类：必须持续执行的信息层和可选择性跳过的增量层。为在保持精度的前提下智能跳过网络层，我们设计了先验-后验跳层引导机制来确定跳层时机，并提出一种支持跳层的两阶段知识蒸馏算法，用于高效地将标准VLA模型训练为DySL-VLA模型。实验表明，在Calvin数据集上，DySL-VLA相比Deer-VLA实现了2.1%的成功长度提升，同时将可训练参数量减少85.7倍，并在同等精度下较RoboFlamingo基线获得3.75倍加速。代码已开源：https://github.com/PKU-SEC-Lab/DYSL_VLA。

---

### 4. GraspLDP: Towards Generalizable Grasping Policy via Latent Diffusion

- **作者**: Enda Xiang, Haoxiang Ma, Xinzhu Ma, Zicheng Liu, Di Huang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.22862v1)
- **发表日期**: 2026-02-26
- **匹配关键词**: diffusion policy, diffusion-based policy
- **arXiv**: [2602.22862v1](http://arxiv.org/abs/2602.22862v1)
- **📥 PDF**: 已下载至本地 (`2602.22862v1_GraspLDP_Towards_Generalizable_Grasping_Policy_via_Latent_Diffusion.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 本文聚焦于提升通过模仿学习习得的操作策略在抓取精度与泛化能力方面的表现。基于扩散模型的策略学习方法近年来已成为机器人操作任务的主流范式。抓取作为操作中的关键子任务，模仿学习策略执行精确且可泛化抓取的能力值得特别关注。现有抓取模仿学习方法常面临抓取执行不精确、空间泛化能力有限及物体泛化性能不足等问题。为应对这些挑战，我们将抓取先验知识融入扩散策略框架：采用潜在扩散策略，以抓取姿态先验引导动作块解码，确保生成的运动轨迹紧密贴合可行抓取构型；同时，在扩散过程中引入自监督重构目标以嵌入抓取性先验——在逆向扩散的每一步，通过中间表征反投影抓取性信息，重构腕部相机图像。仿真与真实机器人实验均表明，本方法显著优于基线方法，并展现出强大的动态抓取能力。

---

### 5. ArtPro: Self-Supervised Articulated Object Reconstruction with Adaptive Integration of Mobility Proposals

- **作者**: Xuelu Li, Zhaonan Wang, Xiaogang Wang, Lei Wu, Manyi Li, Changhe Tu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.22666v1)
- **发表日期**: 2026-02-26
- **匹配关键词**: articulated object, gaussian splatting, 3D gaussian splatting
- **arXiv**: [2602.22666v1](http://arxiv.org/abs/2602.22666v1)
- **📥 PDF**: 已下载至本地 (`2602.22666v1_ArtPro_Self-Supervised_Articulated_Object_Reconstruction_with_Adaptive_Integration_of_Mobility_Propo.pdf`)
- **🔓 开源**: MODEL
- **中文摘要**: 重建高保真数字孪生关节物体对于机器人操控和交互仿真等应用至关重要。当前基于可微分渲染框架（如3D高斯泼溅）的自监督方法仍高度依赖初始部件分割结果，其采用启发式聚类或预训练模型的策略常导致优化陷入局部最优，尤其对于复杂多部件物体。为突破这些局限，我们提出ArtPro——一种引入运动假设自适应整合机制的新型自监督框架。该方法首先通过几何特征与运动先验引导的过分割初始化，生成具有合理运动假设的部件提案。在优化过程中，我们通过分析空间邻域间的运动一致性动态合并提案，同时采用碰撞感知的运动剪枝机制防止错误运动估计。在合成与真实物体数据集上的大量实验表明，ArtPro能实现对复杂多部件物体的鲁棒重建，在精度与稳定性上显著超越现有方法。

---

### 6. Rethinking the Practicality of Vision-language-action Model: A Comprehensive Benchmark and An Improved Baseline

- **作者**: Wenxuan Song, Jiayi Chen, Xiaoquan Sun, Huashuo Lei, Yikai Qin, Wei Zhao, Pengxiang Ding, Han Zhao, Tongxin Wang, Pengxu Hou, Zhide Zhong, Haodong Yan, Donglin Wang, Jun Ma, Haoang Li
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.22663v1)
- **发表日期**: 2026-02-26
- **匹配关键词**: vision-language-action model, mobile manipulation, navigation, navigation and manipulation, vision-language-action, VLA
- **arXiv**: [2602.22663v1](http://arxiv.org/abs/2602.22663v1)
- **📥 PDF**: 已下载至本地 (`2602.22663v1_Rethinking_the_Practicality_of_Vision-language-action_Model_A_Comprehensive_Benchmark_and_An_Improve.pdf`)
- **🔓 开源**: CODE
- **中文摘要**: 视觉-语言-动作（VLA）模型已成为通用机器人智能体的重要发展方向。然而，现有VLA模型普遍面临参数量过大、预训练成本高昂、跨实体平台适应性有限等挑战。为提升VLA模型的实用性，本研究提出系统性评测基准与改进基线方案。首先，我们构建了CEBench基准测试平台，涵盖仿真环境与真实场景中的多样化机器人实体，并引入领域随机化设计。该平台包含1.44万条仿真轨迹与1600条专家标注真实轨迹，为模型训练提供数据支撑。其次，基于CEBench的系统性实验，我们针对VLA实用性的三个关键维度展开研究，并获得多项重要发现。基于这些发现，我们提出LLaVA-VLA模型——专为消费级GPU部署设计的轻量化高性能VLA架构。该架构融合紧凑型视觉语言模型骨干网络，集成多视角感知、本体感知令牌化与动作分块处理机制。为摆脱对昂贵预训练的依赖，LLaVA-VLA采用包含后训练与微调的两阶段训练范式。此外，模型通过扩展动作空间实现了导航与操作任务的统一处理。跨实体实验验证了LLaVA-VLA的泛化能力与多任务适应性，真实场景移动操作实验则首次实现了端到端VLA模型在移动操作任务中的完整验证。本研究承诺在论文录用后开源全部数据集、代码与模型权重，以促进研究可复现性与后续探索。

---

### 7. Metamorphic Testing of Vision-Language Action-Enabled Robots

- **作者**: Pablo Valle, Sergio Segura, Shaukat Ali, Aitor Arrieta
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.22579v1)
- **发表日期**: 2026-02-26
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2602.22579v1](http://arxiv.org/abs/2602.22579v1)
- **📥 PDF**: 已下载至本地 (`2602.22579v1_Metamorphic_Testing_of_Vision-Language_Action-Enabled_Robots.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型是一种多模态机器人任务控制器，它根据指令和视觉输入生成一系列低级控制动作（或运动指令），使机器人能够在物理环境中执行所需任务。这些系统从多个角度面临测试预言问题。一方面，必须为每个指令提示定义测试预言，这是一种复杂且难以泛化的方法。另一方面，当前最先进的预言通常捕捉世界的符号表示（例如机器人和物体状态），从而能够评估任务的正确性，但无法评估其他关键方面，例如支持VLA的机器人执行任务的质量。本文探讨了蜕变测试（MT）是否能够缓解这一背景下的测试预言问题。为此，我们提出了两种蜕变关系模式和五种蜕变关系，以评估测试输入的变化是否影响支持VLA的机器人的原始轨迹。一项涉及五个VLA模型、两个模拟机器人和四个机器人任务的实证研究表明，MT能够通过自动检测多种类型的故障（包括但不限于未完成的任务）有效缓解测试预言问题。更重要的是，所提出的蜕变关系具有泛化性，使得该方法适用于不同的VLA模型、机器人和任务，即使在缺乏测试预言的情况下也是如此。

---

### 8. SignVLA: A Gloss-Free Vision-Language-Action Framework for Real-Time Sign Language-Guided Robotic Manipulation

- **作者**: Xinyu Tan, Ningwei Bai, Harry Gardener, Zhengyang Zhong, Luoyu Zhang, Liuhaichen Yang, Zhekai Duan, Monkgogi Galeitsiwe, Zezhi Tang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.22514v1)
- **发表日期**: 2026-02-26
- **匹配关键词**: VLA, vision-language-action, human-robot interaction
- **arXiv**: [2602.22514v1](http://arxiv.org/abs/2602.22514v1)
- **📥 PDF**: 已下载至本地 (`2602.22514v1_SignVLA_A_Gloss-Free_Vision-Language-Action_Framework_for_Real-Time_Sign_Language-Guided_Robotic_Man.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 据我们所知，我们首次提出了基于手语驱动的视觉-语言-动作框架，以实现直观且包容的人机交互。与依赖注释作为中间监督的传统方法不同，该系统采用无注释范式，直接将视觉手语手势映射为语义指令。这一设计降低了标注成本，避免了注释表示带来的信息损失，从而实现更自然、可扩展的多模态交互。

本研究聚焦于实时字母级指拼交互界面，为机器人控制提供稳健、低延迟的通信通道。与大规模连续手语识别相比，字母级交互在安全关键的具体环境中具有更高的可靠性、可解释性和部署可行性。所提出的流程通过几何归一化、时间平滑和词汇优化，将连续手势流转化为连贯的语言指令，确保交互的稳定性和一致性。

此外，该框架设计支持未来集成基于Transformer的无注释手语模型，以实现可扩展的单词级和句子级语义理解。实验结果表明，该系统在不同交互场景下能有效将手语指令转化为精确的机器人动作。这些成果凸显了该框架在推动可访问、可扩展、多模态具身智能发展方面的潜力。

---

### 9. When to Act, Ask, or Learn: Uncertainty-Aware Policy Steering

- **作者**: Jessie Yuan, Yilin Wu, Andrea Bajcsy
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.22474v1)
- **发表日期**: 2026-02-25
- **匹配关键词**: diffusion policy
- **arXiv**: [2602.22474v1](http://arxiv.org/abs/2602.22474v1)
- **📥 PDF**: 已下载至本地 (`2602.22474v1_When_to_Act,_Ask,_or_Learn_Uncertainty-Aware_Policy_Steering.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 策略引导是一种在部署时调整机器人行为的新兴方法：通过学习验证器分析预训练策略（如扩散策略）提出的低层动作样本，仅选择与任务相符的动作。尽管视觉语言模型因其推理能力有望成为通用验证器，但现有框架常假设这些模型已良好校准。实际上，在任务规范存在高层语义不确定性，以及预训练策略存在低层动作不确定性或能力不足的情况下，视觉语言模型的过度自信判断会降低引导性能。我们提出不确定性感知策略引导框架，该框架能同时推理语义任务不确定性与低层动作可行性，并选择不确定性解决策略：执行高置信度动作、通过自然语言查询澄清任务歧义，或在判定低层策略无法胜任任务时请求动作干预。我们利用共形预测校准视觉语言模型与预训练基础策略的组合，为验证器选择正确策略提供统计保证。在部署过程中收集干预数据后，采用残差学习提升预训练策略的能力，使系统能够持续学习，同时最大限度减少昂贵的人工反馈。通过仿真与硬件实验验证，本框架能有效区分确信场景、模糊场景与能力不足场景，相较于未校准基线及先验的人机协同持续学习方法，显著减少了高成本用户干预。实验视频详见 https://jessie-yuan.github.io/ups/

---

### 10. Are Foundation Models the Route to Full-Stack Transfer in Robotics?

- **作者**: Freek Stulp, Samuel Bustamante, João Silvério, Alin Albu-Schäffer, Jeannette Bohg, Shuran Song ⭐
  - **高亮作者**: Shuran Song
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.22001v1)
- **发表日期**: 2026-02-25
- **匹配关键词**: VLA
- **arXiv**: [2602.22001v1](http://arxiv.org/abs/2602.22001v1)
- **📥 PDF**: 已下载至本地 (`2602.22001v1_Are_Foundation_Models_the_Route_to_Full-Stack_Transfer_in_Robotics?.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 在人类与机器人领域，迁移学习发生在不同抽象层次——从高层次的语言迁移到低层次的运动技能迁移。本文系统梳理了基础模型与Transformer网络对这些不同层次迁移学习的影响，推动机器人技术比以往更接近"全栈迁移"的实现。从机器人迁移学习的视角审视大语言模型、视觉语言模型及视觉语言动作模型，使我们能够超越具体技术实现，聚焦迁移学习中反复出现的核心概念。我们还探讨了基础模型时代下机器人数据收集与迁移基准测试所面临的挑战。基础模型是否真能引领机器人实现全栈迁移？我们的判断是，它们必将作为关键技术持续推动这一进程。

---

### 11. Humanizing Robot Gaze Shifts: A Framework for Natural Gaze Shifts in Humanoid Robots

- **作者**: Jingchao Wei, Jingkai Qin, Yuxiao Cao, Jingcheng Huang, Xiangrui Zeng, Min Li, Zhouping Yin
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.21983v1)
- **发表日期**: 2026-02-25
- **匹配关键词**: HRI, visual feedback
- **arXiv**: [2602.21983v1](http://arxiv.org/abs/2602.21983v1)
- **📥 PDF**: 已下载至本地 (`2602.21983v1_Humanizing_Robot_Gaze_Shifts_A_Framework_for_Natural_Gaze_Shifts_in_Humanoid_Robots.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 利用听觉与视觉反馈进行注意力重定向，是实现社交互动中自然视线转移的关键。然而，在开放场景的人机交互中，使人形机器人能够执行自然且符合情境的视线转移仍具挑战，因为这需要将认知注意力机制与仿生运动生成相结合。本研究提出机器人视线转移框架，将这两个组件整合为统一流程。该框架首先采用基于视觉-语言模型的视线推理管道，从多模态交互线索中推断符合情境的注视目标，确保与人类视线转移规律保持一致；其次引入条件向量量化变分自编码器模型，用于生成眼-头协调的视线转移动作，从而产生多样化且类人的视线转移行为。实验验证表明，该框架能有效复现类人的目标选择机制，并生成逼真、多样化的视线转移动作。

---

### 12. Dream-SLAM: Dreaming the Unseen for Active SLAM in Dynamic Environments

- **作者**: Xiangqi Meng, Pengxu Hou, Zhenjun Zhao, Javier Civera, Daniel Cremers, Hesheng Wang, Haoang Li ⭐
  - **高亮作者**: Daniel Cremers
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.21967v1)
- **发表日期**: 2026-02-25
- **匹配关键词**: exploration, motion planning, localization and mapping
- **arXiv**: [2602.21967v1](http://arxiv.org/abs/2602.21967v1)
- **📥 PDF**: 已下载至本地 (`2602.21967v1_Dream-SLAM_Dreaming_the_Unseen_for_Active_SLAM_in_Dynamic_Environments.pdf`)
- **🔓 开源**: CODE
- **中文摘要**: 除了同步定位与建图（SLAM）的核心任务外，主动SLAM还涉及生成机器人动作，以实现对未知环境的高效探索。然而，现有主动SLAM流程主要受限于三个因素：其一，它们继承了所采用底层SLAM模块的固有局限；其二，其运动规划策略通常缺乏长远视野，局限于短期决策；其三，多数方法难以有效处理动态场景。为突破这些限制，本文提出一种新颖的单目主动SLAM方法——Dream-SLAM，该方法基于对部分观测动态环境的跨时空图像与语义合理结构的梦境生成。通过将生成的跨时空图像与真实观测数据融合，有效降低了噪声影响并弥补了数据不完整性，从而实现了更精确的相机位姿估计和更连贯的三维场景重建。此外，我们整合梦境生成与观测得到的场景结构，构建具有长远视野的规划能力，生成促进高效全面探索的远见轨迹。在公开数据集及自采集数据集上的大量实验表明，Dream-SLAM在定位精度、建图质量与探索效率方面均优于现有先进方法。论文录用后源代码将公开提供。

---

### 13. Enhancing Cellular-enabled Collaborative Robots Planning through GNSS data for SAR Scenarios

- **作者**: Arnau Romero, Carmen Delgado, Jana Baguer, Raúl Suárez, Xavier Costa-Pérez
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.21899v1)
- **发表日期**: 2026-02-25
- **匹配关键词**: collaborative robot, exploration
- **arXiv**: [2602.21899v1](http://arxiv.org/abs/2602.21899v1)
- **📥 PDF**: 已下载至本地 (`2602.21899v1_Enhancing_Cellular-enabled_Collaborative_Robots_Planning_through_GNSS_data_for_SAR_Scenarios.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 基于蜂窝网络的协作机器人在搜救与应急响应中正变得至关重要。这些机器人高度依赖稳定的移动网络连接，在快速定位受困者、探索危险或难以进入区域等任务中发挥着不可替代的作用。然而，其对电池供电的依赖以及对持续低延迟通信的需求，限制了其作业时间和移动能力。为解决这一问题，并考虑到5G/6G网络不断演进的能力，我们提出了一种新型搜救框架，包含任务规划与任务执行两个阶段，可优化机器人部署方案。通过综合考虑搜索区域大小、地形高程、机器人集群规模、通信能耗特征、目标探索速率及响应时间等参数，该框架能够确定所需机器人的最小数量及其最优路径，从而确保在移动网络环境下实现有效区域覆盖与及时数据回传。研究结果揭示了轮式与四足机器人在数量配置、探索范围及响应时间之间的权衡关系。此外，我们量化了地形高程数据对任务时长与能耗的影响，证明了将可能影响移动信号传播与连接的真实环境因素纳入搜救规划的优越性。该框架为利用新一代移动网络增强自主搜救作业效能提供了重要参考依据。

---

### 14. EndoDDC: Learning Sparse to Dense Reconstruction for Endoscopic Robotic Navigation via Diffusion Depth Completion

- **作者**: Yinheng Lin, Yiming Huang, Beilei Cui, Long Bai, Huxin Gao, Hongliang Ren, Jiewen Lai
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.21893v2)
- **发表日期**: 2026-02-25
- **匹配关键词**: navigation, 3d reconstruction, 3D reconstruction
- **arXiv**: [2602.21893v2](http://arxiv.org/abs/2602.21893v2)
- **📥 PDF**: 已下载至本地 (`2602.21893v2_EndoDDC_Learning_Sparse_to_Dense_Reconstruction_for_Endoscopic_Robotic_Navigation_via_Diffusion_Dept.pdf`)
- **🔓 开源**: GITHUB, CODE
  - 链接：https://github.com/yinheng-lin/EndoDDC.
- **中文摘要**: 精确的深度估计在内窥镜手术机器人导航中起着至关重要的作用，为三维重建和安全器械引导奠定基础。预训练模型的微调高度依赖具有精确深度标注的内窥镜手术数据集。虽然现有的自监督深度估计技术无需精确深度标注，但其在纹理弱、光照多变环境中的性能会下降，导致重建稀疏且深度估计无效。利用稀疏深度图进行深度补全可以缓解这些问题并提高准确性。尽管深度补全技术在通用领域已取得进展，但其在内窥镜领域的应用仍然有限。为克服这些限制，我们提出EndoDDC——一种融合图像、稀疏深度信息与深度梯度特征，并通过扩散模型优化深度图的内窥镜深度补全方法，以解决内窥镜环境中纹理弱和光反射问题。在两个公开可用的内窥镜数据集上进行的大量实验表明，我们的方法在深度准确性和鲁棒性方面均优于现有最优模型。这证明了我们的方法在复杂内窥镜环境中减少视觉误差的潜力。我们的代码将在https://github.com/yinheng-lin/EndoDDC发布。

---

### 15. Joint-Aligned Latent Action: Towards Scalable VLA Pretraining in the Wild

- **作者**: Hao Luo, Ye Wang, Wanpeng Zhang, Haoqi Yuan, Yicheng Feng, Haiweng Xu, Sipeng Zheng, Zongqing Lu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.21736v1)
- **发表日期**: 2026-02-25
- **匹配关键词**: VLA, vision-language-action, vision-language-action model
- **arXiv**: [2602.21736v1](http://arxiv.org/abs/2602.21736v1)
- **📥 PDF**: 已下载至本地 (`2602.21736v1_Joint-Aligned_Latent_Action_Towards_Scalable_VLA_Pretraining_in_the_Wild.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 尽管已有进展，视觉-语言-动作模型（VLAs）仍受限于大规模多样化机器人数据的稀缺。虽然人类操作视频提供了丰富的替代资源，但现有方法不得不在小规模精准标注数据集与海量追踪标签不可靠的野外视频之间做出取舍。我们提出JALA——一种学习联合对齐潜在动作的预训练框架。该方法绕过了完整的视觉动态重建，转而学习与逆向动力学及真实动作双重对齐的预测性动作嵌入，从而构建出适用于异构人类数据学习的、具备状态转移感知与行为中心化特性的潜在空间。我们通过UniHand-Mix数据集（包含750万视频片段，总时长超2000小时）融合实验室与野外视频素材，实现了该方法的规模化应用。实验表明，JALA在受控与非受限场景下均能生成更逼真的手部动作，显著提升了仿真与真实世界任务中的机器人操作性能。这些结果表明，联合对齐潜在动作为基于人类数据的VLA预训练提供了可扩展的路径。

---

### 16. VGG-T$^3$: Offline Feed-Forward 3D Reconstruction at Scale

- **作者**: Sven Elflein, Ruilong Li, Sérgio Agostinho, Zan Gojcic, Laura Leal-Taixé, Qunjie Zhou, Aljosa Osep
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.23361v1)
- **发表日期**: 2026-02-26
- **匹配关键词**: 3d reconstruction, 3D reconstruction
- **arXiv**: [2602.23361v1](http://arxiv.org/abs/2602.23361v1)
- **📥 PDF**: 已下载至本地 (`2602.23361v1_VGG-T$^3$_Offline_Feed-Forward_3D_Reconstruction_at_Scale.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出了一种可扩展的三维重建模型，旨在解决离线前馈方法的一个关键局限：其计算与内存需求随输入图像数量呈二次方增长。我们的方法基于一个核心发现：这一瓶颈源于场景几何的可变长度键值空间表示。我们通过测试时训练将其提炼为固定大小的多层感知机。VGG-T$^3$（视觉几何基础测试时训练模型）在处理输入视图时具有线性复杂度，与在线模型类似，仅需$54$秒即可完成$1k$规模图像集的重建，相比依赖softmax注意力的基线方法实现了$11.6$倍的加速。由于本方法保留了全局场景聚合能力，其点云重建误差显著优于其他线性时间复杂度方法。最后，我们通过使用未见过的图像查询场景表示，展示了模型在视觉定位方面的能力。

---

### 17. PackUV: Packed Gaussian UV Maps for 4D Volumetric Video

- **作者**: Aashish Rai, Angela Xing, Anushka Agarwal, Xiaoyan Cong, Zekun Li, Tao Lu, Aayush Prakash, Srinath Sridhar
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.23040v1)
- **发表日期**: 2026-02-26
- **匹配关键词**: gaussian splatting
- **arXiv**: [2602.23040v1](http://arxiv.org/abs/2602.23040v1)
- **📥 PDF**: 已下载至本地 (`2602.23040v1_PackUV_Packed_Gaussian_UV_Maps_for_4D_Volumetric_Video.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 体积视频提供了沉浸式的4D体验，但在大规模重建、存储和流式传输方面仍面临挑战。现有基于高斯泼溅的方法虽能实现高质量重建，但在长序列处理、时间一致性保持方面存在不足，且难以应对大幅运动与遮挡解除场景。此外，其输出通常与传统视频编码流程不兼容，限制了实际应用。

我们提出PackUV——一种创新的4D高斯表征方法，将全部高斯属性映射至结构化多尺度UV图集序列，实现紧凑的图像原生存储。为从多视角视频中适配该表征，我们开发了PackUV-GS时序一致性拟合方法，直接在UV域优化高斯参数。通过流引导的高斯标记与视频关键帧模块，系统能识别动态高斯元素、稳定静态区域，即使在大幅运动和遮挡解除场景下仍能保持时间连贯性。最终生成的UV图集格式首次实现了与标准视频编解码器（如FFV1）的无损兼容，可在现有多媒体基础设施中实现高效流式传输。

为评估长时体积捕捉性能，我们构建了迄今最大的多视角视频数据集PackUV-2B，包含100个序列共20亿帧画面，配置超过50台同步摄像机，涵盖显著运动与频繁遮挡解除场景。大量实验表明，我们的方法在渲染保真度上超越现有基线，并能以稳定质量扩展至长达30分钟的连续序列。

---

### 18. UCM: Unifying Camera Control and Memory with Time-aware Positional Encoding Warping for World Models

- **作者**: Tianxing Xu, Zixuan Wang, Guangyuan Wang, Li Hu, Zhongyi Zhang, Peng Zhang, Bang Zhang, Song-Hai Zhang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.22960v1)
- **发表日期**: 2026-02-26
- **匹配关键词**: 3d reconstruction, 3D reconstruction
- **arXiv**: [2602.22960v1](http://arxiv.org/abs/2602.22960v1)
- **📥 PDF**: 已下载至本地 (`2602.22960v1_UCM_Unifying_Camera_Control_and_Memory_with_Time-aware_Positional_Encoding_Warping_for_World_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 基于视频生成的世界模型在模拟交互环境方面展现出巨大潜力，但长期面临两大核心挑战：场景重访时难以保持内容一致性，以及难以根据用户输入实现精确的相机控制。现有基于显式三维重建的方法常在无边界场景和精细结构上牺牲灵活性；而依赖历史生成帧的替代方案因缺乏显式空间对应关系，制约了可控性与一致性。为此，我们提出UCM框架，通过时序感知的位置编码扭曲机制，将长期记忆与精确相机控制相统一。为降低计算成本，我们设计了高效的双流扩散变换器以实现高保真生成。此外，我们引入基于点云渲染的可扩展数据构建策略，模拟场景重访过程，成功在超过50万段单目视频上完成训练。在真实场景与合成数据集上的大量实验表明，UCM在长期场景一致性方面显著优于现有先进方法，同时在高保真视频生成中实现了精确的相机可控性。

---

### 19. BetterScene: 3D Scene Synthesis with Representation-Aligned Generative Model

- **作者**: Yuci Han, Charles Toth, John E. Anderson, William J. Shuart, Alper Yilmaz
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.22596v1)
- **发表日期**: 2026-02-26
- **匹配关键词**: gaussian splatting, 3D gaussian splatting
- **arXiv**: [2602.22596v1](http://arxiv.org/abs/2602.22596v1)
- **📥 PDF**: 已下载至本地 (`2602.22596v1_BetterScene_3D_Scene_Synthesis_with_Representation-Aligned_Generative_Model.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出BetterScene方法，通过使用极稀疏、无约束的照片来提升多样化真实场景的新视角合成质量。该方法以经过数十亿帧预训练、具备生产就绪性的稳定视频扩散模型作为强大骨干网络，旨在推理过程中减少伪影并恢复视角一致的细节。传统方法已开发出类似的基于扩散模型的解决方案来应对新视角合成的这些挑战。尽管已有显著改进，但这些方法通常依赖现成的预训练扩散先验，仅对UNet模块进行微调而保持其他组件冻结，即使结合深度或语义条件等几何感知正则化手段，仍会导致细节不一致和伪影问题。为解决这一问题，我们深入研究了扩散模型的潜在空间，并引入两个关键组件：(1)时间等变性正则化与(2)视觉基础模型对齐表征，二者均应用于稳定视频扩散流程中的变分自编码器模块。BetterScene整合了前馈式3D高斯溅射模型，通过渲染特征作为稳定视频扩散增强器的输入，从而生成连续、无伪影且保持视角一致的新视图。我们在具有挑战性的DL3DV-10K数据集上进行评估，结果表明该方法相较于现有先进技术展现出更优越的性能。

---

### 20. GSTurb: Gaussian Splatting for Atmospheric Turbulence Mitigation

- **作者**: Hanliang Du, Zhangji Lu, Zewei Cai, Qijian Tang, Qifeng Yu, Xiaoli Liu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.22800v1)
- **发表日期**: 2026-02-26
- **匹配关键词**: gaussian splatting
- **arXiv**: [2602.22800v1](http://arxiv.org/abs/2602.22800v1)
- **📥 PDF**: 已下载至本地 (`2602.22800v1_GSTurb_Gaussian_Splatting_for_Atmospheric_Turbulence_Mitigation.pdf`)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/DuhlLiamz/3DGS_turbulence/tree/main.
- **中文摘要**: 大气湍流会导致像素位移（倾斜）和模糊，从而显著降低图像质量，尤其在远距离成像应用中尤为明显。本文提出了一种新颖的大气湍流抑制框架GSTurb，该框架结合了光流引导的倾斜校正与高斯泼溅技术，用于建模非等晕模糊。该框架利用高斯参数表示倾斜和模糊，并通过多帧优化来提升图像恢复效果。在ATSyn-static数据集上的实验结果表明，本方法具有显著效果，峰值PSNR达到27.67 dB，SSIM为0.8735。与现有最优方法相比，GSTurb将PSNR提升了1.3 dB（增幅4.5%），SSIM提升了0.048（增幅5.8%）。此外，在包括TSRWGAN Real-World和CLEAR在内的真实数据集上，GSTurb均优于现有方法，在定性和定量性能上均展现出显著提升。这些结果证明，结合光流引导的倾斜校正与高斯泼溅技术，能有效增强合成及真实湍流条件下的图像恢复效果。本方法的代码将在https://github.com/DuhlLiamz/3DGS_turbulence/tree/main 公开。

---

