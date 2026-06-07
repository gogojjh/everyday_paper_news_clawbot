# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-06-07 08:01

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 3/20 篇提供

**🌟 Highlight**: 13 篇 | **📌 Poster**: 7 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. TempoVLA: Learning Speed-Controllable Vision-Language-Action Policies

- **作者**: Dong Jing, Jingchen Nie, Tianqi Zhang, Jiaqi Liu, Huaxiu Yao, Zhiwu Lu, Mingyu Ding
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.06491v1)
- **发表日期**: 2026-06-04
- **匹配关键词**: VLA, vision-language-action model, vision-language-action
- **arXiv**: [2606.06491v1](http://arxiv.org/abs/2606.06491v1)
- **📥 PDF**: 已下载至本地 (`2606.06491v1_TempoVLA_Learning_Speed-Controllable_Vision-Language-Action_Policies.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 机器人操作在低风险过渡阶段需要快速执行，而在高风险接触阶段则要求缓慢、精确的运动。然而，现有的视觉-语言-动作模型（VLAs）仅能从训练演示中继承单一的固定速度。此前通过模型压缩、KV缓存复用或强化学习来加速VLA的尝试，只是将策略从一种固定速度切换到另一种，而几乎未探索减速机制。我们观察到，每个预测动作的幅度本身已经决定了机器人的移动速度，这为可控执行速度开辟了直接路径。基于这一发现，我们提出了TempoVLA——一种执行速度可通过显式条件控制的单一VLA模型。TempoVLA结合了两个耦合组件：（1）数据侧的变速度轨迹增强（VSTA），通过合并或拆分动作来重新调整演示的时间分布至任意目标速度，同时保留其运动语义；（2）模型侧的条件机制，将速度信息输入策略网络。统计数据显示，VSTA能以可忽略的运动误差达到指定速度。仿真与真实世界任务的实验表明，TempoVLA实现了双向灵活的速度控制，而VSTA通过更优的数据利用进一步提升了默认1倍速的性能。此外，通过与大型多模态模型协作，TempoVLA实现了动态速度控制：在低风险阶段加速，在高风险阶段减速。

---

### 2. AffordanceVLA: A Vision-Language-Action Model Empowering Action Generation through Affordance-Aware Understanding

- **作者**: Qize Yu, Jiadi You, Yuran Wang, Jiaqi Liang, Bowen Ping, Yang Tian, Yue Chen, Minghong Cai, Zeying Gong, Ruihai Wu, Yinchuan Li, Junwei Liang, Yingcong Chen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.06155v1)
- **发表日期**: 2026-06-04
- **匹配关键词**: affordance, VLA, vision-language-action model, vision-language-action
- **arXiv**: [2606.06155v1](http://arxiv.org/abs/2606.06155v1)
- **📥 PDF**: 已下载至本地 (`2606.06155v1_AffordanceVLA_A_Vision-Language-Action_Model_Empowering_Action_Generation_through_Affordance-Aware_U.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型利用预训练视觉-语言模型（VLM）丰富的世界知识，实现遵循指令的机器人操作。然而，VLM语义空间与具身控制策略之间的结构不匹配，往往阻碍了精确感知-动作映射的学习。为解决这一挑战，我们提出**AffordanceVLA**——一个统一框架，通过引入结构化的可供性预测作为面向任务的中间表征，建立更精确、鲁棒的感知-动作映射。具体而言，我们通过三个互补组件逐步建模操作先验：1）**Which2Act**：通过视觉潜在预测实现以物体为中心的定位，抑制干扰；2）**Where2Act**：通过可供性图估计实现二维交互定位；3）**How2Act**：通过三维几何推理引导操作策略。这些可供性线索提供了空间锚定、语义条件化且与动作耦合的中间表征，从而自然桥接视觉、语言与动作。我们将这些模块集成到具有专门专家的混合Transformer（MoT）架构中，并采用渐进式数据课程的三阶段训练策略进行模型训练。为克服机器人数据集中密集可供性标签的稀缺性，我们还开发了鲁棒的自动化数据增强流水线。在仿真和真实环境中的大量实验表明，AffordanceVLA在多种操作场景中均展现出优异性能。

---

### 3. L-SDPPO: Policy Optimization of Spiking Diffusion Policy for Intra-vehicular Robotic Manipulation

- **作者**: Liwen Zhang, Dong Zhou, Guanghui Sun, Yifei Zheng, Yuhui Hu, Kaihong Ouyang, Zuoquan Zhao
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.06049v1)
- **发表日期**: 2026-06-04
- **匹配关键词**: diffusion policy
- **arXiv**: [2606.06049v1](http://arxiv.org/abs/2606.06049v1)
- **📥 PDF**: 已下载至本地 (`2606.06049v1_L-SDPPO_Policy_Optimization_of_Spiking_Diffusion_Policy_for_Intra-vehicular_Robotic_Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 航天器舱内机器人有助于减轻宇航员工作负担并提升任务效率。近期研究聚焦于利用深度学习方法实现这些复杂环境下的精准操控。然而，物体在无重力阻尼条件下会呈现不可预测的无约束漂移，这要求系统具备应对复杂多模态动作分布的鲁棒性。扩散策略虽能建模此类复杂动作，但其迭代采样过程对航天器有限的能源预算消耗过大。为此，我们提出低能耗舱内机器人操控框架L-SDPPO，该框架采用强化学习算法优化脉冲扩散策略。针对微重力环境下动态时空特征感知不足的问题，我们提出状态依赖延迟注入机制，通过模拟生物神经延迟动态调节输入信息时序。在五项典型舱内日常任务（如舱门开启、精密容器封盖）的评估中，与现有最优机器人操控方法相比，本方法始终实现更高成功率与更低能耗。实验结果表明，该方法是一种可行的舱内机器人操控方案。

---

### 4. World-Language-Action Model for Unified World Modeling, Language Reasoning, and Action Synthesis

- **作者**: Yi Yang, Zhihong Liu, Siqi Kou, Yiyang Chen, Yanzhe Hu, Jianbo Zhou, Boyuan Zhao, Zhijie Wei, Xiao Xia, Xueqi Li, Pengfei Liu, Zhijie Deng
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.05979v1)
- **发表日期**: 2026-06-04
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2606.05979v1](http://arxiv.org/abs/2606.05979v1)
- **📥 PDF**: 已下载至本地 (`2606.05979v1_World-Language-Action_Model_for_Unified_World_Modeling,_Language_Reasoning,_and_Action_Synthesis.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出世界-语言-动作（WLA）模型，作为一类新的具身基础模型。WLA以文本指令、图像和机器人状态为输入，联合预测文本子任务、子目标图像和机器人动作，融合了世界建模接口（从世界-动作模型（WAM）中学习大量自我中心视频）和语言推理能力（如视觉-语言-动作（VLA）模型解决复杂长时程任务）。WLA的核心是一个自回归（AR）Transformer主干网络，而非WAM中的双向扩散Transformer，用于预测下一状态，包括语义级别的文本意图和互补的细粒度物理动态。物理动态由基于专用世界专家的世界建模目标监督，并用于简化动作专家对状态-动作相关性的刻画。WLA利用元查询使世界预测隐式影响动作生成，从而在推理时可禁用前者。世界预测也可被激活以实现测试时扩展，提升机器人控制性能。我们的WLA-0原型拥有20亿活跃参数，在NVIDIA RTX 5090上每次推理仅需40毫秒。在模拟和真实环境中的评估表明，WLA-0实现了最先进的多任务和长时程学习能力，例如在RoboTwin2.0 Clean上成功率达92.94%，在RMBench上成功率达56.5%。WLA-0还具备直接从跨具身机器人视频中学习新任务（无需动作标注）的潜力。

---

### 5. PiL-World: A Chunk-Wise World Model for VLA Policy-in-the-Loop Evaluation

- **作者**: Chong Ma, Taiyi Su, Jian Zhu, Jianjun Zhang, Zitai Huang, Yi Xu, Hanli Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.05773v1)
- **发表日期**: 2026-06-04
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2606.05773v1](http://arxiv.org/abs/2606.05773v1)
- **📥 PDF**: 已下载至本地 (`2606.05773v1_PiL-World_A_Chunk-Wise_World_Model_for_VLA_Policy-in-the-Loop_Evaluation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）策略在真实机器人任务中以闭环方式运行：机器人观察场景，执行一个动作片段，并根据执行结果产生的观测来决定下一步动作。然而，现有用于机器人动作评估的世界模型大多局限于沿预采集动作轨迹进行开环预测，这使其无法支持闭环VLA评估——因为每个动作片段必须基于前次执行产生的观测来调整。为填补这一空白，我们提出PiL-World——一种专为策略在环VLA评估设计的片段级世界模型。给定当前观测和VLA策略生成的动作轨迹，PiL-World可生成与VLA执行过程一致的多视角未来观测，并匹配策略所需的图像输入。通过交替进行VLA推理与世界模型预测，PiL-World无需每步真实机器人执行即可实现闭环评估。为提升生成轨迹的保真度，PiL-World将视频生成条件建立在动作衍生的视觉控制信号（来自头部视角的机器人运动）和编码任务执行上下文的潜在历史状态之上，同时联合预测互补的多视角观测。除成功的遥操作演示外，该模型还能从失败执行轨迹中学习，使生成的想象轨迹更贴合真实策略执行的分布。我们在三个真实双臂操作任务上评估了PiL-World。实验表明，PiL-World生成的想象轨迹与真实机器人执行高度一致。更重要的是，与基线方法相比，它将真实环境执行与闭环世界模型评估测得的VLA成功率之间的误差从63.2%降低至12.0%。

---

### 6. DRIFT: A Residual Flow Adapter for Decoding Continuous Outputs in Vision-Language Models

- **作者**: Zhuoming Liu, Jinhong Lin, Kwan Man Cheng, Lin Zhang, Shayok Bagchi, Yin Li
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.05758v1)
- **发表日期**: 2026-06-04
- **匹配关键词**: VLA
- **arXiv**: [2606.05758v1](http://arxiv.org/abs/2606.05758v1)
- **📥 PDF**: 已下载至本地 (`2606.05758v1_DRIFT_A_Residual_Flow_Adapter_for_Decoding_Continuous_Outputs_in_Vision-Language_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 许多现代视觉-语言模型（VLM）基于离散标记的自回归解码构建。尽管基于文本的输出接口支持可扩展的预训练，并在多种任务中展现出强大的零样本泛化能力，但它们难以适用于需要精确连续输出的问题，例如定位事件的时间边界或生成机器人控制动作。为解决这一挑战，我们提出DRIFT——一种将预训练VLM适配至连续解码任务的通用框架。DRIFT结合了基础预测器（提供目标输出的粗略估计）与基于流匹配的生成式精化模块（通过迭代优化改进预测）。这种残差公式将生成建模问题从学习全局输出分布转化为在强先验附近建模局部残差分布，显著简化了优化过程。我们在感知与规划任务（包括视觉定位和机器人控制）上评估了DRIFT。在涵盖多模态大语言模型（MLLM）、视觉-语言-动作模型（VLA）和世界动作模型（WAM）的多种任务与架构中，DRIFT始终优于一系列强大的基于回归和生成的方法。

---

### 7. Let It Be Simple: One-Step Action Generation for Vision-Language-Action Models

- **作者**: Yitong Chen, Shiduo Zhang, Jingjing Gong, Xipeng Qiu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.05737v1)
- **发表日期**: 2026-06-04
- **匹配关键词**: VLA, vision-language-action model, vision-language-action
- **arXiv**: [2606.05737v1](http://arxiv.org/abs/2606.05737v1)
- **📥 PDF**: 已下载至本地 (`2606.05737v1_Let_It_Be_Simple_One-Step_Action_Generation_for_Vision-Language-Action_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 基于扩散的视觉-语言-动作（VLA）模型常继承图像生成的视角：动作通过迭代去噪生成。我们认为VLA动作生成具有不同的条件-目标结构：策略以丰富的观测、语言和状态为条件，但仅预测紧凑、低维的动作片段。在这种不对称性下，强单步动作生成未必需要采用为图像合成开发的先进单步方法。我们保留标准的速度预测，不添加教师模型、蒸馏阶段或辅助目标；主要方案中，仅将训练时间分布偏向高噪声状态。我们首先在受控的MNIST网格到序列任务中隔离该效应，随后通过大量机器人策略实验进行验证。在标准LIBERO、LIBERO-Plus和LIBERO-Pro上，采用高噪声偏向调度训练的单步策略通常匹配相同方案下的十步解码性能，且在标准LIBERO上可超越均匀时间分布训练的十步策略。真实机器人双臂YAM RSS评估以少量样本跨架构验证了相同的采样器趋势。在配备30M动作头的1.4B视觉语言模型上，单步解码在LIBERO-Long上达到95.6%的准确率。这些结果表明，无需引入为图像生成开发的完整少步扩散机制，通过标准扩散训练即可实现强单步VLA动作生成。

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
- **中文摘要**: 在人形运动控制中，模型预测控制（MPC）提供了基于物理的预测和约束处理能力，而强化学习（RL）则通过大规模仿真实现鲁棒的全身体技能。然而，在强化学习框架内使用MPC通常需要耗时的模型构建或过高的训练开销，这使得此类框架在实际应用中难以推广。本研究提出了一种高效的训练阶段MPC引导方法，用于人形机器人运动与操作任务，称为MPC-RL。我们引入了一种基于质心动力学的MPC奖励函数，在训练阶段利用MPC轨迹的引导信息。为使其在大规模并行强化学习中具备实用性，我们开发了$π^n$MPC——一种并行化时域、免构建的批量GPU MPC求解器，可直接处理时变动力学方程，从而避免高内存占用和预编译需求。通过多项对比实验与硬件验证，我们发现MPC-RL在运动与操作技能上均展现出卓越性能。相关代码已开源至https://github.com/junhengl/mpc-rl。

---

### 9. MPCoT: Reward-Guided Multi-Path Latent Reasoning for Test-Time Scalable Vision-Language-Action

- **作者**: Boyang Zhang, Lianlei Shan
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.06245v1)
- **发表日期**: 2026-06-04
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2606.06245v1](http://arxiv.org/abs/2606.06245v1)
- **📥 PDF**: 已下载至本地 (`2606.06245v1_MPCoT_Reward-Guided_Multi-Path_Latent_Reasoning_for_Test-Time_Scalable_Vision-Language-Action.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）策略在长时域和高不确定性控制任务中仍显脆弱，其单次动作解码提供的推理时推演能力有限。显式思维链虽能增强推理深度，但会引入令牌延迟及间接的文本-动作接口。本文提出MPCoT——一种奖励引导的多路径隐式推理框架，该框架初始化M条假设路径，经过K轮权重共享的迭代优化后，在动作解码前对路径进行软聚合。训练阶段独有的路径偏好目标函数，通过专家动作一致性、基于世界模型/视觉语言模型的进展评估及成功反馈，对候选动作分支进行评价，使隐式路径评分器与下游执行质量对齐。MPCoT保持原始8步动作接口，零推理令牌生成，并提供可配置的推理控制参数（K,M）。在LIBERO和CALVIN基准的匹配协议下，MPCoT提升了长时域任务性能，消融实验验证了深度-宽度效应、置信度加权聚合及奖励引导路径监督的有效性。

---

### 10. WorldFly: A World-Model-Based Vision-Language-Action Model for UAV Navigation

- **作者**: Shengtao Zheng, Kai Li, Weichen Zhang, Yu Meng, Chen Gao, Xinlei Chen, Yong Li, Xiao-Ping Zhang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.06147v1)
- **发表日期**: 2026-06-04
- **匹配关键词**: VLA, vision-language-action model, vision-language-action, navigation
- **arXiv**: [2606.06147v1](http://arxiv.org/abs/2606.06147v1)
- **📥 PDF**: 已下载至本地 (`2606.06147v1_WorldFly_A_World-Model-Based_Vision-Language-Action_Model_for_UAV_Navigation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 端到端的视觉-语言-动作（VLA）模型在无人机导航中展现出潜力。然而，现有方法通常依赖历史观测直接预测动作，在密集城市环境中常面临挑战——严重遮挡与急转弯导致视角剧烈切换。我们认为，世界模型所固有的"想象"未来状态的能力，对于在这种部分可观测条件下做出稳健决策至关重要。为此，我们构建了具有挑战性的城市峡谷穿越基准测试，专门用于评估严重遮挡与视角剧烈切换场景下的空间理解能力。基于此，我们提出WorldFly——一种基于世界模型的新型VLA框架，采用双分支耦合流匹配机制联合生成未来视频预测与导航动作，从而通过空间想象显式引导智能体策略。在该基准上的大量评估表明，WorldFly优于其他基线方法，尤其在未知环境中表现突出，验证了将世界模型集成到具身空中智能体中的有效性。

---

### 11. Texture-preserving implicit neural representation for Cone beam CT truncated reconstruction

- **作者**: Genyuan Zhang, Junyao Wang, Haoran Lan, Chuandong Tan, Songtao Zhu, Fenglin Liu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.06039v1)
- **发表日期**: 2026-06-04
- **匹配关键词**: neural scene representation, 3d reconstruction, 3D reconstruction
- **arXiv**: [2606.06039v1](http://arxiv.org/abs/2606.06039v1)
- **📥 PDF**: 已下载至本地 (`2606.06039v1_Texture-preserving_implicit_neural_representation_for_Cone_beam_CT_truncated_reconstruction.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 锥束计算机断层扫描（CBCT）常受数据截断影响，导致严重伪影并限制有效视野（FOV）。现有用于截断CBCT重建的深度学习方法存在显著局限，包括严格依赖有监督的真实数据，以及未能考虑连续三维空间截断变化。为解决这些挑战，我们提出一种基于神经场景表征的自监督三维重建框架。通过投影监督下将空间坐标直接映射为辐射密度，该方法本质上绕过了传统滤波反投影操作，从而从根本上消除截断引起的环形伪影，同时实现稳健的连续三维数据外推。然而，坐标网络存在固有的频谱偏差，导致临床关键的高频纹理信息严重丢失。为突破这一瓶颈，我们进一步在神经场景表征架构中融入基于物理的迭代优化模块。利用坐标网络生成的无伪影外推体数据作为最优初始化，该模块逐步从原始投影中重新提取高频结构信息并注入体数据。在模拟和真实数据集上的大量实验表明，我们的方法成功统一了神经网络卓越的伪影抑制与外推能力，以及迭代算法的高保真细节保持特性。

---

### 12. Deep Learning-based 3D Oral Cavity Reconstruction Using 2D Intraoral Images

- **作者**: Jihun Cho, Soo-Yeon Jeong, Eun-Jeong Bae, Sun-Young Ihm
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.05998v1)
- **发表日期**: 2026-06-04
- **匹配关键词**: 3d reconstruction, 3D reconstruction
- **arXiv**: [2606.05998v1](http://arxiv.org/abs/2606.05998v1)
- **📥 PDF**: 已下载至本地 (`2606.05998v1_Deep_Learning-based_3D_Oral_Cavity_Reconstruction_Using_2D_Intraoral_Images.pdf`)
- **🔓 开源**: CODE
- **中文摘要**: 口腔三维建模是牙科诊疗中最关键的环节之一，目前常用的方法包括取模和口内扫描，但各有明显局限。取模需将藻酸盐或硅橡胶材料置于托盘后置入口腔形成阴模，存在患者不适感强、材料形变误差大、存储运输困难等问题。口内扫描仪通过结构光或激光技术实时直接扫描口腔结构，虽能获得先进效果，但设备成本极高。为解决上述问题，本文提出一种基于软件的方案，仅需从不同角度拍摄十张二维口内图像即可重建三维口腔模型，无需专用硬件设备。该方法可降低成本、消除物理扫描设备需求、减少患者不适感，并实现自动化三维重建。模型基于公开数据集Dental3DS（含950个上颌样本）训练，采用MobileNetV2作为图像编码器，结合多头注意力机制进行多视角特征融合。在最近邻匹配距离阈值为0.035的条件下，模型准确率达77.49%。但预测顶点倾向于集中在真实值的高密度区域，导致重建模型点云分布不均匀。

---

### 13. LiAuto-GeoX: Efficient Grounded Driving Transformer

- **作者**: Jiawei Lian, Haoyi Sun, Yang Wu, Lifu Mu, Siyuan Wang, Le Hui, Ning Mao, Tao Wei, Pan Zhou, Kun Zhan, Jian Yang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.05774v1)
- **发表日期**: 2026-06-04
- **匹配关键词**: 3d reconstruction, 3D reconstruction
- **arXiv**: [2606.05774v1](http://arxiv.org/abs/2606.05774v1)
- **📥 PDF**: 已下载至本地 (`2606.05774v1_LiAuto-GeoX_Efficient_Grounded_Driving_Transformer.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 稠密三维重建在空间理解方面展现出巨大潜力，但其作为自动驾驶实时车载表征的可行性仍是一个开放挑战。现有大规模视觉几何模型通常需要大量计算资源，且缺乏动态驾驶环境所需的远距离几何保真度、环视一致性及实时效率。为弥合这一差距，我们提出\textbf{LiAuto-GeoX}——一种专为可部署的自我中心三维场景理解设计的高效接地驾驶Transformer。该方法首先从大规模环视数据中学习高容量驾驶几何模型，利用稀疏激光雷达先验为远距离、模糊或结构稀疏区域提供稳健的几何基准。随后通过新颖的几何保持蒸馏框架，将该能力实例化为高度紧凑的1.55亿参数车载模型。该框架采用掩码引导的深度感知蒸馏，通过强调几何信息丰富区域保留细粒度度量结构；并利用相对位姿关系蒸馏，通过位姿诱导的几何关系强制跨视角空间一致性。大量评估表明，\textbf{LiAuto-GeoX}在KITTI数据集上以220 FPS运行，同时保持高保真稠密重建，实现实时部署。所学几何特征无缝迁移至下游自主任务，在轨迹预测中达到90.6 PDMS，占用预测中达到24.63 mIoU，未来帧预测中达到47.67 IoU。这些成果证明，高效稠密三维重建可超越其作为感知目标的传统角色，成为下一代自动驾驶可扩展的基础几何表征。

---

## 📌 Poster

*其他相关研究*

---

### 1. Attitude-Aided Linear Calibration of Triaxial Accelerometers

- **作者**: Yongqiang Yu, Tian Huang, Yipeng Yang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.06308v1)
- **发表日期**: 2026-06-04
- **匹配关键词**: navigation
- **arXiv**: [2606.06308v1](http://arxiv.org/abs/2606.06308v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 三轴MEMS加速度计广泛应用于惯性传感、导航与传感器融合领域，但现有标定方法常依赖昂贵的参考设备或非线性迭代优化，限制了其在低成本或自标定系统中的效率与适用性。本文提出姿态辅助线性加速度计标定方法（ALAC），该方法可在任何提供姿态信息的平台（如转台、机械臂或惯性测量单元）上运行。ALAC通过构建组合误差矩阵（CEM）统一标定模型中的传感器误差，实现线性最小二乘估计。该方法联合估计零偏与重力矢量，隐式补偿平台对准误差，并通过CEM矩阵分解恢复尺度因子、非正交性及对准旋转参数。在静态重力条件下，标定问题被转化为约束齐次最小二乘（CHLS）问题，并利用标准线性代数获得闭式解。该方法仅需五次任意方向的测量，其递归扩展形式支持在线或现场标定。在固定于机械臂的加速度计与准静态公开IMU轨迹上的实验表明：无论离线还是在线模式，ALAC在精度与传感器噪声鲁棒性方面均优于基于参考的标定方法与在线基线方法。在相同数据集上，ALAC在滤波条件下与迭代自标定性能相当，而在原始测量数据上超越所有评估基线。这些结果验证了该方案对基于MEMS的惯性平台（特别是低成本IMU与在线标定场景）的鲁棒性与实用性。

---

### 2. Multi-Resolution Tactile Imitation Learning for Contact-Rich Robotic Manipulation

- **作者**: Rickmer Krohn, Erik Helmut, Niklas Funk, Jan Peters, Vignesh Prasad, Georgia Chalvatzaki
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.06281v1)
- **发表日期**: 2026-06-04
- **匹配关键词**: contact-rich manipulation
- **arXiv**: [2606.06281v1](http://arxiv.org/abs/2606.06281v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: PROJECT_PAGE
  - 链接：http://mitas-touch.github.io.
- **中文摘要**: 触觉感知对于解决多种操作任务具有重要价值。尽管现有多种不同特性的触觉传感器，但利用多类异构触觉传感器的融合来提升操作学习能力仍是一个未被充分探索的领域。我们提出多分辨率触觉感知框架（MiTaS），该表征框架通过整合不同时间分辨率的多类触觉传感器，解决复杂的接触密集型操作任务。我们创新性地设计了基于模态特定卷积主干网络与Transformer融合的架构，有效整合了RGB摄像头流、基于视觉的GelSight Mini传感器以及高频事件型Evetac传感器的信息。这种多传感器表征随后用于调控流匹配策略，以完成下游任务。在五项接触密集型操作任务上的实验结果表明，多分辨率触觉特征在模仿学习中具有显著效果。MiTaS实现了80%的平均成功率，而纯视觉基线（31%）和视觉-触觉基线（54%）均无法可靠完成任务。在策略评估阶段无需使用Evetac传感器的情况下，通过多触觉数据联合训练视觉-触觉模型可使特定任务性能提升超过10%。详细的传感器读数与注意力分析揭示了不同传感器在任务执行过程中的重要性，验证了我们的多分辨率触觉感知方法。项目页面：http://mitas-touch.github.io

---

### 3. RadiusFPS: Efficient Farthest Point Sampling on CPUs and GPUs via Spherical Voxel Pruning

- **作者**: Ziyang Yu, Xiang Li, Qiong Chang, Jun Miyazaki
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.06255v1)
- **发表日期**: 2026-06-04
- **匹配关键词**: localization and mapping, navigation
- **arXiv**: [2606.06255v1](http://arxiv.org/abs/2606.06255v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 点云是机器人感知的主要感官表示形式，支撑着基于激光雷达的自动驾驶、同步定位与地图构建（SLAM）及导航系统。在这些流程中，最远点采样（FPS）是最著名的下采样算子，其均匀覆盖特性能够保留下游感知任务所依赖的几何结构。然而，经典FPS算法的时间复杂度较高，难以适应现代3D传感器每秒百万级点云的处理需求，成为与机器人系统实时性和有限机载计算预算相冲突的主要延迟瓶颈。为此，我们提出RadiusFPS——一种基于球形体素剪枝的FPS加速框架，在相同初始化和断点策略下保持标准FPS更新规则。通过使用球形体素索引点云，RadiusFPS推导出保守几何边界以剪枝每次迭代中的冗余距离计算，并辅以逐坐标点跳过测试消除残余更新。我们进一步提出RadiusFPS-G，一种基于线程束级别的GPU实现，将体素选择、剪枝和距离更新融合为内存合并内核，消除昂贵的全局内存往返。在室内（S3DIS、ScanNet）和室外LiDAR（SemanticKITTI）基准测试中，RadiusFPS-G相比基于GPU的FPS实现最高提速2.5倍，在评估方法中与QuickFPS性能相当或更优，同时仅使用其约一半的GPU内存，且分割精度相当。当与基于学习的FastPoint采样器结合时，所得流程在所有评估配置中实现了最快的端到端推理速度。这些特性使得高质量FPS风格采样在延迟和内存受限的机器人视觉中变得切实可行。

---

### 4. ActiveMimic: Egocentric Video Pretraining with Active Perception

- **作者**: Xingyao Lin, Guojin Zhong, Tianyi Lu, Ziyi Ye, Yichen Zhu, Zuxuan Wu, Yu-Gang Jiang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.06194v1)
- **发表日期**: 2026-06-04
- **匹配关键词**: active perception, perception and manipulation
- **arXiv**: [2606.06194v1](http://arxiv.org/abs/2606.06194v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 以自我为中心的人类视频为机器人预训练提供了一种可扩展的替代数据源，但基于此类视频预训练的模型始终逊色于基于机器人数据预训练的模型。我们将这一差距归因于缺失的关键信号——自我中心视频中的主动感知行为：人类在操作过程中会持续调整视角，由此产生的相机运动被标准流程视为噪声。为解决这一问题，我们提出ActiveMimic预训练框架，该框架能从单台穿戴式RGB相机中恢复同步的相机与手腕轨迹，将相机运动建模为视角动作，并在适应目标机器人之前，从真实世界自我中心人类视频中联合学习主动感知与操作技能。实验表明，在具有不同主动感知需求的多项真实世界任务中，ActiveMimic始终超越基于人类视频预训练的基线模型，并达到与基于机器人数据预训练的最先进模型相当的性能。进一步分析证实，主动感知能力源自自我中心人类视频预训练而非机器人特定微调，从而验证了主动感知是解锁自我中心人类视频用于机器人预训练的关键。

---

### 5. Towards Realistic 3D Sonar Simulation

- **作者**: Youssef Attia, Davide Costa, Francesco Wanderlingh, Filippo Campagnaro, Enrico Simetti
- **单位**: University of Genova, Italy; University of Padova, Italy; University of Genova, Italy...
- **发表日期**: 2026-06-04
- **匹配关键词**: autonomous navigation, navigation
- **arXiv**: [2606.06130v1](http://arxiv.org/abs/2606.06130v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 随着水下机器人研究日益聚焦于复杂三维感知与自主导航，声纳仿真的保真度已成为算法开发的关键因素。当前仿真框架通常依赖几何驱动渲染，将三维声纳近似为水下等效激光雷达，未能考虑折射、多径干扰及相位相关信号形成等基础声学现象。本文提出一种模块化架构，通过集成GPU加速图形引擎与基于物理的声传播原理，实现高保真三维声纳仿真。我们在NVIDIA Isaac Sim环境中构建了基于Water Linked 3D-15传感器的体素三维声纳模型，并将其整合至综合水下仿真框架。通过硬件在环配置验证系统性能：在NVIDIA Jetson Orin Nano上运行的改进型FastLIO2 SLAM流水线，利用合成三维声纳、DVL、IMU及压力数据进行传感器融合。最后，通过模拟输出与港口板桩检测真实数据的定性对比，刻画了仿真与现实的剩余差距，并确立了迈向全声学驱动体素感知的技术路线图。

---

### 6. 3D Underwater Path Planning via Generative Flow Field Surrogates

- **作者**: Zachary Cooper-Baldock, Paulo E. Santos, Russell S. A. Brinkworth, Karl Sammut
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.06077v1)
- **发表日期**: 2026-06-04
- **匹配关键词**: path planning
- **arXiv**: [2606.06077v1](http://arxiv.org/abs/2606.06077v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 自主水下航行器（AUV）在行进母船船体内的布放与回收（LAR）需穿越复杂的三维螺旋桨尾流，其水动力结构无法用均匀流模型表征。高保真雷诺平均纳维-斯托克斯（RANS）计算流体动力学（CFD）仿真能以足够精度解析该结构用于路径规划，但计算成本过高难以实现机载应用。我们通过集成两种条件生成对抗网络（cGAN）架构——正则化PatchGAN与带自注意力机制的2D3DGAN——作为RANS CFD数据的即插即用替代方案，应用于三维能量加权A*路径规划框架。两种生成器均由层级化流水线驱动，仅通过标量工况输入即可合成完整的$128^3$体素流场体数据，端到端推理时间约28-146微秒，而单次RANS计算需数小时。我们针对四种环境知识水平（均匀流、真实CFD、PatchGAN、2D3DGAN~SA）进行基准测试，在涵盖550种不同流态的19,800条独立生成轨迹上展开评估。相较于均匀流规划，完整CFD尾流知识可降低5.7-12.5%的能量消耗，减少高达77.8%的高速尾流核心区域穿越，且两种效益随工况严酷度递增。cGAN替代模型在边缘设备兼容的推理速度下，可恢复约45-60%的CFD能量效益与高速单元规避效益。这些结果首次系统量化了三维海洋机器人应用中cGAN预测水动力场对下游路径规划的价值。

---

### 7. Sample-efficient Low-level Motion Planning for Robotic Manipulation Tasks via Zero-shot Transfer Learning

- **作者**: Yuanzhi He, Victor Romero-Cano, José J. Patiño, Juan David Hernández, William Sawtell, Gualtiero Colombo
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.06041v1)
- **发表日期**: 2026-06-04
- **匹配关键词**: motion planning
- **arXiv**: [2606.06041v1](http://arxiv.org/abs/2606.06041v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 随着机器人系统日益复杂，其运动规划模型的复杂度不断提升，训练时间也显著延长，这带来了巨大挑战。近年来，样本高效交叉熵方法（iCEM）等进化算法通过高效的知识复用策略提升性能，在低层级实时规划中展现出良好潜力。尽管iCEM在诸多控制任务中表现有效，但在更复杂的场景（特别是涉及堆叠、滑动和货架放置的任务）中，其性能可能受到限制。本研究提出了一种创新的iCEM+TL框架，明确利用迁移学习（TL）技术，将关键iCEM参数从简单上游任务迁移至复杂下游任务以提供指导。此外，我们通过任务分解对堆叠物体和货架放置任务应用奖励重塑（RR）策略，以优化特定任务性能。仿真结果表明，该框架的成功率提升最高可达23%。该框架进一步在真实Franka Emika机器人堆叠任务中得到验证，证明了其在实际部署中的可行性。

---

