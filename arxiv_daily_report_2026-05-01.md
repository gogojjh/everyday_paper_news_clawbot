# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-05-01 08:04

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 5/20 篇提供

**🌟 Highlight**: 10 篇 | **📌 Poster**: 10 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. Bi-Level Optimization for Contact and Motion Planning in Rope-Assisted Legged Robots

- **作者**: Ruben Malacarne, Ioannis Tsikelis, Enrico Mingo Hoffman, Michele Focchi
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.26910v1)
- **发表日期**: 2026-04-29
- **匹配关键词**: motion planning
- **arXiv**: [2604.26910v1](http://arxiv.org/abs/2604.26910v1)
- **📥 PDF**: 已下载至本地 (`2604.26910v1_Bi-Level_Optimization_for_Contact_and_Motion_Planning_in_Rope-Assisted_Legged_Robots.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 本文提出了一种用于绳索辅助机器人攀爬垂直表面的运动规划框架。该框架采用双层优化方案，解决了一个混合整数问题：在优化控制输入（即绳索张力与腿部作用力）及落足点的同时，选择可行的地形区域作为着陆点。外层优化采用交叉熵方法求解，内层则基于梯度非线性优化计算动态可行的运动轨迹。该方法的有效性在新型攀爬机器人平台ALPINE上得到验证，并成功应用于多种复杂地形配置场景。

---

### 2. Safe Navigation using Neural Radiance Fields via Reachable Sets

- **作者**: Omanshu Thapliyal, Malarvizhi Sankaranarayanasamy, Ravigopal Vennelakanti
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.26899v1)
- **发表日期**: 2026-04-29
- **匹配关键词**: path planning, neural radiance field, nerf, navigation
- **arXiv**: [2604.26899v1](http://arxiv.org/abs/2604.26899v1)
- **📥 PDF**: 已下载至本地 (`2604.26899v1_Safe_Navigation_using_Neural_Radiance_Fields_via_Reachable_Sets.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 在杂乱环境中安全导航是自主系统面临的重要挑战。当机器人穿越充满障碍物的场景时，需要能够安全地应对不同几何形状的障碍物、目标及自身物体。本研究利用状态空间中机器人实时能力的可达集表示来捕捉安全导航需求，同时采用神经辐射场（NeRF）按需计算、存储和操控障碍物或自身车辆的体积表示。通过约束最优控制方法构建路径规划问题，其中包含线性矩阵不等式约束。我们展示了两种不同场景下存在大量障碍物时的路径规划仿真结果，并通过在相应约束最优控制问题中应用可达集验证了安全导航能力。

---

### 3. STARRY: Spatial-Temporal Action-Centric World Modeling for Robotic Manipulation

- **作者**: Yuxuan Tian, Yurun Jin, Bin Yu, Yukun Shi, Hao Wu, Chi Harold Liu, Kai Chen, Cong Huang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.26848v1)
- **发表日期**: 2026-04-29
- **匹配关键词**: VLA
- **arXiv**: [2604.26848v1](http://arxiv.org/abs/2604.26848v1)
- **📥 PDF**: 已下载至本地 (`2604.26848v1_STARRY_Spatial-Temporal_Action-Centric_World_Modeling_for_Robotic_Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 机器人操作的关键在于对未来的时空交互进行推理，然而现有的VLA策略和世界模型增强策略并未充分建模与动作相关的时空交互结构。我们提出STARRY，一种将时空预测与动作生成对齐的世界模型增强动作生成策略。STARRY联合去噪未来的时空潜在变量和动作序列，并引入几何感知选择性注意力调制，将预测的深度和末端执行器几何结构转化为令牌对齐的权重，用于选择性动作注意力调制。在RoboTwin 2.0上，STARRY在干净和随机设置下分别实现了93.82%和93.30%的平均成功率。真实世界实验进一步将平均成功率从$π_{0.5}$的42.5%提升至70.8%，证明了以动作为中心的时空世界建模对于高时空要求的机器人动作生成的有效性。

---

### 4. Walk With Me: Long-Horizon Social Navigation for Human-Centric Outdoor Assistance

- **作者**: Lingfeng Zhang, Xiaoshuai Hao, Xizhou Bu, Yingbo Tang, Hongsheng Li, Jinghui Lu, Xiu-shen Wei, Jiayi Ma, Yu Liu, Jing Zhang, Hangjun Ye, Xiaojun Liang, Long Chen, Wenbo Ding
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.26839v1)
- **发表日期**: 2026-04-29
- **匹配关键词**: VLA, navigation, vision-language-action, social navigation
- **arXiv**: [2604.26839v1](http://arxiv.org/abs/2604.26839v1)
- **📥 PDF**: 已下载至本地 (`2604.26839v1_Walk_With_Me_Long-Horizon_Social_Navigation_for_Human-Centric_Outdoor_Assistance.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 在开放世界户外环境中辅助人类，要求机器人能够将高层级的自然语言意图转化为安全、长时域且符合社交规范的导航行为。现有基于地图的方法依赖成本高昂的预建高精地图，而基于学习的策略大多局限于室内和短时域场景。为弥合这一差距，我们提出"与我同行"（Walk with Me）——一个无需地图的框架，能够根据高层级人类指令实现长时域社交导航。该框架利用GPS上下文和公共地图API中的轻量级兴趣点候选，实现语义目的地定位与路径点提议。高层级视觉语言模型将抽象指令转化为具体目的地，并规划粗略的路径点序列。在执行过程中，基于观测感知的路由机制会判断低层级视觉-语言-动作策略能否应对当前情境，或是否需要高层级视觉语言模型进行显式安全推理。常规路段由低层级视觉-语言-动作模型执行，而拥挤路口等复杂情境则会触发高层级推理，并在不安全时触发"停-等"行为。通过融合语义意图定位、无地图长时域规划、安全感知推理与低层级动作生成，"与我同行"框架实现了以人为中心的实用化户外社交导航。

---

### 5. Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising

- **作者**: Jun Guo, Qiwei Li, Peiyan Li, Zilong Chen, Nan Sun, Yifei Su, Heyun Wang, Yuan Zhang, Xinghang Li, Huaping Liu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.26694v1)
- **发表日期**: 2026-04-29
- **匹配关键词**: 3D reconstruction, 3d reconstruction
- **arXiv**: [2604.26694v1](http://arxiv.org/abs/2604.26694v1)
- **📥 PDF**: 已下载至本地 (`2604.26694v1_Unified_4D_World_Action_Modeling_from_Video_Priors_with_Asynchronous_Denoising.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出X-WAM——一种统一的4D世界模型，在单一框架内同时实现实时机器人动作执行与高保真4D世界合成（视频+三维重建），解决了先前统一世界模型（如UWM）仅建模二维像素空间、无法平衡动作效率与世界建模质量的关键局限。为利用预训练视频扩散模型的强大视觉先验，X-WAM通过预测多视角RGB-D视频来想象未来世界，并通过轻量级结构适配高效获取空间信息：将预训练扩散变换器的最后几个模块复制到专用深度预测分支中，用于重建未来空间信息。此外，我们提出异步噪声采样（ANS）以联合优化生成质量与动作解码效率。ANS在推理阶段采用专门的异步去噪调度，通过更少的步骤快速解码动作以实现高效实时执行，同时将完整步骤序列用于生成高保真视频。不同于训练阶段完全解耦时间步长，ANS从其联合分布中采样以对齐推理分布。在超过5800小时机器人数据上预训练的X-WAM，在RoboCasa和RoboTwin 2.0基准测试中分别达到79.2%和90.7%的平均成功率，同时生成的高保真4D重建与生成在视觉和几何指标上均超越现有方法。

---

### 6. HiPAN: Hierarchical Posture-Adaptive Navigation for Quadruped Robots in Unstructured 3D Environments

- **作者**: Jeil Jeong, Minsung Yoon, Seokryun Choi, Heechan Shin, Taegeun Yang, Sung-eui Yoon
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.26504v1)
- **发表日期**: 2026-04-29
- **匹配关键词**: navigation, exploration, obstacle avoidance
- **arXiv**: [2604.26504v1](http://arxiv.org/abs/2604.26504v1)
- **📥 PDF**: 已下载至本地 (`2604.26504v1_HiPAN_Hierarchical_Posture-Adaptive_Navigation_for_Quadruped_Robots_in_Unstructured_3D_Environments.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 在非结构化三维环境中引导四足机器人导航面临显著挑战，需要实现目标导向运动、有效探索以逃离局部极小值，以及通过姿态调整穿越狭窄、高度受限的空间。传统方法采用顺序建图-规划流程，但存在累积感知误差和高计算开销的问题，限制了其在资源受限平台上的适用性。为解决这些挑战，我们提出分层姿态自适应导航框架（HiPAN），该框架在部署时直接基于机载深度图像运行。HiPAN采用分层设计：高层策略生成战略性导航指令（平面速度与身体姿态），由低层姿态自适应运动控制器执行。为缓解短视行为并促进长程导航，我们引入路径引导课程学习，逐步将导航范围从反应式避障扩展至战略性导航。仿真实验中，HiPAN相比经典反应式规划器和端到端基线方法实现了更高的导航成功率和路径效率，而真实环境实验进一步验证了其在多样化非结构化三维场景中的适用性。

---

### 7. KinDER: A Physical Reasoning Benchmark for Robot Learning and Planning

- **作者**: Yixuan Huang, Bowen Li, Vaibhav Saxena, Yichao Liang, Utkarsh Aashu Mishra, Liang Ji, Lihan Zha, Jimmy Wu, Nishanth Kumar, Sebastian Scherer, Danfei Xu, Tom Silver ⭐
  - **高亮作者**: Sebastian Scherer
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.25788v1)
- **发表日期**: 2026-04-28
- **匹配关键词**: object manipulation, tool use, mobile manipulator, motion planning
- **arXiv**: [2604.25788v1](http://arxiv.org/abs/2604.25788v1)
- **📥 PDF**: 已下载至本地 (`2604.25788v1_KinDER_A_Physical_Reasoning_Benchmark_for_Robot_Learning_and_Planning.pdf`)
- **🔓 开源**: CODE
- **中文摘要**: 与物理世界交互的机器人系统必须推理其自身形态、环境及当前任务所施加的运动学和动力学约束。我们提出KinDER——面向运动学与动力学具身推理的基准测试，针对机器人学习与规划中的物理推理挑战。KinDER包含25个程序化生成的环境、一个兼容Gymnasium的Python库（含参数化技能与演示），以及标准化评估套件（涵盖13个基线方法，涉及任务与运动规划、模仿学习、强化学习及基于基础模型的方法）。这些环境被设计用于隔离五大核心物理推理挑战：基本空间关系、非抓取式多物体操作、工具使用、组合几何约束及动力学约束，同时排除感知、语言理解及特定应用复杂性的干扰。实验评估表明，现有方法难以解决多数环境，揭示了当前物理推理方法的显著不足。我们还在移动操作平台上进行了真实-仿真-真实实验，以评估仿真与现实物理交互的一致性。KinDER完全开源，旨在推动不同范式间的系统性比较，促进机器人物理推理的发展。网站与代码：https://prpl-group.com/kinder-site/

---

### 8. GS-Playground: A High-Throughput Photorealistic Simulator for Vision-Informed Robot Learning

- **作者**: Yufei Jia, Heng Zhang, Ziheng Zhang, Junzhe Wu, Mingrui Yu, Zifan Wang, Dixuan Jiang, Zheng Li, Chenyu Cao, Zhuoyuan Yu, Xun Yang, Haizhou Ge, Yuchi Zhang, Jiayuan Zhang, Zhenbiao Huang, Tianle Liu, Shenyu Chen, Jiacheng Wang, Bin Xie, Xuran Yao, Xiwa Deng, Guangyu Wang, Jinzhi Zhang, Lei Hao, Zhixing Chen, Yuxiang Chen, Anqi Wang, Hongyun Tian, Yiyi Yan, Zhanxiang Cao, Yizhou Jiang, Hanyang Shao, Yue Li, Lu Shi, Bokui Chen, Wei Sui, Hanqing Cui, Yusen Qin, Ruqi Huang, Lei Han, Tiancai Wang, Guyue Zhou
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.25459v1)
- **发表日期**: 2026-04-28
- **匹配关键词**: gaussian splatting, 3D gaussian splatting, navigation, contact-rich manipulation
- **arXiv**: [2604.25459v1](http://arxiv.org/abs/2604.25459v1)
- **📥 PDF**: 已下载至本地 (`2604.25459v1_GS-Playground_A_High-Throughput_Photorealistic_Simulator_for_Vision-Informed_Robot_Learning.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 具身人工智能研究正经历向视觉中心感知范式的转变。尽管大规模并行模拟器已在基于本体感知的运动控制领域催生突破性进展，但由于大规模逼真渲染带来的高昂计算开销，其在视觉驱动任务中的潜力仍未得到充分开发。此外，可模拟3D资产的创建严重依赖劳动密集型手工建模，而显著的模拟-现实物理差距阻碍了接触密集型操作策略的迁移。为解决这些瓶颈，我们提出GS-Playground——一个旨在加速端到端感知学习的多模态模拟框架。我们开发了新型高性能并行物理引擎，专门设计用于与批量3D高斯泼溅（3DGS）渲染管线集成，确保高保真同步。该系统在640×480分辨率下实现了10^4 FPS的突破性吞吐量，显著降低了大规模视觉强化学习的门槛。同时，我们引入自动化Real2Sim工作流，可重建照片级逼真、物理一致且内存高效的环境，简化复杂可模拟场景的生成流程。在运动控制、导航和操作任务上的大量实验表明，GS-Playground有效弥合了不同具身任务中的感知与物理差距。项目主页：https://gsplayground.github.io。

---

### 9. Three-Step Nav: A Hierarchical Global-Local Planner for Zero-Shot Vision-and-Language Navigation

- **作者**: Wanrong Zheng, Yunhao Ge, Laurent Itti
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.26946v1)
- **发表日期**: 2026-04-29
- **匹配关键词**: vision-and-language navigation, navigation, VLN
- **arXiv**: [2604.26946v1](http://arxiv.org/abs/2604.26946v1)
- **📥 PDF**: 已下载至本地 (`2604.26946v1_Three-Step_Nav_A_Hierarchical_Global-Local_Planner_for_Zero-Shot_Vision-and-Language_Navigation.pdf`)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/ZoeyZheng0/3-step-Nav.
- **中文摘要**: 基于多模态大语言模型（MLLMs）的视觉导航技术已在未知环境探索中取得突破性进展。这类模型通过在每个时间步评估当前视角与任务目标的匹配度，能够规划出一系列运动序列。然而，当前由MLLMs驱动的零样本视觉语言导航（VLN）智能体仍存在偏离路线、过早停止及整体成功率偏低等问题。为此，我们提出三步导航法（Three-Step Nav），通过三视角协议应对上述缺陷：首先，"向前看"提取全局地标并勾勒粗略规划；其次，"看当下"将当前视觉观测与下一子目标对齐，实现细粒度引导；最后，"回头看"在停止前对整个轨迹进行审计以修正累积偏差。该方法无需梯度更新或任务特定微调，仅需极低开销即可嵌入现有VLN流程。在R2R-CE和RxR-CE数据集上，三步导航法实现了零样本场景下的最优性能。代码已开源：https://github.com/ZoeyZheng0/3-step-Nav。

---

### 10. Color-Encoded Illumination for High-Speed Volumetric Scene Reconstruction

- **作者**: David Novikov, Eilon Vaknin, Narek Tumanyan, Mark Sheinin
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.26920v1)
- **发表日期**: 2026-04-29
- **匹配关键词**: gaussian splatting
- **arXiv**: [2604.26920v1](http://arxiv.org/abs/2604.26920v1)
- **📥 PDF**: 已下载至本地 (`2604.26920v1_Color-Encoded_Illumination_for_High-Speed_Volumetric_Scene_Reconstruction.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 近年来，从二维图像中捕捉并渲染三维动态场景的任务日益受到关注。然而，传统相机受限于30-60帧/秒的带宽，使得这些方法仅适用于静态或缓慢变化的场景。尽管在通用场景中突破带宽限制存在困难，但近年来涌现了大量计算成像方法，能够利用传统相机为特定应用（如运动捕捉和粒子图像测速）生成高速视频。然而，这些方法大多需要改造相机光学系统或添加机械运动部件，且局限于单视角高速捕捉。因此，它们难以直接用于获取快速场景运动的三维表征。本文提出一种新颖方法，仅使用未经改造的低速相机即可捕捉并重建高速场景的体积表征。我们无需修改单个相机的硬件或光学系统，而是通过快速连续的颜色编码序列照亮场景，从而编码高速场景动态。这种方法实现了场景的多视角同步捕捉，高速时间信息被编码在捕获图像的空间强度与颜色变化中。为构建动态场景的高速体积表征，我们开发了一种基于动态高斯泼溅的新方法，从图像中解码时间信息。通过多相机成像系统在模拟场景和真实实验中的评估，我们首次实现了高速场景体积重建。

---

## 📌 Poster

*其他相关研究*

---

### 1. Stochastic Entanglement of Deterministic Origami Tentacles For Universal Robotic Gripping

- **作者**: Alec Boron, Bokun Zheng, Ziyang Zhou, Noel Naughton, Suyi Li
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.26897v1)
- **发表日期**: 2026-04-29
- **匹配关键词**: HRI, object manipulation
- **arXiv**: [2604.26897v1](http://arxiv.org/abs/2604.26897v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 受折纸启发的机器人夹爪因其紧凑的体积和机械灵活性，在物体操控任务中展现出巨大潜力。然而，在动态工作环境中稳健抓取随机形状的物体，往往需要以增加驱动通道和控制复杂度为代价。本文提出一种肌腱驱动的折纸触手夹爪，通过协同局部确定性变形编程与全局随机缠绕机制，实现通用物体抓取。每个折纸触手由薄聚酯薄膜切割制成，其设计包含：用于引导驱动肌腱的精确孔位、控制变形的折痕结构，以及锥形轮廓。通过定制这些设计特征，可预设收缩、弯曲和扭转变形模式，最终仅通过单根肌腱牵引即可实现确定性卷曲。当多个卷曲触手紧密排列时，会产生随机缠绕现象，使触手能够编织、打结并抓取任意形状的物体。我们通过将折纸力学与Cosserat杆理论相结合建立仿真模型，关联折纸设计、肌腱变形及其集体抓取性能。随后通过实验验证了这些卷曲缠绕式折纸触手在重力环境及水下抓取物体的能力，并测试了收纳释放部署机构以模拟在轨抓取场景。总体而言，这种兼具趣味性的折纸触手夹爪为以简洁设计和驱动方式实现稳健物体抓取提供了新策略。

---

### 2. Persona-Based Process Design for Assistive Human-Robot Workplaces for Persons with Disabilities

- **作者**: Nils Mandischer, Daria Eckert and, Lars Mikelsons
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.26527v1)
- **发表日期**: 2026-04-29
- **匹配关键词**: human-robot interaction
- **arXiv**: [2604.26527v1](http://arxiv.org/abs/2604.26527v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 人机交互正逐渐成为将残障人士融入工作场所的重要范式。尽管这类系统能够帮助个体参与工作，但其设计大多具有个性化特征，阻碍了在个体用户之外的广泛推广。通用设计范式作为包容性设计的核心支柱，强调系统对所有用户的可及性。要将通用设计融入人机协作工作场所的流程设计，通常需要具备专业知识，而这往往难以获得。为简化人机协作工作场所的流程设计，我们提出了一种基于角色模型的设计方法。首先，将劳动力中普遍存在或与特定流程高度相关的典型障碍特征抽象为残障角色模型。工作流程被细分为连续的操作步骤。针对每个操作步骤和角色模型，通过设计思维方法制定达成操作目标的具体策略。最终形成的操作方案按机器人辅助程度（即机器人参与度）排序，并采用行为树进行实现。由此，工作场所的宏观行为可在线适配不同角色模型。我们通过一个包含七种残障角色模型的协作纸箱折叠流程验证了该方法。基于角色模型的流程设计展现出显著优势：既能生成更全面的流程策略，又能实现符合通用设计理念的自适应行为。

---

### 3. Variational Neural Belief Parameterizations for Robust Dexterous Grasping under Multimodal Uncertainty

- **作者**: Clinton Enwerem, Shreya Kalyanaraman, John S. Baras, Calin Belta
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.25897v1)
- **发表日期**: 2026-04-28
- **匹配关键词**: dexterous grasping
- **arXiv**: [2604.25897v1](http://arxiv.org/abs/2604.25897v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 接触变异性、感知不确定性和外部扰动使得抓取执行具有随机性。期望质量目标忽略了尾部结果，往往选择在不利接触情况下失败的抓取方案。风险敏感的POMDP模型可应对此类失效模式，但多数方法采用粒子滤波置信度，该方式扩展性差、阻碍基于梯度的优化，且通过高方差近似估计条件风险价值（CVaR）。我们转而将抓取获取建模为对潜在接触参数和物体位姿的变分推断，利用可微高斯混合分布表示置信度。通过Gumbel-Softmax分量选择与位置-尺度重参数化，将样本表示为置信度参数的平滑函数，从而通过可微CVaR替代函数实现路径梯度，直接优化尾部鲁棒性。仿真实验中，我们的变分神经置信度在接触参数不确定性和外力扰动条件下提升了鲁棒抓取成功率，同时将规划时间较粒子滤波模型预测控制降低约一个数量级。在多指串联机械臂平台上，我们以高斯基线为对照，验证了物体位姿不确定性下的抓取-提升成功率。两种方法在测试扰动下均能成功，但我们的控制器以更少步数和更短实际时间完成任务，同时获得更高的触觉抓取质量代理指标。此外，学习得到的置信度能更精确地校准风险，在测试仿真场景中平均绝对校准误差始终低于0.14，而交叉熵方法规划器的该指标为0.58。

---

### 4. SlicerRoboTMS: An Open-Source 3D Slicer Extension for Robot-Assisted Transcranial Magnetic Stimulation

- **作者**: Wenzhi Bai, Yituo Guo, Bhaskar Basu, Andrew Weightman, Zhenhong Li
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.25661v1)
- **发表日期**: 2026-04-28
- **匹配关键词**: navigation
- **arXiv**: [2604.25661v1](http://arxiv.org/abs/2604.25661v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: GITHUB, CODE
  - 链接：https://github.com/OpenRoboTMS/SlicerRoboTMS.
- **中文摘要**: 机器人辅助经颅磁刺激（Robo-TMS）是一种基于图像引导的机器人干预技术，可提升传统经颅磁刺激（TMS）的精准度与可重复性。TMS作为临床治疗和神经科学研究中广泛使用的非侵入性脑刺激手段，其技术发展因需整合医学影像、计算机视觉与机器人学等多学科专业知识而面临挑战。本文提出SlicerRoboTMS——一个开源3D Slicer扩展模块，为Robo-TMS研究提供统一交互基础设施。该扩展利用3D Slicer的医学影像计算与可视化能力，支持基于磁共振成像（MRI）的神经导航，并通过标准化通信协议与可配置系统描述实现与机器人系统的对接。本文通过典型集成案例，展示SlicerRoboTMS如何融入代表性Robo-TMS工作流程。该扩展旨在适配多样化硬件配置并支持快速原型开发，有效降低技术准入门槛，促进Robo-TMS研究的可重复性与可扩展性。扩展代码已开源至https://github.com/OpenRoboTMS/SlicerRoboTMS。

---

### 5. Bridging the Indoor-Outdoor Gap: Cross-Technology Ranging for Seamless Robot Navigation

- **作者**: Paul Schwarzbach
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.25541v1)
- **发表日期**: 2026-04-28
- **匹配关键词**: robot navigation, navigation
- **arXiv**: [2604.25541v1](http://arxiv.org/abs/2604.25541v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: CODE
- **中文摘要**: 在户外与室内环境间移动的移动机器人在实现连续定位方面仍面临挑战。基于卫星与地面测距技术各自在所属领域表现良好，但将二者在原始测量层面进行融合的研究尚不充分，而建筑边界区域恰恰是两类技术性能同时下降的薄弱环节。本文报告了HYMN数据集的初步观测结果，该数据集在工业场景中实现了GNSS、超宽带（UWB）、WiFi精细时间测量（FTM）及低功耗蓝牙（BLE）的原始测量数据与毫米级地面实况的时间同步。研究刻画了各区域的测量可用性及测距残差特征，发现两类技术具有互补性，而室内外过渡区域正是其性能短板重叠之处。该数据集已公开共享。

---

### 6. COMPASS: COmpact Multi-channel Prior-map And Scene Signature for Floor-Plan-Based Visual Localization

- **作者**: Muhammad Shaheer, Miguel Fernandez-Cortizas, Asier Bikandi-Noya, Holger Voos, Jose Luis Sanchez-Lopez
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.25388v1)
- **发表日期**: 2026-04-28
- **匹配关键词**: place recognition
- **arXiv**: [2604.25388v1](http://arxiv.org/abs/2604.25388v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 建筑平面图是广泛可用的先验信息，不仅包含环境的几何结构，还包含语义信息，然而现有的定位方法大多忽略了这些语义信息。为解决这一问题，我们提出了COMPASS算法，该算法利用平面图中的几何和语义先验来估计配备双鱼眼摄像头的机器人的位姿。受基于激光雷达的地点识别中的扫描上下文描述符启发，我们设计了一种多通道径向描述符，用于编码位置周围的几何布局。从平面图出发，在360个方位角区间内投射射线，并将结果编码为五个通道：归一化距离、结构命中类型（墙壁、窗户或开口）、距离梯度、逆距离和局部距离方差。在图像方面，通过检测鱼眼图像中的结构元素来填充相同的描述符结构。作为迈向完整跨模态匹配的第一步，我们提出了一种针对鱼眼图像的窗户检测算法，该算法使用线段检测器通过垂直边缘聚类和亮度验证来识别窗框。检测到的窗户通过鱼眼相机模型投影到方位角方向，生成视觉描述符的命中类型通道。作为概念验证，我们从Hilti-Trimble SLAM挑战赛2026数据集的单个已知位姿生成两种描述符，并证明从每个摄像头第一帧图像中提取的墙壁-窗户模式与平面图描述符高度匹配，验证了跨模态结构匹配的可行性。

---

### 7. ANCHOR: A Physically Grounded Closed-Loop Framework for Robust Home-Service Mobile Manipulation

- **作者**: Jinhao Jiang, Shengyu Fang, Sibo Zuo, Yujie Tang, Yirui Li
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.25323v1)
- **发表日期**: 2026-04-28
- **匹配关键词**: mobile manipulation, navigation
- **arXiv**: [2604.25323v1](http://arxiv.org/abs/2604.25323v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://anchor9178.github.io/ANCHOR/
- **中文摘要**: 开放词汇移动操作的最新进展已将机器人带入真实的家居环境。在此类场景中，面对开放集物体引用和频繁干扰，可靠的长期任务执行变得至关重要。然而，许多失败依然存在。这些失败并非源于语义理解错误，而是由符号化规划与动态变化的物理世界之间的不一致性导致，具体表现为三个反复出现的局限：（i）现有系统常依赖预扫描的语义地图，但场景变化和干扰后该地图会变得不一致；（ii）系统选择导航终点时未考虑下游操作可行性，导致"抵达但无法操作"问题；（iii）系统通过无差别的全局重规划处理异常，往往无法有效控制局部错误。为解决这种执行不一致性，我们提出ANCHOR——一种物理锚定的闭环框架，能在执行过程中将符号推理与可验证的物理状态对齐。ANCHOR整合了三种机制：（i）物理锚定任务规划，将符号谓词绑定到可观测的几何锚点，并在每次动作后重新验证；（ii）可操作性感知的基座对齐，确保导航终点满足运动学可达性和局部碰撞可行性；（iii）最小责任层分层恢复，在感知层、基座-机械臂协调层和执行层定位故障，防止级联重试。在60次未见环境中的真实机器人试验中，ANCHOR将任务成功率从53.3%提升至71.7%，并在扰动下实现71.4%的恢复率，证明显式物理锚定和结构化故障遏制对鲁棒移动操作至关重要。项目页面：https://anchor9178.github.io/ANCHOR/。

---

### 8. Optimal UGV-UAV Cooperative Partitioning and Inspection of Shortest Paths

- **作者**: Ninh Nguyen, Srinivas Akella
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.25284v1)
- **发表日期**: 2026-04-28
- **匹配关键词**: path planning
- **arXiv**: [2604.25284v1](http://arxiv.org/abs/2604.25284v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 我们研究了在存在未知道路阻塞的环境下，由无人机辅助的地面无人车辆协同最短路径规划问题——这些阻塞仅在机器人抵达受损点时才会被发现。该问题推广了经典的加拿大旅行者问题（CTP），后者假设仅有一辆地面车辆，且所有邻接边的通行状态在到达顶点时才会揭示。首先，我们分析了起点与终点由k条不相交路径连接的情况，并证明单辆UGV的最坏情况竞争比ρ为2k-1。在无人机辅助下，且假设无人机初始通行与空载成本可忽略时，该比值优化为ρ= 2(v_G/(v_A+v_G))k - 1，其中v_G与v_A分别表示UGV与无人机的速度。针对一般图结构及不可忽略的无人机初始通行与空载成本，我们提出了一种最优路径分段策略：由UGV负责路径前缀段探查，无人机负责路径后缀段探查，并证明了该无人机探查策略在一般图上的最优性。我们基于全球50个人口最多城市的道路网络进行随机阻塞实验评估，结果表明所提方法可将UGV通行时间降低高达30%。

---

### 9. HANDFUL: Sequential Grasp-Conditioned Dexterous Manipulation with Resource Awareness

- **作者**: Ethan Foong, Yunshuang Li, Hao Jiang, Gaurav S. Sukhatme, Daniel Seita
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.25126v1)
- **发表日期**: 2026-04-28
- **匹配关键词**: grasp planning, exploration
- **arXiv**: [2604.25126v1](http://arxiv.org/abs/2604.25126v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 灵巧机器人手为多功能操作提供了丰富的机会，机器人需按顺序执行多种技能，同时保持对已抓取物体的控制。现有灵巧操作研究大多聚焦于单物体、单技能任务。与此不同，我们的核心洞察在于：许多顺序任务需要资源感知型抓取，即保留手指以备后续动作。本文研究顺序抓取条件灵巧操作——机器人先抓取物体，随后在保持初始抓取的同时执行第二个不同的操作子任务。我们提出HANDFUL学习框架，将手指使用建模为有限资源，并通过手指级接触奖励鼓励探索资源感知型抓取。随后通过基于课程策略学习为下游任务选择这些抓取方式。我们进一步提出HANDFUL-Bench仿真基准，在共享抓取条件设置下引入包含推、拉、按等多种第二子任务目标的顺序灵巧操作任务。大量仿真结果表明，与在尝试第二子任务前贪婪优化初始抓取的基线方法相比，优先考虑资源感知型抓取能提升第二子任务的成功率与鲁棒性。我们还在真实灵巧LEAP手上验证了该方法。本研究确立了资源感知型抓取规划作为多功能灵巧操作的关键原则。补充材料见网站：https://handful-dex.github.io。

---

### 10. Breaking the Rigid Prior: Towards Articulated 3D Anomaly Detection

- **作者**: Jinye Gan, Bozhong Zheng, Xiaohao Xu, Junye Ren, Zixuan Zhang, Na Ni, Yingna Wu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.26868v1)
- **发表日期**: 2026-04-29
- **匹配关键词**: articulated object
- **arXiv**: [2604.26868v1](http://arxiv.org/abs/2604.26868v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 现有三维异常检测方法建立在刚性先验基础上：正常几何形状具有姿态不变性，可通过配准或对齐进行规范化。这一先验不适用于具有铰链或滑动关节的铰接物体——其有效姿态变化会引发结构化几何变形，无法简化为单一规范模板，导致姿态引发的变形被误判为异常，而真实结构缺陷却被掩盖。目前尚无基准数据集解决该问题。我们提出ArtiAD——首个面向铰接三维异常检测的大规模基准数据集，包含39个物体类别的15,229个点云，涵盖密集关节角度变化和六种结构异常类型。每个样本均标注关节构型与部件级运动标签，可显式分离姿态引发的几何变形与结构缺陷。ArtiAD还提供可见/未见关节构型划分，以评估对新型关节构型的插值与外推能力。我们提出形状-姿态感知符号距离场（SPA-SDF）基线方法，用连续姿态条件隐式场替代刚性先验，将其分解为与关节无关的结构先验和傅里叶编码的关节嵌入。推理时通过最小化重建能量恢复关节状态，并基于点云与学习流形的偏差识别异常。SPA-SDF在可见构型上达到0.884的物体级AUROC，在未见构型上达到0.874，显著优于所有基于刚性先验的基线方法。代码与基准数据集将公开发布以促进后续研究。

---

