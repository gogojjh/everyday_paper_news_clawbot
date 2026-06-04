# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-06-04 08:02

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 3/20 篇提供

**🌟 Highlight**: 15 篇 | **📌 Poster**: 5 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. SimuScene: Simulation-Ready Compositional 3D Scene Reconstruction from a Single Image

- **作者**: Inhee Lee, Sangwon Baik, Sungjoo Kim, Hyeonwoo Kim, Hyunsoo Cha, Hanbyul Joo
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.03994v1)
- **发表日期**: 2026-06-02
- **匹配关键词**: 3d reconstruction, 3D reconstruction
- **arXiv**: [2606.03994v1](http://arxiv.org/abs/2606.03994v1)
- **📥 PDF**: 已下载至本地 (`2606.03994v1_SimuScene_Simulation-Ready_Compositional_3D_Scene_Reconstruction_from_a_Single_Image.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 从单张图像重建可交互、可直接用于仿真的三维场景，是机器人操作领域的关键瓶颈。尽管现有的单图像三维重建方法能够恢复合理的物体形状，但将这些形状组合成场景后，由于物体间存在相互穿透、悬空或下沉等问题，在物理仿真中会出现坍塌。现有物理感知方法仅将物理约束作为事后布局修正手段，未能解决底层几何误差。为此，我们提出SimuScene——一种将物理约束融入形状与布局估计流程的组合式三维重建管线。不同于仅将物理用于布局清理，我们在生成过程中将物理引擎作为诊断测量工具：通过对重建物体进行重力作用下的诊断仿真，将穿透与支撑失效转化为量化修正信号，驱动重力轴拉伸与非模态形状重采样。这种物理感知的反馈循环能够抑制累积的重建误差，生成稳定且可直接用于仿真的组合式三维场景。大量实验表明，该方法在物理稳定性与几何对齐基准上达到最优性能。我们进一步通过将重建环境部署到人形机器人控制与机械臂操作任务中，验证了SimuScene的实用价值。

---

### 2. Worth Remembering: Surprise-Gated Robot Episodic Memory

- **作者**: Nicolas Gorlo, Derek K. Wise, Alberto Speranzon, Luca Carlone ⭐
  - **高亮作者**: Luca Carlone
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.03787v1)
- **发表日期**: 2026-06-02
- **匹配关键词**: scene graph
- **arXiv**: [2606.03787v1](http://arxiv.org/abs/2606.03787v1)
- **📥 PDF**: 已下载至本地 (`2606.03787v1_Worth_Remembering_Surprise-Gated_Robot_Episodic_Memory.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 执行通用任务的机器人需要能够将指令与自身过往经验相关联，因为人类在布置任务时可能会提及显著的历史事件（例如：“带我去昨天发生化学品泄漏的地方”）。由于存储所有历史事件受限于记忆容量，长期机器人记忆必须具备选择性，理想情况下仅保留对未来任务具有高实用性的片段。然而通用机器人的未来任务通常无法预先设定。为筛选具有通用价值的记忆，我们提出将贝叶斯惊奇度作为记忆形成的门控机制。我们开发了一种方法，在V-JEPA-2提供的语义丰富且与部署环境无关的潜在空间中计算惊奇度。通过将这种门控情景记忆与基于4D场景图的增强型空间记忆相结合，我们在机器人问答任务中相较现有最优基准实现了持续改进：针对时间、空间和二元问题的回答准确率较先前机器人记忆方法提升≥12%，并在事件分割任务中采用无监督因果方法超越了监督方法与非因果方法的性能表现。

---

### 3. Revisiting Embodied Chain-of-Thought for Generalizable Robot Manipulation

- **作者**: Nan Sun, Yuan Zhang, Yongkun Yang, Wentao Zhao, Peiyan Li, Jun Guo, Wenxuan Song, Pengxiang Ding, Runze Suo, Yifei Su, Xin Xiao, Xinghang Li, Huaping Liu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.03784v1)
- **发表日期**: 2026-06-02
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2606.03784v1](http://arxiv.org/abs/2606.03784v1)
- **📥 PDF**: 已下载至本地 (`2606.03784v1_Revisiting_Embodied_Chain-of-Thought_for_Generalizable_Robot_Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 具身思维链（Embodied CoT）旨在桥接语言推理与机器人控制，但其有效形式与整合策略仍待深入探索。本文在大规模场景下重新审视了面向视觉-语言-动作（VLA）模型的具身思维链。我们构建了迄今最大的具身思维链语料库，包含978,743条轨迹、2.263亿个样本及2592.5小时的机器人数据。通过大量实验发现，有效的具身思维链应将高层语义理解转化为具体动作指导（如末端执行器运动描述与图像空间轨迹），而仅依赖高层推理仅能带来边际收益。进一步研究表明，当将显式思维链作为自回归动作前缀使用时，其扩展性不可靠，原因在于复合推理误差与不稳定的推理-动作耦合。为解决这些局限，我们提出ERVLA模型——将具身思维链作为表征塑造监督信号而非强制测试时推理。该模型采用推理丢弃策略进行训练，使模型在训练阶段吸收丰富推理轨迹的同时，在推理阶段无需思维链解码即可直接预测动作。这种设计提升了随预训练数据规模增长的扩展性，并避免了自回归不稳定性。ERVLA在LIBERO-Plus上以86.9%的成功率取得最优性能，在VLABench上达到53.2%的成功率，展现出强大的分布外泛化能力。在真实机器人实验中，ERVLA进一步超越多个竞争性基线模型，尤其在需要语义消歧与长程执行的任务中表现突出。代码、数据及模型检查点将开源发布。

---

### 4. GN0: Toward a Unified Paradigm for Generation, Evaluation, and Policy Learning in Visual-Language Navigation

- **作者**: Xinhai Li, Xiaotao Zhang, Yuehao Huang, Jiankun Dong, Tianhang Wang, Sunyao Zhou, Yunzi Wu, Chengnuo Sun, Yunfei Ge, Qizhen Weng, Chi Zhang, Chenjia Bai, Xuelong Li
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.03682v1)
- **发表日期**: 2026-06-02
- **匹配关键词**: exploration, vision-and-language navigation, VLN, navigation, human-robot interaction, gaussian splatting, 3D gaussian splatting
- **arXiv**: [2606.03682v1](http://arxiv.org/abs/2606.03682v1)
- **📥 PDF**: 已下载至本地 (`2606.03682v1_GN0_Toward_a_Unified_Paradigm_for_Generation,_Evaluation,_and_Policy_Learning_in_Visual-Language_Nav.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 具身导航连接智能体与物理世界，是实现通用机器人智能的基础。导航数据的有限可用性和质量限制了视觉-语言导航（VLN）系统的泛化能力和长程任务能力。为解决这一问题，我们整理了多样化的三维场景，并开发了大规模导航数据的自动化流水线，构建了GN-Matrix数据集。基于三维高斯泼溅（3DGS）引擎，我们引入了一个支持交互式漫游和碰撞感知导航的高保真仿真平台。进一步地，我们提出了GN-Bench——首个基于鸟瞰图（BEV）的基准测试，结合动态3DGS虚拟角色用于人机交互评估。为充分利用该仿真器，我们开发了基于强化学习的导航基础模型——Break and Establish（BAE）。在监督学习后，DAgger方法使模型暴露于策略展开生成的状态中，打破狭窄的专家中心分布，并支持下游强化学习探索。这一统一VLN范式整合了基于地图和无地图任务，包括指令跟随、人类跟随及目标导航。GN-BAE将高保真3DGS渲染的鸟瞰图表示形式化为紧凑记忆，释放了视觉-语言模型（VLM）中的潜在空间推理能力。在GN-Bench和VLN-CE上的广泛评估表明，GN0优于当前最先进的VLN方法。总体而言，GN-Matrix提供了涵盖数据、仿真和学习的统一框架，推动了具身导航在研究与工业应用中的发展。

---

### 5. PHASER: Phase-Aware and Semantic Experience Replay for Vision-Language-Action Models

- **作者**: Ziyang Chen, Shaoguang Wang, Weiyu Guo, Qianyi Cai, He Zhang, Pengteng Li, Yiren Zhao, Yandong Guo
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.03598v1)
- **发表日期**: 2026-06-02
- **匹配关键词**: vision-language-action, vision-language-action model, VLA
- **arXiv**: [2606.03598v1](http://arxiv.org/abs/2606.03598v1)
- **📥 PDF**: 已下载至本地 (`2606.03598v1_PHASER_Phase-Aware_and_Semantic_Experience_Replay_for_Vision-Language-Action_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型在语言条件机器人操作任务中取得了显著成功。然而，在开放环境中部署这些模型需要持续获取新技能，这一过程不可避免地会严重遗忘先前学习的行为。虽然经验回放（ER）是标准的缓解策略，但朴素均匀采样从根本上与操作轨迹的时间特性不匹配——它系统性地低估了短暂但因果关键的子技能，导致阶段饥饿，并完全忽略了历史任务中不同程度的遗忘。为克服这些局限，我们提出PHASER，一种架构无关的持续学习框架。PHASER采用以阶段为中心的能力分配机制，确保所有子技能获得均等的记忆支持，同时结合多模态干扰路由策略，动态优先处理遗忘风险高的历史阶段。此外，为实现完全自主的终身适应，我们整合了Auto-PC轻量级流水线，该流水线将无监督动作信号变化点检测与基于VLM的语义验证相结合，无需密集人工监督即可提取时间边界。在LIBERO持续学习套件上基于三种VLA骨干网络的评估表明，PHASER取得了显著实证提升：与同等预算的ER相比，平均成功率（ASR）最高提升31%，在LIBERO-Goal持续学习设置中最终ASR达到87.8%。

---

### 6. Partially Observable Adversarial Patch Attacks on Vision-Language-Action Models in Robotics

- **作者**: Xiaofei Wang, Mingliang Han, Tianyu Hao, Yi Yang, Yun-Bo Zhao, Keke Tang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.03556v1)
- **发表日期**: 2026-06-02
- **匹配关键词**: vision-language-action, vision-language-action model, VLA
- **arXiv**: [2606.03556v1](http://arxiv.org/abs/2606.03556v1)
- **📥 PDF**: 已下载至本地 (`2606.03556v1_Partially_Observable_Adversarial_Patch_Attacks_on_Vision-Language-Action_Models_in_Robotics.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型在机器人领域日益受到关注，但其对对抗攻击的鲁棒性仍鲜有研究。现有工作表明，对抗性补丁可以误导基于VLA的机器人，但这类方法假设攻击者能完全获取整个执行轨迹，这一要求在实际场景中难以实现。针对这一局限，我们提出了一种部分可观测的威胁模型——攻击者仅能利用轨迹的短前缀生成固定补丁，并将其应用于后续所有帧。在此设定下，我们提出两阶段框架：首先，利用模型注意力图定位补丁，识别与完整指令对应的视觉关键区域；其次，优化补丁以破坏目标对象的语义关联，并增大动作轨迹的曲率，从而在感知与控制层面引发复合性故障。在仿真与真实机器人环境中的大量实验表明，我们的方法在部分可观测条件下仍能维持对抗效果，诱导长时域故障并显著降低任务成功率。

---

### 7. Human2Humanoid: Physics-Aware Cross-Morphology Motion Retargeting for Humanoid Robots

- **作者**: Tianchen Huang, Feiyang Yuan, Junchi Gu, Shurui Fang, Xiaohu Zhang, Yu Wang, Wei Gao, Shiwu Zhang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.03476v1)
- **发表日期**: 2026-06-02
- **匹配关键词**: human-robot interaction
- **arXiv**: [2606.03476v1](http://arxiv.org/abs/2606.03476v1)
- **📥 PDF**: 已下载至本地 (`2606.03476v1_Human2Humanoid_Physics-Aware_Cross-Morphology_Motion_Retargeting_for_Humanoid_Robots.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 将人体运动重定向至人形机器人对于远程操控、模仿学习及人机交互至关重要。然而，由于人类与机器人在骨骼拓扑结构、肢体比例、自由度等方面存在显著形态差异，且配对运动数据稀缺，这一任务仍面临挑战。本文提出Human2Humanoid——一种无监督运动重定向框架，能够将人体运动高保真地迁移至人形机器人行为。为弥合非配对数据下的领域差异，我们采用基于CycleGAN的架构，并配备骨架感知图卷积网络以捕捉拓扑相关的运动特征。针对跨域尺度不匹配问题，我们引入形态不变末端执行器一致性损失函数，通过对齐归一化末端执行器轨迹来保留跨实体的运动语义。为提升物理合理性并减少接触伪影，我们施加显式的物理感知可行性约束，以鼓励复现源运动中的接触模式。实验结果表明，所提方法无需配对数据即可成功将人体运动重定向至Unitree G1人形机器人，并在下游可控性与物理可行性方面均优于现有方法。

---

### 8. OpenEAI-Platform: An Open-source Embodied Artificial Intelligence Hardware-Software Unified Platform

- **作者**: Jinyuan Zhang, Luoyi Fan, Leiyu Wang, Yeqiang Wang, Yicheng Zhu, Cewu Lu, Nanyang Ye
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.03392v1)
- **发表日期**: 2026-06-02
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2606.03392v1](http://arxiv.org/abs/2606.03392v1)
- **📥 PDF**: 已下载至本地 (`2606.03392v1_OpenEAI-Platform_An_Open-source_Embodied_Artificial_Intelligence_Hardware-Software_Unified_Platform.pdf`)
- **🔓 开源**: CODE
- **中文摘要**: 真实世界中的具身人工智能既需要精确的硬件，也需要稳健的视觉-语言-动作（VLA）策略。我们提出OpenEAI-Platform，这是一个完全开源平台，集成了低成本6+1自由度机械臂（OpenEAI-Arm）和可复现的VLA模型（OpenEAI-VLA）。OpenEAI-Arm提供开源机械设计以降低制造成本，并采用柔顺控制方法提升精度。OpenEAI-VLA基于Qwen3-VL-4B构建，使用扩散Transformer动作头，仅通过开源机器人及多模态数据集进行两阶段训练。在四项真实世界操作任务中，OpenEAI-Arm在相同策略下优于两款商用6+1自由度机械臂，而OpenEAI-VLA在仅使用有限预训练数据的情况下，其成功率可与大规模预训练的pi0基线相媲美。我们将发布完整的硬件设计、驱动程序、模型及训练/数据流水线，以支持可复现研究与可扩展数据采集。相关代码、布局及模型将在论文接收后公开。

---

### 9. Grasp-Then-Plan with Failure Attribution: A Closed Two-Stage Framework for Precise and Generalizable Robotic Manipulation

- **作者**: Jiahao Xu, Peiyuan Wang, Hanzhuo Zhang, Zihao Yu, Tianyu Fu, Hao Chen, Xuanhao Xiang, Jianbo Yu, Chenchen Fu, Wanyuan Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.03385v1)
- **发表日期**: 2026-06-02
- **匹配关键词**: motion planning, VLA
- **arXiv**: [2606.03385v1](http://arxiv.org/abs/2606.03385v1)
- **📥 PDF**: 已下载至本地 (`2606.03385v1_Grasp-Then-Plan_with_Failure_Attribution_A_Closed_Two-Stage_Framework_for_Precise_and_Generalizable_.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 在机器人操作中，抓取与运动规划之间的紧密耦合常常掩盖了真正的失败原因，导致低效的试错过程。为了实现高效的长时域操作，我们提出了GTP-FA（先抓取后规划与失败归因）框架，这是一种面向任务的两阶段抓取-规划框架，首先生成抓取候选方案，再基于选定的抓取执行下游运动规划。针对失败的操作轨迹，我们学习了一个失败归因模型，该模型能够泛化到未见过的抓取动作，并生成关于失败模式的稳定分布，用于诊断引导的优化。基于这些归因结果，我们以诊断驱动的方式对两个模块进行优化：在抓取侧，我们将任务级先验知识和风险惩罚引入抓取候选评分与优化过程，以抑制不稳定或与任务不兼容的抓取；在规划侧，我们通过数据收集和微调聚焦高风险初始状态，以解决真正的规划瓶颈。我们在仿真和真实机器人实验中评估了所提出的框架，结果表明GTP-FA在基于强化学习、模仿学习、扩散策略和视觉-语言-动作模型的方法中均提升了对应基础学习器的性能，实现了显著更高的整体任务成功率。

---

### 10. GeoAlign: Beyond Semantics with State-Guided Spatial Alignment in VLA Models

- **作者**: Yizhi Chen, Zhanxiang Cao, Xinyi Peng, Yixiao Zheng, Xiaxi Si, Yiheng Li, Liyun Yan, Keqi Zhu, Xueyun Chen, Shengcheng Fu, Tianyue Zhan, Yufei Jia, Jinming Yao, Yan Xie, Kun Wang, Cewu Lu, Yue Gao
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.03240v1)
- **发表日期**: 2026-06-02
- **匹配关键词**: affordance, VLA
- **arXiv**: [2606.03240v1](http://arxiv.org/abs/2606.03240v1)
- **📥 PDF**: 已下载至本地 (`2606.03240v1_GeoAlign_Beyond_Semantics_with_State-Guided_Spatial_Alignment_in_VLA_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 当前视觉-语言-动作（VLA）模型通常侧重于语义对齐优化，而可执行操作需要几何感知的空间对齐和动态功能选择。我们提出GeoAlign——一种面向VLA策略学习的状态引导空间对齐架构。GeoAlign通过机器人域RGB-D监督对RGB几何分支进行后训练，生成用于策略执行的RGB衍生几何增强后训练（GEP）特征。机器人本体感知状态查询GEP特征网格，生成紧凑的相位相关几何标记用于动作预测。GeoAlign在LIBERO基准上达到99.0%准确率，在三个SimplerEnv-Fractal任务中平均85.3%，在八个几何关键的真实世界ALOHA任务中达78.8%。消融实验证实了几何后训练和本体感知状态引导查询的有效性。

---

### 11. AURA: Action-Gated Memory for Robot Policies at Constant VRAM

- **作者**: Josef Chen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.02775v1)
- **发表日期**: 2026-06-01
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2606.02775v1](http://arxiv.org/abs/2606.02775v1)
- **📥 PDF**: 已下载至本地 (`2606.02775v1_AURA_Action-Gated_Memory_for_Robot_Policies_at_Constant_VRAM.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: KV缓存是数据中心的合适内存，却是机器人的错误内存。数据中心推理处理大量短请求并重置它们，将注意力缓存在群体中分摊。而具身智能体则在带宽受限的边缘硬件上运行单个长周期、非重置的回合，此时高带宽内存和闪存稀缺，闪存写入寿命有限，内存写入而非计算可能成为约束瓶颈。

AURA-Mem（动作效用循环自适应内存）针对这一场景设计。它用一个固定大小的循环内存和一个学习型门控机制包裹冻结的视觉-语言-动作骨干网络，该门控仅在当前观测会改变下一步动作时执行写入：即懂得何时保持静默的内存。与基于重建的内存不同，该门控直接针对闭环动作误差信号进行训练。其推理状态固定为4,224字节，不受时间跨度影响，而KV缓存在10万步时体积增长至其6,061倍。

在受控合成基准测试中，AURA-Mem在精度上匹配最佳O(1)基线，同时写入次数减少5.19-6.13倍，在较简单配置下写入次数减少高达9.19倍。预算匹配的随机和周期性调度无法恢复这一增益，从而将优势归因于动作意外信号。在LIBERO-Long（每机械臂60个回合）上训练的闭环OpenVLA-OFT 7B面板测试中，该门控未损害成功率：AURA-Mem匹配无门控基础策略（0.233），并略超始终写入的KV分支（0.217），同时写入次数减少7.0倍且内存恒定。我们还实例化了近似信息状态价值损失界限作为方法论演示；在此规模下，该界限是空洞的而非保证。

---

### 12. SeeTraceAct: Visibility-Aware Latent Planning from Cross-Embodiment Demonstration Videos

- **作者**: Jaehyeon Son, Junhyun Kim, Kyle Kam, Jeremiah Coholich, Seok Joon Kim, Jinhoo Kim, Chris Dongjoo Kim, Jaemin Cho, Dieter Fox, Zsolt Kira
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.02745v1)
- **发表日期**: 2026-06-01
- **匹配关键词**: vision-language-action, vision-language-action model, VLA
- **arXiv**: [2606.02745v1](http://arxiv.org/abs/2606.02745v1)
- **📥 PDF**: 已下载至本地 (`2606.02745v1_SeeTraceAct_Visibility-Aware_Latent_Planning_from_Cross-Embodiment_Demonstration_Videos.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作模型（VLAs）是极具前景的通用机器人策略，但将其适配至新任务通常需要昂贵的特定任务遥操作数据。作为替代方案，我们研究了单样本演示条件型VLA，即机器人策略以未见任务的单段演示视频为条件。研究发现，当成功执行需要精确定位小目标区域时，现有端到端方法往往表现不佳。为解决这一局限，我们提出SeeTraceAct——一种通过可见性感知的未来末端执行器轨迹预测来增强空间定位精度的演示条件型VLA框架。为支持跨具身演示的可复现评估，我们引入并发布了RoboCasa-DC——RoboCasa的演示条件扩展数据集，包含逐集配对的人形机器人视频。在RoboCasa-DC及真实世界基准测试（Franka Panda机械臂以人类演示为条件）中的实验表明，SeeTraceAct优于基线方法，在全部四个RoboCasa-DC场景中均取得最佳成功率，并将真实世界平均成功率提升12.5个百分点。

---

### 13. See Less, Specify More: Visual Evidence Budgets for Generalizable VLAs

- **作者**: Yueh-Hua Wu, Tatsuya Matsushima, Kei Ota
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.02735v1)
- **发表日期**: 2026-06-01
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2606.02735v1](http://arxiv.org/abs/2606.02735v1)
- **📥 PDF**: 已下载至本地 (`2606.02735v1_See_Less,_Specify_More_Visual_Evidence_Budgets_for_Generalizable_VLAs.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 泛化能力仍是视觉-语言-动作（VLA）模型的核心瓶颈：在干扰物、外观变化和语义相似任务中，策略往往需要从粗略指令中推断局部执行细节，同时决定图像中哪些部分对控制至关重要。我们提出S2（少看多指定）框架，通过训练执行器在更清晰的接口下运行，提升VLA模型的泛化能力。

"多指定"将原始指令作为稳定的高层目标保留，同时将每条轨迹重新标注为细化的轨迹级和子任务级语言，以消除当前执行模式的歧义。与原生注意力机制不同，"少看"施加了显式的视觉证据预算，训练执行器基于任务充分的证据而非无约束的视觉上下文行动，且无需任何区域或掩码标注。

该接口使执行器能够遵循详细指导，无需依赖干扰性视觉补丁或自行解决可避免的歧义，同时通过上下文学习与现成的VLM规划器保持兼容。在主要评估设置中，S2通过改变执行器的学习问题提升了整体泛化指标：粗略指令导致可避免的监督混叠，目标保持的局部指导在主要消融实验中优于指令替换，显式证据预算减少了对广泛视觉上下文的依赖（超越效率考量）。

在TX-G2（兼容AgiBot G2的变体）和HSR上的八项真实机器人任务中，S2将平均子任务成功率从pi0.5的54.2%提升至79.0%。这些结果表明，当执行器被训练基于信息丰富的局部指导和任务充分的视觉证据行动（而非从弱监督中同时恢复两者）时，VLA模型的泛化能力得到提升。

---

### 14. SparseStreet: Sparse Gaussian Splatting for Real-Time Street Scene Simulation

- **作者**: Qingpo Wuwu, Xiaobao Wei, Peng Chen, Nan Huang, Zhongyu Zhao, Hao Wang, Ming Lu, Ningning Ma, Shanghang Zhang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.03909v1)
- **发表日期**: 2026-06-02
- **匹配关键词**: gaussian splatting, 3D gaussian splatting
- **arXiv**: [2606.03909v1](http://arxiv.org/abs/2606.03909v1)
- **📥 PDF**: 已下载至本地 (`2606.03909v1_SparseStreet_Sparse_Gaussian_Splatting_for_Real-Time_Street_Scene_Simulation.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://sparsestreet.github.io/.
- **中文摘要**: 尽管3D高斯泼溅在街景重建中展现出良好效果，但现有方法需要大量高斯基元来捕捉精细细节，导致存储成本过高且渲染速度缓慢。我们观察到动态物体（如车辆和行人）需要高保真表示以维持时间一致性，而静态背景区域往往存在大量冗余。基于此，我们提出SparseStreet——一种专为街景设计的通用压缩框架。首先，我们引入基于节点的可学习剪枝策略，在保留视觉关键区域的同时系统性地移除低贡献高斯基元。其次，当场景表示稳定后，我们应用背景压缩进一步减少静态区域的冗余。该方法在有效保持动态物体几何与外观的同时，显著降低了高斯基元总数。在Waymo和nuScenes数据集上的大量实验表明，SparseStreet在质量损失极小的情况下实现了高达80%的压缩率，实现了资源高效的高保真动态场景重建。项目网站：https://sparsestreet.github.io/。

---

### 15. MLP Splatting: Object-Centric Neural Fields

- **作者**: Shinjeong Kim, Yuzhou Cheng, Xin Kong, Paul H. J. Kelly, Andrew J. Davison
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.03877v1)
- **发表日期**: 2026-06-02
- **匹配关键词**: gaussian splatting, 3D gaussian splatting, neural radiance field
- **arXiv**: [2606.03877v1](http://arxiv.org/abs/2606.03877v1)
- **📥 PDF**: 已下载至本地 (`2606.03877v1_MLP_Splatting_Object-Centric_Neural_Fields.pdf`)
- **🔓 开源**: PROJECT_PAGE
- **中文摘要**: 三维表示是场景渲染、理解和交互的基础。近期方法如3D高斯泼溅和神经辐射场虽能实现令人惊叹的照片级新视角合成，但难以将场景元素轻松分解为少量基元，需要额外分割或分组才能进行对象级操作。我们提出MLP-Splatting方法，通过少量具有表现力的光场基元实现场景分解，同时保持照片级新视角合成能力。

MLP-Splatting将每个基元建模为具有局部空间支撑的独立紧凑型MLP，用于预测辐射度和不透明度。与低层次高斯基元或单一全局辐射场相比，我们的神经基元在保持空间局部性的同时具备更强的表达能力。渲染通过光线-基元交互的高效稀疏体素合成实现。

我们的基元仅通过RGB监督进行训练，生成的基元能表征通常对应物体或物体部件的局部场景区域，无需分割掩码即可通过选择少量基元实现交互式对象级编辑。该方法结合可选的语义特征蒸馏，支持开放词汇场景交互和开放集实例分割。与最先进方法相比，我们在实验中展示出显著更低的内存占用（1/15×）和更快的渲染速度（3×），相关对比结果已与语义3DGS方法进行验证。项目页面：https://shinjeongkim.com/mlp-splatting

---

## 📌 Poster

*其他相关研究*

---

### 1. Self-Refining Agentic Reinforcement Learning for Vision-Conditioned UAV Navigation

- **作者**: Roohan Ahmed Khan, Yasheerah Yaqoot, Muhammad Ahsan Mustafa, Dzmitry Tsetserukou
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.03963v1)
- **发表日期**: 2026-06-02
- **匹配关键词**: navigation, obstacle avoidance
- **arXiv**: [2606.03963v1](http://arxiv.org/abs/2606.03963v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 深度强化学习在使自主机器人学习复杂导航任务方面展现出巨大潜力。然而，其实际应用仍高度依赖人工设计的奖励函数和反复的手动调参，这一过程耗时且无法保证在目标任务中取得高成功率。本文提出AgenticRL——一种智能体引导的强化学习框架，旨在提升无人机（UAV）导航任务中奖励函数设计、策略优化及真实世界部署的自主性。AgenticRL利用多模态生成式预训练Transformer（GPT）智能体解析任务信息与视觉场景观测，生成任务特定奖励函数，通过近端策略优化（PPO）算法训练策略，并作为评论家通过诊断包评估训练策略以生成反馈。基于该反馈，智能体识别失败模式并在闭环自我改进过程中优化奖励函数。为在推理阶段进一步利用多模态GPT智能体，AgenticRL通过真实世界图像与自然语言任务信息自动识别当前场景，并选择相应训练策略执行。该框架在多项导航任务中进行了评估，包括穿越闸门、避障、穿越障碍墙并着陆、轨迹跟踪及运动行为学习。实验结果表明，与初始奖励相比，闭环优化过程使策略行为提升71%。我们还展示了该框架的仿真到真实迁移能力，实现了91%的真实世界成功率与94%的仿真到真实准确率。

---

### 2. Face versus Body Tracking for Human-Robot Interaction: An Egocentric Dataset

- **作者**: Jessica Wenninger, Gabriel Skantze
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.03694v1)
- **发表日期**: 2026-06-02
- **匹配关键词**: human-robot interaction, HRI
- **arXiv**: [2606.03694v1](http://arxiv.org/abs/2606.03694v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 为实现有意义的人机交互（HRI），机器人必须通过持续追踪用户来实时评估其参与度。然而，当前最先进的计算机视觉模型主要针对监控或自动驾驶场景进行优化。社交机器人面临独特的自我中心挑战，例如人类跳跃、相互遮挡或离开画面。频繁的身份切换（IDSW）会导致机器人在对话中失去追踪目标。为解决这一问题，我们通过Furhat机器人收集了一个新颖的、自定义标注的自我中心数据集，以捕捉复杂的社会动态。我们提出了一种系统评估方法：将检测错误与追踪逻辑分离，比较面部追踪与身体追踪的效果，并评估扩展空间记忆与外观重识别（ReID）的影响。结果表明，增加空间记忆可缓解长时间遮挡问题，但无法应对复杂动态事件。集成ReID能解决复杂身份切换，但会产生相反效果：它显著提升了身体追踪的稳定性，却因侧面角度敏感性导致面部IDSW激增。最终，优化后的管道将IDSW降低了49%，减少了交互中断。由于标准基准缺乏密集、近距离的遮挡场景，本研究凸显了原生捕捉社会动态对真正验证HRI感知模型的必要性。

---

### 3. A 3D Isovist World Model -- Revealing a City's Unseen Geometry and Its Emergent Cross-City Signature

- **作者**: Xuhui Lin, Stephen Law, Nanjiang Chen, Kunyao Li, Tao Yang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.03609v1)
- **发表日期**: 2026-06-02
- **匹配关键词**: navigation
- **arXiv**: [2606.03609v1](http://arxiv.org/abs/2606.03609v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 在城市中导航的具身智能体依赖于世界模型，该模型能预测其周围环境随移动而发生的变化。但对于导航而言，建筑物的外观并不重要，重要的是智能体能够到达的区域。然而，大多数世界模型仍以预测外观为目标，学习场景的视觉呈现而非智能体可通行的空间。那些针对几何结构建模的模型（如鸟瞰视角的占据网格）会将三维环境压缩至地面平面，从而丢弃了构成真实导航的空中与多层结构。目前缺失的是一种预测目标：既能捕捉智能体实际穿越的可通行几何结构，又不受光度信息干扰，同时保留三维空间的完整性。我们的核心思想是建模建筑物之间的开放空间——即负空间，并将其编码为三维等视域图：一种记录每个方向到最近表面距离的球形可见深度图。我们提出一种具身世界模型，通过过去短时段的等视域序列与运动动作预测下一时刻的等视域。该预测被公式化为深度残差，使解码器继承清晰的建筑边缘；通过自滚动调度采样训练，确保几何流形上的上下文信息不被破坏；并配备持久化的隐式鸟瞰空间地图，实现跨路径一致性。我们的核心发现具有涌现性与意外性：在曼哈顿与巴黎训练的单城市盲模型，竟发展出跨城市的空间特征——其时间隐变量可线性解码出城市身份，且解码准确率远超单帧基线。这意味着该特征存在于学习到的动力学中，而非外观层面。该表征轻量、可解释且可复现，为具身人工智能、机器人学与城市分析中的空间推理提供了几何基础，并已随开放数据集与流程一同发布。

---

### 4. SPADE: Sketch-guided Path Planning Augmented with Diffusion Experts

- **作者**: Charbel Abi Hana, Tatiana Ghantous, Mikael Khalil, Anthony Rizk
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.03512v1)
- **发表日期**: 2026-06-02
- **匹配关键词**: path planning
- **arXiv**: [2606.03512v1](http://arxiv.org/abs/2606.03512v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 路径规划对于自主移动机器人（AMR）至关重要。传统将人类偏好融入规划的方法通常依赖于复杂的奖励工程或硬件密集型解决方案。近期最先进的框架利用模仿学习，通过专家示范训练特定行为的路径规划模型。然而，这些方法面临两个关键限制：对未见环境的泛化能力有限，以及示范收集过程中的鲁棒性不足。为解决这些问题，本研究提出了一种增强框架，主要贡献包括：基于ROS 2重构的标注工具，以及将扩散增强集成到基线行为克隆模型中的新型训练策略。我们提供了专家示范数据集，并通过消融实验评估所提方案的鲁棒性。增强方法在绝对位姿误差（APE）上降低39.1%，在弗雷歇初始距离（FID）上降低33.5%，同时可训练参数减少93.8%，优于现有最先进方法。此外，该方法在保持最先进模型实时性与边缘部署特性的同时，实现了扩散级别的泛化能力。

---

### 5. Reliability-Guided Depth Fusion for Glare-Resilient Navigation Costmaps

- **作者**: Shang-En Tsai
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.03421v1)
- **发表日期**: 2026-06-02
- **匹配关键词**: navigation
- **arXiv**: [2606.03421v1](http://arxiv.org/abs/2606.03421v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 反光地板、玻璃边界及光滑室内表面产生的镜面眩光常会破坏主动立体RGB-D深度测量，导致占据栅格代价地图中累积形成持续性的幻影障碍物空洞与尖峰。本文提出一种基于显式深度可靠性建模的防眩光代价地图构建方法。轻量级深度可靠性网络（DRM-Net）可预测镜面干扰下逐像素测量的可信度，而可靠性引导的加权门控融合机制（RGF）能在错误测量值累积到地图前调节占据状态更新。为支撑鲁棒训练与评估，该方法采用位姿对齐的多视角参考深度构建技术以降低循环监督偏差，并通过融合变体消融实验、参数敏感性分析、跨条件测试、配对导航对比、可靠性地图指标评估及嵌入式运行时性能分析进行验证。在配备Intel RealSense D435与Jetson Orin Nano的真实移动机器人平台上的实验表明，该方法能减少虚假障碍物插入、提升自由空间保持能力，并在反光地板、玻璃墙及自然光眩光条件下维持实时吞吐量。这些结果支持将眩光视为测量可靠性问题而非密集深度补全问题，用于安全关键型室内导航。

---

