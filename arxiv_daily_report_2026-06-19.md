# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-06-19 08:04

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 3/20 篇提供

**🌟 Highlight**: 17 篇 | **📌 Poster**: 3 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. Does VLA Even Know the Basics? Measuring Commonsense and World Knowledge Retention in Vision-Language-Action Models

- **作者**: Nikita Kachaev, Andrey Moskalenko, Matvey Skripkin, Nikita Kurlaev, Daria Pugacheva, Albina Burlova, Mikhail Kolosov, Denis Shepelev, Andrey Kuznetsov, Elena Tutubalina, Aleksandr I. Panov, Alexey K. Kovalev, Vlad Shakhuro
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.19297v1)
- **发表日期**: 2026-06-17
- **匹配关键词**: VLA, vision-language-action model, vision-language-action
- **arXiv**: [2606.19297v1](http://arxiv.org/abs/2606.19297v1)
- **📥 PDF**: 已下载至本地 (`2606.19297v1_Does_VLA_Even_Know_the_Basics?_Measuring_Commonsense_and_World_Knowledge_Retention_in_Vision-Languag.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 具身视觉-语言-动作（VLA）模型通常通过在机器人数据上微调强大的预训练VLM获得，但尚不清楚它们在适应后保留了多少常识和事实知识。在知识敏感型任务上的失败具有模糊性，难以区分是知识缺失还是底层控制泛化能力不足。我们提出Act2Answer，一种轻量级评估协议，通过要求智能体以动作作答，将VLM知识基准适配至VLA评估。每个问题被转化为一个简短的桌面操作场景，智能体通过执行单个物体放置动作从候选答案中选择，从而得到基于动作的成功率，并减少控制干扰。我们构建了涵盖多种常识与世界知识类别的测试环境套件，并引入逐层意图探测方法，以定位VLM主干网络和动作头中与答案相关的信息。在对7个VLA模型和9个VLM基线的大规模研究中，我们系统性地按类别对模型进行排名，发现：VLA在简单概念上表现稳健，但在语义更丰富的类别上相较于源VLM存在更大差距；VQA联合训练与更好的知识保留相关；与答案相关的信号在VLA中间层达到峰值，但在高层衰减。Act2Answer代码已开源：https://tttonyalpha.github.io/act2answer/。

---

### 2. Mobile Pedipulation for Object Sliding via Hierarchical Control on a Wheeled Bipedal Robot

- **作者**: Yue Qin, Yulun Zhuang, Zelin Shen, Yanran Ding
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.19233v1)
- **发表日期**: 2026-06-17
- **匹配关键词**: object manipulation
- **arXiv**: [2606.19233v1](http://arxiv.org/abs/2606.19233v1)
- **📥 PDF**: 已下载至本地 (`2606.19233v1_Mobile_Pedipulation_for_Object_Sliding_via_Hierarchical_Control_on_a_Wheeled_Bipedal_Robot.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 本文提出了一种分层控制框架，使轮式双足机器人能够利用其轮式腿部完成平面物体滑动任务。该方法基于降阶三刚体动力学模型构建了非线性模型预测控制器，该模型显式考虑了髋关节滚动自由度及多种轮地接触模式，这对侧向步态和腿部操作任务至关重要。在该框架中，非线性模型预测控制器同步调节机器人运动与交互力，使机器人能够稳定执行滚动与物体操作行为。我们开发了基于轨迹优化的机器人-物体运动规划器，用于生成包含地面-物体接触中粘滑转换的参考运动。通过实际硬件实验验证了两种代表性腿部操作动作——滑移与侧向滑动，实验中机器人成功从桌底取回1千克物体，并通过滑移动作将4千克物体移动了0.228米。

---

### 3. Invertible Neural Network Adapter for One-Step Flow Matching in Robot Manipulation

- **作者**: Yu Zhang, Kangyi Ji, Yongxiang Zou, Rongtao Xu, Feng Zheng, Long Cheng
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.19194v1)
- **发表日期**: 2026-06-17
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2606.19194v1](http://arxiv.org/abs/2606.19194v1)
- **📥 PDF**: 已下载至本地 (`2606.19194v1_Invertible_Neural_Network_Adapter_for_One-Step_Flow_Matching_in_Robot_Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 本文提出了一种适用于通用机器人操作的可逆神经网络适配器，该适配器基于流匹配框架设计，通过单步去噪过程，在视觉、语言和本体感知等多模态观测条件下生成精确的高维动作。所提出的适配器能够有效将动作生成轨迹约束在可逆潜空间内，从而仅需单次推理步骤即可实现高效、高质量的灵巧动作合成。与传统的迭代流匹配策略相比，该框架在保持强动作预测精度和稳定性的同时，显著降低了推理复杂度。通过在多种仿真基准测试和真实机器人平台上开展的大量实验，验证了所提方法的有效性。在仿真基准测试中，该适配器在各类操作任务上持续展现出优于或接近当前最优的性能。此外，真实世界实验表明，该适配器显著提升了视觉-语言-动作（VLA）模型的推理效率，在保持强任务性能的同时，将平均推理延迟从110毫秒降低至61毫秒。

---

### 4. Sensor Configuration Matters: A Systematic Evaluation of Multimodal SLAM on Quadruped Robots

- **作者**: Roberto Corlito, Fabian Schmidt, Nils Seibert, Markus Enzweiler, Abhinav Valada, Arne Roennau
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.19067v1)
- **发表日期**: 2026-06-17
- **匹配关键词**: navigation, localization and mapping, autonomous navigation
- **arXiv**: [2606.19067v1](http://arxiv.org/abs/2606.19067v1)
- **📥 PDF**: 已下载至本地 (`2606.19067v1_Sensor_Configuration_Matters_A_Systematic_Evaluation_of_Multimodal_SLAM_on_Quadruped_Robots.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 四足机器人在多样化环境中的自主导航，从根本上依赖于具有鲁棒性的同步定位与地图构建（SLAM）技术。尽管视觉-惯性SLAM已在轮式、手持和空中平台上趋于成熟，但在腿部运动剧烈动力学条件下，硬件级传感器配置如何影响性能仍存在关键评估空白。四足机器人会带来独特的本体感知挑战，包括足部冲击、高频机械振动和快速角旋转，这些都会降低标准感知管线的性能。为填补这一空白，我们利用在ANYmal D四足机器人上记录的GrandTour数据集，对当前最先进的视觉、视觉-惯性以及激光雷达-视觉-惯性SLAM方法进行了系统性评估。我们分离并量化了相机模态、快门技术和惯性传感器层级的影响，分析了它们在定位精度、算法鲁棒性和计算资源利用方面的权衡。实验结果表明，硬件选择对系统鲁棒性具有显著影响：立体配置始终优于单目和RGB-D模态；全局快门相机相比卷帘快门相机能显著减少运动导致的跟踪失败；尤为关键的是，在剧烈腿部运动条件下，标准惯性集成反而可能降低以视觉为主的框架的性能。这些发现还为定制传感器载荷以在敏捷腿部系统上实现可靠感知提供了具体的设计指南。

---

### 5. Motion-Focused Latent Action Enables Cross-Embodiment VLA Training from Human EgoVideos

- **作者**: Runze Xu, Yiluo Zhang, Jian Wang, Yu Wang, Jincheng Yu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.18955v1)
- **发表日期**: 2026-06-17
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2606.18955v1](http://arxiv.org/abs/2606.18955v1)
- **📥 PDF**: 已下载至本地 (`2606.18955v1_Motion-Focused_Latent_Action_Enables_Cross-Embodiment_VLA_Training_from_Human_EgoVideos.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 训练通用视觉-语言-动作（VLA）模型通常需要海量、多样化的机器人数据集，并附带高保真度的动作标注。尽管以自我为中心的人类操作视频资源丰富且能捕捉显著的环境多样性，但缺乏动作标签使其难以应用于传统训练范式。为解决这一问题，我们提出了一种基于潜在动作的框架，旨在从无标签人类视频中提取通用动作先验。该架构采用混合解耦VQ-VAE，通过物理掩码将运动动态与环境背景分离，从而构建跨具身动作码本。通过使用该码本对人类视频进行预训练，视觉语言模型（VLM）主干网络能够学习动作意图的深层表征。针对特定具身形态的适配，我们引入意图-感知解耦策略：VLM预测动作意图，而独立的冻结视觉编码器为动作专家提供状态特定特征，从而减少动作幻觉。仿真与真实环境实验结果表明，仅使用无标签人类视频预训练的该方法，其性能可与基于大规模标注数据集训练的最先进VLA模型相媲美，且仅需50条轨迹即可完成下游适配。

---

### 6. Object-Centric Residual RL for Zero-Shot Sim-to-Real VLA Enhancement

- **作者**: Kinam Kim, Namiko Saito, Heecheol Kim, Katsushi Ikeuchi, Jaegul Choo, Yasuyuki Matsushita
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.18953v1)
- **发表日期**: 2026-06-17
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2606.18953v1](http://arxiv.org/abs/2606.18953v1)
- **📥 PDF**: 已下载至本地 (`2606.18953v1_Object-Centric_Residual_RL_for_Zero-Shot_Sim-to-Real_VLA_Enhancement.pdf`)
- **🔓 开源**: PROJECT_PAGE
- **中文摘要**: 视觉-语言-动作（VLA）模型能够泛化到多种操作任务，但其基于模仿学习的策略在精确物理交互中仍因累积执行误差而表现脆弱。能否通过纯仿真训练的强化学习策略零样本提升真实世界VLA的鲁棒性？残差强化学习（Residual RL）在冻结的VLA模型之上学习修正策略，为此提供了自然框架，但现有方法面临根本性的仿真到现实困境：基于特权状态的方法需要有损蒸馏才能部署；基于图像的方法受视觉域差异影响；而真实世界RL成本高昂且存在安全隐患。我们提出一种以物体为中心的残差RL框架，利用物体位姿优化VLA动作，构建可在仿真与现实间稳定迁移的紧凑观测空间。为对齐两个域，我们额外在仿真中回放相同的遥操作演示，以训练真实世界VLA的仿真对应模型。残差RL策略仅在仿真中通过位姿噪声注入和丢弃机制训练，并零样本迁移至真实机器人。在真实Franka Research 3（FR3）机器人上的五项操作任务中，我们的方法将零样本成功率从42%提升至76%，且改进后的轨迹可进一步用于重新训练基础VLA模型实现自我优化，无需额外遥操作。项目页面：https://www.microsoft.com/en-us/research/articles/object-centric-residual-rl/

---

### 7. HALOMI: Learning Humanoid Loco-Manipulation with Active Perception from Human Demonstrations

- **作者**: Zehui Zhao, Yuxuan Zhao, Gaojing Zhang, Chenxi Liu, Maolin Zheng, Wenzhao Lian
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.18772v1)
- **发表日期**: 2026-06-17
- **匹配关键词**: navigation, active perception, bimanual manipulation
- **arXiv**: [2606.18772v1](http://arxiv.org/abs/2606.18772v1)
- **📥 PDF**: 已下载至本地 (`2606.18772v1_HALOMI_Learning_Humanoid_Loco-Manipulation_with_Active_Perception_from_Human_Demonstrations.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 人类示范能够大规模收集并自然捕捉主动的手眼协调，是学习人形机器人全身操控的有前景数据源。然而，直接将人类示范迁移至人形机器人需要精确的世界坐标系跟踪控制器，该控制器在分布外目标下往往脆弱易失效，同时人形机器人与人类在自我中心观测和动作执行方面仍存在差距。为解决这些挑战，我们提出HALOMI——一个从人类示范中学习具有主动感知能力的人形机器人全身操控的可扩展框架。HALOMI扩展了通用操控接口，通过自我中心感知大规模采集自我视角和腕部视角的观测数据，以及头部-手部轨迹。我们进一步提出流形约束控制器，在学习的潜在行为流形中进行规划，以实现世界坐标系下精确鲁棒的头部-手部跟踪。为弥合人形机器人与人类的差距，我们进行自我视角对齐，并引入控制器感知的参考轨迹自适应方法，以减少观测和动作执行中的不匹配。我们在配备主动颈部的宇树G1人形机器人上，通过五项涉及导航、抓取、双臂操控、全身协调和动态行为的真实世界任务验证了HALOMI。在三个定量评估任务中，HALOMI实现了平均85%的成功率，而额外的定性演示展示了其支持动态抛掷和深蹲抓取的能力。

---

### 8. Generating Natural and Expressive Robot Gestures through Iterative Reinforcement Learning with Human Feedback using LLMs

- **作者**: Chris Lee, Flora Salim, Benjamin Tag, Francisco Cruz
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.18747v1)
- **发表日期**: 2026-06-17
- **匹配关键词**: HRI, human-robot interaction
- **arXiv**: [2606.18747v1](http://arxiv.org/abs/2606.18747v1)
- **📥 PDF**: 已下载至本地 (`2606.18747v1_Generating_Natural_and_Expressive_Robot_Gestures_through_Iterative_Reinforcement_Learning_with_Human.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 表达性手势对于自然有效的沟通至关重要，能在语言信息不足时（例如指向动作）补充言语表达。对于像Pepper这样的人形社交机器人而言，生成自然且富有表现力的动作对于改善人机交互（HRI）和长期接受度至关重要。然而，由于依赖专家编写的动画，手势生成仍面临挑战，导致动作僵化，难以适应动态多变的环境。另一方面，机器学习方法往往难以捕捉感知自然性，随着自由度增加，这一挑战愈发严峻。因此，生成富有表现力的机器人手势需要一套既能适应环境，又能遵循社会规范和物理约束的系统。大语言模型（LLMs）的最新进展实现了动态代码生成，为从自然语言实时合成手势提供了新机遇。本文中，我们将ChatGPT集成到人形机器人Pepper中，以生成与对话输出同步的伴随语言手势。尽管这一基线方法实现了灵活的手势生成，但生成的动作常显得僵硬且不自然。为解决这一局限，我们引入了一种基于人类反馈的迭代强化学习（RLHF）系统，通过用户评估对手势生成进行微调，并利用迭代用户研究比较Pepper生成的手势。结果表明，RLHF提升了LLM的伴随语言生成能力，产生了更具表现力、相关性和流畅性的动作。

---

### 9. EffiNav: Fusing Depth and Vision-Language for Efficient Object Goal Navigation

- **作者**: Zecheng Yin, Benedict Jun Ma
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.18634v1)
- **发表日期**: 2026-06-17
- **匹配关键词**: navigation, exploration
- **arXiv**: [2606.18634v1](http://arxiv.org/abs/2606.18634v1)
- **📥 PDF**: 已下载至本地 (`2606.18634v1_EffiNav_Fusing_Depth_and_Vision-Language_for_Efficient_Object_Goal_Navigation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 在未知环境中定位目标物体是自主智能体的基本能力，其应用范围涵盖搜索救援到野外机器人等场景。该任务的简化版本称为目标导向导航（Object Goal Navigation, ObjNav）。在ObjNav任务中，成功抵达目标物体是衡量性能的基本指标；然而，导航轨迹的效率同样重要，因为它反映了智能体探索的智能程度以及后续任务可用的时间余量。在未知环境中，高效导航的关键在于决定下一步的探索方向。尽管许多先前工作致力于解决这一核心挑战并在特定场景中取得了良好性能，但近期基于训练的模型和非训练框架仍分别存在泛化能力不足和效率低下的问题，最坏情况下可能导致对已访问区域的过度探索或冗余的往复运动。我们在两个广泛使用的仿真基准——Habitat Matterport 3D（HM3D）和开放词汇目标导航（OVON）上评估了EffiNav，并在真实物理机器人上验证了其有效性。通过对大量仿真回合的失败分析，我们仅需最小化修改即可将EffiNav扩展到GOAT-BENCH数据集上的记忆增强型ObjNav任务，证明了其超越标准ObjNav设置的适应性。在成功率（SR）和路径长度加权成功率（SPL）两项标准指标上，EffiNav达到或超越了近期基线方法，体现了其高效性、鲁棒性和实际应用价值。考虑到两个数据集的不同侧重点，实验结果表明该框架在高效ObjNav任务中具有更均衡和更泛化的性能表现。

---

### 10. SC3-Eval: Evaluating Robot Foundation Models via Self-Consistent Video Generation

- **作者**: Wei-Cheng Tseng, Gashon Hussein, Yuzhu Dong, Allen Z. Ren, Lucy X. Shi, XuDong Wang, Sergey Levine, Zhaoshuo Li, Jinwei Gu, Florian Shkurti, Ming-Yu Liu, Quan Vuong ⭐
  - **高亮作者**: Sergey Levine
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.18610v1)
- **发表日期**: 2026-06-17
- **匹配关键词**: vision-language-action
- **arXiv**: [2606.18610v1](http://arxiv.org/abs/2606.18610v1)
- **📥 PDF**: 已下载至本地 (`2606.18610v1_SC3-Eval_Evaluating_Robot_Foundation_Models_via_Self-Consistent_Video_Generation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 在现实世界中评估通用机器人操作策略成本高昂、速度缓慢且难以规模化。基于动作条件的视频世界模型通过模拟策略推演提供了一种可扩展的替代方案。自回归推演会累积复合误差，多视角观测必须保持相互一致性，且评估器需泛化至行为超出训练分布的策略。我们提出SC3-Eval方法应对这些挑战——这是一种自一致视频生成方案，通过强制实施三种互补一致性约束，将预训练视频基础模型转化为精准策略评估器。其一，前向-逆向动力学一致性联合训练模型，使其既能根据动作预测帧序列，又能从帧序列中恢复动作，将生成推演锚定于物理合理的动作流形，并抵消纯前向模型无法惩罚的漂移。其二，跨视角一致性训练模型通过其他视角补全当前视角，无需显式记忆机制即可在多视角观测的长程推演中保持连贯性。其三，测试时一致性在推理阶段复用逆向动力学模式，将其作为每动作块的置信度信号，当生成帧偏离指定动作时终止推演。我们还证明SC3-Eval推演能复现策略在真实推演中表现出的故障模式，支持细粒度诊断性比较而不仅是聚合排名。在七种真实世界视觉-语言-动作策略上，SC3-Eval实现了0.929的闭环皮尔逊相关系数和0.119的MMRV指标，超越三种基于视频模型的强基线方法，并能泛化至新任务。

---

### 11. DREAM-Chunk: Reactive Action Chunking with Latent World Model

- **作者**: Wenxi Chen, Kaidi Zhang, Chi Lin, Zhiyuan Zhang, Yu She, Yuejiang Liu, Raymond A. Yeh, Shaoshuai Mou, Yan Gu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.18589v1)
- **发表日期**: 2026-06-17
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2606.18589v1](http://arxiv.org/abs/2606.18589v1)
- **📥 PDF**: 已下载至本地 (`2606.18589v1_DREAM-Chunk_Reactive_Action_Chunking_with_Latent_World_Model.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 动作分块已成为视觉-语言-动作（VLA）模型的通用接口，使得低频策略推理能够驱动高频机器人执行。然而，一旦动作分块被提交，其在随机动力学、硬件执行误差和部分可观测性条件下，开环执行可能变得脆弱。我们提出DREAM-Chunk，一种测试时扩展方法，通过轻量级潜在世界模型增强基于分块的策略，无需额外策略微调。在测试时，DREAM-Chunk采样多个候选动作分块，展开其预测的潜在未来状态，并从预测状态与观测展开最匹配的分块中选择动作。通过这种方式，DREAM-Chunk利用额外的测试时计算覆盖多个可能的随机未来，并在长时域分块执行过程中提升响应能力。在Kinetix基准测试中，DREAM-Chunk在动作噪声增加时提升了鲁棒性，并受益于更大的候选样本量，尤其在演示包含修正行为时。我们进一步在两种机器人平台的四个操作任务和两种VLA策略下，针对多种随机性来源验证了DREAM-Chunk。在仿真和硬件实验中，DREAM-Chunk提升了动作分块策略在随机动力学中的鲁棒性。

---

### 12. VEGA: Learning Navigation VLAs from In-the-Wild Egocentric Video with Geometric Trajectory Supervision

- **作者**: Gershom Seneviratne, Yohan Abeysinghe, Jianyu An, Vaibhav Shende, Dinesh Manocha
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.18426v1)
- **发表日期**: 2026-06-16
- **匹配关键词**: navigation, VLA
- **arXiv**: [2606.18426v1](http://arxiv.org/abs/2606.18426v1)
- **📥 PDF**: 已下载至本地 (`2606.18426v1_VEGA_Learning_Navigation_VLAs_from_In-the-Wild_Egocentric_Video_with_Geometric_Trajectory_Supervisio.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出VEGA方法，一种从无标注的第一人称导航视频中训练视觉-语言-动作（VLA）导航模型的技术。互联网规模的第一人称视频提供了可扩展的导航相关视觉观测来源，捕捉了真实空间中的杂乱场景、近距离障碍物和自然人体运动。然而，这些视频无法直接用于策略学习，因为它们无法提供基于机器人坐标系中明确导航目标的障碍物感知轨迹。VEGA通过从单目视频重建局部场景几何结构、采样导航目标（以文本、图像或空间路径点形式表示）并利用重建的几何结构生成障碍物感知轨迹来解决这一差距。随后，利用生成的轨迹分布训练基于流匹配的VLA导航策略。通过仅在训练阶段使用几何信息，VEGA将障碍物感知规划直接提炼为基于视觉的策略。此外，我们引入VEGA-Bench基准测试，包含25万场景和约500万个与场景几何配对的导航目标，旨在评估VLA的目标进展、碰撞避免和障碍物规避能力。实验表明，在VEGA-Bench上，VEGA在实现具有竞争力的目标进展的同时，碰撞率降低33.0%，障碍物规避能力提升17.9%；在真实世界测试中，成功率至少提升150.0%，碰撞率至少降低66.7%，障碍物规避能力至少提升60.0%。最终，我们证明视频衍生的几何监督为训练障碍物感知导航VLA提供了可扩展且有效的信号。代码和基准测试将在论文发表时开源。

---

### 13. Zero-Shot Long-Horizon Dexterous Manipulation via Multi-View 3D-Grounded VLM Reasoning

- **作者**: Jisoo Kim, Sangwon Baik, Taeksoo Kim, Sungjoo Kim, Junyoung Lee, Mingi Choi, Hanbyul Joo
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.19340v1)
- **发表日期**: 2026-06-17
- **匹配关键词**: VLA, affordance
- **arXiv**: [2606.19340v1](http://arxiv.org/abs/2606.19340v1)
- **📥 PDF**: 已下载至本地 (`2606.19340v1_Zero-Shot_Long-Horizon_Dexterous_Manipulation_via_Multi-View_3D-Grounded_VLM_Reasoning.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出了一种零样本框架，用于长时程灵巧操作，该框架将语言指令从校准的多视角RGB图像中转化为可执行的3D任务规划。不同于训练端到端策略，我们的系统利用视觉语言模型（VLM）生成参考系任务定位和原始级别的2D关键点，再通过多视角融合将其提升至3D空间。这种提升结合了视角级VLM定位的三角测量与参考视角射线投票——后者沿语义相机射线搜索相邻视角中几何一致的关键点候选。生成的3D关键点同时支持抓取放置与工具使用：对于工具使用，我们根据推断的技能类别检索以物体为中心的原子动作，并将其存储的6D工具轨迹与场景对齐；对于灵巧执行，我们将提升后的抓取关键点扩展为任务条件化的抓取可供性区域，并通过手臂-手部运动生成器生成可行的抓取-运动对。真实世界实验表明，与单视角RGB-D定位及微调VLA基线相比，本方法在3D定位精度和执行可靠性上均有提升。我们进一步通过闭环状态验证与重规划实现长时程操作，在未见物体和新型场景中完成零样本工具使用任务。

---

### 14. NeuMesh++: Towards Versatile and Efficient Volumetric Editing with Disentangled Neural Mesh-based Implicit Field

- **作者**: Chong Bao, Yuan Li, Bangbang Yang, Yujun Shen, Hujun Bao, Zhaopeng Cui, Yinda Zhang, Guofeng Zhang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.19316v1)
- **发表日期**: 2026-06-17
- **匹配关键词**: neural rendering, neural radiance field
- **arXiv**: [2606.19316v1](http://arxiv.org/abs/2606.19316v1)
- **📥 PDF**: 已下载至本地 (`2606.19316v1_NeuMesh++_Towards_Versatile_and_Efficient_Volumetric_Editing_with_Disentangled_Neural_Mesh-based_Imp.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://zju3dv.github.io/neumeshplusplus/
- **中文摘要**: 近年来，神经隐式渲染技术发展迅速，在新视角合成和三维场景重建方面展现出显著优势。然而，现有用于编辑目的的神经渲染方法功能有限，例如仅支持刚性变换和特定类别的编辑。本文提出了一种基于网格的新型表示方法，通过在网格顶点上编码解耦的几何、纹理和语义码来构建神经辐射场，从而支持一系列高效且全面的编辑功能，包括网格引导的几何编辑、通过纹理交换、填充和绘制操作实现的指定纹理编辑，以及语义引导的编辑。为此，我们开发了多项技术：一种新颖的局部空间参数化方法以提升渲染质量和训练稳定性；一种顶点上的可学习修改颜色以提高纹理编辑的保真度；一种空间感知优化策略以实现精确的纹理编辑；以及一种语义辅助的区域选择方法以简化隐式场编辑中繁琐的标注工作。在真实和合成数据集上的大量实验和编辑示例表明，我们的方法在表示质量和编辑能力方面具有优越性。项目页面：https://zju3dv.github.io/neumeshplusplus/

---

### 15. Hand-4DGS: Feed-Forward 3D Gaussian Splatting for 4D Hand Reconstruction from Egocentric Videos

- **作者**: Jeongmin Bae, Seoha Kim, Marc Pollefeys, Mahdi Rad, Youngjung Uh, Taein Kwon ⭐
  - **高亮作者**: Marc Pollefeys
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.19156v1)
- **发表日期**: 2026-06-17
- **匹配关键词**: gaussian splatting, 3D gaussian splatting
- **arXiv**: [2606.19156v1](http://arxiv.org/abs/2606.19156v1)
- **📥 PDF**: 已下载至本地 (`2606.19156v1_Hand-4DGS_Feed-Forward_3D_Gaussian_Splatting_for_4D_Hand_Reconstruction_from_Egocentric_Videos.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 从第一人称视角视频中进行动态3D手部重建对于下一代计算平台（如AR/VR和AI眼镜）至关重要。尽管其重要性显著，但以往的研究大多聚焦于多视角3D手部重建或4D人体重建。由于头部快速运动、手部动态剧烈、严重遮挡以及单视角观测固有的模糊性，第一人称视角的4D手部重建仍面临挑战。为解决这些问题，我们提出Hand-4DGS——首个直接从第一人称视频重建动态4D手部的前馈框架，支持快速推理（约60 FPS）并具备强泛化能力。该方法通过网格引导表示提供结构先验，并利用时间卷积建模动态运动。我们在两个具有挑战性的第一人称数据集H2O和ARCTIC上评估了该框架，结果表明其显著优于基线方法。得益于前馈网络的泛化能力以及通过高斯泼溅实现的有效二维图像监督，我们的方法无需昂贵的3D手部姿态真实标注即可实现优异性能。

---

### 16. FlowObject: Flow Steering for Bridging Generative Priors and Reconstruction Fidelity

- **作者**: Yuchen Rao, Xuqian Ren, Yinyu Nie, Sayan Deb Sarkar, Biao Zhang, Vincent Lepetit, Friedrich Fraundorfer
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.19019v1)
- **发表日期**: 2026-06-17
- **匹配关键词**: gaussian splatting, 3D gaussian splatting, 3d reconstruction, 3D reconstruction
- **arXiv**: [2606.19019v1](http://arxiv.org/abs/2606.19019v1)
- **📥 PDF**: 已下载至本地 (`2606.19019v1_FlowObject_Flow_Steering_for_Bridging_Generative_Priors_and_Reconstruction_Fidelity.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 从少量随意拍摄的图像中恢复物体的完整三维表示仍是一项重大挑战。近年来，基于流匹配（Flow-Matching, FM）的三维生成模型能够合成高质量的纹理资产，但这类方法常存在"合成偏差"问题——学习先验会覆盖观测证据，同时缺乏与观测实例的对齐。相比之下，基于优化的方法（如三维高斯泼溅法，3DGS）虽能在可见表面实现高保真度，却无法推理未观测区域的几何结构。本文提出FlowObject框架，将稀疏视角三维重建重新定义为无需训练的引导式逆问题。该方法采用双空间引导策略，通过流匹配模型的常微分方程（ODE）轨迹调控，在利用生成先验补全未观测区域的同时，严格保持与现实观测的一致性。通过集成3DGS精化阶段，FlowObject进一步弥合了"合成感"生成输出与照片级重建之间的差距。在合成数据集和真实世界数据集上的全面基准测试表明，现有最优方法难以同时实现几何完整性与观测一致性，尤其在严重遮挡场景下表现更甚。相比之下，我们的方法在几何完整性和视角相关外观保真度方面均显著超越当前最优的生成模型与优化框架。

---

### 17. EDoF-NeRF: extended depth-of-field neural radiance fields using a coded aperture camera

- **作者**: Yoshiyuki Shirasaki, Ryoichi Horisaki
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.18826v1)
- **发表日期**: 2026-06-17
- **匹配关键词**: nerf, neural radiance field
- **arXiv**: [2606.18826v1](http://arxiv.org/abs/2606.18826v1)
- **📥 PDF**: 已下载至本地 (`2606.18826v1_EDoF-NeRF_extended_depth-of-field_neural_radiance_fields_using_a_coded_aperture_camera.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出了一种扩展景深（DoF）的方法，用于构建高保真神经辐射场（NeRF）——这是一种基于隐式神经表征的新兴技术，能够从不同视角拍摄的图像数据集中渲染出逼真的新视角。由于NeRF所使用的数据集由传统相机采集，因此景深与进光量之间的权衡不仅存在于传统相机中，也存在于NeRF中。为解决这一问题，我们在相机光瞳处引入编码光圈，以保留离焦条件下的空间频率成分。我们开发了一种将编码光圈融入NeRF的相机模型，该模型可直接输入编码图像，并生成具有扩展景深的新视角。通过仿真与实验，我们验证了所提出的方法（称为扩展景深NeRF，即EDoF-NeRF），并证明其性能优于传统光圈相机。

---

## 📌 Poster

*其他相关研究*

---

### 1. Seeing Through Occlusion: Deterministic Arm Kinematic Correction for Robot Teleoperation

- **作者**: Thomas M. Kwok, Nicholas Koenig, Yue Hu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.19240v1)
- **发表日期**: 2026-06-17
- **匹配关键词**: human-robot interaction
- **arXiv**: [2606.19240v1](http://arxiv.org/abs/2606.19240v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 基于单RGB-D摄像头的无标记运动捕捉技术，为机器人遥操作提供了一种低成本、非侵入性的替代传统标记点系统的方法。然而，在自遮挡情况下（尤其是上肢运动时），深度估计往往会出现退化。本文提出了一种手臂运动学校正（AKC）方法，通过基于恒定臂长的几何约束来改进深度估计。该方法利用手腕位置和预设臂长，基于勾股定理的确定性公式重建被遮挡的关节深度，从而避免了复杂的概率建模或参数调优。通过Vicon参考系统的实验验证，采用均方根误差（RMSE）和皮尔逊相关系数评估，该方法在静态和动态关节运动中均表现出可靠性能。此外，在仿真和物理机器人环境中成功演示了运动映射遥操作。结果表明，即使与可靠性较低的时间滤波器配合使用，AKC方法也能在长时间、严重自遮挡条件下增强鲁棒性并保持解剖学一致性，突显了其在机器人遥操作和人机交互等实时应用中的实用性。

---

### 2. Monocular 3D Occupancy Perception for Robots on Sidewalks via Hybrid 2D-3D Learning

- **作者**: Yukai Ma, Joe Lin, Liu Liu, Honglin He, Lulu Ricketts, Brad Squicciarini, Yong Liu, Bolei Zhou
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.19122v1)
- **发表日期**: 2026-06-17
- **匹配关键词**: navigation
- **arXiv**: [2606.19122v1](http://arxiv.org/abs/2606.19122v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 现实世界中的人行道比道路更加拥挤、杂乱且结构松散，这使得三维占据预测成为配送机器人、电动轮椅等移动机器人安全导航的关键技术。现有占据学习流程主要面向道路自动驾驶场景，通常在大规模配准的激光雷达-可见光数据集上训练，依赖密集的三维监督信号和多摄像头输入，不仅采集成本高昂，且未能充分捕捉人行道的独特特征。为此，我们提出WalkOCC——一种面向人行道机器人的混合射线步进单目三维占据感知框架。该框架通过激光雷达-可见光配准数据显式耦合几何先验，同时利用大规模非配准单目图像实现可扩展学习。它从配准序列中引导生成伪占据监督信号，并在额外仅含二维图像的数据上联合学习图像级表征。该方法无需昂贵的三维占据标注即可实现稳定优化与泛化性能提升。大量实验表明，与基于自监督的图像基线方法相比，本方法在预测精度、路缘石和排水沟等细微城市结构的细粒度分割，以及对环境变化和跨载体迁移的鲁棒性方面均取得一致性提升。为便于评估与基准测试，我们还发布了Sidewalk3D——一个大规模人行道感知数据集，包含跨多地点、多时段采集的激光雷达-相机配准序列，并附有用于评估的三维语义占据标注。代码与数据将开源。

---

### 3. ART-VS: Adaptive Resolution Tiling for Vision Transformer Visual Servoing

- **作者**: Alessandro Scherl, Bernhard Neuberger, Simon Schwaiger, David Mulero-Pérez, Lucas Muster, Jose Garcia-Rodriguez
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.19089v1)
- **发表日期**: 2026-06-17
- **匹配关键词**: visual servoing
- **arXiv**: [2606.19089v1](http://arxiv.org/abs/2606.19089v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: CODE
  - 链接：https://art-vs.github.io/.
- **中文摘要**: 基于自监督视觉Transformer（ViT）特征的视觉伺服方法，能够实现无需训练的机器人定位并具备强泛化能力，但面临鲁棒性与精度之间的根本性权衡。粗粒度块级描述符虽能提供稳定对应关系，却限制了定位精度。提升图像分辨率可改善精度，但鲁棒性增益有限——在扰动条件下，尽管ViT块数量增加12倍，高分辨率处理仅将收敛成功率从76.6%提升至81.0%。为此，我们提出自适应分辨率分块视觉伺服方法（ART-VS），这是一种根据伺服进程自适应调整特征粒度的两阶段方法：粗粒度阶段采用ViT原生分辨率实现稳定对齐，随后进入分块高分辨率阶段，通过将匹配限制在局部邻域来提升定位精度。无需任何任务特定训练，ART-VS在扰动条件下达到95.4%的收敛率，较标准与全分辨率ViT伺服方法分别提升18.8和14.4个百分点。相较于前者，定位误差降低53%；相较于后者，运行速度提升10倍以上，显存占用减少27%。我们在三种ViT骨干网络上验证了ART-VS，并展示了针对未见物体实例的真实场景类别级抓取能力：透明瓶抓取成功率95/100，鞋类抓取成功率98/100。代码开源地址：https://art-vs.github.io/。

---

