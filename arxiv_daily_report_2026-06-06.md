# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-06-06 08:03

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 3/20 篇提供

**🌟 Highlight**: 20 篇 | **📌 Poster**: 0 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. TempoVLA: Learning Speed-Controllable Vision-Language-Action Policies

- **作者**: Dong Jing, Jingchen Nie, Tianqi Zhang, Jiaqi Liu, Huaxiu Yao, Zhiwu Lu, Mingyu Ding
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.06491v1)
- **发表日期**: 2026-06-04
- **匹配关键词**: vision-language-action, VLA, vision-language-action model
- **arXiv**: [2606.06491v1](http://arxiv.org/abs/2606.06491v1)
- **📥 PDF**: 已下载至本地 (`2606.06491v1_TempoVLA_Learning_Speed-Controllable_Vision-Language-Action_Policies.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 机器人操作在低风险过渡阶段需要快速执行，而在高风险接触阶段则要求缓慢精确的运动。然而，现有的视觉-语言-动作模型（VLAs）仅能从训练示范中继承单一的固定速度。此前通过模型压缩、KV缓存复用或强化学习加速VLA的方法，仅能将策略从一种固定速度切换至另一种，而减速控制几乎未被探索。我们观察到，每个预测动作的幅值本身已决定了机器人的移动速度，这为可控执行速度提供了直接路径。基于此发现，我们提出TempoVLA——一种通过显式条件控制执行速度的单一VLA模型。TempoVLA包含两个耦合组件：（1）数据端的变速轨迹增强（VSTA），通过合并或拆分动作并保持运动语义，将示范重新定时至任意目标速度；（2）模型端的速度条件机制，将速度信息输入策略网络。统计表明，VSTA能以可忽略的运动误差达到指定速度。仿真与真实世界任务实验证明，TempoVLA实现了双向灵活的速度控制，而VSTA通过更优的数据利用进一步提升了默认1倍速性能。此外，通过与大型多模态模型协同，TempoVLA实现了动态速度控制——在低风险阶段加速，在高风险阶段减速。

---

### 2. AffordanceVLA: A Vision-Language-Action Model Empowering Action Generation through Affordance-Aware Understanding

- **作者**: Qize Yu, Jiadi You, Yuran Wang, Jiaqi Liang, Bowen Ping, Yang Tian, Yue Chen, Minghong Cai, Zeying Gong, Ruihai Wu, Yinchuan Li, Junwei Liang, Yingcong Chen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.06155v1)
- **发表日期**: 2026-06-04
- **匹配关键词**: vision-language-action, VLA, vision-language-action model, affordance
- **arXiv**: [2606.06155v1](http://arxiv.org/abs/2606.06155v1)
- **📥 PDF**: 已下载至本地 (`2606.06155v1_AffordanceVLA_A_Vision-Language-Action_Model_Empowering_Action_Generation_through_Affordance-Aware_U.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型利用预训练视觉-语言模型（VLM）丰富的世界知识，实现了遵循指令的机器人操作。然而，VLM语义空间与具身控制策略之间的结构不匹配往往阻碍了精确感知-动作映射的学习。为解决这一挑战，我们提出**AffordanceVLA**——一个统一框架，通过引入结构化可供性预测作为面向任务的中间表征，建立更精确、鲁棒的感知-动作映射。具体而言，我们通过三个互补组件逐步建模操作先验：1）**Which2Act**：通过视觉潜在预测实现以物体为中心的定位，抑制干扰；2）**Where2Act**：通过可供性图估计实现二维交互定位；3）**How2Act**：通过三维几何推理引导操作策略。这些可供性线索提供了空间锚定、语义条件化和动作耦合的中间表征，从而自然桥接视觉、语言与动作。我们将这些模块集成到具有专门专家的混合Transformer（MoT）架构中，并采用渐进式数据课程的三阶段训练策略进行模型训练。为解决机器人数据集中密集可供性标签稀缺的问题，我们还开发了稳健的自动化数据增强流水线。在仿真和真实环境中的大量实验表明，AffordanceVLA在多种操作场景中均展现出卓越性能。

---

### 3. L-SDPPO: Policy Optimization of Spiking Diffusion Policy for Intra-vehicular Robotic Manipulation

- **作者**: Liwen Zhang, Dong Zhou, Guanghui Sun, Yifei Zheng, Yuhui Hu, Kaihong Ouyang, Zuoquan Zhao
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.06049v1)
- **发表日期**: 2026-06-04
- **匹配关键词**: diffusion policy
- **arXiv**: [2606.06049v1](http://arxiv.org/abs/2606.06049v1)
- **📥 PDF**: 已下载至本地 (`2606.06049v1_L-SDPPO_Policy_Optimization_of_Spiking_Diffusion_Policy_for_Intra-vehicular_Robotic_Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 航天器舱内机器人有助于减轻宇航员工作负荷并提升任务效率。近期研究聚焦于利用深度学习方法实现这些复杂环境中的精准操控。然而，在无重力阻尼条件下，物体呈现不可预测、无约束的漂移特性。这些因素要求系统具备应对复杂多模态动作分布的鲁棒性。扩散策略（DP）虽能建模此类复杂动作，但其迭代采样过程对航天器有限能源预算而言能耗过高。为此，我们提出低能耗舱内机器人操控框架L-SDPPO，该框架采用强化学习（RL）算法优化脉冲扩散策略（SDP）。此外，针对微重力环境下动态时空特征感知不足的问题，我们提出状态依赖延迟注入（SDLI）机制，通过模拟生物神经延迟动态调节输入信息的时序。在五项典型舱内日常任务（如舱门开启、精密容器封盖）的评估中，与现有最优机器人操控方法相比，本方法始终实现更高成功率与更低能耗。实验结果表明，该方法是一种可行的舱内机器人操控方案。

---

### 4. World-Language-Action Model for Unified World Modeling, Language Reasoning, and Action Synthesis

- **作者**: Yi Yang, Zhihong Liu, Siqi Kou, Yiyang Chen, Yanzhe Hu, Jianbo Zhou, Boyuan Zhao, Zhijie Wei, Xiao Xia, Xueqi Li, Pengfei Liu, Zhijie Deng
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.05979v1)
- **发表日期**: 2026-06-04
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2606.05979v1](http://arxiv.org/abs/2606.05979v1)
- **📥 PDF**: 已下载至本地 (`2606.05979v1_World-Language-Action_Model_for_Unified_World_Modeling,_Language_Reasoning,_and_Action_Synthesis.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出世界-语言-动作（WLA）模型，作为一类新的具身基础模型。WLA以文本指令、图像和机器人状态为输入，联合预测文本子任务、子目标图像和机器人动作，融合了世界-动作模型（WAM）中通过大规模自我中心视频学习的**世界建模接口**，以及视觉-语言-动作（VLA）模型中解决复杂长时任务的**语言推理能力**。WLA的核心是一个**自回归（AR）Transformer**主干网络（而非WAM中的双向扩散Transformer），用于预测**下一状态**，包含**语义层面**的文本意图和互补的**细粒度**物理动态。物理动态通过基于专用世界专家（World Expert）的世界建模目标进行监督，并用于简化动作专家（Action Expert）的状态-动作相关性表征。WLA利用元查询使世界预测**隐式地**影响动作生成，从而在推理时可禁用前者。世界预测也可被激活以实现测试时扩展，提升机器人控制性能。我们的WLA-0原型模型（含2B活跃参数）在NVIDIA RTX 5090上每次推理仅需40毫秒。在模拟和真实环境中的评估表明，WLA-0实现了最先进的多任务和长时学习能力，例如在RoboTwin2.0 Clean上成功率达92.94%，在RMBench上成功率达56.5%。WLA-0还具备直接从**跨具身机器人视频**（无需动作标注）学习新任务的潜力。

---

### 5. PiL-World: A Chunk-Wise World Model for VLA Policy-in-the-Loop Evaluation

- **作者**: Chong Ma, Taiyi Su, Jian Zhu, Jianjun Zhang, Zitai Huang, Yi Xu, Hanli Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.05773v1)
- **发表日期**: 2026-06-04
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2606.05773v1](http://arxiv.org/abs/2606.05773v1)
- **📥 PDF**: 已下载至本地 (`2606.05773v1_PiL-World_A_Chunk-Wise_World_Model_for_VLA_Policy-in-the-Loop_Evaluation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）策略在真实机器人任务中以闭环方式运行：机器人观察场景，执行一个动作片段，并根据执行结果产生的观测来调整下一步决策。然而，现有的大多数用于机器人动作评估的世界模型仅限于沿预采集动作轨迹进行开环预测。这导致它们无法支持闭环VLA评估——因为每个动作片段必须基于前序执行产生的观测来调整。为解决这一局限，我们提出PiL-World——一种专为策略参与式闭环VLA评估设计的片段级世界模型。给定当前观测和VLA策略生成的动作轨迹，PiL-World能生成与VLA执行过程一致的多视角未来观测，并匹配策略所需的图像输入。通过交替进行VLA推理与世界模型预测，PiL-World无需每一步都依赖真实机器人执行即可实现闭环评估。为提升生成轨迹的保真度，PiL-World将视频生成过程与两类信息进行条件约束：来自头部视角机器人运动的动作驱动视觉控制信号，以及编码任务执行上下文的潜在历史状态，同时联合预测互补的多视角观测。除成功遥操作演示外，该模型还能从失败执行轨迹中学习，使生成的想象轨迹更贴合真实策略执行的数据分布。我们在三项真实双臂操作任务上评估了PiL-World。实验表明，PiL-World生成的想象轨迹与真实机器人执行结果高度一致。更重要的是，与基线方法相比，它将真实环境执行与闭环世界模型评估之间VLA成功率的测量误差从63.2%降低至12.0%。

---

### 6. DRIFT: A Residual Flow Adapter for Decoding Continuous Outputs in Vision-Language Models

- **作者**: Zhuoming Liu, Jinhong Lin, Kwan Man Cheng, Lin Zhang, Shayok Bagchi, Yin Li
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.05758v1)
- **发表日期**: 2026-06-04
- **匹配关键词**: VLA
- **arXiv**: [2606.05758v1](http://arxiv.org/abs/2606.05758v1)
- **📥 PDF**: 已下载至本地 (`2606.05758v1_DRIFT_A_Residual_Flow_Adapter_for_Decoding_Continuous_Outputs_in_Vision-Language_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 许多现代视觉-语言模型（VLM）依赖于离散令牌的自回归解码。尽管基于文本的输出接口支持可扩展的预训练，并在各类任务中展现出强大的零样本泛化能力，但它们难以胜任需要精确连续输出的问题，例如定位事件的时间边界或生成机器人控制动作。为应对这一挑战，我们提出DRIFT——一个将预训练VLM适配至连续解码任务的通用框架。DRIFT结合了基础预测器（提供目标输出的粗略估计）与基于流匹配的生成式精化模块（通过迭代优化改进预测）。这种残差公式将生成建模问题从学习全局输出分布转化为在强先验条件下建模局部残差分布，显著简化了优化过程。我们在感知与规划任务（包括视觉定位和机器人控制）上评估了DRIFT。在涵盖多模态大语言模型（MLLM）、视觉-语言-动作模型（VLA）和世界动作模型（WAM）的多种任务与架构中，DRIFT始终优于一系列基于回归和生成方法的强基线方案。

---

### 7. Let It Be Simple: One-Step Action Generation for Vision-Language-Action Models

- **作者**: Yitong Chen, Shiduo Zhang, Jingjing Gong, Xipeng Qiu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.05737v1)
- **发表日期**: 2026-06-04
- **匹配关键词**: vision-language-action, VLA, vision-language-action model
- **arXiv**: [2606.05737v1](http://arxiv.org/abs/2606.05737v1)
- **📥 PDF**: 已下载至本地 (`2606.05737v1_Let_It_Be_Simple_One-Step_Action_Generation_for_Vision-Language-Action_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 基于扩散的视觉-语言-动作（VLA）模型常继承图像生成视角：动作通过迭代去噪生成。我们认为VLA动作生成具有不同的条件-目标结构：策略以丰富的观测、语言和状态为条件，但仅预测紧凑的低维动作片段。在这种非对称性下，强单步动作生成未必需要采用为图像合成开发的高级单步方法。我们保留标准速度预测，不添加教师模型、蒸馏阶段或辅助目标；核心方案仅是将训练时间分布向高噪声状态偏移。我们首先在受控的MNIST网格到序列任务中隔离该效应，随后通过大量机器人策略实验进行验证。在标准LIBERO、LIBERO-Plus和LIBERO-Pro基准上，采用高噪声偏置调度训练的单步策略通常匹配相同方案下的十步解码性能，且在标准LIBERO上可超越均匀时间分布训练的十步策略。真实机器人双臂YAM RSS评估通过小样本跨架构验证了相同采样器趋势。在配备30M动作头的1.4B视觉语言模型上，单步解码在LIBERO-Long任务中达到95.6%的成功率。这些结果表明，无需引入为图像生成开发的完整少步扩散机制，标准扩散训练即可涌现出强大的单步VLA动作生成能力。

---

### 8. Accelerating and Scaling MPC-Guided Reinforcement Learning for Humanoid Locomotion and Manipulation

- **作者**: Junheng Li, Liang Wu, Sergio A. Esteban, Lizhi Yang, Ján Drgoňa, Aaron D. Ames
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.05687v1)
- **发表日期**: 2026-06-04
- **匹配关键词**: locomotion and manipulation
- **arXiv**: [2606.05687v1](http://arxiv.org/abs/2606.05687v1)
- **📥 PDF**: 已下载至本地 (`2606.05687v1_Accelerating_and_Scaling_MPC-Guided_Reinforcement_Learning_for_Humanoid_Locomotion_and_Manipulation.pdf`)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/junhengl/mpc-rl.
- **中文摘要**: 在仿人运动控制领域，模型预测控制（MPC）提供了基于物理的预测与约束处理能力，而强化学习（RL）则通过大规模仿真实现鲁棒的全身体技能。然而，在强化学习框架内集成MPC通常需要耗费大量时间构建问题模型或产生过高的训练开销，这使得此类框架在实际应用中难以体现其价值。本研究提出一种高效的训练阶段MPC引导方法（称为MPC-RL），用于仿人运动与操作任务。我们引入基于质心动力学的MPC奖励函数，在训练阶段利用MPC轨迹的引导信息。为使其适用于大规模并行强化学习，我们开发了πⁿMPC——一种基于并行时间域、免构建的批量GPU MPC求解器，可直接处理时变动力学问题，避免高内存占用与预编译需求。通过多项对比实验与硬件验证，我们发现MPC-RL在运动与操作技能上展现出卓越性能。相关代码已开源：https://github.com/junhengl/mpc-rl。

---

### 9. FlowPRO: Reward-Free Reinforced Fine-Tuning of Flow-Matching VLAs via Proximalized Preference Optimization

- **作者**: Yihao Wu, He Zhang, Junbo Tan, Xueqian Wang, Zhengyou Zhang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.05468v1)
- **发表日期**: 2026-06-03
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2606.05468v1](http://arxiv.org/abs/2606.05468v1)
- **📥 PDF**: 已下载至本地 (`2606.05468v1_FlowPRO_Reward-Free_Reinforced_Fine-Tuning_of_Flow-Matching_VLAs_via_Proximalized_Preference_Optimiz.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 将训练后的视觉-语言-动作（VLA）模型转化为可在真实机器人上可靠部署的策略，仍是当前的主要瓶颈。SFT和DAgger仅能间接利用失败信号，而基于奖励的强化学习则受限于真实世界奖励设计的难度以及训练可靠评论家的困难。我们提出FlowPRO——一种面向流匹配VLA的无奖励离线强化微调框架。在算法层面，我们提出RPRO（机器人流匹配近端偏好优化），这是一种针对VLA模型流匹配动作头量身定制的偏好优化目标。RPRO将对比优化器与显式近端正则化器相结合，该正则化器锚定隐式奖励的绝对幅度，从而消除了普通Flow-DPO的奖励黑客失败模式。在数据层面，一种遥操作干预与回滚范式通过单一操作员动作在真实机器人上生成自然配对的正面与负面轨迹$(τ^w, τ^l)$；结合批量混合的平滑插值过程，将这些稀疏修正转化为密集的逐状态监督，同时保持基础策略的能力。在四项长时程双臂任务中，FlowPRO取得了最高成功率，优于四种代表性基线，消融实验证实了每个损失组件的贡献。

---

### 10. MoDex: A Diffusion Policy for Sequential Multi-Object Dexterous Grasping

- **作者**: Haofei Lu, Hongjia Liu, Yifei Dong, Florian T. Pokorny, Jens Lundell, Danica Kragic
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.05407v1)
- **发表日期**: 2026-06-03
- **匹配关键词**: dexterous grasping, diffusion policy
- **arXiv**: [2606.05407v1](http://arxiv.org/abs/2606.05407v1)
- **📥 PDF**: 已下载至本地 (`2606.05407v1_MoDex_A_Diffusion_Policy_for_Sequential_Multi-Object_Dexterous_Grasping.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://modex2026.github.io/.
- **中文摘要**: 本研究针对使用单只灵巧手在不释放已抓取物体的情况下，依次抓取多个物体的任务。现有大多数灵巧抓取方法将手部所有自由度都用于抓取单个物体，未能充分利用其灵巧性，且无法为后续抓取保留冗余能力。本文提出的解决方案MoDex是一种扩散策略，可直接根据观测信息预测下一个夹爪位姿，并以对向空间和点云作为条件约束。其中，对向空间条件用于指定当前抓取中参与的手指，使夹爪仅使用部分可用自由度，同时为后续抓取保留剩余自由度。为实现仿真到现实的迁移，MoDex采用两阶段训练：首先通过专家示范的模仿学习进行预训练，随后通过强化学习微调，持续提升预训练策略的成功率。我们在基于MuJoCo的Franka Emika Panda机器人（配备Allegro Hand）仿真环境及对应真实硬件平台上评估了MoDex。在仿真与真实实验中，MoDex均取得了优于所评估的基于学习的基线方法的成功率，性能分别提升2.92%-17.92%和6.67%-17.78%。项目页面：https://modex2026.github.io/。

---

### 11. GRAIL: Generating Humanoid Loco-Manipulation from 3D Assets and Video Priors

- **作者**: Tianyi Xie, Haotian Zhang, Jinhyung Park, Zi Wang, Bowen Wen, Jiefeng Li, Xueting Li, Qingwei Ben, Haoyang Weng, Yufei Ye, David Minor, Tingwu Wang, Chenfanfu Jiang, Sanja Fidler, Jan Kautz, Linxi Fan, Yuke Zhu, Zhengyi Luo, Umar Iqbal, Ye Yuan ⭐
  - **高亮作者**: Yuke Zhu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.05160v1)
- **发表日期**: 2026-06-03
- **匹配关键词**: object manipulation
- **arXiv**: [2606.05160v1](http://arxiv.org/abs/2606.05160v1)
- **📥 PDF**: 已下载至本地 (`2606.05160v1_GRAIL_Generating_Humanoid_Loco-Manipulation_from_3D_Assets_and_Video_Priors.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 扩展人形机器人全身操作与移动能力，需要覆盖多样化物体、全身动作及场景几何形态的机器人兼容演示数据。然而，遥操作与动作捕捉技术难以规模化应用，因为每次数据采集都依赖于物理设备、穿戴传感器的演员及机器人操作。我们提出GRAIL——一种在部署前完全保持虚拟化的数字生成管线：通过组合3D资产、仿真就绪场景及视频基础模型先验知识，无需重建物理环境或远程操控机器人即可合成交互动作。不同于对无约束野外视频进行重建，GRAIL从完全指定的3D配置出发，在视频生成前即明确物体几何、相机参数、度量尺度、环境深度及机器人比例角色，并在重建阶段复用这些信息。这种特权化设置优化了4D恢复条件，通过基于模型的物体追踪、人体运动估计及交互感知优化，重建出度量级4D人-物交互轨迹，有效降低深度模糊性与形态错配。我们将恢复的运动重定向至人形机器人，并训练互补的任务通用追踪器：面向操作的物体感知潜在适配器与面向地形穿越的场景感知追踪器。GRAIL生成了超过20,000个序列，涵盖抓取、物体操作、坐姿及地形穿越。仅使用GRAIL生成数据，我们通过仿真到现实管线训练以自我为中心的视觉策略，并将其部署至Unitree G1人形机器人，在多样化物体抓取任务中实现84%的真实世界成功率，在爬楼梯任务中达到90%的成功率。

---

### 12. MPCoT: Reward-Guided Multi-Path Latent Reasoning for Test-Time Scalable Vision-Language-Action

- **作者**: Boyang Zhang, Lianlei Shan
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.06245v1)
- **发表日期**: 2026-06-04
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2606.06245v1](http://arxiv.org/abs/2606.06245v1)
- **📥 PDF**: 已下载至本地 (`2606.06245v1_MPCoT_Reward-Guided_Multi-Path_Latent_Reasoning_for_Test-Time_Scalable_Vision-Language-Action.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）策略在长时域和高不确定性控制中仍显脆弱，其单次动作解码提供的推理时推演能力有限。显式思维链虽能提升推理深度，但会引入令牌延迟和间接的文本-动作接口。我们提出MPCoT，一种奖励引导的多路径潜在推理框架：初始化M条假设路径，经K次权重共享步骤迭代优化，在动作解码前进行软聚合。训练阶段独有的路径偏好目标函数，通过专家动作一致性、基于世界模型/视觉语言模型的进展评估及成功反馈，对候选动作分支进行评价，从而将潜在路径评分器与下游执行质量对齐。MPCoT保持原始8步动作接口，零推理令牌生成，并暴露可配置的推理控制参数（K,M）。在LIBERO和CALVIN基准的匹配协议下，MPCoT提升了长时域任务性能，消融实验验证了深度-宽度效应、置信加权聚合及奖励引导路径监督的有效性。

---

### 13. WorldFly: A World-Model-Based Vision-Language-Action Model for UAV Navigation

- **作者**: Shengtao Zheng, Kai Li, Weichen Zhang, Yu Meng, Chen Gao, Xinlei Chen, Yong Li, Xiao-Ping Zhang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.06147v1)
- **发表日期**: 2026-06-04
- **匹配关键词**: vision-language-action, navigation, VLA, vision-language-action model
- **arXiv**: [2606.06147v1](http://arxiv.org/abs/2606.06147v1)
- **📥 PDF**: 已下载至本地 (`2606.06147v1_WorldFly_A_World-Model-Based_Vision-Language-Action_Model_for_UAV_Navigation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 端到端的视觉-语言-动作（VLA）模型在无人机导航领域展现出应用潜力。然而，现有方法通常依赖历史观测直接预测动作，在密集城市环境中常面临挑战——严重遮挡与急转弯导致视角剧烈切换。我们认为，世界模型所固有的"想象"未来状态的能力，对于在部分可观测条件下实现鲁棒决策至关重要。为此，我们构建了具有挑战性的城市峡谷穿越基准测试，专门评估在严重遮挡与视角剧烈切换场景中的空间理解能力。基于此，我们提出WorldFly——一种基于世界模型的新型VLA框架，采用双分支耦合流匹配机制联合生成未来视频预测与导航动作，通过空间想象显式引导智能体策略。在基准测试上的大量评估表明，WorldFly在未知环境中尤其优于其他基线方法，验证了将世界模型融入具身空中智能体的有效性。

---

### 14. Texture-preserving implicit neural representation for Cone beam CT truncated reconstruction

- **作者**: Genyuan Zhang, Junyao Wang, Haoran Lan, Chuandong Tan, Songtao Zhu, Fenglin Liu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.06039v1)
- **发表日期**: 2026-06-04
- **匹配关键词**: 3D reconstruction, 3d reconstruction, neural scene representation
- **arXiv**: [2606.06039v1](http://arxiv.org/abs/2606.06039v1)
- **📥 PDF**: 已下载至本地 (`2606.06039v1_Texture-preserving_implicit_neural_representation_for_Cone_beam_CT_truncated_reconstruction.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 锥束计算机断层扫描（CBCT）常因数据截断而产生严重伪影，并限制有效视野（FOV）。现有用于截断CBCT重建的深度学习方法存在显著局限，包括严格依赖有监督的真实数据，以及未能考虑连续三维空间截断变化。为解决这些挑战，我们提出了一种基于神经场景表示的自监督三维重建框架。通过将空间坐标直接映射到投影监督下的辐射密度，该方法本质上绕过了传统的滤波和反投影操作，从而从根本上消除了截断引起的环状伪影，同时实现了鲁棒的连续三维数据外推。然而，坐标网络易受固有频谱偏差影响，导致临床关键的高频纹理严重丢失。为突破这一瓶颈，我们进一步在神经场景表示架构中引入基于物理的迭代优化模块。利用坐标网络生成的无伪影外推体数据作为最优初始化，该模块逐步从原始投影中重新提取高频结构信息并将其注入体数据。在模拟和真实数据集上的大量实验表明，我们的方法成功统一了神经网络卓越的伪影抑制与外推能力，以及迭代算法的高保真细节保留特性。

---

### 15. Deep Learning-based 3D Oral Cavity Reconstruction Using 2D Intraoral Images

- **作者**: Jihun Cho, Soo-Yeon Jeong, Eun-Jeong Bae, Sun-Young Ihm
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.05998v1)
- **发表日期**: 2026-06-04
- **匹配关键词**: 3D reconstruction, 3d reconstruction
- **arXiv**: [2606.05998v1](http://arxiv.org/abs/2606.05998v1)
- **📥 PDF**: 已下载至本地 (`2606.05998v1_Deep_Learning-based_3D_Oral_Cavity_Reconstruction_Using_2D_Intraoral_Images.pdf`)
- **🔓 开源**: CODE
- **中文摘要**: 口腔三维建模是牙科诊疗中最关键的环节之一，目前常用的方法包括取模和口内扫描，但两者均存在显著局限性。取模需将藻酸盐或硅橡胶材料置于托盘后置入口腔形成阴模，不仅令患者产生明显不适，还易出现材料形变误差，且存储运输困难。口内扫描仪采用结构光或激光技术实时直接扫描口腔结构，虽能获得先进效果，但设备成本极为高昂。针对上述问题，本文提出一种基于软件的解决方案，仅需从不同角度拍摄十张二维口内图像即可重建三维口腔模型，无需专用硬件设备。该方法可降低成本、免除物理扫描设备需求、减轻患者不适感，并实现自动化三维重建。模型基于公开数据集Dental3DS（含950个上颌样本）训练，采用MobileNetV2作为图像编码器，结合多头注意力机制进行多视角特征融合。在最近邻匹配距离阈值设为0.035的条件下，模型准确率达77.49%。但预测顶点倾向于集中在真实值的高密度区域，导致重建模型点云分布不均匀。

---

### 16. LiAuto-GeoX: Efficient Grounded Driving Transformer

- **作者**: Jiawei Lian, Haoyi Sun, Yang Wu, Lifu Mu, Siyuan Wang, Le Hui, Ning Mao, Tao Wei, Pan Zhou, Kun Zhan, Jian Yang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.05774v1)
- **发表日期**: 2026-06-04
- **匹配关键词**: 3D reconstruction, 3d reconstruction
- **arXiv**: [2606.05774v1](http://arxiv.org/abs/2606.05774v1)
- **📥 PDF**: 已下载至本地 (`2606.05774v1_LiAuto-GeoX_Efficient_Grounded_Driving_Transformer.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 密集三维重建在空间理解方面展现出巨大潜力，但其作为自动驾驶实时车载表征的可行性仍是一个开放挑战。现有大规模视觉几何模型通常需要大量计算资源，且缺乏动态驾驶环境所需的远距离几何保真度、环视一致性和实时效率。为弥合这一差距，我们提出\textbf{LiAuto-GeoX}——一种专为可部署的自我中心三维场景理解设计的高效接地驾驶Transformer。该方法首先利用大规模环视数据学习高容量驾驶几何模型，通过稀疏激光雷达先验为远距离、模糊或结构稀疏区域提供稳健的几何接地。随后，通过新颖的几何保持蒸馏框架，将这一能力实例化为高度紧凑的1.55亿参数车载模型。该框架采用掩码引导的深度感知蒸馏，通过强调几何信息丰富区域保留细粒度度量结构；并利用相对位姿关系蒸馏，通过位姿诱导的几何关系强制执行跨视角空间一致性。大量评估表明，\textbf{LiAuto-GeoX}在KITTI数据集上以220 FPS运行，同时保持高保真密集重建，实现实时部署。所学几何特征无缝迁移至下游自主任务，在轨迹预测中达到90.6 PDMS，在占用预测中达到24.63 mIoU，在未来帧预测中达到47.67 IoU。这些成果共同证明，高效密集三维重建可超越其作为感知目标的传统角色，成为下一代自动驾驶可扩展的基础几何表征。

---

### 17. Robust Scene Transfer for PointGoal Navigation via Privileged Sensor Guided Contrastive Learning

- **作者**: Amirhossein Zhalehmehrabi, Tiziano Tezze, Alberto Castelini, Alessandro Farinelli
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.05506v1)
- **发表日期**: 2026-06-03
- **匹配关键词**: navigation
- **arXiv**: [2606.05506v1](http://arxiv.org/abs/2606.05506v1)
- **📥 PDF**: 已下载至本地 (`2606.05506v1_Robust_Scene_Transfer_for_PointGoal_Navigation_via_Privileged_Sensor_Guided_Contrastive_Learning.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出了一种基于传感器引导的自适应对比学习框架，用于PointGoal导航中的视觉表征学习。在训练过程中，特权激光雷达传感通过几何感知相似度度量和自适应温度缩放来引导对比目标，促使视觉嵌入捕捉与导航相关的结构信息，而非场景特定的外观特征。由此产生的编码器独立预训练后冻结，作为强化学习的感知主干网络，将表征学习与策略优化解耦。我们进一步在表征预训练与策略学习之间引入跨阶段域不匹配，以抑制环境特定捷径，促进对任务相关特征的依赖。

在高保真仿真中的大量实验表明，我们的方法显著提升了策略在不同室内外环境中的场景迁移能力。在部署阶段，智能体仅依赖单目RGB观测以及目标位置、本体感知信号等标准任务相关输入，无需激光雷达或其他特权传感器。在严重外观和语义偏移条件下，我们的方法优于大型预训练视觉模型和标准对比学习基线。我们还发布了一个多模态数据集，以支持未来关于导航中特权引导视觉表征学习的研究。代码已开源：

---

### 18. Unpaired RGB-Thermal Gaussian-Splatting Using Visual Geometric Transformers

- **作者**: Jean Cordonnier, Chenghao Xu, Olga Fink, Malcolm Mielle
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.05491v1)
- **发表日期**: 2026-06-03
- **匹配关键词**: 3D gaussian splatting, gaussian splatting
- **arXiv**: [2606.05491v1](http://arxiv.org/abs/2606.05491v1)
- **📥 PDF**: 已下载至本地 (`2606.05491v1_Unpaired_RGB-Thermal_Gaussian-Splatting_Using_Visual_Geometric_Transformers.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 多模态新颖视角合成（NVS）结合RGB与热成像技术，能够利用视觉和热信息实现精确的三维场景重建。然而，现有方法通常依赖精确标定的RGB-热图像对或立体装置，限制了其可扩展性和实际部署。为解决这一问题，我们提出了一种非配对RGB-热NVS框架，该框架利用VGGT（一种三维前馈Transformer架构）独立估计每种模态的相机位姿。随后，通过Procrustes算法结合跨模态特征匹配器对齐位姿集合，从而无需配对标定即可实现联合配准。基于此对齐，我们进一步提出一种多模态三维高斯泼溅方法，可直接从非配对的RGB和热图像中学习。在多种场景上的实验表明，我们的方法在保持RGB保真度的同时，在热视角合成中取得了具有竞争力的性能。此外，我们证明现有重建方法生成的模态特定重建缺乏跨模态一致性。为此，我们引入了一个基准测试框架，以严格评估各模态图像合成质量及重建场景的多模态一致性。

---

### 19. WAM-Nav: Asymmetric Latent World-Action Modeling for Unified Visual Navigation

- **作者**: Ning Yang, Yan Huang, Kaiwen Peng, Ziheng He, Kai Wang, Cui Miao, Kailin Lyu, Guo Li, Xiaofeng Wang, Zheng Zhu, Jing Liu, Nianfeng Liu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.04907v1)
- **发表日期**: 2026-06-03
- **匹配关键词**: navigation, visual navigation, exploration, point-goal navigation
- **arXiv**: [2606.04907v1](http://arxiv.org/abs/2606.04907v1)
- **📥 PDF**: 已下载至本地 (`2606.04907v1_WAM-Nav_Asymmetric_Latent_World-Action_Modeling_for_Unified_Visual_Navigation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉导航需要在复杂的几何与物理约束下生成平滑且无碰撞的轨迹。现有将观测直接映射为动作的反应式策略缺乏前瞻性推理能力，限制了其主动避障的性能。尽管视觉想象能提供预测性预判，但传统模块化方法将场景预测与策略学习分离，常导致误差累积和推理效率低下。为解决上述局限，我们提出WAM-Nav——一种面向具身视觉导航的隐式世界-动作联合模型，该模型同步学习动作生成与隐式视觉预判，在不牺牲推理效率的前提下实现更鲁棒且具前瞻性的导航决策。具体而言，WAM-Nav采用共享扩散Transformer进行非对称联合扩散，同时生成长时域动作与短时域视觉预判，有效降低多步自回归推演中固有的推理延迟与视觉误差累积。为进一步促进轨迹生成的平滑性与一致性，我们引入双流上下文条件机制，将回合级自运动历史与序列化视觉观测相融合。结合统一目标对齐模块（该模块可保持不同目标类型间的均衡表征），WAM-Nav在单一策略中自然支持图像目标导航、点目标导航与无目标探索。在具有挑战性的ClutterScenes与InternScenes基准上的大量实验表明，WAM-Nav展现出强大的泛化能力，尤其在图像目标导航与点目标导航任务中，成功率分别提升15.7%和3.3%。实际场景部署进一步验证了其零样本仿真到现实迁移的有效性，在多样化室内外环境中实现了平均85%的任务成功率。

---

### 20. Recent Advances and Trends in Learning-based 3D Representations

- **作者**: Adrien Schockaert, Hamid Laga, Hazem Wannous, Vincent Magnier, Guillaume Dufaye, Jean-françois Witz
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.04871v1)
- **发表日期**: 2026-06-03
- **匹配关键词**: implicit representation, 3d reconstruction, robot navigation, gaussian splatting, 3D gaussian splatting, neural rendering, 3D reconstruction, navigation
- **arXiv**: [2606.04871v1](http://arxiv.org/abs/2606.04871v1)
- **📥 PDF**: 已下载至本地 (`2606.04871v1_Recent_Advances_and_Trends_in_Learning-based_3D_Representations.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 选择合适的3D表示是决定现代计算机视觉与图形学管线效率、质量及能力的基础性设计决策，其应用涵盖三维重建、新视角合成与渲染、形状与运动分析、识别及生成等任务。尽管传统表示方法（如网格、点云和体素网格）仍是3D传感器（如激光雷达和三维扫描仪）的标准输出格式，并广泛应用于下游应用（如编辑与仿真），但基于神经网络的基元表示方法（如3D高斯泼溅）提供了紧凑且可微分的替代方案，为游戏、AR/VR、自动驾驶、机器人导航及医学成像等领域开辟了广阔的应用前景。本文旨在系统梳理从离散显式格式到基于神经渲染或基元泼溅的连续隐式场等主要3D表示方法家族。针对每种表示类型，我们阐述其通用公式及变体形式，讨论其优势与局限性，并重点介绍关键应用场景。最后，我们通过概述当前面临的开放挑战与未来潜在研究方向来总结全文。与近期广泛覆盖3D物体与场景重建的综述不同，本文聚焦于3D表示方法本身的演进脉络，特别强调向隐式表示的范式转变，为理解这些新兴格式如何根本性改变3D/4D工作流程提供全新视角。

---

