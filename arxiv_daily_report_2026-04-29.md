# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-04-29 08:02

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 5/20 篇提供

**🌟 Highlight**: 10 篇 | **📌 Poster**: 10 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. Learning Human-Intention Priors from Large-Scale Human Demonstrations for Robotic Manipulation

- **作者**: Yifan Xie, YuAn Wang, Guangyu Chen, Jinkun Liu, Yu Sun, Wenbo Ding
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.24681v1)
- **发表日期**: 2026-04-27
- **匹配关键词**: vision-language-action
- **arXiv**: [2604.24681v1](http://arxiv.org/abs/2604.24681v1)
- **📥 PDF**: 已下载至本地 (`2604.24681v1_Learning_Human-Intention_Priors_from_Large-Scale_Human_Demonstrations_for_Robotic_Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 人类视频包含丰富的操作先验知识，但将其用于机器人学习仍面临挑战，因为原始观测数据将场景理解、人体运动与具身化动作纠缠在一起。我们提出MoT-HRA，一种分层视觉-语言-动作框架，能从大规模人类示范中学习人类意图先验。首先构建HA-2.2M数据集，该数据集包含220万条动作-语言片段，通过手部中心过滤、空间重建、时间分割和语言对齐从异构人类视频中重建得到。基于该数据集，MoT-HRA将操作分解为三个耦合专家模块：视觉-语言专家预测与具身无关的3D轨迹，意图专家将MANO风格的手部运动建模为潜在人类运动先验，精细专家将意图感知表征映射为机器人动作块。共享注意力主干与只读键值传递机制使下游控制能利用人类先验，同时限制对上游表征的干扰。在手部运动生成、模拟操作和真实机器人任务上的实验表明，MoT-HRA在分布偏移下提升了运动合理性与鲁棒控制能力。

---

### 2. CF-VLA: Efficient Coarse-to-Fine Action Generation for Vision-Language-Action Policies

- **作者**: Fan Du, Feng Yan, Jianxiong Wu, Xinrun Xu, Weiye Zhang, Weinong Wang, Yu Guo, Bin Qian, Zhihai He
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.24622v1)
- **发表日期**: 2026-04-27
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2604.24622v1](http://arxiv.org/abs/2604.24622v1)
- **📥 PDF**: 已下载至本地 (`2604.24622v1_CF-VLA_Efficient_Coarse-to-Fine_Action_Generation_for_Vision-Language-Action_Policies.pdf`)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/EmbodiedAI-RoboTron/CF-VLA.
- **中文摘要**: 基于流的视觉-语言-动作（VLA）策略在动作生成中展现出强大的表达能力，但其存在根本性的效率缺陷：从无信息的高斯噪声中恢复动作结构需要多步推理，导致在实时约束下效率与质量难以平衡。我们通过重新思考生成式动作建模中起始点的作用来解决这一问题。不同于缩短采样轨迹，我们提出CF-VLA——一种由粗到精的两阶段框架，将动作生成重构为两个步骤：首先通过粗初始化步骤构建动作感知的起始点，随后通过单步局部精炼修正残差。具体而言，粗阶段学习终点速度的条件后验分布，将高斯噪声转化为结构化初始化，而精阶段从该初始化出发执行固定时长的精炼。为稳定训练，我们引入分步策略：先学习受控的粗预测器，再进行联合优化。在CALVIN和LIBERO上的实验表明，我们的方法在低NFE（函数评估次数）场景下建立了强大的效率-性能边界：它持续优于现有NFE=2方法，在多项指标上匹配或超越NFE=10的$π_{0.5}$基线，将动作采样延迟降低75.4%，并实现最佳平均真实机器人成功率83.0%，分别超过MIP 19.5个百分点和$π_{0.5}$ 4.0个百分点。这些结果表明，结构化的由粗到精生成能够同时实现强性能和高效推理。我们的代码已开源：https://github.com/EmbodiedAI-RoboTron/CF-VLA。

---

### 3. Characterizing Vision-Language-Action Models across XPUs: Constraints and Acceleration for On-Robot Deployment

- **作者**: Kaijun Zhou, Qiwei Chen, Da Peng, Zhiyang Li, Xijun Li, Jinyu Gu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.24447v1)
- **发表日期**: 2026-04-27
- **匹配关键词**: vision-language-action model, VLA, vision-language-action
- **arXiv**: [2604.24447v1](http://arxiv.org/abs/2604.24447v1)
- **📥 PDF**: 已下载至本地 (`2604.24447v1_Characterizing_Vision-Language-Action_Models_across_XPUs_Constraints_and_Acceleration_for_On-Robot_D.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型在通用机器人控制领域展现出巨大潜力，但其在机器人上的实际部署受限于严格成本与能耗预算下的实时推理瓶颈。现有评估大多基于桌面级GPU，掩盖了异构边缘加速器（GPU/XPU/NPU）带来的性能权衡与机遇。我们通过模型-硬件协同表征，对低成本VLA部署进行了系统性分析。首先，我们构建了跨加速器性能排行榜，并在成本、能耗、时间（CET）指标下评估模型-硬件组合，结果表明：尺寸适配的边缘设备在满足控制速率约束的同时，可比旗舰GPU更具成本与能效优势。其次，通过深度性能剖析，我们发现了一致的两阶段推理模式：计算密集的VLM骨干网络后接内存密集的动作专家模块，这种阶段性特征导致硬件利用率不足与效率低下。最后，基于上述发现，我们提出DP-Cache与V-AEFusion方法，分别减少扩散冗余并实现异步流水线并行，在GPU上获得最高2.9倍加速，在边缘NPU上获得6倍加速，且任务成功率仅轻微下降。示例排行榜网站见：https://vla-leaderboard-01.vercel.app/。

---

### 4. $M^2$-VLA: Boosting Vision-Language Models for Generalizable Manipulation via Layer Mixture and Meta-Skills

- **作者**: Siyao Xiao, Yuhong Zhang, Zhifang Liu, Zihan Gao, Jingye Zhang, Sinwai Choo, Dake Zhong, Mengzhe Wang, Xiao Lin, Xianfeng Zhou, Jia Jia, Haoqian Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.24182v1)
- **发表日期**: 2026-04-27
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2604.24182v1](http://arxiv.org/abs/2604.24182v1)
- **📥 PDF**: 已下载至本地 (`2604.24182v1_$M^2$-VLA_Boosting_Vision-Language_Models_for_Generalizable_Manipulation_via_Layer_Mixture_and_Meta-.pdf`)
- **🔓 开源**: CODE, MODEL
- **中文摘要**: 当前视觉-语言-动作（VLA）模型主要依赖端到端微调。尽管这种方法有效，但会损害视觉-语言模型（VLM）固有的泛化能力，并引发灾难性遗忘问题。为解决这些局限，我们提出$M^2$-VLA模型，证明通用型VLM可直接作为机器人操作任务的强大骨干网络。然而，弥合VLM高层语义理解与机器人控制精确需求之间的鸿沟仍是关键挑战。为此，我们引入分层混合（MoL）策略，从密集语义特征中选择性提取任务关键信息。此外，为在受限模型容量下实现高效轨迹学习，我们提出融合强归纳偏置的元技能模块（MSM）。在仿真与真实环境中的大量实验验证了本方法的有效性。进一步的泛化与消融研究证实了架构的零样本能力，并确认了各关键组件的贡献。我们的代码与预训练模型将公开发布。

---

### 5. AsyncShield: A Plug-and-Play Edge Adapter for Asynchronous Cloud-based VLA Navigation

- **作者**: Kai Yang, Zedong Chu, Yingnan Guo, Zhengbo Wang, Shichao Xie, Yanfen Shen, Xiaolong Wu, Xing Li, Mu Xu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.24086v1)
- **发表日期**: 2026-04-27
- **匹配关键词**: navigation, VLA, obstacle avoidance, vision-language-action
- **arXiv**: [2604.24086v1](http://arxiv.org/abs/2604.24086v1)
- **📥 PDF**: 已下载至本地 (`2604.24086v1_AsyncShield_A_Plug-and-Play_Edge_Adapter_for_Asynchronous_Cloud-based_VLA_Navigation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 尽管视觉-语言-动作（VLA）模型已被证明在机器人控制中具有强大的零样本泛化能力，但其庞大的参数量通常需要基于云端的部署。然而，云端部署会引入网络抖动和推理延迟，在连续位移的移动导航中可能导致严重的时空错位，使得过去自车帧中表达的过时意图在当前帧中可能产生空间错误，进而引发碰撞。为解决这一问题，我们提出AsyncShield，一种即插即用的异步控制框架。AsyncShield摒弃了传统的黑盒时间序列预测，转而采用确定性的物理白盒空间映射。通过维护一个时间位姿缓冲区并利用运动学变换，系统将时间延迟精确转换为空间位姿偏移，以恢复VLA的原始几何意图。为平衡意图恢复保真度与物理安全性，边缘适配被建模为约束马尔可夫决策过程（CMDP）。通过PPO-Lagrangian算法求解，强化学习适配器动态权衡跟踪VLA意图与响应高频激光雷达避障硬约束之间的关系。此外，得益于标准化的通用子目标接口、域随机化以及通过碰撞半径膨胀实现的感知层适配，AsyncShield可作为轻量级即插即用模块运行。仿真与真实世界实验表明，无需微调任何云端基础模型，该框架展现出零样本且鲁棒的泛化能力，有效提升了异步导航的成功率与物理安全性。

---

### 6. Bringing a Personal Point of View: Evaluating Dynamic 3D Gaussian Splatting for Egocentric Scene Reconstruction

- **作者**: Jan Warchocki, Xi Wang, Jonas Kulhanek, Jan van Gemert
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.23803v1)
- **发表日期**: 2026-04-26
- **匹配关键词**: 3D reconstruction, 3d reconstruction, 3D gaussian splatting, gaussian splatting
- **arXiv**: [2604.23803v1](http://arxiv.org/abs/2604.23803v1)
- **📥 PDF**: 已下载至本地 (`2604.23803v1_Bringing_a_Personal_Point_of_View_Evaluating_Dynamic_3D_Gaussian_Splatting_for_Egocentric_Scene_Reco.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 第一人称视角视频为理解人类感知与交互提供了独特视角，在增强现实、机器人技术和辅助技术领域具有日益重要的应用价值。然而，快速相机运动与复杂场景动态为该视角下的三维重建带来了重大挑战。尽管三维高斯泼溅（3DGS）已成为高效高质量新视角合成的先进方法，但针对单目视频动态场景重建的改进模型鲜少在自我中心视频上进行评估。现有模型能否泛化至该场景，或是否需要开发自我中心专用解决方案，目前尚不明确。本研究利用EgoExo4D数据集中的成对自我中心与外部视角记录，对动态单目3DGS模型在两类视频上的表现进行了评估。研究发现，自我中心视角的重建质量始终较低。分析表明，以峰值信噪比衡量的重建质量差异源于静态内容（而非动态内容）的重建效果。本研究的发现揭示了当前方法的局限性，推动了自我中心专用方法的研发，同时强调了分别评估视频静态与动态区域的重要性。

---

### 7. Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms

- **作者**: Qi Li, Bo Yin, Weiqi Huang, Ruhao Liu, Bojun Zou, Runpeng Yu, Jingwen Ye, Weihao Yu, Xinchao Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.23775v1)
- **发表日期**: 2026-04-26
- **匹配关键词**: vision-language-action model, VLA, vision-language-action
- **arXiv**: [2604.23775v1](http://arxiv.org/abs/2604.23775v1)
- **📥 PDF**: 已下载至本地 (`2604.23775v1_Vision-Language-Action_Safety_Threats,_Challenges,_Evaluations,_and_Mechanisms.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型正成为具身智能的统一基础。这一转变带来了新型安全挑战，源于VLA系统的具身特性，包括不可逆的物理后果、跨视觉、语言和状态的多模态攻击面、防御的实时延迟约束、长程轨迹中的错误传播以及数据供应链中的漏洞。然而，现有文献在机器人学习、对抗性机器学习、人工智能对齐和自主系统安全等领域仍呈碎片化分布。本综述提供了VLA模型安全的统一且最新的概述。我们沿两条并行的时序轴组织该领域：攻击时序（训练时与推理时）和防御时序（训练时与推理时），将每类威胁与其可被缓解的阶段相关联。我们首先定义VLA安全的范围，将其与纯文本大语言模型安全和经典机器人安全区分开来，并回顾VLA模型的基础，包括架构、训练范式和推理机制。随后，我们通过四个视角审视文献：攻击、防御、评估和部署。我们调查了训练时威胁（如数据投毒和后门）以及推理时攻击（包括对抗性补丁、跨模态扰动、语义越狱和冻结攻击）。我们回顾了训练时和运行时防御，分析了现有基准和指标，并讨论了六个部署领域的安全挑战。最后，我们强调了关键开放问题，包括具身轨迹的可认证鲁棒性、物理可实现的防御、安全感知训练、统一运行时安全架构以及标准化评估。

---

### 8. Unleashing the Agility of Wheeled-Legged Robots for High-Dynamic Reflexive Obstacle Evasion

- **作者**: Yongen Zhao, Zihao Xu, Wenzhi Lu, Zhen Chu, Ce Hao
- **单位**: School of Mechanical Engineering, Tianjin University, Tianjin, China; School of Computing, National University of Singapore, Singapore; School of Mechanical Engineering, Tianjin University, Tianjin, China...
- **发表日期**: 2026-04-26
- **匹配关键词**: obstacle avoidance
- **arXiv**: [2604.23761v1](http://arxiv.org/abs/2604.23761v1)
- **📥 PDF**: 已下载至本地 (`2604.23761v1_Unleashing_the_Agility_of_Wheeled-Legged_Robots_for_High-Dynamic_Reflexive_Obstacle_Evasion.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 轮腿机器人结合了轮式运动的高能效与腿式系统的地形适应性，使其成为在复杂动态环境中实现敏捷移动的理想平台。然而，由于此类平台的混合形态、模式耦合及非完整约束特性，实现针对快速移动障碍物的高动态反射式规避仍具挑战性。本文提出AWARE（自适应轮腿规避与反射式闪避）——一种用于轮腿机器人高动态避障的分层强化学习框架。该系统能自然展现出多样化的涌现步态与规避行为，包括前冲扑击与侧向闪避，从而利用机器人的混合形态增强其在高度动态威胁下的敏捷性。在Isaac Lab仿真环境及M20平台真实场景中的大量实验表明，AWARE在实现鲁棒敏捷避障的同时，展现出行为特征各异的规避策略。这些结果既验证了AWARE的实际有效性，也凸显了轮腿机器人固有的反射式敏捷性。

---

### 9. Move-Then-Operate: Behavioral Phasing for Human-Like Robotic Manipulation

- **作者**: Haoming Xu, Lei Lei, Jie Gu, Chu Tang, Jingmin Chen, Ruiqi Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.23620v1)
- **发表日期**: 2026-04-26
- **匹配关键词**: vision language action
- **arXiv**: [2604.23620v1](http://arxiv.org/abs/2604.23620v1)
- **📥 PDF**: 已下载至本地 (`2604.23620v1_Move-Then-Operate_Behavioral_Phasing_for_Human-Like_Robotic_Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出“先移动后操作”（Move-Then-Operate）这一视觉-语言-动作框架，将机器人操作显式解耦为两个不同的行为阶段：粗定位移动（move）与接触关键交互（operate）。与将异质模式混为一谈的整体式策略不同，我们的架构采用由可学习阶段选择器路由的双专家策略，引入结构归纳偏置以隔离各阶段特有的动力学特征。阶段标签通过基于多模态大语言模型（MLLM）的流水线自动生成，该流水线以末端执行器速度、子任务分解等轻量级上下文线索为条件，确保与人类运动模式对齐。在RoboTwin2基准测试中，我们的方法平均成功率达68.9%，比整体式π₀基线高出24%。其性能与使用10倍数据训练的模型相当或更优，且训练步骤减少40%即可达到峰值性能，这表明移动与操作阶段的架构解耦是掌握高精度操作任务的高效策略。

---

### 10. FreqCache: Accelerating Embodied VLN Models with Adaptive Frequency-Guided Token Caching

- **作者**: Zihao Zheng, Xingyue Zhou, Zhihao Mao, Songyu Sun, Lingyue Zhang, Yulong Ao, Yupu Feng, Qiongqiong Zhang, Yonghua Lin, Xiang Chen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.24391v1)
- **发表日期**: 2026-04-27
- **匹配关键词**: navigation, VLN
- **arXiv**: [2604.24391v1](http://arxiv.org/abs/2604.24391v1)
- **📥 PDF**: 已下载至本地 (`2604.24391v1_FreqCache_Accelerating_Embodied_VLN_Models_with_Adaptive_Frequency-Guided_Token_Caching.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-导航（VLN）模型展现出卓越的导航精度，但计算开销较高。令牌缓存作为一种无需重新训练的有前景策略，通过复用令牌计算结果来降低计算成本；然而，现有令牌缓存方法依赖视觉域方法进行可缓存令牌选择，在适配VLN模型时面临挑战：1）当视点发生迁移时，视觉域方法失效；2）缺乏辅助算法时，视觉域方法会忽略关键边缘信息；3）视觉域方法忽视场景的时间变化特性，且缺乏缓存预算的可调节性。本文通过详细分析发现，这些挑战的影响在频域中具有不变性和可分析性。基于此，我们提出频域引导的令牌缓存框架FreqCache。利用频域的固有特性，FreqCache实现了最优令牌缓存的建立、刷新与自适应调整。实验表明，FreqCache在可忽略的开销下实现1.59倍加速，验证了频域方法在VLN令牌缓存中的有效性。

---

## 📌 Poster

*其他相关研究*

---

### 1. Passage-Aware Structural Mapping for RGB-D Visual SLAM

- **作者**: Ali Tourani, Miguel Fernandez-Cortizas, Saad Ejaz, David Pérez Saura, Asier Bikandi-Noya, Jose Luis Sanchez-Lopez, Holger Voos
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.24707v1)
- **发表日期**: 2026-04-27
- **匹配关键词**: navigation, robot navigation, scene graph
- **arXiv**: [2604.24707v1](http://arxiv.org/abs/2604.24707v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: GITHUB, CODE
  - 链接：https://github.com/snt-arg/visual_sgraphs/tree/doorway_integration.
- **中文摘要**: 门廊与通道是室内机器人导航的关键结构元素，但在现代视觉SLAM（VSLAM）框架中尚未得到充分探索。本文提出一种面向RGB-D VSLAM的通道感知结构建图方法，通过融合几何、语义与拓扑线索联合检测门与可通行开口。门被建模为嵌入墙体的平面实体，并根据其与支撑墙体的共面性分类为可通行或不可通行。通道的推断通过两种互补策略实现：基于连续关键帧间相机-墙体交互积累的通行证据，以及基于已建图墙体几何不连续性的开口几何验证。该方法作为概念验证集成至vS-Graphs中，通过通道层级抽象丰富其场景图并改进房间连通性建模。在室内办公序列上的定性评估展示了可靠的门口检测能力，该框架为在BIM赋能的VSLAM中利用这些元素奠定了基础。源代码已开源：https://github.com/snt-arg/visual_sgraphs/tree/doorway_integration。

---

### 2. Sliding Mode Control for Safe Trajectory Tracking with Moving Obstacles Avoidance: Experimental Validation on Planar Robots

- **作者**: Shubham Sawarkar, P Sangeerth, S Saharsh, Pushpak Jagtap
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.24518v1)
- **发表日期**: 2026-04-27
- **匹配关键词**: obstacle avoidance
- **arXiv**: [2604.24518v1](http://arxiv.org/abs/2604.24518v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 本文提出了一种适用于多种移动机器人的统一控制框架，用于实现鲁棒轨迹跟踪与移动障碍物规避。通过构建广义运动学变换，我们将不同车辆动力学模型转化为严格反馈形式，从而便于设计滑模控制策略以实现精确且鲁棒的参考轨迹跟踪。为确保动态环境中的操作安全性，该跟踪控制器与基于碰撞锥控制障碍函数的安全滤波器相结合。所提出的架构能够在存在外部扰动的情况下保证渐近跟踪性能，同时严格满足避碰约束。本研究的创新之处在于首次为阿克曼转向等地面机器人设计了滑模控制器。通过数值仿真以及在阿克曼转向车辆、差速驱动机器人和四旋翼无人机三种不同平台上的大量真实实验，验证了该方法的有效性与通用性。实验视频可参见https://youtu.be/dWcxwum96vk。

---

### 3. Guiding Vector Field Generation via Score-based Diffusion Model

- **作者**: Zirui Chen, Shiliang Guo, Shiyu Zhao
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.24487v1)
- **发表日期**: 2026-04-27
- **匹配关键词**: navigation
- **arXiv**: [2604.24487v1](http://arxiv.org/abs/2604.24487v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: GITHUB
  - 链接：https://github.com/czr-gif/Guiding-Vector-Field-Generation-via-Score-based-Diffusion-Model.
- **中文摘要**: 引导向量场（GVFs）是机器人路径跟踪的强大工具。然而，经典方法假设路径为平滑有序曲线，当路径无序、多分支或由概率模型生成时便会失效。我们提出统一框架——分数诱导引导向量场（SGVF），利用基于分数的生成建模直接从数据分布构建向量场。SGVF通过单位范数、正交性和方向一致性损失从点云中学习切向量场，确保几何保真度与控制可行性。该方法摆脱了对特定路径分割的依赖，能够引导复杂拓扑结构（如分支和伪流形）。研究建立了扩散模型中分数消失与GVF奇点之间的对应关系，并揭示了在尖锐路径曲率附近的表征能力。平面环境中的机器人导航实验表明，SGVF在经典GVF失效的场景下仍能实现可靠路径跟踪，凸显其作为生成建模与几何控制桥梁的潜力。代码与实验视频详见https://github.com/czr-gif/Guiding-Vector-Field-Generation-via-Score-based-Diffusion-Model。

---

### 4. IntentVLM: Open-Vocabulary Intention Recognition through Forward-Inverse Modeling with Video-Language Models

- **作者**: Hamed Rahimi, Clemence Grislain, Adrien Jacquet Cretides, Olivier Sigaud, Mohamed Chetouani
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.24002v1)
- **发表日期**: 2026-04-27
- **匹配关键词**: human-robot interaction
- **arXiv**: [2604.24002v1](http://arxiv.org/abs/2604.24002v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 提升人机交互的有效性要求社交机器人通过稳健的意图理解来准确推断人类目标。这一挑战在多模态环境中尤为关键，因为智能体必须整合包括文本和视觉线索在内的异构信号，以形成对用户意图的连贯解读。本文提出IntentVLM，一种新颖的两阶段视频-语言框架，专为开放词汇的人类意图识别而设计。该方法受认知科学中的前向-逆向建模启发，将意图理解分解为目标候选生成，随后通过选择进行结构化推理，有效减少潜在推理中的幻觉现象。在IntentQA和Inst-IT Bench数据集上的评估显示，IntentVLM实现了高达80%的准确率，显著超越基线性能30%，并达到人类水平。我们的研究结果表明，这种结构化推理方法在不发生灾难性遗忘的情况下增强了开放词汇的意图理解，为以人为中心的机器人技术提供了稳健基础。

---

### 5. Multi-Robot Motions in Milliseconds: Vector-Accelerated Primitives for Sampling-Based Planning

- **作者**: James D. Motes, Marco Morales, Nancy M. Amato
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.23960v1)
- **发表日期**: 2026-04-27
- **匹配关键词**: motion planning
- **arXiv**: [2604.23960v1](http://arxiv.org/abs/2604.23960v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 本文将近期提出的向量加速运动规划（VAMP）框架扩展至多机器人运动规划（MRMP）领域。我们开发了两种向量加速原语——多机器人运动验证（MotVal）与首冲突检测（FFC），通过在多机器人域中利用SIMD并行计算实现加速。在纯多机器人运动验证测试中，该方法实现了超过1100倍的验证速度提升。此外，我们对一组具有代表性的MRMP算法进行改进，使其能够运用这些新原语。在包含机械臂、刚体及异构机器人团队的场景中，研究了各算法的相对加速比，部分实例可在毫秒级内生成多机器人解决方案，且多数情况下规划速度提升超过850倍。

---

### 6. Decentralized Heterogeneous Multi-Robot Collaborative Exploration for Indoor and Outdoor 3D Environments

- **作者**: Yuxiang Li, Kun Chen, Jiancheng Wang, Shihao Fang, Haoyao Chen, Yunhui Liu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.23693v1)
- **发表日期**: 2026-04-26
- **匹配关键词**: exploration
- **arXiv**: [2604.23693v1](http://arxiv.org/abs/2604.23693v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 异构多机器人系统在复杂环境中具有显著的适应性，但如何实现充分挖掘机器人潜能的协同合作仍是核心挑战。本文提出一种面向异构多机器人系统的分布式协同框架，用于自主探索室内外三维环境。首先，设计融合地形与观测指标的基础感知地图，并开发改进的超体素分割方法以简化地图结构，形成支持轻量化通信的高层表征。其次，对异构机器人的遍历与观测能力进行建模，以评估由不完整超体素衍生的任务视角需求。这些任务视角按需求分组并聚类以简化分配。随后，将视角-聚类分配问题建模为异构多车场多旅行商问题（HMDMTSP），该模型融合了视角-聚类需求与机器人能力间的约束。通过改进遗传算法高效求解该问题，同时确保全局一致性。基于分配结果，消除聚类内的冗余视角以优化探索路径，最终解决机器人运动路径间的冲突。在杂乱室内外环境中的仿真与实地实验表明，本方法能有效协调异构机器人间的探索任务，相较于现有先进方法，实现了更优的探索效率与通信资源节省。

---

### 7. Safe Navigation in Unknown and Cluttered Environments via Direction-Aware Convex Free-Region Generation

- **作者**: Zhicheng Song, Yongjian Li, Kai Chen, Yulin Li, Fan Shi, Jun Ma
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.23648v1)
- **发表日期**: 2026-04-26
- **匹配关键词**: navigation, robot navigation
- **arXiv**: [2604.23648v1](http://arxiv.org/abs/2604.23648v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: GITHUB, CODE
  - 链接：https://github.com/ZhichengSong6/FRGraph.
- **中文摘要**: 凸自由区域为未知杂乱环境中的机器人导航提供了一种结构化且利于优化的无碰撞空间表示。然而，现有方法通常仅依据周围障碍物几何形状来扩大局部无碰撞区域。在杂乱环境中，此类策略可能无法生成既能容纳机器人几何形状、又能沿候选运动方向保持可通行延伸的区域，从而限制下游轨迹规划，尤其在狭窄通道中。即便获得此类区域，安全运动生成仍具挑战性——当显式建模机器人几何形状时，离散化轨迹采样点的安全检查无法保证连续无碰撞运动。为解决上述问题，我们提出一种导航框架，该框架将候选运动方向与机器人几何形状联合纳入凸自由区域生成过程，并通过连续安全轨迹生成实现持续无碰撞运动。在每个区域内，框架执行几何感知的目标位姿选择与轨迹生成，结合基于Lipschitz条件的连续安全认证与局部优化。生成的自由区域与候选运动通过区域图结构维护，以支持增量式规划。在杂乱二维导航场景中的量化结果表明，所提方法生成的自由区域更契合下游轨迹规划需求，可实现可靠的无碰撞导航；同时，四足机器人与无人机上的三维及真实世界实验验证了该框架的扩展性与实际应用价值。开源项目地址：https://github.com/ZhichengSong6/FRGraph。

---

### 8. Learning to Rotate: Temporal and Semantic Rotary Encoding for Sequential Modeling

- **作者**: Hailing Cheng, Daqi Sun, Xinyu Lu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.24717v1)
- **发表日期**: 2026-04-27
- **匹配关键词**: exploration
- **arXiv**: [2604.24717v1](http://arxiv.org/abs/2604.24717v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 每个Transformer架构都投入了巨大的容量，用于在语义嵌入空间中学习丰富的表征——然而，由旋转位置编码（RoPE）驱动的旋转流形，却一直被视为一个固定的、手工设计的结构，其中仅填充了离散的序数索引。我们认为，这个旋转空间是注意力机制中一个很大程度上被忽视的、用于表达能力的第二维度，对其系统性的探索可能为基于注意力的架构打开一扇新的大门。与复数的类比具有启发性：正如引入虚数轴——与实数轴正交且独立——曾解锁了曾被认为不可能的代数结构一样，将旋转流形视为一个可学习的、受信号调节的空间，为注意力机制开辟了一个正交的自由度。在此框架下，词元嵌入编码了表征的语义（实）分量——即词元的意义——而旋转则编码了其动态（虚）分量——即该词元如何随时间、位置和上下文与其他每个词元相关联。

我们提出了SIREN-RoPE，作为这一思想的具体实现，它通过一个双分支正弦表示网络（SIREN），用异质信号——连续时间戳、周期性时间模式和分类元数据——来填充旋转维度。作为概念验证，我们使用生成式推荐器作为排序模型，在一个来自主要社交网络的生产级新闻推送数据集上进行评估，结果表明，激活这一隐藏维度能够在校准和排序目标上带来一致的改进，且计算开销可忽略不计。我们邀请学界将旋转空间视为一个尚未开发的轴，而非一个已解决的、细节性的位置编码问题；其丰富的结构可能对注意力机制产生的影响，正如虚数单位对代数产生的影响一样深远。

---

### 9. Scalable Hyperparameter-Divergent Ensemble Training with Automatic Learning Rate Exploration for Large Models

- **作者**: Hailing Cheng, Tao Huang, Chen Zhu, Antonio Alonso
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.24708v1)
- **发表日期**: 2026-04-27
- **匹配关键词**: exploration
- **arXiv**: [2604.24708v1](http://arxiv.org/abs/2604.24708v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 采用数据并行随机梯度下降训练大型神经网络时，会分配N个GPU副本计算几乎相同的更新——这种实践在训练过程中完全未探索学习率配置的丰富空间。我们提出超参数发散集成训练方法(HDET)，该方法重新利用这些副本以可忽略的通信开销同时进行学习率探索。HDET采用交替阶段运行：发散阶段中副本在结构化对称学习率分布下独立训练，收敛阶段中每T步通过AllReduce对所有副本参数进行平均。基于此集成基础，我们进一步提出自动学习率控制器，将副本间相对训练损失作为性能信号，通过基于动量的无梯度元更新将共享基础调度向更高性能配置调整。该组合方法产生自适应学习率调度，无需额外超参数扫描或训练预算即可提升优化质量与泛化能力。

关键的是，该框架可推广至学习率之外的超参数：任何不改变模型架构的标量超参数（如丢弃率、注意力缩放温度或权重衰减系数）均可通过相同的发散/收敛协议在副本间探索，副本间损失差异作为零阶超梯度引导搜索方向。HDET作为PyTorch的OneCycleLR调度器的即插即用替代方案实现，无需修改模型架构、优化器或数据流水线。

---

### 10. Towards Lawful Autonomous Driving: Deriving Scenario-Aware Driving Requirements from Traffic Laws and Regulations

- **作者**: Bowen Jian, Rongjie Yu, Hong Wang, Liqiang Wang, Zihang Zou
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.24562v1)
- **发表日期**: 2026-04-27
- **匹配关键词**: navigation
- **arXiv**: [2604.24562v1](http://arxiv.org/abs/2604.24562v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 遵守交通法律法规是人类驾驶员的基本要求，但自动驾驶汽车（AVs）在多种现实场景中可能违反这些要求。为将法律合规性编码到自动驾驶系统中，传统方法使用形式化逻辑语言明确指定行为约束，但这一过程劳动密集、难以扩展且维护成本高昂。随着人工智能的最新进展，利用大语言模型（LLMs）从交通法律法规中推导法律要求成为可行方案。然而，由于缺乏对结构化交通场景的显式锚定与推理，LLMs常检索到无关条款或遗漏适用条款，导致要求不精确。为解决此问题，我们提出了一种新型流水线，通过编码层级语义的节点锚点，将LLM推理锚定在交通场景分类体系中。基于中国交通法规与OnSite数据集（5,897个场景），我们的方法将法律-场景匹配率提升29.1%，并将推导出的强制性要求与禁止性要求的准确率分别提升36.9%和38.2%。我们进一步通过构建自动驾驶导航的法律合规层，并开发用于现场测试的车载实时合规监控器，验证了其实用性，为未来自动驾驶汽车的开发、部署与监管监督奠定了坚实基础。

---

