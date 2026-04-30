# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-04-30 08:03

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 8/20 篇提供

**🌟 Highlight**: 10 篇 | **📌 Poster**: 10 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. KinDER: A Physical Reasoning Benchmark for Robot Learning and Planning

- **作者**: Yixuan Huang, Bowen Li, Vaibhav Saxena, Yichao Liang, Utkarsh Aashu Mishra, Liang Ji, Lihan Zha, Jimmy Wu, Nishanth Kumar, Sebastian Scherer, Danfei Xu, Tom Silver ⭐
  - **高亮作者**: Sebastian Scherer
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.25788v1)
- **发表日期**: 2026-04-28
- **匹配关键词**: mobile manipulator, object manipulation, tool use, motion planning
- **arXiv**: [2604.25788v1](http://arxiv.org/abs/2604.25788v1)
- **📥 PDF**: 已下载至本地 (`2604.25788v1_KinDER_A_Physical_Reasoning_Benchmark_for_Robot_Learning_and_Planning.pdf`)
- **🔓 开源**: CODE
- **中文摘要**: 与物理世界交互的机器人系统必须推理其自身具身形态、环境及当前任务所施加的运动学和动力学约束。我们提出KinDER——面向运动学与动力学具身推理的基准测试，针对机器人学习与规划中的物理推理挑战。KinDER包含25个程序化生成的环境、一个兼容Gymnasium的Python库（含参数化技能与演示数据），以及一个标准化评估套件（涵盖任务与运动规划、模仿学习、强化学习及基于基础模型的方法等13个基线实现）。这些环境被设计用于隔离五大核心物理推理挑战：基础空间关系、非抓取式多物体操作、工具使用、组合几何约束及动力学约束，同时排除感知、语言理解及特定应用复杂性的干扰。实证评估表明，现有方法难以解决多数环境中的问题，揭示了当前物理推理方法的显著缺陷。我们还在移动操作平台上进行了"仿真-真实-仿真"实验，以评估仿真与现实物理交互之间的对应关系。KinDER完全开源，旨在促进不同范式间的系统性比较，推动机器人物理推理研究的发展。网站与代码：https://prpl-group.com/kinder-site/

---

### 2. GS-Playground: A High-Throughput Photorealistic Simulator for Vision-Informed Robot Learning

- **作者**: Yufei Jia, Heng Zhang, Ziheng Zhang, Junzhe Wu, Mingrui Yu, Zifan Wang, Dixuan Jiang, Zheng Li, Chenyu Cao, Zhuoyuan Yu, Xun Yang, Haizhou Ge, Yuchi Zhang, Jiayuan Zhang, Zhenbiao Huang, Tianle Liu, Shenyu Chen, Jiacheng Wang, Bin Xie, Xuran Yao, Xiwa Deng, Guangyu Wang, Jinzhi Zhang, Lei Hao, Zhixing Chen, Yuxiang Chen, Anqi Wang, Hongyun Tian, Yiyi Yan, Zhanxiang Cao, Yizhou Jiang, Hanyang Shao, Yue Li, Lu Shi, Bokui Chen, Wei Sui, Hanqing Cui, Yusen Qin, Ruqi Huang, Lei Han, Tiancai Wang, Guyue Zhou
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.25459v1)
- **发表日期**: 2026-04-28
- **匹配关键词**: navigation, 3D gaussian splatting, gaussian splatting, contact-rich manipulation
- **arXiv**: [2604.25459v1](http://arxiv.org/abs/2604.25459v1)
- **📥 PDF**: 已下载至本地 (`2604.25459v1_GS-Playground_A_High-Throughput_Photorealistic_Simulator_for_Vision-Informed_Robot_Learning.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 具身人工智能研究正经历向视觉中心感知范式的转变。虽然大规模并行模拟器已在基于本体感知的运动控制领域催生突破性进展，但由于大规模逼真渲染带来的高昂计算开销，这类模拟器在视觉相关任务中的潜力仍未得到充分开发。此外，可模拟三维资产的创建仍高度依赖劳动密集型手工建模，而显著的模拟-现实物理差距阻碍了接触密集型操作策略的迁移。为突破这些瓶颈，我们提出GS-Playground——一个旨在加速端到端感知学习的多模态仿真框架。我们开发了新型高性能并行物理引擎，专门设计用于与批量三维高斯泼溅（3DGS）渲染管线集成，确保高保真同步。该系统在640x480分辨率下实现了每秒10^4帧的突破性吞吐量，显著降低了大规模视觉强化学习的门槛。同时，我们引入自动化Real2Sim工作流，可重建照片级逼真、物理一致且内存高效的环境，简化复杂可模拟场景的生成流程。在运动控制、导航与操作任务上的大量实验表明，GS-Playground有效弥合了不同具身任务中的感知与物理差距。项目主页：https://gsplayground.github.io。

---

### 3. Libra-VLA: Achieving Learning Equilibrium via Asynchronous Coarse-to-Fine Dual-System

- **作者**: Yifei Wei, Linqing Zhong, Yi Liu, Yuxiang Lu, Xindong He, Maoqing Yao, Guanghui Ren
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.24921v1)
- **发表日期**: 2026-04-27
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2604.24921v1](http://arxiv.org/abs/2604.24921v1)
- **📥 PDF**: 已下载至本地 (`2604.24921v1_Libra-VLA_Achieving_Learning_Equilibrium_via_Asynchronous_Coarse-to-Fine_Dual-System.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型通过将高层语义指令转化为可执行的物理动作，成为通用机器人操作领域极具前景的范式。然而，现有方法通常采用单一生成范式，以扁平化、非层次化的方式直接将视觉-语言特征映射为高频电机指令。这种策略忽视了机器人操作固有的层次结构——复杂动作本可在混合动作空间中自然建模，分解为离散的宏观方向到达与连续的微观位姿对齐，这严重扩大了语义-执行鸿沟，并为将高层语义映射到连续动作带来了沉重的表征负担。为此，我们提出Libra-VLA——一种新颖的由粗到精双系统VLA架构。我们明确地将学习复杂度解耦为从粗到精的层次结构以实现训练均衡，同时利用这种结构模块化特性实现异步执行策略。语义规划器预测捕获宏观方向意图的离散动作标记，而动作精化器则以粗粒度意图为条件生成用于精确对齐的高频连续动作。关键的是，我们的实证分析表明：性能相对于动作分解粒度呈现倒U型曲线，恰好在两个子系统间学习难度达到平衡时达到峰值。借助异步设计，我们的方法为开放世界操作提供了可扩展、鲁棒且响应迅速的解决方案。

---

### 4. asRoBallet: Closing the Sim2Real Gap via Friction-Aware Reinforcement Learning for Underactuated Spherical Dynamics

- **作者**: Fang Wan, Guangyi Huang, Tianyu Wu, Zishang Zhang, Bangchao Huang, Haoran Sun, Mingdong Chen, Chaoyang Song
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.24916v1)
- **发表日期**: 2026-04-27
- **匹配关键词**: exploration
- **arXiv**: [2604.24916v1](http://arxiv.org/abs/2604.24916v1)
- **📥 PDF**: 已下载至本地 (`2604.24916v1_asRoBallet_Closing_the_Sim2Real_Gap_via_Friction-Aware_Reinforcement_Learning_for_Underactuated_Sphe.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出asRoBallet——据我们所知，这是首个成功将强化学习（RL）部署于仿人轮腿机器人（ballbot）硬件平台的案例。传统上，轮腿机器人作为欠驱动与非完整约束控制的经典基准，其轮-球-地面交互的复杂摩擦模型存在显著的现实差距。现有文献虽已展示通过LQR和MPC实现三维平衡控制，但基于RL的仿人轮腿机器人向实际硬件迁移仍受限于接触建模、执行器延迟与抖动、安全硬件探索等关键缺口。本研究构建了高保真MuJoCo仿真环境，显式建模ETH型全向轮离散滚子力学机制，从而捕获此前被忽略的寄生振动与接触不连续性。我们进一步开发了摩擦感知强化学习框架，通过掌握轮-球界面与球-地面界面的耦合滚动摩擦、侧向摩擦及扭转摩擦通道，实现零样本仿真到现实迁移。通过减法重构设计，我们将过约束四足机器人的关键组件重新部署至全新结构框架，以低成本构建了稳健的研究平台asRoBallet。同时开发的通用iOS生态系统将消费电子产品转化为低延迟交互界面，使单操作员可通过直观自然动作编排富有表现力的仿人运动。

---

### 5. MotionBricks: Scalable Real-Time Motions with Modular Latent Generative Model and Smart Primitives

- **作者**: Tingwu Wang, Olivier Dionne, Michael De Ruyter, David Minor, Davis Rempe, Kaifeng Zhao, Mathis Petrovich, Ye Yuan, Chenran Li, Zhengyi Luo, Brian Robison, Xavier Blackwell, Bernardo Antoniazzi, Xue Bin Peng, Yuke Zhu, Simon Yuen ⭐
  - **高亮作者**: Yuke Zhu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.24833v1)
- **发表日期**: 2026-04-27
- **匹配关键词**: navigation
- **arXiv**: [2604.24833v1](http://arxiv.org/abs/2604.24833v1)
- **📥 PDF**: 已下载至本地 (`2604.24833v1_MotionBricks_Scalable_Real-Time_Motions_with_Modular_Latent_Generative_Model_and_Smart_Primitives.pdf`)
- **🔓 开源**: CODE
- **中文摘要**: 尽管生成式运动合成领域取得了变革性进展，实时交互式运动控制仍主要由传统技术主导。本研究识别出连接研究与产业应用的两大关键挑战：1）实时可扩展性：产业应用要求实时生成海量运动技能库，而生成式方法在实时计算约束下会出现显著的质量退化与可扩展性下降；2）集成性：产业应用需要包含速度指令、风格选择及精确关键帧的细粒度多模态控制，现有文本或标签驱动模型难以满足这一需求。为突破这些限制，我们提出MotionBricks——一个具备双重解决方案的大规模实时生成框架。首先，我们构建了专为稳健实时运动生成设计的大规模模块化隐式生成主干网络，通过单一模型有效建模超过35万个运动片段的数据集。其次，我们引入智能基元，为导航与物体交互的创作提供统一、稳健且直观的接口。应用设计可像搭积木般即插即用，无需专业动画知识。定量实验表明，MotionBricks在多种规模的开源与专有数据集上均达到业界领先的运动质量，同时实现15,000 FPS实时吞吐量与2毫秒延迟。我们通过完整的工业级动画演示验证了MotionBricks的灵活性与鲁棒性，该演示采用统一模型覆盖多种风格的导航与物体场景交互。为展示框架超越动画领域的应用潜力，我们将MotionBricks部署于宇树G1人形机器人，验证其在实时机器人控制中的灵活性与泛化能力。

---

### 6. Learning Human-Intention Priors from Large-Scale Human Demonstrations for Robotic Manipulation

- **作者**: Yifan Xie, YuAn Wang, Guangyu Chen, Jinkun Liu, Yu Sun, Wenbo Ding
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.24681v1)
- **发表日期**: 2026-04-27
- **匹配关键词**: vision-language-action
- **arXiv**: [2604.24681v1](http://arxiv.org/abs/2604.24681v1)
- **📥 PDF**: 已下载至本地 (`2604.24681v1_Learning_Human-Intention_Priors_from_Large-Scale_Human_Demonstrations_for_Robotic_Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 人类视频包含丰富的操作先验知识，但将其用于机器人学习仍面临挑战，因为原始观测数据混杂了场景理解、人体运动与具身化动作。我们提出MoT-HRA——一种分层视觉-语言-动作框架，能从大规模人类示范中学习人类意图先验。首先构建HA-2.2M数据集，该数据集包含220万条动作-语言片段，通过手部中心过滤、空间重建、时间分割和语言对齐，从异构人类视频中重建而成。基于该数据集，MoT-HRA将操作分解为三个耦合专家模块：视觉-语言专家预测与具身无关的3D轨迹，意图专家将MANO风格手部运动建模为潜在人类运动先验，精细专家将意图感知表征映射为机器人动作块。共享注意力主干与只读键值传输机制使下游控制能利用人类先验，同时限制对上游表征的干扰。在手部运动生成、模拟操作和真实机器人任务上的实验表明，MoT-HRA在分布偏移下提升了运动合理性与鲁棒控制能力。

---

### 7. CF-VLA: Efficient Coarse-to-Fine Action Generation for Vision-Language-Action Policies

- **作者**: Fan Du, Feng Yan, Jianxiong Wu, Xinrun Xu, Weiye Zhang, Weinong Wang, Yu Guo, Bin Qian, Zhihai He, Fei Wang, Heng Yang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.24622v2)
- **发表日期**: 2026-04-27
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2604.24622v2](http://arxiv.org/abs/2604.24622v2)
- **📥 PDF**: 已下载至本地 (`2604.24622v2_CF-VLA_Efficient_Coarse-to-Fine_Action_Generation_for_Vision-Language-Action_Policies.pdf`)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/EmbodiedAI-RoboTron/CF-VLA.
- **中文摘要**: 基于流的视觉-语言-动作（VLA）策略在动作生成中展现出强大的表达能力，但其存在根本性的效率问题：从无信息的高斯噪声中恢复动作结构需要多步推理，导致在实时约束下效率与质量难以平衡。我们通过重新审视生成式动作建模中起始点的作用来解决这一问题。不同于缩短采样轨迹，我们提出CF-VLA——一种由粗到精的两阶段框架，将动作生成重构为两个步骤：首先通过粗初始化步骤构建一个感知动作的起始点，随后通过单步局部精化修正残差。具体而言，粗阶段学习终点速度的条件后验分布，将高斯噪声转化为结构化初始化；精阶段则从该初始化出发进行固定步长的精化。为稳定训练，我们引入分步策略：先学习受控的粗预测器，再进行联合优化。在CALVIN和LIBERO上的实验表明，我们的方法在低NFE（函数评估次数）场景下建立了强大的效率-性能边界：它持续优于现有NFE=2的方法，在多项指标上匹配或超越NFE=10的$π_{0.5}$基线，将动作采样延迟降低75.4%，并达到最佳真实机器人平均成功率83.0%，分别超过MIP 19.5个百分点和$π_{0.5}$ 4.0个百分点。这些结果表明，结构化的由粗到精生成能够同时实现强性能与高效推理。我们的代码开源在https://github.com/EmbodiedAI-RoboTron/CF-VLA。

---

### 8. Characterizing Vision-Language-Action Models across XPUs: Constraints and Acceleration for On-Robot Deployment

- **作者**: Kaijun Zhou, Qiwei Chen, Da Peng, Zhiyang Li, Xijun Li, Jinyu Gu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.24447v1)
- **发表日期**: 2026-04-27
- **匹配关键词**: VLA, vision-language-action model, vision-language-action
- **arXiv**: [2604.24447v1](http://arxiv.org/abs/2604.24447v1)
- **📥 PDF**: 已下载至本地 (`2604.24447v1_Characterizing_Vision-Language-Action_Models_across_XPUs_Constraints_and_Acceleration_for_On-Robot_D.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型在通用机器人控制领域展现出巨大潜力，但其在机器人本体部署时受限于严格成本与能耗预算下的实时推理瓶颈。现有评估多基于桌面级GPU，掩盖了异构边缘加速器（GPU/XPU/NPU）带来的性能权衡与机遇。我们通过模型-硬件协同表征，对低成本VLA部署展开系统性分析。首先，构建跨加速器排行榜，在成本-能耗-时间（CET）框架下评估模型-硬件组合，证明尺寸适配的边缘设备可在满足控制速率约束的同时，比旗舰级GPU更具成本与能效优势。其次，通过深度性能剖析，揭示出一致的两阶段推理模式：计算密集的VLM主干网络后接存储密集的动作专家模块，这种阶段依赖性导致资源利用率不足与硬件效率低下。最后，基于上述发现，我们提出DP-Cache与V-AEFusion方法，分别减少扩散冗余并实现异步流水线并行，在GPU上获得最高2.9倍加速，在边缘NPU上获得6倍加速，且任务成功率仅轻微下降。示例排行榜网站见：https://vla-leaderboard-01.vercel.app/。

---

### 9. $M^2$-VLA: Boosting Vision-Language Models for Generalizable Manipulation via Layer Mixture and Meta-Skills

- **作者**: Siyao Xiao, Yuhong Zhang, Zhifang Liu, Zihan Gao, Jingye Zhang, Sinwai Choo, Dake Zhong, Mengzhe Wang, Xiao Lin, Xianfeng Zhou, Jia Jia, Haoqian Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.24182v1)
- **发表日期**: 2026-04-27
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2604.24182v1](http://arxiv.org/abs/2604.24182v1)
- **📥 PDF**: 已下载至本地 (`2604.24182v1_$M^2$-VLA_Boosting_Vision-Language_Models_for_Generalizable_Manipulation_via_Layer_Mixture_and_Meta-.pdf`)
- **🔓 开源**: CODE, MODEL
- **中文摘要**: 当前的视觉-语言-动作（VLA）模型主要依赖端到端微调。尽管这种方法有效，但它损害了视觉-语言模型（VLM）固有的泛化能力，并导致灾难性遗忘。为解决这些局限，我们提出$M^2$-VLA，证明一个通用的VLM能够直接作为机器人操作的强大骨干网络。然而，如何弥合VLM高层语义理解与机器人控制精确需求之间的差距仍是关键挑战。为此，我们引入分层混合（MoL）策略，从密集语义特征中选择性提取任务关键信息。此外，为在有限模型容量下实现高效轨迹学习，我们提出集成强归纳偏置的元技能模块（MSM）。在仿真和真实环境中的大量实验验证了本方法的有效性。进一步的泛化与消融研究证实了该架构的零样本能力，并确认了每个关键组件的贡献。我们的代码和预训练模型将公开发布。

---

### 10. AsyncShield: A Plug-and-Play Edge Adapter for Asynchronous Cloud-based VLA Navigation

- **作者**: Kai Yang, Zedong Chu, Yingnan Guo, Zhengbo Wang, Shichao Xie, Yanfen Shen, Xiaolong Wu, Xing Li, Mu Xu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.24086v1)
- **发表日期**: 2026-04-27
- **匹配关键词**: navigation, obstacle avoidance, VLA, vision-language-action
- **arXiv**: [2604.24086v1](http://arxiv.org/abs/2604.24086v1)
- **📥 PDF**: 已下载至本地 (`2604.24086v1_AsyncShield_A_Plug-and-Play_Edge_Adapter_for_Asynchronous_Cloud-based_VLA_Navigation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 尽管视觉-语言-动作（VLA）模型已被证明在机器人控制中具有强大的零样本泛化能力，但其庞大的参数量通常需要云端部署。然而，云端部署会引入网络抖动和推理延迟，导致连续位移下的移动导航出现严重的时空错位，使得过去自车帧中表达的过时意图在当前帧中可能产生空间错误，进而引发碰撞。为解决这一问题，我们提出AsyncShield——一种即插即用的异步控制框架。该框架摒弃了传统的黑盒时间序列预测，转而采用确定性的物理白盒空间映射。通过维护时序位姿缓冲区并利用运动学变换，系统将时间延迟精确转换为空间位姿偏移，从而恢复VLA的原始几何意图。为平衡意图恢复保真度与物理安全性，边缘适配被建模为约束马尔可夫决策过程（CMDP）。通过PPO-Lagrangian算法求解，强化学习适配器动态权衡VLA意图跟踪与高频激光雷达避障硬约束响应之间的取舍。此外，得益于标准化的通用子目标接口、域随机化以及通过碰撞半径膨胀实现的感知层适配，AsyncShield可作为轻量级即插即用模块运行。仿真与真实世界实验表明，无需微调任何云端基础模型，该框架展现出零样本且鲁棒的泛化能力，有效提升了异步导航的成功率与物理安全性。

---

## 📌 Poster

*其他相关研究*

---

### 1. Variational Neural Belief Parameterizations for Robust Dexterous Grasping under Multimodal Uncertainty

- **作者**: Clinton Enwerem, Shreya Kalyanaraman, John S. Baras, Calin Belta
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.25897v1)
- **发表日期**: 2026-04-28
- **匹配关键词**: dexterous grasping
- **arXiv**: [2604.25897v1](http://arxiv.org/abs/2604.25897v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 接触变异性、感知不确定性和外部扰动使得抓取执行具有随机性。期望质量目标忽略了尾部结果，往往选择在不利接触实现下失败的抓取。风险敏感型POMDP解决了这种失效模式，但许多方法使用粒子滤波置信度，其扩展性差、阻碍基于梯度的优化，并通过高方差近似估计条件风险价值（CVaR）。我们转而将抓取获取建模为对潜在接触参数和物体姿态的变分推断，使用可微高斯混合表示置信度。通过Gumbel-Softmax分量选择和位置-尺度重参数化，将样本表达为置信度参数的平滑函数，从而通过可微CVaR替代函数实现路径梯度，直接优化尾部鲁棒性。在仿真中，我们的变分神经置信度在接触参数不确定性和外力扰动下提升了鲁棒抓取成功率，同时将规划时间相对于粒子滤波模型预测控制减少约一个数量级。在多指手串联机器人臂上，我们针对物体姿态不确定性验证了抓取-提升成功率，并与高斯基线对比。两种方法在测试扰动下均成功，但我们的控制器在更少的步数和更短的墙钟时间内终止，同时实现了更高的触觉抓取质量代理指标。我们的学习置信度还能更准确地校准风险，在测试的仿真场景中平均绝对校准误差保持在0.14以下，而交叉熵方法规划器为0.58。

---

### 2. SlicerRoboTMS: An Open-Source 3D Slicer Extension for Robot-Assisted Transcranial Magnetic Stimulation

- **作者**: Wenzhi Bai, Yituo Guo, Bhaskar Basu, Andrew Weightman, Zhenhong Li
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.25661v1)
- **发表日期**: 2026-04-28
- **匹配关键词**: navigation
- **arXiv**: [2604.25661v1](http://arxiv.org/abs/2604.25661v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: CODE, GITHUB
  - 链接：https://github.com/OpenRoboTMS/SlicerRoboTMS.
- **中文摘要**: 机器人辅助经颅磁刺激（Robo-TMS）是一种基于图像引导的机器人干预技术，可提升传统经颅磁刺激（TMS）的精准度与可重复性。TMS作为一种广泛应用于临床治疗和神经科学研究的非侵入性脑刺激方法，其技术发展仍面临挑战——Robo-TMS的开发需要整合医学影像、计算机视觉和机器人学等多学科专业知识。本文提出SlicerRoboTMS这一开源3D Slicer扩展模块，为Robo-TMS研究提供统一的交互基础设施。该扩展模块利用3D Slicer的医学影像计算与可视化能力，支持基于磁共振成像（MRI）的神经导航，并通过标准化通信协议和可配置系统描述与机器人系统对接。文中通过典型集成案例展示了SlicerRoboTMS如何融入代表性Robo-TMS工作流程。该扩展模块旨在适配多样化硬件配置并支持快速原型开发，降低了技术准入门槛，促进了Robo-TMS研究的可重复性与可扩展性。扩展模块代码已开源至https://github.com/OpenRoboTMS/SlicerRoboTMS。

---

### 3. Bridging the Indoor-Outdoor Gap: Cross-Technology Ranging for Seamless Robot Navigation

- **作者**: Paul Schwarzbach
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.25541v1)
- **发表日期**: 2026-04-28
- **匹配关键词**: navigation, robot navigation
- **arXiv**: [2604.25541v1](http://arxiv.org/abs/2604.25541v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: CODE
- **中文摘要**: 在户外与室内环境间移动的移动机器人在实现稳定定位方面仍面临挑战。基于卫星的定位与地面测距技术各自在其适用领域表现良好，但在原始测量层面的融合尚未得到充分关注，而建筑边界区域恰恰是两类技术性能均会下降的临界点。本文报告了HYMN数据集的初步观测结果，该数据集在工业场景下，将全球导航卫星系统（GNSS）、超宽带（UWB）、WiFi精细时间测量（FTM）及低功耗蓝牙（BLE）的原始测量数据与毫米级地面实况进行时间同步。研究刻画了各区域的测量可用性及测距残差特性，发现两类技术具有互补性，而室内外过渡区域正是其性能短板重叠之处。该数据集已公开提供。

---

### 4. COMPASS: COmpact Multi-channel Prior-map And Scene Signature for Floor-Plan-Based Visual Localization

- **作者**: Muhammad Shaheer, Miguel Fernandez-Cortizas, Asier Bikandi-Noya, Holger Voos, Jose Luis Sanchez-Lopez
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.25388v1)
- **发表日期**: 2026-04-28
- **匹配关键词**: place recognition
- **arXiv**: [2604.25388v1](http://arxiv.org/abs/2604.25388v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 建筑平面图是广泛可用的先验信息，不仅包含环境的几何结构，还包含语义信息，然而现有的定位方法大多忽略了这些语义信息。为解决这一问题，我们提出了COMPASS算法，该算法利用平面图中的几何和语义先验信息，来估计配备双鱼眼相机的机器人的位姿。受基于激光雷达的场所识别中扫描上下文描述符的启发，我们设计了一种多通道径向描述符，用于编码位置周围的几何布局。从平面图中，沿360个方位角区间发射射线，并将结果编码为五个通道：归一化距离、结构命中类型（墙壁、窗户或开口）、距离梯度、逆距离和局部距离方差。在图像方面，通过检测鱼眼图像中的结构元素来填充相同的描述符结构。作为迈向完整跨模态匹配的第一步，我们提出了一种用于鱼眼图像的窗户检测算法，该算法利用线段检测器通过垂直边缘聚类和亮度验证来识别窗框。检测到的窗户通过鱼眼相机模型投影到方位角方向，生成视觉描述符的命中类型通道。作为概念验证，我们从Hilti-Trimble SLAM挑战赛2026数据集的单个已知位姿生成两种描述符，并证明从每个相机第一帧提取的墙壁-窗户模式与平面图描述符高度匹配，验证了跨模态结构匹配的可行性。

---

### 5. ANCHOR: A Physically Grounded Closed-Loop Framework for Robust Home-Service Mobile Manipulation

- **作者**: Jinhao Jiang, Shengyu Fang, Sibo Zuo, Yujie Tang, Yirui Li
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.25323v1)
- **发表日期**: 2026-04-28
- **匹配关键词**: navigation, mobile manipulation
- **arXiv**: [2604.25323v1](http://arxiv.org/abs/2604.25323v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://anchor9178.github.io/ANCHOR/
- **中文摘要**: 开放词汇移动操作的最新进展已将机器人带入真实的家庭环境。在此类场景中，面对开放集物体引用和频繁干扰，可靠的长期任务执行变得至关重要。然而，许多失败依然存在。这些失败并非源于语义理解错误，而是由于符号计划与不断变化的物理世界之间的不一致，表现为三种反复出现的局限性：(i) 现有系统通常依赖预扫描的语义地图，但场景变化和干扰后该地图会变得不一致；(ii) 它们选择导航终点时未考虑下游操作可行性，导致“到达但无法操作”的问题；(iii) 它们通过无差别的全局重规划处理异常，往往无法有效控制局部错误。为解决这种执行不一致性，我们提出ANCHOR——一种物理锚定的闭环框架，在执行过程中将符号推理与可验证的物理状态对齐。ANCHOR整合了三种机制：(i) 物理锚定任务规划，将符号谓词绑定到可观测的几何锚点，并在每次动作后重新验证；(ii) 可操作性感知的基座对齐，确保导航终点满足运动学可达性和局部碰撞可行性；(iii) 最小责任层分层恢复，在感知、基座-手臂协调和执行层定位故障，防止级联重试。在60次真实机器人试验（面对未见环境）中，ANCHOR将任务成功率从53.3%提升至71.7%，并在扰动下实现71.4%的恢复率，证明显式物理锚定和结构化故障遏制对鲁棒移动操作至关重要。我们的项目页面见https://anchor9178.github.io/ANCHOR/。

---

### 6. Optimal UGV-UAV Cooperative Partitioning and Inspection of Shortest Paths

- **作者**: Ninh Nguyen, Srinivas Akella
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.25284v1)
- **发表日期**: 2026-04-28
- **匹配关键词**: path planning
- **arXiv**: [2604.25284v1](http://arxiv.org/abs/2604.25284v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 我们研究了在存在未知道路阻塞的环境中，由无人机辅助的地面无人车辆协同最短路径规划问题。这些阻塞仅在机器人到达受损点时才会被发现。该问题推广了经典的加拿大旅行者问题（CTP），后者假设仅有一辆地面车辆，且所有相邻边的通行状态在到达顶点时才会揭示。我们首先分析了起点与终点由k条不相交路径连接的情况，并证明单辆UGV的最坏情况竞争比ρ为2k-1。在无人机辅助下，且假设无人机初始通行和空载成本可忽略时，该比率改进为ρ=2(v_G/(v_A+v_G))k-1，其中v_G和v_A分别表示UGV和无人机的速度。针对一般图结构及不可忽略的无人机初始通行和空载成本，我们提出了一种最优路径划分策略，将路径前缀检查分配给UGV，后缀检查分配给无人机，并证明了该无人机检查策略在一般图上的最优性。我们通过在全球50个人口最多城市的道路网络上进行随机阻塞实验评估算法，结果表明所提方法可将UGV行驶时间降低高达30%。

---

### 7. HANDFUL: Sequential Grasp-Conditioned Dexterous Manipulation with Resource Awareness

- **作者**: Ethan Foong, Yunshuang Li, Hao Jiang, Gaurav S. Sukhatme, Daniel Seita
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.25126v1)
- **发表日期**: 2026-04-28
- **匹配关键词**: exploration, grasp planning
- **arXiv**: [2604.25126v1](http://arxiv.org/abs/2604.25126v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 灵巧机器手为多功能操作提供了丰富可能，机器人需在保持对已抓取物体控制的同时，顺序执行多项技能。现有灵巧操作研究多聚焦于单物体、单技能任务。与此不同，我们的核心见解在于：许多顺序任务需要资源感知型抓取，即保留手指用于后续动作。本文研究顺序抓取条件灵巧操作——机器人先抓取物体，随后在维持初始抓取姿态的前提下，执行第二个独立操作子任务。我们提出HANDFUL学习框架，将手指使用建模为有限资源，通过手指级接触奖励鼓励探索资源感知型抓取。这些抓取姿态随后通过基于课程策略学习被选用于下游任务。我们进一步提出HANDFUL-Bench仿真基准，在共享抓取条件设置下，引入包含推、拉、按等多种第二子任务目标的顺序灵巧操作任务。大量仿真结果表明，相较于在尝试第二子任务前贪婪优化初始抓取的基线方法，优先考虑资源感知型抓取能提升第二子任务的成功率与鲁棒性。我们还在真实灵巧LEAP手上验证了该方法。本研究确立了资源感知型抓取规划作为多功能灵巧操作的关键原则。补充材料详见网站：https://handful-dex.github.io。

---

### 8. Logic of Fuzzy Paths

- **作者**: Kush Grover, Pratham Gupta, Jan Křetínský
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.24907v1)
- **发表日期**: 2026-04-27
- **匹配关键词**: motion planning
- **arXiv**: [2604.24907v1](http://arxiv.org/abs/2604.24907v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出了一种面向运动规划（MP）规范的新型时序逻辑族。该逻辑建立在信号时序逻辑（STL）基础之上——STL是一种针对实值信号的线性时序逻辑，因其具备定量语义而在信息物理系统、机器人学，特别是机器人运动规划领域广受欢迎。然而，与STL不同，本文提出的逻辑将路径作为首要对象，将几何问题与逻辑问题分离处理。这进而产生了更简洁易懂的公式，以及能够反映行为偏好的更精细的满足性概念。从技术层面而言，该逻辑建立在模糊时变信号约束之上。由于这种表达能力，它（i）在运动规划中更适用于人类给定的规范，且（ii）比其他逻辑更易于从示范中学习规范。前者对于机器人运动规划中传统的验证风格至关重要；后者正逐渐被公认为在人类感知运动规划中挖掘数据驱动任务和控制器合成的关键。我们通过示例展示了所提出逻辑的优势，并在多个场景中论证了该框架的通用性与灵活性。最后，我们给出了一种带有原型实现的学习算法，并探讨了模型检测与监控的可能性。

---

### 9. Passage-Aware Structural Mapping for RGB-D Visual SLAM

- **作者**: Ali Tourani, Miguel Fernandez-Cortizas, Saad Ejaz, David Pérez Saura, Asier Bikandi-Noya, Jose Luis Sanchez-Lopez, Holger Voos
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.24707v1)
- **发表日期**: 2026-04-27
- **匹配关键词**: navigation, robot navigation, scene graph
- **arXiv**: [2604.24707v1](http://arxiv.org/abs/2604.24707v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: CODE, GITHUB
  - 链接：https://github.com/snt-arg/visual_sgraphs/tree/doorway_integration.
- **中文摘要**: 门廊与通道是室内机器人导航的关键结构元素，但在现代视觉SLAM（VSLAM）框架中仍未被充分探索。本文提出一种面向RGB-D VSLAM的通道感知结构建图方法，通过融合几何、语义和拓扑线索来检测门及可通行开口。门被建模为嵌入墙体的平面实体，并根据其与支撑墙体的共面性分类为可通行或不可通行。通道的推断通过两种互补策略实现：基于连续关键帧间相机-墙体交互积累的通行证据，以及基于映射墙体几何不连续性的几何开口验证。该方法作为概念验证集成至vS-Graphs中，通过通道级抽象丰富其场景图并改进房间连通性建模。在室内办公序列上的定性评估展示了可靠的门口检测能力，该框架为在BIM辅助VSLAM中利用这些元素奠定了基础。源代码已开源：https://github.com/snt-arg/visual_sgraphs/tree/doorway_integration。

---

### 10. Sliding Mode Control for Safe Trajectory Tracking with Moving Obstacles Avoidance: Experimental Validation on Planar Robots

- **作者**: Shubham Sawarkar, P Sangeerth, S Saharsh, Pushpak Jagtap
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.24518v1)
- **发表日期**: 2026-04-27
- **匹配关键词**: obstacle avoidance
- **arXiv**: [2604.24518v1](http://arxiv.org/abs/2604.24518v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 本文提出了一种适用于多种移动机器人的统一控制框架，用于实现鲁棒轨迹跟踪与移动障碍物规避。通过构建广义运动学变换，我们将不同车辆动力学模型转化为严格反馈形式，从而便于设计滑模控制策略以实现精确且鲁棒的参考轨迹跟踪。为确保动态环境中的运行安全，该跟踪控制器与基于碰撞锥控制障碍函数的安全滤波器相结合。所提出的架构能够在存在外部扰动的情况下保证渐近跟踪性能，同时严格满足避碰约束。本工作的创新之处在于首次为阿克曼转向等地面机器人设计了滑模控制器。通过数值仿真以及在三种不同平台（阿克曼转向车辆、差速驱动机器人、四旋翼无人机）上的大量真实实验，验证了该方法的有效性与通用性。实验视频可访问 https://youtu.be/dWcxwum96vk 观看。

---

