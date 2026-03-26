# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-03-26 08:04

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 5/20 篇提供

**🌟 Highlight**: 19 篇 | **📌 Poster**: 1 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. A Multimodal Framework for Human-Multi-Agent Interaction

- **作者**: Shaid Hasan, Breenice Lee, Sujan Sarker, Tariq Iqbal
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.23271v1)
- **发表日期**: 2026-03-24
- **匹配关键词**: exploration, human-robot interaction
- **arXiv**: [2603.23271v1](http://arxiv.org/abs/2603.23271v1)
- **📥 PDF**: 已下载至本地 (`2603.23271v1_A_Multimodal_Framework_for_Human-Multi-Agent_Interaction.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 人机交互正日益向多机器人、社会性环境方向发展。现有系统难以将多模态感知、具身表达与协调决策整合到统一框架中，这限制了共享物理空间中自然且可扩展的交互。为此，我们提出一种人机多智能体交互的多模态框架，其中每个机器人作为自主认知体运行，具备整合的多模态感知能力，并依托具身基础采用大语言模型驱动的规划机制。在团队层面，集中式协调机制通过调控发言轮转与智能体参与度，有效避免语音重叠与行为冲突。该框架在两个人形机器人上实现，通过融合语音、手势、视线与移动的交互策略，实现了连贯的多智能体交互。典型交互案例展示了跨智能体的协调多模态推理能力及基于具身环境的响应生成。未来工作将聚焦于更大规模的用户研究，并深入探索社会性多智能体交互的动态机制。

---

### 2. Efficient Hybrid SE(3)-Equivariant Visuomotor Flow Policy via Spherical Harmonics for Robot Manipulation

- **作者**: Qinglun Zhang, Shen Cheng, Tian Dan, Haoqiang Fan, Guanghui Liu, Shuaicheng Liu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.23227v1)
- **发表日期**: 2026-03-24
- **匹配关键词**: diffusion policy
- **arXiv**: [2603.23227v1](http://arxiv.org/abs/2603.23227v1)
- **📥 PDF**: 已下载至本地 (`2603.23227v1_Efficient_Hybrid_SE(3)-Equivariant_Visuomotor_Flow_Policy_via_Spherical_Harmonics_for_Robot_Manipula.pdf`)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/zql-kk/E3Flow.
- **中文摘要**: 现有等变方法虽能提升数据效率，却存在计算强度高、依赖单模态输入、与快速采样方法结合时不稳定等局限。本研究提出E3Flow框架，首次成功将高效整流流与稳定的多模态等变学习相统一，有效解决了等变扩散策略的关键缺陷。该框架基于球谐函数表示构建，确保严格的SO(3)等变性。我们创新性地引入不变特征增强模块（FEM），动态融合点云与图像混合视觉模态，将丰富的视觉线索注入球谐特征。我们在MimicGen数据集的8个操作任务上评估E3Flow，并进一步开展4项真实环境实验验证其物理有效性。仿真结果表明，E3Flow在平均成功率上较当前最优的球面扩散策略（SDP）提升3.12%，同时实现7倍推理加速。这标志着E3Flow为机器人策略学习在性能、效率与数据效率之间实现了创新性的高效平衡。代码已开源：https://github.com/zql-kk/E3Flow。

---

### 3. Gaze-Regularized Vision-Language-Action Models for Robotic Manipulation

- **作者**: Anupam Pani, Yanchao Yang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.23202v1)
- **发表日期**: 2026-03-24
- **匹配关键词**: vision-language-action model, VLA, vision-language-action
- **arXiv**: [2603.23202v1](http://arxiv.org/abs/2603.23202v1)
- **📥 PDF**: 已下载至本地 (`2603.23202v1_Gaze-Regularized_Vision-Language-Action_Models_for_Robotic_Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 尽管视觉-语言-动作（VLA）模型已取得进展，但机器人操作在精细任务上仍面临挑战，因为现有模型缺乏主动视觉注意力分配的机制。人类注视行为天然编码了意图、规划与执行模式——这为引导机器人感知提供了强大的监督信号。我们提出一种注视正则化训练框架，在不改变模型结构或增加推理开销的前提下，使VLA模型的内部注意力与人类视觉模式对齐。该方法将时序聚合的注视热力图转化为区块级分布，通过KL散度对Transformer注意力进行正则化，从而建立面向任务相关特征的归纳偏置，同时保持部署效率。当集成到现有VLA架构时，我们的方法在多个操作基准测试中实现了4-12%的性能提升。注视正则化模型能以更少的训练步骤达到同等性能，并在光照变化和传感器噪声下保持鲁棒性。除性能指标外，学习到的注意力模式可生成反映人类策略的可视化结果，增强了机器人系统的可信度。此外，该框架无需眼动追踪设备，可直接应用于现有数据集。这些结果表明，人类感知先验能显著加速机器人学习，同时提升任务性能和系统可解释性。

---

### 4. VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models

- **作者**: Jintao Cheng, Haozhe Wang, Weibin Li, Gang Wang, Yipu Zhang, Xiaoyu Tang, Jin Wu, Xieyuanli Chen, Yunhui Liu, Wei Zhang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.22991v1)
- **发表日期**: 2026-03-24
- **匹配关键词**: vision-language-action model, VLA, vision-language-action
- **arXiv**: [2603.22991v1](http://arxiv.org/abs/2603.22991v1)
- **📥 PDF**: 已下载至本地 (`2603.22991v1_VLA-IAP_Training-Free_Visual_Token_Pruning_via_Interaction_Alignment_for_Vision-Language-Action_Mode.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://chengjt1999.github.io/VLA-IAP.github.io/
- **中文摘要**: 视觉-语言-动作（VLA）模型快速发展，推动了具身智能的进步，使机器人能够执行复杂的指令驱动任务。然而，随着模型容量和视觉上下文长度的增加，VLA系统的推理成本成为在资源受限平台上实际部署的主要瓶颈。现有的视觉标记剪枝方法主要依赖语义显著性或简单的时间线索，忽视了VLA任务的基本特性——持续的物理交互。因此，当前方法往往会剪除视觉上稀疏但在结构上对操作至关重要的区域，导致任务早期阶段行为不稳定。为解决这一问题，我们提出转向明确的“交互优先”范式。我们提出的**无需训练**的方法VLA-IAP（交互对齐剪枝）引入了几何先验机制以保留结构锚点，并采用动态调度策略，根据语义-运动对齐调整剪枝强度。这使得系统能够实现从保守到激进的过渡，确保在早期不确定性阶段的鲁棒性，并在交互锁定后提升效率。大量实验表明，VLA-IAP在LIBERO基准测试中实现了**97.8%的成功率**和**1.25倍的加速**，在保持性能**与未剪枝骨干网络相当**的同时，最高可实现**1.54倍的加速**。此外，该方法在多种模型架构、三个不同的仿真环境以及真实机器人平台上均表现出优越且一致的性能，验证了其强大的泛化能力和实际适用性。我们的项目网站为：\href{https://chengjt1999.github.io/VLA-IAP.github.io/}{VLA-IAP.com}。

---

### 5. Task-Aware Positioning for Improvisational Tasks in Mobile Construction Robots via an AI Agent with Multi-LMM Modules

- **作者**: Seongju Jang, Francis Baek, SangHyun Lee
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.22903v1)
- **发表日期**: 2026-03-24
- **匹配关键词**: navigation
- **arXiv**: [2603.22903v1](http://arxiv.org/abs/2603.22903v1)
- **📥 PDF**: 已下载至本地 (`2603.22903v1_Task-Aware_Positioning_for_Improvisational_Tasks_in_Mobile_Construction_Robots_via_an_AI_Agent_with_.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 由于建筑施工环境的多变性，现场许多任务以即兴方式展开。现有移动建造机器人的研究在应对即兴任务方面仍存在局限，这类任务所需的位置、发生时机及执行所需的上下文信息均无法预先获知。本研究提出一种智能体，能够理解自然语言描述的即兴任务，识别任务所需位置并自主定位。该智能体功能被分解为三个并行运行的大型多模态模型模块，分别实现基于LMM的任务解析与拆解、施工图纸导航，以及通过视觉推理识别非预设任务位置。研究采用四足机器人平台进行系统验证，在三项即兴任务处理测试中，该智能体识别任务位置并成功定位的准确率达到92.2%。本项研究为移动建造机器人自主执行非预设任务提供了可行方案。

---

### 6. Agile-VLA: Few-Shot Industrial Pose Rectification via Implicit Affordance Anchoring

- **作者**: Teng Yan, Zhengyang Pei, Chengyu Shi, Yue Yu, Yikun Chen, Zilong Zhu, Zelin Fang, Kaile Guo, Zihang Wang, Peigen Tian, Bingzhuo Zhong
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.22899v1)
- **发表日期**: 2026-03-24
- **匹配关键词**: VLA, affordance, vision-language-action
- **arXiv**: [2603.22899v1](http://arxiv.org/abs/2603.22899v1)
- **📥 PDF**: 已下载至本地 (`2603.22899v1_Agile-VLA_Few-Shot_Industrial_Pose_Rectification_via_Implicit_Affordance_Anchoring.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 在资源受限的边缘平台上部署视觉-语言-动作模型时，高频语义推理与动态操控所需的高频控制之间存在根本性矛盾。为解决这一挑战，本文提出Agile-VLA分层框架，专为NVIDIA Jetson Orin Nano等边缘设备的工业位姿重定向任务设计。其核心创新在于隐式可供性锚定机制，该机制直接将几何视觉线索（特别是质心与边缘关键点锚）映射为结构化参数化动作基元，从而在闭环控制中大幅降低对高延迟语义推理的依赖。通过异步双流架构实现感知（10Hz）与控制（50Hz）的解耦，系统有效缓解了基于边缘的机器人学习固有的频率失配问题。在标准六自由度机械臂上的实验结果表明，Agile-VLA仅需5次演示即可通过外在灵巧性实现对复杂不规则工件的稳健位姿校正。

---

### 7. Grounding Sim-to-Real Generalization in Dexterous Manipulation: An Empirical Study with Vision-Language-Action Models

- **作者**: Ruixing Jin, Zicheng Zhu, Ruixiang Ouyang, Sheng Xu, Bo Yue, Zhizheng Wu, Guiliang Liu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.22876v1)
- **发表日期**: 2026-03-24
- **匹配关键词**: vision-language-action model, VLA, vision-language-action
- **arXiv**: [2603.22876v1](http://arxiv.org/abs/2603.22876v1)
- **📥 PDF**: 已下载至本地 (`2603.22876v1_Grounding_Sim-to-Real_Generalization_in_Dexterous_Manipulation_An_Empirical_Study_with_Vision-Langua.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 学习灵巧操作的通用控制策略通常依赖于大规模数据集。鉴于现实世界数据收集成本高昂，一种实用的替代方案是通过仿真生成合成数据。然而，由此产生的合成数据往往与现实世界分布存在显著差异。尽管先前许多研究提出了弥合仿真与现实差异的算法，但仍缺乏将这些方法应用于现实世界操作任务的原则性研究，特别是对视觉-语言-动作（VLA）模型等通用策略的性能评估。本研究通过实证方法，从四个维度考察仿真到现实泛化的主要决定因素：多层级域随机化、照片级真实感渲染、物理真实建模以及强化学习更新。为支持这项研究，我们设计了一套综合评估方案，用于量化操作任务在现实世界中的性能表现。该方案考虑了背景、光照、干扰物、物体类型和空间特征等关键变量。通过超过一万次现实世界试验，我们获得了关于仿真到现实迁移的重要洞见。为促进未来研究发展，我们公开了机器人平台和评估方案，以便独立验证，从而为灵巧操作策略建立现实且标准化的基准。

---

### 8. CATNAV: Cached Vision-Language Traversability for Efficient Zero-Shot Robot Navigation

- **作者**: Aditya Potnis, Francisco Affonso, Shreya Gummadi, Naveen Kumar Uppalapati, Girish Chowdhary
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.22800v1)
- **发表日期**: 2026-03-24
- **匹配关键词**: robot navigation, navigation, vision-language-action
- **arXiv**: [2603.22800v1](http://arxiv.org/abs/2603.22800v1)
- **📥 PDF**: 已下载至本地 (`2603.22800v1_CATNAV_Cached_Vision-Language_Traversability_for_Efficient_Zero-Shot_Robot_Navigation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 在非结构化环境中导航需要评估相对于机器人物理能力的穿越风险，这一挑战因机器人具体形态而异。我们提出CATNAV——一种成本感知的可通行性导航框架，该框架利用多模态大语言模型实现零样本、形态感知的成本地图生成，无需针对特定任务进行训练。我们引入了视觉语义缓存机制，通过检测场景新颖性并复用语义相似帧的先前风险评估，将在线视觉语言模型查询量减少85.7%。此外，我们开发了基于视觉语言模型的轨迹选择模块，通过视觉推理评估候选路径，在给定行为约束条件下选择最安全路线。我们在四足机器人上对CATNAV进行了室内外非结构化环境测试，并与最先进的视觉-语言-动作基线方法进行比较。在五项导航任务中，CATNAV实现了平均目标到达率提升10个百分点，行为约束违反次数减少33%。

---

### 9. PhotoAgent: A Robotic Photographer with Spatial and Aesthetic Understanding

- **作者**: Lirong Che, Zhenfeng Gan, Yanbo Chen, Junbo Tan, Xueqian Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.22796v1)
- **发表日期**: 2026-03-24
- **匹配关键词**: gaussian splatting, 3D gaussian splatting
- **arXiv**: [2603.22796v1](http://arxiv.org/abs/2603.22796v1)
- **📥 PDF**: 已下载至本地 (`2603.22796v1_PhotoAgent_A_Robotic_Photographer_with_Spatial_and_Aesthetic_Understanding.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 从事摄影等创意任务的具身智能体，必须弥合高层级语言指令与几何控制之间的语义鸿沟。我们提出的PhotoAgent通过融合大型多模态模型推理与新型控制范式实现了这一目标。该智能体首先通过LMM驱动的思维链推理，将主观审美目标转化为可求解的几何约束，使解析求解器能够计算出高质量的初始拍摄视角。随后，借助基于3D高斯泼溅技术构建的光照真实内部世界模型，通过视觉反思对该初始位姿进行迭代优化。这种"心智模拟"机制替代了昂贵耗时的物理试错过程，实现了向美学更优结果的快速收敛。实验评估证实，PhotoAgent在空间推理方面表现卓越，并能获得更优的最终图像质量。

---

### 10. Instrument-Splatting++: Towards Controllable Surgical Instrument Digital Twin Using Gaussian Splatting

- **作者**: Shuojue Yang, Zijian Wu, Chengjiaao Liao, Qian Li, Daiyun Shen, Chang Han Low, Septimiu E. Salcudean, Yueming Jin
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.22792v1)
- **发表日期**: 2026-03-24
- **匹配关键词**: gaussian splatting, 3D gaussian splatting
- **arXiv**: [2603.22792v1](http://arxiv.org/abs/2603.22792v1)
- **📥 PDF**: 已下载至本地 (`2603.22792v1_Instrument-Splatting++_Towards_Controllable_Surgical_Instrument_Digital_Twin_Using_Gaussian_Splattin.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 高质量且可控的手术器械数字孪生体对于机器人辅助手术中的真实到仿真（Real2Sim）至关重要，它们能够实现新颖姿态下的逼真模拟、合成数据生成和感知学习。我们提出Instrument-Splatting++，一种单目三维高斯泼溅（3DGS）框架，可将手术器械重建为具有高保真度的完全可控高斯资产。我们的流程始于部件级几何预训练，将CAD先验知识注入高斯基元，并通过部件感知语义渲染增强表征能力。基于预训练模型，我们提出语义感知姿态估计与跟踪（SAPET）方法，从无位姿标注的内窥镜视频中恢复每帧的六自由度位姿和关节角度——其中完全基于合成语义训练的夹钳尖端网络提供鲁棒监督，而宽松正则化机制则抑制异常关节状态。最后，我们引入鲁棒纹理学习（RTL）方法，通过交替执行位姿优化与鲁棒外观学习，有效缓解纹理学习过程中的位姿噪声干扰。该框架能够从无位姿视频中同时实现姿态估计与真实纹理学习。我们在EndoVis17/18、SAR-RARP及内部数据集提取的序列上验证了本方法，相较于现有先进基线展现出更优的光度学质量与几何精度。我们进一步展示了在下游关键点检测任务中，利用可控器械高斯模型生成的新视角数据增强能有效提升模型性能。

---

### 11. DiSCo: Diffusion Sequence Copilots for Shared Autonomy

- **作者**: Andy Wang, Xu Yan, Brandon McMahan, Michael Zhou, Yuyang Yuan, Johannes Y. Lee, Ali Shreif, Matthew Li, Zhenghao Peng, Bolei Zhou, Yuchen Cui, Jonathan C. Kao
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.22787v1)
- **发表日期**: 2026-03-24
- **匹配关键词**: diffusion policy
- **arXiv**: [2603.22787v1](http://arxiv.org/abs/2603.22787v1)
- **📥 PDF**: 已下载至本地 (`2603.22787v1_DiSCo_Diffusion_Sequence_Copilots_for_Shared_Autonomy.pdf`)
- **🔓 开源**: PROJECT_PAGE
- **中文摘要**: 共享自主性结合了人类用户与AI副驾驶的操作，共同控制机器人手臂等复杂系统。当任务具有挑战性、需要高维度控制或面临干扰时，共享自主性可通过训练有素的副驾驶以符合用户目标的方式有效修正用户操作，从而显著提升任务执行效果。为大幅提升共享自主性的性能，我们提出扩散序列副驾驶（DiSCo）：这是一种结合扩散策略的共享自主方法，能够规划与用户历史操作保持一致的行动序列。DiSCo通过用户提供的操作进行扩散过程的种子生成与修复，并利用超参数平衡专家操作遵循度、用户意图对齐度及系统响应感知度。实验证明，DiSCo在模拟驾驶和机器人手臂任务中显著提升了任务执行性能。项目网站：https://sites.google.com/view/disco-shared-autonomy/

---

### 12. SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation

- **作者**: Ruisen Tu, Arth Shukla, Sohyun Yoo, Xuanlin Li, Junxi Li, Jianwen Xie, Hao Su, Zhuowen Tu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.22760v1)
- **发表日期**: 2026-03-24
- **匹配关键词**: mobile manipulation, vision-language-action model, VLA, affordance, vision-language-action
- **arXiv**: [2603.22760v1](http://arxiv.org/abs/2603.22760v1)
- **📥 PDF**: 已下载至本地 (`2603.22760v1_SG-VLA_Learning_Spatially-Grounded_Vision-Language-Action_Models_for_Mobile_Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型在机器人控制领域展现出潜力，但在复杂家庭环境中的表现仍不尽如人意。移动操作任务需同时理解全局场景布局、细粒度几何结构和高维连续动作空间，这使得标准模仿学习方法难以胜任。我们提出一种空间感知增强的VLA模型学习框架，通过辅助任务协同训练与多模态输入增强来强化感知与表征能力。该方法针对包含协调底盘运动、机械臂关节控制与夹爪操作的13维动作空间控制难题，构建了多视角RGB观测、深度信息与短时序历史相结合的多模态输入体系，同时捕捉全局场景结构与局部操作上下文。为提升表征质量，我们协同训练辅助解码器，从共享的视觉-语言特征中重构可解释的中间信号——包括全局机器人位姿、关节构型、抓取可操作性、目标物体相对位姿及分割掩码。这些目标函数通过密集监督促使骨干网络形成具有空间基础且感知操作意图的潜在表征。在家庭重排列任务上的大量实验表明，该方法在拾取、放置、开启、关闭等操作中均取得稳定提升，显著优于直接模仿学习方法。我们的研究证实，通过辅助任务与多模态学习实现空间感知增强，为VLA模型向通用家庭机器人方向扩展提供了有效路径。

---

### 13. Learning Safe-Stoppability Monitors for Humanoid Robots

- **作者**: Yifan Sun, Yiyuan Pan, Shangtao Li, Caiwu Ding, Tao Cui, Lingyun Wang, Changliu Liu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.22703v1)
- **发表日期**: 2026-03-24
- **匹配关键词**: exploration
- **arXiv**: [2603.22703v1](http://arxiv.org/abs/2603.22703v1)
- **📥 PDF**: 已下载至本地 (`2603.22703v1_Learning_Safe-Stoppability_Monitors_for_Humanoid_Robots.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 紧急停止机制是机器人安全领域的实际标准。然而对于人形机器人而言，突然切断电源本身可能导致灾难性故障；相反，紧急停止必须执行预设的回退控制器，以保持平衡并使机器人进入最低风险状态。这引发了一个关键问题：人形机器人从哪些状态可以安全执行此类停止？

本研究将人形机器人的紧急停止形式化为策略依赖的安全可停止性问题，并采用数据驱动方法刻画安全可停止域。我们提出PRISM（重要性采样可停止性监测器的主动优化框架），该仿真驱动框架通过学习神经预测器实现状态级可停止性判断。PRISM通过重要性采样迭代优化决策边界，实现对罕见但安全关键状态的定向探索。这种定向探索在固定仿真预算下显著提升数据效率，同时减少错误安全预测。我们通过在真实人形机器人平台部署预训练监测器，进一步验证了仿真到现实的迁移能力。结果表明，将安全性建模为策略依赖的可停止性能够实现主动安全监测，并支持人形机器人故障安全行为的可扩展认证。

---

### 14. CaP-X: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation

- **作者**: Max Fu, Justin Yu, Karim El-Refai, Ethan Kou, Haoru Xue, Huang Huang, Wenli Xiao, Guanzhi Wang, Fei-Fei Li, Guanya Shi, Jiajun Wu, Shankar Sastry, Yuke Zhu, Ken Goldberg, Linxi "Jim" Fan ⭐
  - **高亮作者**: Guanya Shi, Yuke Zhu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.22435v1)
- **发表日期**: 2026-03-23
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2603.22435v1](http://arxiv.org/abs/2603.22435v1)
- **📥 PDF**: 已下载至本地 (`2603.22435v1_CaP-X_A_Framework_for_Benchmarking_and_Improving_Coding_Agents_for_Robot_Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: "代码即策略"探讨了可执行代码如何补充数据密集型的视觉-语言-动作方法，但其作为具身操控自主控制器的有效性仍未得到充分探索。我们提出CaP-X——一个用于系统研究机器人操控中代码即策略智能体的开源框架。其核心是CaP-Gym交互环境，智能体通过合成并执行融合感知与控制基元的程序来控制机器人。在此基础上，CaP-Bench从不同抽象层级、交互程度和感知基础三个维度评估前沿语言与视觉-语言模型。通过对12个模型的测试，CaP-Bench揭示出一致趋势：性能随人工设计的抽象层级提升而改善，但当这些先验知识被移除时性能下降，暴露出对设计者框架的依赖。同时我们发现，通过扩展智能体在测试时的计算能力——包括多轮交互、结构化执行反馈、视觉差分、自动技能合成和集成推理——即使智能体仅使用底层基元操作，其鲁棒性也能显著提升。这些发现使我们构建出CaP-Agent0，这个无需训练的框架在仿真环境和真实实体机器人上均能在多项操控任务中达到人类水平的可靠性。我们进一步提出CaP-RL，证明通过可验证奖励的强化学习能提升成功率，并以最小差距实现从仿真到现实的迁移。CaP-X共同构成了推进具身编码智能体发展的原则性开源平台。

---

### 15. DualCoT-VLA: Visual-Linguistic Chain of Thought via Parallel Reasoning for Vision-Language-Action Models

- **作者**: Zhide Zhong, Junfeng Li, Junjie He, Haodong Yan, Xin Gong, Guanyi Zhao, Yingjie Cai, Jiantao Gao, Xu Yan, Bingbing Liu, Yingcong Chen, Liuqing Yang, Haoang Li
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.22280v1)
- **发表日期**: 2026-03-23
- **匹配关键词**: vision-language-action model, VLA, vision-language-action
- **arXiv**: [2603.22280v1](http://arxiv.org/abs/2603.22280v1)
- **📥 PDF**: 已下载至本地 (`2603.22280v1_DualCoT-VLA_Visual-Linguistic_Chain_of_Thought_via_Parallel_Reasoning_for_Vision-Language-Action_Mod.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型能够将视觉观察与语言指令直接映射为机器人动作。虽然这类模型在简单任务中表现良好，但标准的VLA模型在处理需要逻辑规划的复杂多步骤任务以及依赖精细空间感知的精确操作时往往力不从心。近期研究尝试引入思维链（CoT）推理机制，赋予VLA模型“先思考后行动”的能力。然而，当前基于CoT的VLA模型面临两大关键局限：1）由于依赖孤立单模态CoT，无法同时捕捉底层视觉细节与高层逻辑规划；2）逐步自回归解码导致推理延迟高且误差会逐级累积。为突破这些限制，我们提出DualCoT-VLA——一种具备并行推理机制的视觉-语言CoT方法。为实现全面多模态推理，该方法融合了面向底层空间理解的视觉CoT与负责高层任务规划的语言CoT。此外，为克服延迟瓶颈，我们设计了并行CoT机制，通过引入两组可学习的查询标记，将自回归推理转变为单步前向推理。大量实验表明，DualCoT-VLA在LIBERO和RoboCasa GR1基准测试以及实际平台中均取得了最先进的性能表现。

---

### 16. UniDex: A Robot Foundation Suite for Universal Dexterous Hand Control from Egocentric Human Videos

- **作者**: Gu Zhang, Qicheng Xu, Haozhe Zhang, Jianhan Ma, Long He, Yiming Bao, Zeyu Ping, Zhecheng Yuan, Chenhao Lu, Chengbo Yuan, Tianhai Liang, Xiaoyu Tian, Maanping Shao, Feihong Zhang, Mingyu Ding, Yang Gao, Hao Zhao, Hang Zhao, Huazhe Xu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.22264v1)
- **发表日期**: 2026-03-23
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2603.22264v1](http://arxiv.org/abs/2603.22264v1)
- **📥 PDF**: 已下载至本地 (`2603.22264v1_UniDex_A_Robot_Foundation_Suite_for_Universal_Dexterous_Hand_Control_from_Egocentric_Human_Videos.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 灵巧操作因真实机器人遥操作数据采集成本高、手部执行器异构性强以及控制维度复杂而持续面临挑战。本文提出UniDex——一个集大规模机器人中心数据集、统一视觉-语言-动作策略及实用人体数据采集系统于一体的机器人基础套件，旨在实现通用灵巧手控制。首先，我们构建了UniDex-Dataset，这是一个包含八种灵巧手（6-24自由度）超过5万条轨迹的机器人中心数据集，数据源自第一人称人类视频数据集。为将人类数据转化为机器人可执行轨迹，我们采用人机协同重定向流程对齐指尖轨迹并保持合理的手物接触关系，同时通过掩码处理人类手部的显式三维点云数据以缩小运动学与视觉差异。其次，我们提出功能-执行器对齐空间（FAAS），该统一动作空间将功能相似执行器映射至共享坐标，实现跨手型知识迁移。基于FAAS的动作参数化方案，我们训练了UniDex-VLA——一个在UniDex-Dataset上预训练、经任务演示微调的三维视觉-语言-动作策略模型。此外，我们开发了UniDex-Cap便携采集系统，可同步记录RGB-D视频流与人体手部姿态，并将其转化为机器人可执行轨迹，实现人机数据协同训练以降低对高成本机器人演示的依赖。在两种不同手型执行工具使用任务的测试中，UniDex-VLA达成81%的平均任务进度，显著超越现有视觉-语言-动作基线模型，同时展现出强大的空间泛化、物体泛化及零样本跨手型泛化能力。UniDex-Dataset、UniDex-VLA与UniDex-Cap共同构成了可扩展的通用灵巧操作基础套件。

---

### 17. ROBOGATE: Adaptive Failure Discovery for Safe Robot Policy Deployment via Two-Stage Boundary-Focused Sampling

- **作者**: Byungjin Kim
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.22126v1)
- **发表日期**: 2026-03-23
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2603.22126v1](http://arxiv.org/abs/2603.22126v1)
- **📥 PDF**: 已下载至本地 (`2603.22126v1_ROBOGATE_Adaptive_Failure_Discovery_for_Safe_Robot_Policy_Deployment_via_Two-Stage_Boundary-Focused_.pdf`)
- **🔓 开源**: CODE
- **中文摘要**: 在工业环境中部署习得的机器人操作策略需要进行严格的部署前验证，然而在高维参数空间中进行穷尽测试是不可行的。我们提出了ROBOGATE——一个部署风险管理框架，该框架将基于物理的仿真与两阶段自适应采样策略相结合，以高效发现操作参数空间中的失效边界。第一阶段在8维参数空间中使用拉丁超立方采样（LHS），通过20,000个均匀分布的实验建立粗略的失效态势图。第二阶段采用边界聚焦采样，在成功率30-70%的过渡区域集中进行10,000次额外实验，从而实现精确的失效边界映射。利用搭载牛顿物理引擎的NVIDIA Isaac Sim仿真平台，我们在两种机器人实体——Franka Panda（7自由度）和UR5e（6自由度）上对预设的抓放控制器进行了总计30,000次实验评估。我们的逻辑回归风险模型在合并数据集上取得了0.780的AUC值（相较第一阶段单独模型的0.754有所提升），推导出闭式失效边界方程，并揭示了影响两种机器人平台的四个共性危险区域。我们进一步将该框架应用于视觉语言动作（VLA）模型评估：Octo-Small模型在68个对抗场景中成功率为0.0%，而预设基线模型达到100%——这100个百分点的差距凸显了在工业场景中部署基础模型所面临的挑战。ROBOGATE为开源框架，可在单GPU工作站上运行。

---

### 18. FreeArtGS: Articulated Gaussian Splatting Under Free-moving Scenario

- **作者**: Hang Dai, Hongwei Fan, Han Zhang, Duojin Wu, Jiyao Zhang, Hao Dong
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.22102v1)
- **发表日期**: 2026-03-23
- **匹配关键词**: gaussian splatting, articulated object
- **arXiv**: [2603.22102v1](http://arxiv.org/abs/2603.22102v1)
- **📥 PDF**: 已下载至本地 (`2603.22102v1_FreeArtGS_Articulated_Gaussian_Splatting_Under_Free-moving_Scenario.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://freeartgs.github.io/
- **中文摘要**: 随着增强现实和机器人技术需求的日益增长，对高可扩展性关节物体重建的需求也日益迫切。然而，现有基于离散关节状态或随意单目视频的重建方法往往需要进行复杂的轴对齐处理，或存在覆盖范围不足的问题，限制了其实际应用。本文提出FreeArtGS，一种在自由移动场景下重建关节物体的新方法，该场景设置简单且具有高可扩展性。FreeArtGS将自由移动部件分割与关节估计及端到端优化相结合，仅需单目RGB-D视频作为输入。通过利用现有点跟踪和特征模型提供的先验信息进行优化，自由移动部件分割模块能够在无约束拍摄条件下根据相对运动识别刚性部件。关节估计模块则校准统一的对象到相机位姿，并从部件分割结果中稳健地恢复关节类型与轴线。最后，基于3DGS的端到端优化被用于联合重建关节物体的视觉纹理、几何结构及关节角度。我们在两个基准数据集及真实世界自由移动关节物体上进行了实验。结果表明，FreeArtGS在自由移动关节物体重建方面表现优异，同时在传统重建场景中保持高度竞争力，证明了其作为现实资产生成方案的实用性与有效性。项目页面详见：https://freeartgs.github.io/

---

### 19. Do World Action Models Generalize Better than VLAs? A Robustness Study

- **作者**: Zhanguang Zhang, Zhiyuan Li, Behnam Rahmati, Rui Heng Yang, Yintao Ma, Amir Rasouli, Sajjad Pakdamansavoji, Yangzheng Wu, Lingfeng Zhang, Tongtong Cao, Feng Wen, Xingyue Quan, Yingxue Zhang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.22078v1)
- **发表日期**: 2026-03-23
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2603.22078v1](http://arxiv.org/abs/2603.22078v1)
- **📥 PDF**: 已下载至本地 (`2603.22078v1_Do_World_Action_Models_Generalize_Better_than_VLAs?_A_Robustness_Study.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 现实世界中的机器人动作规划具有挑战性，因为它不仅需要理解环境的当前状态，还需预测环境如何随动作演化。视觉-语言-动作模型通过调用动作专家将大规模视觉语言模型重新用于机器人动作生成，已在多种机器人任务中取得显著成功。然而，其性能仍受限于训练数据范围，对未见场景的泛化能力有限，且易受多样化上下文干扰的影响。近期，世界模型作为视觉-语言-动作模型的替代方案重新受到关注。这类基于世界模型构建的动作模型通过海量视频数据训练以预测未来状态，经适度调整后其潜在表征可解码为机器人动作。研究表明，其显式的动态预测能力与从网络规模视频预训练中获得的时空先验相结合，使动作模型比视觉-语言-动作模型具备更有效的泛化能力。本文对当前主流的视觉-语言-动作策略与最新发布的动作模型进行了对比研究，通过在LIBERO-Plus和RoboTwin 2.0-Plus基准测试中评估它们在不同视觉与语言干扰下的表现。实验结果表明，动作模型展现出强大的鲁棒性：LingBot-VA在RoboTwin 2.0-Plus上达到74.2%的成功率，Cosmos-Policy在LIBERO-Plus上取得82.2%的成功率。虽然如$π_{0.5}$等视觉-语言-动作模型在特定任务中能达到相当的鲁棒性，但通常需要依赖多样化机器人数据集和多重学习目标进行大量训练。部分融合视频动态学习的混合方法表现出中等程度的鲁棒性，这凸显了视频先验整合方式的重要性。

---

## 📌 Poster

*其他相关研究*

---

### 1. SIMART: Decomposing Monolithic Meshes into Sim-ready Articulated Assets via MLLM

- **作者**: Chuanrui Zhang, Minghan Qin, Yuang Wang, Baifeng Xie, Hang Li, Ziwei Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.23386v1)
- **发表日期**: 2026-03-24
- **匹配关键词**: articulated object
- **arXiv**: [2603.23386v1](http://arxiv.org/abs/2603.23386v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 高质量可动三维资产对于具身人工智能与物理模拟至关重要，然而当前三维生成技术仍主要聚焦于静态网格模型，导致"模拟就绪"的交互式对象存在明显缺口。现有的大多数可动物体创建方法依赖于多阶段流程，各解耦模块间的误差会逐级累积。相比之下，统一的多模态大语言模型为静态资产理解与模拟就绪资产生成提供了单阶段解决方案。但基于密集体素的三维标记化方法会产生冗长的三维标记序列和高昂的内存开销，限制了处理复杂可动物体的扩展能力。为此，我们提出SIMART框架——一个能够同步执行部件级分解与运动学预测的统一多模态大语言模型。通过引入稀疏三维VQ-VAE编码器，SIMART将标记数量较密集体素标记减少70%，实现了高保真度的多部件装配。该框架在PartNet-Mobility数据集和开放域AIGC数据集上均达到最先进性能，并成功支持基于物理的机器人仿真应用。

---

