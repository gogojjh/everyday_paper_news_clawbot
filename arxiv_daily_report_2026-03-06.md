# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-03-06 08:04

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 4/20 篇提供

**🌟 Highlight**: 14 篇 | **📌 Poster**: 6 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. RoboCasa365: A Large-Scale Simulation Framework for Training and Benchmarking Generalist Robots

- **作者**: Soroush Nasiriany, Sepehr Nasiriany, Abhiram Maddukuri, Yuke Zhu ⭐
  - **高亮作者**: Yuke Zhu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.04356v1)
- **发表日期**: 2026-03-04
- **匹配关键词**: mobile manipulation
- **arXiv**: [2603.04356v1](http://arxiv.org/abs/2603.04356v1)
- **📥 PDF**: 已下载至本地 (`2603.04356v1_RoboCasa365_A_Large-Scale_Simulation_Framework_for_Training_and_Benchmarking_Generalist_Robots.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 机器人学习领域的最新进展加速了通用机器人技术的发展，这类机器人能够在人类环境中执行日常任务。然而，我们距离这一愿景的实现还有多远，目前仍难以准确评估。该领域缺乏一个可复现、大规模的系统性评估基准。为填补这一空白，我们推出了RoboCasa365——一个面向家庭移动操作任务的综合性仿真基准平台。基于RoboCasa平台构建的RoboCasa365涵盖了365项日常任务，覆盖2500个多样化的厨房场景，提供超过600小时的人类示范数据及1600余小时的合成示范数据，使其成为研究通用策略最具多样性和规模性的资源库之一。该平台旨在支持多任务学习、机器人基础模型训练和终身学习等不同问题场景的系统性评估。我们采用前沿方法在此基准上进行了大量实验，分析了任务多样性、数据集规模和环境变化对泛化能力的影响。实验结果揭示了影响通用机器人性能的关键因素，为该领域未来的发展策略提供了新的见解。

---

### 2. RVN-Bench: A Benchmark for Reactive Visual Navigation

- **作者**: Jaewon Lee, Jaeseok Heo, Gunmin Lee, Howoong Jun, Jeongwoo Oh, Songhwai Oh
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.03953v1)
- **发表日期**: 2026-03-04
- **匹配关键词**: navigation, visual navigation
- **arXiv**: [2603.03953v1](http://arxiv.org/abs/2603.03953v1)
- **📥 PDF**: 已下载至本地 (`2603.03953v1_RVN-Bench_A_Benchmark_for_Reactive_Visual_Navigation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 安全视觉导航对于在杂乱环境中运行的室内移动机器人至关重要。然而，现有基准测试往往忽略碰撞问题，或专为室外场景设计，使其不适用于室内视觉导航。为弥补这一不足，我们提出了反应式视觉导航基准测试（RVN-Bench），这是一个面向室内移动机器人的碰撞感知基准测试平台。在RVN-Bench中，智能体仅依靠视觉观测且无预设地图，必须在先前未接触过的环境中依次抵达目标位置，同时避免碰撞。该平台基于Habitat 2.0模拟器，利用高保真HM3D场景构建，提供大规模多样化的室内环境，定义了碰撞感知导航任务与评估指标，并配备了标准化训练与基准测试工具。通过提供在线强化学习环境、轨迹图像数据集生成器，以及用于记录碰撞事件的负轨迹图像数据集制作工具，RVN-Bench同时支持在线与离线学习。实验表明，基于RVN-Bench训练的策略能有效泛化至未知环境，验证了其作为安全鲁棒视觉导航标准化基准测试平台的价值。代码及相关资料详见：https://rvn-bench.github.io/。

---

### 3. Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning

- **作者**: Huihan Liu, Changyeon Kim, Bo Liu, Minghuan Liu, Yuke Zhu ⭐
  - **高亮作者**: Yuke Zhu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.03818v1)
- **发表日期**: 2026-03-04
- **匹配关键词**: VLA, vision-language-action model, vision-language-action
- **arXiv**: [2603.03818v1](http://arxiv.org/abs/2603.03818v1)
- **📥 PDF**: 已下载至本地 (`2603.03818v1_Pretrained_Vision-Language-Action_Models_are_Surprisingly_Resistant_to_Forgetting_in_Continual_Learn.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 持续学习是机器人策略学习领域长期存在的挑战，要求策略在不断获取新技能的同时避免灾难性遗忘已掌握技能。尽管先前研究已对从零训练的小规模行为克隆策略模型中的持续学习进行了广泛探讨，但在现代大规模预训练视觉-语言-动作模型中的表现仍待深入探索。本研究发现，与从零训练的小型策略模型相比，预训练的VLA模型展现出显著的抗遗忘特性。简单的经验回放方法在VLA模型上表现优异，有时即使使用极小的回放数据量也能实现零遗忘。分析表明，预训练对下游持续学习性能具有关键影响：大规模预训练模型仅需少量回放缓冲区即可有效缓解遗忘，同时保持强大的前向学习能力。此外，研究发现VLA模型在学习新任务期间虽可能出现性能下降，但仍能保留先前任务的相关知识。这种知识保留特性使得模型能够通过微调快速恢复看似遗忘的技能。综合而言，这些发现表明大规模预训练从根本上改变了持续学习的动态机制，使模型能够通过简单回放方法持续获取新技能。代码及更多信息详见https://ut-austin-rpl.github.io/continual-vla。

---

### 4. Cognition to Control - Multi-Agent Learning for Human-Humanoid Collaborative Transport

- **作者**: Hao Zhang, Ding Zhao, H. Eric Tseng
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.03768v1)
- **发表日期**: 2026-03-04
- **匹配关键词**: affordance, vision-language-action, human-robot collaboration, VLA
- **arXiv**: [2603.03768v1](http://arxiv.org/abs/2603.03768v1)
- **📥 PDF**: 已下载至本地 (`2603.03768v1_Cognition_to_Control_-_Multi-Agent_Learning_for_Human-Humanoid_Collaborative_Transport.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 有效的人机协作需要将高层意图转化为接触稳定的全身运动，并持续适应人类伙伴。许多视觉-语言-动作系统学习从观察到指令再到动作的端到端映射，但它们通常强调反应式行为，未能明确如何将持续的系统2式深思熟虑与可靠、低延迟的连续控制相结合。这一缺陷在多智能体人机协作中尤为突出，因为长期协调决策与物理执行必须在接触、可行性和安全约束下协同演化。我们通过认知到控制三层架构解决这一局限，该架构明确了从深思到控制的路径：基于视觉语言模型的感知层维护持久场景参照并推断具身感知的可用性/约束；作为系统2核心的深思技能/协调层通过去中心化多智能体强化学习优化长期技能选择与序列，将其建模为具有共享任务进度编码势函数的马尔可夫势博弈；以及全身控制层高频执行选定技能，同时确保运动学/动力学可行性与接触稳定性。深思层作为相对于标称控制器的残差策略实现，无需显式角色分配即可内化伙伴动态。协作操控任务实验表明，相比单智能体和端到端基线方法，本架构在成功率与鲁棒性上表现更优，实现了稳定协调与涌现的领导者-跟随者行为。

---

### 5. HALyPO: Heterogeneous-Agent Lyapunov Policy Optimization for Human-Robot Collaboration

- **作者**: Hao Zhang, Yaru Niu, Yikai Wang, Ding Zhao, H. Eric Tseng
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.03741v1)
- **发表日期**: 2026-03-04
- **匹配关键词**: exploration, human-robot collaboration
- **arXiv**: [2603.03741v1](http://arxiv.org/abs/2603.03741v1)
- **📥 PDF**: 已下载至本地 (`2603.03741v1_HALyPO_Heterogeneous-Agent_Lyapunov_Policy_Optimization_for_Human-Robot_Collaboration.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 为提升人机协作的泛化能力与鲁棒性，机器人需应对人类行为与情境的组合多样性，这推动了多智能体强化学习的发展。然而，机器人系统与人类智能体间的内在异质性会在学习过程中产生理性鸿沟——即分散式最优响应动态与集中式协同上升机制间的变分失配。由此形成的学习问题属于一般和可微博弈范畴，若无额外结构约束，独立策略梯度更新可能产生振荡或发散现象。本研究提出异构智能体李雅普诺夫策略优化方法，通过在参数空间分歧度量上强制实施步进式李雅普诺夫递减条件，直接在策略参数空间建立形式化稳定性。与传统基于李雅普诺夫的安全强化学习（针对约束马尔可夫决策过程中的状态/轨迹约束）不同，本方法运用李雅普诺夫认证机制来稳定分散式策略学习。该方法通过最优二次投影修正分散式梯度，确保理性鸿沟的单调收缩，实现对开放式交互空间的有效探索。大量仿真实验与真实世界人形机器人测试表明，这种经过认证的稳定性显著提升了协作边缘场景中的泛化能力与鲁棒性。

---

### 6. PROSPECT: Unified Streaming Vision-Language Navigation via Semantic--Spatial Fusion and Latent Predictive Representation

- **作者**: Zehua Fan, Wenqi Lyu, Wenxuan Song, Linge Zhao, Yifei Yang, Xi Wang, Junjie He, Lida Huang, Haiyan Liu, Bingchuan Sun, Guangjun Bao, Xuanyao Mao, Liang Xu, Yan Wang, Feng Gao
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.03739v1)
- **发表日期**: 2026-03-04
- **匹配关键词**: VLA, vision-language-action, VLN, navigation
- **arXiv**: [2603.03739v1](http://arxiv.org/abs/2603.03739v1)
- **📥 PDF**: 已下载至本地 (`2603.03739v1_PROSPECT_Unified_Streaming_Vision-Language_Navigation_via_Semantic--Spatial_Fusion_and_Latent_Predic.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 多模态大语言模型（MLLMs）推动了零样本端到端视觉语言导航（VLN）的发展，但鲁棒的导航不仅需要语义理解，还需对环境动态与空间结构进行预测建模。我们提出PROSPECT——一种融合流式视觉语言动作（VLA）策略与潜在预测表征学习的统一流式导航智能体。PROSPECT采用CUT3R作为流式三维基础空间编码器，生成长上下文、绝对尺度的空间特征，并通过交叉注意力将其与SigLIP语义特征融合。训练过程中，我们引入可学习的流式查询令牌，这些令牌查询流式上下文并预测下一步的二维与三维潜在特征（而非像素或显式模态），并在冻结的SigLIP与CUT3R教师模型的潜在空间中进行监督。预测分支在无需推理开销的情况下塑造内部表征。在VLN-CE基准测试及真实机器人部署中的实验表明，该方法实现了最先进的性能，并在多样化光照条件下展现出更强的长时程鲁棒性。我们将很快向社区开源代码。

---

### 7. MEM: Multi-Scale Embodied Memory for Vision Language Action Models

- **作者**: Marcel Torne, Karl Pertsch, Homer Walke, Kyle Vedder, Suraj Nair, Brian Ichter, Allen Z. Ren, Haohuan Wang, Jiaming Tang, Kyle Stachowicz, Karan Dhabalia, Michael Equi, Quan Vuong, Jost Tobias Springenberg, Sergey Levine, Chelsea Finn, Danny Driess ⭐
  - **高亮作者**: Sergey Levine, Chelsea Finn
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.03596v1)
- **发表日期**: 2026-03-04
- **匹配关键词**: vision language action model, vision language action
- **arXiv**: [2603.03596v1](http://arxiv.org/abs/2603.03596v1)
- **📥 PDF**: 已下载至本地 (`2603.03596v1_MEM_Multi-Scale_Embodied_Memory_for_Vision_Language_Action_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 传统上，端到端机器人学习中的记忆机制通常涉及将一系列历史观测数据输入到学习策略中。然而，在复杂的多阶段现实任务中，机器人的记忆需要以多粒度表征过去事件：从捕捉抽象语义概念的长期记忆（例如烹饪晚餐的机器人应记住食谱中已完成哪些步骤），到记录近期事件并补偿遮挡的短期记忆（例如机器人需记住被机械臂遮挡的待拾取物体）。本研究的核心观点是：用于长时程机器人控制的有效记忆架构应融合多种模态以捕捉不同抽象层级的信息。我们提出了多尺度具身记忆方法，这是一种在机器人策略中实现混合模态长时程记忆的技术。该方法通过视频编码器压缩视频式短时程记忆，并与文本式长时程记忆相结合，使机器人策略能够执行长达十五分钟的任务，如清理厨房或制作烤奶酪三明治。此外，我们发现记忆机制能使多尺度具身记忆策略在情境中智能调整操作策略。

---

### 8. Utonia: Toward One Encoder for All Point Clouds

- **作者**: Yujia Zhang, Xiaoyang Wu, Yunhan Yang, Xianzhe Fan, Han Li, Yuechen Zhang, Zehao Huang, Naiyan Wang, Hengshuang Zhao
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.03283v1)
- **发表日期**: 2026-03-03
- **匹配关键词**: vision-language-action
- **arXiv**: [2603.03283v1](http://arxiv.org/abs/2603.03283v1)
- **📥 PDF**: 已下载至本地 (`2603.03283v1_Utonia_Toward_One_Encoder_for_All_Point_Clouds.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 我们梦想着这样一个未来：来自所有领域的点云能够汇聚一堂，共同构建一个惠及所有领域的统一模型。为实现这一目标，我们提出了Utonia——这是迈向跨领域训练单一自监督点云Transformer编码器的第一步，涵盖遥感、室外激光雷达、室内RGB-D序列、以物体为中心的CAD模型，以及从纯RGB视频中提取的点云。尽管这些数据在感知几何、密度和先验知识上存在显著差异，Utonia仍能学习到一个跨领域一致的表示空间。这种统一不仅提升了感知能力，还揭示了仅在多领域联合训练时才会出现的引人注目的涌现行为。除了感知任务，我们还观察到Utonia的表征能力可进一步赋能具身智能与多模态推理：在机器人操作任务中，基于Utonia特征的视觉-语言-动作策略得到显著改善；将其集成到视觉-语言模型中，空间推理能力也获得提升。我们希望Utonia能成为稀疏三维数据基础模型发展的一步阶梯，并为增强现实/虚拟现实、机器人技术和自动驾驶等下游应用提供支持。

---

### 9. ZipMap: Linear-Time Stateful 3D Reconstruction with Test-Time Training

- **作者**: Haian Jin, Rundi Wu, Tianyuan Zhang, Ruiqi Gao, Jonathan T. Barron, Noah Snavely, Aleksander Holynski
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.04385v1)
- **发表日期**: 2026-03-04
- **匹配关键词**: 3d reconstruction, 3D reconstruction
- **arXiv**: [2603.04385v1](http://arxiv.org/abs/2603.04385v1)
- **📥 PDF**: 已下载至本地 (`2603.04385v1_ZipMap_Linear-Time_Stateful_3D_Reconstruction_with_Test-Time_Training.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 前馈Transformer模型推动了三维视觉领域的快速发展，但VGGT和$π^3$等先进方法的计算成本随输入图像数量呈二次方增长，在处理大规模图像集时效率低下。序列重建方法虽能降低计算成本，却以牺牲重建质量为代价。我们提出ZipMap模型——一种具备状态保持能力的前馈模型，在实现线性时间双向三维重建的同时，其精度达到甚至超越了二次时间复杂度方法。ZipMap采用训练时测试层技术，通过单次前向传播即可将整个图像集压缩为紧凑的隐式场景状态，在单个H100 GPU上实现10秒内重建超过700帧图像，比VGGT等先进方法快20倍以上。此外，我们展示了状态化表征在实时场景状态查询中的优势，并将其扩展至序列流式重建场景。

---

### 10. Perception-Aware Time-Optimal Planning for Quadrotor Waypoint Flight

- **作者**: Chao Qin, Jiaxu Xing, Rudolf Reiter, Angel Romero, Yifan Lin, Hugh H. -T. Liu, Davide Scaramuzza ⭐
  - **高亮作者**: Davide Scaramuzza
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.04305v1)
- **发表日期**: 2026-03-04
- **匹配关键词**: exploration
- **arXiv**: [2603.04305v1](http://arxiv.org/abs/2603.04305v1)
- **📥 PDF**: 已下载至本地 (`2603.04305v1_Perception-Aware_Time-Optimal_Planning_for_Quadrotor_Waypoint_Flight.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 敏捷四旋翼飞行在控制、驱动和机载感知方面不断突破极限。尽管时间最优轨迹规划已被广泛研究，但现有方法通常忽略了飞行器动力学、环境几何结构与机载状态估计视觉需求之间的紧密耦合。这导致动态可行的轨迹可能因视觉质量下降而在闭环执行中失败。本文提出了一种基于视觉的四旋翼统一时间最优轨迹优化框架，该框架将感知约束与完整的非线性动力学、旋翼驱动限制、空气动力效应、相机视场约束以及凸几何门框表征进行显式整合。

该框架能够为具有不同形状和朝向门框的任意赛道求解最小圈时轨迹，同时保持数值鲁棒性和计算效率。我们推导出基于信息论的位置不确定性度量标准，通过三个感知目标将其融入规划器：位置不确定性最小化、序列视场约束和前视对准。这使得系统能够系统性地探索速度与感知可靠性之间的权衡关系。

为精确跟踪生成的感知感知轨迹，我们开发了分离横向误差与进程误差的模型预测轮廓跟踪控制器。实验证明，在具有挑战性的Split-S赛道上，系统实现了最高9.8米/秒的实际飞行速度，平均跟踪误差仅为0.07米，闭环成功率从55%提升至100%。该研究系统为探索感知感知、时间最优自主飞行的根本极限提供了可扩展的基准框架。

---

### 11. EmbodiedSplat: Online Feed-Forward Semantic 3DGS for Open-Vocabulary 3D Scene Understanding

- **作者**: Seungjun Lee, Zihan Wang, Yunsong Wang, Gim Hee Lee
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.04254v1)
- **发表日期**: 2026-03-04
- **匹配关键词**: 3d reconstruction, exploration, 3D reconstruction
- **arXiv**: [2603.04254v1](http://arxiv.org/abs/2603.04254v1)
- **📥 PDF**: 已下载至本地 (`2603.04254v1_EmbodiedSplat_Online_Feed-Forward_Semantic_3DGS_for_Open-Vocabulary_3D_Scene_Understanding.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://0nandon.github.io/EmbodiedSplat/.
- **中文摘要**: 在具身任务中，智能体需要以在线且近乎实时的方式构建和理解三维场景，因此通过探索即时理解三维场景至关重要。本研究提出EmbodiedSplat——一种面向开放词汇场景理解的在线前馈式3D高斯泼溅方法，能够从流式图像中同时实现在线三维重建与三维语义理解。与现有通常局限于离线或逐场景优化设置的开放词汇3DGS方法不同，我们的目标具有双重性：1）以在线方式从超过300张流式图像中重建整个场景的语义嵌入3DGS；2）通过前馈设计实现对新场景的高度泛化能力，并结合实时二维模型支持近乎实时的三维语义重建。为实现这些目标，我们提出了一种结合CLIP全局码本的在线稀疏系数场，将二维CLIP嵌入与每个三维高斯单元绑定，在最小化内存消耗的同时完整保留CLIP的语义泛化能力。此外，我们通过三维U-Net聚合3DGS的部分点云，生成具有三维几何感知的CLIP特征，以弥补面向二维的语言嵌入所缺失的三维几何先验信息。在ScanNet、ScanNet++和Replica等多个室内数据集上的大量实验证明了我们方法的有效性和高效性。项目详情请访问：https://0nandon.github.io/EmbodiedSplat/。

---

### 12. NOVA3R: Non-pixel-aligned Visual Transformer for Amodal 3D Reconstruction

- **作者**: Weirong Chen, Chuanxia Zheng, Ganlin Zhang, Andrea Vedaldi, Daniel Cremers ⭐
  - **高亮作者**: Daniel Cremers
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.04179v1)
- **发表日期**: 2026-03-04
- **匹配关键词**: 3d reconstruction, 3D reconstruction
- **arXiv**: [2603.04179v1](http://arxiv.org/abs/2603.04179v1)
- **📥 PDF**: 已下载至本地 (`2603.04179v1_NOVA3R_Non-pixel-aligned_Visual_Transformer_for_Amodal_3D_Reconstruction.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出NOVA3R方法，这是一种从前馈式非位姿配准图像集中实现非像素对齐三维重建的有效途径。与将几何绑定于单射线预测的像素对齐方法不同，我们的框架通过学习全局、视角无关的场景表征，将重建过程与像素对齐解耦。这一设计解决了像素对齐三维重建中的两个关键局限：(1) 通过完整场景表征同时恢复可见与不可见点云；(2) 在重叠区域生成物理合理的几何结构，显著减少重复构造。为实现这一目标，我们引入了跨未配准图像聚合信息的场景令牌机制，以及基于扩散模型的三维解码器，该解码器能够重建完整的非像素对齐点云。在场景级和物体级数据集上的大量实验表明，NOVA3R在重建精度与完整性方面均优于当前最先进方法。

---

### 13. RIVER: A Real-Time Interaction Benchmark for Video LLMs

- **作者**: Yansong Shi, Qingsong Zhao, Tianxiang Jiang, Xiangyu Zeng, Yi Wang, Limin Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.03985v1)
- **发表日期**: 2026-03-04
- **匹配关键词**: VLA
- **arXiv**: [2603.03985v1](http://arxiv.org/abs/2603.03985v1)
- **📥 PDF**: 已下载至本地 (`2603.03985v1_RIVER_A_Real-Time_Interaction_Benchmark_for_Video_LLMs.pdf`)
- **🔓 开源**: CODE, GITHUB
  - 链接：https://github.com/OpenGVLab/RIVER.
- **中文摘要**: 随着多模态大语言模型的快速发展，其展现出的强大能力令人瞩目，然而现有模型几乎均采用离线处理模式，这限制了实时交互的实现。为填补这一空白，我们推出了实时视频交互基准测试平台（RIVER Bench），专门用于评估在线视频理解能力。RIVER Bench创新性地构建了包含回溯记忆、实时感知与前瞻预测任务的评估框架，该框架更贴近真实对话场景中的渐进式交互，而非一次性处理完整视频。我们采用多源、多时长视频数据进行精细化标注，并明确定义了实时交互格式。通过对各类模型的系统评估发现，离线模型虽然在单轮问答任务中表现良好，但在实时处理方面存在明显不足。针对现有模型在在线视频交互中存在的局限，特别是长期记忆与未来感知能力的缺陷，我们提出了一种通用改进方法，使模型能够更灵活地实现实时人机交互。我们相信这项工作将有力推动实时交互式视频理解模型的发展，并为这一新兴领域的后续研究提供重要启示。数据集与代码已公开于https://github.com/OpenGVLab/RIVER。

---

### 14. SkillVLA: Tackling Combinatorial Diversity in Dual-Arm Manipulation via Skill Reuse

- **作者**: Xuanran Zhai, Zekai Huang, Longyan Wu, Qianyou Zhao, Qiaojun Yu, Jieji Ren, Ce Hao, Harold Soh
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.03836v1)
- **发表日期**: 2026-03-04
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2603.03836v1](http://arxiv.org/abs/2603.03836v1)
- **📥 PDF**: 已下载至本地 (`2603.03836v1_SkillVLA_Tackling_Combinatorial_Diversity_in_Dual-Arm_Manipulation_via_Skill_Reuse.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型的最新进展在双臂操控领域展现出巨大潜力，能够实现复杂行为并泛化至未见环境。然而主流双操作臂VLA框架普遍忽视了组合多样性的关键挑战——不同单臂行为的配对组合可能产生性质完全不同的任务行为，而现有模型未能显式建模这种结构特征。我们认为有效的双臂VLA系统应当支持技能复用能力，即能够将已习得的单臂技能通过新颖的左右配对进行重组，从而避免为每种可能组合单独学习。当前VLA设计将跨臂技能相互耦合，阻碍了这种重组机制并限制了可扩展性。为此我们提出SkillVLA框架，专门为实现双臂操控中的技能复用而设计。大量实验表明，SkillVLA显著提升了技能组合能力，将整体成功率从0%提升至51%，并在协作任务与长时程任务中表现出优异性能。

---

## 📌 Poster

*其他相关研究*

---

### 1. Gaussian Mixture-Based Inverse Perception Contract for Uncertainty-Aware Robot Navigation

- **作者**: Bingyao Du, Joonkyung Kim, Yiwei Lyu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.04329v1)
- **发表日期**: 2026-03-04
- **匹配关键词**: robot navigation, navigation
- **arXiv**: [2603.04329v1](http://arxiv.org/abs/2603.04329v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 在杂乱环境中实现可靠导航，不仅需要感知输出具有高精度，还需配备适用于安全控制的不确定性集合。逆感知契约通过将感知估计映射至以高置信度包含真实状态的集合，为此建立了连接桥梁。然而，现有逆感知契约方法将不确定性实例化为单一椭球集，并依赖确定性信任分数指导机器人运动。这种表示方法无法捕捉细粒度感知误差的多模态与非规则结构，往往导致集合过于保守并降低导航性能。本研究提出基于高斯混合模型的逆感知契约，通过扩展逆感知契约框架，利用从高斯混合模型导出的椭球置信集之并集来表示不确定性。该设计突破了确定性单集合抽象的限制，能够以形式化保证捕捉细粒度、多模态及非凸的误差结构。我们提出一种学习框架，通过训练高斯混合逆感知契约来兼顾概率包含性、分布匹配与空域惩罚，确保预测集合的有效性与紧致性。研究进一步表明，所得不确定性特征可被下游规划框架用于实时安全导航，在保持概率安全性的同时，实现更少保守性、更高适应性的机器人运动。

---

### 2. OmniPlanner: Universal Exploration and Inspection Path Planning across Robot Morphologies

- **作者**: Angelos Zacharia, Mihir Dharmadhikari, Mohit Singh, Kostas Alexis
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.04284v1)
- **发表日期**: 2026-03-04
- **匹配关键词**: exploration, path planning
- **arXiv**: [2603.04284v1](http://arxiv.org/abs/2603.04284v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 自主机器人系统在复杂非结构化环境中的测绘、监测与巡检应用日益广泛。然而现有路径规划方法大多局限于特定领域（空中、陆地或水下），其可扩展性与跨平台适用性受到制约。本文提出OmniPlanner——一种面向空中、地面及水下机器人的自主探索与巡检统一规划框架。该方法将体积探索与基于视点的巡检策略，以及目标抵达行为集成于单一模块化架构中，并通过平台抽象层捕获形态特异的感知、可通行性与运动约束。这使得同一规划策略能够以最小调整适应不同运动领域。该框架通过大量仿真实验及地下矿井、工业设施、森林、海底掩体与结构化户外环境等实地部署得到验证。在多样化场景中，OmniPlanner展现出鲁棒性能、稳定的跨领域泛化能力，并在探索与巡检效率方面优于代表性前沿基线方法。

---

### 3. SSR: A Generic Framework for Text-Aided Map Compression for Localization

- **作者**: Mohammad Omama, Po-han Li, Harsh Goel, Minkyu Choi, Behdad Chalaki, Vaishnav Tadiparthi, Hossein Nourkhiz Mahjoub, Ehsan Moradi Pari, Sandeep P. Chinchali
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.04272v1)
- **发表日期**: 2026-03-04
- **匹配关键词**: place recognition
- **arXiv**: [2603.04272v1](http://arxiv.org/abs/2603.04272v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 地图构建在机器人定位与下游决策中至关重要。随着机器人在更广泛场景中的部署，其所依赖的地图规模持续扩大。然而，长期存储这些地图（冷存储）、跨网络传输地图或将定位查询发送至云端托管地图，都会产生极高的内存与带宽成本。我们提出一种文本增强压缩框架，在保持高精度定位能力的同时显著降低内存与带宽占用。其核心思想是将文本视为替代模态——一种可通过大型语言模型实现无损压缩的形式。我们提出利用轻量级文本描述结合极小的图像特征向量，通过捕捉"互补信息"来构建地图任务的紧凑表征。在此基础上，我们创新的相似空间复现技术能够一次性学习自适应图像嵌入，仅捕获与文本描述形成"互补"的信息。我们在多个下游定位任务中验证了该压缩框架的有效性，包括视觉位置识别以及室内外场景下以物体为中心的蒙特卡洛定位。在TokyoVal、Pittsburgh30k、Replica和KITTI等前沿数据集上的实验表明，该技术实现了比现有基线方法高2倍的压缩效率。

---

### 4. GarmentPile++: Affordance-Driven Cluttered Garments Retrieval with Vision-Language Reasoning

- **作者**: Mingleyang Li, Yuran Wang, Yue Chen, Tianxing Chen, Jiaqi Liang, Zishun Shen, Haoran Lu, Ruihai Wu, Hao Dong
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.04158v1)
- **发表日期**: 2026-03-04
- **匹配关键词**: affordance
- **arXiv**: [2603.04158v1](http://arxiv.org/abs/2603.04158v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://garmentpile2.github.io/.
- **中文摘要**: 服装操作因其在家庭辅助机器人中的关键作用而受到越来越多的关注。然而，现有的大多数服装操作研究都假设初始状态仅包含一件衣物，而在实际场景中，衣物堆叠的情况更为常见。为弥补这一差距，我们提出了一种新颖的衣物检索流程，该流程不仅能根据语言指令执行安全、整洁的检索，还能确保每次尝试仅检索一件衣物，从而为下游任务（如折叠、悬挂、穿着）的执行奠定坚实基础。我们的流程将视觉语言推理与视觉可供性感知无缝集成，充分利用了视觉语言模型的高层推理与规划能力，以及视觉可供性在底层动作中的泛化能力。为增强视觉语言模型对衣物堆中每件衣物状态的全面感知，我们采用视觉分割模型（SAM2）对衣物堆进行对象分割，为基于视觉语言模型的推理提供充分的视觉线索。此外，我们还引入了掩码微调机制，以应对初始分割结果不理想的情况。针对大型或长款衣物，以及因抓取点判断错误导致的衣物过度下垂等问题——这些情况对单臂操作而言较为困难——我们部署了双臂协作框架进行处理。我们的流程在真实世界和仿真环境中的多样化任务与不同场景下均表现出一致的有效性。项目页面：https://garmentpile2.github.io/。

---

### 5. Lightweight Visual Reasoning for Socially-Aware Robots

- **作者**: Alessio Galatolo, Ronald Cumbal, Alexandros Rouchitsas, Katie Winkle, Didem Gürdür Broo, Ginevra Castellano
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.03942v1)
- **发表日期**: 2026-03-04
- **匹配关键词**: human-robot interaction, HRI, navigation
- **arXiv**: [2603.03942v1](http://arxiv.org/abs/2603.03942v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: GITHUB
  - 链接：https://github.com/alessioGalatolo/VLM-Reasoning-for-Robotics
- **中文摘要**: 在共享人类环境中运行的机器人不仅需要导航、交互和感知周围环境，还必须能够解读并应对动态且往往不可预测的人类行为。尽管近期研究通过视觉语言模型（VLMs）在提升机器人感知与指令跟随能力方面展现出潜力，但在处理多模态人机交互（HRI）的复杂性方面仍存在局限。针对这一挑战，我们提出了一种轻量级的语言到视觉反馈模块，该模块通过门控多层感知机（MLP）将图像令牌的隐藏状态映射回视觉编码器的输入端，实现大语言模型（LLM）与VLM视觉编码器之间的闭环连接，从而在文本语境引导下对场景进行二次解读。我们在三项以机器人为中心的任务上评估了该方法：模拟环境导航（Habitat）、序列场景描述（Mementos-Robotics）以及人类意图识别（自建HRI数据集）。实验结果表明，该方法以不足3%的额外参数量，使Qwen 2.5（7B）模型在导航任务中减少3.3%的移动距离，在场景描述任务中提升0.057分，在意图识别任务中提高2.93%的准确率；Gemma 3（4B）和LLaVA OV 1.5（4B）模型的导航结果存在波动，但在后两项任务中分别获得+0.111/+0.055的描述分数提升和+10.81%/+4.79%的准确率提升。代码已开源：https://github.com/alessioGalatolo/VLM-Reasoning-for-Robotics

---

### 6. IROSA: Interactive Robot Skill Adaptation using Natural Language

- **作者**: Markus Knauer, Samuel Bustamante, Thomas Eiband, Alin Albu-Schäffer, Freek Stulp, João Silvério
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.03897v1)
- **发表日期**: 2026-03-04
- **匹配关键词**: obstacle avoidance
- **arXiv**: [2603.03897v1](http://arxiv.org/abs/2603.03897v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 基础模型已在多个领域展现出卓越能力，而模仿学习则为机器人从有限数据中适应技能提供了系统性方法。将这两种方法相结合，有望直接应用于机器人技术，但这一结合尚未得到充分关注，尤其在工业部署领域。我们提出了一种新颖框架，通过基于工具的系统架构实现开放词汇的技能适应，在语言模型与机器人硬件之间保持保护性抽象层。该方法利用预训练大语言模型选择和参数化特定工具，以调整机器人技能，无需进行微调或直接模型-机器人交互。我们在执行工业轴承环装配任务的7自由度扭矩控制机器人上验证了该框架，通过自然语言指令成功实现了速度调节、轨迹修正和避障等技能适应，同时保持了系统的安全性、透明度和可解释性。

---

