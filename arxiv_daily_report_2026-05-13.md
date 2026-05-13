# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-05-13 08:03

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 0/20 篇提供

**🌟 Highlight**: 20 篇 | **📌 Poster**: 0 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. HarmoWAM: Harmonizing Generalizable and Precise Manipulation via Adaptive World Action Models

- **作者**: Qiuxuan Feng, Jiale Yu, Jiaming Liu, Yueru Jia, Zhuangzhe Wu, Hao Chen, Zezhong Qian, Shuo Gu, Peng Jia, Siwei Ma, Shanghang Zhang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.10942v1)
- **发表日期**: 2026-05-11
- **匹配关键词**: VLA, exploration
- **arXiv**: [2605.10942v1](http://arxiv.org/abs/2605.10942v1)
- **📥 PDF**: 已下载至本地 (`2605.10942v1_HarmoWAM_Harmonizing_Generalizable_and_Precise_Manipulation_via_Adaptive_World_Action_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 世界动作模型（WAMs）通过建模物理动力学，已成为机器人控制领域一种前景广阔的新范式。当前WAMs主要遵循两种范式：一是"先想象后执行"方法，通过视频预测并利用逆动力学推断动作；二是"联合建模"方法，将动作与视频表征进行联合建模。基于系统性实验，我们观察到这两种范式存在根本性权衡：前者显式利用世界模型实现可泛化的状态转移，但缺乏交互精度；后者虽能生成细粒度、时间连贯的动作，却受限于训练分布的探索空间。受此启发，我们提出HarmoWAM——一种端到端的世界动作模型，它充分利用世界模型统一预测式控制与反应式控制，同时实现可泛化的状态转移与精准操控。具体而言，世界模型提供时空物理先验，用于条件化两个互补的动作专家：预测专家利用潜在动力学进行迭代动作生成，反应专家则直接从预测的视觉演化中推断动作。为实现自适应协调，我们提出过程自适应门控机制，自动决定两者切换的时机与位置。这使得世界模型能驱动反应专家扩展探索空间，同时让预测专家在任务不同阶段执行精准交互。为评估性能，我们构建了涵盖六项真实机器人任务的三个训练未见测试环境，涉及背景、位置和物体语义的变化。值得注意的是，HarmoWAM在这些场景中展现出强大的零样本泛化能力，相较于先前最先进的VLA模型和WAMs，性能分别显著提升33%和29%。

---

### 2. PriorVLA: Prior-Preserving Adaptation for Vision-Language-Action Models

- **作者**: Xinyu Guo, Bin Xie, Wei Chai, Xianchi Deng, Tiancai Wang, Zhengxing Wu, Xingyu Chen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.10925v1)
- **发表日期**: 2026-05-11
- **匹配关键词**: VLA, vision-language-action model, vision-language-action
- **arXiv**: [2605.10925v1](http://arxiv.org/abs/2605.10925v1)
- **📥 PDF**: 已下载至本地 (`2605.10925v1_PriorVLA_Prior-Preserving_Adaptation_for_Vision-Language-Action_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 大规模预训练使视觉-语言-动作（VLA）模型成为通用机器人操作的理想基础，但将其适配到下游任务仍必不可少。然而，常见的全参数微调将预训练视为初始化过程，可能导致广泛的先验知识向狭窄的训练分布模式偏移。我们提出PriorVLA——一种保留预训练先验知识并学习利用其进行高效适配的新框架。PriorVLA将冻结的先验专家作为只读先验知识源，同时训练适配专家用于下游任务特化。专家查询机制从预训练VLM中提取场景先验，并从先验专家中提取运动先验，将两者整合至适配专家以指导适配过程。相较于全参数微调，PriorVLA仅需更新25%的参数。在RoboTwin 2.0、LIBERO及真实世界任务中，PriorVLA的整体性能全面超越全参数微调及当前最优VLA基线方法，尤其在分布外（OOD）和少样本场景下提升最为显著。PriorVLA在RoboTwin 2.0-Hard上较pi0.5提升11个百分点，在LIBERO上达到99.1%的平均成功率。在八项真实世界任务及两种机器人形态中，PriorVLA使用标准数据实现81%的分布内（ID）成功率和57%的OOD成功率。当每项任务仅使用10条示范数据时，PriorVLA仍能达到48%的ID成功率和32%的OOD成功率，分别超越pi0.5达24和22个百分点。

---

### 3. RoboMemArena: A Comprehensive and Challenging Robotic Memory Benchmark

- **作者**: Huashuo Lei, Wenxuan Song, Huarui Zhang, Jieyuan Pei, Jiayi Chen, Haodong Yan, Han Zhao, Pengxiang Ding, Zhipeng Zhang, Lida Huang, Donglin Wang, Yan Wang, Haoang Li
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.10921v1)
- **发表日期**: 2026-05-11
- **匹配关键词**: VLA
- **arXiv**: [2605.10921v1](http://arxiv.org/abs/2605.10921v1)
- **📥 PDF**: 已下载至本地 (`2605.10921v1_RoboMemArena_A_Comprehensive_and_Challenging_Robotic_Memory_Benchmark.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 记忆是机器人智能的关键组成部分，因为机器人必须依赖过去的观察和行动，在部分可观测环境中完成长期任务。然而，现有的机器人记忆基准仍缺乏用于记忆形成的多模态标注，任务覆盖范围和结构复杂度有限，且仅局限于仿真环境，缺乏真实世界评估。为解决这一问题，我们提出了RoboMemArena，这是一个包含26个任务的大规模基准，每个任务的平均轨迹长度超过1000步，其中68.9%的子任务依赖于记忆。该生成流程利用视觉语言模型（VLM）设计和组合子任务，通过原子函数生成完整轨迹，并提供与记忆相关的标注，包括子任务指令和原生关键帧标注，同时配套的真实世界记忆任务支持物理评估。我们进一步设计了PrediMem，这是一个双系统视觉-语言-动作（VLA）模型，其中高层VLM规划器管理包含近期和关键帧缓冲区的记忆库，并使用预测编码头来提升对任务动态变化的敏感性。在RoboMemArena上的大量实验表明，PrediMem优于所有基线方法，并为复杂记忆系统的记忆管理、模型架构和扩展规律提供了深入见解。

---

### 4. Unified Noise Steering for Efficient Human-Guided VLA Adaptation

- **作者**: Junjie Lu, Xinyao Qin, Yuhua Jiang, Kaixin Wang, Chuheng Zhang, Bin Liang, Jun Yang, Min Xu, Li Zhao
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.10821v1)
- **发表日期**: 2026-05-11
- **匹配关键词**: VLA, exploration, vision-language-action
- **arXiv**: [2605.10821v1](http://arxiv.org/abs/2605.10821v1)
- **📥 PDF**: 已下载至本地 (`2605.10821v1_Unified_Noise_Steering_for_Efficient_Human-Guided_VLA_Adaptation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 基于扩散的视觉-语言-动作（VLA）模型已成为机器人操作领域的强大先验知识，但将其适配到真实世界分布仍面临挑战。具体而言，在机器人本体上进行强化学习（RL）成本高昂且耗时，因此有效适配依赖于在有限真实世界交互预算内实现高效策略改进。噪声空间强化学习通过保持预训练VLA作为去噪生成器固定不变，仅更新预测噪声的轻量级动作网络来降低开销。然而，由于自主探索效率低下，其性能仍受限制。人类纠正性干预可减少探索负担，但这类干预天然存在于动作空间，而噪声空间微调需要针对噪声变量的监督信号。为解决这些问题，我们提出UniSteer——一种统一噪声引导框架，通过近似动作到噪声的逆映射，将人类纠正性引导与噪声空间强化学习相结合。给定人类纠正动作后，UniSteer逆向冻结的流匹配解码器以恢复噪声目标，为同时通过强化学习优化的同一噪声动作网络提供监督引导。在多种操作任务的真实世界实验中，UniSteer比强噪声空间强化学习和动作空间人在回路基线方法展现出更高效的适配能力，在四项真实世界适配任务中平均耗时66分钟将成功率从20%提升至90%。

---

### 5. ALAM: Algebraically Consistent Latent Transitions for Vision-Language-Action Models

- **作者**: Zuojin Tang, Haoyun Liu, Xinyuan Chang, Changjie Wu, Dongjie Huo, Yandan Yang, Bin Liu, Zhejia Cai, Feng Xiong, Mu Xu, jiachen Luo, De Ma, Zhiheng Ma, Gang Pan
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.10819v1)
- **发表日期**: 2026-05-11
- **匹配关键词**: VLA, vision-language-action model, vision-language-action
- **arXiv**: [2605.10819v1](http://arxiv.org/abs/2605.10819v1)
- **📥 PDF**: 已下载至本地 (`2605.10819v1_ALAM_Algebraically_Consistent_Latent_Transitions_for_Vision-Language-Action_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型仍受限于带动作标签的机器人数据稀缺问题，而无动作视频则提供了物理世界如何变化的丰富证据。潜在动作模型为从视频中提取此类先验知识提供了可行方案，但基于重建训练的潜在编码未必适用于策略生成：它们虽能预测未来观测，却缺乏与机器人动作协同复用或生成所需的结构化特性。我们提出ALAM（代数潜在动作模型），这是一种代数一致性潜在动作模型，可将无动作视频中的时序关系转化为结构监督。通过帧三元组训练，ALAM在重建约束下学习潜在状态转移，同时通过组合一致性与反转一致性进行正则化，从而构建局部可加性的转移空间。在下游VLA学习中，我们冻结预训练编码器，将其潜在转移序列作为辅助生成目标，在联合流匹配目标下与机器人动作协同生成。这种设计将结构化潜在转移与基于流的策略生成相结合，使策略能够利用ALAM的局部一致性转移几何结构，而无需进行潜在到动作的解码。表征探针实验表明，相较于非结构化潜在动作基线，ALAM将可加性与可逆性误差降低25-85倍，并提升了长程累积重建效果。当迁移至VLA策略时，ALAM在MetaWorld MT50上将平均成功率从47.9%提升至85.0%，在LIBERO上从94.1%提升至98.1%，并在真实世界操控任务中取得一致增益。消融实验进一步证实，代数结构化潜在转移与联合流匹配的协同效应带来了最显著的性能提升。

---

### 6. MAGS-SLAM: Monocular Multi-Agent Gaussian Splatting SLAM for Geometrically and Photometrically Consistent Reconstruction

- **作者**: Zhihao Cao, Qi Shao, Shuhao Zhai, Jing Zhang, Anh Nguyen, Baoru Huang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.10760v1)
- **发表日期**: 2026-05-11
- **匹配关键词**: gaussian splatting, 3D gaussian splatting, exploration, 3D reconstruction, 3d reconstruction
- **arXiv**: [2605.10760v1](http://arxiv.org/abs/2605.10760v1)
- **📥 PDF**: 已下载至本地 (`2605.10760v1_MAGS-SLAM_Monocular_Multi-Agent_Gaussian_Splatting_SLAM_for_Geometrically_and_Photometrically_Consis.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 多智能体协同的逼真三维重建能够实现快速的大规模场景捕捉，适用于虚拟制作和多机器人协同探索。尽管近期基于3D高斯泼溅（3DGS）的SLAM算法能够生成高保真实时地图，但现有的大多数多智能体高斯SLAM方法仍依赖RGB-D传感器获取度量深度并简化跨智能体对齐，这限制了其在轻量级、低成本或功耗受限的机器人平台上的部署。为解决这一挑战，我们提出MAGS-SLAM——首个仅依赖RGB图像的多智能体3DGS SLAM框架，用于协同场景重建。每个智能体独立构建局部单目高斯子地图，并传输紧凑的子地图摘要而非原始观测数据或稠密地图。为应对单目尺度模糊性下的鲁棒协同，该框架整合了紧凑子地图通信、几何与外观感知的闭环验证以及占用感知的高斯融合，从而在无需主动深度传感器的情况下实现连贯的全局重建。我们进一步引入ReplicaMultiagent Plus基准测试，用于评估协同高斯SLAM性能。在合成与真实数据集上的大量实验表明，MAGS-SLAM在仅依赖RGB图像的情况下，达到了与最先进的RGB-D协同高斯SLAM方法相当的跟踪精度，以及可比或更优的渲染质量。

---

### 7. ObjView-Bench: Rethinking Difficulty and Deployment for Object-Centric View Planning

- **作者**: Sicong Pan, Hao Hu, Xuying Huang, Benno Wingender, Maren Bennewitz
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.10707v1)
- **发表日期**: 2026-05-11
- **匹配关键词**: 3d reconstruction, 3D reconstruction
- **arXiv**: [2605.10707v1](http://arxiv.org/abs/2605.10707v1)
- **📥 PDF**: 已下载至本地 (`2605.10707v1_ObjView-Bench_Rethinking_Difficulty_and_Deployment_for_Object-Centric_View_Planning.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 以物体为中心的视角规划是机器人主动几何三维重建的核心组成部分，然而现有评估常常混淆物体复杂度、规划难度、预算假设和物理可达性约束。因此，从理想化视角规划评估中得出的结论可能无法可靠预测实际重建场景下的性能。我们提出ObjView-Bench，一个重新思考以物体为中心的视角规划中难度与部署问题的评估框架。首先，我们解耦了视角规划评估中的三个关键量：作为物体侧属性的全方位自遮挡、观测饱和难度，以及通过集合覆盖公式定义的协议依赖型规划难度。这种分离支持可控数据集构建、慢饱和物体分析，并通过案例研究表明，考虑规划难度的采样能够改进学习型视角规划器。其次，我们设计了面向部署的评估协议，揭示预算机制和可达视角约束如何改变方法行为。在经典、学习型和混合型规划器中，ObjView-Bench表明难度、预算和可达性约束会显著改变方法排名和失败模式。

---

### 8. VEGA: Visual Encoder Grounding Alignment for Spatially-Aware Vision-Language-Action Models

- **作者**: Hao Wang, Xiaobao Wei, Jingyang He, Chengyu Bai, Chun-Kai Fan, Jiajun Cao, Jintao Chen, Ying Li, Shanyu Rong, Ming Lu, Xiaozhu Ju, Jian Tang, Shanghang Zhang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.10485v1)
- **发表日期**: 2026-05-11
- **匹配关键词**: gaussian splatting, VLA, vision-language-action model, 3D gaussian splatting, vision-language-action
- **arXiv**: [2605.10485v1](http://arxiv.org/abs/2605.10485v1)
- **📥 PDF**: 已下载至本地 (`2605.10485v1_VEGA_Visual_Encoder_Grounding_Alignment_for_Spatially-Aware_Vision-Language-Action_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 精确的空间推理是机器人操作的基础，然而当前视觉-语言-动作（VLA）模型的视觉主干主要基于二维图像数据预训练，缺乏明确的三维几何监督，导致其表征缺乏准确的空间感知能力。现有隐式空间对齐方法通过将VLA特征与三维感知基础模型的特征对齐来部分解决这一问题，但这些方法依赖经验性的层搜索，并在语言语义已与空间结构纠缠的LLM级视觉令牌上执行对齐，限制了泛化能力和几何可解释性。我们提出VEGA（视觉编码器基础对齐）——一个简单而有效的框架，直接将VLA视觉编码器的输出与DINOv2-FiT3D（经多视角一致三维高斯泼溅监督微调的DINOv2模型）的空间感知特征对齐。通过在视觉编码器输出层面执行对齐，VEGA在语言语义纠缠发生前就植入了空间感知能力，提供了更具可解释性和原则性的对齐目标。该对齐通过轻量级投影器实现，采用余弦相似度损失与标准动作预测目标联合训练，推理时该投影器被丢弃，不引入额外计算开销。在仿真基准和真实世界操作任务上的大量实验表明，VEGA始终优于现有隐式空间对齐基线，在VLA模型的隐式空间对齐方法中确立了新的最优水平。

---

### 9. OpenSGA: Efficient 3D Scene Graph Alignment in the Open World

- **作者**: Gang Chen, Sebastián Barbas Laina, Stefan Leutenegger, Javier Alonso-Mora ⭐
  - **高亮作者**: Stefan Leutenegger
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.10484v1)
- **发表日期**: 2026-05-11
- **匹配关键词**: scene graph
- **arXiv**: [2605.10484v1](http://arxiv.org/abs/2605.10484v1)
- **📥 PDF**: 已下载至本地 (`2605.10484v1_OpenSGA_Efficient_3D_Scene_Graph_Alignment_in_the_Open_World.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 场景图对齐旨在建立由部分重叠观测构建的两个三维场景图之间的物体对应关系。这使机器人在重访某地点时能够实现高效的场景理解和物体级重定位，同时支持多智能体间的全局地图融合。此类能力对于需要长期记忆以执行涉及环境交互的长时域任务的机器人至关重要。现有方法主要聚焦于子扫描到子扫描（S2S）对齐，且高度依赖几何点云特征，而帧到扫描（F2S）对齐与开放集视觉语言特征的研究仍不充分。此外，现有场景图对齐数据集规模较小且物体多样性有限，制约了系统化训练与评估。我们提出一种统一高效的场景图对齐框架，通过融合视觉语言、文本、几何特征及空间上下文来预测物体对应关系。该框架包含距离门控空间注意力编码器、基于最小费用流的分配器及全局场景嵌入生成器等模块，即使在坐标偏差较大的情况下也能实现精确对齐。我们进一步推出ScanNet-SG大规模数据集，通过自动化标注流程生成超过70万个样本，涵盖ScanNet标签中的509个物体类别及基于GPT-4o标注的3000余个类别。实验表明，本方法在F2S和S2S任务上均取得最佳综合性能，显著超越现有场景图对齐方法。代码与数据集已发布于：https://autonomousrobots.nl/paper_websites/opensga。

---

### 10. PaMoSplat: Part-Aware Motion-Guided Gaussian Splatting for Dynamic Scene Reconstruction

- **作者**: Yinan Deng, Jianyu Dou, Jiahui Wang, Jingyu Zhao, Yi Yang, Yufeng Yue
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.10307v1)
- **发表日期**: 2026-05-11
- **匹配关键词**: gaussian splatting
- **arXiv**: [2605.10307v1](http://arxiv.org/abs/2605.10307v1)
- **📥 PDF**: 已下载至本地 (`2605.10307v1_PaMoSplat_Part-Aware_Motion-Guided_Gaussian_Splatting_for_Dynamic_Scene_Reconstruction.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 动态场景重建是计算机视觉与机器人领域一项基础且极具挑战性的任务。尽管基于3DGS的方法在动态场景建模方面取得了最新进展，但在处理包含复杂大幅运动的场景时，实现高保真渲染与精确跟踪仍面临显著困难。为解决这些挑战，我们提出PaMoSplat——一种融合部件感知与运动先验的新型动态高斯泼溅框架。该方法基于两个关键观察：1）部件可作为场景形变的基本单元；2）光流中的运动线索能有效引导部件运动。具体而言，PaMoSplat首先通过图聚类将多视角分割掩码提升至三维空间，建立连贯的高斯部件。针对后续时间戳，我们利用差分进化算法，借助多视角光流线索估计这些部件的刚体运动，为后续优化提供稳健的初始值。此外，PaMoSplat引入自适应迭代次数机制、内部可学习刚体性及光流监督渲染损失，以加速并优化训练过程。在包含真实环境的多样化场景中的全面评估表明，相比现有方法，PaMoSplat实现了更优的渲染质量、更高的跟踪精度及更快的收敛速度。同时，该方法支持多种部件级下游应用，如4D场景编辑。

---

### 11. HeteroGenManip: Generalizable Manipulation For Heterogeneous Object Interactions

- **作者**: Zhenhao Shen, Zeming Yang, Yue Chen, Yuran Wang, Shengqiang Xu, Mingleyang Li, Hao Dong, Ruihai Wu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.10201v1)
- **发表日期**: 2026-05-11
- **匹配关键词**: diffusion policy
- **arXiv**: [2605.10201v1](http://arxiv.org/abs/2605.10201v1)
- **📥 PDF**: 已下载至本地 (`2605.10201v1_HeteroGenManip_Generalizable_Manipulation_For_Heterogeneous_Object_Interactions.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 涉及跨类型物体交互的通用操作是机器人领域中一项关键且具有挑战性的能力。为可靠完成此类任务，机器人必须解决两个基本问题："操作位置"（接触点定位）与"操作方式"（后续交互轨迹规划）。现有基于基础模型的方法常采用端到端学习，模糊了这两个阶段的界限，加剧了长时域任务中的误差累积。此外，这类方法通常依赖单一统一模型，难以捕捉异质物体所需的多样化类别特异性特征。为突破这些局限，我们提出HeteroGenManip——一种任务条件化的两阶段框架，旨在将初始抓取与复杂交互执行解耦。首先，基础对应引导抓取模块利用结构先验对齐初始接触状态，显著降低抓取位姿不确定性。随后，多基础模型扩散策略通过双流交叉注意力机制，将物体路由至类别特化的基础模型，融合细粒度几何信息与高度可变的部件特征。实验评估表明，HeteroGenManip实现了稳健的类内形状与位姿泛化能力。该框架在宽类型设置的仿真任务中平均性能提升31%，在四种不同交互类型的真实世界任务中平均性能提升36.7%。

---

### 12. Retrieve-then-Steer: Online Success Memory for Test-Time Adaptation of Generative VLAs

- **作者**: Jianchao Zhao, Huoren Yang, Hu Yusong, Yuyang Gao, Qiguan Ou, Cong Wan, SongLin Dong, Zhiheng Ma, Yihong Gong
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.10094v1)
- **发表日期**: 2026-05-11
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2605.10094v1](http://arxiv.org/abs/2605.10094v1)
- **📥 PDF**: 已下载至本地 (`2605.10094v1_Retrieve-then-Steer_Online_Success_Memory_for_Test-Time_Adaptation_of_Generative_VLAs.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型在通用机器人操作领域展现出巨大潜力，但其闭环可靠性在本地部署条件下常会下降。现有评估通常将测试回合视为独立的零样本试验。然而，真实机器人往往在相同或缓慢变化的环境中重复运行，此时成功执行可提供环境验证的可靠行为模式证据。本研究聚焦这种持续部署场景，探究部分胜任的冻结VLA模型能否通过复用成功的测试时经验提升可靠性。我们提出了一种面向生成式VLA的在线成功记忆引导测试时自适应框架。在部署过程中，机器人将经过进度校准的成功观测-动作片段存储至长期记忆；推理时，系统检索与状态相关的动作片段，通过轨迹级一致性过滤不一致候选，并将其聚合为精英动作先验。为将该先验融入动作生成过程，我们引入置信度自适应先验引导机制——将精英先验注入流匹配动作采样器的中间状态，并根据检索置信度动态调节引导强度。该设计使冻结VLA既能利用环境特定的成功经验，又能保留基于观测的条件生成精化能力。这种"检索-引导"机制实现了无需参数更新的轻量级非参数测试时自适应。仿真与真实实验表明，该方法在任务成功率与闭环稳定性方面均有提升，尤其适用于长时域及多阶段任务。

---

### 13. EFGCL: Learning Dynamic Motion through Spotting-Inspired External Force Guided Curriculum Learning

- **作者**: Keita Yoneda, Kento Kawaharazuka, Kei Okada
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.10063v1)
- **发表日期**: 2026-05-11
- **匹配关键词**: exploration
- **arXiv**: [2605.10063v1](http://arxiv.org/abs/2605.10063v1)
- **📥 PDF**: 已下载至本地 (`2605.10063v1_EFGCL_Learning_Dynamic_Motion_through_Spotting-Inspired_External_Force_Guided_Curriculum_Learning.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 通过强化学习（RL）让足式机器人学习动态全身运动仍具挑战性，主要源于高失败风险导致探索效率低下且学习过程不稳定。本文提出外力引导课程学习（EFGCL），这是一种基于物理引导原理的引导式强化学习方法，在训练过程中引入外部辅助力。受艺术体操中"保护性助力"的启发，EFGCL使智能体无需依赖特定任务奖励塑形或参考轨迹，即可物理体验成功运动执行。在四足机器人执行跳跃、后空翻和侧空翻任务的实验中，EFGCL将跳跃任务的学习速度提升约两倍，并成功习得传统RL方法无法掌握的复杂全身运动。我们进一步证明，学习到的策略可部署至真实机器人，复现与仿真观测一致的运动。这些结果表明，物理引导式探索——让智能体在训练早期体验成功——是提升动态全身运动任务学习效率的有效通用策略。

---

### 14. StereoPolicy: Improving Robotic Manipulation Policies via Stereo Perception

- **作者**: Evans Han, Yunfan Jiang, Yingke Wang, Haoyue Xiao, Huang Huang, Jianwen Xie, Jiajun Wu, Li Fei-Fei, Ruohan Zhang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.09989v1)
- **发表日期**: 2026-05-11
- **匹配关键词**: VLA, mobile manipulation, 3D reconstruction, 3d reconstruction, vision-language-action
- **arXiv**: [2605.09989v1](http://arxiv.org/abs/2605.09989v1)
- **📥 PDF**: 已下载至本地 (`2605.09989v1_StereoPolicy_Improving_Robotic_Manipulation_Policies_via_Stereo_Perception.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 近期机器人模仿学习领域的进展催生了强大的视觉运动策略，使机器人能够直接从单目视觉输入操控多种物体。然而，单目观测本质上缺乏可靠的深度线索和空间感知能力，而这对于在杂乱或几何复杂场景中实现精准操控至关重要。为解决这一局限，我们提出StereoPolicy——一种新型视觉运动策略学习框架，该框架直接利用同步立体图像对增强几何推理能力，无需显式三维重建或相机标定。StereoPolicy采用预训练的二维视觉编码器独立处理每张图像，并通过立体Transformer融合所得表征，隐式捕获空间对应关系与视差线索。该框架可与基于扩散模型及预训练视觉-语言-动作（VLA）策略无缝集成，在RoboMimic、RoboCasa和OmniGibson三个仿真基准测试中，相较于RGB、RGB-D、点云及多视角基线方法均实现持续性能提升。我们进一步在真实机器人实验中验证了StereoPolicy，涵盖桌面操作与双臂移动操作场景。研究结果表明，立体视觉作为一种可扩展且稳健的感知模态，能够有效桥接二维预训练表征与三维几何理解，赋能机器人操控任务。

---

### 15. LoopVLA: Learning Sufficiency in Recurrent Refinement for Vision-Language-Action Models

- **作者**: Boyang Shen, Kaixiang Yang, Hao Wang, Qiuyu Yu, Qiang Xie, Qiang Li, Zhiwei Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.09948v1)
- **发表日期**: 2026-05-11
- **匹配关键词**: VLA, vision-language-action model, vision-language-action
- **arXiv**: [2605.09948v1](http://arxiv.org/abs/2605.09948v1)
- **📥 PDF**: 已下载至本地 (`2605.09948v1_LoopVLA_Learning_Sufficiency_in_Recurrent_Refinement_for_Vision-Language-Action_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 当前的视觉-语言-动作（VLA）模型通常将视觉-语言骨干网络的最深层表征视为动作预测的通用最优解。然而，机器人操作包含大量频繁的闭环空间调整，过度抽象可能浪费计算资源并削弱精确控制所需的底层几何线索。现有早期退出策略试图通过预设层停止或应用动作一致性等启发式规则来减少计算量，但未能直接回答"表征何时真正足以支撑动作"这一核心问题。本文提出LoopVLA——一种循环VLA架构，可联合学习表征优化、动作预测与充分性估计。LoopVLA通过迭代应用共享Transformer模块优化多模态令牌，每次迭代同时生成候选动作与评估是否需要进一步优化的充分性分数。通过跨迭代共享参数，LoopVLA将优化过程与绝对层索引解耦，并使充分性估计植根于不断演化的表征本身。由于充分性缺乏直接监督信号，我们引入自监督分布对齐目标：训练中间置信度分数匹配各优化阶段相对动作质量，从而将充分性学习与策略优化信号关联。在LIBERO、LIBERO-Plus和VLA-Arena上的实验表明，LoopVLA推动了VLA策略的效率-性能边界，在匹配或超越强基线任务成功率的同时，参数量减少45%，推理吞吐量提升高达1.7倍。

---

### 16. SABER: A Scalable Action-Based Embodied Dataset for Real-World VLA Adaptation

- **作者**: Narsimha Menga, Parikshit Sakurikar, Amirreza Rouhi, Satya Sai Reddy, Anirudh Govil, Sri Harsha Chittajallu, Rajat Aggarwal, Anoop Namboodiri, Sashi Reddi
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.09613v1)
- **发表日期**: 2026-05-10
- **匹配关键词**: VLA
- **arXiv**: [2605.09613v1](http://arxiv.org/abs/2605.09613v1)
- **📥 PDF**: 已下载至本地 (`2605.09613v1_SABER_A_Scalable_Action-Based_Embodied_Dataset_for_Real-World_VLA_Adaptation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 机器人在真实环境中的部署既依赖于强大的模型架构，也依赖于丰富的领域特定动作数据。通用机器人基础模型在开箱即用时，面对零售领域操作等复杂未见任务表现平平。其根本原因在于数据缺口：零售环境在结构上普遍缺失于通用机器人预训练分布，而通过遥操作填补这一缺口的路径成本高昂、受物流限制且难以规模化。我们提出SABER——一个高保真零售机器人动作数据集，基于在多个真实杂货店环境中超过100小时的自然店内采集构建。头戴式摄像头的第一人称视角视频记录了交互点的精细手部活动，而DreamVu的ALIA摄像头提供的360度全景场景视角则同步观测整个空间内的所有参与者与活动。这种组合形成了人类零售行为的独特完整图景：灵巧手部活动、全身运动与场景动态，全程无需布景、脚本或遥操作开销。SABER语料库包含三个动作表征流的44.8K训练样本：通过LAPA风格编码的25K潜在动作序列、重定向至机器人关节空间的18.6K灵巧手部姿态轨迹，以及重定向至人形机器人本体的1.2K全身同步运动序列。当通过共享骨干多任务后训练方案应用于GR00T N1.6时，SABER在十项零售操作任务中实现了29.3%的平均成功率——是微调基线（13.4%）的2.19倍以上。SABER证明，实现高性能零售机器人的路径在于更优质的数据，这些数据如今无需机器人参与即可大规模采集。数据集与代码已开源：https://dreamvu.ai/saber

---

### 17. Drift is a Sampling Error: SNR-Aware Power Distributions for Long-Horizon Robotic Planning

- **作者**: Kewei Chen, Yayu Long, Mingsheng Shang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.09537v1)
- **发表日期**: 2026-05-10
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2605.09537v1](http://arxiv.org/abs/2605.09537v1)
- **📥 PDF**: 已下载至本地 (`2605.09537v1_Drift_is_a_Sampling_Error_SNR-Aware_Power_Distributions_for_Long-Horizon_Robotic_Planning.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 尽管视觉-语言-动作（VLA）模型在机器人控制领域取得了快速进展，但在长时域任务中，指令漂移仍然是一个持续存在的失败模式。本文重新概念化了这一现象，认为指令漂移本质上是一种系统性采样误差：局部贪婪采样容易坍缩为“负关键窗口”——即具有高局部概率且不可逆的局部最优解，从而切断全局成功路径。为解决这一问题，我们提出了上下文感知幂采样（CAPS），这是一种无需训练、仅在推理时计算的方法。CAPS利用幂分布来锐化全局轨迹概率，从而实现对模型条件生成轨迹分布的前瞻性搜索。此外，我们引入了一种基于信噪比（SNR）的元认知控制机制。该机制仅在检测到漂移风险时触发自适应MCMC搜索，实现从“直觉快速思考”到“理性慢速搜索”的动态切换。在RoboTwin、Simpler-WindowX和Libero-long基准上的实验表明，CAPS在无需参数更新的情况下，相较于包括OpenVLA和TACO在内的强基线方法取得了显著改进。这些结果验证了自适应推理时计算在提升具身控制长时域鲁棒性方面的有效性。

---

### 18. Beyond Isolation: A Unified Benchmark for General-Purpose Navigation

- **作者**: Samson Sun, Tianyi Yang, Tengyue Wang, Yikai Xue, Zhengjie Xu, Lingming Zhang, Qichen Zhang, Chao Liang, Zhipeng Zhang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.09441v1)
- **发表日期**: 2026-05-10
- **匹配关键词**: exploration, navigation, VLN
- **arXiv**: [2605.09441v1](http://arxiv.org/abs/2605.09441v1)
- **📥 PDF**: 已下载至本地 (`2605.09441v1_Beyond_Isolation_A_Unified_Benchmark_for_General-Purpose_Navigation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 通用型具身智能体的发展受限于碎片化的评估体系——这些体系将导航技能割裂开来，并固着于特定机器人形态，无法反映智能体需在不同形态下协调多样化行为的真实场景。为弥合这一鸿沟，我们提出OmniNavBench，一个面向跨技能协调与跨形态泛化的基准测试。OmniNavBench引入三大范式转变：（1）组合复杂性。我们提出复合指令，将6类子任务（点导航、视觉语言导航、目标导航、社交导航、人类跟随与问答）交织组合，迫使智能体在单次任务中实现探索、交互与社交规范的动态切换。（2）形态普适性与传感器灵活性。我们构建的仿真平台打破了对单一形态评估的依赖，支持人形、四足及轮式机器人的泛化测试，配备模块化传感器接口，并整合170个融合合成资产与真实扫描数据的场景。（3）示范质量。超越最短路径算法，我们通过人类遥操作精心采集1779条专家轨迹，捕捉探索性扫视、预期性避障等行为细节。大量评估表明，当前方法虽声称具备统一设计，却难以应对通用导航中复杂交织的任务特性。这揭示了现有能力与现实部署需求间的关键差距，凸显OmniNavBench作为新一代通用导航智能体试验平台的价值。数据集、代码与排行榜已发布于http://omninavbench.cloud-ip.cc。

---

### 19. MAG-VLAQ: Multi-modal Aerial-Ground Query Aggregation for Cross-View Place Recognition

- **作者**: Zhengyi Xu, Yuhang Ming, Zhihao Zhan, Hanyu Zhu, Javier Civera, Wanzeng Kong
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.09418v1)
- **发表日期**: 2026-05-10
- **匹配关键词**: VLA, place recognition
- **arXiv**: [2605.09418v1](http://arxiv.org/abs/2605.09418v1)
- **📥 PDF**: 已下载至本地 (`2605.09418v1_MAG-VLAQ_Multi-modal_Aerial-Ground_Query_Aggregation_for_Cross-View_Place_Recognition.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 多模态跨视角地点识别仍是计算机视觉与机器人领域的基础性挑战，主要源于地面观测与空中参考之间存在严重的视角、模态及空间结构差异。为解决该问题，我们提出MAG-VLAQ——一种基于基础模型增强的查询聚合框架，用于多模态空地跨视角地点识别。具体而言，本方法利用预训练基础模型从地面与空中图像中提取密集视觉标记，同时从地面激光雷达观测中提取具有表达力的几何标记。这些异构标记随后被投影至共享嵌入空间进行跨模态对齐与融合。作为核心贡献，我们提出基于常微分方程（ODE）约束的VLAQ机制，该机制将基于神经ODE的RGB-激光雷达融合与局部聚合查询向量（VLAQ）紧密耦合。在此设计中，VLAQ查询中心根据融合后的多模态状态动态调整。该机制使最终全局描述符既能保留全局学习的检索原型，又能对场景特定的视觉与几何证据保持响应性，显著提升了空地匹配性能。在KITTI360-AG与nuScenes-AG数据集上的大量实验验证了MAG-VLAQ的有效性。值得注意的是，在KITTI360-AG卫星设置下，MAG-VLAQ的Recall@1达到61.1%，较最优对比方法的34.5%近乎翻倍，实现了当前最优性能。

---

### 20. CAGS: Color-Adaptive Volumetric Video Streaming with Dynamic 3D Gaussian Splatting

- **作者**: Daheng Yin, Yili Jin, Jianxin Shi, Isaac Ding, Miao Zhang, Fangxin Wang, Zhaowu Huang, Cong Zhang, Jiangchuan Liu, Fang Dong
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.09279v1)
- **发表日期**: 2026-05-10
- **匹配关键词**: gaussian splatting, 3D gaussian splatting
- **arXiv**: [2605.09279v1](http://arxiv.org/abs/2605.09279v1)
- **📥 PDF**: 已下载至本地 (`2605.09279v1_CAGS_Color-Adaptive_Volumetric_Video_Streaming_with_Dynamic_3D_Gaussian_Splatting.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 体积视频（VV）流传输技术能够实现对远程三维环境的实时沉浸式访问，为远程呈现、生态监测和机器人远程操作提供支持。这些应用将VV流传输转变为远程物理环境的实时交互界面，对系统级能力提出了新要求：包括照片级场景再现、低延迟交互以及在异构网络下的稳健性能。三维高斯泼溅（3DGS）凭借其卓越的视觉质量和渲染性能，已被广泛用于实时照片级渲染，但受限于带宽消耗问题。此外，作为自适应VV流传输的基础，现有基于密度的细节层级（LoD）方法并不适用于高斯表征，会导致明显的视觉间隙和严重的质量退化。近期研究还探索了属性压缩技术以降低带宽消耗。我们的前期研究表明，激进式属性压缩主要导致色彩失真，而这种失真可通过参考图像在渲染结果中有效校正。基于这些发现，我们提出了一种面向自适应VV流传输的新型色彩自适应方案，该方案采用向量量化（VQ）构建LoD，并利用低分辨率参考图像校正色彩失真。我们进一步提出CAGS——一种兼容多种高斯表征的自适应VV流传输系统，该系统通过流媒体服务器端渲染参考图像并在客户端执行色彩恢复来集成色彩自适应方案。在原型系统上的大量实验表明：在波动带宽条件下，CAGS的PSNR指标比现有自适应流传输系统提升5~20 dB；其运行速度显著优于现有可扩展高斯压缩方法；且能泛化适用于不同高斯表征。

---

