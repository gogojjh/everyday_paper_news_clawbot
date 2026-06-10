# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-06-10 08:02

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 2/20 篇提供

**🌟 Highlight**: 17 篇 | **📌 Poster**: 3 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. MemoryVLA++: Temporal Modeling via Memory and Imagination in Vision-Language-Action Models

- **作者**: Hao Shi, Weiye Li, Bin Xie, Yulin Wang, Renping Zhou, Tiancai Wang, Xiangyu Zhang, Ping Luo, Gao Huang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.09827v1)
- **发表日期**: 2026-06-08
- **匹配关键词**: VLA, vision-language-action, vision-language-action model
- **arXiv**: [2606.09827v1](http://arxiv.org/abs/2606.09827v1)
- **📥 PDF**: 已下载至本地 (`2606.09827v1_MemoryVLA++_Temporal_Modeling_via_Memory_and_Imagination_in_Vision-Language-Action_Models.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://shihao1895.github.io/MemoryVLA-PP-Web
- **中文摘要**: 时间建模对于机器人操作至关重要，因为有效控制既需要记忆过去的交互，也需要想象未来的状态。然而，大多数VLA模型主要依赖当前观测，因此在长时域、时间依赖型任务中表现不佳。认知科学表明，人类依赖工作记忆缓冲短期情境，依赖海马系统保存过去经历的情景记忆，并依赖内部模型想象可能的未来状态演化。受这些机制启发，我们提出MemoryVLA++，一个完整的时间建模框架，为VLA模型配备记忆与想象能力以支持机器人操作。预训练的VLM将当前观测编码为感知和认知标记，形成工作记忆。这些标记查询感知-认知记忆库以检索相关历史情境。该记忆库存储来自过去交互的低层细节和高层语义，并通过冗余感知整合进行更新。一个世界模型在去噪潜在空间中想象未来状态，并在记忆引导下整合想象潜在表示，形成完整的时间感知标记。最终标记条件化一个扩散动作专家，以预测时间一致的动作序列。我们在5个仿真基准和3类真实机器人任务（涵盖3种机器人）上进行了广泛实验，覆盖通用操作、长时域时间任务、鲁棒性和泛化性。我们的方法在Libero、SimplerEnv、Mikasa-Robo、Calvin、Libero-Plus以及多种真实机器人任务上均取得了强劲性能，验证了结合记忆与想象的完整时间建模的有效性。例如，在真实机器人上，它在通用任务、记忆依赖任务和想象依赖任务上分别实现了+9%、+26%和+28%的性能提升。项目页面：https://shihao1895.github.io/MemoryVLA-PP-Web

---

### 2. Your Model Already Knows: Attention-Guided Safety Filter for Vision-Language-Action Models

- **作者**: Seongbin Park, Fan Zhang, Baharan Mirzasoleiman, Shahriar Talebi, Nader Sehatbakhsh
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.09749v1)
- **发表日期**: 2026-06-08
- **匹配关键词**: VLA, vision-language-action, vision-language-action model
- **arXiv**: [2606.09749v1](http://arxiv.org/abs/2606.09749v1)
- **📥 PDF**: 已下载至本地 (`2606.09749v1_Your_Model_Already_Knows_Attention-Guided_Safety_Filter_for_Vision-Language-Action_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型在多种机器人操作任务中展现出令人印象深刻的端到端性能。然而，这些策略无法保证避免与场景中任务无关物体的碰撞。现有安全过滤器通过查询视觉-语言模型（VLM）来识别障碍物及其位置，从而规避这一问题。但这种方法在控制循环中运行速度过慢，只能在任务初始化阶段调用一次，导致过滤器无法追踪移动障碍物。我们发现，VLA模型中的少量注意力头能够可靠地定位策略意图接近的目标物体。这些注意力头可在无训练的安全框架中加以利用：该框架每步从注意力头中获取当前活动目标，将场景其余部分视为障碍物，并将这些信息输入控制屏障函数（CBF）过滤器。结合轻量级实时目标追踪器，该方法能够实现对非静态障碍物的避碰。我们在SafeLIBERO基准测试（已扩展加入移动障碍物）上评估了该框架。在原始静态基准测试中，我们的方法性能与使用特权模拟器状态识别目标（模拟基于VLM的初始化阶段单次识别步骤）的基准方法相当。在动态变体测试中，当基准方法的初始化阶段目标分配失效时，我们的方法平均性能显著提升43%。研究结果表明，实时安全过滤所需的感知信号已存在于VLA策略内部，无需额外训练或繁重的辅助模型即可加以利用。

---

### 3. ProbeAct: Probe-Guided Training-Free Failure Recovery in Vision-Language-Action Models

- **作者**: Fan Zhang, Seongbin Park, Baharan Mirzasoleiman, Shariar Talebi, Nader Sehatbakhsh
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.09740v1)
- **发表日期**: 2026-06-08
- **匹配关键词**: VLA, vision-language-action, vision-language-action model
- **arXiv**: [2606.09740v1](http://arxiv.org/abs/2606.09740v1)
- **📥 PDF**: 已下载至本地 (`2606.09740v1_ProbeAct_Probe-Guided_Training-Free_Failure_Recovery_in_Vision-Language-Action_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型在训练分布内的语言条件机器人操作任务中展现出强大性能，但其泛化能力仍存在根本性局限。这些模型缺乏应对扰动所需的鲁棒性，当面临光照变化、相机视角改变或初始状态微小差异时，常常出现操作失败。我们提出PROBEACT——一种无需训练即可运行的运行时干预框架，能够在预训练VLA策略中检测并恢复抓取与放置失败，且无需修改模型权重或额外演示数据。PROBEACT整合三大组件：（i）轻量级多目标隐藏状态探针，通过中间VLA特征预测任务相关物体的三维位置，并采用匈牙利匹配身份追踪技术处理多物体场景；（ii）与物体无关的运动学状态机，仅利用夹爪内部信号与末端执行器运动学信息检测抓取、搬运和放置失败；（iii）分层控制障碍函数（CBF）滤波器，将重复失败位置编码为软安全集约束，在最小化修正VLA动作的同时保持基线行为。作为即插即用、无需训练的干预循环模块，PROBEACT与现有训练流程正交。在LIBERO-plus基准测试中，该框架作为通用安全网，将OpenVLA-OFT模型的成功率从69.6%提升至74.1%，并展现出对基础与微调VLA策略的广泛适用性。

---

### 4. Shape Formation for the Cooperative Transportation of Arbitrary Objects Using Multi-Agent Reinforcement Learning

- **作者**: Mohamed Sayed, Wolfram Burgard, Tanja Katharina Kaiser ⭐
  - **高亮作者**: Wolfram Burgard
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.09610v1)
- **发表日期**: 2026-06-08
- **匹配关键词**: navigation
- **arXiv**: [2606.09610v1](http://arxiv.org/abs/2606.09610v1)
- **📥 PDF**: 已下载至本地 (`2606.09610v1_Shape_Formation_for_the_Cooperative_Transportation_of_Arbitrary_Objects_Using_Multi-Agent_Reinforcem.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 协作物体运输在工业到家庭服务等多个领域至关重要。一种常见的运输策略是将物体置于多机器人系统上方进行搬运。该任务通常被分解为三个相互关联的子问题：编队控制、协作导航与避障。现实物体可能具有任意形状与非均匀质量分布，这要求机器人编队能够稳固支撑物体。针对此类真实物体的编队控制难题，本文提出了一种新颖的多智能体强化学习方法。该方法使多机器人系统能够自主定位至物体下方以支撑其重量，同时在编队过程中规避障碍物。我们在不同环境与不同数量机器人的实验评估表明，该方法能生成可靠策略，实现均衡编队，并泛化至复杂几何形状与非均匀质量分布的物体及杂乱场景。

---

### 5. CT-VAM: A Cerebello-Thalamic-Inspired Vision-Action Model for Efficient Visuomotor Control

- **作者**: Jiacheng Li, Yize Guo, Jiabin Guo, Qingchen Liu, Jiahu Qin
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.09572v1)
- **发表日期**: 2026-06-08
- **匹配关键词**: VLA, vision-language-action, vision-language-action model
- **arXiv**: [2606.09572v1](http://arxiv.org/abs/2606.09572v1)
- **📥 PDF**: 已下载至本地 (`2606.09572v1_CT-VAM_A_Cerebello-Thalamic-Inspired_Vision-Action_Model_for_Efficient_Visuomotor_Control.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作模型在机器人操作领域展现出巨大潜力，但原始语言主要被用于指定任务意图，而非在高频低层级执行过程中反复处理。基于这一分离特性，我们提出了一种受小脑-丘脑启发的视觉-动作模型（CT-VAM），用于高效的任务条件化视觉运动控制。CT-VAM作为紧凑的局部执行策略，通过双视角视觉观测、本体感知及轻量级任务条件预测动作片段，有望实现实用的云-边协同范式——大型模型处理高层语义推理，而本地硬件运行快速闭环控制。为有效融合异构输入，CT-VAM引入了TARS（丘脑动作路由流），这是一种流分离的条件注意力解码器，可独立路由动作、视觉和任务流，避免密集的感知标记淹没紧凑的任务相关条件。仅含6800万参数的CT-VAM在LIBERO基准测试中取得了与规模更大的VLA模型相媲美的成功率，同时降低了推理延迟。结合用于异步片段执行的流一致性修复技术，CT-VAM支持高频控制，并在资源受限的机器人平台上展现出稳健的实际部署能力。

---

### 6. Targeting World Models to Compromise Robot Learning Pipelines

- **作者**: Ethan Rathbun, Ahmed Agha, Saaduddin Mahmud, Christopher Amato, Alina Oprea, Eugene Bagdasarian
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.09499v1)
- **发表日期**: 2026-06-08
- **匹配关键词**: VLA
- **arXiv**: [2606.09499v1](http://arxiv.org/abs/2606.09499v1)
- **📥 PDF**: 已下载至本地 (`2606.09499v1_Targeting_World_Models_to_Compromise_Robot_Learning_Pipelines.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 世界模型近年来在流行度和能力上迅速增长，成为生成机器人训练数据或模拟真实世界环境的更高效数据工具，许多研究提出将其整合到机器人学习流程中。尽管具有高度实用性，但本研究证明，世界模型为机器人学习供应链引入了一种独特且隐蔽的有效数据投毒入口，可能导致部署不安全或受损的机器人策略，即使训练数据看似安全且基于真实数据。与传统数据投毒技术直接将危险轨迹植入已售或已上传数据集不同，我们的新型攻击方法将恶意提示或破坏性转移动态注入到视觉上安全的远程操作数据集中，这些数据仅在通过世界模型作为输入时被激活。这可能导致生成合成且危险的机器人训练轨迹，进而产生不安全或受损的机器人策略。我们针对最先进的基于动作条件和文本条件的世界模型展示了攻击的有效性，在下游深度强化学习策略上实现了完整的端到端后门攻击，并在视觉-语言-动作设置中提供了概念验证。总体而言，这些发现要求对更安全的世界模型进行研究，并重新评估其在机器人学习供应链中的位置。

---

### 7. Harness Engineering for Physical AI: Robot Middleware Is the Harness Layer

- **作者**: Sanghoon Lee, Jiyeong Chae, Kyung-Joon Park
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.09416v1)
- **发表日期**: 2026-06-08
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2606.09416v1](http://arxiv.org/abs/2606.09416v1)
- **📥 PDF**: 已下载至本地 (`2606.09416v1_Harness_Engineering_for_Physical_AI_Robot_Middleware_Is_the_Harness_Layer.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 机器人中间件在物理AI时代面临新的角色。学习策略、规划器以及视觉-语言-动作（VLA）模型如今作为控制路径上的因果参与者进入已部署的机器人系统，但将它们与时序、调度和网络集成的中间层尚未被命名。近期语言智能体领域的研究将这一层称为"驾驭层"（harness），即协调工具、管理状态、约束资源并记录执行的外部系统。机器人学界尚未采纳这一框架，我们提出机器人中间件正是这种驾驭层。物理AI驾驭层与软件驾驭层的区别在于干预位置：软件驾驭层在工具调用边界进行协调，而物理AI驾驭层必须同时协调控制、计算和通信三个维度——因为学习策略的输出跨越全部三者：其指令改变轨迹，其推理时间改变调度，其数据负载改变带宽。机器人中间件是机器人堆栈中最低层且具备覆盖三者的协调抽象层，因此最适合构建它们的强制执行机制。它已提供驾驭层所需的大部分功能，但缺乏针对AI模型的强制执行机制。我们将缺失的强制执行机制命名为三项功能：投射（Projection）在输出时对每个结果进行门控，隔离（Isolation）约束模型的执行与传输时隙，转移（Transfer）在检查失败时回退至已验证基线。这些功能当前在已部署的机器人系统中均以手工构建的应用代码形式存在，构建于机器人中间件已提供的接口之上。机器人中间件不应仅作为单一维度的执行器，而应作为整合这三者的层级。我们将其勾勒为ROS 2驾驭层配置文件（ROS 2 Harness Profile），这是一种部署构件，承载AI模型声明的输出区域、推理预算和运行机制，同时由中间件在ROS 2、DDS和Zenoh协议栈中强制执行。

---

### 8. TORL-VLA: Tactile Guided Online Reinforcement Learning for Contact-Rich Manipulation

- **作者**: Huaihang Zheng, Yi Yang, Kai Ma, Shenglin Xu, Tian Xie, Guozheng Li, Xiangyu Wang, Yiren Ma, Si Liu, Yinian Mao, Baoxu Liu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.09337v1)
- **发表日期**: 2026-06-08
- **匹配关键词**: contact-rich manipulation, VLA, vision-language-action
- **arXiv**: [2606.09337v1](http://arxiv.org/abs/2606.09337v1)
- **📥 PDF**: 已下载至本地 (`2606.09337v1_TORL-VLA_Tactile_Guided_Online_Reinforcement_Learning_for_Contact-Rich_Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型已成为机器人操作领域的强大框架，近期研究通过引入触觉或力反馈扩展了VLA在接触密集型任务中的应用。然而，这类模型通常以离线策略形式部署。当接触条件偏离训练数据分布时，策略无法进行在线自适应，导致接触力不当、重试效率低下等问题。为此，我们提出TORL-VLA——一种触觉引导的在线强化学习框架，通过耦合触觉反馈与策略优化实现接触密集型操作。该方法引入触觉衍生力矩感知VLA模型，用于预测参考动作与未来力矩序列，同时采用轻量级在线强化学习模块对参考动作进行优化。为稳定混合探索性策略生成数据与人工干预数据的学习过程，我们设计了干预截断评判器，防止干预后的成功信号被错误归因于干预前的策略生成动作。在包含门闩操作、咖啡杯放置和鸡蛋处理等长时域接触密集型任务的真实机器人实验中，TORL-VLA在子任务与完整任务层面的成功率及时间约束执行效率上均显著超越强基线方法。

---

### 9. MotionWAM: Towards Foundation World Action Models for Real-Time Humanoid Loco-Manipulation

- **作者**: Jia Zheng, Teli Ma, Yudong Fan, Zifan Wang, Shuo Yang, Junwei Liang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.09215v1)
- **发表日期**: 2026-06-08
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2606.09215v1](http://arxiv.org/abs/2606.09215v1)
- **📥 PDF**: 已下载至本地 (`2606.09215v1_MotionWAM_Towards_Foundation_World_Action_Models_for_Real-Time_Humanoid_Loco-Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 世界动作模型（WAMs）将视频动态先验与策略相结合，在桌面操作任务中展现出令人鼓舞的成果，但针对高维视频-动作潜在表示的迭代去噪过程使其速度过慢，无法满足实时人形机器人全身操控的需求。这一问题因主流分层范式而进一步加剧：高层操作策略仅控制上半身，而低层控制器则追踪粗略的基座指令——这导致上下半身处于不一致的动作空间，并将腿部功能简化为维持平衡的运动。我们提出MotionWAM，一种实时WAM模型，通过将策略条件建立在视频世界模型的中间去噪特征上，仅凭单目自中心摄像头即可驱动自主人形机器人全身操控。MotionWAM用统一的动作潜在表示取代了上下半身分离的架构，预测覆盖运动、躯干动作、高度调节、足部交互和手部操作的全身动作令牌，所有动作均处于单一动作空间。三阶段学习框架逐步将视频世界模型适配至自中心视觉动态及目标人形机器人本体。在九项真实世界Unitree G1任务中，MotionWAM实现实时运行，整体成功率较基于相同演示微调的视觉-语言-动作（VLA）基线模型提升超过30%，并执行了上下半身解耦策略无法实现的任务驱动型足部交互。我们的结果表明，经视频预训练的WAM模型可从桌面操作任务拓展至协调、类人的全身人形机器人控制。

---

### 10. Scaling by Diversified Experience for Vision-Language-Action Models

- **作者**: Leiyu Wang, Zhaofengnian Wang, Xueqi Li, Luoyi Fan, Cewu Lu, Nanyang Ye
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.09009v1)
- **发表日期**: 2026-06-08
- **匹配关键词**: VLA, vision-language-action, vision-language-action model
- **arXiv**: [2606.09009v1](http://arxiv.org/abs/2606.09009v1)
- **📥 PDF**: 已下载至本地 (`2606.09009v1_Scaling_by_Diversified_Experience_for_Vision-Language-Action_Models.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://sy-vla.github.io/
- **中文摘要**: 视觉-语言-动作模型在实际部署中面临重大挑战，原因在于高层推理与低层控制的相互纠缠以及策略优化的不稳定性。本文提出SyVLA——一种通过多样化经验训练的鲁棒VLA模型。我们设计了意图解耦算法，将控制相关特征从推理上下文中分离出来，并构建了基于相似样本引导的强化学习流水线，以稳定策略更新并缓解分布偏移。在真实机器人任务和多模态基准上的大量实验表明，与现有方法相比，SyVLA在任务成功率与分布外泛化能力上均取得更优表现，同时有效保留了核心视觉-语言能力。代码与数据集已发布于项目主页\href{https://sy-vla.github.io/}{sy-vla.github.io}。

---

### 11. SpaceVLN: A Zero-Shot Vision-and-Language Navigation Agent with Online Spatial Cognitive Memory and Reasoning

- **作者**: Yucheng Deng, Pingrui Lai, Xinhai Li, Chenjia Bai, Xiaoheng Deng, Chengnuo Sun, Xuelong Li, Hua Yang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.08992v1)
- **发表日期**: 2026-06-08
- **匹配关键词**: VLN, vision-and-language navigation, object-goal navigation, navigation
- **arXiv**: [2606.08992v1](http://arxiv.org/abs/2606.08992v1)
- **📥 PDF**: 已下载至本地 (`2606.08992v1_SpaceVLN_A_Zero-Shot_Vision-and-Language_Navigation_Agent_with_Online_Spatial_Cognitive_Memory_and_R.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 连续环境下的视觉与语言导航要求智能体理解未知环境的空间结构，以便遵循语言指令。尽管基础模型为零样本导航（无需特定任务策略训练）开辟了可行路径，但许多导航器仍依赖局部视觉线索和基于线性历史记录的推理，忽视了导航过程中探索区域、遍历路径、地标及其空间关系的空间本质。本文提出SpaceVLN——一种基于空间认知记忆与任务引导空间推理的导航智能体。具体而言，SpaceVLN引入高效的阶段式闭环框架，其中规划与执行围绕可验证的空间-地标阶段组织。导航过程中，智能体逐步将探索区域抽象为空间航点，并动态维护子任务锚定的地标证据，形成层次化空间认知记忆，用于进度定位与空间关系理解。基于该记忆，Spatial-CoT将任务进度推理与空间感知、分析及预测相结合，实现面向具身导航的任务引导空间推理。统一的阶段接口使SpaceVLN能够在统一零样本设置下同时处理视觉与语言导航及目标导向导航任务，无需特定任务策略训练。在R2R-CE、RxR-CE、GN-Bench和HM3D-OVON基准测试中，SpaceVLN取得了最先进的零样本性能，真实机器人部署进一步验证了其适用性。这些结果凸显了空间认知记忆与任务引导空间推理作为构建更强具身导航智能体的实用基础。

---

### 12. C$^3$ache: Accelerating World Action Models with Cross Inference Chunk Cache

- **作者**: Weisen Zhao, Lam Nguyen, Zhicong Lu, Yuzhang Shang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.08962v1)
- **发表日期**: 2026-06-08
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2606.08962v1](http://arxiv.org/abs/2606.08962v1)
- **📥 PDF**: 已下载至本地 (`2606.08962v1_C$^3$ache_Accelerating_World_Action_Models_with_Cross_Inference_Chunk_Cache.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 世界动作模型（WAMs）在泛化能力上优于标准视觉-语言-动作（VLA）策略，能够更好地适应新动作和新环境，这是因为其视频建模目标使其能够从大量未标注视频中学习，而非依赖稀缺的标注机器人演示数据。然而，这种泛化能力带来了高昂的计算成本。为完成一项任务，WAM需运行多个推理片段，每个片段都需要昂贵的去噪过程。现有加速方法通过缓存和复用单个片段去噪轨迹中的计算来降低这一成本。我们的实证分析揭示了它们忽略的一个重大冗余来源：片段间的冗余。当机器人执行平滑行为时，在给定去噪步骤中计算的残差在连续片段间具有强相关性。我们提出C$^3$ache——一种无需训练的方法，能够在相同去噪步骤的推理片段间缓存并复用这些残差。基于Fast-WAM骨干网络的基准实验表明，C$^3$ache在总端到端推理时间上实现了最高$2.5\times$的加速，且任务成功率几乎无下降。

---

### 13. Benchmarking Vision-Language-Action Models on SO-101: Failure and Recovery Analysis

- **作者**: Yi Yu, Xinchuan Qiu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.08881v1)
- **发表日期**: 2026-06-07
- **匹配关键词**: VLA, vision-language-action, vision-language-action model
- **arXiv**: [2606.08881v1](http://arxiv.org/abs/2606.08881v1)
- **📥 PDF**: 已下载至本地 (`2606.08881v1_Benchmarking_Vision-Language-Action_Models_on_SO-101_Failure_and_Recovery_Analysis.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型在机器人操作中展现出强大的泛化能力，然而现有评估主要基于仿真环境或昂贵的机器人平台，其在低成本真实机器人上的鲁棒性尚未得到充分探索。我们提出了一套标准化的真实世界基准测试，用于在低成本SO-101机器人平台上评估代表性VLA模型与模仿学习策略。该基准包含四项典型操作任务及统一评估协议，能够在具身不确定性条件下进行系统性比较。通过真实遥操作演示数据，我们在物理平台上直接微调并评估了$π_{0.5}$、SmolVLA、Wall-X和ACT模型。除传统任务成功率外，该基准引入了结构化失败分类体系、语义级与执行级失败分解机制，以及考虑恢复能力的评估指标，以刻画策略鲁棒性。实验结果表明，预训练更强的VLA策略整体优于模仿学习基线，但在低成本机器人部署条件下，性能仍高度依赖具体任务。执行不稳定性成为主要失败来源，而不同架构的恢复能力差异显著。这些结果凸显了超越二元任务成功率的失败与恢复分析的重要性，并将SO-101确立为在真实低成本机器人部署条件下评估具身AI系统的实用基准。

---

### 14. Unifying Object-Centric World Models and Diffusion Policy: A Hierarchical Framework for Multi-Stage Robotic Tasks

- **作者**: Raktim Gautam Goswami, Prashanth Krishnamurthy, Yann LeCun, Farshad Khorrami
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.08775v1)
- **发表日期**: 2026-06-07
- **匹配关键词**: diffusion policy
- **arXiv**: [2606.08775v1](http://arxiv.org/abs/2606.08775v1)
- **📥 PDF**: 已下载至本地 (`2606.08775v1_Unifying_Object-Centric_World_Models_and_Diffusion_Policy_A_Hierarchical_Framework_for_Multi-Stage_R.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉世界模型在学习复杂系统动力学方面展现出巨大潜力。最新研究进展将这些模型作为模型预测控制框架中的转移函数，用于解决各类控制任务。然而在机器人应用中，这些方法仅适用于单阶段任务（如抓取或触碰），难以应对需要复杂序列规划的多阶段任务。本研究提出WorldDP——专为多阶段机器人操作设计的世界模型框架。我们的分层方法利用高层世界模型作为转移函数，在运行时优化可行子目标，随后由低层扩散策略实现这些子目标。为进一步辅助动力学学习与规划，我们引入以物体为中心的表征，将环境实体解耦，从而能够针对每个实体进行序列规划。在多个机器人基准测试中的评估表明，WorldDP始终优于现有基线方法，验证了将世界模型的物理基础规划与扩散策略的高效执行相结合，能够显著提升多阶段任务性能。

---

### 15. Guided Discovery of New Behaviors using Diffusion Policies

- **作者**: Dian Yu, Sebastian Sanokowski, Majid Khadiv
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.08743v1)
- **发表日期**: 2026-06-07
- **匹配关键词**: diffusion policy
- **arXiv**: [2606.08743v1](http://arxiv.org/abs/2606.08743v1)
- **📥 PDF**: 已下载至本地 (`2606.08743v1_Guided_Discovery_of_New_Behaviors_using_Diffusion_Policies.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 扩散模型已成为机器人领域生成式建模的强大工具，其中扩散策略在建模多模态动作轨迹分布方面表现优异。然而，当演示数据有限时，标准采样往往复现主导行为，而忽略有效但罕见的模式，限制了新解决方案的发现。现有方法，如引导方法或将强化学习与扩散模型结合，要么将样本推向不可行区域，要么难以摆脱局部最优，无法系统性地挖掘多样化行为。为应对这些挑战，我们提出了一种结合Feynman-Kac校正器与新型引导势能的框架，该系统性地引导扩散策略样本朝向有前景但未被充分代表的样本。这些轨迹通过基于采样的轨迹优化进行精炼，并重新纳入训练集以重新训练扩散策略。我们的方法有效挖掘并修复了新颖轨迹，实现了多样化且可执行行为的系统性发现。我们在多种操作环境中验证了该框架的有效性，并持续发现了新的行为模式。

---

### 16. ReCoVLA: VLM-Guided Reward Compilation for Failure Recovery in Vision-Language-Action Policies

- **作者**: Haodi Hu, Chung-Ta Huang, Jing Liu, Ye Wang, Kei Suzuki, Matthew Brand, Toshiaki Koike-Akino
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.09630v1)
- **发表日期**: 2026-06-08
- **匹配关键词**: contact-rich manipulation, VLA, vision-language-action
- **arXiv**: [2606.09630v1](http://arxiv.org/abs/2606.09630v1)
- **📥 PDF**: 已下载至本地 (`2606.09630v1_ReCoVLA_VLM-Guided_Reward_Compilation_for_Failure_Recovery_in_Vision-Language-Action_Policies.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）策略为语言条件操控提供了强大的先验知识，但在需要针对性恢复的非标称状态下仍显脆弱。我们提出ReCoVLA——一种基于失败条件的残差恢复框架，该框架保持预训练VLA策略冻结，利用外部视觉语言模型（VLM）推断失败模式与恢复阶段，并从任务相关组件中编译结构化奖励。ReCoVLA并非直接使用VLM生成动作或奖励，而是将其作为语义奖励选择器：它预测恢复描述符和奖励掩码用于仿真残差策略训练，随后将训练好的恢复策略进行零样本仿真到现实迁移。这种设计将高层失败理解与低层修正控制解耦，以支持不同VLA模型。在短时域、长时域及高接触操控任务的实验中，ReCoVLA平均性能优于测试基线。在仿真中，我们的奖励编译器将微调π₀.₅基线的平均成功率从36.7%提升至66.7%。在物理零样本仿真到现实实验中，ReCoVLA以61.7%的成功率取得最佳平均性能。

---

### 17. Back to the Familiar Future: Failure Recovery for VLA Policies via Pre-Imagined Milestone Selection

- **作者**: Suyeon Shin, Juwon Kim, Hyeonbin Park, Hyunseo Kim, Hyundo Lee, Hyung-Sin Kim, Byoung-Tak Zhang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.09258v1)
- **发表日期**: 2026-06-08
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2606.09258v1](http://arxiv.org/abs/2606.09258v1)
- **📥 PDF**: 已下载至本地 (`2606.09258v1_Back_to_the_Familiar_Future_Failure_Recovery_for_VLA_Policies_via_Pre-Imagined_Milestone_Selection.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）策略在操作过程中可能偏离标称轨迹，即使任务在物理上仍然可行。从这些偏离中恢复具有挑战性，因为偏离会将策略推入陌生的状态空间，而直接重新规划往往会破坏动作序列的稳定性。我们提出“回到熟悉的未来”（B2FF），这是一种面向前瞻性VLA的恢复框架，利用未来视觉条件作为恢复接口。在执行前，VLA基于干净的初始观测生成一个由熟悉未来状态组成的里程碑库。在恢复时刻，一个可恢复性感知的选择器从该库中选取一个恢复里程碑，并将其作为固定的视觉目标强制执行。这使得VLA能够将偏离轨迹的观测稳健地映射回熟悉的未来状态。在注入故障的LIBERO基准测试中，在受控的恢复时机与注入故障同步的条件下，B2FF将基线VLA的平均成功率从56.3%提升至74.0%，证明预想的里程碑无需微调底层动作生成器即可引导恢复。

---

## 📌 Poster

*其他相关研究*

---

### 1. iMaC: Translating Actions into Motion and Contact Images for Embodied World Models

- **作者**: Zhenyu Wu, Xiuwei Xu, Yukun Zhou, Yifan Li, Qiuping Deng, Xiaofeng Wang, Zheng Zhu, Bingyao Yu, Ziwei Wang, Jiwen Lu, Haibin Yan
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.09813v1)
- **发表日期**: 2026-06-08
- **匹配关键词**: perception and manipulation
- **arXiv**: [2606.09813v1](http://arxiv.org/abs/2606.09813v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 具身世界模型已成为视觉机器人决策与交互环境模拟的关键范式。然而，传统具身框架依赖低维结构化动作向量（如关节角度与末端执行器位姿），存在表达能力受限、跨本体泛化能力弱、复杂物理交互动态建模不自然等问题。针对上述局限，本文提出iMac（图像即动作控制）——一种将原始视觉图像作为具身世界模型原生动作表征的新型统一控制范式。不同于传统显式运动学动作编码，iMac将连续视觉操控转化为基于图像的动作标记，其天然蕴含空间运动意图、交互几何约束与细微物理动态。我们构建了由图像动作编码器与动态世界预测器组成的双分支具身架构：编码器将目标驱动视觉图像压缩为紧凑动作嵌入，预测器则学习以图像动作为条件的环境转移规则，实现高保真未来状态预测与闭环具身控制。在公开具身操控基准与真实机器人场景中的大量实验表明，iMac在预测精度、任务成功率与跨场景泛化能力上均优于基于向量的动作控制基线。此外，我们的图像动作设计消除了对人工定义动作空间的依赖，实现了异构具身智能体的灵活通用控制。这项工作为具身世界模型提供了创新的视觉-动作视角，为可扩展的机器人感知与操控提供了简洁有效的范式。

---

### 2. SynManDex: Synthesizing Human-like Dexterous Grasps from Synthetic Human Pre-Grasps

- **作者**: Yanming Shao, Zanxin Chen, Wenwei Lin, Mingjie Zhou, Tianxing Chen, Xiaokang Yang, Yichen Chi, Yao Mu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.09798v1)
- **发表日期**: 2026-06-08
- **匹配关键词**: affordance
- **arXiv**: [2606.09798v1](http://arxiv.org/abs/2606.09798v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 人类手-物体交互编码了功能性意图，但直接迁移到机器人手上常因形态、接触和可达性约束而失败。我们提出SynManDex，一种合成流程：将生成的人类预抓取作为感知可行性的提议，并通过机器人原生优化解决最终接触问题。SynManDex采样物体条件化的数字人类预抓取姿态，将其重定向至灵巧机器人手部姿态，在目标实体上优化力闭合接触，并接受通过各步骤检查的轨迹。生成的关健帧不仅支持抓取-举升演示，还能通过VLM智能体设计茶壶倒水、拍照、吹笛子等多种抓取操作任务。实验表明，SynManDex兼具高抓取质量（86.4%抓取稳定性）与4.67/5的人类相似度（93.4%）。在36自由度双臂灵巧机器人平台上，仿真成功率达80.7%，真实机器人成功率达25/30（83.3%）。

---

### 3. AetheRock: An Arm-Worn Robot Teaching System for Force-Guided Vision-Tactile Learning

- **作者**: Hong Li, Yue Xu, Yihan Tang, Yankang Dong, Chenyuan Liu, Chenyang Yu, Xuyang Li, Siyuan Huang, Yujun Shen, Nan Xue, Yong-Lu Li
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.09777v1)
- **发表日期**: 2026-06-08
- **匹配关键词**: contact-rich manipulation
- **arXiv**: [2606.09777v1](http://arxiv.org/abs/2606.09777v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 在接触密集的操作任务中，力觉与触觉感知不可或缺。然而，由于手持或可穿戴设备中触觉传感器与力传感器的装配不兼容，力觉感知的机器人学习面临严峻挑战。为解决这些局限，我们首先提出AetheRock系统，用于夹爪力、视觉与触觉数据采集。该臂戴式设备在指尖集成模块化、易制造的视触觉传感器GelSlim-MiniFab，在人体手指接触区域配备电阻式压力传感器，搭载定制PCB模块，并通过可穿戴套件实现舒适稳定的数据采集。在此基础上，我们提出ForceVT表征学习框架，利用力觉与视觉引导保真度无关的触觉学习，实现任意触觉场景下的鲁棒推理。实际实验表明，AetheRock具备高效的数据采集能力，而ForceVT能有效缓解视触觉传感器在制造与使用不一致时产生的效率低下问题。总体而言，本研究通过创新的硬件设计与算法，缓解了夹爪力-视觉-触觉机器人学习中的局限性。

---

