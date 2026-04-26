# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-04-26 08:04

**今日新增**: 10 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 1/10 篇提供

**🌟 Highlight**: 7 篇 | **📌 Poster**: 3 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. Long-Horizon Manipulation via Trace-Conditioned VLA Planning

- **作者**: Isabella Liu, An-Chieh Cheng, Rui Yan, Geng Chen, Ri-Zhao Qiu, Xueyan Zou, Sha Yi, Hongxu Yin, Xiaolong Wang, Sifei Liu ⭐
  - **高亮作者**: Xiaolong Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.21924v1)
- **发表日期**: 2026-04-23
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2604.21924v1](http://arxiv.org/abs/2604.21924v1)
- **📥 PDF**: 已下载至本地 (`2604.21924v1_Long-Horizon_Manipulation_via_Trace-Conditioned_VLA_Planning.pdf`)
- **🔓 开源**: PROJECT_PAGE
- **中文摘要**: 长程操作对视觉-语言-动作（VLA）策略仍具挑战性：实际任务具有多步骤、依赖进度且易因执行错误累积而失败的特点。我们提出LoHo-Manip模块化框架，通过专用任务管理视觉语言模型（VLM），将短程VLA执行扩展至长程指令跟踪。该管理器与执行器解耦，采用递推式调用机制：基于当前观测，预测包含进度感知的剩余计划，该计划结合（i）子任务序列（含显式的已完成/待完成划分作为轻量语言记忆）与（ii）视觉轨迹——一种紧凑的2D关键点路径提示，指明下一步移动方向与接近目标。执行器VLA通过条件化渲染轨迹进行适配，从而将长程决策转化为通过轨迹跟踪实现的重复性局部控制。关键在于，每步预测剩余计划形成隐式闭环：失败步骤会持续影响后续输出，轨迹随之更新，实现无需人工设计恢复逻辑或脆弱视觉历史缓冲区的自动延续与重规划。在具身规划、长程推理、轨迹预测及仿真与真实Franka机器人端到端操作中的大量实验表明，该方法在长程成功率、鲁棒性及分布外泛化能力上均取得显著提升。项目页面：https://www.liuisabella.com/LoHoManip

---

### 2. X2-N: A Transformable Wheel-legged Humanoid Robot with Dual-mode Locomotion and Manipulation

- **作者**: Yan Ning, Xingzhou Chen, Delong Li, Hao Zhang, Hanfu Gai, Tongyuan Li, Cheng Zhang, Zhihui Peng, Ling Shi
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.21541v1)
- **发表日期**: 2026-04-23
- **匹配关键词**: locomotion and manipulation
- **arXiv**: [2604.21541v1](http://arxiv.org/abs/2604.21541v1)
- **📥 PDF**: 已下载至本地 (`2604.21541v1_X2-N_A_Transformable_Wheel-legged_Humanoid_Robot_with_Dual-mode_Locomotion_and_Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 轮腿机器人结合了轮式运动的高效性与腿式系统的多地形适应能力，能够在连续与离散地形上实现快速移动。然而，传统设计通常采用固定轮式足部且髋关节自由度有限，导致其腿式运动时的稳定性和机动性低于具有平足结构的人形机器人。此外，现有平台大多缺乏配备机械臂的完整上半身结构，限制了其执行灵巧操作任务的能力。

本文提出X2-N——一种具备双模式运动与操作能力的高自由度可变形机器人。该机器人可切换人形与轮腿两种形态，并通过关节重构实现无缝变形。我们进一步提出基于强化学习的全身控制框架，针对该形态特点实现混合运动、变形与操作任务的统一控制。通过动态滑行运动、爬楼梯及包裹递送等系列挑战性任务验证，X2-N展现出高运动效率、强地形适应能力及稳定的运动-操作协同性能，凸显其实际部署潜力。

---

### 3. From Noise to Intent: Anchoring Generative VLA Policies with Residual Bridges

- **作者**: Yiming Zhong, Yaoyu He, Zemin Yang, Pengfei Tian, Yifan Huang, Qingqiu Huang, Xinge Zhu, Yuexin Ma
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.21391v1)
- **发表日期**: 2026-04-23
- **匹配关键词**: VLA
- **arXiv**: [2604.21391v1](http://arxiv.org/abs/2604.21391v1)
- **📥 PDF**: 已下载至本地 (`2604.21391v1_From_Noise_to_Intent_Anchoring_Generative_VLA_Policies_with_Residual_Bridges.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 在具身智能领域，连接高层语义理解与底层物理控制始终是一个持续存在的挑战，其根源在于认知与行动之间存在根本性的时空尺度不匹配。现有生成式视觉-语言-动作（VLA）策略通常采用"从噪声生成"范式，该范式忽视了这一差异，导致优化过程中表征效率低下且条件对齐能力薄弱。本研究提出ResVLA架构，将范式转变为"从意图精炼"。基于机器人运动可自然分解为全局意图与局部动力学的认知，ResVLA利用频谱分析将控制解耦为确定性低频锚点与随机性高频残差。通过将生成过程锚定于预测的意图，我们的模型通过残差扩散桥严格聚焦于局部动力学的精炼。大量仿真实验表明，ResVLA在性能、对语言及机器人形态扰动的鲁棒性方面均达到竞争水平，且收敛速度快于标准生成基线模型。该架构在真实机器人实验中同样展现出优异性能。

---

### 4. A Replicable Robotics Awareness Method Using LLM-Enabled Robotics Interaction: Evidence from a Corporate Challenge

- **作者**: S. A. Prieto, M. A. Gopee, Y. Ben Arab, B. García de Soto, J. Esteba, P. Olivera Brizzio
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.21377v1)
- **发表日期**: 2026-04-23
- **匹配关键词**: human-robot collaboration
- **arXiv**: [2604.21377v1](http://arxiv.org/abs/2604.21377v1)
- **📥 PDF**: 已下载至本地 (`2604.21377v1_A_Replicable_Robotics_Awareness_Method_Using_LLM-Enabled_Robotics_Interaction_Evidence_from_a_Corpor.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 大型语言模型正越来越多地被探索作为人类与机器人系统之间的接口，但关于此类技术如何不仅用于交互，还能作为一种结构化手段，在真实组织环境中向非专业用户介绍机器人技术的证据仍然有限。本文介绍并评估了一种基于挑战的机器人认知方法，该方法通过由大型语言模型驱动的人形机器人活动在阿联酋AD Ports集团员工中实施。活动中，参与者在一个受物流启发的任务环境中，使用通过基于大型语言模型的控制框架解析的语音指令与人形机器人互动。该活动被设计为一种基于团队、角色驱动的体验，旨在让参与者在无需机器人专业知识的情况下接触具身人工智能和人机协作。为评估该方法，一项活动后调查开放了16天，收集了102份回复。结果表明整体接受度很高，满意度高（8.46/10），对机器人技术和人工智能的兴趣增加（4.47/5），以及对新兴人机协作形式的理解提升（4.45/5）。直接与机器人互动的参与者还报告了自然的交互体验（4.37/5），并强烈感受到随着活动进行交互变得更加容易（4.74/5）。同时，可靠性和可预测性方面的较低评分指出了未来迭代中重要的技术和设计挑战。研究结果表明，基于挑战、由大型语言模型驱动的人形机器人互动可以作为一种有前景且可复制的机器人认知方法，适用于工业和运营环境。

---

### 5. A Deployable Embodied Vision-Language Navigation System with Hierarchical Cognition and Context-Aware Exploration

- **作者**: Kuan Xu, Ruimeng Liu, Yizhuo Yang, Denan Liang, Tongxing Jin, Shenghai Yuan, Chen Wang, Lihua Xie ⭐
  - **高亮作者**: Chen Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.21363v1)
- **发表日期**: 2026-04-23
- **匹配关键词**: navigation, VLN, exploration
- **arXiv**: [2604.21363v1](http://arxiv.org/abs/2604.21363v1)
- **📥 PDF**: 已下载至本地 (`2604.21363v1_A_Deployable_Embodied_Vision-Language_Navigation_System_with_Hierarchical_Cognition_and_Context-Awar.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 弥合具身智能与嵌入式部署之间的差距，仍是智能机器人系统面临的关键挑战——感知、推理与规划必须在计算、内存、能耗及实时执行的严格约束下协同运作。在视觉语言导航（VLN）领域，现有方法往往面临强推理能力与真实平台高效部署之间的根本性权衡。本文提出一种可部署的具身VLN系统，在真实机器人平台上同时实现了高效性与稳健的高层推理能力。为此，我们将系统解耦为三个异步模块：用于连续环境感知的实时感知模块、用于空间语义聚合的记忆整合模块，以及用于高层决策的推理模块。我们通过增量构建认知记忆图来编码场景信息，并将其进一步分解为子图，从而支持视觉语言模型（VLM）的推理。为提升导航效率与精度，我们还利用认知记忆图将探索问题建模为上下文感知的加权旅行维修工问题（WTRP），该模型可最小化视点的加权等待时间。在仿真环境与真实机器人平台上的大量实验表明，相较于现有VLN方法，本系统在提升导航成功率和效率的同时，能够在资源受限硬件上保持实时性能。

---

### 6. How VLAs (Really) Work In Open-World Environments

- **作者**: Amir Rasouli, Yangzheng Wu, Zhiyuan Li, Rui Heng Yang, Xuan Zhao, Charles Eret, Sajjad Pakdamansavoji
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.21192v1)
- **发表日期**: 2026-04-23
- **匹配关键词**: vision-language-action model, vision-language-action, VLA
- **arXiv**: [2604.21192v1](http://arxiv.org/abs/2604.21192v1)
- **📥 PDF**: 已下载至本地 (`2604.21192v1_How_VLAs_(Really)_Work_In_Open-World_Environments.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作模型（VLAs）已广泛应用于机器人领域，在各类操作任务中取得了显著成功。近期，VLAs被用于长时域任务，并在BEHAVIOR1K（B1K）等基准测试中评估其解决复杂家务的能力。此类基准测试的常用评估指标是基于与过程无关的标准满足程度（即仅考虑物体的最终状态，而不关注导致该状态的事件）的成功率或部分得分。本文认为，采用此类评估协议不仅难以反映操作的安全性，还可能夸大报告性能，从而削弱未来实际部署中的核心挑战。为此，我们对B1K挑战赛中的前沿模型进行了深入分析，从性能的可复现性与一致性、策略操作的安全性、任务感知能力以及导致任务未完成的关键要素等维度评估策略的鲁棒性。进而提出能够捕捉安全违规行为的评估协议，以更准确地衡量策略在更复杂交互场景中的真实性能。最后，我们探讨了现有VLAs的局限性，并为未来研究提供了方向。

---

### 7. DualSplat: Robust 3D Gaussian Splatting via Pseudo-Mask Bootstrapping from Reconstruction Failures

- **作者**: Xu Wang, Zhiru Wang, Shiyun Xie, Chengwei Pan, Yisong Chen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.21631v1)
- **发表日期**: 2026-04-23
- **匹配关键词**: nerf, gaussian splatting, 3D gaussian splatting
- **arXiv**: [2604.21631v1](http://arxiv.org/abs/2604.21631v1)
- **📥 PDF**: 已下载至本地 (`2604.21631v1_DualSplat_Robust_3D_Gaussian_Splatting_via_Pseudo-Mask_Bootstrapping_from_Reconstruction_Failures.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 尽管3D高斯泼溅（3DGS）能够实现实时逼真渲染，但当训练图像包含破坏多视角一致性的瞬态物体时，其性能会显著下降。现有方法面临循环依赖问题：精确的瞬态检测需要良好重建的静态场景，而干净的重建本身又依赖于可靠的瞬态掩码。我们提出DualSplat——一种"失败转先验"框架，将首次重建的失败转化为第二次重建阶段的显式先验。我们观察到，仅出现在部分视角中的瞬态物体，在保守的初始训练过程中常表现为不完整碎片。通过结合光度残差、特征不匹配和SAM2实例边界，我们利用这些失败构建物体级伪掩码。这些伪掩码随后引导干净的二次3DGS优化，同时轻量级MLP通过从先验监督逐步过渡到自一致性来在线优化掩码。在RobustNeRF和NeRF On-the-go上的实验表明，DualSplat优于现有基线，尤其在瞬态密集场景和瞬态区域展现出显著优势。

---

## 📌 Poster

*其他相关研究*

---

### 1. SLAM as a Stochastic Control Problem with Partial Information: Optimal Solutions and Rigorous Approximations

- **作者**: Ilir Gusija, Fady Alajaji, Serdar Yüksel
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.21693v1)
- **发表日期**: 2026-04-23
- **匹配关键词**: localization and mapping, exploration
- **arXiv**: [2604.21693v1](http://arxiv.org/abs/2604.21693v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 同时定位与地图构建（SLAM）是机器人学中一项基础的状态估计问题，要求机器人在构建环境地图的同时，精准确定自身在该地图中的位置。本文通过最优随机控制的视角研究主动SLAM问题，将其重新表述为部分信息下的决策问题。在回顾若干常见模型后，我们提出主动SLAM的通用随机控制公式，并对运动、感知与地图表示进行严格处理。针对信息采集动作的评估，我们引入一种新的探索阶段代价函数，该函数能够编码状态几何特征。这一公式被构建为非标准的部分可观测马尔可夫决策过程（POMDP），随后通过分析推导出具有严格理论依据的近似最优解。为支撑该分析，我们在适用于广泛机器人应用的通用假设下，研究了相关的正则性条件。针对特定案例，我们开展了大规模数值研究，利用标准学习算法学习近最优策略。

---

### 2. Full-Body Dynamic Safety for Robot Manipulators: 3D Poisson Safety Functions for CBF-Based Safety Filters

- **作者**: Meg Wilkinson, Gilbert Bahati, Ryan M. Bena, Emily Fourney, Joel W. Burdick, Aaron D. Ames
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.21189v1)
- **发表日期**: 2026-04-23
- **匹配关键词**: HRI
- **arXiv**: [2604.21189v1](http://arxiv.org/abs/2604.21189v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 机械臂避碰需要在高维构型空间中强制执行全身安全约束。基于控制障碍函数的安全滤波器已被证明能有效实现安全行为，但执行安全操作所需的大量约束条件会带来理论和计算上的挑战。本文提出了一种利用三维泊松安全函数实现动态环境中机械臂全身避碰的框架。具体而言，根据环境占用数据，我们以指定分辨率对机械臂表面进行采样，并通过庞特里亚金差分法根据该分辨率收缩自由空间。在此缓冲域上，通过求解泊松方程合成全局光滑的控制障碍函数，从而为整个环境生成单一安全函数。该安全函数在每个采样点处的评估值，通过多约束二次规划由实时安全滤波器生成任务空间控制障碍函数约束。我们证明，在缓冲区域内保持采样点安全即可保证整个连续机械臂表面的避碰性能。该框架在动态环境中的七自由度机械臂上得到了验证。

---

### 3. Task-specific Subnetwork Discovery in Reinforcement Learning for Autonomous Underwater Navigation

- **作者**: Yi-Ling Liu, Melvin Laux, Mariela De Lucas Alvarez, Frank Kirchner, Rebecca Adam
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.21640v1)
- **发表日期**: 2026-04-23
- **匹配关键词**: navigation
- **arXiv**: [2604.21640v1](http://arxiv.org/abs/2604.21640v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 自主水下航行器需要在动态、不确定的环境和有限的感知条件下，以可解释的方式自适应地执行多种任务，这是传统控制器难以应对的挑战。这要求具备鲁棒性、泛化能力且内在可解释的控制策略，以实现可靠的长期监测。强化学习，特别是多任务强化学习，通过利用共享表征实现跨任务和跨环境的高效适应，克服了这些局限。然而，尽管此类策略在仿真和受控实验中展现出良好效果，但其内部决策过程仍不透明，对智能体决策机制的理解有限，导致在透明度、可信度和安全性方面存在不足，阻碍了实际部署。其内部策略结构和任务特定专业化机制尚不明确。为弥补这些不足，我们通过识别并比较HoloOcean水下导航仿真器中预训练多任务强化学习网络中负责导航至不同物种的任务特定子网络，分析了其内部结构。研究发现，在相关任务的上下文多任务强化学习设置中，网络仅使用约1.5%的权重来区分不同任务。其中，约85%的权重连接输入层中的上下文变量节点与下一隐藏层，凸显了上下文变量在此类设置中的重要性。我们的方法揭示了共享与专业化网络组件的特性，有助于通过上下文多任务强化学习方法实现水下监测中的高效模型编辑、迁移学习和持续学习。

---

