# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-05-03 08:01

**今日新增**: 10 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 2/10 篇提供

**🌟 Highlight**: 5 篇 | **📌 Poster**: 5 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. LaST-R1: Reinforcing Action via Adaptive Physical Latent Reasoning for VLA Models

- **作者**: Hao Chen, Jiaming Liu, Zhonghao Yan, Nuowei Han, Renrui Zhang, Chenyang Gu, Jialin Gao, Ziyu Guo, Siyuan Qian, Yinxi Wang, Peng Jia, Chi-Wing Fu, Shanghang Zhang, Pheng-Ann Heng
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.28192v1)
- **发表日期**: 2026-04-30
- **匹配关键词**: exploration, vision-language-action, VLA
- **arXiv**: [2604.28192v1](http://arxiv.org/abs/2604.28192v1)
- **📥 PDF**: 已下载至本地 (`2604.28192v1_LaST-R1_Reinforcing_Action_via_Adaptive_Physical_Latent_Reasoning_for_VLA_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型越来越多地融入推理机制以应对复杂机器人操作任务。然而，现有方法存在一个关键局限：无论是采用存在延迟和离散化问题的显式语言推理，还是利用更具表达力的连续潜在推理，它们都主要局限于静态模仿学习，限制了适应性和泛化能力。虽然在线强化学习（RL）已被引入VLA以实现试错探索，但当前方法仅优化原始动作空间，绕过了底层的物理推理过程。本文提出\textbf{LaST-R1}，一个统一的VLA框架，在动作执行前整合了基于物理动力学的潜在思维链（CoT）推理，并配套设计了专门的RL后训练范式。具体而言，我们提出\textbf{潜在到动作策略优化（LAPO）}，一种联合优化潜在推理过程与动作生成的新型RL算法。通过桥接推理与控制，LAPO改进了物理世界建模的表征能力，并增强了交互环境中的鲁棒性。此外，引入\textbf{自适应潜在CoT机制}，使策略能根据环境复杂度动态调整推理深度。大量实验表明，LaST-R1在仅需一次监督预热的情况下，在LIBERO基准上实现了近乎完美的99.8%平均成功率，显著提升了收敛速度与性能，超越此前最优方法。在实际部署中，LAPO后训练在四个复杂任务（包括单臂与双臂场景）上相比初始预热策略最高提升44%。最后，LaST-R1在仿真与真实环境中均展现出强大的泛化能力。

---

### 2. MotuBrain: An Advanced World Action Model for Robot Control

- **作者**: MotuBrain Team, Chendong Xiang, Fan Bao, Haitian Liu, Hengkai Tan, Hongzhe Bi, James Li, Jiabao Liu, Jingrui Pang, Kiro Jing, Louis Liu, Mengchen Cai, Rongxu Cui, Ruowen Zhao, Runqing Wang, Shuhe Huang, Yao Feng, Yinze Rong, Zeyuan Wang, Jun Zhu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.27792v1)
- **发表日期**: 2026-04-30
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2604.27792v1](http://arxiv.org/abs/2604.27792v1)
- **📥 PDF**: 已下载至本地 (`2604.27792v1_MotuBrain_An_Advanced_World_Action_Model_for_Robot_Control.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型具备强大的语义泛化能力，但往往缺乏对世界动力学的细粒度建模。近期研究探索将视频生成模型作为世界建模的基础，从而催生了统一的世界动作模型（WAMs），该模型能够联合建模视觉动态与动作。我们提出MotuBrain——一个统一的多模态生成模型，基于UniDiffuser框架与三流混合Transformer架构，实现视频与动作的联合建模。该单一模型支持多种推理模式，包括策略学习、世界建模、视频生成、逆动力学建模以及视频-动作联合预测，同时可扩展至异构多模态数据（如纯视频数据与跨具身机器人数据）。为提升实际应用能力，MotuBrain引入了统一的多视角表征、显式语言-动作耦合机制以及高效推理栈，在实时部署中实现了超过50倍的加速效果。

---

### 3. Robot Learning from Human Videos: A Survey

- **作者**: Junyi Ma, Erhang Zhang, Haoran Yang, Ditao Li, Chenyang Xu, Guangming Wang, Hesheng Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.27621v1)
- **发表日期**: 2026-04-30
- **匹配关键词**: VLA
- **arXiv**: [2604.27621v1](http://arxiv.org/abs/2604.27621v1)
- **📥 PDF**: 已下载至本地 (`2604.27621v1_Robot_Learning_from_Human_Videos_A_Survey.pdf`)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/IRMVLab/awesome-robot-learning-from-human-videos.
- **中文摘要**: 制约具身智能与机器人领域进一步发展的关键瓶颈在于机器人数据规模化扩展的挑战。为解决这一问题，近年来，受人类活动视频的丰富性及计算机视觉技术进步的驱动，从人类视频数据中学习机器人操作技能的研究方向迅速获得关注。该研究方向有望使机器人能够从海量且易于获取的人类演示资源中被动习得技能，从而显著促进通用型机器人系统的可扩展学习。为此，本文通过综述全面且系统地梳理了机器人领域中基于人类视频的学习技术，重点关注人-机器人技能迁移与数据基础两大维度。我们首先回顾了机器人策略学习的基础理论，继而阐述了融合人类视频的基本接口。随后，我们构建了将人类视频迁移至机器人技能的层级化分类体系，涵盖任务导向、观测导向与动作导向三类路径，并跨家族分析了其与不同数据配置及学习范式的耦合关系。此外，我们深入探究了数据基础，包括广泛使用的人类视频数据集与视频生成方案，并提供了数据集开发与利用的大规模统计趋势。最后，我们着重强调了该领域固有的挑战与局限性，并勾勒了未来研究的潜在方向。本综述的论文列表可访问 https://github.com/IRMVLab/awesome-robot-learning-from-human-videos 获取。

---

### 4. PRTS: A Primitive Reasoning and Tasking System via Contrastive Representations

- **作者**: Yang Zhang, Jiangyuan Zhao, Chenyou Fan, Fangzheng Yan, Tian Li, Haitong Tang, Sen Fu, Xuan'er Wu, Qizhen Weng, Weinan Zhang, Xiu Li, Chi Zhang, Chenjia Bai, Xuelong Li
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.27472v1)
- **发表日期**: 2026-04-30
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2604.27472v1](http://arxiv.org/abs/2604.27472v1)
- **📥 PDF**: 已下载至本地 (`2604.27472v1_PRTS_A_Primitive_Reasoning_and_Tasking_System_via_Contrastive_Representations.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型通过强大的视觉-语言先验知识推动了机器人控制技术的发展。然而，现有VLA模型主要将预训练框架化为监督式行为克隆，忽视了机器人学习的本质——这是一个需要理解时间任务进度的目标达成过程。我们提出**PRTS**（**P**rimitive **R**easoning and **T**asking **S**ystem，原始推理与任务系统），这是一种通过目标条件强化学习重构预训练的VLA基础模型。通过将语言指令视为目标并采用对比强化学习，PRTS学习到一个统一的嵌入空间，其中状态-动作嵌入与目标嵌入的内积近似于对数折扣目标占用率——即从当前状态-动作达到语言指定目标的概率，从而在静态语义匹配之外定量评估物理可行性。PRTS直接从离线轨迹中提取这种密集的目标可达性监督信号，无需奖励标注，并通过角色感知因果掩码将其融入VLM骨干网络，相比原始行为克隆仅增加可忽略的额外开销。这一范式赋予高层推理系统内在的目标可达性感知能力，桥接了语义推理与时间任务进度，并进一步促进目标条件动作预测。通过在167B token的多样化操作与具身推理数据上预训练，PRTS在LIBERO、LIBERO-Pro、LIBERO-Plus、SimplerEnv以及包含14个复杂任务的真实世界套件中达到最先进性能，尤其在长时域、高接触和零样本新指令场景下取得显著提升，证实注入目标可达性感知能显著提升通用机器人基础策略的执行成功率与长时域规划能力。

---

### 5. Sparse-View 3D Gaussian Splatting in the Wild

- **作者**: Wongi Park, Jordan A. James, Myeongseok Nam, Minjae Lee, Soomok Lee, Sang-Hyun Lee, William J. Beksi
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.27422v1)
- **发表日期**: 2026-04-30
- **匹配关键词**: 3D gaussian splatting, gaussian splatting
- **arXiv**: [2604.27422v1](http://arxiv.org/abs/2604.27422v1)
- **📥 PDF**: 已下载至本地 (`2604.27422v1_Sparse-View_3D_Gaussian_Splatting_in_the_Wild.pdf`)
- **🔓 开源**: PROJECT_PAGE, CODE
  - 链接：https://robotic-vision-lab.github.io/SaveWildGS/
- **中文摘要**: 我们提出了一种面向包含干扰物的无约束真实场景的三维稀疏视角合成框架。现有方法主要从无瞬态元素的稀疏约束图像集合进行新视角合成，或利用无约束密集图像集合增强真实场景的三维表示，而我们的方法不仅能有效处理稀疏无约束图像集合，还能呈现高质量的三维渲染结果。为此，我们引入基于扩散模型的参考引导视角优化技术，通过瞬态掩码和参考图像增强三维表示并减少渲染视角中的伪影。此外，我们通过伪视角生成结合稀疏感知高斯复制策略，对高斯场中的稀疏区域进行增强，以放大稀疏区域的高斯分布。在公开数据集上的大量实验表明，我们的方法始终优于现有方法（例如PSNR提升17.2%，SSIM提升10.8%，LPIPS降低4.0%），并生成高保真三维渲染结果。这一进展为无需繁重数据采集即可实现无约束真实场景的渲染铺平了道路。项目页面请访问：$\href{https://robotic-vision-lab.github.io/SaveWildGS/}{此处}$

---

## 📌 Poster

*其他相关研究*

---

### 1. OmniRobotHome: A Multi-Camera Platform for Real-Time Multiadic Human-Robot Interaction

- **作者**: Junyoung Lee, Sookwan Han, Jeonghwan Kim, Inhee Lee, Mingi Choi, Jisoo Kim, Wonjung Woo, Hanbyul Joo
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.28197v1)
- **发表日期**: 2026-04-30
- **匹配关键词**: human-robot interaction, human-robot collaboration
- **arXiv**: [2604.28197v1](http://arxiv.org/abs/2604.28197v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 人机协作的研究主要集中在二元或顺序协作场景中。然而，真实家庭环境需要多元协作——多个人类与机器人共享工作空间，在紧密的空间与时间耦合下并行执行交错子任务。这一模式尚未得到充分探索，因为人类、机器人与物体之间的近距离交互会产生持续遮挡和快速状态变化，使得可靠的实时三维追踪成为核心瓶颈。现有平台均无法提供实现该模式实验可操作所需的实时、抗遮挡、房间级感知能力。我们提出OmniRobotHome——首个将广域实时三维人体与物体感知、多机器人协调驱动统一于共享世界坐标系的房间级住宅平台。该系统在自然家居环境中部署48台硬件同步RGB相机，实现无标记、抗遮挡的多人体与物体追踪，并与两台基于实时场景状态运行的Franka机械臂保持时间对齐。在此一致坐标系下的连续捕捉，还能从累积轨迹中支持长时程人类行为建模。该平台使多元协作模式具备实验可操作性。我们聚焦两大核心问题：人机共享空间的安全性与人类预判型机器人辅助，并证明实时感知与累积行为记忆均能为两者带来可量化的性能提升。

---

### 2. Learning-Based Hierarchical Scene Graph Matching for Robot Localization Leveraging Prior Maps

- **作者**: Nimrod Millenium Ndulue, Jose Andres Millan-Romera, Matteo Giorgi, Holger Voos, Jose Luis Sanchez-Lopez
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.27821v1)
- **发表日期**: 2026-04-30
- **匹配关键词**: scene graph
- **arXiv**: [2604.27821v1](http://arxiv.org/abs/2604.27821v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 精确的定位是室内自主机器人运行的基本要求。场景图将环境的空间结构编码为语义实体及其关系的层次结构，既可以通过机器人传感器数据在线构建，也可以从建筑信息模型（BIM）等先验知识离线生成。匹配这两种互补的表示形式，能够通过将机器人观测结果与已知结构先验进行对齐，实现SLAM中的漂移校正。然而，在两者之间建立可靠的节点到节点对应关系仍是一个开放性挑战：现有的组合方法在大规模场景下计算成本过高，而先前的学习方法仅处理平面图匹配，忽略了两种表示中存在的多层次语义结构。本文提出一种可学习的端到端可微分流水线，通过为两种图结构添加基于语义的边类型（编码层内与层间关系），显式利用这种层次结构实现从高层房间概念到低层墙面表面的同步匹配。该方法仅基于平面图进行训练，在真实激光雷达环境中的F1分数上优于组合基线方法，同时运行速度快一个数量级，证明了其在BIM辅助机器人定位中具有可行的零样本泛化能力。

---

### 3. Can Tabular Foundation Models Guide Exploration in Robot Policy Learning?

- **作者**: Buqing Ou, Frederike Dümbgen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.27667v1)
- **发表日期**: 2026-04-30
- **匹配关键词**: exploration
- **arXiv**: [2604.27667v1](http://arxiv.org/abs/2604.27667v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 机器人高维连续控制中的策略优化仍是一个具有挑战性的问题。主流方法本质上是局部的，通常需要大量调参和精心选择的初始猜测才能获得良好性能，而更具全局性且对初始化不敏感的搜索方法往往会产生高昂的 rollout 成本。我们提出 TFM-S3，一种表格化混合局部-全局方法，用于在有限 rollout 成本下提升机器人策略学习中的全局探索能力。我们将高频局部更新与间歇性全局搜索轮次交替进行。在每个搜索轮次中，我们通过奇异值分解构建动态更新的低维策略子空间，并在该空间内执行迭代代理引导优化。预训练的表格化基础模型可根据少量上下文集预测候选回报，从而在有限 rollout 成本下实现大规模筛选。在连续控制基准上的实验表明，与 TD3 和基于种群的基线方法相比，在相同 rollout 预算下，TFM-S3 持续加速了早期收敛并提升了最终性能。这些结果表明，基础模型是创建机器人连续控制中样本高效策略学习方法的有力新工具。

---

### 4. SASI: Leveraging Sub-Action Semantics for Robust Early Action Recognition in Human-Robot Interaction

- **作者**: Yongpeng Cao, Masahiro Hirano, Hyuno Kim, Yuji Yamakawa
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.27508v1)
- **发表日期**: 2026-04-30
- **匹配关键词**: human-robot interaction, HRI
- **arXiv**: [2604.27508v1](http://arxiv.org/abs/2604.27508v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 理解人类行为对于推进人机交互中的行为分析至关重要。特别是在需要快速主动反馈的任务中，机器人必须从非完整的观测中尽早识别人类行为。由于人类行为本质上是结构化的，可以分解为更小、有意义的单元，因此子行为为此提供了所需的语义和层次化线索。然而，传统方法主要关注整体行为，往往忽略了子行为中蕴含的丰富语义结构，导致其难以适用于早期识别。为解决这一问题，我们提出了SASI（子行为语义集成跨模态融合）框架——一种将现有图卷积网络与子行为语义融合的新型框架，用于整合时空特征。SASI利用分割模型与基于骨架的传统图卷积网络，在29赫兹的实时运行频率下，既能捕捉细粒度的子行为语义，又能保留整体空间上下文。在具有帧级标注的骨架数据集BABEL上的实验表明，我们的方法相比传统方法提升了识别准确率，且随着子行为分割质量的提高，性能有望进一步提升。值得注意的是，SASI在理解部分动作序列方面也展现出卓越性能，揭示了其早期识别能力——这对于实现主动且无缝的人机交互至关重要。代码已开源：https://anonymous.4open.science/r/SASI

---

### 5. RAY-TOLD: Ray-Based Latent Dynamics for Dense Dynamic Obstacle Avoidance with TDMPC

- **作者**: Seungho Han, Seokju Lee, Jeonguk Kang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.27450v1)
- **发表日期**: 2026-04-30
- **匹配关键词**: navigation, obstacle avoidance
- **arXiv**: [2604.27450v1](http://arxiv.org/abs/2604.27450v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 密集、动态的人群对自主移动机器人构成了持续的挑战。纯反应式规划方法（如模型预测路径积分控制）因其有限的预测范围，在复杂场景中往往无法摆脱局部最优解。为解决这一问题，我们提出了基于射线的任务导向潜在动力学（RAY-TOLD）混合控制架构，该架构将障碍物信息整合到潜在动力学中，并利用基于物理的MPPI的鲁棒性与强化学习的长期前瞻能力。RAY-TOLD采用以激光雷达为中心的潜在动力学模型，将高维传感器数据编码为紧凑的状态表示，从而学习终端价值函数和策略先验。我们引入了一种策略混合采样策略，通过从学习到的策略中衍生出的轨迹来扩充MPPI候选种群，在保持运动学可行性的同时有效引导规划器朝向目标。在具有高密度动态障碍物的随机环境中的大量测试表明，我们的方法优于MPPI基线，降低了碰撞率。结果证实，将短视的基于物理的轨迹展开与学习到的长期意图相结合，显著提升了导航的可靠性和安全性。

---

