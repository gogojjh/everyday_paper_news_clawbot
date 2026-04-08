# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-04-08 08:05

**今日新增**: 11 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 3/11 篇提供

**🌟 Highlight**: 6 篇 | **📌 Poster**: 5 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. E-VLA: Event-Augmented Vision-Language-Action Model for Dark and Blurred Scenes

- **作者**: Jiajun Zhai, Hao Shi, Shangwei Guo, Kailun Yang, Kaiwei Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.04834v1)
- **发表日期**: 2026-04-06
- **匹配关键词**: VLA, vision-language-action model, perception-action, vision-language-action
- **arXiv**: [2604.04834v1](http://arxiv.org/abs/2604.04834v1)
- **📥 PDF**: 已下载至本地 (`2604.04834v1_E-VLA_Event-Augmented_Vision-Language-Action_Model_for_Dark_and_Blurred_Scenes.pdf`)
- **🔓 开源**: GITHUB, CODE
  - 链接：https://github.com/JJayzee/E-VLA.
- **中文摘要**: 机器人视觉-语言-动作（VLA）模型在开放式操作任务中展现出良好的泛化能力，但其感知系统在极端低光、运动模糊和黑场裁剪等传感退化条件下表现脆弱。本文提出E-VLA——一种事件增强型VLA框架，能够在传统帧式视觉不可靠时提升操作鲁棒性。该方法不依赖事件流重建图像，而是直接利用事件流中的运动与结构线索，在恶劣条件下保持语义感知及感知-动作一致性。我们搭建了配备DAVIS346事件相机的开源遥操作平台，采集了涵盖多任务与多光照条件的真实世界同步RGB-事件-动作操作数据集。同时提出轻量化、与预训练模型兼容的事件集成策略，并研究了事件窗口化与融合技术以实现稳定部署。实验表明，即使是简单的无参数融合（如在RGB图像上叠加累积事件图），也能显著提升黑暗与强模糊场景下的鲁棒性：在20勒克斯光照的抓放任务中，成功率从纯图像的0%提升至叠加融合的60%，采用事件适配器后可达90%；在严重运动模糊（1000毫秒曝光）条件下，抓放任务成功率从0%提升至20-25%，分类任务从5%提升至32.5%。总体而言，E-VLA系统性地证明了事件驱动感知能有效融入VLA模型，为超越传统帧式成像的鲁棒具身智能指明了方向。代码与数据集发布于https://github.com/JJayzee/E-VLA。

---

### 2. ROSClaw: A Hierarchical Semantic-Physical Framework for Heterogeneous Multi-Agent Collaboration

- **作者**: Rongfeng Zhao, Xuanhao Zhang, Zhaochen Guo, Xiang Shao, Zhongpan Zhu, Bin He, Jie Chen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.04664v1)
- **发表日期**: 2026-04-06
- **匹配关键词**: VLA, vision-language-action, navigation, VLN
- **arXiv**: [2604.04664v1](http://arxiv.org/abs/2604.04664v1)
- **📥 PDF**: 已下载至本地 (`2604.04664v1_ROSClaw_A_Hierarchical_Semantic-Physical_Framework_for_Heterogeneous_Multi-Agent_Collaboration.pdf`)
- **🔓 开源**: PROJECT_PAGE
- **中文摘要**: 大型语言模型（LLMs）与具身智能体的融合提升了高层推理能力，但在语义理解与物理执行之间仍存在关键断层。尽管视觉-语言-动作（VLA）与视觉-语言-导航（VLN）系统使机器人能够根据自然语言指令执行操作与导航任务，它们在处理长时程序列化及时间结构化任务时仍面临挑战。现有框架通常采用模块化流程进行数据收集、技能训练与策略部署，导致实验验证与策略优化的成本高昂。为突破这些局限，我们提出ROSClaw——一个面向异构机器人的智能体框架，将策略学习与任务执行整合于统一的视觉-语言模型（VLM）控制器中。该框架利用异构机器人的e-URDF表征作为物理约束，构建仿真到现实的拓扑映射，实现对仿真环境与真实世界智能体物理状态的实时访问。我们进一步引入数据收集与状态积累机制，在真实执行过程中持续存储机器人状态、多模态观测与执行轨迹，为后续迭代式策略优化提供支持。在部署阶段，统一智能体维持推理与执行间的语义连续性，并动态分配任务专属控制权至不同智能体，从而提升多策略执行的鲁棒性。通过建立自主闭环框架，ROSClaw最大程度降低了对机器人专属开发流程的依赖。该框架支持硬件级验证、自动化生成SDK级控制程序及基于工具的执行，实现了机器人技能的快速跨平台迁移与持续进化。项目主页：https://www.rosclaw.io/。

---

### 3. Veo-Act: How Far Can Frontier Video Models Advance Generalizable Robot Manipulation?

- **作者**: Zhongru Zhang, Chenghan Yang, Qingzhou Lu, Yanjiang Guo, Jianke Zhang, Yucheng Hu, Jianyu Chen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.04502v1)
- **发表日期**: 2026-04-06
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2604.04502v1](http://arxiv.org/abs/2604.04502v1)
- **📥 PDF**: 已下载至本地 (`2604.04502v1_Veo-Act_How_Far_Can_Frontier_Video_Models_Advance_Generalizable_Robot_Manipulation?.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视频生成模型发展迅速，已开始展现出对物理动力学的深刻理解。本文探讨了如Veo-3这类先进视频生成模型在多大程度上能支持可泛化的机器人操作。我们首先研究了一种零样本方法：Veo-3根据当前机器人观测预测未来图像序列，同时逆动力学模型IDM还原对应的机器人动作。IDM仅通过随机交互数据进行训练，无需人工监督或专家示范。其核心思路在于，若视频模型能在图像空间生成物理合理的未来运动轨迹，IDM即可将这些视觉轨迹转化为可执行的机器人动作。我们在仿真环境与真实世界中，使用高自由度灵巧手对"Veo-3+IDM"方案进行评估。研究发现，得益于前沿视频模型的强大泛化能力，Veo-3+IDM能持续生成基本正确的任务级轨迹，但其底层控制精度仍不足以可靠完成多数任务。基于此发现，我们开发了分层框架Veo-Act：以Veo-3作为高层运动规划器，视觉语言动作策略作为底层执行器，显著提升了当前最优视觉语言动作策略的指令跟随性能。总体而言，研究结果表明随着视频生成模型的持续进步，视频模型有望成为可泛化机器人学习的重要组件。

---

### 4. GA-GS: Generation-Assisted Gaussian Splatting for Static Scene Reconstruction

- **作者**: Yedong Shen, Shiqi Zhang, Sha Zhang, Yifan Duan, Xinran Zhang, Wenhao Yu, Lu Zhang, Jiajun Deng, Yanyong Zhang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.04331v1)
- **发表日期**: 2026-04-06
- **匹配关键词**: gaussian splatting
- **arXiv**: [2604.04331v1](http://arxiv.org/abs/2604.04331v1)
- **📥 PDF**: 已下载至本地 (`2604.04331v1_GA-GS_Generation-Assisted_Gaussian_Splatting_for_Static_Scene_Reconstruction.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 从单目视频中重建包含动态物体的静态三维场景，对于虚拟现实和自动驾驶等众多应用具有重要意义。现有方法通常依赖背景进行静态场景重建，限制了恢复被动态物体遮挡区域的能力。本文提出GA-GS——一种生成辅助的高斯溅射静态场景重建方法。本研究的核心创新在于利用生成技术辅助重建被遮挡区域：我们采用运动感知模块分割并移除动态区域，随后运用扩散模型对遮挡区域进行修复，提供伪真实值监督。为平衡真实背景与生成区域的贡献，我们为每个高斯基元引入可学习的真实性标量，该标量能在溅射过程中动态调节不透明度，实现真实性感知的渲染与监督。由于现有数据集均未提供含动态物体视频的静态场景真实值，我们构建了名为Trajectory-Match的数据集，通过固定路径机器人记录每个场景在有/无动态物体时的状态，从而实现对遮挡区域重建的定量评估。在DAVIS数据集及自建数据集上的大量实验表明，GA-GS在静态场景重建方面达到最先进性能，尤其在大规模持续遮挡的挑战性场景中表现突出。

---

### 5. Adaptive Action Chunking at Inference-time for Vision-Language-Action Models

- **作者**: Yuanchang Liang, Xiaobo Wang, Kai Wang, Shuo Wang, Xiaojiang Peng, Haoyu Chen, David Kim Huat Chua, Prahlad Vadakkepat
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.04161v1)
- **发表日期**: 2026-04-05
- **匹配关键词**: VLA, vision-language-action model, vision-language-action
- **arXiv**: [2604.04161v1](http://arxiv.org/abs/2604.04161v1)
- **📥 PDF**: 已下载至本地 (`2604.04161v1_Adaptive_Action_Chunking_at_Inference-time_for_Vision-Language-Action_Models.pdf`)
- **🔓 开源**: CODE
  - 链接：https://lance-lot.github.io/adaptive-chunking.github.io/.
- **中文摘要**: 在视觉-语言-动作（VLA）模型中，动作分块（即无需中间重新规划即可执行一系列动作）是提升机器人操作能力的关键技术。然而，过大的分块尺寸会降低模型对新信息的响应能力，而过小的分块则会增加模式跳跃的风险——即因分块间不连续导致的动作突变问题。因此，如何选择最优分块尺寸以平衡模型的反应性与连贯性成为迫切需求。遗憾的是，当前VLA模型普遍采用经验性固定分块长度的推理方式，这限制了其在不同操作任务中的优越性与可扩展性。为解决这一问题，我们提出了一种新颖的自适应动作分块（AAC）策略，该策略利用动作熵作为线索，根据当前预测动态调整分块尺寸。通过在大量模拟与真实机器人操作任务上的实验验证，本方法显著超越了现有最优方案的性能表现。演示视频与源代码已公开于https://lance-lot.github.io/adaptive-chunking.github.io/。

---

### 6. VLA-Forget: Vision-Language-Action Unlearning for Embodied Foundation Models

- **作者**: Ravi Ranjan, Agoritsa Polyzou
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.03956v1)
- **发表日期**: 2026-04-05
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2604.03956v1](http://arxiv.org/abs/2604.03956v1)
- **📥 PDF**: 已下载至本地 (`2604.03956v1_VLA-Forget_Vision-Language-Action_Unlearning_for_Embodied_Foundation_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型正逐渐成为机器人操作领域的具身基础模型，但其部署带来了新的遗忘挑战：如何在消除不安全、虚假或隐私敏感行为的同时，不损害感知能力、语言理解与动作控制。在OpenVLA类策略中，行为通过融合视觉编码器、跨模态投影器和预测分词化机器人动作的语言主干网络生成，因此不良知识可能分散在感知层、对齐层及推理/动作层中，而非局限于单一模块。这导致仅针对视觉模块或语言主干的部分遗忘往往效果不足，而传统针对独立视觉或语言模型设计的遗忘基线方法在具身场景中可能残留遗忘痕迹或造成不必要的性能损失。我们提出VLA-Forget混合遗忘框架，该框架结合了面向感知与跨模态特性的比例感知选择性编辑技术，以及面向推理/动作层的选择性分层遗忘机制，实现效用保持的精准遗忘。VLA-Forget通过分阶段更新视觉编码器、投影器及上层动作生成Transformer模块，联合优化三大目标：定向遗忘、感知保持与推理保留。在遗忘集行为探测与保留任务评估中，相较于强遗忘基线方法，VLA-Forget将遗忘效能提升10%，感知特异性保持率提高22%，推理与任务成功率保留度增加9%，并将量化后行为恢复率降低55%。

---

## 📌 Poster

*其他相关研究*

---

### 1. AnyUser: Translating Sketched User Intent into Domestic Robots

- **作者**: Songyuan Yang, Huibin Tan, Kailun Yang, Wenjing Yang, Shaowu Yang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.04811v1)
- **发表日期**: 2026-04-06
- **匹配关键词**: mobile manipulator
- **arXiv**: [2604.04811v1](http://arxiv.org/abs/2604.04811v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 我们推出AnyUser系统，这是一种统一的机器人指令系统，可通过在相机图像上进行自由手绘草图（可选结合语言）实现直观的家庭任务指令。AnyUser将多模态输入（草图、视觉、语言）解析为空间语义基元，无需依赖先验地图或模型即可生成可执行的机器人动作。其创新组件包括用于理解的多模态融合模块和用于鲁棒动作生成的层次化策略模块。系统效能通过广泛评估得以验证：（1）在大规模数据集上的定量基准测试表明，该系统在多种模拟家庭场景中能高精度解析多样化的草图指令；（2）在两个不同机器人平台上的真实世界验证——静态安装的7自由度辅助机械臂（KUKA LBR iiwa）和双臂移动操作机器人（Realman RMC-AIDAL），成功执行了目标擦拭和区域清洁等代表性任务，证实了系统在物理环境中可靠解析并执行指令的能力；（3）涵盖多元人群（老年人、模拟非语言使用者、低技术素养者）的综合用户研究表明，该系统显著提升了可用性和任务指定效率，实现了高任务完成率（85.7%-96.4%）和用户满意度。AnyUser弥合了先进机器人能力与非专业用户可及性交互需求之间的鸿沟，为适应真实人类环境的实用辅助机器人奠定了技术基础。

---

### 2. FORMULA: FORmation MPC with neUral barrier Learning for safety Assurance

- **作者**: Qintong Xie, Weishu Zhan, Peter Chin
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.04409v1)
- **发表日期**: 2026-04-06
- **匹配关键词**: obstacle avoidance, navigation
- **arXiv**: [2604.04409v1](http://arxiv.org/abs/2604.04409v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 多机器人系统在大规模应用中至关重要，例如灾害响应、物资运输和仓储物流，然而在杂乱和动态环境中确保鲁棒且具备安全意识的编队控制仍然是一个重大挑战。现有的模型预测控制方法在可扩展性和可证明的安全性方面存在局限，而控制屏障函数虽然具有强制执行安全性的理论优势，却难以针对大规模非线性系统进行人工设计。本文提出了FORMULA框架，这是一种安全的分布式学习增强预测控制方法，它将模型预测控制与控制李雅普诺夫函数相结合以确保稳定性，并采用基于神经网络的控制屏障函数实现去中心化的安全保障，从而无需人工设计安全约束。该方案在避障过程中保持编队完整性，解决了密集配置下的死锁问题，并降低了在线计算负担。仿真结果表明，FORMULA能够为复杂环境中的多机器人团队实现可扩展、具备安全意识且保持编队的导航。

---

### 3. Precise Robot Command Understanding Using Grammar-Constrained Large Language Models

- **作者**: Xinyun Huo, Raghav Gnanasambandam, Xinyao Zhang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.04233v1)
- **发表日期**: 2026-04-05
- **匹配关键词**: human-robot collaboration
- **arXiv**: [2604.04233v1](http://arxiv.org/abs/2604.04233v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 工业环境中的人机协作需要精确可靠的通信以提升操作效率。尽管大语言模型能够理解通用语言，但在确保工业指令安全可执行所需的领域特定严谨性方面往往存在不足。为解决这一问题，本文提出了一种新型语法约束大语言模型，将语法驱动的自然语言理解系统与微调后的大语言模型相结合，既保持了对话灵活性，又满足了机器人学所需的确定性精度。我们的方法采用两阶段处理流程：首先，经过微调的大语言模型对自然语言输入进行高层上下文推理和参数推断；其次，通过结构化语言模型和基于语法的规范化器对大语言模型输出进行约束，将其强制转换为由有效动作框架和指令元素组成的标准化符号格式。这一过程确保生成的指令有效且以机器人可读的JSON格式结构化。该模型的关键特性在于验证与反馈循环机制：语法解析器根据预定义的可执行机器人动作列表验证输出结果，若指令无效，系统将自动生成修正提示并重新调用大语言模型。这种迭代式自我修正机制使模型能够从初始解析错误中恢复，从而提升系统鲁棒性。我们将该语法约束混合模型与两种基线模型进行对比评估：基于API的微调大语言模型和独立语法驱动自然语言理解模型。通过使用人机交互语料库数据集，我们证明混合方法在指令有效性方面表现卓越，有助于实现更安全高效的工业人机协作。

---

### 4. Learning from Imperfect Demonstrations via Temporal Behavior Tree-Guided Trajectory Repair

- **作者**: Aniruddh G. Puranic, Sebastian Schirmer, John S. Baras, Calin Belta
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.04225v1)
- **发表日期**: 2026-04-05
- **匹配关键词**: navigation
- **arXiv**: [2604.04225v1](http://arxiv.org/abs/2604.04225v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 从演示中学习机器人控制策略是一种强大的范式，然而现实世界的数据往往存在次优、噪声或其他不完美问题，这为模仿学习和强化学习带来了显著挑战。本研究提出了一种基于时序行为树的形式化框架——该框架将信号时序逻辑扩展至行为树语义——用于在策略学习前修复次优轨迹。针对违反时序行为树规范的演示数据，我们采用基于模型的修复算法对轨迹片段进行校正，使其满足形式化约束，从而生成兼具逻辑一致性与可解释性的数据集。修复后的轨迹被用于提取势函数，这些函数通过塑造强化学习的奖励信号，引导智能体向符合任务要求的状态空间区域探索，且无需依赖智能体的运动学模型知识。我们在离散网格世界导航任务以及连续单智能体/多智能体抵达规避任务中验证了该框架的有效性，展示了在无法获得高质量演示场景下实现数据高效机器人学习的潜力。

---

### 5. VA-FastNavi-MARL: Real-Time Robot Control with Multimedia-Driven Meta-Reinforcement Learning

- **作者**: Yang Zhang, Shengxi Jing, Fengxiang Wang, Yuan Feng, Hong Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.03998v1)
- **发表日期**: 2026-04-05
- **匹配关键词**: human-robot interaction
- **arXiv**: [2604.03998v1](http://arxiv.org/abs/2604.03998v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 实时响应动态异构多媒体指令对于人机交互至关重要。本文提出VA-FastNavi-MARL框架，通过将异步视听输入对齐为统一潜在表征，将多样化指令视为可导航目标的分布进行元强化学习。该方法能以可忽略的推理开销快速适应未见指令，突破传统方法因繁重感官处理形成的性能瓶颈。我们的模态无关流确保了无缝低延迟控制，在多臂工作空间的验证表明，VA-FastNavi-MARL在样本效率上显著优于基线方法，即使在嘈杂多媒体流下仍能保持稳健的实时执行能力。

---

