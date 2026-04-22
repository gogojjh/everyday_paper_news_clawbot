# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-04-22 08:04

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 4/20 篇提供

**🌟 Highlight**: 13 篇 | **📌 Poster**: 7 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. A Comparative Evaluation of Geometric Accuracy in NeRF and Gaussian Splatting

- **作者**: Mikolaj Zielinski, Eryk Vykysaly, Bartlomiej Biesiada, Jan Baturo, Mateusz Capala, Dominik Belter
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.18205v1)
- **发表日期**: 2026-04-20
- **匹配关键词**: neural rendering, object manipulation, nerf, gaussian splatting
- **arXiv**: [2604.18205v1](http://arxiv.org/abs/2604.18205v1)
- **📥 PDF**: 已下载至本地 (`2604.18205v1_A_Comparative_Evaluation_of_Geometric_Accuracy_in_NeRF_and_Gaussian_Splatting.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 神经渲染技术的最新进展催生了多种三维场景表示方法。尽管标准计算机视觉指标能够评估生成图像的视觉质量，却常常忽略表面几何结构的保真度。这一局限在机器人领域尤为关键，因为精确的几何结构对于抓取和物体操控等任务至关重要。本文提出了一套专注于几何精度的神经渲染方法评估流程，并构建了包含19个多样化场景的基准测试集。我们的方法能够从表面和形状保真度两个维度系统评估重建方法，从而对传统视觉评估指标形成有效补充。

---

### 2. Unmasking the Illusion of Embodied Reasoning in Vision-Language-Action Models

- **作者**: Haiweng Xu, Sipeng Zheng, Hao Luo, Wanpeng Zhang, Ziheng Xi, Zongqing Lu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.18000v1)
- **发表日期**: 2026-04-20
- **匹配关键词**: VLA, vision-language-action model, vision-language-action
- **arXiv**: [2604.18000v1](http://arxiv.org/abs/2604.18000v1)
- **📥 PDF**: 已下载至本地 (`2604.18000v1_Unmasking_the_Illusion_of_Embodied_Reasoning_in_Vision-Language-Action_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 近期视觉-语言-动作模型在标准机器人测试中展现出令人瞩目的成功率，这增强了对通用物理智能实现的乐观预期。然而最新研究表明，标准测试的成功率与真实具身推理能力存在系统性错位，引发了对高分是否反映真实认知能力的质疑。为填补这一研究空白，我们提出BeTTER基准测试框架——一个专门用于检验机器人策略中真实具身推理能力的诊断性基准。该框架通过实施针对性因果干预（如空间布局变换、时序外推）并强制运动学隔离，明确解耦高层推理失误与底层执行限制。系统性评估显示，当前最先进的视觉-语言-动作模型在动态场景中会出现灾难性失效，表现为严重的词汇-运动捷径依赖、行为惯性及语义特征坍缩。机制分析表明，这些症状源于根本性的架构瓶颈——如容量压缩与短视降采样——这些瓶颈系统性地削弱了模型的基础语义表征能力。我们论证了高度静态的评估方案通过允许模型过度拟合感觉运动先验，有效掩盖了这种表征退化现象。通过真实机器人实验验证，我们的研究证实这种表征崩溃并非仿真环境产物，强调未来视觉-语言-动作范式必须解决高频控制与高层推理之间的结构性矛盾。

---

### 3. Can Explicit Physical Feasibility Benefit VLA Learning? An Empirical Study

- **作者**: Yubai Wei, Chen Wu, Hashem Haghbayan
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.17896v1)
- **发表日期**: 2026-04-20
- **匹配关键词**: VLA, vision-language-action, obstacle avoidance
- **arXiv**: [2604.17896v1](http://arxiv.org/abs/2604.17896v1)
- **📥 PDF**: 已下载至本地 (`2604.17896v1_Can_Explicit_Physical_Feasibility_Benefit_VLA_Learning?_An_Empirical_Study.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作模型能够将多模态输入直接映射为机器人动作，通常通过大规模模仿学习进行训练。尽管该范式已展现出卓越性能，但当前主流的VLA训练流程并未对硬性物理约束（如避障或运动学可行性）进行显式监督。因此，物理可行行为背后的几何结构只能从演示数据中隐式推断。本文研究引入显式可行性监督能否为VLA策略提供有效的结构化指导。我们构建了一个基于几何基础的简易可行性目标，并将其整合到基于扩散的VLA策略训练阶段。为系统验证该思路，我们采用障碍物感知操作作为几何相关物理可行性的受控测试场景。实验结果表明，通过可行性监督增强VLA训练能同时提升物理可靠性与整体任务性能，并在低数据场景下提高学习效率。这些发现表明，显式可行性信号能有效补充基于模仿的VLA学习，凸显了其在开发更可靠VLA策略方面的潜力。

---

### 4. StableIDM: Stabilizing Inverse Dynamics Model against Manipulator Truncation via Spatio-Temporal Refinement

- **作者**: Kerui Li, Zhe Jing, Xiaofeng Wang, Zheng Zhu, Yukun Zhou, Guan Huang, Dongze Li, Qingkai Yang, Huaibo Huang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.17887v1)
- **发表日期**: 2026-04-20
- **匹配关键词**: VLA
- **arXiv**: [2604.17887v1](http://arxiv.org/abs/2604.17887v1)
- **📥 PDF**: 已下载至本地 (`2604.17887v1_StableIDM_Stabilizing_Inverse_Dynamics_Model_against_Manipulator_Truncation_via_Spatio-Temporal_Refi.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 逆动力学模型（IDMs）将视觉观测映射为底层动作指令，是具身人工智能中数据标注与策略执行的核心组件。然而在机械臂截断这种常见故障模式下，其性能会严重下降——该场景使状态恢复问题不适定并导致控制失稳。我们提出StableIDM，一种时空特征优化框架，通过精炼视觉输入特征来提升局部可观测条件下的动作预测稳定性。该框架融合三个互补模块：（1）辅助性机器人中心掩码机制以抑制背景干扰；（2）方向性特征聚合模块实现几何感知的空间推理，沿可见机械臂推断方向提取各向异性特征；（3）时序动态优化模块通过运动连续性平滑修正预测。大量实验验证了本方法的有效性：在AgiBot基准测试中，StableIDM在严重截断场景下将严格动作准确率提升12.1%；真实机器人回放任务中平均成功率提高9.7%。此外，在解码视频生成规划时端到端抓取成功率提升11.5%，作为自动标注器使用时下游视觉语言动作模型的真实机器人成功率提升17.6%。这些结果表明，StableIDM为具身人工智能的策略执行与数据生成提供了鲁棒且可扩展的基础架构。

---

### 5. ST-$π$: Structured SpatioTemporal VLA for Robotic Manipulation

- **作者**: Chuanhao Ma, Hanyu Zhou, Shihan Peng, Yan Li, Tao Gu, Luxin Yan
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.17880v1)
- **发表日期**: 2026-04-20
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2604.17880v1](http://arxiv.org/abs/2604.17880v1)
- **📥 PDF**: 已下载至本地 (`2604.17880v1_ST-$π$_Structured_SpatioTemporal_VLA_for_Robotic_Manipulation.pdf`)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/chuanhaoma/ST-pi.
- **中文摘要**: 视觉-语言-动作（VLA）模型在通用机器人任务上已取得显著成功，但在细粒度时空操作方面仍面临挑战。现有方法通常将时空知识嵌入视觉与动作表征中，并直接通过跨模态映射进行步级动作预测。然而，这种时空推理过程大多隐式进行，难以处理具有明确时空边界的多段连续行为。为此，我们提出ST-$π$——一种面向机器人操作的**结构化时空VLA模型**。该模型基于两项核心设计：1）**时空视觉语言模型**：我们将四维观测数据与任务指令编码至潜在空间，并输入大语言模型以生成由子任务、空间定位与时间定位构成的因果有序的**块级动作提示序列**；2）**时空动作专家模块**：在块级动作提示的引导下，我们设计了结构化双生成器指导机制，联合建模空间依赖性与时间因果性，从而预测步级动作参数。在此结构化框架中，视觉语言模型显式规划全局时空行为，动作专家模块则进一步细化局部时空控制。此外，我们构建了带有结构化时空标注的真实世界机器人数据集用于微调。大量实验验证了模型的有效性。代码链接：https://github.com/chuanhaoma/ST-pi。

---

### 6. OFlow: Injecting Object-Aware Temporal Flow Matching for Robust Robotic Manipulation

- **作者**: Kuanning Wang, Ke Fan, Chenhao Qiu, Zeyu Shangguan, Yuqian Fu, Yanwei Fu, Daniel Seita, Xiangyang Xue
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.17876v1)
- **发表日期**: 2026-04-20
- **匹配关键词**: VLA
- **arXiv**: [2604.17876v1](http://arxiv.org/abs/2604.17876v1)
- **📥 PDF**: 已下载至本地 (`2604.17876v1_OFlow_Injecting_Object-Aware_Temporal_Flow_Matching_for_Robust_Robotic_Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 稳健的机器人操作不仅需要预测场景随时间的变化，还需在复杂场景中识别任务相关对象。然而，现有视觉语言动作模型面临两大局限：通常仅基于当前帧执行动作，而未来预测与对象感知推理往往在不同潜在空间中分别学习。我们提出OFlow框架——将对象感知时序流匹配注入视觉语言动作模型，通过在共享语义潜在空间中统一时序预见与对象感知推理，同时解决这两项局限。该方法使用时序流匹配预测未来潜在状态，将其分解为强调物理相关线索、过滤任务无关变化的对象感知表征，并基于这些预测生成连续动作。通过将OFlow集成至视觉语言动作模型流程，我们的方法能在分布偏移下实现更可靠的控制。在LIBERO、LIBERO-Plus、MetaWorld和SimplerEnv基准测试及实际任务中的大量实验表明，对象感知预见能力能持续提升系统的鲁棒性与任务成功率。

---

### 7. ReFineVLA: Multimodal Reasoning-Aware Generalist Robotic Policies via Teacher-Guided Fine-Tuning

- **作者**: Tuan Van Vo, Tan Q. Nguyen, Khang Nguyen, Nhat Xuan Tran, Duy H. M. Nguyen, An T. Le, Ngo Anh Vien, Minh Nhat Vu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.17800v1)
- **发表日期**: 2026-04-20
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2604.17800v1](http://arxiv.org/abs/2604.17800v1)
- **📥 PDF**: 已下载至本地 (`2604.17800v1_ReFineVLA_Multimodal_Reasoning-Aware_Generalist_Robotic_Policies_via_Teacher-Guided_Fine-Tuning.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型因其能够将多模态观察与语言指令转化为期望的机器人动作而受到研究界的广泛关注。尽管取得了进展，VLA模型往往忽视显式推理，仅学习功能性的输入-动作映射，忽略了关键的逻辑步骤，这在复杂、长时程操作任务的可解释性和泛化能力方面尤为明显。本研究提出ReFineVLA，一种多模态推理感知框架，通过教师引导的推理对VLA模型进行微调。我们首先利用专家教师模型生成的推理依据增强机器人数据集，引导VLA模型学习对其动作进行推理。随后，通过ReFineVLA框架使用推理增强数据集对预训练的VLA模型进行微调，在保持基础泛化能力的同时提升推理能力。我们还通过注意力图可视化分析ReFineVLA在视觉观察、语言提示与待执行动作之间的对齐关系，表明模型能够聚焦于相关任务和动作。通过这一额外步骤，我们发现经ReFineVLA训练的模型在视觉-语言与动作领域之间展现出有意义的关联性，突显了增强的多模态理解与泛化能力。在SimplerEnv仿真环境中，通过WidowX和Google Robot任务的一系列操作基准测试评估，ReFineVLA在WidowX基准和Google Robot任务中均取得优于次优方法的成功率，实现了最先进的性能表现。

---

### 8. AnchorRefine: Synergy-Manipulation Based on Trajectory Anchor and Residual Refinement for Vision-Language-Action Models

- **作者**: Tingzheng Jia, Kan Guo, Lanping Qian, Yongli Hu, Daxin Tian, Guixian Qu, Chunmian Lin, Baocai Yin, Jiapu Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.17787v1)
- **发表日期**: 2026-04-20
- **匹配关键词**: VLA, vision-language-action model, vision-language-action
- **arXiv**: [2604.17787v1](http://arxiv.org/abs/2604.17787v1)
- **📥 PDF**: 已下载至本地 (`2604.17787v1_AnchorRefine_Synergy-Manipulation_Based_on_Trajectory_Anchor_and_Residual_Refinement_for_Vision-Lang.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 精度要求极高的操作任务既需要全局轨迹规划，也需要局部执行校正，然而多数视觉-语言-动作（VLA）策略在单一统一空间内生成动作。这种整体化建模方式迫使宏观层面的移动与微观层面的精细调整必须在同一目标下进行优化，导致大幅动作主导学习过程，而压制了微小却对防失败至关重要的校正信号。相比之下，人类操作行为遵循着全局运动规划与执行中持续局部调整相结合的结构原则。受此启发，我们提出AnchorRefine分层框架，将VLA动作建模分解为轨迹锚点预测与残差精细化校正两个阶段。锚点规划器负责生成粗略运动框架，精细化模块则通过校正执行层面的偏差来提升几何定位与接触精度。我们还设计了决策感知的夹爪精细化机制，以更好地捕捉夹爪控制中离散且边界敏感的特性。在LIBERO、CALVIN仿真任务及真实机器人实验中的结果表明，AnchorRefine能持续提升基于回归和基于扩散的两类VLA基础模型性能，在仿真任务中成功率最高提升7.8%，在真实场景中成功率最高提升18%。

---

### 9. HyKey: Hyperspectral Keypoint Detection and Matching in Minimally Invasive Surgery

- **作者**: Alexander Saikia, Chiara Di Vece, Zhehua Mao, Sierra Bonilla, Chloe He, Joao Ramalhinho, Tobias Czempiel, Sophia Bano, Danail Stoyanov
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.17446v1)
- **发表日期**: 2026-04-19
- **匹配关键词**: 3d reconstruction, 3D reconstruction
- **arXiv**: [2604.17446v1](http://arxiv.org/abs/2604.17446v1)
- **📥 PDF**: 已下载至本地 (`2604.17446v1_HyKey_Hyperspectral_Keypoint_Detection_and_Matching_in_Minimally_Invasive_Surgery.pdf`)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/alexsaikia/HyKey-Hyperspectral-Keypoint-Detection
- **中文摘要**: 目的：在微创手术中，三维重建通过增强可视化、工具追踪和扩展现实技术，能够提升手术引导效果。然而，传统的基于RGB的关键点检测与匹配流程在应对手术场景中的挑战时存在困难，例如纹理贫乏和光照复杂。本研究探讨使用快照式高光谱成像是否能在手术场景的关键点检测与匹配方面提供更优结果。方法：我们开发了HyKey模型，这是一种高光谱关键点检测与描述模型，由混合3D-2D卷积神经网络构成，能够从高光谱图像中联合提取空间-光谱特征。该模型通过在机器人采集的双摄像头RGB-HSI腹腔镜离体器官数据集（包含标定相机位姿）上，采用合成单应性增强和对极几何约束进行训练。我们将其性能与现有基于RGB的方法（包括SuperPoint和ALIKE）进行了基准比较。结果：我们的基于HSI的模型在配准的RGB帧上表现优于RGB基线方法，实现了96.62%的平均匹配准确率和67.18%的位姿估计10度平均准确率，在多项评估指标上均展现出持续改进。结论：整合高光谱立方体的光谱信息为微创手术中稳健的单目三维重建提供了有前景的解决方案，通过增强光谱-空间特征区分能力，有效应对纹理贫乏手术环境的局限性。我们的模型和数据集已公开于https://github.com/alexsaikia/HyKey-Hyperspectral-Keypoint-Detection。

---

### 10. A Rapid Deployment Pipeline for Autonomous Humanoid Grasping Based on Foundation Models

- **作者**: Yifei Yan, Yankai Liao, Linqi Ye
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.17258v1)
- **发表日期**: 2026-04-19
- **匹配关键词**: 3d reconstruction, 3D reconstruction
- **arXiv**: [2604.17258v1](http://arxiv.org/abs/2604.17258v1)
- **📥 PDF**: 已下载至本地 (`2604.17258v1_A_Rapid_Deployment_Pipeline_for_Autonomous_Humanoid_Grasping_Based_on_Foundation_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 部署人形机器人操作新物体传统上需要一到两天的工作量：数据收集、手动标注、三维模型获取和模型训练。本文提出了一种端到端的快速部署流程，该流程整合了三个基础模型组件，将新物体的上机周期缩短至约30分钟：（i）基于Roboflow的自动标注辅助训练YOLOv8物体检测器；（ii）基于Meta SAM 3D的三维重建，无需专用激光扫描仪；（iii）基于FoundationPose的零样本六自由度姿态跟踪，直接使用SAM~3D生成的网格作为模板。估计的姿态驱动基于Unity的逆运动学规划器，其关节指令通过UDP流传输至Unitree~G1人形机器人，并通过Unitree SDK执行。我们展示了mAP@0.5 = 0.995的检测精度、$σ< 1.05$ mm的姿态跟踪精度，以及在机器人工作空间内五个位置成功实现抓取。我们进一步在汽车车窗涂胶任务中验证了该流程的通用性。结果表明，将感知基础模型与日常成像设备（如智能手机）相结合，能够显著降低人形机器人操作任务的部署门槛。

---

### 11. OneVL: One-Step Latent Reasoning and Planning with Vision-Language Explanation

- **作者**: Jinghui Lu, Jiayi Guan, Zhijian Huang, Jinlong Li, Guang Li, Lingdong Kong, Yingyan Li, Han Wang, Shaoqing Xu, Yuechen Luo, Fang Li, Chenxu Dang, Junli Wang, Tao Xu, Jing Wu, Jianhua Wu, Xiaoshuai Hao, Wen Zhang, Tianyi Jiang, Lingfeng Zhang, Lei Zhou, Yingbo Tang, Jie Wang, Yinfeng Gao, Xizhou Bu, Haochen Tian, Yihang Qiu, Feiyang Jia, Lin Liu, Yigu Ge, Hanbing Li, Yuannan Shen, Jianwei Cui, Hongwei Xie, Bing Wang, Haiyang Sun, Jingwei Zhao, Jiahui Huang, Pei Liu, Zeyu Zhu, Yuncheng Jiang, Zibin Guo, Chuhong Gong, Hanchao Leng, Kun Ma, Naiyang Wang, Guang Chen, Kuiyuan Yang, Hangjun Ye, Long Chen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.18486v1)
- **发表日期**: 2026-04-20
- **匹配关键词**: VLA
- **arXiv**: [2604.18486v1](http://arxiv.org/abs/2604.18486v1)
- **📥 PDF**: 已下载至本地 (`2604.18486v1_OneVL_One-Step_Latent_Reasoning_and_Planning_with_Vision-Language_Explanation.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://xiaomi-embodied-intelligence.github.io/OneVL
- **中文摘要**: 思维链推理已成为基于视觉语言模型的自动驾驶轨迹预测的强大驱动力，但其自回归特性带来的延迟成本使其难以实现实时部署。潜在思维链方法试图通过将推理过程压缩至连续隐状态来弥补这一差距，但其性能始终未能超越显式推理方法。我们认为，这源于纯语言潜在表征仅压缩了世界的符号化抽象，而非实际支配驾驶行为的因果动态。为此，我们提出OneVL（基于视觉语言解释的单步潜在推理与规划框架），这是一个融合视觉语言模型与世界模型的统一架构，通过双辅助解码器监督的紧凑潜在标记实现推理路径规划。在重构文本思维链的语言解码器基础上，我们引入了视觉世界模型解码器来预测未来帧标记，迫使潜在空间内化道路几何、智能体运动与环境变化的因果动态。通过三阶段训练流程逐步对齐轨迹、语言与视觉目标，确保稳定的联合优化。在推理阶段，辅助解码器被移除，所有潜在标记通过单次并行前向传播完成预填充，实现与纯答案预测相当的速度。在四个基准测试中，OneVL成为首个超越显式思维链的潜在推理方法，在保持纯答案预测延迟的同时达到最先进的准确率，并直接证明：在语言与世界模型双重监督指导下，更紧密的压缩比逐标记的冗长推理能产生更具泛化能力的表征。项目页面：https://xiaomi-embodied-intelligence.github.io/OneVL

---

### 12. XEmbodied: A Foundation Model with Enhanced Geometric and Physical Cues for Large-Scale Embodied Environments

- **作者**: Kangan Qian, ChuChu Xie, Yang Zhong, Jingrui Pang, Siwen Jiao, Sicong Jiang, Zilin Huang, Yunlong Wang, Kun Jiang, Mengmeng Yang, Hao Ye, Guanghao Zhang, Hangjun Ye, Guang Chen, Long Chen, Diange Yang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.18484v1)
- **发表日期**: 2026-04-20
- **匹配关键词**: VLA, affordance, vision-language-action
- **arXiv**: [2604.18484v1](http://arxiv.org/abs/2604.18484v1)
- **📥 PDF**: 已下载至本地 (`2604.18484v1_XEmbodied_A_Foundation_Model_with_Enhanced_Geometric_and_Physical_Cues_for_Large-Scale_Embodied_Envi.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型驱动着新一代自主系统，但其训练需要来自复杂环境的大规模高质量标注。当前云端处理流程依赖通用的视觉-语言模型（VLM），这些模型因其二维图像-文本预训练而缺乏几何推理和领域语义理解能力。为解决这一不匹配问题，我们提出XEmbodied——一种云端基础模型，通过赋予VLM内在的三维几何感知能力，使其能与物理线索（如占据栅格、三维边界框）进行交互。XEmbodied并非将几何信息作为辅助输入，而是通过结构化三维适配器整合几何表征，并利用高效图像-具身适配器将物理信号提炼为上下文标记。通过渐进式领域课程学习和强化学习后训练，XEmbodied在保持通用能力的同时，在18个公共基准测试中展现出稳健性能。该模型显著提升了空间推理、交通语义理解、具身可供性感知以及分布外泛化能力，为大规模场景挖掘和具身视觉问答任务提供了有力支撑。

---

### 13. Instruction-as-State: Environment-Guided and State-Conditioned Semantic Understanding for Embodied Navigation

- **作者**: Zhen Liu, Yuhan Liu, Jinjun Wang, Jianyi Liu, Wei Song, Jingwen Fu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.18223v1)
- **发表日期**: 2026-04-20
- **匹配关键词**: vision-and-language navigation, navigation, VLN
- **arXiv**: [2604.18223v1](http://arxiv.org/abs/2604.18223v1)
- **📥 PDF**: 已下载至本地 (`2604.18223v1_Instruction-as-State_Environment-Guided_and_State-Conditioned_Semantic_Understanding_for_Embodied_Na.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉与语言导航任务要求智能体在视觉动态变化的环境中遵循自然语言指令进行导航。其核心挑战在于语言与观察之间的动态耦合关系：随着智能体视野与空间环境的演变，指令的含义也会发生相应变化。然而，现有许多模型将指令编码为静态全局表征，限制了其根据当前视觉语境调整指令理解的能力。为此，我们将指令理解建模为"指令即状态"变量：这是一种与决策相关的、基于词元层级的指令状态，该状态随着智能体感知状态的变化而逐步演化，其中感知状态表示每一步基于观察的导航语境。

为实现这一原理，我们提出了状态耦合的环境引导指令理解框架——一种从粗粒度到细粒度的状态条件化分段激活与词元级语义优化框架。在粗粒度层面，该框架会激活与当前观察语义对齐的指令片段；在细粒度层面，则通过观察引导的词元定位与语境建模对激活片段进行语义优化，使其在当前观察条件下形成更精确的内部语义表征。这两个阶段共同维护着在导航过程中随智能体感知状态持续更新的指令状态。

该框架在多项关键指标上表现出色：在REVERIE测试集的未见场景中实现了+2.68%的SPL提升，并在多个视觉与语言导航基准测试中展现出持续的性能增益，充分验证了动态指令-感知耦合机制的重要价值。

---

## 📌 Poster

*其他相关研究*

---

### 1. DAG-STL: A Hierarchical Framework for Zero-Shot Trajectory Planning under Signal Temporal Logic Specifications

- **作者**: Ruijia Liu, Ancheng Hou, Xiao Yu, Xiang Yin
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.18343v1)
- **发表日期**: 2026-04-20
- **匹配关键词**: navigation, navigation and manipulation
- **arXiv**: [2604.18343v1](http://arxiv.org/abs/2604.18343v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 信号时序逻辑（STL）是一种用于描述时序结构化机器人任务的强大语言。当系统动力学和环境结构无法通过解析方式获取时，在STL约束下规划可执行轨迹仍然具有挑战性。现有方法通常假设存在显式模型或学习特定任务行为，这限制了其对未见STL任务的零样本泛化能力。本研究利用与任务无关的轨迹数据，探索在未知动力学下的离线STL规划问题。我们的核心设计理念是将逻辑推理与轨迹实现相分离。通过DAG-STL这一分层框架，我们将长时域STL规划转化为三个阶段：首先将STL公式分解为通过共享时序约束连接的可达性与不变性进度条件；随后利用学习得到的可达时间估计分配定时路径点；最后通过基于扩散的生成器合成这些路径点间的轨迹。这种“分解-分配-生成”流程将全局规划简化为更短且更具支撑性的子问题。为弥合规划层正确性与执行层可行性之间的差距，我们进一步提出免展开的动态一致性度量方法、基于有限预算改进多分配假设的随时优化搜索流程，以及用于执行时恢复的分层在线重规划机制。在Maze2D、OGBench AntMaze和立方体领域的实验表明，DAG-STL在复杂长时域STL任务上显著优于直接鲁棒性引导扩散方法，并在导航与操作场景中展现出良好的泛化能力。在基于优化参考的自定义环境中，DAG-STL能恢复大多数模型可解任务，同时相较于基于显式系统模型的直接优化方法保持显著计算优势。

---

### 2. Enhancing Glass Surface Reconstruction via Depth Prior for Robot Navigation

- **作者**: Jiamin Zheng, Jingwen Yu, Guangcheng Chen, Hong Zhang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.18336v1)
- **发表日期**: 2026-04-20
- **匹配关键词**: navigation, robot navigation
- **arXiv**: [2604.18336v1](http://arxiv.org/abs/2604.18336v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: GITHUB
  - 链接：https://github.com/jarvisyjw/GlassRecon.
- **中文摘要**: 室内机器人导航常因玻璃表面而受阻，这些表面会严重干扰深度传感器的测量精度。尽管如Depth Anything 3等基础模型能提供出色的几何先验信息，但它们缺乏绝对度量尺度。我们提出了一种无需训练的框架，利用深度基础模型作为结构先验，通过鲁棒的局部RANSAC对齐方法将其与原始传感器深度数据融合。这种方法自然避免了玻璃区域错误测量的干扰，并恢复了精确的度量尺度。此外，我们引入了\ti{GlassRecon}——一个新颖的RGB-D数据集，其中包含基于几何推导的玻璃区域真实标注。大量实验证明，我们的方法在各项指标上均优于现有先进基线，尤其在传感器深度数据严重受损的情况下表现突出。该数据集及相关代码将在https://github.com/jarvisyjw/GlassRecon发布。

---

### 3. EmbodiedLGR: Integrating Lightweight Graph Representation and Retrieval for Semantic-Spatial Memory in Robotic Agents

- **作者**: Paolo Riva, Leonardo Gargani, Matteo Frosi, Matteo Matteucci
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.18271v1)
- **发表日期**: 2026-04-20
- **匹配关键词**: human-robot interaction
- **arXiv**: [2604.18271v1](http://arxiv.org/abs/2604.18271v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 随着应用于机器人领域的智能体人工智能不断发展，对能够高效构建和检索记忆与观察的智能体需求日益增长。在复杂环境中运行的机器人必须建立记忆结构，通过利用当前操作情境的记忆表征来实现有效的人机交互。与机器人交互的用户可能期望具身智能体能够提供关于位置、事件或物体的信息，这要求智能体在类人推理时间内提供精确答案，以展现响应能力。我们提出具身轻量图检索智能体（EmbodiedLGR-Agent），这是一种由视觉语言模型驱动的智能体架构，能够构建机器人操作环境的密集高效表征。该架构通过基于参数高效视觉语言模型的混合构建-检索方法，将物体及其位置的低层级信息存储在语义图中，同时通过传统检索增强架构保留对观察场景的高层级描述，从而直接满足对环境进行高效记忆表征的需求。在NaVQA数据集上的评估表明，EmbodiedLGR-Agent在推理和查询时间方面达到具身智能体的最先进水平，同时在全局任务准确率上保持与当前最优方法的竞争力。此外，该智能体已成功部署于实体机器人，通过在本地运行视觉语言模型及构建-检索流程，在人机交互场景中展现出实际应用价值。

---

### 4. COFFAIL: A Dataset of Successful and Anomalous Robot Skill Executions in the Context of Coffee Preparation

- **作者**: Alex Mitrevski, Ayush Salunke
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.18236v1)
- **发表日期**: 2026-04-20
- **匹配关键词**: bimanual manipulation
- **arXiv**: [2604.18236v1](http://arxiv.org/abs/2604.18236v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 在机器人操作学习的背景下，精心策划的数据集是推动技术前沿发展的重要资源；然而，现有数据集通常仅包含成功执行案例，或专注于特定类型的技能。本文简要介绍了一个围绕咖啡制作场景收集的多样化技能数据集。该数据集被命名为COFFAIL，包含在厨房环境中由实体机器人采集的成功与异常技能执行片段，其中部分片段采用双手协同操作方式完成。除描述数据采集设置与收集内容外，本文还展示了如何利用COFFAIL数据集通过模仿学习来训练机器人策略。

---

### 5. Continuous Focus Groups: A Longitudinal Method for Clinical HRI in Autism Care

- **作者**: Ghiglino Davide, Foglino Caterina, Wykowska Agnieszka
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.18197v1)
- **发表日期**: 2026-04-20
- **匹配关键词**: HRI, human-robot interaction
- **arXiv**: [2604.18197v1](http://arxiv.org/abs/2604.18197v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 定性方法与定量方法结合使用对改善人机交互至关重要，但现有定性研究往往采用静态或一次性形式，难以捕捉利益相关方观点随时间演变的过程。这一局限在临床情境中尤为突出，因为患者家庭面临沉重负担，难以反复参与研究。为弥补这一空白，我们提出持续性焦点小组法——一种纵向协同研究方法，旨在与从事自闭症谱系障碍儿童辅助护理的专业人员保持持续对话。我们在机器人辅助治疗方案的连续阶段组织了三个焦点小组，使参与者能够在干预推进过程中重新审视并完善先前观点。研究结果表明：持续性机制不仅促进了信任建立，支持将隐性临床经验融入设计决策，还通过允许参与者重新协商参与程度、提出新关切，发挥了伦理保障功能。通过将家庭、儿童和临床医生的治疗迭代过程与研究者、开发者的研究设计迭代相衔接，持续性焦点小组法构建了一种兼具实践可行性与设计严谨性的方法论贡献。除自闭症护理领域外，该方法为推进人机交互定性研究提供了可迁移框架，尤其适用于用户直接参与受限且连续性至关重要的敏感领域。

---

### 6. Chatting about Conditional Trajectory Prediction

- **作者**: Yuxiang Zhao, Wei Huang, Haipeng Zeng, Huan Zhao, Yujie Song
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.18126v1)
- **发表日期**: 2026-04-20
- **匹配关键词**: path planning, motion planning
- **arXiv**: [2604.18126v1](http://arxiv.org/abs/2604.18126v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 人类行为具有相互依赖的特性，这要求人机交互系统能够通过建模复杂的社会交互来预测周围智能体的轨迹，从而避免碰撞并执行安全的路径规划。尽管已有多种轨迹预测方法，但大多数方法未考虑自车智能体自身的运动状态，仅基于静态信息进行交互建模。受人类在轨迹选择过程中心智理论启发，我们提出一种跨时域意图交互的条件轨迹预测方法（CiT）。该方法通过联合分析随时间变化的行为意图，实现了不同时域间的信息互补与融合——自身时域的意图可通过另一时域的社会交互信息进行修正，从而获得更精确的意图表征。此外，CiT设计紧密衔接机器人运动规划与控制模块，能够基于自车智能体的潜在运动状态，为所有周围智能体生成一组可选的轨迹预测结果。大量实验表明，所提出的CiT方法显著优于现有方法，在基准测试中达到了最先进的性能水平。

---

### 7. A Hamilton-Jacobi Reachability-Guided Search Framework for Efficient and Safe Indoor Planar Robot Navigation

- **作者**: Hanyang Hu, Cameron Siu, Mo Chen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.17679v1)
- **发表日期**: 2026-04-20
- **匹配关键词**: navigation, robot navigation, autonomous navigation
- **arXiv**: [2604.17679v1](http://arxiv.org/abs/2604.17679v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 自主导航需要在复杂且可能动态的环境中规划出一条安全高效的路径以抵达目标。基于图搜索的算法因其通用性及配备可采纳启发式时的理论保证而被广泛采用。然而，图搜索的计算复杂度随搜索空间维度迅速增长，常使动态环境中的实时规划难以实现。本文结合离线汉密尔顿-雅可比可达性分析与在线图搜索，以发挥两者的互补优势。预计算的汉密尔顿-雅可比值函数作为信息启发式与主动安全约束，分摊了图搜索过程的在线计算量。同时，图搜索使基于可达性的推理能够融入在线规划，克服了汉密尔顿-雅可比可达性分析需完全掌握环境信息的长期挑战。大量仿真实验与真实场景测试表明，无论环境中是否存在行人，所提方法在规划效率与导航安全性方面均持续优于基线方法。

---

