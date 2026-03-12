# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-03-12 08:04

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 5/20 篇提供

**🌟 Highlight**: 19 篇 | **📌 Poster**: 1 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. TiPToP: A Modular Open-Vocabulary Planning System for Robotic Manipulation

- **作者**: William Shen, Nishanth Kumar, Sahit Chintalapudi, Jie Wang, Christopher Watson, Edward Hu, Jing Cao, Dinesh Jayaraman, Leslie Pack Kaelbling, Tomás Lozano-Pérez
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.09971v1)
- **发表日期**: 2026-03-10
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2603.09971v1](http://arxiv.org/abs/2603.09971v1)
- **📥 PDF**: 已下载至本地 (`2603.09971v1_TiPToP_A_Modular_Open-Vocabulary_Planning_System_for_Robotic_Manipulation.pdf`)
- **🔓 开源**: CODE, PROJECT_PAGE
  - 链接：https://tiptop-robot.github.io
- **中文摘要**: 我们推出TiPToP，这是一个可扩展的模块化系统，它将预训练的视觉基础模型与现有的任务与运动规划器（TAMP）相结合，能够直接从输入的RGB图像和自然语言指令中解决多步骤操作任务。我们的系统设计追求简洁易用：可在标准DROID配置中于一小时内完成安装并运行，且只需极少调整即可适配新的机器人实体。我们在仿真和真实环境中对TiPToP进行了28项桌面操作任务评估——该系统无需任何机器人训练数据——结果显示其性能达到甚至超越了经过350小时实体专用演示微调的视觉-语言-动作模型$π_{0.5}\text{-DROID}$。TiPToP的模块化架构使我们能够在组件层面分析系统故障模式。通过对173次实验评估结果的分析，我们明确了系统改进方向。我们将TiPToP开源发布，以推动模块化操作系统研究及学习与规划更紧密融合的探索。项目网站与代码：https://tiptop-robot.github.io

---

### 2. NS-VLA: Towards Neuro-Symbolic Vision-Language-Action Models

- **作者**: Ziyue Zhu, Shangyang Wu, Shuai Zhao, Zhiqiu Zhao, Shengjie Li, Yi Wang, Fang Li, Haoran Luo
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.09542v1)
- **发表日期**: 2026-03-10
- **匹配关键词**: vision-language-action, vision-language-action model, VLA, exploration
- **arXiv**: [2603.09542v1](http://arxiv.org/abs/2603.09542v1)
- **📥 PDF**: 已下载至本地 (`2603.09542v1_NS-VLA_Towards_Neuro-Symbolic_Vision-Language-Action_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型旨在将指令与视觉情境相结合，并生成机器人操作的动作序列。尽管近期取得进展，VLA模型仍面临诸多挑战：如何学习相关且可重用的基础动作单元、降低对大规模数据和复杂架构的依赖，以及实现超越演示样本的自主探索。为应对这些挑战，我们提出一种基于在线强化学习（RL）的新型神经符号视觉-语言-动作（NS-VLA）框架。该框架引入符号编码器以嵌入视觉与语言特征并提取结构化基础单元，采用符号求解器实现数据高效的动作序列规划，并利用在线强化学习通过扩展式探索优化动作生成。在机器人操作基准测试中的实验表明，NS-VLA在单次训练和数据扰动场景下均优于现有方法，同时展现出更强的零样本泛化能力、更高的数据效率以及更广阔的探索空间。代码已开源。

---

### 3. Beyond Short-Horizon: VQ-Memory for Robust Long-Horizon Manipulation in Non-Markovian Simulation Benchmarks

- **作者**: Wang Honghui, Jing Zhi, Ao Jicong, Song Shiji, Li Xuelong, Huang Gao, Bai Chenjia
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.09513v1)
- **发表日期**: 2026-03-10
- **匹配关键词**: vision-language-action model, VLA, vision-language-action, articulated manipulation, articulated object
- **arXiv**: [2603.09513v1](http://arxiv.org/abs/2603.09513v1)
- **📥 PDF**: 已下载至本地 (`2603.09513v1_Beyond_Short-Horizon_VQ-Memory_for_Robust_Long-Horizon_Manipulation_in_Non-Markovian_Simulation_Benc.pdf`)
- **🔓 开源**: PROJECT_PAGE
- **中文摘要**: 真实机器人数据采集的高成本使得机器人仿真成为评估与数据生成的可扩展平台。然而现有基准测试大多集中于抓放等简单操作任务，未能捕捉现实任务中的非马尔可夫特性以及关节物体交互的复杂性。为突破这一局限，我们提出RuleSafe——一个基于可扩展大语言模型辅助仿真框架的新型关节操作基准测试系统。RuleSafe设计了配备多样化解锁机制（如钥匙锁、密码锁、逻辑锁）的保险箱，这些机制要求不同的多阶段推理与操作策略。由大语言模型生成的规则产生了需要时序建模和基于记忆推理的非马尔可夫长周期任务。我们进一步提出VQ-Memory，这是一种紧凑的结构化时序表征方法，利用向量量化变分自编码器将历史本体感知状态编码为离散潜在标记。该表征在过滤底层噪声的同时保留高层任务阶段上下文，为现有视觉-语言-动作模型提供轻量级且鲁棒的时序线索。在先进视觉-语言-动作模型与扩散策略上的大量实验表明，VQ-Memory能持续提升长周期规划能力，增强对未见配置的泛化性能，并以更低计算成本实现更高效操作。项目页面：vqmemory.github.io

---

### 4. SEA-Nav: Efficient Policy Learning for Safe and Agile Quadruped Navigation in Cluttered Environments

- **作者**: Shiyi Chen, Mingye Yang, Haiyan Mao, Jiaqi Zhang, Haiyi Liu, Shuheng He, Debing Zhang, Zihao Qiu, Chun Zhang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.09460v1)
- **发表日期**: 2026-03-10
- **匹配关键词**: robot navigation, navigation, exploration
- **arXiv**: [2603.09460v1](http://arxiv.org/abs/2603.09460v1)
- **📥 PDF**: 已下载至本地 (`2603.09460v1_SEA-Nav_Efficient_Policy_Learning_for_Safe_and_Agile_Quadruped_Navigation_in_Cluttered_Environments.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 在密集杂乱环境中高效训练四足机器人导航仍是一项重大挑战。现有方法要么受限于简单障碍物分布下安全性与敏捷性的不足，要么在复杂环境中运动速度缓慢，且通常需要过长的训练周期。为此，我们提出SEA-Nav（安全、高效、敏捷导航）强化学习框架。在多样化密集障碍环境中，基于可微分控制屏障函数（CBF）的安全屏障约束导航策略输出安全速度指令。通过引入自适应碰撞回放机制与危险探索奖励机制，提升从关键经验中学习的概率，引导高效探索与利用。最后整合运动学动作约束以确保速度指令的安全性，促进成功物理部署。据我们所知，这是首个能在分钟级训练时间内实现现实世界高难度四足导航任务的方法。

---

### 5. CORAL: Scalable Multi-Task Robot Learning via LoRA Experts

- **作者**: Yuankai Luo, Woping Chen, Tong Liang, Zhenguo Li
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.09298v1)
- **发表日期**: 2026-03-10
- **匹配关键词**: mobile manipulator, vision-language-action, VLA
- **arXiv**: [2603.09298v1](http://arxiv.org/abs/2603.09298v1)
- **📥 PDF**: 已下载至本地 (`2603.09298v1_CORAL_Scalable_Multi-Task_Robot_Learning_via_LoRA_Experts.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 在现实世界的机器人技术中部署视觉-语言-动作（VLA）模型面临一个核心的多任务学习挑战：如何协调多任务机器人学习中的任务干扰。当多个任务在单一阶段联合微调时，来自不同任务的梯度可能发生冲突，导致负迁移并降低每个任务的性能。然而，为每个任务维护一个完整独立的检查点通常因存储和部署成本过高而不可行。为解决这一困境，我们提出了CORAL框架，这是一个与主干网络和具体实现无关的框架，旨在主要缓解多任务干扰，同时自然支持持续扩展新任务。CORAL冻结一个预训练的VLA主干网络，并为每个任务附加一个轻量级的低秩适应（LoRA）专家模块；在运行时，动态推理引擎（CORAL管理器）将语言指令路由到相应的专家模块，并在零推理开销的情况下实时切换专家。这种严格的参数隔离避免了复杂的门控网络，并通过设计防止参数层面的跨任务干扰；作为附加能力，它还支持顺序引入新任务而不会因灾难性遗忘导致参数覆盖。我们在真实世界的Galaxea R1双臂移动操作机器人及三个仿真基准（LIBERO、WidowX、Google Robot）上验证了CORAL，结果表明CORAL能够克服细粒度指令歧义，显著优于联合训练方法，为终身多任务机器人学习提供了一个实用且可扩展的系统。网站：https://frontierrobo.github.io/CORAL

---

### 6. See, Plan, Rewind: Progress-Aware Vision-Language-Action Models for Robust Robotic Manipulation

- **作者**: Tingjun Dai, Mingfei Han, Tingwen Du, Zhiheng Liu, Zhihui Li, Salman Khan, Jun Yu, Xiaojun Chang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.09292v1)
- **发表日期**: 2026-03-10
- **匹配关键词**: vision-language-action, vision-language-action model, VLA
- **arXiv**: [2603.09292v1](http://arxiv.org/abs/2603.09292v1)
- **📥 PDF**: 已下载至本地 (`2603.09292v1_See,_Plan,_Rewind_Progress-Aware_Vision-Language-Action_Models_for_Robust_Robotic_Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 通过明确、可操作的里程碑来测量任务进度对于实现稳健的机器人操作至关重要。这种进度感知能力使模型能够定位当前任务状态，预测可验证的中间状态，并在进度停滞时检测故障并从中恢复。为体现这一能力，我们提出了"观察-规划-回退"框架——一种动态将语言指令转化为空间子目标序列的进度感知视觉-语言-动作框架。该框架通过持续的核心循环运行：观察当前状态与即将到达的里程碑，规划前往下一个二维路径点的轨迹，并通过监控预期序列的进度在失败时回退至可恢复状态。这种闭环方法实现了稳健的错误纠正，无需额外训练数据或辅助模型。大量实验证明了该框架的有效性、泛化能力和稳健性：在LIBERO基准测试中，SPR比MolmoAct基线高出5%。在具有未知指令和初始状态的挑战性LIBERO-Plus基准测试中，SPR以最小的性能下降实现了最先进的稳健性，超越了OpenVLA-OFT和UniVLA，展现出卓越的分布外稳健性。

---

### 7. DenoiseSplat: Feed-Forward Gaussian Splatting for Noisy 3D Scene Reconstruction

- **作者**: Fuzhen Jiang, Zhuoran Li, Yinlin Zhang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.09291v1)
- **发表日期**: 2026-03-10
- **匹配关键词**: 3D gaussian splatting, nerf, gaussian splatting
- **arXiv**: [2603.09291v1](http://arxiv.org/abs/2603.09291v1)
- **📥 PDF**: 已下载至本地 (`2603.09291v1_DenoiseSplat_Feed-Forward_Gaussian_Splatting_for_Noisy_3D_Scene_Reconstruction.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 三维场景重建与新视角合成是虚拟现实、机器人技术和内容创作领域的基础任务。然而，大多数神经辐射场与三维高斯溅射流程均假设输入数据为洁净图像，在实际噪声与伪影干扰下性能会显著下降。为此，我们提出DenoiseSplat——一种面向含噪多视角图像的前馈式三维高斯溅射方法。通过在RE10K数据集上注入强度可控的高斯噪声、泊松噪声、散斑噪声及椒盐噪声，我们构建了大规模、场景一致的含噪-洁净基准数据集。采用轻量级MVSplat风格的前馈主干网络，我们仅以洁净的二维渲染图像作为监督信号进行端到端训练，无需任何三维真值数据。在含噪RE10K数据集上的实验表明，DenoiseSplat在峰值信噪比、结构相似性指数和感知损失指标上均优于原始MVSplat方法及强力的两阶段基线方法（IDF+MVSplat），且在不同噪声类型与强度下均保持稳定优势。

---

### 8. Embodied Human Simulation for Quantitative Design and Analysis of Interactive Robotics

- **作者**: Chenhui Zuo, Jinhao Xu, Michael Qian Vergnolle, Yanan Sui
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.09218v1)
- **发表日期**: 2026-03-10
- **匹配关键词**: human-robot interaction, exploration
- **arXiv**: [2603.09218v1](http://arxiv.org/abs/2603.09218v1)
- **📥 PDF**: 已下载至本地 (`2603.09218v1_Embodied_Human_Simulation_for_Quantitative_Design_and_Analysis_of_Interactive_Robotics.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 物理交互机器人技术——从可穿戴设备到协作型人形机器人——需要机械设计与控制系统的紧密协调。然而，由于复杂的人体生物力学与运动响应特性，交互动力学的评估始终面临挑战。传统实验方法依赖间接测量指标，无法获取人体内部状态（如肌肉力量或关节负荷）的直接数据。为此，我们开发了一个基于仿真的可扩展框架，用于物理人机交互的定量分析。该框架的核心是一个全身肌肉骨骼模型，作为人体动力学系统的预测代理。在强化学习控制器的驱动下，该模型能够生成具有生理学依据的自适应运动行为。我们采用序列化训练流程，使预训练的人类运动控制策略作为一致性评估器，从而在大规模设计空间探索中实现计算可行性。通过模拟耦合的人机系统，该框架可获取内部生物力学指标，为机器人结构参数与控制策略的协同优化提供系统化方法。我们在人机外骨骼交互优化中验证了该框架的有效性，展示了关节对位改善与接触力降低的优化效果。本研究确立了具身化人体仿真作为交互式机器人设计的可扩展范式。

---

### 9. DexHiL: A Human-in-the-Loop Framework for Vision-Language-Action Model Post-Training in Dexterous Manipulation

- **作者**: Yifan Han, Zhongxi Chen, Yuxuan Zhao, Congsheng Xu, Yanming Shao, Yichuan Peng, Yao Mu, Wenzhao Lian
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.09121v1)
- **发表日期**: 2026-03-10
- **匹配关键词**: vision-language-action, vision-language-action model, VLA
- **arXiv**: [2603.09121v1](http://arxiv.org/abs/2603.09121v1)
- **📥 PDF**: 已下载至本地 (`2603.09121v1_DexHiL_A_Human-in-the-Loop_Framework_for_Vision-Language-Action_Model_Post-Training_in_Dexterous_Man.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://chenzhongxi-sjtu.github.io/dexhil/
- **中文摘要**: 虽然视觉-语言-动作模型在机器人操作中展现出良好的泛化能力，但在特定且复杂的下游任务中部署仍需有效的后训练。与此同时，人机协同学习已被证明是优化机器人策略的有效机制。然而，将这一范式扩展至灵巧操作仍面临挑战：多指控制具有高维度、密集接触的特点，其执行分布与标准手臂动作存在显著差异，导致现有灵巧视觉-语言-动作系统在可靠性和适应性方面受限。我们提出DexHiL——首个面向灵巧视觉-语言-动作模型的集成化手臂-人手协同操作框架，实现了在单一系统中对手臂与灵巧手的协同干预。DexHiL引入了具备干预感知的数据采样策略，优先选取校正片段进行后训练，并配备支持实时人工校正的轻量级遥操作界面。真实机器人实验表明，DexHiL作为高效的后训练框架能带来显著的性能提升，在不同任务中的平均成功率较标准纯离线微调基线高出25%。

项目主页：https://chenzhongxi-sjtu.github.io/dexhil/

---

### 10. SurgCalib: Gaussian Splatting-Based Hand-Eye Calibration for Robot-Assisted Minimally Invasive Surgery

- **作者**: Zijian Wu, Shuojue Yang, Yu Chung Lee, Eitan Prisman, Yueming Jin, Septimiu E. Salcudean
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.08983v1)
- **发表日期**: 2026-03-09
- **匹配关键词**: gaussian splatting
- **arXiv**: [2603.08983v1](http://arxiv.org/abs/2603.08983v1)
- **📥 PDF**: 已下载至本地 (`2603.08983v1_SurgCalib_Gaussian_Splatting-Based_Hand-Eye_Calibration_for_Robot-Assisted_Minimally_Invasive_Surger.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出了一种基于高斯点云的手术机器人手眼标定框架。在视觉引导的机器人系统中，准确估计机器人基座与相机坐标系之间的刚性变换对于实现可靠的闭环控制至关重要。对于线缆驱动的手术机器人，这一任务面临独特挑战。由于线缆拉伸和回程间隙，手术器械编码器提供的本体感知测量往往不够精确。传统手眼标定方法通常依赖已知的基准标记图案，并通过求解AX=XB方程实现标定。虽然有效，但在手术室环境中引入额外标记物可能违反无菌操作规范并干扰手术流程。本研究提出SurgCalib——一种无需标记物的自动标定框架，具备在手术室应用的潜力。该框架首先利用原始运动学测量值初始化手术器械位姿，随后在高斯点云可微分渲染管道中，通过远程运动中心约束下的两阶段优化过程对位姿进行精细化调整。我们在公开的dVRK基准数据集SurgPose上评估了所提方法。结果显示：左右器械的二维工具尖端重投影误差分别为12.24像素（2.06毫米）和11.33像素（1.9毫米），三维工具尖端欧氏距离误差分别为5.98毫米和4.75毫米。

---

### 11. FAME: Force-Adaptive RL for Expanding the Manipulation Envelope of a Full-Scale Humanoid

- **作者**: Niraj Pudasaini, Yutong Zhang, Jensen Lavering, Alessandro Roncone, Nikolaus Correll
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.08961v1)
- **发表日期**: 2026-03-09
- **匹配关键词**: bimanual manipulation
- **arXiv**: [2603.08961v1](http://arxiv.org/abs/2603.08961v1)
- **📥 PDF**: 已下载至本地 (`2603.08961v1_FAME_Force-Adaptive_RL_for_Expanding_the_Manipulation_Envelope_of_a_Full-Scale_Humanoid.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 在仿人机器人双手操作中，承受外部手部作用力时保持平衡至关重要，因为交互力会通过运动链传递并限制可行的操作范围。我们提出\textbf{FAME}——一种力自适应强化学习框架，该框架通过编码上半身关节构型与双手交互力的隐式上下文来调节站立策略。训练过程中，我们在仿真环境中对每只手施加多样化、球面采样的三维作用力以注入扰动，并结合上半身姿态课程学习，使策略能够适应连续变化的手臂构型所产生的操作扰动。部署阶段，通过机器人动力学系统估算交互力并输入同一编码器，无需腕部力/力矩传感器即可实现在线自适应。在五种固定手臂构型、随机手部作用力及指令化基座高度的仿真实验中，FAME将平均站立成功率提升至73.84%，而仅采用课程学习的基线方法为51.40%，基础策略仅为29.44%。我们进一步将习得策略部署于全尺寸宇树H12仿人机器人，在典型负载交互场景（包括非对称单臂负载与对称双手负载）中评估其鲁棒性。代码与演示视频详见https://fame10.github.io/Fame/。

---

### 12. Fly, Track, Land: Infrastructure-less Magnetic Localization for Heterogeneous UAV-UGV Teaming

- **作者**: Valerio Brunacci, Davide Plozza, Alessio De Angelis, Michele Magno, Tommaso Polonelli
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.08926v1)
- **发表日期**: 2026-03-09
- **匹配关键词**: navigation, exploration
- **arXiv**: [2603.08926v1](http://arxiv.org/abs/2603.08926v1)
- **📥 PDF**: 已下载至本地 (`2603.08926v1_Fly,_Track,_Land_Infrastructure-less_Magnetic_Localization_for_Heterogeneous_UAV-UGV_Teaming.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出了一套完整的无基础设施磁感应定位系统，使轻型无人机能够以厘米级精度在作为动态对接平台的移动四足机器人上实现自主悬停、跟踪与降落。本研究推进了异构机器人协作的愿景——超轻型飞行机器人可作为地面无人驾驶车辆（UGV）的移动感知代理。通过扩展感知范围并提供互补视角，无人机可提升大规模未知环境中的探索效率与数据采集质量。该系统旨在通过紧凑、嵌入式且无需基础设施的磁传感方式，与传统定位模式形成互补，提供精确的短距离相对定位，从而弥合粗略导航与精确无人机对接之间的差距。无人机搭载的单个轻型接收线圈及全嵌入式估计流程可在UGV坐标系中实现20赫兹的相对位姿估计，三维位置均方根误差（RMSE）达到5厘米。系统采用实时估计与热启动求解器计算三维位置，再通过机载扩展卡尔曼滤波器与惯性及光流测量数据融合。真实环境实验验证了该框架的有效性：相较于现有先进方法，在无基础设施场景中显著提升了无人机-UGV协同作业能力，且无需外部锚点或全局定位。在动态场景中，无人机成功实现对移动UGV的跟踪对接，保持7.2厘米的均方根误差，并完成自主着陆。

---

### 13. Proprioceptive Safe Active Navigation and Exploration for Planetary Environments

- **作者**: Matthew Y. Jiang, Feifei Qian, Shipeng Liu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.08905v1)
- **发表日期**: 2026-03-09
- **匹配关键词**: navigation, exploration
- **arXiv**: [2603.08905v1](http://arxiv.org/abs/2603.08905v1)
- **📥 PDF**: 已下载至本地 (`2603.08905v1_Proprioceptive_Safe_Active_Navigation_and_Exploration_for_Planetary_Environments.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 可变形颗粒地形在行星探测中带来显著的运动与停滞风险，且难以通过遥感技术（如视觉）进行探测。腿式机器人能够在运动过程中通过腿与地形的相互作用感知地形特性，为评估可变形环境中的通行性提供了直接手段。然而，如何系统利用这种交互信息进行导航规划仍缺乏深入研究。为此，我们提出PSANE框架——一种基于本体感知的安全主动导航与探索系统，该框架利用腿-地形交互测量数据，在未知可变形环境中实现安全导航与探索。PSANE通过高斯过程回归学习通行性模型，在线估计并认证安全区域、识别探索边界，并将这些估计结果与反应式控制器集成以实现实时导航。边界选择被构建为多目标优化问题，平衡安全集扩展概率与目标导向成本，并通过帕累托最优边界集的标量化方法选定子目标。实验表明，PSANE仅依靠本体感知估计的通行性即可安全探索未知颗粒地形并抵达指定目标，其性能较基线方法有明显提升。

---

### 14. APPLV: Adaptive Planner Parameter Learning from Vision-Language-Action Model

- **作者**: Yuanjie Lu, Beichen Wang, Zhengqi Wu, Yang Li, Xiaomin Lin, Chengzhi Mao, Xuesu Xiao
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.08862v1)
- **发表日期**: 2026-03-09
- **匹配关键词**: robot navigation, vision-language-action model, VLA, autonomous navigation, vision-language-action, navigation
- **arXiv**: [2603.08862v1](http://arxiv.org/abs/2603.08862v1)
- **📥 PDF**: 已下载至本地 (`2603.08862v1_APPLV_Adaptive_Planner_Parameter_Learning_from_Vision-Language-Action_Model.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 在高度受限环境中实现自主导航对移动机器人而言仍具挑战性。经典导航方法虽能提供安全保障，但需针对特定环境进行参数调优；端到端学习虽绕过了参数调优环节，却在受限空间内难以实现精确控制。为此，近期机器人学习方法在保持经典系统安全性的同时实现了参数自动调优，但在泛化至未知环境方面仍面临挑战。最近，视觉-语言-动作模型通过利用基础模型的场景理解能力展现出潜力，但在导航任务中仍受限于精确控制与推理延迟问题。本文提出基于视觉-语言-动作模型的自适应规划器参数学习方法。与传统直接输出动作的视觉-语言-动作模型不同，该方法通过预训练的视觉-语言模型结合回归头来预测配置经典规划器的参数。我们开发了两种训练策略：基于采集导航轨迹的监督学习微调，以及进一步优化导航性能的强化学习微调。我们在模拟的自主机器人导航基准数据集和实体机器人实验中，对多种运动规划器进行了评估。结果表明，该方法在导航性能及对未知环境的泛化能力上均优于现有方法。

---

### 15. ReCoSplat: Autoregressive Feed-Forward Gaussian Splatting Using Render-and-Compare

- **作者**: Freeman Cheng, Botao Ye, Xueting Li, Junqi You, Fangneng Zhan, Ming-Hsuan Yang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.09968v1)
- **发表日期**: 2026-03-10
- **匹配关键词**: gaussian splatting
- **arXiv**: [2603.09968v1](http://arxiv.org/abs/2603.09968v1)
- **📥 PDF**: 已下载至本地 (`2603.09968v1_ReCoSplat_Autoregressive_Feed-Forward_Gaussian_Splatting_Using_Render-and-Compare.pdf`)
- **🔓 开源**: PROJECT_PAGE
- **中文摘要**: 在线新视角合成仍具挑战性，需要从连续且通常无位姿标注的观测中实现稳健的场景重建。我们提出ReCoSplat——一种支持含位姿或无位姿输入（无论是否包含相机内参）的自回归前馈高斯泼溅模型。虽然利用相机位姿组装局部高斯模型比规范空间预测更具扩展性，但这在训练中产生了矛盾：使用真实位姿能确保稳定性，但在推理阶段使用预测位姿时会导致分布失配。为解决此问题，我们引入了渲染比对模块。该模块从预测视角渲染当前重建结果，并与输入观测进行比对，从而提供稳定的条件信号以补偿位姿误差。为支持长序列处理，我们提出结合早期层截断与分块级选择性保留的混合键值缓存压缩策略，在超过100帧的场景中将键值缓存大小减少90%以上。ReCoSplat在分布内与分布外基准测试的不同输入设置下均实现了最先进的性能。代码与预训练模型将公开发布。项目页面详见 https://freemancheng.com/ReCoSplat 。

---

### 16. World2Mind: Cognition Toolkit for Allocentric Spatial Reasoning in Foundation Models

- **作者**: Shouwei Ruan, Bin Wang, Zhenyu Wu, Qihui Zhu, Yuxiang Zhang, Hang Su, Yubin Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.09774v1)
- **发表日期**: 2026-03-10
- **匹配关键词**: 3d reconstruction, 3D reconstruction
- **arXiv**: [2603.09774v1](http://arxiv.org/abs/2603.09774v1)
- **📥 PDF**: 已下载至本地 (`2603.09774v1_World2Mind_Cognition_Toolkit_for_Allocentric_Spatial_Reasoning_in_Foundation_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 实现稳健的空间推理仍是当前多模态基础模型面临的核心挑战。现有方法要么通过三维定位数据过度拟合统计捷径，要么局限于二维视觉感知，限制了空间推理的准确性及在未见场景中的泛化能力。受生物智能空间认知映射机制启发，我们提出无需训练的空间智能工具包World2Mind。其核心在于利用三维重建与实例分割模型构建结构化空间认知地图，使多模态基础模型能够主动获取目标地标与兴趣路径的针对性空间知识。为提供稳健的几何拓扑先验，World2Mind合成了以椭圆参数精确建模地标自上而下布局的自我中心空间树。为缓解三维重建固有的不精确性，我们设计了包含工具调用评估、模态解耦线索收集、几何语义交织推理的三阶段推理链。大量实验表明，World2Mind将GPT-5.2等前沿模型的性能提升5%~18%。令人惊讶的是，仅依靠自我中心空间树的结构化文本，纯文本基础模型即可执行复杂的三维空间推理，其性能接近先进多模态模型水平。

---

### 17. Let's Reward Step-by-Step: Step-Aware Contrastive Alignment for Vision-Language Navigation in Continuous Environments

- **作者**: Haoyuan Li, Rui Liu, Hehe Fan, Yi Yang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.09740v1)
- **发表日期**: 2026-03-10
- **匹配关键词**: navigation, VLN
- **arXiv**: [2603.09740v1](http://arxiv.org/abs/2603.09740v1)
- **📥 PDF**: 已下载至本地 (`2603.09740v1_Let's_Reward_Step-by-Step_Step-Aware_Contrastive_Alignment_for_Vision-Language_Navigation_in_Continu.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 在连续环境下的视觉语言导航任务要求智能体从长程人类交互中学习复杂推理。虽然多模态大语言模型推动了近期进展，但现有训练范式难以平衡泛化能力、错误恢复与训练稳定性。具体而言：(i) 基于监督微调的策略易受复合误差影响，难以从分布外状态中恢复；(ii) 强化微调方法（如GRPO）受限于稀疏结果奖励，其二元反馈机制无法为单步动作分配信用，导致失败主导批次中的梯度信号崩溃。为解决这些挑战，我们提出步感知对比对齐框架，该框架能从非完美轨迹中提取密集监督信号。其核心在于感知基底的步感知评估器，该组件通过逐步评估进展，将失败轨迹解构为有效前缀与精确分歧点。基于这些信号，场景条件分组构建机制动态分配批次至专用重采样与优化策略。在连续视觉语言导航基准测试上的大量实验表明，该框架实现了最先进的性能表现。

---

### 18. GSStream: 3D Gaussian Splatting based Volumetric Scene Streaming System

- **作者**: Zhiye Tang, Qiudan Zhang, Lei Zhang, Junhui Hou, You Yang, Xu Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.09718v1)
- **发表日期**: 2026-03-10
- **匹配关键词**: 3D gaussian splatting, gaussian splatting
- **arXiv**: [2603.09718v1](http://arxiv.org/abs/2603.09718v1)
- **📥 PDF**: 已下载至本地 (`2603.09718v1_GSStream_3D_Gaussian_Splatting_based_Volumetric_Scene_Streaming_System.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 近期，用于实时辐射场渲染的3D高斯泼溅（3DGS）技术彻底改变了体素场景表示领域，为用户带来沉浸式体验。但与此同时，该技术也产生了海量数据，对传输带宽提出了极高要求。前沿研究者尝试引入不同方法并构建多种3DGS变体以获得更紧凑的场景表示，但实现实时传输仍面临挑战。本文提出GSStream——一种支持3DGS数据格式的新型体素场景流式传输系统。具体而言，GSStream集成协同视口预测模块，通过从多用户历史数据及用户视口序列中学习协同先验与历史先验，更精准预测用户未来行为；同时采用基于深度强化学习（DRL）的码率自适应模块，应对码率自适应问题中状态与动作空间的多变性，实现高效的体素场景传输。此外，我们首次构建了面向体素场景的用户视口轨迹数据集，以支持系统训练与流式传输仿真。大量实验证明，我们提出的GSStream系统在视觉质量与网络利用率方面均优于现有代表性体素场景流式传输系统。演示视频：https://youtu.be/3WEe8PN8yvA。

---

### 19. ProGS: Towards Progressive Coding for 3D Gaussian Splatting

- **作者**: Zhiye Tang, Lingzhuo Liu, Shengjie Jiao, Qiudan Zhang, Junhui Hou, You Yang, Xu Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.09703v1)
- **发表日期**: 2026-03-10
- **匹配关键词**: 3D gaussian splatting, gaussian splatting
- **arXiv**: [2603.09703v1](http://arxiv.org/abs/2603.09703v1)
- **📥 PDF**: 已下载至本地 (`2603.09703v1_ProGS_Towards_Progressive_Coding_for_3D_Gaussian_Splatting.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 随着3D高斯泼溅（3DGS）技术的兴起，针对海量3DGS数据的高效压缩问题已涌现出许多开创性研究。3DGS通过可学习的3维高斯分布实现了对三维场景的高效可扩展表示，但其生成数据量庞大，给存储与传输带来了巨大挑战。现有方法因无法支持渐进式编码而受限，而这一特性在带宽多变的流媒体应用中至关重要。为突破此局限，本文提出一种创新方法，将3DGS数据组织为八叉树结构以实现高效渐进编码。所提出的ProGS是一种支持流式传输的编解码器，为3D高斯泼溅实现渐进式编码，显著提升了压缩效率与视觉保真度。该方法通过八叉树层级节点间的关联性，引入互信息增强机制以降低结构冗余。通过自适应调整八叉树结构并动态锚定节点，ProGS在保证渲染质量的同时实现了可扩展的数据压缩。相较于原始3DGS格式，ProGS实现了高达45倍的文件存储缩减，同时视觉性能提升超过10%。这表明ProGS能为网络条件多变的实时应用提供稳健解决方案。

---

## 📌 Poster

*其他相关研究*

---

### 1. BEACON: Language-Conditioned Navigation Affordance Prediction under Occlusion

- **作者**: Xinyu Gao, Gang Chen, Javier Alonso-Mora
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.09961v1)
- **发表日期**: 2026-03-10
- **匹配关键词**: affordance, navigation
- **arXiv**: [2603.09961v1](http://arxiv.org/abs/2603.09961v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://xin-yu-gao.github.io/beacon.
- **中文摘要**: 语言条件化局部导航要求机器人根据当前观察和开放词汇关系指令推断附近可通行的目标位置。现有视觉语言空间定位方法通常依赖视觉语言模型在图像空间进行推理，生成与可见像素绑定的二维预测。因此，这些方法难以推断被遮挡区域（通常由家具或移动行人造成）的目标位置。为解决这一问题，我们提出BEACON方法，该方法能在包含遮挡区域的有限局部范围内预测以机器人为中心的鸟瞰图可通行性热力图。给定指令和机器人周围四个方向的全景RGB-D观测数据，BEACON通过向视觉语言模型注入空间线索，并将其输出与深度衍生的鸟瞰图特征融合，从而预测鸟瞰图热力图。通过在Habitat模拟器中构建的遮挡感知数据集，我们进行了详细的实验分析，验证了鸟瞰图空间构建方式及各模块的设计选择。在目标位置被遮挡的验证子集上，我们的方法在测地线阈值平均准确率上比最先进的图像空间基线提升了22.74个百分点。项目页面为：https://xin-yu-gao.github.io/beacon。

---

