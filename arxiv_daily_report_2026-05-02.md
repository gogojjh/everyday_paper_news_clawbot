# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-05-02 08:03

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 2/20 篇提供

**🌟 Highlight**: 11 篇 | **📌 Poster**: 9 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. LaST-R1: Reinforcing Action via Adaptive Physical Latent Reasoning for VLA Models

- **作者**: Hao Chen, Jiaming Liu, Zhonghao Yan, Nuowei Han, Renrui Zhang, Chenyang Gu, Jialin Gao, Ziyu Guo, Siyuan Qian, Yinxi Wang, Peng Jia, Chi-Wing Fu, Shanghang Zhang, Pheng-Ann Heng
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.28192v1)
- **发表日期**: 2026-04-30
- **匹配关键词**: vision-language-action, exploration, VLA
- **arXiv**: [2604.28192v1](http://arxiv.org/abs/2604.28192v1)
- **📥 PDF**: 已下载至本地 (`2604.28192v1_LaST-R1_Reinforcing_Action_via_Adaptive_Physical_Latent_Reasoning_for_VLA_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型越来越多地融入推理机制以完成复杂机器人操作任务。然而现有方法存在一个关键局限：无论是采用存在延迟和离散化问题的显式语言推理，还是利用更具表达力的连续潜在推理，它们都主要局限于静态模仿学习，限制了适应性和泛化能力。虽然在线强化学习（RL）已被引入VLA以实现试错探索，但当前方法仅优化原始动作空间，绕过了底层的物理推理过程。本文提出\textbf{LaST-R1}——一个统一的VLA框架，该框架在执行动作前整合了基于物理动力学的潜在思维链（CoT）推理，并配套设计了定制化RL后训练范式。具体而言，我们提出\textbf{潜在到动作策略优化（LAPO）}，这是一种联合优化潜在推理过程与动作生成的新型RL算法。通过桥接推理与控制，LAPO改进了物理世界建模的表征能力，增强了交互环境中的鲁棒性。此外，我们引入\textbf{自适应潜在CoT机制}，使策略能够根据环境复杂度动态调整推理深度。大量实验表明，LaST-R1在仅需一次监督预热的情况下，在LIBERO基准测试中实现了近乎完美的99.8%平均成功率，显著提升了收敛速度与性能，超越此前最优方法。在实际部署中，LAPO后训练在包含单臂和双臂设置的四个复杂任务上，相较于初始预热策略实现了最高44%的性能提升。最后，LaST-R1在仿真与真实环境中均展现出强大的泛化能力。

---

### 2. MotuBrain: An Advanced World Action Model for Robot Control

- **作者**: MotuBrain Team, Chendong Xiang, Fan Bao, Haitian Liu, Hengkai Tan, Hongzhe Bi, James Li, Jiabao Liu, Jingrui Pang, Kiro Jing, Louis Liu, Mengchen Cai, Rongxu Cui, Ruowen Zhao, Runqing Wang, Shuhe Huang, Yao Feng, Yinze Rong, Zeyuan Wang, Jun Zhu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.27792v1)
- **发表日期**: 2026-04-30
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2604.27792v1](http://arxiv.org/abs/2604.27792v1)
- **📥 PDF**: 已下载至本地 (`2604.27792v1_MotuBrain_An_Advanced_World_Action_Model_for_Robot_Control.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型在语义泛化方面表现优异，但往往缺乏对世界动态的细粒度建模。近期研究探索将视频生成模型作为世界建模的基础，从而催生了统一的世界动作模型（WAMs），该模型可联合建模视觉动态与动作。我们提出MotuBrain——一个统一的多模态生成模型，基于UniDiffuser框架与三流混合Transformer架构，联合建模视频与动作。单一模型支持多种推理模式，包括策略学习、世界建模、视频生成、逆动力学建模以及联合视频-动作预测，同时可扩展至异构多模态数据（如纯视频数据与跨具身机器人数据）。为提升实际应用能力，MotuBrain引入了统一的多视角表征、显式语言-动作耦合机制以及高效推理栈，在实时部署中实现了超过50倍的加速效果。

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
- **中文摘要**: 制约具身智能与机器人技术进一步发展的关键瓶颈在于机器人数据规模化扩展的挑战。为应对这一难题，近年来，受人类活动视频的丰富性及计算机视觉技术进步的驱动，从人类视频数据中学习机器人操作技能的研究方向迅速获得关注。该研究路线有望使机器人能够从海量易得的人类演示资源中被动习得技能，从而显著促进通用型机器人系统的可扩展学习。为此，本综述旨在全面且及时地梳理机器人领域基于人类视频的学习技术，重点关注人机技能迁移与数据基础两大维度。我们首先回顾机器人策略学习的基础理论，继而阐述整合人类视频的基本接口。随后，我们提出将人类视频迁移至机器人技能的分层分类体系，涵盖任务导向、观测导向与动作导向三大路径，并跨家族分析其与不同数据配置及学习范式的耦合关系。此外，我们深入探讨数据基础，包括广泛使用的人类视频数据集与视频生成方案，并提供数据集开发与利用的大规模统计趋势。最后，我们强调该领域固有的挑战与局限，并勾勒未来研究的潜在方向。本综述的论文列表详见 https://github.com/IRMVLab/awesome-robot-learning-from-human-videos。

---

### 4. PRTS: A Primitive Reasoning and Tasking System via Contrastive Representations

- **作者**: Yang Zhang, Jiangyuan Zhao, Chenyou Fan, Fangzheng Yan, Tian Li, Haitong Tang, Sen Fu, Xuan'er Wu, Qizhen Weng, Weinan Zhang, Xiu Li, Chi Zhang, Chenjia Bai, Xuelong Li
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.27472v1)
- **发表日期**: 2026-04-30
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2604.27472v1](http://arxiv.org/abs/2604.27472v1)
- **📥 PDF**: 已下载至本地 (`2604.27472v1_PRTS_A_Primitive_Reasoning_and_Tasking_System_via_Contrastive_Representations.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型通过强大的视觉-语言先验知识推动了机器人控制的发展。然而，现有VLA主要将预训练框架化为监督式行为克隆，忽视了机器人学习的本质——即作为需要理解时间任务进度的目标达成过程。我们提出**PRTS**（**P**rimitive **R**easoning and **T**asking **S**ystem，原始推理与任务系统），这是一个通过目标条件强化学习重构预训练的VLA基础模型。通过将语言指令视为目标并采用对比强化学习，PRTS学习了一个统一的嵌入空间，其中状态-动作与目标嵌入的内积近似于对数折扣目标占用率——即从当前状态-动作达到语言指定目标的概率，从而在静态语义匹配之外定量评估物理可行性。PRTS直接从离线轨迹中提取这种密集的目标可达性监督信号，无需奖励标注，并通过角色感知因果掩码将其融入VLM骨干网络，相较于普通行为克隆仅增加极小的计算开销。该范式赋予高层推理系统内在的目标可达性感知能力，桥接了语义推理与时间任务进度，并进一步促进目标条件动作预测。通过在167B token的多样化操作与具身推理数据上预训练，PRTS在LIBERO、LIBERO-Pro、LIBERO-Plus、SimplerEnv以及包含14个复杂任务的真实世界测试套件中达到最先进性能，尤其在长时域、高接触和零样本新指令场景中取得显著提升，证实注入目标可达性感知能显著提升通用机器人基础策略的执行成功率和长时域规划能力。

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
- **中文摘要**: 我们提出了一种面向包含干扰物的无约束真实场景的三维稀疏视角合成框架。与现有方法主要从无瞬态元素的稀疏约束图像进行新视角合成，或利用无约束密集图像集合增强真实场景三维表征不同，我们的方法不仅能有效处理稀疏无约束图像集合，还能呈现高质量的三维渲染结果。为此，我们引入基于扩散模型的参考引导视角优化技术，通过瞬态掩码和参考图像增强三维表征并减少渲染视角中的伪影。此外，我们通过伪视角生成结合稀疏感知高斯复制策略，解决高斯场中的稀疏区域问题，从而放大稀疏区域的高斯分布。在公开数据集上的大量实验表明，我们的方法始终优于现有方法（例如PSNR提升17.2%，SSIM提升10.8%，LPIPS降低4.0%），并实现高保真三维渲染结果。这一进展为无需繁重数据采集即可实现无约束真实场景的渲染铺平了道路。项目页面详见：$\href{https://robotic-vision-lab.github.io/SaveWildGS/}{此处}$

---

### 6. Bi-Level Optimization for Contact and Motion Planning in Rope-Assisted Legged Robots

- **作者**: Ruben Malacarne, Ioannis Tsikelis, Enrico Mingo Hoffman, Michele Focchi
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.26910v1)
- **发表日期**: 2026-04-29
- **匹配关键词**: motion planning
- **arXiv**: [2604.26910v1](http://arxiv.org/abs/2604.26910v1)
- **📥 PDF**: 已下载至本地 (`2604.26910v1_Bi-Level_Optimization_for_Contact_and_Motion_Planning_in_Rope-Assisted_Legged_Robots.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 本文提出了一种用于绳索辅助机器人攀爬垂直表面的运动规划框架。该框架采用双层优化方案，旨在解决混合整数问题：在优化控制输入（即绳索张力与腿部作用力）及着陆位置的同时，选择可行的地形着陆区域。外层优化通过交叉熵方法求解，内层优化则基于梯度非线性优化计算动态可行运动。该方法的有效性在新型攀爬机器人平台ALPINE上得到了验证，并针对多种复杂地形构型进行了测试。

---

### 7. Safe Navigation using Neural Radiance Fields via Reachable Sets

- **作者**: Omanshu Thapliyal, Malarvizhi Sankaranarayanasamy, Ravigopal Vennelakanti
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.26899v1)
- **发表日期**: 2026-04-29
- **匹配关键词**: nerf, neural radiance field, path planning, navigation
- **arXiv**: [2604.26899v1](http://arxiv.org/abs/2604.26899v1)
- **📥 PDF**: 已下载至本地 (`2604.26899v1_Safe_Navigation_using_Neural_Radiance_Fields_via_Reachable_Sets.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 在杂乱环境中实现安全导航是自主系统面临的重要挑战。当机器人穿越布满障碍物的场景时，需要能够安全地应对不同几何形状的障碍物、目标物及自车物体。本研究利用状态空间中机器人实时能力的可达集表示来捕捉安全导航需求，同时采用神经辐射场（NeRF）按需计算、存储和操控障碍物或自车的体积表示。通过约束最优控制方法构建路径规划问题，其中包含线性矩阵不等式约束。我们展示了两种不同场景下存在大量障碍物时的路径规划仿真结果，并通过在相应约束最优控制问题中应用可达集验证了安全导航的有效性。

---

### 8. STARRY: Spatial-Temporal Action-Centric World Modeling for Robotic Manipulation

- **作者**: Yuxuan Tian, Yurun Jin, Bin Yu, Yukun Shi, Hao Wu, Chi Harold Liu, Kai Chen, Cong Huang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.26848v1)
- **发表日期**: 2026-04-29
- **匹配关键词**: VLA
- **arXiv**: [2604.26848v1](http://arxiv.org/abs/2604.26848v1)
- **📥 PDF**: 已下载至本地 (`2604.26848v1_STARRY_Spatial-Temporal_Action-Centric_World_Modeling_for_Robotic_Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 机器人操作的关键在于对未来时空交互进行推理，然而现有的VLA策略和世界模型增强策略并未充分建模与动作相关的时空交互结构。我们提出STARRY——一种世界模型增强的动作生成策略，该策略将时空预测与动作生成对齐。STARRY联合去噪未来时空潜在表征与动作序列，并引入几何感知选择性注意力调制机制，将预测的深度信息与末端执行器几何结构转化为令牌对齐的权重，用于选择性动作注意力调制。在RoboTwin 2.0基准测试中，STARRY在干净环境和随机环境下分别达到93.82%和93.30%的平均成功率。真实世界实验进一步将平均成功率从$π_{0.5}$的42.5%提升至70.8%，验证了以动作为中心的时空世界建模对高时空需求机器人动作生成的有效性。

---

### 9. Walk With Me: Long-Horizon Social Navigation for Human-Centric Outdoor Assistance

- **作者**: Lingfeng Zhang, Xiaoshuai Hao, Xizhou Bu, Yingbo Tang, Hongsheng Li, Jinghui Lu, Xiu-shen Wei, Jiayi Ma, Yu Liu, Jing Zhang, Hangjun Ye, Xiaojun Liang, Long Chen, Wenbo Ding
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.26839v1)
- **发表日期**: 2026-04-29
- **匹配关键词**: VLA, vision-language-action, social navigation, navigation
- **arXiv**: [2604.26839v1](http://arxiv.org/abs/2604.26839v1)
- **📥 PDF**: 已下载至本地 (`2604.26839v1_Walk_With_Me_Long-Horizon_Social_Navigation_for_Human-Centric_Outdoor_Assistance.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 在开放世界户外环境中辅助人类，要求机器人将高级自然语言意图转化为安全、长时域且符合社交规范的导航行为。现有基于地图的方法依赖成本高昂的预建高精地图，而基于学习的策略大多局限于室内和短时域场景。为弥合这一差距，我们提出"与我同行"（Walk with Me）框架——一种无需地图、基于高级人类指令实现长时域社交导航的方案。该框架利用GPS上下文和公共地图API提供的轻量级候选兴趣点，实现语义目的地定位与路径点生成。高级视觉语言模型将抽象指令转化为具体目的地并规划粗略路径点序列。在执行过程中，基于观测感知的路由机制判定低级视觉-语言-动作策略能否应对当前情境，或是否需要高级视觉语言模型进行显式安全推理。常规路段由低级视觉-语言-动作策略执行，而拥挤路口等复杂场景则触发高级推理，在存在安全隐患时启动"停-等"行为。通过融合语义意图定位、无地图长时域规划、安全感知推理与低级动作生成，"与我同行"框架实现了以人为中心的实用化户外社交导航。

---

### 10. Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising

- **作者**: Jun Guo, Qiwei Li, Peiyan Li, Zilong Chen, Nan Sun, Yifei Su, Heyun Wang, Yuan Zhang, Xinghang Li, Huaping Liu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.26694v1)
- **发表日期**: 2026-04-29
- **匹配关键词**: 3D reconstruction, 3d reconstruction
- **arXiv**: [2604.26694v1](http://arxiv.org/abs/2604.26694v1)
- **📥 PDF**: 已下载至本地 (`2604.26694v1_Unified_4D_World_Action_Modeling_from_Video_Priors_with_Asynchronous_Denoising.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出X-WAM，一种统一的4D世界模型，将实时机器人动作执行与高保真4D世界合成（视频+3D重建）整合于单一框架中，解决了先前统一世界模型（如UWM）仅建模2D像素空间、无法平衡动作效率与世界建模质量的关键局限。为利用预训练视频扩散模型的强大视觉先验，X-WAM通过预测多视角RGB-D视频来想象未来世界，并通过轻量级结构适配高效获取空间信息：将预训练扩散Transformer的最后几个模块复制到专用深度预测分支中，用于重建未来空间信息。此外，我们提出异步噪声采样（ANS）以联合优化生成质量与动作解码效率。ANS在推理过程中采用专门的异步去噪调度，通过更少的步骤快速解码动作以实现高效实时执行，同时将完整步骤序列用于生成高保真视频。与训练期间完全解耦时间步不同，ANS从其联合分布中采样以对齐推理分布。X-WAM在超过5800小时机器人数据上预训练后，在RoboCasa和RoboTwin 2.0基准测试中分别达到79.2%和90.7%的平均成功率，同时生成的高保真4D重建与生成在视觉和几何指标上均超越现有方法。

---

### 11. HiPAN: Hierarchical Posture-Adaptive Navigation for Quadruped Robots in Unstructured 3D Environments

- **作者**: Jeil Jeong, Minsung Yoon, Seokryun Choi, Heechan Shin, Taegeun Yang, Sung-eui Yoon
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.26504v1)
- **发表日期**: 2026-04-29
- **匹配关键词**: obstacle avoidance, exploration, navigation
- **arXiv**: [2604.26504v1](http://arxiv.org/abs/2604.26504v1)
- **📥 PDF**: 已下载至本地 (`2604.26504v1_HiPAN_Hierarchical_Posture-Adaptive_Navigation_for_Quadruped_Robots_in_Unstructured_3D_Environments.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 在非结构化三维环境中引导四足机器人导航面临重大挑战，需要实现目标导向运动、有效探索以摆脱局部极小值，以及通过姿态调整穿越狭窄、高度受限空间。传统方法采用顺序建图-规划流程，但存在感知误差累积和计算开销大的问题，限制了其在资源受限平台上的适用性。为解决这些挑战，我们提出层次化姿态自适应导航框架（HiPAN），该框架可直接在部署时的机载深度图像上运行。HiPAN采用层次化设计：高层策略生成战略性导航指令（平面速度与身体姿态），由低层姿态自适应运动控制器执行。为缓解短视行为并促进长程导航，我们引入路径引导课程学习，逐步将导航范围从反应式避障扩展至战略性导航。仿真实验中，HiPAN相比经典反应式规划器和端到端基线方法实现了更高的导航成功率和路径效率，而真实世界实验进一步验证了其在多样化非结构化三维环境中的适用性。

---

## 📌 Poster

*其他相关研究*

---

### 1. OmniRobotHome: A Multi-Camera Platform for Real-Time Multiadic Human-Robot Interaction

- **作者**: Junyoung Lee, Sookwan Han, Jeonghwan Kim, Inhee Lee, Mingi Choi, Jisoo Kim, Wonjung Woo, Hanbyul Joo
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.28197v1)
- **发表日期**: 2026-04-30
- **匹配关键词**: human-robot collaboration, human-robot interaction
- **arXiv**: [2604.28197v1](http://arxiv.org/abs/2604.28197v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 人机协作的研究主要集中在二元或顺序交互场景中。然而，真实家庭环境需要多主体协作，即多个人类与机器人共享工作空间，在紧密的空间与时间耦合下，对交错子任务进行并行操作。这一领域尚未得到充分探索，因为人类、机器人与物体之间的近距离交互会产生持续遮挡和快速状态变化，使得可靠的实时三维追踪成为核心瓶颈。目前尚无平台能够提供实时、抗遮挡、房间尺度的感知能力，使该场景在实验中具备可操作性。我们提出OmniRobotHome——首个将广域实时三维人体与物体感知、多机器人协同驱动统一于共享世界坐标系的房间尺度住宅平台。该系统在自然家居环境中部署了48台硬件同步RGB相机，实现无标记、抗遮挡的多人体与物体追踪，并与两台基于实时场景状态运行的Franka机械臂保持时间同步。在该统一坐标系下的连续数据采集，进一步支持从累积轨迹中学习长时域人类行为模型。该平台使多主体协作场景具备实验可操作性。我们聚焦两大核心问题：人机共享空间的安全性与人类预判型机器人辅助，并证明实时感知与累积行为记忆均能在两方面带来可量化的性能提升。

---

### 2. Learning-Based Hierarchical Scene Graph Matching for Robot Localization Leveraging Prior Maps

- **作者**: Nimrod Millenium Ndulue, Jose Andres Millan-Romera, Matteo Giorgi, Holger Voos, Jose Luis Sanchez-Lopez
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.27821v1)
- **发表日期**: 2026-04-30
- **匹配关键词**: scene graph
- **arXiv**: [2604.27821v1](http://arxiv.org/abs/2604.27821v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 精确的定位是室内自主机器人运行的基本要求。场景图将环境的空间结构编码为语义实体及其关系的层次结构，既可以通过机器人传感器数据在线构建，也可以从建筑信息模型（BIM）等先验知识离线生成。通过将这两种互补的表征进行匹配，能够基于已知的结构先验对机器人观测数据进行校正，从而修正SLAM中的漂移误差。然而，在这两种表征之间建立可靠的节点对应关系仍是一个开放挑战：现有的组合方法在大规模场景中计算成本过高，而先前基于学习的方法仅处理平面图匹配，忽略了两种表征中存在的多层次语义结构。本文提出了一种可学习的端到端可微分流水线，通过为两种图结构添加基于语义的边类型（编码层内与层间关系），显式利用这种层次结构实现从高层房间概念到低层墙面表面的同步匹配。该方法仅使用平面图进行训练，在真实激光雷达环境中的F1指标上优于组合基线方法，同时运行速度快一个数量级，证明了其在BIM辅助机器人定位中具有可行的零样本泛化能力。

---

### 3. Can Tabular Foundation Models Guide Exploration in Robot Policy Learning?

- **作者**: Buqing Ou, Frederike Dümbgen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.27667v1)
- **发表日期**: 2026-04-30
- **匹配关键词**: exploration
- **arXiv**: [2604.27667v1](http://arxiv.org/abs/2604.27667v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 机器人学中高维连续控制的策略优化仍是一个具有挑战性的问题。主流方法本质上具有局部性，通常需要大量调参和精心选择的初始猜测才能获得良好性能，而更具全局性且对初始化不敏感的搜索方法往往会产生高昂的 rollout 成本。我们提出 TFM-S3，一种表格化混合局部-全局方法，用于在有限 rollout 成本下提升机器人策略学习中的全局探索能力。该方法将高频局部更新与间歇性全局搜索轮次交替进行。在每轮搜索中，我们通过奇异值分解构建动态更新的低维策略子空间，并在该空间内执行迭代代理引导优化。预训练的表格化基础模型可根据少量上下文集预测候选回报，从而在有限 rollout 成本下实现大规模筛选。连续控制基准实验表明，在相同 rollout 预算下，与 TD3 和基于种群的基线方法相比，TFM-S3 持续加速了早期收敛并提升了最终性能。这些结果表明，基础模型是创建机器人连续控制样本高效策略学习方法的强大新工具。

---

### 4. SASI: Leveraging Sub-Action Semantics for Robust Early Action Recognition in Human-Robot Interaction

- **作者**: Yongpeng Cao, Masahiro Hirano, Hyuno Kim, Yuji Yamakawa
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.27508v1)
- **发表日期**: 2026-04-30
- **匹配关键词**: HRI, human-robot interaction
- **arXiv**: [2604.27508v1](http://arxiv.org/abs/2604.27508v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 理解人类行为对于推进人机交互中的行为分析至关重要。特别是在需要快速主动反馈的任务中，机器人必须从非完整的观测中尽早识别人类行为。子行为为此提供了所需的语义和层级线索，因为人类行为本身具有结构性，可分解为更小、有意义的单元。然而，传统方法主要关注整体行为，往往忽视子行为中蕴含的丰富语义结构，导致其难以适用于早期识别。为填补这一空白，我们提出了SASI（子行为语义集成跨模态融合）框架，该创新框架整合现有图卷积网络，将时空特征与子行为语义相融合。SASI利用分割模型与传统基于骨架的图卷积网络，在29Hz实时运行的同时，既能捕捉细粒度子行为语义，又能保留整体空间上下文。在具有帧级标注的骨架数据集BABEL上的实验表明，我们的方法相较于传统方法提升了识别准确率，且随着子行为分割质量的提高，性能有望进一步提升。值得注意的是，SASI在理解部分动作序列方面也展现出卓越性能，揭示了其早期识别能力——这对实现主动且无缝的人机交互至关重要。代码已开源：https://anonymous.4open.science/r/SASI

---

### 5. RAY-TOLD: Ray-Based Latent Dynamics for Dense Dynamic Obstacle Avoidance with TDMPC

- **作者**: Seungho Han, Seokju Lee, Jeonguk Kang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.27450v1)
- **发表日期**: 2026-04-30
- **匹配关键词**: obstacle avoidance, navigation
- **arXiv**: [2604.27450v1](http://arxiv.org/abs/2604.27450v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 密集、动态的人群对自主移动机器人构成了持续的挑战。纯反应式规划方法（如模型预测路径积分控制）因其有限的预测范围，在复杂场景中常难以摆脱局部最优解。为解决这一问题，我们提出基于射线的任务导向潜在动力学（RAY-TOLD）混合控制架构，该架构将障碍物信息整合至潜在动力学中，并融合基于物理的MPPI的鲁棒性与强化学习的长期前瞻能力。RAY-TOLD采用以激光雷达为中心的潜在动力学模型，将高维传感器数据编码为紧凑状态表征，从而学习终端价值函数与策略先验。我们引入策略混合采样策略，通过从学习策略中生成的轨迹扩充MPPI候选种群，在保持运动学可行性的同时有效引导规划器向目标移动。在高密度动态障碍物的随机环境中的大量测试表明，我们的方法优于MPPI基线，降低了碰撞率。结果证实，将基于物理的短时域推演与学习型长时域意图相结合，能显著提升导航的可靠性与安全性。

---

### 6. From Prompt to Physical Actuation: Holistic Threat Modeling of LLM-Enabled Robotic Systems

- **作者**: Neha Nagaraja, Hayretdin Bahsi, Carlo R. da Cunha
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.27267v1)
- **发表日期**: 2026-04-29
- **匹配关键词**: tool use
- **arXiv**: [2604.27267v1](http://arxiv.org/abs/2604.27267v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 随着大语言模型被集成到自主机器人系统中用于任务规划与控制，受损的输入或非安全的模型输出可能通过规划流水线传播，进而引发物理世界的实际后果。尽管已有研究分别探讨了机器人网络安全、对抗性感知攻击以及大语言模型安全性，但尚无研究追踪这些威胁类别如何在统一架构模型中跨越信任边界进行交互与传播。为填补这一空白，我们以边缘-云架构中的大语言模型赋能自主机器人为对象，将其建模为分层数据流图，并采用三类威胁分类体系（传统网络威胁、对抗性威胁与对话威胁），对六个跨边界交互点进行基于STRIDE的逐交互分析。分析表明，这些威胁类别在相同的边界交叉点汇聚，我们进一步追踪了三条从外部入口点到非安全物理执行器的跨边界攻击链，每条链均揭示了独特的架构特性：用户输入与执行器调度之间缺乏独立的语义验证、从视觉感知到语言模型指令的跨模态转换，以及通过提供方工具使用实现的无中介边界跨越。据我们所知，这是首个基于数据流图的威胁分析，将全部三类威胁整合至大语言模型赋能机器人系统的完整感知-规划-执行流水线中。

---

### 7. The Field of Safe Motion: Operationalizing Affordances in the Field of Safe Travel Using Reachability Analysis

- **作者**: Leif Johnson, Trent Victor, Johan Engström
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.27168v1)
- **发表日期**: 2026-04-29
- **匹配关键词**: affordance
- **arXiv**: [2604.27168v1](http://arxiv.org/abs/2604.27168v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出了安全运动场（FSM）这一量化安全模型，通过考虑驾驶员的生理能力及其他道路使用者的可预见行为，用于判定驾驶员在任何时刻是否保持无碰撞的逃生路径（即"出路"）。安全行驶场（FST）为表征驾驶员可获取的感官信息类型及可采取的行动提供了框架。然而，自近90年前首次提出以来，FST本质上仍停留在概念层面——至今缺乏具体的计算操作化实现。与此同时，可达性分析通过可解释的运动学模型，为评估道路使用者可能采取的行动提供了量化基础，但这类模型迄今主要局限于工程与机器人学文献。将这两种方法相结合，可为评估各类驾驶场景中的驾驶行为提供可解释的量化工具。除了具备可解释性外，我们的方法仅依赖少量易于列举和推理的基本假设。此外，将可解释的可达性模型与运动学假设相结合，能够界定道路使用者合理可预见的未来位置的不确定性边界。我们通过不同驾驶场景验证了FSM的适用性，并讨论了该模型的优势与局限性。

---

### 8. Stochastic Entanglement of Deterministic Origami Tentacles For Universal Robotic Gripping

- **作者**: Alec Boron, Bokun Zheng, Ziyang Zhou, Noel Naughton, Suyi Li
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.26897v1)
- **发表日期**: 2026-04-29
- **匹配关键词**: HRI, object manipulation
- **arXiv**: [2604.26897v1](http://arxiv.org/abs/2604.26897v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 受折纸启发的机器人抓取器因其紧凑的体积和机械灵活性，在物体操控任务中展现出巨大潜力。然而，在动态工作环境中稳健抓取随机形状的物体，往往需要以增加驱动通道和控制复杂度为代价。本文提出一种腱驱动的折纸触手抓取器，通过结合局部确定性变形编程与全局随机纠缠的协同作用，实现通用物体抓取。每个折纸触手由薄聚酯薄膜切割制成，其设计包含：用于引导驱动腱的精确孔位、控制变形的折痕结构以及锥形轮廓。通过定制这些设计特征，可预设收缩、弯曲和扭转变形，最终仅通过单根腱牵引即可实现确定性卷曲。当多个卷曲触手邻近放置时，会产生随机纠缠现象，使触手能够编织、打结并抓取任意形状的物体。我们通过整合折纸力学与Cosserat杆理论建立仿真模型，关联折纸设计、腱变形及其集体抓取性能。随后通过实验测试了这些卷曲纠缠折纸触手在重力环境及水下抓取物体的能力，并验证了用于模拟在轨抓取的收放式部署机构。总体而言，这种趣味性的折纸触手抓取器为通过简单设计与驱动实现稳健物体抓取提供了新策略。

---

### 9. Persona-Based Process Design for Assistive Human-Robot Workplaces for Persons with Disabilities

- **作者**: Nils Mandischer, Daria Eckert and, Lars Mikelsons
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.26527v1)
- **发表日期**: 2026-04-29
- **匹配关键词**: human-robot interaction
- **arXiv**: [2604.26527v1](http://arxiv.org/abs/2604.26527v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 人机交互正成为将残障人士融入工作场所的重要范式。尽管这类系统能使个体参与工作，但其设计大多高度个性化，阻碍了超越个体用户的广泛使用。通用设计范式作为包容性设计的核心支柱，强调系统对所有用户的可及性。要将通用设计融入人机协作工作场所的流程设计，需要通常难以获取的专业知识。为简化人机协作工作场所的流程设计，我们提出了一种基于角色（persona）的设计方法。首先，将劳动力中普遍存在或与流程特别相关的典型障碍抽象为残障角色。工作流程被细分为连续动作。针对每个动作和角色，通过设计思维方法制定达成动作目标的策略。最终动作按机器人辅助程度（即机器人参与度）排序，并实现为行为树。由此，工作场所的宏观行为可在线适应个体角色。我们通过一个包含七种残障角色的协作折箱流程验证了该方法。基于角色的流程设计在生成更全面的流程策略的同时，实现了通用设计意义上的自适应行为，展现出良好前景。

---

