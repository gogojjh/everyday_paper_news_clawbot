# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-03-13 08:04

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 3/20 篇提供

**🌟 Highlight**: 20 篇 | **📌 Poster**: 0 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. PPGuide: Steering Diffusion Policies with Performance Predictive Guidance

- **作者**: Zixing Wang, Devesh K. Jha, Ahmed H. Qureshi, Diego Romeres
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.10980v1)
- **发表日期**: 2026-03-11
- **匹配关键词**: diffusion policy
- **arXiv**: [2603.10980v1](http://arxiv.org/abs/2603.10980v1)
- **📥 PDF**: 已下载至本地 (`2603.10980v1_PPGuide_Steering_Diffusion_Policies_with_Performance_Predictive_Guidance.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 扩散策略已被证明在学习机器人操作的复杂多模态行为方面非常高效。然而，生成动作序列中的误差会随时间累积，可能导致任务失败。现有方法通过增加专家示范数据或学习预测性世界模型来缓解这一问题，但这些方案可能带来较高的计算成本。我们提出性能预测引导框架，这是一种基于分类器的轻量级框架，能够在推理阶段引导预训练的扩散策略避开失败模式。该框架采用新颖的自监督流程：通过基于注意力的多示例学习技术，自动识别策略运行过程中哪些观测-动作片段与任务成败相关，并利用这些自标注数据训练性能预测器。在推理阶段，该预测器通过实时梯度引导策略生成更稳健的动作序列。我们在Robomimic和MimicGen基准测试的多样化任务中验证了所提框架的有效性，实验结果表明该方法能持续提升任务执行性能。

---

### 2. RL-Augmented MPC for Non-Gaited Legged and Hybrid Locomotion

- **作者**: Andrea Patrizi, Carlo Rizzardo, Arturo Laurenzi, Francesco Ruscelli, Luca Rossini, Nikos G. Tsagarakis
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.10878v1)
- **发表日期**: 2026-03-11
- **匹配关键词**: navigation
- **arXiv**: [2603.10878v1](http://arxiv.org/abs/2603.10878v1)
- **📥 PDF**: 已下载至本地 (`2603.10878v1_RL-Augmented_MPC_for_Non-Gaited_Legged_and_Hybrid_Locomotion.pdf`)
- **🔓 开源**: GITHUB, CODE
  - 链接：https://github.com/AndrePatri/AugMPC.
- **中文摘要**: 我们提出了一种显式接触的分层架构，将强化学习（RL）与模型预测控制（MPC）相结合，其中高层RL智能体向低层运动MPC提供步态与导航指令。通过在仿真环境中进行试错学习非周期步态，该架构将接触时序的组合负担从MPC中剥离。研究表明，仅需最小化的奖励设置与有限调参即可获得有效策略。我们在仿真环境中验证了该架构在50公斤至120公斤不同机器人平台及多种MPC实现中的适用性，观察到在平坦地形腿式与混合式运动中非周期步态及时序适应的涌现，并进一步证明了其在非平坦地形中的扩展能力。所有平台均实现了无需域随机化的零样本仿真到仿真迁移，并在我们120公斤轮腿式人形机器人Centauro上进一步展示了无需域随机化的零样本仿真到现实迁移。相关软件框架与评估结果已公开于https://github.com/AndrePatri/AugMPC。

---

### 3. FG-CLTP: Fine-Grained Contrastive Language Tactile Pretraining for Robotic Manipulation

- **作者**: Wenxuan Ma, Chaofan Zhang, Yinghao Cai, Guocai Yao, Shaowei Cui, Shuo Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.10871v1)
- **发表日期**: 2026-03-11
- **匹配关键词**: vision-language-action, contact-rich manipulation, VLA
- **arXiv**: [2603.10871v1](http://arxiv.org/abs/2603.10871v1)
- **📥 PDF**: 已下载至本地 (`2603.10871v1_FG-CLTP_Fine-Grained_Contrastive_Language_Tactile_Pretraining_for_Robotic_Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 将触觉感知整合到视觉-语言-动作（VLA）模型中的最新进展已展现出对机器人感知能力的变革潜力。然而，现有的触觉表征主要依赖定性描述符（如纹理），忽略了力的大小、接触几何形态和主轴方向等定量接触状态，而这些对于精细操作至关重要。为弥补这一空白，我们提出了FG-CLTP——一种细粒度对比语言触觉预训练框架。我们首先构建了一个包含超过10万个触觉三维点云-语言对的新型数据集，该数据集从传感器视角明确捕捉了多维接触状态。随后，我们采用离散化数值标记机制实现定量-语义对齐，将显式物理度量有效注入多模态特征空间。所提出的FG-CLTP模型在分类任务中达到95.9%的准确率，相较于现有最优方法将回归误差（MAE）降低了52.6%。此外，三维点云表征的整合建立了传感器无关的基础框架，其仿真到现实的差距仅为3.5%。基于这种细粒度表征，我们开发了由流匹配策略驱动的三维触觉-语言-动作（3D-TLA）架构，以实现多模态推理与控制。大量实验表明，我们的框架在接触密集型操作任务中显著优于现有基线方法，为触觉-语言-动作模型提供了稳健且可泛化的基础。

---

### 4. FutureVLA: Joint Visuomotor Prediction for Vision-Language-Action Model

- **作者**: Xiaoxu Xu, Hao Li, Jinhui Ye, Yilun Chen, Jia Zeng, Xinyi Chen, Linning Xu, Dahua Lin, Weixin Li, Jiangmiao Pang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.10712v1)
- **发表日期**: 2026-03-11
- **匹配关键词**: vision-language-action, vision-language-action model, VLA
- **arXiv**: [2603.10712v1](http://arxiv.org/abs/2603.10712v1)
- **📥 PDF**: 已下载至本地 (`2603.10712v1_FutureVLA_Joint_Visuomotor_Prediction_for_Vision-Language-Action_Model.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 预测性前瞻对智能具身代理至关重要。由于机器人的运动执行本质上受其环境几何视觉感知的约束，有效预测未来需要捕捉这种紧密耦合的视觉运动交互。尽管近期视觉-语言-动作模型尝试融入未来指导，却难以实现这种联合建模。现有显式方法将模型容量分散至任务无关的视觉细节，而依赖稀疏帧对的隐式方法则破坏了时间连续性。这些方法因过度依赖视觉重建而受视觉主导，将静态场景上下文与动态动作意图相互纠缠。我们认为有效的视觉运动联合预测建模需要同时满足时间连续性及视觉条件监督解耦。为此，我们提出FutureVLA模型，其创新性在于构建了联合视觉运动预测架构。该模型通过先解耦视觉与运动信息，再联合编码广义物理先验，旨在提取联合视觉运动嵌入表示。具体而言，在预训练阶段，我们利用异构操作数据集并引入联合视觉运动门控机制，从结构上分离视觉状态保持与时序动作建模。该机制使运动流能专注于连续物理动态，同时显式查询视觉标记以获取环境约束，从而生成高度可泛化的联合视觉运动嵌入。随后在后训练阶段，我们采用潜在嵌入对齐策略，使多样化下游视觉-语言-动作模型无需修改推理架构即可内化这些时序先验。大量实验表明，FutureVLA能持续提升各类视觉-语言-动作框架的性能。

---

### 5. OnFly: Onboard Zero-Shot Aerial Vision-Language Navigation toward Safety and Efficiency

- **作者**: Guiyong Zheng, Yueting Ban, Mingjie Zhang, Juepeng Zheng, Boyu Zhou
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.10682v1)
- **发表日期**: 2026-03-11
- **匹配关键词**: navigation, VLN
- **arXiv**: [2603.10682v1](http://arxiv.org/abs/2603.10682v1)
- **📥 PDF**: 已下载至本地 (`2603.10682v1_OnFly_Onboard_Zero-Shot_Aerial_Vision-Language_Navigation_toward_Safety_and_Efficiency.pdf`)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/Robotics-STAR-Lab/OnFly
- **中文摘要**: 空中视觉语言导航（AVLN）使无人机能够在复杂三维环境中遵循自然语言指令飞行。然而，现有零样本AVLN方法常面临单流视觉语言模型决策不稳定、长时程进度监测不可靠，以及安全性与效率难以兼顾的问题。本文提出OnFly——一个完全机载、实时的零样本AVLN框架。OnFly采用共享感知的双智能体架构，将高频目标生成与低频进度监测解耦，从而稳定决策过程。该框架进一步采用混合关键帧-近期帧记忆机制，在保持KV缓存前缀稳定性的同时保留全局轨迹上下文，实现具备终止与恢复信号的可靠长时程监测。此外，语义几何验证器利用VLM特征与深度线索，对VLM预测目标进行指令一致性与几何安全性优化；而滚动时域规划器在几何安全约束下生成优化的无碰撞轨迹，同步提升安全性与效率。仿真实验中，OnFly将任务成功率从现有最强基线的26.4%提升至67.8%，完全机载的实机飞行验证了其实时部署的可行性。代码将在https://github.com/Robotics-STAR-Lab/OnFly发布。

---

### 6. Cybo-Waiter: A Physical Agentic Framework for Humanoid Whole-Body Locomotion-Manipulation

- **作者**: Peng Ren, Haoyang Ge, Chuan Qi, Cong Huang, Hong Li, Jiang Zhao, Pei Chi, Kai Chen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.10675v1)
- **发表日期**: 2026-03-11
- **匹配关键词**: locomotion and manipulation, whole-body manipulation
- **arXiv**: [2603.10675v1](http://arxiv.org/abs/2603.10675v1)
- **📥 PDF**: 已下载至本地 (`2603.10675v1_Cybo-Waiter_A_Physical_Agentic_Framework_for_Humanoid_Whole-Body_Locomotion-Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 随着机器人在人类环境中执行开放式自然语言指令的需求日益增长，这要求其在部分可观测条件下实现可靠的长时程任务执行。对人形机器人而言，这一挑战尤为严峻，因为其移动与操作能力通过姿态、可达性与平衡约束紧密耦合。本文提出一种人形机器人智能体框架，该框架将视觉语言模型生成的规划转化为可验证的任务程序，并通过多目标三维几何监督实现闭环控制。视觉语言模型规划器将每条指令编译为具有明确谓词前置条件与成功条件的类型化JSON子任务序列。借助SAM3与RGB-D技术，我们在三维空间中定位所有任务相关实体，估算物体质心与空间范围，并在稳定坐标系下评估谓词以获取条件级诊断信息。监督器利用这些诊断结果验证子任务完成情况，并为任务推进与重规划提供条件级反馈。通过协调人形机器人的移动与全身操作能力，我们在满足可达性与平衡约束的前提下选择可行的运动基元来执行每个子任务。在桌面操作及长时程人形机器人移动操作任务中的实验表明，多目标三维定位、时序稳定性与故障恢复驱动的重规划机制显著提升了系统鲁棒性。

---

### 7. Splat2Real: Novel-view Scaling for Physical AI with 3D Gaussian Splatting

- **作者**: Hansol Lim, Jongseong Brad Choi
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.10638v1)
- **发表日期**: 2026-03-11
- **匹配关键词**: 3D gaussian splatting, gaussian splatting
- **arXiv**: [2603.10638v1](http://arxiv.org/abs/2603.10638v1)
- **📥 PDF**: 已下载至本地 (`2603.10638v1_Splat2Real_Novel-view_Scaling_for_Physical_AI_with_3D_Gaussian_Splatting.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 物理人工智能面临训练与部署间的视角偏移问题，单目RGB到3D感知的新视角鲁棒性至关重要。我们将Real2Render2Real单目深度预训练构建为数字孪生先知驱动的模仿学习式监督：学生深度网络通过模仿从场景网格渲染的专家度量深度/可见性进行学习，而3D高斯泼溅技术提供可扩展的新视角观测。我们提出以新视角扩展为核心的Splat2Real方法：性能提升更取决于新增视角的质量而非原始视角数量。我们引入CN-Coverage课程策略，通过几何增益与外推惩罚贪婪选择视角，并为低可靠性教师模型设置质量感知防护机制。在20组TUM RGB-D序列的步进匹配预算实验中（新增渲染视角N=0至2000，其中独特视角≤500，更大预算时采用重采样），简单扩展策略表现不稳定；相较于Robot/Coverage策略，CN-Coverage能缓解最差情况下的性能衰退，而门控CN-Coverage方案在中高预算区间展现出最强的稳定性与最低的高新颖性尾端误差。下游控制代理实验结果通过视角偏移下安全性与进度的权衡变化，为具身相关性提供了实证依据。

---

### 8. DepthCache: Depth-Guided Training-Free Visual Token Merging for Vision-Language-Action Model Inference

- **作者**: Yuquan Li, Lianjie Ma, Han Ding, Lijun Zhu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.10469v1)
- **发表日期**: 2026-03-11
- **匹配关键词**: vision-language-action, vision-language-action model, VLA
- **arXiv**: [2603.10469v1](http://arxiv.org/abs/2603.10469v1)
- **📥 PDF**: 已下载至本地 (`2603.10469v1_DepthCache_Depth-Guided_Training-Free_Visual_Token_Merging_for_Vision-Language-Action_Model_Inferenc.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型能够实现通用机器人操控，但存在推理延迟较高的问题。这一瓶颈源于大型语言主干网络需要处理海量视觉标记。现有方法通常对标记进行均匀剪枝或合并，这会损害机器人控制所需的关键空间推理能力。本文提出DepthCache——一种无需训练即可利用深度信息作为视觉标记压缩结构先验的框架。该框架将观测数据按深度划分为不同区域，并采用空间差异化的合并比例，在压缩远处背景的同时保留近场工作空间细节。为利用时间冗余性，DepthCache将合并过程分散至连续帧间，在降低单步计算量的同时保持表征一致性。通过运动自适应流水线进一步根据末端执行器动态优化辅助视角压缩。该框架无需修改模型结构，可泛化至多种VLA架构。在LIBERO基准测试中，DepthCache在三种VLA模型（pi_0.5、OpenVLA、GR00T）上实现最高1.28倍推理加速，平均成功率下降不足1%，而相同压缩率下的剪枝与合并基线方法性能下降达4-24%。在实体机械臂上的真实场景实验表明，DepthCache能在延迟敏感场景中实现更高任务吞吐量与更灵敏的闭环控制响应。

---

### 9. DiT4DiT: Jointly Modeling Video Dynamics and Actions for Generalizable Robot Control

- **作者**: Teli Ma, Jia Zheng, Zifan Wang, Chuili Jiang, Andy Cui, Junwei Liang, Shuo Yang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.10448v1)
- **发表日期**: 2026-03-11
- **匹配关键词**: vision-language-action, action diffusion, VLA
- **arXiv**: [2603.10448v1](http://arxiv.org/abs/2603.10448v1)
- **📥 PDF**: 已下载至本地 (`2603.10448v1_DiT4DiT_Jointly_Modeling_Video_Dynamics_and_Actions_for_Generalizable_Robot_Control.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型已成为机器人学习领域备受关注的研究范式，但其表征能力仍主要源自静态图文预训练，物理动态特性需从相对有限的动作数据中学习。相比之下，生成式视频模型能够编码丰富的时空结构与隐式物理规律，为机器人操作任务提供了极具潜力的基础框架，然而现有研究尚未充分挖掘其潜力。为弥补这一空白，我们提出DiT4DiT——一种端到端的视频-动作模型，通过统一级联框架将视频扩散变换器与动作扩散变换器深度融合。该模型摒弃传统依赖重构未来帧的方法，转而从视频生成过程中提取去噪中间特征，将其作为具有时序锚定特性的条件信号用于动作预测。我们进一步提出具有解耦时间步与噪声尺度的双重流匹配目标，实现视频预测、隐状态提取与动作推理的协同联合训练。在仿真与真实场景基准测试中，DiT4DiT取得业界领先性能：在LIBERO基准达到98.6%的平均成功率，在RoboCasa GR1基准实现50.8%的成功率，且训练数据消耗显著降低。在Unitree G1机器人平台上，该系统同样展现出卓越的实际操作能力与强大的零样本泛化性能。值得注意的是，DiT4DiT将样本效率提升超过10倍，收敛速度加快达7倍，有力验证了视频生成可作为机器人策略学习的有效扩展代理。相关代码与模型已发布于https://dit4dit.github.io/。

---

### 10. SignSparK: Efficient Multilingual Sign Language Production via Sparse Keyframe Learning

- **作者**: Jianhe Low, Alexandre Symeonidis-Herzig, Maksym Ivashechkin, Ozge Mercanoglu Sincan, Richard Bowden
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.10446v1)
- **发表日期**: 2026-03-11
- **匹配关键词**: 3D gaussian splatting, gaussian splatting
- **arXiv**: [2603.10446v1](http://arxiv.org/abs/2603.10446v1)
- **📥 PDF**: 已下载至本地 (`2603.10446v1_SignSparK_Efficient_Multilingual_Sign_Language_Production_via_Sparse_Keyframe_Learning.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 生成自然且语言准确的手语虚拟形象仍是一项艰巨挑战。当前手语生成框架面临明显权衡：直接文本到姿态模型易受均值回归效应影响，而词典检索方法则会产生机械化的断裂式过渡。为解决这一问题，我们提出一种新颖的训练范式，利用稀疏关键帧捕捉人类手语的真实运动学分布。通过从这些离散锚点预测密集运动，我们的方法在确保流畅表达的同时缓解了均值回归问题。为实现该范式的大规模应用，我们首先提出FAST——一种能自动挖掘精确时间边界的超高效手语分割模型。随后我们推出SignSparK，这是一个基于条件流匹配的大规模框架，利用提取的锚点在SMPL-X和MANO空间中合成三维手语序列。这种关键帧驱动的架构还独特实现了关键帧到姿态的生成功能，使手语序列的精确时空编辑成为可能。此外，我们采用基于重建的条件流匹配目标，可在少于十次采样步骤中实现高保真合成；这使得SignSparK能够扩展至四种不同手语体系，构建了迄今规模最大的多语言手语生成框架。最后，通过集成三维高斯泼溅技术实现照片级真实感渲染，我们通过广泛评估证明SignSparK在多样化手语生成任务和多语言基准测试中确立了新的技术标杆。

---

### 11. World2Act: Latent Action Post-Training via Skill-Compositional World Models

- **作者**: An Dinh Vuong, Tuan Van Vo, Abdullah Sohail, Haoran Ding, Liang Ma, Xiaodan Liang, Anqing Duan, Ivan Laptev, Ian Reid
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.10422v1)
- **发表日期**: 2026-03-11
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2603.10422v1](http://arxiv.org/abs/2603.10422v1)
- **📥 PDF**: 已下载至本地 (`2603.10422v1_World2Act_Latent_Action_Post-Training_via_Skill-Compositional_World_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 世界模型已成为视觉-语言-动作策略后训练的一种有效方法，能够提升策略在环境变化下的鲁棒性与泛化能力。然而，当前多数基于世界模型的后训练方法依赖于像素空间监督，导致策略容易受到不完美世界模型推演产生的像素级伪影和幻觉影响。我们提出World2Act后训练框架，通过对比匹配目标将VLA动作直接与世界模型的视频动态潜在空间对齐，从而降低对像素的依赖。后训练效果与推演质量密切相关，但现有世界模型大多基于固定长度视频片段训练，难以适应机器人执行时长差异巨大的任意长度视频生成需求。为此，我们设计了一种基于大语言模型的自动技能分解流程，将高层指令拆解为低层提示。该流程生成的RoboCasa-Skill和LIBERO-Skill数据集支持技能组合式世界模型，确保在不同任务时间跨度下保持时序一致性。实验表明，将World2Act应用于GR00T-N1.6和Cosmos Policy等VLA模型，在RoboCasa和LIBERO基准上取得最先进性能，现实场景任务表现提升6.7%，显著增强了具身智能体的泛化能力。

---

### 12. Overcoming Visual Clutter in Vision Language Action Models via Concept-Gated Visual Distillation

- **作者**: Sangmim Song, Sarath Kodagoda, Marc Carmichael, Karthick Thiyagarajan
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.10340v1)
- **发表日期**: 2026-03-11
- **匹配关键词**: vision-language-action, vision language action model, VLA, vision language action
- **arXiv**: [2603.10340v1](http://arxiv.org/abs/2603.10340v1)
- **📥 PDF**: 已下载至本地 (`2603.10340v1_Overcoming_Visual_Clutter_in_Vision_Language_Action_Models_via_Concept-Gated_Visual_Distillation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型在零样本泛化方面表现出色，但在杂乱环境中常面临"精确推理鸿沟"问题。这一缺陷源于背景诱导的特征稀释现象——高频语义噪声会破坏精确操作所需的几何基础。为弥合此鸿沟，我们提出概念门控视觉蒸馏（CGVD），这是一种无需训练、模型无关的推理框架，能有效稳定VLA策略。CGVD通过将指令解析为安全集与干扰集，采用双层目标精炼流程——结合交叉验证与空间消歧——显式惩罚误报目标并隔离真实操作对象。随后通过基于傅里叶的修复技术处理场景，生成能主动抑制语义干扰、同时保留关键空间几何与视觉本体感知的洁净观测数据。在高度杂乱的操作任务中进行大量评估表明，CGVD能有效防止性能崩溃。在密集语义干扰环境中，本方法显著优于现有先进基线模型，成功率提升至77.5%（基线模型为43.0%）。通过强制严格属性遵循，CGVD确立了推理时视觉蒸馏作为杂乱环境下鲁棒机器人操作的关键前提。

---

### 13. Update-Free On-Policy Steering via Verifiers

- **作者**: Maria Attarian, Ian Vyse, Claas Voelcker, Jasper Gerigk, Evgenii Opryshko, Anas Almasri, Sumeet Singh, Yilun Du, Igor Gilitschenski
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.10282v1)
- **发表日期**: 2026-03-10
- **匹配关键词**: diffusion policy
- **arXiv**: [2603.10282v1](http://arxiv.org/abs/2603.10282v1)
- **📥 PDF**: 已下载至本地 (`2603.10282v1_Update-Free_On-Policy_Steering_via_Verifiers.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 近年来，行为克隆已成为机器人模仿人类演示的主流方法之一。然而，尽管取得了一定成功，行为克隆策略往往存在脆弱性，在精确操作任务中表现欠佳。为克服这些问题，我们提出UF-OPS方法——一种无需更新的在线策略引导机制，使机器人能够预测其动作的成功概率并在执行过程中动态调整策略。该方法通过在策略初始评估阶段获取的策略推演数据训练验证函数，随后利用这些验证函数引导基础策略选择更高成功率的动作。我们的方法在不改变基础参数的前提下提升了黑盒扩散策略的性能，具有轻量化与灵活性的特点。通过仿真与真实场景数据验证，该方法在五项实际任务中平均成功率较基础策略提升49%。

---

### 14. Cross-Hand Latent Representation for Vision-Language-Action Models

- **作者**: Guangqi Jiang, Yutong Liang, Jianglong Ye, Jia-Yang Huang, Changwei Jing, Rocky Duan, Pieter Abbeel, Xiaolong Wang, Xueyan Zou ⭐
  - **高亮作者**: Xiaolong Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.10158v1)
- **发表日期**: 2026-03-10
- **匹配关键词**: vision-language-action, vision-language-action model, VLA
- **arXiv**: [2603.10158v1](http://arxiv.org/abs/2603.10158v1)
- **📥 PDF**: 已下载至本地 (`2603.10158v1_Cross-Hand_Latent_Representation_for_Vision-Language-Action_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 灵巧操作对于现实世界中的机器人自主性至关重要，这正如人类手部协调在日常活动中扮演的核心角色。人类依赖丰富的多模态感知——视觉、听觉和语言引导的意图——来执行灵巧动作，这启发了基于视觉和语言条件的机器人操作系统的发展。然而，为灵巧操作训练可靠的视觉-语言-动作模型需要大量不同机器人手的大规模演示数据。此外，随着新型灵巧机器人形态的快速涌现，为每种形态收集数据变得成本高昂且不切实际，因此亟需可扩展的跨形态学习方案。我们提出了XL-VLA框架，这是一个集成了跨多种灵巧手共享的统一潜在动作空间的视觉-语言-动作系统。这种形态无关的潜在空间可直接嵌入标准VLA架构，实现无缝的跨形态训练，并高效复用现有及新收集的数据。实验结果表明，XL-VLA在原始关节空间操作的基准VLA模型上持续表现出更优性能，证明其是可扩展跨形态灵巧操作的有效解决方案。

---

### 15. AR-VLA: True Autoregressive Action Expert for Vision-Language-Action Models

- **作者**: Yutong Hu, Jan-Nico Zaech, Nikolay Nikolov, Yuanqi Yao, Sombit Dey, Giuliano Albanese, Renaud Detry, Luc Van Gool, Danda Paudel
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.10126v1)
- **发表日期**: 2026-03-10
- **匹配关键词**: vision-language-action, vision-language-action model, VLA
- **arXiv**: [2603.10126v1](http://arxiv.org/abs/2603.10126v1)
- **📥 PDF**: 已下载至本地 (`2603.10126v1_AR-VLA_True_Autoregressive_Action_Expert_for_Vision-Language-Action_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出一种独立的自回归动作专家模型，该模型以可刷新的视觉语言前缀为条件，将动作生成为连续因果序列。与现有视觉-语言-动作模型及扩散策略在每次新观测时重置时间上下文并被动预测动作不同，我们的动作专家通过长效记忆机制维护自身历史状态，具备本质上的上下文感知能力。这种结构解决了快速控制与慢速推理之间的频率失配问题，既能高效独立预训练运动学语法，又可模块化集成重型感知主干网络，自然确保跨帧动作生成的时空一致性。为同步这些异步混合的视觉-语言-动作模态，我们采用重锚定机制，在数学层面同时处理训练与推理过程中的感知滞后效应。在仿真与真实机器人操作任务上的实验表明，该方法能有效替代传统基于分块的动作头部结构，适用于专用与通用策略场景。自回归视觉-语言-动作模型展现出卓越的历史感知能力，在保持或超越先进反应式视觉-语言-动作模型任务成功率的同时，生成的动作轨迹显著更平滑。总体而言，本研究提出了一种可扩展的上下文感知动作生成范式，为训练高效机器人策略提供了稳健的结构基础。

---

### 16. TiPToP: A Modular Open-Vocabulary Planning System for Robotic Manipulation

- **作者**: William Shen, Nishanth Kumar, Sahit Chintalapudi, Jie Wang, Christopher Watson, Edward Hu, Jing Cao, Dinesh Jayaraman, Leslie Pack Kaelbling, Tomás Lozano-Pérez
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.09971v1)
- **发表日期**: 2026-03-10
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2603.09971v1](http://arxiv.org/abs/2603.09971v1)
- **📥 PDF**: 已下载至本地 (`2603.09971v1_TiPToP_A_Modular_Open-Vocabulary_Planning_System_for_Robotic_Manipulation.pdf`)
- **🔓 开源**: PROJECT_PAGE, CODE
  - 链接：https://tiptop-robot.github.io
- **中文摘要**: 我们推出TiPToP，这是一个可扩展的模块化系统，它将预训练的视觉基础模型与现有的任务与运动规划器（TAMP）相结合，能够直接从输入的RGB图像和自然语言指令中解决多步骤操作任务。我们的系统设计追求简洁易用：可在标准DROID配置上于一小时内完成安装并运行，且只需极少调整即可适配新的机器人实体。我们在仿真和真实环境中对TiPToP进行了28项桌面操作任务评估——该系统无需任何机器人训练数据——结果显示其性能达到甚至超越了经过350小时实体专用演示微调的视觉-语言-动作模型$π_{0.5}\text{-DROID}$。TiPToP的模块化架构使我们能够在组件层面分析系统故障模式。通过对173次实验评估结果的分析，我们明确了系统改进方向。我们将TiPToP开源发布，以推动模块化操作系统研究及学习与规划更紧密融合的探索。项目网站与代码：https://tiptop-robot.github.io

---

### 17. Neural Field Thermal Tomography: A Differentiable Physics Framework for Non-Destructive Evaluation

- **作者**: Tao Zhong, Yixun Hu, Dongzhe Zheng, Aditya Sood, Christine Allen-Blanchette
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.11045v1)
- **发表日期**: 2026-03-11
- **匹配关键词**: 3d reconstruction, 3D reconstruction
- **arXiv**: [2603.11045v1](http://arxiv.org/abs/2603.11045v1)
- **📥 PDF**: 已下载至本地 (`2603.11045v1_Neural_Field_Thermal_Tomography_A_Differentiable_Physics_Framework_for_Non-Destructive_Evaluation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出神经场热层析成像（NeFTY），这是一种基于瞬态表面温度测量实现材料特性定量三维重建的可微分物理框架。传统热成像技术依赖忽略横向扩散的逐像素一维近似方法，而软约束物理信息神经网络（PINNs）在瞬态扩散场景中常因梯度刚性而失效。NeFTY通过严格数值求解器将三维扩散场参数化为连续神经场进行优化。通过可微分物理求解器，我们的方法以硬约束形式强化热力学定律，同时保持高分辨率三维层析成像所需的内存效率。这种“先离散后优化”范式有效缓解了逆热传导固有的谱偏差和不适定性，实现了任意尺度下亚表面缺陷的精准重构。在合成数据上的实验验证表明，NeFTY在亚表面缺陷定位精度上较基线方法有显著提升。更多细节请访问 https://cab-lab-princeton.github.io/nefty/

---

### 18. DynVLA: Learning World Dynamics for Action Reasoning in Autonomous Driving

- **作者**: Shuyao Shang, Bing Zhan, Yunfei Yan, Yuqi Wang, Yingyan Li, Yasong An, Xiaoman Wang, Jierui Liu, Lu Hou, Lue Fan, Zhaoxiang Zhang, Tieniu Tan
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.11041v1)
- **发表日期**: 2026-03-11
- **匹配关键词**: VLA
- **arXiv**: [2603.11041v1](http://arxiv.org/abs/2603.11041v1)
- **📥 PDF**: 已下载至本地 (`2603.11041v1_DynVLA_Learning_World_Dynamics_for_Action_Reasoning_in_Autonomous_Driving.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出DynVLA——一种创新的驾驶视觉语言动作模型，其核心是引入名为"动态思维链"的全新推理范式。该模型在生成驾驶动作前，先预测紧凑的世界动态表征，从而实现更具信息支撑和物理依据的决策过程。为获得紧凑的动态表征，DynVLA设计了动态分词器，将未来场景演化压缩为少量动态令牌。针对交互密集型驾驶场景中复杂的环境动态，模型创新性地解耦自车动态与环境动态，实现更精准的世界动态建模。通过监督微调与强化微调相结合的训练策略，DynVLA被训练为先产生动态令牌再生成动作的推理流程，在保持低延迟推理的同时显著提升决策质量。相较于缺乏细粒度时空理解的文本思维链，以及因密集图像预测产生冗余的视觉思维链，动态思维链以紧凑、可解释且高效的形式捕捉世界演化规律。在NAVSIM、Bench2Drive及大规模内部数据集上的实验表明，DynVLA在各项指标上持续超越文本思维链与视觉思维链方法，有力验证了动态思维链的有效性与实用价值。

---

### 19. S2D: Sparse to Dense Lifting for 3D Reconstruction with Minimal Inputs

- **作者**: Yuzhou Ji, Qijian Tian, He Zhu, Xiaoqi Jiang, Guangzhi Cao, Lizhuang Ma, Yuan Xie, Xin Tan
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.10893v1)
- **发表日期**: 2026-03-11
- **匹配关键词**: 3D gaussian splatting, 3d reconstruction, 3D reconstruction, gaussian splatting
- **arXiv**: [2603.10893v1](http://arxiv.org/abs/2603.10893v1)
- **📥 PDF**: 已下载至本地 (`2603.10893v1_S2D_Sparse_to_Dense_Lifting_for_3D_Reconstruction_with_Minimal_Inputs.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 显式三维表示已成为三维仿真与理解的重要媒介。然而，最常用的点云与三维高斯泼溅（3DGS）技术分别存在渲染非真实感强及稀疏输入下性能显著退化的问题。本文提出稀疏到稠密提升框架（S2D），通过桥接两种表示形式，实现了以极简输入达成高质量3DGS重建的创新方案。该提升机制包含双重路径：首先设计高效的单步扩散模型，通过提升稀疏点云实现高保真图像伪影修复；同时，为重建三维一致场景，提出结合随机采样丢弃与加权梯度的重建策略，实现从稀疏输入视角到稠密新视角的鲁棒模型拟合。大量实验表明，S2D在不同输入稀疏度下均能生成最具一致性的新视角引导，并达到第一梯队的稀疏视角重建质量。通过以现有方法中最少的采集量重建稳定场景，S2D为3DGS应用实现了最小化输入需求。

---

### 20. PolGS++: Physically-Guided Polarimetric Gaussian Splatting for Fast Reflective Surface Reconstruction

- **作者**: Yufei Han, Chu Zhou, Youwei Lyu, Qi Chen, Si Li, Boxin Shi, Yunpeng Jia, Heng Guo, Zhanyu Ma
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.10801v1)
- **发表日期**: 2026-03-11
- **匹配关键词**: 3D gaussian splatting, gaussian splatting
- **arXiv**: [2603.10801v1](http://arxiv.org/abs/2603.10801v1)
- **📥 PDF**: 已下载至本地 (`2603.10801v1_PolGS++_Physically-Guided_Polarimetric_Gaussian_Splatting_for_Fast_Reflective_Surface_Reconstruction.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 反射表面的精确重建仍是计算机视觉领域的基础性挑战，在实时虚拟现实与数字内容创作中具有广泛应用。尽管三维高斯溅射（3DGS）通过显式表征实现了高效的新视角渲染，但其在反射表面处理上仍落后于隐式神经方法，尤其在精细几何结构与表面法线恢复方面存在局限。为弥补这一差距，我们提出PolGS++——一种物理引导的偏振高斯溅射框架，用于实现快速反射表面重建。具体而言，我们将偏振双向反射分布函数（pBRDF）模型融入3DGS，显式解耦漫反射与镜面反射分量，为反射表面恢复提供物理基础的反射率建模及更强几何线索。此外，我们引入深度引导的可见性掩码获取机制，无需昂贵的光线追踪求交计算即可在高斯溅射中实现基于偏振角（AoP）的切空间一致性约束。这种物理引导设计在仅需约10分钟训练的条件下，显著提升了重建质量与效率。在合成与真实场景数据集上的大量实验验证了本方法的有效性。

---

