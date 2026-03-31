# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-03-31 10:08

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 3/20 篇提供

**🏅 Oral**: 5 篇 | **🌟 Highlight**: 15 篇 | **📌 Poster**: 0 篇

---

## 🏅 Oral (Top recommendations)

*基于用户近期关注方向（world model/action generation；lifelong spatial memory/SLAM2.0；interaction/articulated/tactile）*

---

### 1. DiffusionAnything: End-to-End In-context Diffusion Learning for Unified Navigation and Pre-Grasp Motion

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2603.26322)
- **发表日期**: 
- **匹配关键词**: diffusion policy, VLA, vision-language-action, navigation
- **arXiv**: [2603.26322](https://arxiv.org/abs/2603.26322)
- **📥 PDF**: 已下载至本地 (`2603.26322_DiffusionAnything_End-to-End_In-context_Diffusion_Learning_for_Unified_Navigation_and_Pre-Grasp_Moti.pdf`) | recent-focus score=11.50
- **🔒 开源**: 未提及
- **中文摘要**: arXiv:2603.26322v1 公告类型：新  
摘要：直接从视觉输入高效预测运动规划仍是机器人学的基本挑战，传统规划方法通常需要明确的目标设定和任务特定设计。近期视觉-语言-动作模型虽能直接从视觉推断动作，但需要大量计算资源、海量训练数据，且在新场景中零样本泛化能力不足。我们提出一种统一的图像空间扩散策略，通过多尺度特征调制同时处理米级导航与厘米级操作任务，每项任务仅需5分钟自监督数据。该框架由三项关键创新驱动：(1) 基于任务模式、深度尺度和空间注意力的多尺度FiLM调节机制，使单一模型具备任务适应性行为；(2) 轨迹对齐的深度预测沿生成路径点聚焦度量三维推理；(3) 源自AnyTraverse的自监督注意力机制，无需视觉语言模型和深度传感器即可实现目标导向推断。该模型仅需RGB输入（内存占用2.0 GB，运行频率10 Hz），在保持机载部署适用性的同时，实现了对新场景的鲁棒零样本泛化。

---

### 2. DFM-VLA: Iterative Action Refinement for Robot Manipulation via Discrete Flow Matching

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2603.26320)
- **发表日期**: 
- **匹配关键词**: HRI, VLA
- **arXiv**: [2603.26320](https://arxiv.org/abs/2603.26320)
- **📥 PDF**: 已下载至本地 (`2603.26320_DFM-VLA_Iterative_Action_Refinement_for_Robot_Manipulation_via_Discrete_Flow_Matching.pdf`) | recent-focus score=7.50
- **🔒 开源**: 未提及
- **中文摘要**: arXiv:2603.26320v1 公告类型：新  
摘要：采用离散标记化方案编码动作的视觉-语言-动作（VLA）模型在机器人操作中日益普及，但现有的解码范式仍存在根本性局限。无论是通过自回归VLA顺序解码动作，还是通过离散扩散VLA并行解码，一旦生成标记，通常会被固定且无法在后续迭代中修正，导致早期标记错误难以有效纠正。我们提出DFM-VLA，一种基于离散流匹配的VLA模型，用于动作标记的迭代优化。DFM-VLA通过建模标记级概率速度场，在优化迭代中动态更新完整动作序列。我们研究了两种构建速度场的方法：辅助速度头形式和动作嵌入引导形式。该框架进一步采用两阶段解码策略，包含迭代优化阶段和确定性验证阶段以确保稳定收敛。在CALVIN、LIBERO和真实世界操作任务上的大量实验表明，DFM-VLA在保持高推理效率的同时，其操作性能始终优于强自回归、离散扩散和连续扩散基线模型。特别地，DFM-VLA在CALVIN上实现了4.44的平均连续成功长度，在LIBERO上达到95.7%的平均成功率，凸显了通过离散流匹配进行动作优化对机器人操作的价值。项目地址：\url{https://chris1220313648.github.io/DFM-VLA/}

---

### 3. VLA-OPD: Bridging Offline SFT and Online RL for Vision-Language-Action Models via On-Policy Distillation

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2603.26666)
- **发表日期**: 
- **匹配关键词**: VLA, vision-language-action model, vision-language-action
- **arXiv**: [2603.26666](https://arxiv.org/abs/2603.26666)
- **📥 PDF**: 已下载至本地 (`2603.26666_VLA-OPD_Bridging_Offline_SFT_and_Online_RL_for_Vision-Language-Action_Models_via_On-Policy_Distillat.pdf`) | recent-focus score=7.50
- **🔒 开源**: 未提及
- **中文摘要**: arXiv:2603.26666v1 公告类型：新  
摘要：尽管预训练的视觉-语言-动作（VLA）模型在机器人操作中展现出令人印象深刻的泛化能力，但部署后的训练对于确保可靠性能仍然至关重要。然而，标准的离线监督微调（SFT）存在分布偏移和预训练能力灾难性遗忘的问题，而在线强化学习（RL）则面临稀疏奖励和样本效率低下的挑战。本文提出了一种名为“在线策略VLA蒸馏”（VLA-OPD）的框架，该框架结合了SFT的高效性和RL的鲁棒性。VLA-OPD不依赖稀疏的环境奖励，而是利用专家教师对模型自身生成的轨迹提供密集的令牌级监督。这种方法能够在策略诱导的状态下实现主动错误纠正，同时通过温和的对齐方式保留预训练的通用能力。关键的是，我们通过反向KL目标来构建VLA-OPD。与导致模式覆盖熵爆炸的标准正向KL或导致过早熵崩溃的硬交叉熵不同，我们的有界模式寻求目标通过过滤掉教师的认识不确定性，同时保持动作多样性，确保了策略学习的稳定性。在LIBERO和RoboTwin2.0基准测试中的实验表明，VLA-OPD在样本效率上显著优于RL，在鲁棒性上显著优于SFT，同时有效缓解了训练后的灾难性遗忘问题。

---

### 4. Policy-Guided World Model Planning for Language-Conditioned Visual Navigation

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2603.25981)
- **发表日期**: 
- **匹配关键词**: visual navigation, learned navigation, navigation
- **arXiv**: [2603.25981](https://arxiv.org/abs/2603.25981)
- **📥 PDF**: 已下载至本地 (`2603.25981_Policy-Guided_World_Model_Planning_for_Language-Conditioned_Visual_Navigation.pdf`) | recent-focus score=6.50
- **🔒 开源**: 未提及
- **中文摘要**: arXiv:2603.25981v1 公告类型：新  
摘要：在具身人工智能领域，根据自然语言指令导航至视觉指定目标仍是一个根本性挑战。现有方法要么依赖难以进行长程规划的响应式策略，要么采用在高维空间中动作初始化效果不佳的世界模型。我们提出了PiJEPA框架，该框架结合了学习型导航策略与潜在世界模型规划的优势，用于指令条件视觉导航任务。第一阶段，我们在CAST导航数据集上对基于Octo的通用策略进行微调，并整合冻结的预训练视觉编码器（DINOv2或V-JEPA-2），生成基于当前观测和语言指令的智能动作分布。第二阶段，我们利用该策略导出的分布对独立训练的JEPA世界模型进行模型预测路径积分（MPPI）规划的热启动，该世界模型可在同一冻结编码器的嵌入空间中预测未来潜在状态。通过从策略先验而非无信息的高斯分布初始化MPPI采样分布，我们的规划器能更快收敛到高质量的动作序列以实现目标。我们系统研究了视觉编码器主干网络（对比DINOv2与V-JEPA-2）对策略和世界模型组件的影响。真实世界导航任务的实验表明，PiJEPA在目标到达准确率和指令遵循保真度方面均显著优于独立策略执行和无信息世界模型规划方法。

---

### 5. ETA-VLA: Efficient Token Adaptation via Temporal Fusion and Intra-LLM Sparsification for Vision-Language-Action Models

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2603.25766)
- **发表日期**: 
- **匹配关键词**: VLA, vision-language-action model, vision-language-action
- **arXiv**: [2603.25766](https://arxiv.org/abs/2603.25766)
- **📥 PDF**: 已下载至本地 (`2603.25766_ETA-VLA_Efficient_Token_Adaptation_via_Temporal_Fusion_and_Intra-LLM_Sparsification_for_Vision-Langu.pdf`) | recent-focus score=6.50
- **🔒 开源**: 未提及
- **中文摘要**: arXiv:2603.25766v1 公告类型：新  
摘要：将视觉-语言-动作（VLA）模型集成到自动驾驶系统中，为解析复杂场景和执行控制指令提供了统一框架。然而，为进行精确的时间推理而必须整合历史多视角帧，带来了沉重的计算负担，这主要源于大型语言模型（LLM）中自注意力机制的二次复杂度。为缓解这一瓶颈，我们提出ETA-VLA——一种面向VLA模型的高效令牌自适应框架。ETA-VLA通过处理过去$n$帧多视角图像，并引入一种新颖的LLM内部稀疏聚合器（ILSA）。受人类驾驶员注意力分配机制的启发，ILSA在文本查询和时间一致性的引导下，动态识别并剪枝冗余的视觉令牌。具体而言，我们采用文本引导的评分机制与保持多样性的稀疏化策略，选取关键令牌的稀疏子集，从而确保对驾驶场景的全面感知。在NAVSIM v2数据集上的大量实验表明，ETA-VLA在实现与最先进基线相当的驾驶性能的同时，将计算FLOPs降低了约32%。值得注意的是，我们的方法剪枝了85%的视觉令牌，推理FLOPs减少了61%，但在NAVSIM v2基准测试中仍保持了94%的原始准确率。

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. Chasing Autonomy: Dynamic Retargeting and Control Guided RL for Performant and Controllable Humanoid Running

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2603.25902)
- **发表日期**: 
- **匹配关键词**: obstacle avoidance
- **arXiv**: [2603.25902](https://arxiv.org/abs/2603.25902)
- **📥 PDF**: 已下载至本地 (`2603.25902_Chasing_Autonomy_Dynamic_Retargeting_and_Control_Guided_RL_for_Performant_and_Controllable_Humanoid_.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: arXiv:2603.25902v1 公告类型：新  
摘要：人形机器人有望实现类人运动，包括快速动态奔跑。近年来，能够模仿人类动作的强化学习控制器因其能生成高度动态行为而备受关注，但这些控制器通常局限于单一动作回放，限制了其在长时间自主运动中的应用。本文提出一种通过带硬约束的优化流程动态重定向人类动作的方法，从单次人类演示中生成改进的周期性参考动作库。我们系统研究了参考动作与奖励结构对参考速度和指令速度跟踪的影响，发现以目标为条件、控制为导向的奖励机制结合动态优化的人类数据跟踪能实现最佳性能。该策略已在硬件上部署，通过在宇树G1机器人上实现最高3.3米/秒的奔跑速度，并在真实环境中穿越数百米距离，验证了其速度与耐久性。此外，为展示运动控制能力，我们将该控制器集成于完整感知与规划自主系统，实现了户外奔跑过程中的动态避障。

---

### 2. Partial Motion Imitation for Learning Cart Pushing with Legged Manipulators

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2603.26659)
- **发表日期**: 
- **匹配关键词**: mobile manipulation
- **arXiv**: [2603.26659](https://arxiv.org/abs/2603.26659)
- **📥 PDF**: 已下载至本地 (`2603.26659_Partial_Motion_Imitation_for_Learning_Cart_Pushing_with_Legged_Manipulators.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: arXiv:2603.26659v1 公告类型：新  
摘要：移动操作是足式机器人在现实环境中执行实际移动操作任务（如搬运和推动物体）的关键能力。然而，由于在保持稳定运动的同时执行精确操作行为的难度，学习稳健的移动操作技能仍然具有挑战性。本研究提出了一种部分模仿学习方法，将运动任务中学到的运动风格迁移到推车移动操作中。首先通过广泛的领域和地形随机化训练一个稳健的运动策略，然后通过部分对抗运动先验仅模仿下半身动作来学习移动操作策略。我们通过实验证明，学习到的策略在IsaacLab中成功沿不同轨迹推动推车，并能有效迁移到MuJoCo环境中。我们还与多种基线方法进行比较，结果表明所提出的方法实现了更稳定、更精确的移动操作行为。

---

### 3. Can a Robot Walk the Robotic Dog: Triple-Zero Collaborative Navigation for Heterogeneous Multi-Agent Systems

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2603.21723)
- **发表日期**: 
- **匹配关键词**: path planning, navigation
- **arXiv**: [2603.21723](https://arxiv.org/abs/2603.21723)
- **📥 PDF**: 已下载至本地 (`2603.21723_Can_a_Robot_Walk_the_Robotic_Dog_Triple-Zero_Collaborative_Navigation_for_Heterogeneous_Multi-Agent_.pdf`)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/triple-zeropp/Triple-zero-robot-agent
- **中文摘要**: arXiv:2603.21723v2 公告类型：替换  
摘要：本文提出三重零路径规划（TZPP），一种无需训练、无需先验知识且无需仿真的异构多机器人协同框架。TZPP采用协调者-探索者架构：人形机器人负责任务协调，四足机器人则借助多模态大语言模型的引导进行环境探索与可行路径识别。我们在宇树G1与Go2机器人平台上实现了TZPP，并在包括障碍密集和地标稀疏场景在内的多样化室内外环境中进行评估。实验表明，TZPP展现出鲁棒性、类人效率以及对未知场景的强适应能力。通过消除对训练和仿真的依赖，TZPP为异构机器人协作的实际部署提供了可行路径。代码与演示视频发布于：https://github.com/triple-zeropp/Triple-zero-robot-agent

---

### 4. Can Vision Foundation Models Navigate? Zero-Shot Real-World Evaluation and Lessons Learned

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2603.25937)
- **发表日期**: 
- **匹配关键词**: visual navigation, robot navigation, navigation
- **arXiv**: [2603.25937](https://arxiv.org/abs/2603.25937)
- **📥 PDF**: 已下载至本地 (`2603.25937_Can_Vision_Foundation_Models_Navigate?_Zero-Shot_Real-World_Evaluation_and_Lessons_Learned.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: arXiv:2603.25937v1 公告类型：新  
摘要：视觉导航模型（VNMs）通过大规模视觉演示学习，有望实现通用化的机器人导航。尽管在现实世界中的应用日益增多，现有评估几乎完全依赖于成功率（即机器人是否到达目标），这掩盖了轨迹质量、碰撞行为以及对环境变化的鲁棒性。我们对五种最先进的VNM（GNM、ViNT、NoMaD、NaviBridger和CrossFormer）进行了现实世界评估，涵盖两个机器人平台和五个室内外环境。除了成功率外，我们结合基于路径的指标和基于视觉的目标识别分数，并通过受控图像扰动（运动模糊、太阳耀斑）评估鲁棒性。我们的分析揭示了三个系统性局限：（a）即使是架构复杂的基于扩散和Transformer的模型也频繁发生碰撞，表明其几何理解能力有限；（b）模型无法区分感知相似但存在语义差异的不同位置，导致在重复环境中出现目标预测错误；（c）在分布偏移下性能下降。我们将公开发布评估代码库和数据集，以促进VNM的可复现基准测试。

---

### 5. 120 Minutes and a Laptop: Minimalist Image-goal Navigation via Unsupervised Exploration and Offline RL

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2603.26441)
- **发表日期**: 
- **匹配关键词**: exploration, visual navigation, image-goal navigation, navigation
- **arXiv**: [2603.26441](https://arxiv.org/abs/2603.26441)
- **📥 PDF**: 已下载至本地 (`2603.26441_120_Minutes_and_a_Laptop_Minimalist_Image-goal_Navigation_via_Unsupervised_Exploration_and_Offline_R.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: arXiv:2603.26441v1 公告类型：新  
摘要：当前图像目标视觉导航的主流范式通常依赖于大规模数据集、大量预训练和显著的计算资源。本研究对这一假设提出挑战。我们证明，可以在（1）少于120分钟、（2）仅使用消费级笔记本电脑、（3）无需任何人工干预的条件下，完成数据收集、训练领域内策略并部署至现实世界。我们提出的MINav方法将图像目标导航构建为离线目标条件强化学习问题，结合无监督数据收集、后见目标重标记与离线策略学习。仿真与现实环境中的实验表明，MINav提升了探索效率，在目标环境中优于零样本导航基线，且能随数据集规模扩大而有效扩展。这些结果表明，通过高效计算可实现有效的现实世界机器人学习，从而降低了快速策略原型设计与部署的门槛。

---

### 6. Drive-Through 3D Vehicle Exterior Reconstruction via Dynamic-Scene SfM and Distortion-Aware Gaussian Splatting

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2603.26638)
- **发表日期**: 
- **匹配关键词**: 3D reconstruction, 3D gaussian splatting, 3d reconstruction, gaussian splatting
- **arXiv**: [2603.26638](https://arxiv.org/abs/2603.26638)
- **📥 PDF**: 已下载至本地 (`2603.26638_Drive-Through_3D_Vehicle_Exterior_Reconstruction_via_Dynamic-Scene_SfM_and_Distortion-Aware_Gaussian.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: arXiv:2603.26638v1 公告类型：交叉  
摘要：车辆外观的高保真三维重建能提升在线汽车交易市场中买家的信心，但在杂乱经销商通道中生成此类模型面临严峻技术挑战。与静态场景摄影测量不同，该场景的特点是动态车辆在高度杂乱的静态背景中移动。广角镜头畸变、镜面汽车漆面以及破坏经典对极约束的非刚性车轮旋转进一步加剧了这一问题。我们提出了一种采用双柱相机架的端到端流程。首先，通过将SAM 3实例分割与运动门控相结合，清晰分离运动车辆，并显式掩蔽非刚性车轮以强制执行严格的对极几何，从而解决动态场景的模糊性问题。其次，在语义置信掩模引导下，使用RoMa v2学习匹配器直接在原始畸变的4K图像上提取鲁棒对应点。第三，将这些匹配点集成到基于相机架感知的运动恢复结构（SfM）优化中，利用CAD导出的相对位姿先验消除尺度漂移。最后，我们采用畸变感知的三维高斯泼溅框架（3DGUT）结合随机马尔可夫链蒙特卡洛（MCMC）致密化策略来渲染反射表面。在10家经销商处对25辆真实车辆的评估表明，我们的完整流程在保留视图上实现了28.66 dB的峰值信噪比（PSNR）、0.89的结构相似性指数（SSIM）和0.21的感知图像块相似度（LPIPS），相比标准三维高斯泼溅（3D-GS）提升了3.85 dB，无需受控摄影棚设施即可生成检测级交互式三维模型。

---

### 7. Wanderland: Geometrically Grounded Simulation for Open-World Embodied AI

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2511.20620)
- **发表日期**: 
- **匹配关键词**: 3d reconstruction, visual navigation, 3D reconstruction, navigation
- **arXiv**: [2511.20620](https://arxiv.org/abs/2511.20620)
- **📥 PDF**: 已下载至本地 (`2511.20620_Wanderland_Geometrically_Grounded_Simulation_for_Open-World_Embodied_AI.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://ai4ce.github.io/wanderland/.
- **中文摘要**: arXiv:2511.20620v2 公告类型：替换交叉  
摘要：在具身人工智能（如视觉导航）领域，可复现的闭环评估仍是主要瓶颈。一个前景广阔的解决路径是开发高保真仿真系统，将逼真的传感器渲染与复杂开放世界城市环境中基于几何的交互相结合。尽管近期视频-3DGS方法简化了开放世界场景采集，但由于视觉与几何层面存在显著的仿真与现实差距，它们仍不适用于基准测试。为应对这些挑战，我们推出Wanderland——一个具备多传感器采集、可靠重建、精确几何与鲁棒视图合成能力的实景转仿真框架。通过该流程，我们构建了涵盖室内外城市场景的多样化数据集，系统论证了纯图像流程的可扩展性局限、几何质量对新颖视图合成的影响，以及这些因素如何共同制约导航策略学习与评估可靠性。除作为具身导航的可信测试平台外，Wanderland丰富的原始传感器数据还可用于三维重建与新颖视图合成模型的基准测试。本研究为开放世界具身人工智能的可复现研究奠定了新基础。项目网站：https://ai4ce.github.io/wanderland/

---

### 8. Few TensoRF: Enhance the Few-shot on Tensorial Radiance Fields

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2603.25008)
- **发表日期**: 
- **匹配关键词**: nerf, 3D reconstruction, 3d reconstruction
- **arXiv**: [2603.25008](https://arxiv.org/abs/2603.25008)
- **📥 PDF**: 已下载至本地 (`2603.25008_Few_TensoRF_Enhance_the_Few-shot_on_Tensorial_Radiance_Fields.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 本文提出Few TensoRF，这是一种将TensorRF基于张量的高效表示与FreeNeRF基于频率驱动的少样本正则化相结合的三维重建框架。该方法通过使用TensorRF显著加速渲染速度，并引入频率掩码与遮挡掩码，提升了稀疏输入视角下的稳定性与重建质量。在Synthesis NeRF基准测试上的实验表明，Few TensoRF方法将平均PSNR从21.45 dB（TensorRF）提升至23.70 dB，经微调的版本可达24.52 dB，同时保持了TensorRF约10-15分钟的快速训练时间。在THuman 2.0数据集上的实验进一步验证了其在人体重建任务中的竞争力，仅使用八张输入图像即可达到27.37-34.00 dB的PSNR。这些结果凸显了Few TensoRF作为一种高效且数据利用率高的解决方案，适用于多种场景的实时三维重建。

---

### 9. Geo$^\textbf{2}$: Geometry-Guided Cross-view Geo-Localization and Image Synthesis

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2603.25819)
- **发表日期**: 
- **匹配关键词**: 3D reconstruction, 3d reconstruction
- **arXiv**: [2603.25819](https://arxiv.org/abs/2603.25819)
- **📥 PDF**: 已下载至本地 (`2603.25819_Geo$^textbf{2}$_Geometry-Guided_Cross-view_Geo-Localization_and_Image_Synthesis.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: arXiv:2603.25819v1 公告类型：新  
摘要：跨视角地理空间学习包含两个重要任务：跨视角地理定位（CVGL）与跨视角图像合成（CVIS），二者均依赖于建立地面与航拍视角间的几何对应关系。近期提出的几何基础模型（GFMs）已展现出从图像中提取可泛化三维几何特征的强大能力，但其在跨视角地理空间任务中的应用潜力尚未得到充分探索。本研究提出Geo^2框架，该框架利用GFMs（如VGGT）的几何先验知识，构建统一模型以协同完成CVGL与双向CVIS任务。尽管GFMs具备三维重建能力，但由于地面与航拍图像间存在显著视角差异，直接将其应用于CVGL和CVIS仍面临挑战。为此，我们提出GeoMap方法，将地面与航拍特征嵌入共享的三维感知潜在空间，有效降低跨视角差异对定位任务的影响。该共享潜在空间自然构建了双向跨视角图像合成的桥梁。为充分利用这一特性，我们进一步提出GeoFlow——基于几何感知潜在嵌入的条件流匹配模型，并引入一致性损失函数以强化两个合成方向间的潜在对齐，确保双向合成的一致性。在CVUSA、CVACT和VIGOR等标准基准数据集上的大量实验表明，Geo^2在定位与合成任务中均达到最先进的性能水平，凸显了三维几何先验知识对跨视角地理空间学习的有效性。

---

### 10. FAST3DIS: Feed-forward Anchored Scene Transformer for 3D Instance Segmentation

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2603.25993)
- **发表日期**: 
- **匹配关键词**: 3D reconstruction, 3d reconstruction
- **arXiv**: [2603.25993](https://arxiv.org/abs/2603.25993)
- **📥 PDF**: 已下载至本地 (`2603.25993_FAST3DIS_Feed-forward_Anchored_Scene_Transformer_for_3D_Instance_Segmentation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: arXiv:2603.25993v1 公告类型：新  
摘要：尽管近期的前馈式三维重建模型为场景理解提供了坚实的几何基础，但将其扩展至三维实例分割通常依赖于分离式的“提升-聚类”范式。通过不可微聚类对密集像素级嵌入进行分组的方法，其扩展性随视图数量增加而急剧下降，且使表征学习与最终分割目标脱节。本文提出一种用于三维实例分割的前馈锚定场景变换器（FAST3DIS），这是一种端到端方法，有效绕过了后处理聚类。我们引入了一种基于三维锚定、查询驱动的变换器架构，该架构构建于基础深度骨干网络之上，经过高效适配以学习实例特定的语义，同时保留其零样本几何先验。我们设计了一种可学习的三维锚点生成器，并结合锚点采样交叉注意力机制，以实现视图一致的三维实例分割。通过将三维物体查询直接投影到多视图特征图中，我们的方法能够高效采样上下文信息。此外，我们提出了一种双重正则化策略，将多视图对比学习与动态调度的空间重叠惩罚相结合，以显式防止查询冲突并确保精确的实例边界。在复杂室内三维数据集上的实验表明，相较于当前最先进的基于聚类的方法，我们的方法在实现竞争性分割精度的同时，显著提升了内存可扩展性和推理速度。

---

### 11. Conditional Diffusion for 3D CT Volume Reconstruction from 2D X-rays

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2603.26509)
- **发表日期**: 
- **匹配关键词**: 3D reconstruction, 3d reconstruction
- **arXiv**: [2603.26509](https://arxiv.org/abs/2603.26509)
- **📥 PDF**: 已下载至本地 (`2603.26509_Conditional_Diffusion_for_3D_CT_Volume_Reconstruction_from_2D_X-rays.pdf`)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/ai-med/AXON.
- **中文摘要**: arXiv:2603.26509v1 公告类型：新  
摘要：计算机断层扫描（CT）能提供丰富的三维解剖细节，但常受限于高辐射暴露、高昂成本及有限的可及性。虽然标准胸部X光检查具有成本效益且普及度高，但其仅能提供二维投影，病理信息有限。从二维X光重建三维CT体数据为提升诊断可及性提供了变革性解决方案，然而现有方法主要依赖合成X射线投影，限制了临床泛化能力。本研究提出AXON——一种基于多阶段扩散的框架，可直接从真实X光重建高保真三维CT体数据。AXON采用由粗到精的策略：第一阶段基于布朗桥扩散模型实现全局结构合成，第二阶段通过ControlNet进行局部强度优化。该框架还支持双平面X光输入，以缓解二维到三维重建固有的深度模糊问题。通过集成超分辨率网络，可将生成体数据升级至诊断级分辨率。在公开及外部数据集上的评估表明，AXON显著优于现有先进基线模型，PSNR提升11.9%，SSIM提高11.0%，且在不同临床数据分布中展现出稳健的泛化能力。代码已开源：https://github.com/ai-med/AXON。

---

### 12. Scene Grounding In the Wild

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2603.26584)
- **发表日期**: 
- **匹配关键词**: 3D reconstruction, 3D gaussian splatting, 3d reconstruction, gaussian splatting
- **arXiv**: [2603.26584](https://arxiv.org/abs/2603.26584)
- **📥 PDF**: 已下载至本地 (`2603.26584_Scene_Grounding_In_the_Wild.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: arXiv:2603.26584v1 公告类型：新  
摘要：从非结构化、真实场景图像中重建大规模现实世界场景的精确三维模型，仍然是计算机视觉领域的核心挑战，尤其是在输入视图之间几乎没有重叠的情况下。现有重建流程在这种情况下往往会产生多个互不连接的部分重建结果，或将非重叠区域错误地合并为重叠几何体。本文提出一种框架，将每个部分重建结果锚定到场景的完整参考模型中，从而即使在缺乏视觉重叠的情况下也能实现全局一致的对齐。我们通过从谷歌地球工作室生成的密集、地理空间精确的伪合成渲染中获取参考模型。这些渲染提供了完整的场景覆盖，但其外观与现实世界照片存在显著差异。我们的核心洞见是，尽管存在显著的领域差异，但两个领域共享相同的底层场景语义。我们使用三维高斯泼溅表示参考模型，为每个高斯分布添加语义特征，并将对齐问题表述为基于特征的逆向优化方案，在保持参考模型固定的同时估计全局六自由度姿态和尺度。此外，我们引入了WikiEarth数据集，该数据集将现有的部分三维重建结果与伪合成参考模型进行配准。实验表明，我们的方法在使用各类经典及基于学习的流程初始化后，能持续改进全局对齐效果，同时缓解了最先进的端到端模型的失效模式。所有代码和数据将公开发布。

---

### 13. Wid3R: Wide Field-of-View 3D Reconstruction via Camera Model Conditioning

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2602.05321)
- **发表日期**: 
- **匹配关键词**: nerf, 3D reconstruction, 3d reconstruction
- **arXiv**: [2602.05321](https://arxiv.org/abs/2602.05321)
- **📥 PDF**: 已下载至本地 (`2602.05321_Wid3R_Wide_Field-of-View_3D_Reconstruction_via_Camera_Model_Conditioning.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: arXiv:2602.05321v2 公告类型：替换  
摘要：本文提出Wid3R，一种支持广角相机模型的多视角视觉几何重建前馈神经网络。与现有方法假设输入为校正图像或针孔模型不同，Wid3R无需显式校准或去畸变即可直接处理广角图像。该方法采用基于射线的球谐函数表示，并引入创新的相机模型标记来实现畸变感知重建。据我们所知，Wid3R是首个支持360度图像的多帧前馈三维重建方法。此外，我们证明通过适配不同相机类型能提升对360度场景的泛化能力，并缓解数据稀疏性问题。Wid3R实现了显著的性能提升，在Zip-NeRF（鱼眼数据集）上AUC@30指标最高提升+33.67，在Stanford2D3D（360度数据集）上最高提升+77.33。

---

### 14. Emergent Neural Automaton Policies: Learning Symbolic Structure from Visuomotor Trajectories

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2603.25903)
- **发表日期**: 
- **匹配关键词**: VLA
- **arXiv**: [2603.25903](https://arxiv.org/abs/2603.25903)
- **📥 PDF**: 已下载至本地 (`2603.25903_Emergent_Neural_Automaton_Policies_Learning_Symbolic_Structure_from_Visuomotor_Trajectories.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: arXiv:2603.25903v1 公告类型：新  
摘要：将机器人学习扩展到长时程任务仍然是一个艰巨的挑战。端到端策略通常缺乏有效长期推理所需的结构先验，而传统的神经符号方法则严重依赖手工设计的符号先验。为解决这一问题，我们提出了ENAP（涌现神经自动机策略）框架，该框架允许从视觉运动演示中自适应地涌现出双层神经符号策略。具体而言，我们首先采用自适应聚类和L*算法的扩展，从视觉运动数据中推断出一个Mealy状态机，作为可解释的高层规划器，捕捉潜在的任务模式。随后，这一离散结构通过行为克隆（BC）指导低层反应式残差网络学习精确的连续控制。通过显式建模离散转换和连续残差的任务结构，ENAP在无需任务特定标签的情况下实现了高样本效率和可解释性。在复杂操作和长时程任务上的大量实验表明，ENAP在低数据场景下比最先进的端到端视觉语言动作策略性能提升高达27%，同时提供了机器人意图的结构化表示（图1）。

---

### 15. Realtime-VLA V2: Learning to Run VLAs Fast, Smooth, and Accurate

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2603.26360)
- **发表日期**: 
- **匹配关键词**: VLA
- **arXiv**: [2603.26360](https://arxiv.org/abs/2603.26360)
- **📥 PDF**: 已下载至本地 (`2603.26360_Realtime-VLA_V2_Learning_to_Run_VLAs_Fast,_Smooth,_and_Accurate.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: arXiv:2603.26360v1 公告类型：新  
摘要：在将视觉语言动作模型应用于现实世界机器人任务时，执行速度至关重要。在先前的工作arXiv:2510.26742中，我们分析了如何在GPU上实现VLA神经计算的快速处理。然而，我们尚未解决如何在实际机器人上部署VLA系统的问题。本报告描述了一系列实用技术，旨在实现VLA驱动机器人在需要精确性和灵活性的现实任务中以令人印象深刻的速度进行端到端运行。技术栈涵盖校准、规划与控制，以及基于学习的方法以确定最佳执行速度。在我们展示的任务中，机器人的执行速度甚至与人类日常操作相当，并接近我们轻量级机械臂的硬件极限。未加速的视频和推理轨迹可在https://dexmal.github.io/realtime-vla-v2/获取。

---

