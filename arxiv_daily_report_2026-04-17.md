# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-04-17 08:04

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 1/20 篇提供

**🌟 Highlight**: 9 篇 | **📌 Poster**: 11 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. HiVLA: A Visual-Grounded-Centric Hierarchical Embodied Manipulation System

- **作者**: Tianshuo Yang, Guanyu Chen, Yutian Chen, Zhixuan Liang, Yitian Liu, Zanxin Chen, Chunpu Xu, Haotian Liang, Jiangmiao Pang, Yao Mu, Ping Luo
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.14125v1)
- **发表日期**: 2026-04-15
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2604.14125v1](http://arxiv.org/abs/2604.14125v1)
- **📥 PDF**: 已下载至本地 (`2604.14125v1_HiVLA_A_Visual-Grounded-Centric_Hierarchical_Embodied_Manipulation_System.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 虽然端到端视觉-语言-动作模型为机器人操作提供了前景广阔的研究范式，但基于狭窄控制数据的微调往往会削弱其从基础视觉-语言模型继承的深层推理能力。为解决这一根本性权衡问题，我们提出HiVLA——一个以视觉定位为核心的分层框架，明确将高层语义规划与底层运动控制进行解耦。在高层模块中，视觉-语言规划器首先执行任务分解与视觉定位，生成包含子任务指令和精确目标边界框的结构化方案。随后，为将规划转化为物理动作，我们在底层模块引入配备新型级联交叉注意力机制的流匹配扩散变换器动作专家。该设计通过序列化融合全局上下文、高分辨率目标中心裁剪特征及技能语义，使扩散变换器能够专注于鲁棒的动作执行。这种解耦架构既保留了视觉-语言模型的零样本推理能力，又支持两个组件的独立优化。大量仿真与真实环境实验表明，HiVLA在长周期技能组合及杂乱场景中小物体的精细操作方面表现卓越，显著优于当前最先进的端到端基线模型。

---

### 2. Jump-Start Reinforcement Learning with Vision-Language-Action Regularization

- **作者**: Angelo Moroncelli, Roberto Zanetti, Marco Maccarini, Loris Roveda
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.13733v1)
- **发表日期**: 2026-04-15
- **匹配关键词**: exploration, VLA, vision-language-action
- **arXiv**: [2604.13733v1](http://arxiv.org/abs/2604.13733v1)
- **📥 PDF**: 已下载至本地 (`2604.13733v1_Jump-Start_Reinforcement_Learning_with_Vision-Language-Action_Regularization.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 强化学习（RL）能够为机器人操作提供高频闭环控制，但由于探索效率低下和信用分配不佳，将其扩展到具有稀疏或不完美奖励的长时程任务仍然困难。视觉-语言-动作（VLA）模型利用大规模多模态预训练提供通用任务级推理，但现有局限性阻碍了其在快速精确操作中的直接应用。本文提出视觉-语言-动作跳跃启动（VLAJS）方法，通过连接稀疏的VLA引导与在线策略强化学习来提升探索和学习效率。VLAJS将VLA模型视为高层动作建议的临时来源，用于引导早期探索并改善信用分配，同时保留强化学习基于状态的高频控制特性。该方法通过方向性动作一致性正则化增强近端策略优化（PPO），在训练初期将智能体动作与VLA引导进行柔性对齐，无需强制严格模仿、依赖演示数据或持续查询教师策略。VLA引导以稀疏方式应用并随时间衰减，使智能体能够在线适应并最终超越引导策略。我们在六项具有挑战性的操作任务上评估VLAJS：模拟环境中的抓举、抓放、钉孔重定向、钉孔插入、戳动和推动任务，并在真实Franka Panda机器人上验证了部分任务。VLAJS在样本效率上持续优于PPO和蒸馏式基线方法，在多项任务中减少超过50%的环境交互需求。真实世界实验证明了零样本仿真到现实的迁移能力，以及在杂乱环境、物体变化和外部干扰下的鲁棒执行性能。

---

### 3. Vision-and-Language Navigation for UAVs: Progress, Challenges, and a Research Roadmap

- **作者**: Hanxuan Chen, Jie Zheng, Siqi Yang, Tianle Zeng, Siwei Feng, Songsheng Cheng, Ruilong Ren, Hanzhong Guo, Shuai Yuan, Xiangyue Wang, Kangli Wang, Ji Pei
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.13654v1)
- **发表日期**: 2026-04-15
- **匹配关键词**: VLN, vision-language-action, vision-and-language navigation, VLA, navigation, collaborative robot
- **arXiv**: [2604.13654v1](http://arxiv.org/abs/2604.13654v1)
- **📥 PDF**: 已下载至本地 (`2604.13654v1_Vision-and-Language_Navigation_for_UAVs_Progress,_Challenges,_and_a_Research_Roadmap.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 无人机视觉语言导航是具身人工智能领域的一项关键挑战，其核心在于使无人机能够理解高级人类指令，并在复杂三维环境中执行长时程任务。本文对该领域进行了系统性的全面综述，涵盖从任务形式化定义到当前前沿进展的全貌。我们构建了方法论分类体系，梳理了从早期模块化与深度学习方案，到当前由大规模基础模型驱动的智能体系统的技术演进脉络，包括视觉语言模型、视觉语言动作模型，以及新兴的生成式世界模型与视觉语言动作架构融合的物理推理范式。本综述系统梳理了支撑标准化研究的关键资源生态系统——仿真平台、数据集与评估指标。进一步地，我们对阻碍实际部署的核心挑战展开批判性分析：仿真与现实间的差异、动态户外环境下的鲁棒感知、语言歧义推理，以及大模型在资源受限硬件上的高效部署。通过综合现有基准测试与局限性分析，本文最后提出前瞻性研究路线图，以指引未来在无人机集群协同、空地协作机器人等关键前沿方向的探索。

---

### 4. RobotPan: A 360$^\circ$ Surround-View Robotic Vision System for Embodied Perception

- **作者**: Jiahao Ma, Qiang Zhang, Peiran Liu, Zeran Su, Pihai Sun, Gang Han, Wen Zhao, Wei Cui, Zhang Zhang, Zhiyuan Xu, Renjing Xu, Jian Tang, Miaomiao Liu, Yijie Guo
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.13476v1)
- **发表日期**: 2026-04-15
- **匹配关键词**: navigation, 3D reconstruction, 3d reconstruction
- **arXiv**: [2604.13476v1](http://arxiv.org/abs/2604.13476v1)
- **📥 PDF**: 已下载至本地 (`2604.13476v1_RobotPan_A_360$^circ$_Surround-View_Robotic_Vision_System_for_Embodied_Perception.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://robotpan.github.io/
- **中文摘要**: 全景感知在机器人导航与移动操作中日益重要，尤其在遥操作、数据采集和紧急接管等人机协同场景中。然而，当前机器人视觉界面通常局限于狭窄的前向视野；即使配备多路车载摄像头，也需依赖繁琐的手动切换操作，这会打断操作者的工作流程。现有方案均存在运动抖动问题，易导致头戴式显示器用户产生晕眩感。本文提出一种全景机器人视觉系统，通过融合六路摄像头与激光雷达实现360°全覆盖视觉感知，同时满足实体部署的几何约束与实时性要求。我们进一步提出\textsc{RobotPan}前馈框架，该框架可从标定的稀疏视角输入中预测具有度量尺度且紧凑的三维高斯表征，实现实时渲染、重建与流式传输。\textsc{RobotPan}将多视角特征提升至统一球坐标系，并利用分层球形体素先验解码高斯表征，在机器人近场采用精细分辨率、远场采用粗粒度分辨率，在不损失保真度的前提下减少计算冗余。针对长时序任务，我们的在线融合机制能动态更新场景内容，同时通过选择性外观更新抑制静态区域的无限增长。此外，我们发布了专为机器人360°新视角合成与度量三维重建定制的多传感器数据集，涵盖真实平台上的导航、操作与移动任务。实验表明，\textsc{RobotPan}在保持与现有前馈重建及视角合成方法相当质量的同时，生成的高斯表征数量显著减少，实现了实用的实时实体部署。项目网站：https://robotpan.github.io/

---

### 5. Vectorizing Projection in Manifold-Constrained Motion Planning for Real-Time Whole-Body Control

- **作者**: Shrutheesh R Iyer, I-Chia Chang, Andrew Z. Liu, Yan Gu, Zachary Kingston
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.13323v1)
- **发表日期**: 2026-04-14
- **匹配关键词**: motion planning
- **arXiv**: [2604.13323v1](http://arxiv.org/abs/2604.13323v1)
- **📥 PDF**: 已下载至本地 (`2604.13323v1_Vectorizing_Projection_in_Manifold-Constrained_Motion_Planning_for_Real-Time_Whole-Body_Control.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 许多机器人规划任务要求在整个轨迹中满足一个或多个约束条件。针对几何约束问题，流形约束运动规划算法能够在任务指定的约束子流形上规划起始与目标构型之间的无碰撞路径。当前最先进的方法在应对人形机器人等复杂系统时，可能需要数十秒才能完成求解，这使得实际应用（尤其在动态环境中）难以实现。受硬件加速运动规划最新进展的启发，我们提出一种CPU SIMD加速的流形约束运动规划器，通过并行化视角重新审视基于投影的约束满足方法。通过将相关组件转化为可并行化结构，我们利用SIMD并行技术规划满足约束的解决方案。该方法相比现有技术实现了高达100-1000倍的加速，首次使实时约束运动规划成为可能。我们在真实人形机器人上验证了该规划器，展示了实时全身准静态规划生成能力。本研究成果发布于https://commalab.org/papers/mcvamp/。

---

### 6. Tree Learning: A Multi-Skill Continual Learning Framework for Humanoid Robots

- **作者**: Yifei Yan, Linqi Ye
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.12909v1)
- **发表日期**: 2026-04-14
- **匹配关键词**: navigation, autonomous navigation
- **arXiv**: [2604.12909v1](http://arxiv.org/abs/2604.12909v1)
- **📥 PDF**: 已下载至本地 (`2604.12909v1_Tree_Learning_A_Multi-Skill_Continual_Learning_Framework_for_Humanoid_Robots.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 随着人形机器人强化学习从单任务向多技能范式演进，如何在高效拓展新技能的同时避免灾难性遗忘，已成为具身智能领域的关键挑战。现有方法或依赖混合专家模型中复杂的拓扑结构调整，或需训练超大规模模型，难以实现轻量化部署。为此，我们提出面向人形机器人的多技能持续学习框架——树状学习。该框架采用根-枝分层参数继承机制，通过参数复用为分支技能提供运动先验，从根本上防止灾难性遗忘；设计融合相位调制与插值的多模态前馈适应机制，同时支持周期性与非周期性运动；提出任务级奖励塑形策略以加速技能收敛。基于Unity的仿真实验表明：相较于同步多任务训练，树状学习在多种代表性运动技能中均获得更高奖励，同时保持100%技能留存率，可实现多技能无缝切换与实时交互控制。我们进一步通过两个差异化Unity仿真任务验证了树状学习的性能与泛化能力：受超级马里奥启发的交互场景，以及经典中式园林环境中的自主导航。

---

### 7. Robotic Manipulation is Vision-to-Geometry Mapping ($f(v) \rightarrow G$): Vision-Geometry Backbones over Language and Video Models

- **作者**: Zijian Song, Qichang Li, Jiawei Zhou, Zhenlong Yuan, Tianshui Chen, Liang Lin, Guangrun Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.12908v1)
- **发表日期**: 2026-04-14
- **匹配关键词**: VLA
- **arXiv**: [2604.12908v1](http://arxiv.org/abs/2604.12908v1)
- **📥 PDF**: 已下载至本地 (`2604.12908v1_Robotic_Manipulation_is_Vision-to-Geometry_Mapping_($f(v)_rightarrow_G$)_Vision-Geometry_Backbones_o.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 机器人操作的核心本质是视觉到几何的映射问题（$f(v) \rightarrow G$）。物理动作从根本上由三维位置与空间关系等几何属性定义。因此我们认为，通用化机器人控制的基础应当是视觉-几何主干网络，而非当前广泛采用的视觉-语言或视频模型。传统视觉语言模型与视频预测模型依赖于在大规模二维图文或时序像素数据上预训练的主干网络，虽然有效，但其表征主要受语义概念或二维先验信息塑造，与物理操作所需的精确三维几何特性存在本质错位。基于这一洞见，我们提出视觉-几何-动作模型，该模型直接在预训练的原生三维表征上构建动作生成机制。具体而言，VGA以预训练的三维世界模型替代传统语言或视频主干网络，建立无缝的视觉到几何映射，将视觉输入直接转化为物理动作。为增强几何一致性，我们引入渐进式体素调制模块并采用联合训练策略。大量实验验证了本方法的有效性：在仿真基准测试中，VGA在包括$π_{0.5}$与GeoVLA在内的顶尖视觉语言模型基线上表现优异，展现出精准操作优势；更重要的是，在现实场景部署中，VGA对未见视角展现出卓越的零样本泛化能力，持续超越$π_{0.5}$。这些结果表明，基于原生三维表征而非通过语言或二维视频先验进行转换，是实现通用化物理智能极具前景的研究方向。

---

### 8. DeCoNav: Dialog enhanced Long-Horizon Collaborative Vision-Language Navigation

- **作者**: Sunyao Zhou, Yunzi Wu, Tianhang Wang, Xinhai Li, Guang Chen, Lizheng Liu, Chenjia Bai, Xuelong Li
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.12486v1)
- **发表日期**: 2026-04-14
- **匹配关键词**: navigation, VLN
- **arXiv**: [2604.12486v1](http://arxiv.org/abs/2604.12486v1)
- **📥 PDF**: 已下载至本地 (`2604.12486v1_DeCoNav_Dialog_enhanced_Long-Horizon_Collaborative_Vision-Language_Navigation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 长时程协作视觉语言导航（VLN）对于多机器人系统完成超越单个智能体能力的复杂任务至关重要。CoNavBench迈出了第一步，通过引入首个包含接力式多机器人任务的协作长时程VLN基准测试集、协作分类法，以及基于图的生成与评估方法，以建模共享环境中的任务交接与汇合。然而，现有基准测试和评估通常未在共享世界时间线上强制执行严格同步的双机器人推演，且多依赖静态协调策略，无法在新跨智能体证据出现时进行自适应调整。我们提出对话增强的长时程协作视觉语言导航（DeCoNav），这是一个去中心化框架，将事件触发式对话与动态任务分配及重规划相结合，实现实时自适应协调。在DeCoNav中，机器人通过对话交换紧凑语义状态而无需中央控制器。当出现新证据、不确定性或冲突等关键事件时，系统触发对话机制，在同步执行条件下动态重新分配子目标并重规划路径。通过在DeCoNavBench中实现（涵盖176个HM3D场景的1,213项任务），DeCoNav将双机成功率（BSR）提升了69.2%，证明了对话驱动、动态重分配规划对多机器人协作的有效性。

---

### 9. HazardArena: Evaluating Semantic Safety in Vision-Language-Action Models

- **作者**: Zixing Chen, Yifeng Gao, Li Wang, Yunhan Zhao, Yi Liu, Jiayu Li, Xiang Zheng, Zuxuan Wu, Cong Wang, Xingjun Ma, Yu-Gang Jiang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.12447v1)
- **发表日期**: 2026-04-14
- **匹配关键词**: vision-language-action model, VLA, vision-language-action
- **arXiv**: [2604.12447v1](http://arxiv.org/abs/2604.12447v1)
- **📥 PDF**: 已下载至本地 (`2604.12447v1_HazardArena_Evaluating_Semantic_Safety_in_Vision-Language-Action_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-行动（VLA）模型继承了视觉-语言主干网络丰富的世界知识，并通过动作演示获得可执行技能。然而，现有评估主要关注动作执行成功率，导致动作策略与视觉-语言语义的耦合较为松散。这种脱钩暴露了系统性漏洞：在语义风险下，正确的动作执行可能引发不安全后果。为揭示这一漏洞，我们提出HazardArena基准测试，旨在受控但具有风险的情境中评估VLA模型的语义安全性。该基准通过构建安全/不安全孪生场景实现，这些场景共享相同的物体、布局和动作要求，仅通过决定动作是否不安全的语义情境进行区分。研究发现，仅在安全场景训练的VLA模型在对应不安全场景中常无法保持安全行为。HazardArena包含2000余个资产和40个风险敏感任务，涵盖基于成熟机器人安全标准的7个现实风险类别。为缓解此漏洞，我们提出无需训练的"安全选项层"，通过语义属性或视觉-语言判断器约束动作执行，在基本不影响任务性能的前提下显著减少不安全行为。我们希望HazardArena能促使学界重新思考VLA模型在迈向现实部署时，应如何评估和保障语义安全性。

---

## 📌 Poster

*其他相关研究*

---

### 1. Self-adaptive Multi-Access Edge Architectures: A Robotics Case

- **作者**: Mahyar T Moghaddam, Joakim Leed, Anders Frandsen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.13542v1)
- **发表日期**: 2026-04-15
- **匹配关键词**: path planning
- **arXiv**: [2604.13542v1](http://arxiv.org/abs/2604.13542v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 随着计算密集型人工智能任务的增长，降低处理成本、提升性能与能效的需求日益凸显。这要求引入智能体作为架构自适应监管器，负责基础设施的动态扩展及计算任务在连续体中的高效卸载。本文提出一种面向人机混合环境高效计算系统的自适应方法。该计算任务采用神经网络算法，通过分析传感数据预测人类移动行为，以优化移动机器人的主动路径规划并保障人员安全。为简化神经网络处理流程，我们构建了基于Kubernetes编排的异构处理单元分布式边缘卸载系统。通过监测响应时间与能耗，基于MAPE-K框架的自适应监管器能够智能决策扩展与卸载策略。实验结果表明，相较于传统架构，该系统在服务质量上取得显著提升，验证了所提方法在人工智能驱动系统中的有效性。

---

### 2. Utilizing Inpainting for Keypoint Detection for Vision-Based Control of Robotic Manipulators

- **作者**: Sreejani Chatterjee, Venkatesh Mullur, Abhinav Gandhi, Berk Calli
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.13309v1)
- **发表日期**: 2026-04-14
- **匹配关键词**: visual servoing
- **arXiv**: [2604.13309v1](http://arxiv.org/abs/2604.13309v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 本文提出了一种新颖的视觉伺服框架，通过使用纯自然视觉特征在构型空间内控制机器人机械臂。我们的目标是开发能够稳健检测和跟踪机器人机械臂上自然特征或关键点的方法，这些特征将用于基于视觉的控制，特别是在运行时无法或不适合在机器人上放置外部标记的场景中。针对我们数据驱动方法的模型训练过程，我们创建了一个数据收集流程：在机器人本体上附着ArUco标记，将其中心标注为关键点，然后利用修复方法移除标记并重建被遮挡区域。通过这种方式，我们生成了带有标记位置自动标注的自然（无标记）机器人图像。这些图像用于训练关键点检测算法，进而通过机器人的自然特征控制其构型。与先前依赖精确相机标定和机器人模型来标注训练图像的方法不同，我们的方法通过修复技术消除了这些依赖。为了在存在遮挡时仍能实现稳健的关键点检测，我们引入了第二个修复模型，在运行时实时重建机器人被遮挡区域，从而实现连续的关键点检测。为进一步提升关键点预测的一致性和鲁棒性，我们集成了无迹卡尔曼滤波器（UKF），通过随时间优化关键点估计来增强控制性能的稳定性和可靠性。采用这种无模型、纯视觉的控制策略，我们在完全可见和部分遮挡条件下，利用运行时的机器人自然特征均取得了成功的控制效果。

---

### 3. Capability-Aware Heterogeneous Control Barrier Functions for Decentralized Multi-Robot Safe Navigation

- **作者**: Joonkyung Kim, Yanze Zhang, Wenhao Luo, Yiwei Lyu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.13245v1)
- **发表日期**: 2026-04-14
- **匹配关键词**: navigation
- **arXiv**: [2604.13245v1](http://arxiv.org/abs/2604.13245v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 多机器人系统的安全导航要求在分散决策下确保安全的同时不牺牲任务效率。现有分散式方法通常假设机器人同质性，导致具有结构差异动态特性的异构智能体对共享安全要求产生不一致解读，这可能使某些机器人无法实际履行避障义务，从而引发安全违规或死锁。本文提出能力感知异构控制屏障函数（CA-HCBF）——一种用于异构机器人团队实现一致性安全约束与能力感知协调的分散式框架。我们通过规范变换与反步法推导出规范二阶控制仿射表示，将完整约束与非完整约束机器人统一在加速度控制层面，在保持安全集前向不变性的同时避免异构动态系统间的相对阶失配。进一步引入基于支撑函数的方向性能力度量，量化各机器人执行运动意图的能力，推导出按运动能力比例分配安全责任的成对责任分配机制。可行性感知裁剪机制进一步将分配约束在各智能体物理可实现范围内，缓解密集分散式CBF场景中常见的不可行约束分配问题。通过多达30个异构机器人的仿真实验及物理多机器人演示验证，本方法在安全性与任务效率上均优于基线方法，证实了其在具有不同运动学约束机器人间的实际适用性。

---

### 4. Weakly-supervised Learning for Physics-informed Neural Motion Planning via Sparse Roadmap

- **作者**: Ruiqi Ni, Yuchen Liu, Ahmed H. Qureshi
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.13204v1)
- **发表日期**: 2026-04-14
- **匹配关键词**: motion planning
- **arXiv**: [2604.13204v1](http://arxiv.org/abs/2604.13204v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 运动规划问题需要在复杂高维空间中寻找起点与目标配置之间的无碰撞路径。近期基于学习的方法提供了有前景的解决方案，其中自监督物理信息方法（如神经时间场NTFields）通过求解Eikonal方程来学习价值函数，无需专家示范。然而，现有物理信息方法在复杂多房间环境中难以扩展，仅增加采样数量无法解决局部极小值问题或保证全局一致性。我们提出分层神经时间场（H-NTFields），这是一个弱监督框架，将稀疏路线图的弱监督与物理信息偏微分方程正则化相结合。路线图通过行程时间的上下界提供全局拓扑锚点，而偏微分方程损失则强制保持局部几何保真度和障碍物感知传播。在18个Gibson环境和真实机器人平台上的实验表明，H-NTFields显著提升了先前物理信息方法的鲁棒性，同时通过连续价值表示实现了快速摊销推理。

---

### 5. FastGrasp: Learning-based Whole-body Control method for Fast Dexterous Grasping with Mobile Manipulators

- **作者**: Heng Tao, Yiming Zhong, Zemin Yang, Yuexin Ma
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.12879v1)
- **发表日期**: 2026-04-14
- **匹配关键词**: mobile manipulator, dexterous grasping
- **arXiv**: [2604.12879v1](http://arxiv.org/abs/2604.12879v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 快速抓取对于物流、制造和服务应用中的移动机器人至关重要。现有方法受限于固定基座、简单夹具或缓慢的触觉响应能力，在高速运动下的冲击稳定、实时全身协调以及跨多样物体与场景的泛化方面面临根本性挑战。我们提出\textbf{FastGrasp}，一种基于学习的框架，集成了抓取引导、全身控制和触觉反馈，用于移动快速抓取。我们的两阶段强化学习策略首先通过以物体点云为条件的条件变分自编码器生成多样化的抓取候选方案，随后在最优抓取选择的指导下执行移动基座、机械臂和手部的协调运动。触觉感知支持实时抓取调整，以应对冲击效应和物体变化。大量实验证明，该框架在仿真和现实场景中均展现出卓越的抓取性能，通过有效的仿真到现实迁移，实现了跨不同物体几何形状的鲁棒操作。

---

### 6. Evolving the Complete Muscle: Efficient Morphology-Control Co-design for Musculoskeletal Locomotion

- **作者**: Lidong Sun, Wentao Zhao, Ye Wang, Huaping Liu, Fuchun Sun
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.12855v1)
- **发表日期**: 2026-04-14
- **匹配关键词**: exploration
- **arXiv**: [2604.12855v1](http://arxiv.org/abs/2604.12855v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 肌肉骨骼机器人凭借其固有的柔顺性与灵活性，为多场景运动提供了极具前景的范式。然而现有研究通常依赖固定肌肉生理参数的模型，这种静态物理设定难以适应复杂任务中多样化的动态需求，本质上限制了机器人的性能上限。本研究聚焦于肌肉骨骼系统的形态与控制协同设计，区别于以往仅优化刚度等单一生理属性的研究，我们提出了一个同时演化肌肉力量、速度与刚度的完整肌肉骨骼形态进化空间。为应对全面进化带来的探索空间指数级扩张，我们提出了谱系设计进化框架——一种高效的协同优化方法。该框架通过将双侧对称先验与主成分分析相结合，将复杂的肌肉参数映射至低维谱流形，从而实现高效的形态探索。在MyoSuite框架下对行走、爬梯、丘陵及崎岖地形四项任务进行评估，本方法相较于固定形态与标准进化基线，展现出更优的学习效率与运动稳定性。

---

### 7. Reliability-Guided Depth Fusion for Glare-Resilient Navigation Costmaps

- **作者**: Shang-En Tsai, Wei-Cheng Sun
- **单位**: Department of Computer Science and Information Engineering, Chang Jung Christian University; Department of Computer Science and Information Engineering, Chang Jung Christian University
- **发表日期**: 2026-04-14
- **匹配关键词**: navigation
- **arXiv**: [2604.12753v1](http://arxiv.org/abs/2604.12753v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 镜面反射在地板与玻璃表面产生的眩光常会干扰RGB-D深度测量，导致深度图中出现孔洞与尖峰，这些误差在占据栅格代价地图中累积形成持续的幻影障碍物。本文提出一种基于显式深度可靠性建模的抗眩光代价地图构建方法。通过轻量级深度可靠性地图估计器预测镜面干扰下各像素点的测量可信度，并采用可靠性引导融合机制，在受损测量值累积入地图前，利用该信号调节占据状态更新。在配备英特尔实感D435相机和Jetson Orin Nano平台的真实移动机器人上进行实验，结果表明：该方法在真实反光地板与玻璃表面场景中显著减少了错误障碍物插入，提升了自由空间保持能力，且仅引入适度计算开销。这些发现表明，将眩光视为测量可靠性问题，能为安全关键室内环境中提升代价地图准确性与导航鲁棒性提供实用且轻量化的解决方案。

---

### 8. A hierarchical spatial-aware algorithm with efficient reinforcement learning for human-robot task planning and allocation in production

- **作者**: Jintao Xue, Xiao Li, Nianmin Zhang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.12669v1)
- **发表日期**: 2026-04-14
- **匹配关键词**: path planning
- **arXiv**: [2604.12669v1](http://arxiv.org/abs/2604.12669v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 在先进制造系统中，人与机器人协同完成生产流程。有效的任务规划与分配对实现高效生产至关重要，但在复杂动态的制造环境中仍面临挑战。人与机器人的动态特性，特别是需要考虑空间信息（如人员的实时位置及完成任务需移动的距离），使得任务规划与分配问题显著复杂化。为解决上述难题，我们将生产任务分解为可管理的子任务，并实现了一种实时分层人机任务规划与分配算法，该算法包含负责任务规划的高层智能体与负责任务分配的低层智能体。针对高层智能体，我们提出了一种高效的基于缓冲区的深度Q学习方法，该方法能减少训练时间，并在具有长期稀疏奖励特性的生产问题中提升性能。对于低层智能体，我们设计了基于路径规划的空间感知方法，将任务分配给合适的人机资源，从而实现相应的顺序子任务。我们在三维模拟器中针对复杂实时生产过程进行了实验验证，结果表明所提出的EBQ&SAP方法能有效解决复杂动态生产过程中的人机任务规划与分配问题。

---

### 9. Scalable Trajectory Generation for Whole-Body Mobile Manipulation

- **作者**: Yida Niu, Xinhai Chang, Xin Liu, Ziyuan Jiao, Yixin Zhu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.12565v1)
- **发表日期**: 2026-04-14
- **匹配关键词**: articulated object, mobile manipulation
- **arXiv**: [2604.12565v1](http://arxiv.org/abs/2604.12565v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 部署在非结构化环境中的机器人必须协调全身运动——同时移动移动基座和机械臂——以与物理世界互动。这种移动性与灵巧性的结合产生了一个随场景和物体多样性呈组合增长的状态空间，所需的数据集远大于固定基座操作所需的数据集。然而，现有的采集方法（包括遥操作和规划）要么劳动密集，要么在规模上计算成本过高。核心瓶颈在于缺乏一个可扩展的流程，用于在不同实体和环境之间生成大规模、物理有效、协调的轨迹数据。本文介绍AutoMoMa，这是一个GPU加速框架，它将AKR建模（将基座、机械臂和物体运动学整合为单一链条）与并行化轨迹优化相结合。AutoMoMa实现了每GPU小时5,000个训练片段（比基于CPU的基线快80倍以上），生成了超过50万个物理有效轨迹的数据集，涵盖330个场景、多样化的关节物体和多种机器人实体。以往的数据集不得不在规模、多样性或运动学保真度上做出妥协；AutoMoMa同时解决了这三个问题。训练下游模仿学习策略进一步表明，即使是单个关节物体任务，也需要数万次演示才能使最先进的方法达到约80%的成功率，这证实了数据稀缺（而非算法限制）一直是制约因素。因此，AutoMoMa连接了高性能规划和基于模仿学习的可靠控制，为协调移动操作研究提供了此前缺失的基础设施。通过使大规模、运动学有效的训练数据变得实用，AutoMoMa展示了能够在真实世界多样化、非结构化环境中运行的通用全身机器人策略。

---

### 10. Whole-Body Mobile Manipulation using Offline Reinforcement Learning on Sub-optimal Controllers

- **作者**: Snehal Jauhri, Vignesh Prasad, Georgia Chalvatzaki
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.12509v1)
- **发表日期**: 2026-04-14
- **匹配关键词**: mobile manipulator, articulated object, mobile manipulation
- **arXiv**: [2604.12509v1](http://arxiv.org/abs/2604.12509v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 移动操作（MoMa）关节物体，如开门、抽屉和橱柜，需要机器人底座与手臂之间进行同步的全身协调。传统的全身控制器（WBCs）可以通过分层优化解决此类问题，但需要大量手动调整优化且仍显脆弱。相比之下，基于学习的方法展现出强大的泛化能力，但通常依赖于昂贵的全身遥操作数据或复杂的奖励工程。我们观察到，即使是一个次优的WBC也是一个强大的结构先验：它可以用于在状态-动作空间的任务相关约束区域内收集数据，并且其行为仍可通过离线强化学习进行改进。基于此，我们提出了WHOLE-MoMa，这是一个两阶段流程：首先通过随机化轻量级WBC生成多样化演示，然后应用离线强化学习通过奖励信号识别并整合改进的行为。为了支持复杂协调任务所需的表达性动作分块扩散策略，我们扩展了离线隐式Q学习，引入Q分块技术以实现分块级批评器评估和优势加权策略提取。在使用模拟环境中的TIAGo++移动操作器进行的三个难度递增的任务中，WHOLE-MoMa显著优于WBC、行为克隆及多种离线强化学习基线方法。策略无需微调即可直接迁移到真实机器人上，在双手抽屉操作中达到80%成功率，在同步橱柜开启与物体放置任务中达到68%成功率，且全程未使用任何遥操作或真实世界训练数据。

---

### 11. Designing for Error Recovery in Human-Robot Interaction

- **作者**: Christopher D. Wallbridge, Erwin Jose Lopez Pulgarin
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.12473v1)
- **发表日期**: 2026-04-14
- **匹配关键词**: human-robot interaction
- **arXiv**: [2604.12473v1](http://arxiv.org/abs/2604.12473v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 本立场文件简要探讨了我们尝试为机器人人工智能系统编程的方式。许多人工智能系统基于这样一种理念：试图将单一系统的性能提升至超越所谓的人类基准线。然而，这些系统通常关注一次性、单向的决策，而现实世界则更为连续和互动。相比之下，人类往往能够从错误中恢复并学习，从而实现更高的成功率。我们以机器人核手套箱为例，探讨构建能够检测并自我恢复错误的系统所面临的挑战，以此帮助阐明相关实例。随后，我们将进一步讨论简单的初始设计方案。

---

