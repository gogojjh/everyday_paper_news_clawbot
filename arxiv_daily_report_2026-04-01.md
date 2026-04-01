# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-04-01 08:05

**今日新增**: 18 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 5/18 篇提供

**🌟 Highlight**: 7 篇 | **📌 Poster**: 11 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. FocusVLA: Focused Visual Utilization for Vision-Language-Action Models

- **作者**: Yichi Zhang, Weihao Yuan, Yizhuo Zhang, Xidong Zhang, Jia Wan
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.28740v1)
- **发表日期**: 2026-03-30
- **匹配关键词**: vision-language-action, vision-language-action model, VLA
- **arXiv**: [2603.28740v1](http://arxiv.org/abs/2603.28740v1)
- **📥 PDF**: 已下载至本地 (`2603.28740v1_FocusVLA_Focused_Visual_Utilization_for_Vision-Language-Action_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型通过将策略建立在丰富的视觉-语言信息基础上，提升了动作生成的质量。然而，当前的自回归策略面临三个瓶颈：(1) 架构偏差导致模型忽视视觉细节，(2) 过多的视觉标记使注意力难以聚焦于正确区域，(3) 与任务无关的视觉信息引入大量噪声——这些因素共同严重影响了动作生成的质量。本文探讨了如何有效利用不同视觉表征进行动作生成。为此，我们首先通过实验验证了上述问题，并表明VLA性能主要受限于视觉信息的利用方式，而非视觉表征的质量。基于这些发现，我们提出了FocusVLA这一新范式，该范式引导模型关注与任务相关的视觉区域，从而有效连接视觉与动作。具体而言，我们首先提出模态级联注意力机制以消除捷径路径，迫使VLA模型依赖任务相关的视觉细节生成动作。此外，我们提出聚焦注意力机制，动态选择任务相关的视觉片段以控制信息量，同时显式调节其影响以抑制任务无关的噪声。在模拟和真实机器人基准测试上的大量实验表明，FocusVLA不仅能有效利用视觉细节执行灵巧操作，还能显著提升多种任务的性能并加速收敛。

---

### 2. Pandora: Articulated 3D Scene Graphs from Egocentric Vision

- **作者**: Alan Yu, Yun Chang, Christopher Xie, Luca Carlone ⭐
  - **高亮作者**: Luca Carlone
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.28732v1)
- **发表日期**: 2026-03-30
- **匹配关键词**: scene graph, mobile manipulation
- **arXiv**: [2603.28732v1](http://arxiv.org/abs/2603.28732v1)
- **📥 PDF**: 已下载至本地 (`2603.28732v1_Pandora_Articulated_3D_Scene_Graphs_from_Egocentric_Vision.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 机器人建图系统通常基于机器人自身的传感器和摄像头构建度量-语义场景表征。然而，这种"第一人称"地图因机器人本体结构或技能限制而存在固有缺陷，可能导致环境中的许多方面未被探索。例如，机器人可能无法打开抽屉或触及壁柜。从这种意义上说，地图表征并不完整，需要能力更强的机器人来填补空白。我们通过利用人类佩戴Project Aria眼镜自然探索场景时捕获的自我中心数据来缩小现有方法的盲区，为将人类对可动结构的认知直接迁移至任意可部署机器人提供了途径。实验证明，通过简单启发式方法，我们能够利用自我中心数据重建可动物体部件模型，其质量可与基于其他输入模态的最先进方法相媲美。我们还展示了如何将这些模型整合到三维场景图表征中，从而提升对物体动态特性和物体-容器关系的理解。最后，我们通过波士顿动力Spot机器人执行移动操作任务的应用案例，验证了这些可动三维场景图能增强机器人能力——仅以三维场景图为输入，机器人即可成功定位并取出隐藏的目标物品。

---

### 3. DRIVE-Nav: Directional Reasoning, Inspection, and Verification for Efficient Open-Vocabulary Navigation

- **作者**: Maoguo Gao, Zejun Zhu, Zhiming Sun, Zhengwei Ma, Longze Yuan, Zhongjing Ma, Zhigang Gao, Jinhui Zhang, Suli Zou
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.28691v1)
- **发表日期**: 2026-03-30
- **匹配关键词**: exploration, navigation
- **arXiv**: [2603.28691v1](http://arxiv.org/abs/2603.28691v1)
- **📥 PDF**: 已下载至本地 (`2603.28691v1_DRIVE-Nav_Directional_Reasoning,_Inspection,_and_Verification_for_Efficient_Open-Vocabulary_Navigati.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://coolmaoguo.github.io/drive-nav-page/
- **中文摘要**: 开放词汇目标导航（OVON）要求具身智能体在未知环境中定位语言指定的目标。现有零样本方法通常在局部观测下对密集边界点进行推理，导致路径选择不稳定、重复访问和冗余动作开销。我们提出DRIVE-Nav结构化框架，该框架围绕持久化方向而非原始边界组织探索。通过更完整地检查已遇到的方向，并将后续决策限制在前向240度视野范围内仍相关的方向上，DRIVE-Nav减少了重复访问并提升了路径效率。该框架从加权快速行进法（FMM）路径中提取并追踪方向候选，维护代表性视角进行语义检查，结合视觉语言引导的提示增强与跨帧验证以提高语义关联可靠性。在HM3D-OVON、HM3Dv2和MP3D数据集上的实验显示出优异的综合性能与稳定的效率提升。在HM3D-OVON任务中，DRIVE-Nav达到50.2%的成功率（SR）和32.6%的路径长度加权成功率（SPL），较先前最佳方法提升1.9% SR和5.6% SPL。该框架同时在HM3Dv2和MP3D数据集上取得最优SPL指标，并可迁移至实体人形机器人平台。实际部署验证了其有效性。项目页面：https://coolmaoguo.github.io/drive-nav-page/

---

### 4. ManipArena: Comprehensive Real-world Evaluation of Reasoning-Oriented Generalist Robot Manipulation

- **作者**: Yu Sun, Meng Cao, Ping Yang, Rongtao Xu, Yunxiao Yan, Runze Xu, Liang Ma, Roy Gan, Andy Zhai, Qingxuan Chen, Zunnan Xu, Hao Wang, Jincheng Yu, Lucy Liang, Qian Wang, Ivan Laptev, Ian D Reid, Xiaodan Liang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.28545v1)
- **发表日期**: 2026-03-30
- **匹配关键词**: vision-language-action, mobile manipulation, VLA
- **arXiv**: [2603.28545v1](http://arxiv.org/abs/2603.28545v1)
- **📥 PDF**: 已下载至本地 (`2603.28545v1_ManipArena_Comprehensive_Real-world_Evaluation_of_Reasoning-Oriented_Generalist_Robot_Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作模型与世界模型作为通用机器人智能的新兴范式展现出巨大潜力，但其发展受限于缺乏反映真实场景部署的可靠评估体系。现有基准测试大多以仿真环境为核心，虽具备可控性优势，却难以捕捉由感知噪声、复杂接触动力学、硬件限制及系统延迟造成的现实鸿沟。此外，分散在不同机器人平台上的现实世界评估导致公平性与可复现性不足。为应对这些挑战，我们推出ManipArena标准化评估框架，旨在构建仿真与真实执行的桥梁。该框架包含20类多样化任务与10,812条专家轨迹数据，重点关注需要语义与空间推理的认知型操作任务，通过受控分布外设置支持多层级泛化能力评估，并突破桌面场景局限纳入长时程移动操作。框架进一步提供丰富的传感诊断功能（包括底层运动信号），以及通过高质量三维扫描构建的同步虚实环境。这些特性共同为视觉-语言-动作模型与世界模型方法提供了公平、真实、可复现的评估体系，为具身智能系统的诊断与演进奠定了可扩展的基础。

---

### 5. Tele-Catch: Adaptive Teleoperation for Dexterous Dynamic 3D Object Catching

- **作者**: Weiguang Zhao, Junting Dong, Rui Zhang, Kailin Li, Qin Zhao, Kaizhu Huang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.28427v1)
- **发表日期**: 2026-03-30
- **匹配关键词**: diffusion policy
- **arXiv**: [2603.28427v1](http://arxiv.org/abs/2603.28427v1)
- **📥 PDF**: 已下载至本地 (`2603.28427v1_Tele-Catch_Adaptive_Teleoperation_for_Dexterous_Dynamic_3D_Object_Catching.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 遥操作是将人类灵巧性转移至机器人的关键范式，然而现有研究多聚焦于初始静止的物体操作，如抓取或操控任务。动态物体捕捉——即物体在接触前处于运动状态的情形——仍缺乏深入探索。在此类任务中，纯遥操作常因时机、位姿与施力误差而失败，凸显了需要将人类指令与自主策略相结合的共享控制机制。为此，我们提出Tele-Catch——一个面向动态物体捕捉的灵巧手遥操作系统框架。其核心是DAIM机制，该动态感知自适应融合机制通过将基于数据手套的遥操作信号融入扩散策略去噪过程，实现了人机协同的共享控制，并能依据交互物体的运动状态自适应调节控制参数。为提升策略鲁棒性，我们提出DP-U3R方法，将点云观测中的无监督几何表征融入扩散策略学习，实现几何感知的决策过程。大量实验表明，Tele-Catch在动态捕捉任务中显著提升了操作精度与鲁棒性，同时在不同构型灵巧手及未见物体类别上均展现出稳定的性能增益。

---

### 6. Learning Multi-View Spatial Reasoning from Cross-View Relations

- **作者**: Suchae Jeong, Jaehwi Song, Haeone Lee, Hanna Kim, Jian Kim, Dongjun Lee, Dong Kyu Shin, Changyeon Kim, Dongyoon Hahm, Woogyeol Jin, Juheon Choi, Kimin Lee
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.27967v1)
- **发表日期**: 2026-03-30
- **匹配关键词**: vision-language-action, vision-language-action model
- **arXiv**: [2603.27967v1](http://arxiv.org/abs/2603.27967v1)
- **📥 PDF**: 已下载至本地 (`2603.27967v1_Learning_Multi-View_Spatial_Reasoning_from_Cross-View_Relations.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉语言模型（VLM）在单视角视觉任务上已取得显著成果，但其多视角空间推理能力仍显不足，而这项能力对于具身人工智能系统理解三维环境及跨视角操作物体至关重要。本研究提出跨视角关系数据集（XVR），这是一个专为培养视觉语言模型多视角空间推理能力而构建的大规模数据集。XVR包含源自1.8万个多样化三维场景和7万条机器人操作轨迹的10万个视觉-问题-答案样本，涵盖三大基础空间推理任务：对应关系识别（跨视角物体匹配）、关系验证（空间关系确认）和位置定位（物体坐标识别）。基于XVR微调的视觉语言模型在成熟的多视角与机器人空间推理基准测试（MindCube和RoboSpatial）中取得显著提升。当XVR训练获得的表征作为视觉-语言-动作模型的核心架构时，在RoboCasa平台上的任务成功率得到明显改善。研究结果表明，针对跨视角空间关系的显式训练能显著增强多视角推理能力，并能有效迁移至真实世界的机器人操作任务中。

---

### 7. ProgressVLA: Progress-Guided Diffusion Policy for Vision-Language Robotic Manipulation

- **作者**: Hongyu Yan, Qiwei Li, Jiaolong Yang, Yadong Mu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.27670v1)
- **发表日期**: 2026-03-29
- **匹配关键词**: vision-language-action, diffusion policy, VLA
- **arXiv**: [2603.27670v1](http://arxiv.org/abs/2603.27670v1)
- **📥 PDF**: 已下载至本地 (`2603.27670v1_ProgressVLA_Progress-Guided_Diffusion_Policy_for_Vision-Language_Robotic_Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 现有的大多数用于机器人操作的视觉-语言-动作模型缺乏任务进度感知能力，通常依赖手工设计的启发式规则来判定任务终止。这一局限在涉及级联子目标的长周期任务中尤为突出。本研究聚焦于任务进度的估计与集成，提出了一种名为{\textbf \vla}的新型模型。我们的技术贡献主要体现在两个方面：(1) \emph{鲁棒的进度估计}：我们在大规模无监督视频-文本机器人数据集上预训练了一个进度估计器。该估计器在仿真环境中实现了较低的预测残差（在$[0, 1]$量程上为0.07），并展现出对未见真实世界样本的零样本泛化能力；(2) \emph{可微分的进度引导}：我们引入了一个逆向动力学世界模型，将预测的动作标记映射为未来潜在视觉状态。这些潜在状态随后由进度估计器处理；通过应用最大进度正则化，我们构建了一个可微分流程，为动作标记的优化提供进度引导。在CALVIN和LIBERO基准测试中的大量实验，结合真实世界机器人部署，一致表明我们的方法在成功率和泛化能力方面较现有强基线模型均有显著提升。

---

## 📌 Poster

*其他相关研究*

---

### 1. Serialized Red-Green-Gray: Quicker Heuristic Validation of Edges in Dynamic Roadmap Graphs

- **作者**: Yulie Arad, Stav Ashur, Marta Markowicz, James D. Motes, Marco Morales, Nancy M. Amato
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.28674v1)
- **发表日期**: 2026-03-30
- **匹配关键词**: motion planning
- **arXiv**: [2603.28674v1](http://arxiv.org/abs/2603.28674v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 在动态环境（如机器人仓库）中进行运动规划时，需要快速适应障碍物姿态的频繁变化。传统的基于路线图的方法在此类场景中面临挑战，它们要么依赖低效的路线图重建，要么需要通过昂贵的碰撞检测来更新现有路线图。为解决这些问题，我们提出了红-绿-灰（RGG）框架，该方法基于SPITE算法，通过保守几何近似将路线图边快速分类为无效（红）、有效（绿）或不确定（灰）。序列化RGG通过批量序列化和向量化实现了高性能变体，支持高效的GPU加速。实验结果表明，虽然RGG有效减少了需要完全验证的未知边数量，但SerRGG相比顺序执行实现了2-9倍的加速。这种几何精度与计算速度的结合，使得SerRGG在时间敏感的机器人应用中具有显著优势。

---

### 2. EBuddy: a workflow orchestrator for industrial human-machine collaboration

- **作者**: Michele Banfi, Rocco Felici, Stefano Baraldo, Oliver Avram, Anna Valente
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.28579v1)
- **发表日期**: 2026-03-30
- **匹配关键词**: human-robot collaboration, collaborative robot
- **arXiv**: [2603.28579v1](http://arxiv.org/abs/2603.28579v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 本文介绍EBuddy——一种面向工业环境中自然人机协作的语音引导工作流协调系统。该系统针对工具密集型工作流中的常见瓶颈：专家经验虽有效但难以规模化推广，且当操作流程在不同人员和作业周期中临时重构时，执行质量会下降。EBuddy将专家实践转化为有限状态机驱动的应用程序，在运行时提供可解释的决策框架（当前状态与允许操作），使语音请求能在状态约束下被解析，同时系统执行并监控相应的工具交互。通过模块化工作流组件，EBuddy协调包括图形界面软件和协作机器人在内的异构资源，借助自动语音识别与意图理解实现全语音交互。在基于人机协作的定向能量沉积叶轮叶片检测与修复准备工业试点中，该系统在人员培训、三维扫描处理及修复程序生成等全流程环节显著缩短作业时长，同时保持操作可重复性并降低人员工作负荷。

---

### 3. A Foldable and Agile Soft Electromagnetic Robot for Multimodal Navigation in Confined and Unstructured Environments

- **作者**: Zhihao Lv, Xiaoyong Zhang, Mengfan Zhang, Xiaoyu Song, Xingyue Liu, Yide Liu, Shaoxing Qu, Guoyong Mao
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.28362v1)
- **发表日期**: 2026-03-30
- **匹配关键词**: navigation
- **arXiv**: [2603.28362v1](http://arxiv.org/abs/2603.28362v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 多模态运动对动物在非结构化野生环境中的适应性至关重要。同样，在具有粘弹性黏液、复杂皱襞以及贲门等狭窄括约肌特征的人类胃肠道中，多模态运动对于小型软体机器人执行任务也极为关键。本文介绍了一种专为此类场景设计的小型紧凑、可折叠且坚固的软体电磁机器人（M-SEMR），该机器人具备九种以上的运动模式。M-SEMR采用嵌入液态金属通道的六辐弹性体结构，在静磁场中通过拉普拉斯力驱动，能够在不同运动模式间实现快速切换（<0.35秒）。它展现出卓越的敏捷性，包括高速滚动（818毫米/秒，26体长/秒）、全向爬行、跳跃和游泳。值得注意的是，该机器人可通过折叠将体积缩小79%，从而穿越狭窄空间。我们进一步验证了其在复杂地形上的导航能力，包括离散障碍物、粘弹性明胶表面、粘性流体及模拟生物组织。该系统为开发面向未来生物医学应用的高机动性软体机器人提供了一种通用策略。

---

### 4. Users and Wizards in Conversations: How WoZ Interface Choices Define Human-Robot Interactions

- **作者**: Ekaterina Torubarova, Jura Miniota, Andre Pereira
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.28338v1)
- **发表日期**: 2026-03-30
- **匹配关键词**: human-robot interaction
- **arXiv**: [2603.28338v1](http://arxiv.org/abs/2603.28338v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 本文从用户与操作者双重视角，探讨了不同"绿野仙踪"（WoZ）交互界面对人机沟通的影响。我们在对话场景中测试了三种具有不同对话输入输出限制层级的WoZ界面：a)受限感知图形界面，呈现固定视角视频与语音识别文本，操作者可触发预设语句及动作；b)无限制感知图形界面，在基础上增加参与者与机器人的实时音频传输；c)VR远程呈现界面，为操作者提供沉浸式立体音视频流，并将其自发语音、视线及面部表情实时映射至机器人。研究发现，用户对VR界面中介的交互在机器人特性感知与社会临场感方面评价最高；对操作者而言，VR模式虽最具挑战性，却能建立更强的用户社交联结。在对话间隙与重叠度指标上，VR界面促成了最紧密的互动衔接，而受限图形界面则产生最疏离的交流流与最长静默间隔。基于以上发现，我们主张在WoZ研究中更多采用远程呈现界面，这类研究不仅能更准确地映射未来机器人发展方向，也为基于自然情境化多模态行为数据的自动化研究提供了可行路径。

---

### 5. Point of View: How Perspective Affects Perceived Robot Sociability

- **作者**: Subham Agrawal, Aftab Akthar, Nils Dengler, Maren Bennewitz
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.28272v1)
- **发表日期**: 2026-03-30
- **匹配关键词**: robot navigation, human-robot interaction, navigation
- **arXiv**: [2603.28272v1](http://arxiv.org/abs/2603.28272v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 确保机器人导航的安全性和社会可接受性对于共享环境中舒适的人机交互至关重要。然而，现有的验证方法通常依赖于鸟瞰（他者中心）视角，这未能捕捉到行人在现实世界中遇到机器人时的主观第一人称体验。本文通过研究不同视角如何影响人们对机器人轨迹的社会性和干扰感知，探讨了他者中心验证与自我中心体验之间的感知差异。我们采用沉浸式虚拟现实环境，在用户研究中评估同一机器人轨迹在他者中心视角、自我中心近距视角和自我中心远距视角下的表现。我们对两种不同导航策略生成的轨迹进行分析，以探究观察到的差异是特定于单一轨迹类型，还是具有更广泛的普适性。此外，我们还研究了通过增加点头等社交手势是否能弥合感知差异并提升人类的舒适度。实验表明，从他者中心视角评价为具有社会性的轨迹，在近距离第一人称体验中可能被感知为显著更具干扰性。研究结果还表明，虽然通过距离会影响感知干扰程度，但诸如点头等交流性社交信号能有效提升机器人行为的感知社会性。

---

### 6. osmAG-Nav: A Hierarchical Semantic Topometric Navigation Stack for Robust Lifelong Indoor Autonomy

- **作者**: Yongqi Zhang, Jiajie Zhang, Chengqian Li, Fujing Xie, Sören Schwertfeger
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.28271v1)
- **发表日期**: 2026-03-30
- **匹配关键词**: navigation
- **arXiv**: [2603.28271v1](http://arxiv.org/abs/2603.28271v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: CODE
- **中文摘要**: 在大规模、多楼层环境中部署移动机器人，需要导航系统在实现空间可扩展性的同时不牺牲局部运动精度。传统导航系统依赖单一占据栅格地图，在存储效率、跨楼层推理和长距离规划方面面临严重瓶颈。为解决这些限制，本文提出osmAG-Nav——一个基于分层语义拓扑度量OpenStreetMap区域图（osmAG）地图标准的完整开源ROS2导航系统。该系统采用"系统之系统"架构，将全局拓扑推理与局部度量执行解耦。分层osmAG规划器以通道中心图上的LCA锚定流程替代密集栅格搜索，其边权值源自局部栅格可通行性而非欧氏距离，实现了校园级长路径的毫秒级规划。滚动窗口机制在机器人周围栅格化固定尺寸的局部度量网格，使局部代价地图内存占用与总建图面积无关；分段执行策略则将中间目标分发给标准ROS2控制器以实现平滑交接。系统鲁棒性通过结构感知的LiDAR定位框架增强，该框架依据永久建筑先验信息过滤动态干扰。在真实世界多层室内外校园环境（>11,025平方米）的广泛实验中表明：在同楼层基准子集上，osmAG-Nav在长路径上的规划延迟比基于栅格的基线方法降低达7816倍，同时保持较低路径长度开销与终身定位稳定性。单楼层远程机器人任务进一步验证了集成系统的可靠性。完整系统以模块化ROS2生命周期节点形式发布。

---

### 7. A Position Statement on Endovascular Models and Effectiveness Metrics for Mechanical Thrombectomy Navigation, on behalf of the Stakeholder Taskforce for AI-assisted Robotic Thrombectomy (START)

- **作者**: Harry Robertshaw, Anna Barnes, Phil Blakelock, Raphael Blanc, Robert Crossley, Rebecca Fahrig, Ameer E. Hassan, Benjamin Jackson, Lennart Karstensen, Neelam Kaur, Markus Kowarschik, Jeremy Lynch, Franziska Mathis-Ullrich, Dwight Meglan, Vitor Mendes Pereira, Mouloud Ourak, Matteo Pantano, S. M. Hadi Sadati, Alice Taylor-Gee, Tom Vercauteren, Phil White, Alejandro Granados, Thomas C. Booth
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.28129v1)
- **发表日期**: 2026-03-30
- **匹配关键词**: navigation
- **arXiv**: [2603.28129v1](http://arxiv.org/abs/2603.28129v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 在传染病和癌症治疗不断取得进展的同时，中风患病率的上升将成为21世纪中叶医学面临的主要挑战之一。大血管闭塞尤其具有致残性，但由于地理因素限制，有效治疗（需在数小时内实施以获得最佳疗效）仍十分有限。为改善不同地域人群及时接受机械取栓治疗的机会，部署机器人手术系统是一种解决方案。人工智能辅助技术有望提升操作者在这一新兴治疗方式中的技能水平。本研究旨在建立人工智能辅助取栓机器人开发与验证的共识框架，目标包括制定标准化疗效评估指标，并定义涵盖计算机模拟、体外、离体及活体环境的基准测试平台。为此，我们汇集了神经介入、机器人技术、数据科学、卫生经济学、政策研究、统计学及患者权益倡导等领域的专家，通过创新研讨会、德尔菲法和最终立场声明达成共识。研究确认四类基础测试平台各具验证功能：简单测试平台需包含适配导丝导管操作的真实血管解剖结构，标准测试平台应纳入可变形血管模型，高级测试平台则需整合血流动力学、脉动特征及病理特性。疗效评估指标分为两大类别：针对计算机模拟、体外和离体阶段的技术导航指标，以及针对活体阶段的临床结局指标。患者安全是该技术发展的核心，当前亟需建立体外测量数据与活体并发症的关联性验证体系。

---

### 8. CARLA-Air: Fly Drones Inside a CARLA World -- A Unified Infrastructure for Air-Ground Embodied Intelligence

- **作者**: Tianle Zeng, Hanxuan Chen, Yanci Wen, Hong Zhang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.28032v1)
- **发表日期**: 2026-03-30
- **匹配关键词**: navigation
- **arXiv**: [2603.28032v1](http://arxiv.org/abs/2603.28032v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: CODE, GITHUB
  - 链接：https://github.com/louiszengCN/CarlaAir
- **中文摘要**: 低空经济、具身智能与空地协同系统的融合发展，对能够在统一物理连贯环境中联合建模空中与地面智能体的仿真基础设施提出了日益增长的需求。现有开源平台仍存在领域割裂问题：驾驶仿真器缺乏空中动力学模型，而多旋翼仿真器则缺少真实地面场景。基于桥接的联合仿真会引入同步开销，且无法保证严格的时空一致性。

我们推出CARLA-Air开源基础设施，在单一虚幻引擎进程中实现了高保真城市驾驶与物理精确的多旋翼飞行的统一。该平台完整保留了CARLA和AirSim原生的Python API及ROS 2接口，支持零修改代码复用。通过共享物理时钟与渲染管线，CARLA-Air提供具备规则遵从交通流、社会意识行人模型及空气动力学一致无人机动态的逼真环境，每时钟周期可同步采集全平台多达18种传感器模态数据。平台支持具有代表性的空地具身智能任务，涵盖协同作业、具身导航与视觉语言动作、多模态感知与数据集构建，以及基于强化学习的策略训练。可扩展的资源管线支持将定制机器人平台集成至共享世界。通过继承AirSim（其上游开发已归档）的空中能力，CARLA-Air确保这一广泛应用的飞行技术栈能在现代基础设施中持续演进。

平台已发布预编译二进制文件与完整源代码：https://github.com/louiszengCN/CarlaAir

---

### 9. ForestSim: A Synthetic Benchmark for Intelligent Vehicle Perception in Unstructured Forest Environments

- **作者**: Pragat Wagle, Zheng Chen, Lantao Liu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.27923v1)
- **发表日期**: 2026-03-30
- **匹配关键词**: autonomous navigation, navigation
- **arXiv**: [2603.27923v1](http://arxiv.org/abs/2603.27923v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: CODE, GITHUB
  - 链接：https://vailforestsim.github.io, https://github.com/pragatwagle/ForestSim
- **中文摘要**: 鲁棒场景理解对于在自然非结构化环境中运行的智能车辆至关重要。尽管面向结构化城市驾驶场景的语义分割数据集已十分丰富，但由于生成像素级精确标注的难度与成本，针对极端非结构化野外环境的数据集仍然稀缺。这一局限性阻碍了林业自动化、农业机器人、灾害响应及全地形移动等任务所需的智能地面车辆感知系统的发展。为填补这一空白，我们推出ForestSim——一个专为森林越野与无道路环境中智能车辆语义分割模型训练与评估而设计的高保真合成数据集。ForestSim包含25种不同环境下的2094张逼真图像，涵盖多季节、多地形类型及多种植被密度。通过将虚幻引擎环境与微软AirSim集成，我们生成了涵盖20个与自主导航相关类别的、具有像素级精度的统一标注。我们使用最先进的架构对ForestSim进行基准测试，结果表明即使在非结构化场景的固有挑战下仍能实现优异性能。ForestSim为支持下一代智能越野车辆的感知研究提供了可扩展且易于获取的基础。数据集与代码均已公开：数据集：https://vailforestsim.github.io 代码：https://github.com/pragatwagle/ForestSim

---

### 10. Wan-R1: Verifiable-Reinforcement Learning for Video Reasoning

- **作者**: Ming Liu, Yunbei Zhang, Shilong Liu, Liwen Wang, Wensheng Zhang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.27866v1)
- **发表日期**: 2026-03-29
- **匹配关键词**: navigation
- **arXiv**: [2603.27866v1](http://arxiv.org/abs/2603.27866v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: CODE
- **中文摘要**: 视频生成模型能够生成视觉连贯的内容，但在需要空间推理和多步骤规划的任务上仍面临挑战。强化学习为提高泛化能力提供了路径，但其在视频推理中的有效性取决于奖励设计——这一挑战目前尚未得到系统性研究。我们通过将群体相对策略优化方法适配于基于流的视频模型，并在迷宫求解和机器人导航任务上进行训练，来探究这一问题。首先，我们发现多模态奖励模型在此场景下会出现灾难性失效。为解决这一问题，我们设计了基于客观任务指标的可验证奖励函数。针对结构化游戏环境，我们引入了多组件轨迹奖励机制；对于机器人导航任务，我们提出了嵌入层级的可验证奖励方案。实验表明，采用可验证奖励的强化学习微调能有效提升模型泛化能力。例如在复杂三维迷宫任务中，我们的模型相比监督微调基线将精确匹配准确率提升了29.1%，在陷阱规避任务中提升幅度达51.4%。系统性奖励分析表明，可验证奖励是实现稳定训练的关键要素，而多模态奖励模型可能导致退化解。这些发现确立了可验证奖励设计作为实现鲁棒视频推理的核心推动力。相关代码将公开提供。

---

### 11. Spectral Decomposition of Inverse Dynamics for Fast Exploration in Model-Based Manipulation

- **作者**: Solvin Sigurdson, Benjamin Riviere, Joel Burdick
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.27796v1)
- **发表日期**: 2026-03-29
- **匹配关键词**: exploration
- **arXiv**: [2603.27796v1](http://arxiv.org/abs/2603.27796v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 由于需要通过非线性接触动力学和多种接触模式探索可行轨迹的复杂性，规划长时间机器人操作序列具有挑战性。此外，这种复杂性随着问题的时间跨度增加而增长。我们提出了一种搜索树方法，该方法利用逆动力学方程的谱分解生成轨迹。该方程将执行器位移映射到物体位移，其谱分解在探索中效率较高，因为其分量正交且能近似物体的可达集，同时保持动力学可行性。这些轨迹可与任何基于搜索的方法（如快速探索随机树）结合，用于长时域规划。我们的方法在短时域任务的模型规划方面与近期研究表现相当，并在解决长时域任务方面具有独特优势：现有方法无法完成时，我们的方法能在15秒计算时间内生成持续45秒、包含10种以上接触模式的规划方案，在高度复杂领域展现出实时处理能力。

---

