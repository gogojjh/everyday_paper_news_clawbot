# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-04-09 08:03

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 5/20 篇提供

**🌟 Highlight**: 13 篇 | **📌 Poster**: 7 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. BiCoord: A Bimanual Manipulation Benchmark towards Long-Horizon Spatial-Temporal Coordination

- **作者**: Xingyu Peng, Chen Gao, Liankai Jin, Annan Li, Si Liu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.05831v1)
- **发表日期**: 2026-04-07
- **匹配关键词**: bimanual manipulation, VLA
- **arXiv**: [2604.05831v1](http://arxiv.org/abs/2604.05831v1)
- **📥 PDF**: 已下载至本地 (`2604.05831v1_BiCoord_A_Bimanual_Manipulation_Benchmark_towards_Long-Horizon_Spatial-Temporal_Coordination.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 双手操作，即协调使用两个机械臂完成任务，对实现机器人领域人类水平的灵巧性至关重要。近期仿真基准（如RoboTwin和RLBench2）推动了数据驱动的双手操作学习研究。然而，现有任务多为短时程且协调松散，未能捕捉现实世界中双手行为固有的时空耦合特性。为填补这一空白，我们提出了BiCoord——一个面向长时程紧密协调双手操作的基准测试平台。该平台包含多种需要持续臂间依赖性和跨多子目标动态角色交换的任务。同时，我们设计了一套从时间、空间及时空维度评估协调性的量化指标，实现了对双手协作的系统化度量。实验结果表明，代表性操作策略（如DP、RDT、Pi0和OpenVLA-OFT）在长时程高度耦合任务中表现欠佳，揭示了实现长时程紧密协调任务面临的根本性挑战。我们希望BiCoord能为长时程协作操作研究提供基础，并启发未来面向协调感知的机器人学习研究。所有数据集、代码及补充材料可通过https://buaa-colalab.github.io/BiCoord/获取。

---

### 2. Rectified Schrödinger Bridge Matching for Few-Step Visual Navigation

- **作者**: Wuyang Luan, Junhui Li, Weiguang Zhao, Wenjian Zhang, Tieru Wu, Rui Ma
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.05673v1)
- **发表日期**: 2026-04-07
- **匹配关键词**: navigation, visual navigation
- **arXiv**: [2604.05673v1](http://arxiv.org/abs/2604.05673v1)
- **📥 PDF**: 已下载至本地 (`2604.05673v1_Rectified_Schrödinger_Bridge_Matching_for_Few-Step_Visual_Navigation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉导航是具身人工智能的核心挑战，要求自主智能体将高维感知观测转化为连续、长程的动作轨迹。虽然基于扩散模型和薛定谔桥的生成策略能有效捕捉多模态动作分布，但由于高方差随机传输特性，它们需要数十个积分步骤，这对实时机器人控制构成了关键障碍。我们提出修正型薛定谔桥匹配框架，该框架利用标准薛定谔桥（$\varepsilon=1$，最大熵传输）与确定性最优传输（$\varepsilon\to 0$，如条件流匹配）之间共享的速度场结构，通过单一熵正则化参数$\varepsilon$进行调控。我们证明了两项关键结论：（1）条件速度场的函数形式在整个$\varepsilon$谱系中保持不变（速度结构不变性），使得单一网络可适用于所有正则化强度；（2）降低$\varepsilon$值能线性减少条件速度方差，从而实现更稳定的粗步长常微分方程积分。通过锚定于缩短传输距离的学习条件先验，RSBM在中等$\varepsilon$值下运行，平衡了多模态覆盖与路径平直度。实验表明，标准桥方法需要$\geq 10$步才能收敛，而RSBM仅用3个积分步骤即可实现超过94%的余弦相似度和92%的成功率——无需蒸馏或多阶段训练——显著缩小了高保真生成策略与具身人工智能低延迟需求之间的差距。

---

### 3. A1: A Fully Transparent Open-Source, Adaptive and Efficient Truncated Vision-Language-Action Model

- **作者**: Kaidong Zhang, Jian Zhang, Rongtao Xu, Yu Sun, Shuoshuo Xue, Youpeng Wen, Xiaoyu Guo, Minghao Guo, Weijia Liufu, Liu Zihou, Kangyi Ji, Yangsong Zhang, Jiarun Zhu, Jingzhi Liu, Zihang Li, Ruiyi Chen, Meng Cao, Jingming Zhang, Shen Zhao, Xiaojun Chang, Feng Zheng, Ivan Laptev, Xiaodan Liang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.05672v1)
- **发表日期**: 2026-04-07
- **匹配关键词**: affordance, VLA, vision-language-action, vision-language-action model
- **arXiv**: [2604.05672v1](http://arxiv.org/abs/2604.05672v1)
- **📥 PDF**: 已下载至本地 (`2604.05672v1_A1_A_Fully_Transparent_Open-Source,_Adaptive_and_Efficient_Truncated_Vision-Language-Action_Model.pdf`)
- **🔓 开源**: CODE
- **中文摘要**: 视觉-语言-动作（VLA）模型已成为开放世界机器人操作的重要范式，但其实际部署常受**成本**制约：十亿级参数的视觉语言模型主干与基于迭代扩散/流的动作头部会带来高延迟与计算开销，使得在通用硬件上实现实时控制成本高昂。我们提出A1——一个完全开源透明的VLA框架，旨在实现低成本、高吞吐量的推理，同时不牺牲操作成功率。该方法利用预训练的视觉语言模型为动作生成提供隐式功能先验。我们完整公开训练体系（训练代码、数据/数据处理流程、中间检查点及评估脚本），以实现端到端的可复现性。A1不仅优化视觉语言模型，更通过引入预算感知的自适应推理机制，协同加速主干网络与**动作头部**：通过监控中间层动作一致性以触发早期终止，并提出跨层截断流匹配方法，实现跨层去噪预热，从而以显著更少的有效去噪迭代生成精确动作。在仿真基准测试（LIBERO、VLABench）与实体机器人（Franka、AgiBot）实验中，A1在显著降低推理成本的同时达到最优成功率（例如流匹配推理的每回合延迟降低达72%，主干计算量减少达76.6%且性能损失微小）。在RoboChallenge测试中，A1以29.00%的平均成功率超越基线模型，包括pi0（28.33%）、X-VLA（21.33%）和RDT-1B（15.00%）。

---

### 4. SnapFlow: One-Step Action Generation for Flow-Matching VLAs via Progressive Self-Distillation

- **作者**: Wuyang Luan, Junhui Li, Weiguang Zhao, Wenjian Zhang, Tieru Wu, Rui Ma
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.05656v1)
- **发表日期**: 2026-04-07
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2604.05656v1](http://arxiv.org/abs/2604.05656v1)
- **📥 PDF**: 已下载至本地 (`2604.05656v1_SnapFlow_One-Step_Action_Generation_for_Flow-Matching_VLAs_via_Progressive_Self-Distillation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 基于流匹配的视觉-语言-动作模型（如pi0、pi0.5和SmolVLA）在通用机器人操作领域已达到最先进水平，但其迭代去噪过程（通常需10步ODE计算）会带来显著延迟：在现代GPU上，仅去噪环节就占端到端推理时间的80%。若简单减少步数会导致不可靠结果——由于速度场未针对单步跳跃校准，多数任务成功率会下降。我们提出SnapFlow，一种即插即用的自蒸馏方法，可将流匹配VLA的多步去噪压缩至单次前向传播（1-NFE）。SnapFlow将标准流匹配样本与一致性样本混合，后者的目标是通过模型自身边缘速度预测计算的两步欧拉捷径速度，从理论上避免了条件速度引起的轨迹漂移。通过零初始化目标时间嵌入技术，网络可在单一架构内切换局部速度估计与全局单步生成。该方法无需外部教师模型、不改变架构，单GPU训练仅需约12小时。我们在参数规模相差6倍的两种VLA架构上使用相同超参数验证：在pi0.5（30亿参数）的四个LIBERO测试集（40项任务、400个场景）中，SnapFlow平均成功率高达98.75%——与10步教师模型的97.75%持平并略有超越——去噪速度提升9.6倍，端到端延迟从274毫秒降至83毫秒；在SmolVLA（5亿参数）上，平均平方误差降低8.3%，端到端加速达3.56倍。对长视野任务的动作步数扫描显示，SnapFlow在不同执行视野下均保持优势：当n_act=5时达到93%成功率，而基线模型仅90%。该方法与层蒸馏和令牌剪枝技术正交，可实现组合式加速效果。

---

### 5. FunRec: Reconstructing Functional 3D Scenes from Egocentric Interaction Videos

- **作者**: Alexandros Delitzas, Chenyangguang Zhang, Alexey Gavryushin, Tommaso Di Mario, Boyang Sun, Rishabh Dabral, Leonidas Guibas, Christian Theobalt, Marc Pollefeys, Francis Engelmann, Daniel Barath ⭐
  - **高亮作者**: Marc Pollefeys
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.05621v1)
- **发表日期**: 2026-04-07
- **匹配关键词**: affordance
- **arXiv**: [2604.05621v1](http://arxiv.org/abs/2604.05621v1)
- **📥 PDF**: 已下载至本地 (`2604.05621v1_FunRec_Reconstructing_Functional_3D_Scenes_from_Egocentric_Interaction_Videos.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出FunRec方法，可直接从第一人称视角的RGB-D交互视频中重建室内场景的功能性三维数字孪生。与现有依赖受控设置、多状态捕捉或CAD先验的铰接重建方法不同，FunRec直接在真实人类交互序列上运行，以恢复可交互的三维场景。该方法能自动发现铰接部件、估算其运动学参数、追踪三维运动轨迹，并在规范空间中重建静态与动态几何结构，最终生成兼容仿真的网格模型。在全新构建的真实与模拟基准测试中，FunRec大幅超越先前工作：部件分割的mIoU指标提升最高达50%，关节与姿态误差降低5-10倍，重建精度显著提高。我们进一步展示了其在仿真URDF/USD导出、手部引导的功用映射以及机器人-场景交互等领域的应用潜力。

---

### 6. Grounding Hierarchical Vision-Language-Action Models Through Explicit Language-Action Alignment

- **作者**: Theodor Wulff, Federico Tavella, Rahul Singh Maharjan, Manith Adikari, Angelo Cangelosi
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.05614v1)
- **发表日期**: 2026-04-07
- **匹配关键词**: human-robot collaboration, VLA, vision-language-action, vision-language-action model
- **arXiv**: [2604.05614v1](http://arxiv.org/abs/2604.05614v1)
- **📥 PDF**: 已下载至本地 (`2604.05614v1_Grounding_Hierarchical_Vision-Language-Action_Models_Through_Explicit_Language-Action_Alignment.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 实现机器人透明度是迈向有效人机协作的关键一步。为达到透明化，机器人的自然语言交流必须与其行为保持一致，并明确植根于任务与环境之中。现有的分层视觉-语言-动作模型能够生成语言描述（例如通过思维链）并执行底层动作，但当前研究未在训练过程中充分考虑这些模态间的显式对齐。为填补这一关键空白，我们提出了一种新颖的训练框架，该框架将分层视觉-语言-动作模型的子任务描述显式地锚定在视觉观察与动作空间中。我们采用对比模型评估生成语言与对应动作轨迹之间的匹配度，通过直接对不同语言-轨迹配对进行对齐排序，借助离线偏好学习优化分层视觉-语言-动作模型的语义锚定能力。我们在LanguageTable数据集（人类语言标注轨迹的基准数据集）上验证了该框架，不仅为多模态锚定表征提供了关键见解，同时建立了性能媲美全监督微调的强基线，显著降低了对高成本数据标注的依赖。

---

### 7. Uncovering Linguistic Fragility in Vision-Language-Action Models via Diversity-Aware Red Teaming

- **作者**: Baoshun Tong, Haoran He, Ling Pan, Yang Liu, Liang Lin
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.05595v1)
- **发表日期**: 2026-04-07
- **匹配关键词**: VLA, vision-language-action, vision-language-action model
- **arXiv**: [2604.05595v1](http://arxiv.org/abs/2604.05595v1)
- **📥 PDF**: 已下载至本地 (`2604.05595v1_Uncovering_Linguistic_Fragility_in_Vision-Language-Action_Models_via_Diversity-Aware_Red_Teaming.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型在机器人操作领域取得了显著成功。然而，其对语言细微差异的鲁棒性仍是一个关键且尚未充分探索的安全问题，给实际部署带来了重大安全风险。红队测试（即识别可能引发灾难性行为的环境场景）是确保具身人工智能代理安全部署的重要环节。强化学习（RL）已成为自动化红队测试中一种有前景的方法，旨在揭示这些潜在漏洞。然而，基于强化学习的标准对抗方法因其奖励最大化的特性，常陷入严重的模式坍塌问题——倾向于收敛到一组狭窄的、重复的失败模式，无法全面揭示有意义的风险图谱。为弥补这一不足，我们提出了一种新颖的**多样性感知具身红队测试框架**，旨在暴露VLA模型面对语言变异的脆弱性。该框架通过评估均匀策略生成多样化挑战性指令，同时确保其攻击有效性（以物理模拟器中的执行失败率为衡量标准）。我们在多个机器人基准测试中，针对包括$π_0$和OpenVLA在内的两种先进VLA模型进行了广泛实验。结果表明，我们的方法能持续发现更广泛且更有效的对抗指令，将平均任务成功率从93.33%降至5.85%，这为压力测试VLA代理提供了一种可扩展的方法，有助于在实际部署前暴露关键的安全盲点。

---

### 8. ExpressMM: Expressive Mobile Manipulation Behaviors in Human-Robot Interactions

- **作者**: Souren Pashangpour, Haitong Wang, Matthew Lisondra, Goldie Nejat
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.05320v1)
- **发表日期**: 2026-04-07
- **匹配关键词**: mobile manipulation, HRI, mobile manipulator, human-robot interaction, vision-language-action
- **arXiv**: [2604.05320v1](http://arxiv.org/abs/2604.05320v1)
- **📥 PDF**: 已下载至本地 (`2604.05320v1_ExpressMM_Expressive_Mobile_Manipulation_Behaviors_in_Human-Robot_Interactions.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 移动操作机器人在以人为中心的环境中执行任务的应用日益广泛。在完成任务的同时，它们还应能够通过富有表现力的机器人行为向周围人群传达其意图。先前关于机器人表现行为的研究主要采用预编程或基于示教学习的表现动作，以及由大型语言模型生成的高层交互方式。这些现有方法大多未考虑在任务执行过程中用户可能中断、修改或重定向机器人动作的人机交互场景。本文提出创新的ExpressMM框架，该框架整合了基于视觉语言模型的高层语言引导规划器（用于感知与对话推理）与低层视觉-语言-动作策略，以在协作式人机交互任务中生成富有表现力的机器人行为。此外，ExpressMM支持可中断的交互模式，能够适应用户更新的指令或任务重定向需求。我们在协作装配场景中通过移动操作机器人辅助人类完成任务的案例展示了ExpressMM系统，并基于现场人机交互演示开展了观众评估。问卷结果表明，启用ExpressMM的表现行为能帮助观察者清晰理解机器人的动作与意图，同时支持符合社交规范且易于理解的交互。参与者还反馈，机器人在演示过程中对协作任务具有实用价值，其行为可预测且安全，这增强了人们对机器人在协作任务中实用性、安全性和可预测性的积极认知。

---

### 9. StarVLA: A Lego-like Codebase for Vision-Language-Action Model Developing

- **作者**: StarVLA Community
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.05014v1)
- **发表日期**: 2026-04-06
- **匹配关键词**: VLA, vision-language-action, vision-language-action model
- **arXiv**: [2604.05014v1](http://arxiv.org/abs/2604.05014v1)
- **📥 PDF**: 已下载至本地 (`2604.05014v1_StarVLA_A_Lego-like_Codebase_for_Vision-Language-Action_Model_Developing.pdf`)
- **🔓 开源**: GITHUB, CODE
  - 链接：https://github.com/starVLA/starVLA.
- **中文摘要**: 构建通用具身智能体需要整合感知、语言理解和行动能力，这些正是基于多模态基础模型的视觉-语言-动作（VLA）方法所解决的核心问题，其中涵盖了视觉语言模型与世界模型的最新进展。尽管发展迅速，现有VLA方法仍因架构、代码库和评估协议互不兼容而呈现碎片化，阻碍了系统性比较与结果复现。为此，我们推出面向VLA研究的开源代码库StarVLA，该框架从三个方面应对上述挑战：首先，它提供模块化的主干网络-动作头架构，支持VLM主干（如Qwen-VL）与世界模型主干（如Cosmos），并整合了代表性动作解码范式，所有组件均采用可独立替换的共享抽象设计；其次，框架提供可复用的训练策略，包括跨具身学习与多模态协同训练，这些策略在支持的范式中保持一致性；再者，StarVLA通过统一评估接口集成了主流基准测试（如LIBERO、SimplerEnv、RoboTwin~2.0、RoboCasa-GR1和BEHAVIOR-1K），同时支持仿真环境与真实机器人部署。此外，StarVLA内置简洁且完全可复现的单基准训练方案，在极简数据工程条件下，已使VLM与世界模型主干在多项基准测试中达到或超越现有方法。据我们所知，StarVLA是目前最全面的开源VLA框架之一，有望显著降低现有方法复现与新方法原型开发的难度。本框架将持续维护与扩展，项目进展将同步更新于技术报告。代码与文档详见https://github.com/starVLA/starVLA。

---

### 10. E-VLA: Event-Augmented Vision-Language-Action Model for Dark and Blurred Scenes

- **作者**: Jiajun Zhai, Hao Shi, Shangwei Guo, Kailun Yang, Kaiwei Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.04834v1)
- **发表日期**: 2026-04-06
- **匹配关键词**: VLA, vision-language-action, perception-action, vision-language-action model
- **arXiv**: [2604.04834v1](http://arxiv.org/abs/2604.04834v1)
- **📥 PDF**: 已下载至本地 (`2604.04834v1_E-VLA_Event-Augmented_Vision-Language-Action_Model_for_Dark_and_Blurred_Scenes.pdf`)
- **🔓 开源**: GITHUB, CODE
  - 链接：https://github.com/JJayzee/E-VLA.
- **中文摘要**: 机器人视觉-语言-动作（VLA）模型在开放式操作任务中展现出良好的泛化能力，但其感知系统在极端低光、运动模糊和黑场裁剪等传感退化条件下表现脆弱。本文提出E-VLA——一种事件增强型VLA框架，能够在传统帧式视觉不可靠时提升操作鲁棒性。该方法不依赖事件流重建图像，而是直接利用事件流中的运动与结构线索，在恶劣条件下保持语义感知及感知-动作一致性。我们搭建了配备DAVIS346事件相机的开源遥操作平台，采集了涵盖多任务与多光照条件的真实世界同步RGB-事件-动作操作数据集。同时提出轻量化、与预训练模型兼容的事件集成策略，并研究事件窗口化与融合技术以实现稳定部署。实验表明，即使是简单的无参数融合（如在RGB图像上叠加累积事件图），也能显著提升黑暗与强模糊场景的鲁棒性：在20勒克斯光照的抓放任务中，成功率从纯图像输入的0%提升至叠加融合的60%，采用事件适配器后可达90%；在严重运动模糊条件下（1000毫秒曝光），抓放任务成功率从0%提升至20-25%，分类任务从5%提升至32.5%。总体而言，E-VLA系统性地证明了事件驱动感知能有效融入VLA模型，为超越传统帧式成像的鲁棒具身智能指明方向。代码与数据集详见https://github.com/JJayzee/E-VLA。

---

### 11. ROSClaw: A Hierarchical Semantic-Physical Framework for Heterogeneous Multi-Agent Collaboration

- **作者**: Rongfeng Zhao, Xuanhao Zhang, Zhaochen Guo, Xiang Shao, Zhongpan Zhu, Bin He, Jie Chen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.04664v1)
- **发表日期**: 2026-04-06
- **匹配关键词**: navigation, VLA, vision-language-action, VLN
- **arXiv**: [2604.04664v1](http://arxiv.org/abs/2604.04664v1)
- **📥 PDF**: 已下载至本地 (`2604.04664v1_ROSClaw_A_Hierarchical_Semantic-Physical_Framework_for_Heterogeneous_Multi-Agent_Collaboration.pdf`)
- **🔓 开源**: PROJECT_PAGE
- **中文摘要**: 大型语言模型（LLM）与具身智能体的融合提升了高层推理能力，但在语义理解与物理执行之间仍存在关键断层。尽管视觉-语言-动作（VLA）与视觉-语言-导航（VLN）系统使机器人能够根据自然语言指令执行操作与导航任务，它们在处理长时程序列化及时间结构化任务时仍面临挑战。现有框架通常采用模块化流程进行数据收集、技能训练与策略部署，导致实验验证与策略优化的成本高昂。为突破这些局限，我们提出ROSClaw——一个面向异构机器人的智能体框架，将策略学习与任务执行集成于统一的视觉-语言模型（VLM）控制器中。该框架利用异构机器人的e-URDF表征作为物理约束，构建仿真到现实的拓扑映射，实现对仿真与真实世界智能体物理状态的实时访问。我们进一步引入数据收集与状态积累机制，在真实世界执行过程中存储机器人状态、多模态观测与执行轨迹，以支持后续迭代式策略优化。在部署阶段，统一智能体维持推理与执行间的语义连续性，并动态分配任务专属控制权至不同智能体，从而提升多策略执行的鲁棒性。通过建立自主闭环框架，ROSClaw最大程度降低对机器人专属开发流程的依赖。该框架支持硬件级验证、自动化生成SDK级控制程序及基于工具的执行，实现机器人技能的快速跨平台迁移与持续优化。项目页面：https://www.rosclaw.io/。

---

### 12. Veo-Act: How Far Can Frontier Video Models Advance Generalizable Robot Manipulation?

- **作者**: Zhongru Zhang, Chenghan Yang, Qingzhou Lu, Yanjiang Guo, Jianke Zhang, Yucheng Hu, Jianyu Chen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.04502v1)
- **发表日期**: 2026-04-06
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2604.04502v1](http://arxiv.org/abs/2604.04502v1)
- **📥 PDF**: 已下载至本地 (`2604.04502v1_Veo-Act_How_Far_Can_Frontier_Video_Models_Advance_Generalizable_Robot_Manipulation?.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视频生成模型发展迅速，已开始展现出对物理动力学的深刻理解。本文探讨了如Veo-3这类先进视频生成模型在多大程度上能支持可泛化的机器人操作。我们首先研究了一种零样本方法：Veo-3根据当前机器人观测预测未来图像序列，同时逆动力学模型IDM还原对应的机器人动作。IDM仅通过随机交互数据进行训练，无需人工监督或专家示范。其核心思路在于，若视频模型能在图像空间生成物理合理的未来运动轨迹，IDM即可将这些视觉轨迹转化为可执行的机器人动作。我们在仿真环境与真实世界中通过高自由度灵巧手评估了这种"Veo-3+IDM"方法。研究发现，得益于前沿视频模型的强大泛化能力，Veo-3+IDM能持续生成基本正确的任务级轨迹，但其底层控制精度仍不足以可靠完成多数任务。基于此发现，我们开发了分层框架Veo-Act：以Veo-3作为高层运动规划器，配合VLA策略作为底层执行器，显著提升了当前最先进的视觉-语言-动作策略的指令跟随性能。总体而言，我们的研究表明，随着视频生成模型的持续进步，视频模型有望成为可泛化机器人学习的重要组件。

---

### 13. GA-GS: Generation-Assisted Gaussian Splatting for Static Scene Reconstruction

- **作者**: Yedong Shen, Shiqi Zhang, Sha Zhang, Yifan Duan, Xinran Zhang, Wenhao Yu, Lu Zhang, Jiajun Deng, Yanyong Zhang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.04331v1)
- **发表日期**: 2026-04-06
- **匹配关键词**: gaussian splatting
- **arXiv**: [2604.04331v1](http://arxiv.org/abs/2604.04331v1)
- **📥 PDF**: 已下载至本地 (`2604.04331v1_GA-GS_Generation-Assisted_Gaussian_Splatting_for_Static_Scene_Reconstruction.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 从单目视频中重建包含动态物体的静态三维场景，对于虚拟现实和自动驾驶等众多应用具有重要意义。现有方法通常依赖背景进行静态场景重建，限制了恢复被动态物体遮挡区域的能力。本文提出GA-GS——一种用于静态场景重建的生成辅助高斯溅射方法。本研究的核心创新在于利用生成技术辅助重建被遮挡区域。我们采用运动感知模块分割并移除动态区域，随后使用扩散模型对遮挡区域进行修复，提供伪真实值监督。为平衡真实背景与生成区域的贡献，我们为每个高斯基元引入可学习的真实性标量，该标量能在溅射过程中动态调节不透明度，实现真实性感知的渲染与监督。由于现有数据集均未提供包含动态物体的视频静态场景真实值，我们构建了名为Trajectory-Match的数据集，通过固定路径机器人记录每个场景在有/无动态物体时的状态，从而实现对遮挡区域重建的定量评估。在DAVIS数据集及自建数据集上的大量实验表明，GA-GS在静态场景重建方面达到最先进性能，尤其在大规模持续遮挡的挑战性场景中表现突出。

---

## 📌 Poster

*其他相关研究*

---

### 1. Learning-Guided Force-Feedback Model Predictive Control with Obstacle Avoidance for Robotic Deburring

- **作者**: Krzysztof Wojciechowski, Ege Gursoy, Arthur Haffemayer, Sebastien Kleff, Vincent Bonnet, Florent Lamiraux, Nicolas Mansard
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.06133v1)
- **发表日期**: 2026-04-07
- **匹配关键词**: obstacle avoidance
- **arXiv**: [2604.06133v1](http://arxiv.org/abs/2604.06133v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 模型预测控制（MPC）在扭矩控制机器人领域应用广泛，但传统方法常忽略实时力反馈，且在碰撞约束下的密集接触工业任务中表现欠佳。特别是去毛刺作业，需要在复杂构型下实现精确工具插入、稳定力控以及无碰撞圆周运动，这超出了标准MPC流程的能力范围。为此，我们提出了一种融合力反馈MPC与基于扩散的运动先验框架来解决这些挑战。扩散模型作为运动策略的记忆库，为多任务实例提供鲁棒的初始化与自适应能力，而MPC则通过显式力跟踪、扭矩可行性与碰撞规避确保安全执行。我们在执行工业去毛刺任务的扭矩控制机械臂上验证了该方法的有效性。实验表明，即使在难以到达的构型及障碍物约束下，系统仍能实现可靠的工具插入、精确法向力跟踪及圆周去毛刺运动。据我们所知，这是首次将扩散运动先验与力反馈MPC相结合，用于具有碰撞感知的密集接触工业任务。

---

### 2. Intuitive Human-Robot Interaction: Development and Evaluation of a Gesture-Based User Interface for Object Selection

- **作者**: Bijan Kavousian, Oliver Petrovic, Werner Herfs
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.06073v1)
- **发表日期**: 2026-04-07
- **匹配关键词**: human-robot interaction
- **arXiv**: [2604.06073v1](http://arxiv.org/abs/2604.06073v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 手势是人类之间自然的交流方式，也可用于人机交互。本研究提出了一种基于手势的用户界面，通过指向与点击动作实现目标选择。一项包含20名参与者的实验评估了该系统的准确性与选择耗时，结果证明了其在高效协作方面的应用潜力。

---

### 3. Dialogue based Interactive Explanations for Safety Decisions in Human Robot Collaboration

- **作者**: Yifan Xu, Xiao Zhan, Akilu Yunusa Kaltungo, Ming Shan Ng, Tsukasa Ishizawa, Kota Fujimoto, Clara Cheung
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.05896v1)
- **发表日期**: 2026-04-07
- **匹配关键词**: exploration
- **arXiv**: [2604.05896v1](http://arxiv.org/abs/2604.05896v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 随着机器人在共享安全关键环境中日益普及，仅确保安全行为已不再足够——机器人还必须使其安全决策对人类协作者具有可理解性。在人机协作（HRC）场景中，诸如停止或切换模式等行为通常由内部安全约束触发，而这些约束对现场工作人员往往是不透明的。本文提出一种基于对话的交互式安全决策解释框架，该方法将解释过程与基于约束的安全评估紧密结合，使对话建立在与行为选择机制相同的状态和约束表征基础上。解释直接源自记录在案的决策轨迹，使用户能够就安全干预措施提出因果性（"为什么？"）、对比性（"为什么不？"）及反事实（"如果…会怎样？"）三类质询。反事实推理在固定且经过认证的安全参数范围内进行有界评估，确保交互式探索不会削弱操作安全保障。我们将该框架应用于建筑机器人场景，并通过结构化操作轨迹展示具备约束感知的对话如何阐明安全干预机制并支持协同任务恢复。通过将解释视为安全控制的操作接口，本研究为HRC领域交互式安全感知自主系统的设计提供了新的视角。

---

### 4. Hazard Management in Robot-Assisted Mammography Support

- **作者**: Ioannis Stefanakos, Roisin Bradley, Radu Calinescu, Beverley Townsend, Tianyuan Wang, Jihong Zhu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.05749v1)
- **发表日期**: 2026-04-07
- **匹配关键词**: human-robot interaction
- **arXiv**: [2604.05749v1](http://arxiv.org/abs/2604.05749v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 机器人与具身人工智能系统有望提升临床环境中的可及性与护理质量，但其在与脆弱患者近距离接触场景中的部署也带来了显著的安全风险。本文针对辅助乳腺X光检查的机器人系统MammoBot提出了一套危险管理方法。为确保从早期开发阶段就保障安全性，我们结合利益相关者引导的过程建模、软件危害分析与设计解决方案（SHARD）以及系统理论过程分析（STPA）方法。通过与临床医生、机器人专家及患者代表协作，我们共同定义了机器人辅助工作流程，以捕捉关键的人机交互环节。SHARD用于识别技术和程序偏差，而STPA则用于分析用户交互中产生的不安全控制行为。研究结果表明，许多危险并非源于组件故障，而是由时序错配、操作过早及系统状态误判所引发。这些危险被转化为精细化及补充性的安全要求，用以约束系统行为，降低仅依赖准确人工时序或单一判断的风险。本研究展示了一种结构化且可追溯的安全驱动设计方法，对临床环境中的辅助机器人系统具有潜在适用价值。

---

### 5. CoEnv: Driving Embodied Multi-Agent Collaboration via Compositional Environment

- **作者**: Li Kang, Yutao Fan, Rui Li, Heng Zhou, Yiran Qin, Zhemeng Zhang, Songtao Huang, Xiufeng Song, Zaibin Zhang, Bruno N. Y. Chen, Zhenfei Yin, Dongzhan Zhou, Wangmeng Zuo, Lei Bai
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.05484v1)
- **发表日期**: 2026-04-07
- **匹配关键词**: exploration
- **arXiv**: [2604.05484v1](http://arxiv.org/abs/2604.05484v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 多智能体具身系统在复杂协作操作方面展现出巨大潜力，但面临空间协调、时序推理与共享工作空间感知等关键挑战。受人类认知规划与物理执行分离的协作模式启发，我们提出组合环境概念——通过虚实融合构建协同系统，使多机器人智能体能在统一决策空间中感知意图并协同作业。基于此概念，我们提出CoEnv框架，该框架利用仿真环境进行安全策略探索，同时确保在现实世界中的可靠部署。CoEnv通过三阶段实现：虚实映射的场景重建将物理工作空间数字化，视觉语言模型驱动的动作合成支持基于高级接口的实时规划与代码化轨迹生成的迭代规划，以及通过碰撞检测验证的虚实迁移确保安全部署。在具有挑战性的多机械臂操作基准测试中，大量实验证明CoEnv能实现高任务成功率和执行效率，为多智能体具身人工智能建立了新范式。

---

### 6. Synergizing Efficiency and Reliability for Continuous Mobile Manipulation

- **作者**: Chengkai Wu, Ruilin Wang, Yixin Zeng, Jiayuan Wang, Mingjie Zhang, Guiyong Zheng, Qun Niu, Juepeng Zheng, Jun Ma, Boyu Zhou
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.05430v1)
- **发表日期**: 2026-04-07
- **匹配关键词**: mobile manipulation
- **arXiv**: [2604.05430v1](http://arxiv.org/abs/2604.05430v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: CODE
- **中文摘要**: 人类能够无缝融合前瞻性规划与即时反馈，在执行连续移动操作任务时无需停顿，同时实现高效率与高可靠性。在机器人中复现这种流畅可靠的行为仍面临根本性挑战，这不仅源于长时程规划与实时响应之间的冲突，更因为过度追求效率会损害不确定环境下的可靠性：它会削弱感知稳定性与补偿潜力，同时增加意外接触的风险。本研究提出一个融合效率与可靠性的统一框架，用于实现连续移动操作。该框架的核心是可靠性感知轨迹规划器，它将可靠执行的关键要素嵌入时空优化过程，生成高效且具备可靠性潜力的全局轨迹。该规划器与相位依赖型切换控制器协同工作，能够在追求效率的全局轨迹跟踪和保障可靠性的任务误差补偿之间实现无缝切换。我们还研究了一种分层初始化策略，以应对长时程规划问题的复杂性，实现在线重规划。真实环境实验表明，该方法能够在不确定条件下（如动态干扰、感知与控制误差）高效可靠地完成连续任务。此外，该框架可泛化至具有不同末端执行器约束的任务场景。与现有先进基线方法相比，本方法在保持最高效率的同时，将任务成功率提升了26.67\%--81.67\%。全面的消融实验进一步验证了各模块的有效性。源代码将予以公开。

---

### 7. AnyUser: Translating Sketched User Intent into Domestic Robots

- **作者**: Songyuan Yang, Huibin Tan, Kailun Yang, Wenjing Yang, Shaowu Yang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.04811v1)
- **发表日期**: 2026-04-06
- **匹配关键词**: mobile manipulator
- **arXiv**: [2604.04811v1](http://arxiv.org/abs/2604.04811v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 我们推出AnyUser系统，这是一种统一的机器人指令系统，可通过在相机图像上进行自由手绘草图（可选结合语言）实现直观的家庭任务指令。AnyUser将多模态输入（草图、视觉、语言）解析为空间语义基元，无需依赖先验地图或模型即可生成可执行的机器人动作。其创新组件包括用于理解的多模态融合模块和用于鲁棒动作生成的层次化策略模块。系统效能通过广泛评估得以验证：（1）在大规模数据集上的定量基准测试表明，该系统在多种模拟家庭场景中能高精度解析多样化的草图指令；（2）在两个不同机器人平台上的真实世界验证——静态安装的7自由度辅助机械臂（KUKA LBR iiwa）和双臂移动操作器（Realman RMC-AIDAL），成功执行了目标擦拭和区域清洁等代表性任务，证实了系统在物理环境中可靠解析并执行指令的能力；（3）涵盖多元人群（老年人、模拟非语言使用者、低技术素养者）的综合用户研究表明，系统在可用性和任务指定效率方面显著提升，实现了高任务完成率（85.7%-96.4%）和用户满意度。AnyUser弥合了先进机器人能力与非专业用户可及性交互需求之间的鸿沟，为适应现实人类环境的实用辅助机器人奠定了技术基础。

---

