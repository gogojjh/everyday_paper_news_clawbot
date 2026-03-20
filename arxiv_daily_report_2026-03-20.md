# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-03-20 08:04

**今日新增**: 16 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 4/16 篇提供

**🌟 Highlight**: 7 篇 | **📌 Poster**: 9 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. GMT: Goal-Conditioned Multimodal Transformer for 6-DOF Object Trajectory Synthesis in 3D Scenes

- **作者**: Huajian Zeng, Abhishek Saroha, Daniel Cremers, Xi Wang ⭐
  - **高亮作者**: Daniel Cremers
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.17993v1)
- **发表日期**: 2026-03-18
- **匹配关键词**: object manipulation
- **arXiv**: [2603.17993v1](http://arxiv.org/abs/2603.17993v1)
- **📥 PDF**: 已下载至本地 (`2603.17993v1_GMT_Goal-Conditioned_Multimodal_Transformer_for_6-DOF_Object_Trajectory_Synthesis_in_3D_Scenes.pdf`)
- **🔓 开源**: PROJECT_PAGE
- **中文摘要**: 在三维环境中合成可控的六自由度物体操作轨迹对于实现机器人与复杂场景交互至关重要，但由于需要精确的空间推理、物理可行性及多模态场景理解，该任务仍具挑战性。现有方法多依赖二维或局部三维表征，限制了其对完整场景几何结构的捕捉能力，并制约了轨迹精度。本文提出GMT——一种多模态Transformer框架，通过联合利用三维边界框几何、点云上下文、语义物体类别及目标末端姿态，生成真实且目标导向的物体运动轨迹。该模型将轨迹表示为连续的六自由度姿态序列，并采用定制化的条件融合策略，整合几何、语义、上下文及目标导向信息。在合成与真实场景基准测试中的大量实验表明，GMT在空间精度和姿态控制方面显著优于CHOIS、GIMO等当前最优的人体运动与人-物交互基线方法。本方法为基于学习的操作规划建立了新基准，并展现出对多样化物体及杂乱三维环境的强大泛化能力。项目页面：https://huajian-zeng.github.io/projects/gmt/。

---

### 2. ProbeFlow: Training-Free Adaptive Flow Matching for Vision-Language-Action Models

- **作者**: Zhou Fang, Jiaqi Wang, Yi Zhou, Qiongfeng Shi
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.17850v1)
- **发表日期**: 2026-03-18
- **匹配关键词**: vision-language-action, vision-language-action model, VLA
- **arXiv**: [2603.17850v1](http://arxiv.org/abs/2603.17850v1)
- **📥 PDF**: 已下载至本地 (`2603.17850v1_ProbeFlow_Training-Free_Adaptive_Flow_Matching_for_Vision-Language-Action_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 近期配备流匹配（Flow Matching，FM）动作头的视觉-语言-动作（VLA）模型在复杂机器人操作任务中取得了最先进的性能。然而，FM所需的多步迭代常微分方程求解过程会引入推理延迟，阻碍了响应式物理控制的实现。当前加速研究主要针对视觉-语言模型（VLM）主干进行优化，而动作头部的计算瓶颈尚未得到充分关注。为此，我们提出ProbeFlow——一种专为连续机器人控制设计的免训练自适应推理框架。该框架通过计算初始速度向量与前瞻速度向量之间的余弦相似度来评估轨迹几何复杂度，从而动态调度积分步数以剪枝冗余的网络计算。在MetaWorld基准测试中，该方法将动作解码速度提升14.8倍（平均计算步数从N=50降至2.6），端到端系统延迟降低2.8倍，且未影响操作成功率。在长时程LIBERO基准测试中，探测机制能自动分配更密集的计算调度以应对语义瓶颈，有效解决了流求解器的延迟问题。真实物理场景部署验证表明，ProbeFlow在保证执行稳定性的同时成功降低了动作解码延迟，为低延迟连续生成策略提供了极具实用价值的解决方案。

---

### 3. Generative Control as Optimization: Time Unconditional Flow Matching for Adaptive and Robust Robotic Control

- **作者**: Zunzhe Zhang, Runhan Huang, Yicheng Liu, Shaoting Zhu, Linzhan Mou, Hang Zhao
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.17834v1)
- **发表日期**: 2026-03-18
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2603.17834v1](http://arxiv.org/abs/2603.17834v1)
- **📥 PDF**: 已下载至本地 (`2603.17834v1_Generative_Control_as_Optimization_Time_Unconditional_Flow_Matching_for_Adaptive_and_Robust_Robotic_.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 扩散模型与流匹配已成为机器人模仿学习的基石，但其存在结构性低效问题：推理过程通常受限于固定的积分调度机制，无法根据状态复杂度进行自适应调整。这种范式迫使策略在处理简单动作与复杂任务时消耗相同的计算资源。我们提出生成式控制即优化（GeCO），这是一种时间无关的框架，将动作合成从轨迹积分转化为迭代优化过程。GeCO在动作序列空间中学习一个平稳的速度场，使专家行为形成稳定的吸引子。因此，测试时推理转变为自适应过程，能够根据收敛状态动态分配计算资源——对简单状态提前终止优化，对复杂状态则进行更长时间的精细化调整。此外，这种平稳几何结构产生了一种无需训练的内在安全信号：优化后动作对应的速度场范数可作为鲁棒的分布外（OOD）检测器，在分布内状态下保持较低数值，而对异常状态则显著升高。我们在标准仿真基准测试中验证了GeCO的有效性，并展示了其可无缝扩展至pi0系列视觉-语言-动作（VLA）模型。作为标准流匹配头的即插即用替代方案，GeCO通过原生优化机制提升了任务成功率与执行效率，为安全部署提供了新途径。视频与代码详见 https://hrh6666.github.io/GeCO/

---

### 4. HeiSD: Hybrid Speculative Decoding for Embodied Vision-Language-Action Models with Kinematic Awareness

- **作者**: Zihao Zheng, Zhihao Mao, Sicheng Tian, Maoliang Li, Jiayu Chen, Xinhao Sun, Zhaobo Zhang, Xuanzhe Liu, Donggang Cao, Hong Mei, Xiang Chen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.17573v1)
- **发表日期**: 2026-03-18
- **匹配关键词**: vision-language-action, vision-language-action model, VLA
- **arXiv**: [2603.17573v1](http://arxiv.org/abs/2603.17573v1)
- **📥 PDF**: 已下载至本地 (`2603.17573v1_HeiSD_Hybrid_Speculative_Decoding_for_Embodied_Vision-Language-Action_Models_with_Kinematic_Awarenes.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型已成为机器人控制的主流解决方案，但其推理速度较慢。推测解码（SD）是一种有前景的加速方法，可分为两类：基于草稿器的SD和基于检索的SD。现有方法未能分析这两类SD在VLA模型中的优缺点，导致它们被单独应用或优化。本文分析了VLA模型控制下的机器人轨迹模式，得出一个关键见解：两类SD应以混合方式使用。然而，在VLA模型中实现混合SD面临几个挑战：（1）基于检索的SD中存在草稿拒绝和持续错误；（2）难以确定混合边界。为解决这些问题，我们提出了HeiSD框架。在HeiSD中，我们提出了一种基于检索的SD优化方法，包含验证跳过机制和序列级松弛接受策略。此外，我们在HeiSD中提出了一种基于运动学的融合度量，以自动确定混合边界。实验结果表明，HeiSD在仿真基准测试中实现了高达2.45倍的加速，在真实场景中实现了2.06倍至2.41倍的加速，同时保持了较高的任务成功率。

---

### 5. KineVLA: Towards Kinematics-Aware Vision-Language-Action Models with Bi-Level Action Decomposition

- **作者**: Gaoge Han, Zhengqing Gao, Ziwen Li, Jiaxin Huang, Shaoli Huang, Fakhri Karray, Mingming Gong, Tongliang Liu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.17524v1)
- **发表日期**: 2026-03-18
- **匹配关键词**: vision-language-action, vision-language-action model, VLA
- **arXiv**: [2603.17524v1](http://arxiv.org/abs/2603.17524v1)
- **📥 PDF**: 已下载至本地 (`2603.17524v1_KineVLA_Towards_Kinematics-Aware_Vision-Language-Action_Models_with_Bi-Level_Action_Decomposition.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 本文提出了一种新颖的、富含运动学信息的视觉-语言-动作任务。与传统动作指令仅粗略或部分捕捉运动属性不同，该任务通过语言指令在关键节点密集编码从起始到完成的多样化运动学属性（如方向、轨迹、朝向和相对位移），从而支持细粒度与个性化的操作。在此设定下，任务目标保持恒定，而执行轨迹需根据指令层级的运动学规范进行自适应调整。为应对这一挑战，我们提出KineVLA框架——一种通过双层动作表征与双层推理标记显式解耦目标不变性与运动可变性的视觉-语言-动作框架，这些标记作为受监督的显式中介变量，实现了语言与动作的对齐。为支撑该任务，我们构建了涵盖仿真与真实机器人平台的运动感知VLA数据集，其特点在于指令层级的运动学变体及双层标注。在LIBERO仿真环境与Realman-75实体机器人上的大量实验表明，KineVLA在运动敏感基准测试中持续优于现有VLA基线方法，实现了更精准、可控且可泛化的操作行为。

---

### 6. OmniVLN: Omnidirectional 3D Perception and Token-Efficient LLM Reasoning for Visual-Language Navigation across Air and Ground Platforms

- **作者**: Zhongyuang Liu, Min He, Shaonan Yu, Xinhang Xu, Muqing Cao, Jianping Li, Jianfei Yang, Lihua Xie
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.17351v1)
- **发表日期**: 2026-03-18
- **匹配关键词**: VLN, scene graph, dynamic scene graph, navigation
- **arXiv**: [2603.17351v1](http://arxiv.org/abs/2603.17351v1)
- **📥 PDF**: 已下载至本地 (`2603.17351v1_OmniVLN_Omnidirectional_3D_Perception_and_Token-Efficient_LLM_Reasoning_for_Visual-Language_Navigati.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 语言引导的具身导航要求智能体能够解析物体指代指令，在多个房间中进行搜索，定位目标物体，并执行可靠的运动。现有系统在真实室内环境中仍存在局限：狭窄的视场感知仅能提供每一步的局部场景信息，常迫使机器人频繁旋转，延迟目标发现，并导致空间理解碎片化；同时，若直接将密集三维地图或详尽物体列表输入大语言模型，会迅速超出上下文容量限制。本文提出OmniVLN——一种零样本视觉语言导航框架，通过结合全向三维感知与令牌高效的分层推理机制，同时适用于空中与地面机器人。OmniVLN融合旋转激光雷达与全景视觉构建硬件无关的建图系统，从网格几何到房间及建筑层级结构逐步构建五层动态场景图，并基于持续同调的房间划分与几何/视觉语言模型混合关系验证实现高层拓扑的稳定化。在导航过程中，全局动态场景图被转化为以智能体为中心的三维八分体表示，结合多分辨率空间注意力提示机制，使大语言模型能够逐步筛选候选房间、推断自身朝向、定位目标物体并生成可执行导航指令，同时保持精细的局部细节与紧凑的长程记忆。实验表明，所提出的分层接口将空间指代准确率从77.27%提升至93.18%，在杂乱多房间场景中累计提示令牌减少达61.7%，导航成功率较平面列表基线最高提升11.68%。我们将公开代码与全向多模态数据集以支持可复现研究。

---

### 7. vAccSOL: Efficient and Transparent AI Vision Offloading for Mobile Robots

- **作者**: Adam Zahir, Michele Gucciardom Falk Selker, Anastasios Nanos, Kostis Papazafeiropoulos, Carlos J. Bernardos, Nicolas Weber, Roberto Gonzalez
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.16685v1)
- **发表日期**: 2026-03-17
- **匹配关键词**: navigation
- **arXiv**: [2603.16685v1](http://arxiv.org/abs/2603.16685v1)
- **📥 PDF**: 已下载至本地 (`2603.16685v1_vAccSOL_Efficient_and_Transparent_AI_Vision_Offloading_for_Mobile_Robots.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 移动机器人正日益广泛地应用于巡检、巡逻和搜救任务，其依赖计算机视觉实现环境感知、自主导航与决策。然而，由于机载计算资源有限且受严格能耗约束，在机器人本体执行现代视觉计算任务面临挑战。虽然部分平台配备嵌入式加速器，但这些硬件通常绑定专有软件栈，导致用户自定义工作负载只能在资源受限的配套计算机上运行。

本文提出vAccSOL框架，旨在实现跨异构机器人及边缘平台的高效透明化人工智能视觉任务执行。该框架整合两大核心组件：SOL神经网络编译器可生成具有最小运行时依赖的优化推理库；vAccel轻量级执行框架能够透明化地将推理任务调度至机器人本地或邻近边缘基础设施。这种组合方式在无需修改机器人应用程序的前提下，实现了硬件优化推理与灵活执行部署。

我们在真实测试环境中对vAccSOL进行评估，使用商用四足机器人并涵盖图像分类、视频分类和语义分割三大类共十二个深度学习模型。实验表明：相较于PyTorch编译器基准，SOL达到相当或更优的推理性能；通过边缘卸载机制，vAccSOL较PyTorch方案降低机器人端功耗最高达80%，边缘端功耗最高降低60%，同时将视觉处理流水线帧率提升最高24倍，显著延长了电池供电机器人的持续作业时间。

---

## 📌 Poster

*其他相关研究*

---

### 1. AERR-Nav: Adaptive Exploration-Recovery-Reminiscing Strategy for Zero-Shot Object Navigation

- **作者**: Jingzhi Huang, Junkai Huang, Haoyang Yang, Haoang Li, Yi Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.17712v1)
- **发表日期**: 2026-03-18
- **匹配关键词**: exploration, navigation
- **arXiv**: [2603.17712v1](http://arxiv.org/abs/2603.17712v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 未知多层环境中的零样本目标导航任务面临重大挑战。近期研究主要通过基于语义价值的贪心路径点选择、空间拓扑增强记忆以及多模态大语言模型决策框架等方法取得进展。然而，这些架构在应对未见环境（尤其是多层场景）时难以平衡探索与利用，常出现机器人卡在狭窄交叉口、无效徘徊或无法定位楼梯入口等问题。为突破这些局限，我们提出AERR-Nav——一种能根据环境动态调整状态的零样本目标导航框架。该框架具备两大核心优势：（1）自适应探索-恢复-回溯策略使机器人能在三种状态间动态切换，针对不同导航场景实现专业化响应；（2）配备快慢思维模式的自适应探索状态，帮助机器人基于环境信息演化更好地平衡探索、利用与高层推理。在HM3D和MP3D基准测试中的大量实验表明，AERR-Nav在零样本方法中达到最优性能。系统的消融研究进一步验证了所提策略与模块的有效性。

---

### 2. Consistency-Driven Dual LSTM Models for Kinematic Control of a Wearable Soft Robotic Arm

- **作者**: Xingyu Chen, Yi Xiong, Li Wen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.17672v1)
- **发表日期**: 2026-03-18
- **匹配关键词**: human-robot collaboration
- **arXiv**: [2603.17672v1](http://arxiv.org/abs/2603.17672v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 本文提出了一种基于一致性驱动的双长短期记忆网络框架，用于精确学习集成于可穿戴设备的气动软体机械臂正向与逆向运动学。该方法有效捕捉了软体气动执行器的非线性与迟滞特性，同时解决了驱动输入与末端执行器位置之间一对多映射的难题。通过引入循环一致性损失函数，我们增强了物理真实性并提升了逆向预测的稳定性。大量实验——包括轨迹跟踪、消融研究和可穿戴演示——验证了本方法的有效性。结果表明，与传统方法相比，一致性损失的引入显著提高了预测精度并促进了物理一致性。此外，该可穿戴软体机械臂在物体传递、障碍物感知抓取放置及抽屉操作等日常任务中展现出强大的人机协作能力与适应性。本研究凸显了基于学习的运动学模型在以人为中心的可穿戴机器人系统中的广阔应用前景。

---

### 3. Interpreting Context-Aware Human Preferences for Multi-Objective Robot Navigation

- **作者**: Tharun Sethuraman, Subham Agrawal, Nils Dengler, Jorge de Heuvel, Teena Hassan, Maren Bennewitz
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.17510v1)
- **发表日期**: 2026-03-18
- **匹配关键词**: robot navigation, navigation
- **arXiv**: [2603.17510v1](http://arxiv.org/abs/2603.17510v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 在人类共享环境中运行的机器人，不仅需要实现安全与效率等任务级导航目标，还应使其行为适应人类偏好。然而，由于人类偏好通常以自然语言表达且依赖于环境上下文，难以直接将其整合到低层机器人控制策略中。本研究提出一种技术框架，通过将基础模型与多目标强化学习导航策略相结合，使机器人能够理解并应用上下文相关的导航偏好，从而实现了高层语义推理与低层运动控制的有机融合。视觉语言模型从机载视觉观测中提取结构化环境上下文，而大型语言模型则将自然语言用户反馈转化为可解释的、依赖上下文的行为规则，存储于持久且可更新的规则记忆库中。偏好转换模块随后将上下文信息与存储规则映射为数值化偏好向量，这些向量参数化预训练的多目标强化学习策略，实现实时导航自适应。我们通过组件级定量评估、用户研究以及在多种室内环境中的真实机器人部署对所提框架进行验证。结果表明，该系统能够可靠捕捉用户意图，生成一致的偏好向量，并在多样化场景中实现可控的行为适应。总体而言，所提出的技术框架在保持安全、响应式实时控制的同时，显著提升了共享人机环境中机器人的适应性、透明度和可用性。

---

### 4. DesertFormer: Transformer-Based Semantic Segmentation for Off-Road Desert Terrain Classification in Autonomous Navigation Systems

- **作者**: Yasaswini Chebolu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.17056v1)
- **发表日期**: 2026-03-17
- **匹配关键词**: path planning, autonomous navigation, navigation
- **arXiv**: [2603.17056v1](http://arxiv.org/abs/2603.17056v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: GITHUB
  - 链接：https://github.com/Yasaswini-ch/Vision-based-Desert-Terrain-Segmentation-using-SegFormer.
- **中文摘要**: 可靠的地形感知是自动驾驶在非结构化越野环境中实现自主导航的基本要求。沙漠地貌因地形类别间色彩对比度低、光照变化极端以及植被稀疏等特点，对标准道路场景分割模型的假设构成独特挑战。本文提出DesertFormer——一种基于SegFormer B2架构（采用分层混合变换器MiT-B2主干网络）的越野沙漠地形语义分割系统。该系统将地形划分为十个具有生态意义的类别：树木、茂密灌木、干草、干燥灌木、地面杂物、花卉、原木、岩石、地貌和天空，从而为地面机器人和自动驾驶车辆提供安全感知路径规划能力。通过在包含4,176张512×512分辨率标注图像的专用越野数据集上进行训练，DesertFormer实现了64.4%的平均交并比（mIoU）和86.1%的像素精度，相较于DeepLabV3 MobileNetV2基线模型（41.0% mIoU）实现了24.2%的绝对性能提升。我们进一步通过系统性故障分析识别出主要混淆模式——地面杂物与地貌的误判、干草与地貌的误判，并针对稀有地形类别提出类别加权训练与复制粘贴数据增强策略。相关代码、模型检查点及交互式推理仪表板已发布于https://github.com/Yasaswini-ch/Vision-based-Desert-Terrain-Segmentation-using-SegFormer。

---

### 5. MolmoB0T: Large-Scale Simulation Enables Zero-Shot Manipulation

- **作者**: Abhay Deshpande, Maya Guru, Rose Hendrix, Snehal Jauhri, Ainaz Eftekhar, Rohun Tripathi, Max Argus, Jordi Salvador, Haoquan Fang, Matthew Wallingford, Wilbert Pumacay, Yejin Kim, Quinn Pfeifer, Ying-Chun Lee, Piper Wolters, Omar Rayyan, Mingtong Zhang, Jiafei Duan, Karen Farley, Winson Han, Eli Vanderbilt, Dieter Fox, Ali Farhadi, Georgia Chalvatzaki, Dhruv Shah, Ranjay Krishna
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.16861v1)
- **发表日期**: 2026-03-17
- **匹配关键词**: door opening, articulated object, mobile manipulator, object manipulation, mobile manipulation
- **arXiv**: [2603.16861v1](http://arxiv.org/abs/2603.16861v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: CODE
- **中文摘要**: 机器人学习领域的主流观点认为，仅靠仿真训练是不够的；学界普遍认为要实现有效的仿真到现实迁移，至少需要采集部分真实世界数据或进行任务特定微调，以弥合仿真环境与物理环境之间的差距。我们对此假设提出挑战。通过使用足够大规模且多样化的仿真合成训练数据，我们证明零样本迁移至现实世界不仅可行，而且对静态与移动操作任务均具有显著效果。我们推出MolmoBot-Engine——一个完全开源的流程化数据生成管道，可在MolmoSpaces中跨机器人、任务及多样化仿真环境进行程序化数据生成。基于此，我们发布了MolmoBot-Data数据集，包含180万条针对铰接物体操作与抓放任务的专家轨迹数据。我们训练了三种策略模型：MolmoBot（基于Molmo2的多帧视觉语言模型，配备流匹配动作头）、MolmoBot-Pi0（复现π₀架构以实现直接对比）以及MolmoBot-SPOC（适用于边缘部署且支持强化学习微调的轻量级策略）。我们在两个机器人平台上进行评估：用于桌面操作任务的Franka FR3，以及用于开门、抽屉操作、柜体交互和移动抓放任务的Rainbow Robotics RB-Y1移动机械臂。在未进行任何现实世界微调的情况下，我们的策略实现了对未见物体和环境的零样本迁移。在桌面抓放任务中，MolmoBot在4种场景的现实世界评估中达到79.2%的成功率，显著优于π₀.5的39.2%。我们的研究结果表明，程序化环境生成与多样化铰接资源相结合，能够产生具有广泛现实世界泛化能力的鲁棒操作策略。技术博客：https://allenai.org/blog/molmobot-robot-manipulation

---

### 6. DreamPlan: Efficient Reinforcement Fine-Tuning of Vision-Language Planners via Video World Models

- **作者**: Emily Yue-Ting Jia, Weiduo Yuan, Tianheng Shi, Vitor Guizilini, Jiageng Mao, Yue Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.16860v1)
- **发表日期**: 2026-03-17
- **匹配关键词**: object manipulation
- **arXiv**: [2603.16860v1](http://arxiv.org/abs/2603.16860v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: PROJECT_PAGE
- **中文摘要**: 机器人操作需要复杂的常识推理能力，这种能力正是大规模视觉语言模型（VLMs）所天然具备的。尽管VLMs展现出作为零样本规划器的潜力，但由于缺乏对物理世界的具身理解，在复杂现实环境中部署时（尤其是面对可变形物体操作等挑战性任务时），往往会产生误差累积和成功率低下的问题。虽然强化学习（RL）能够使这些规划器适应特定任务动态，但通过现实世界交互直接微调VLMs成本极高、存在安全隐患且样本效率低下。为突破这一瓶颈，我们提出了DreamPlan——一种通过视频世界模型对VLM规划器进行强化微调的新框架。DreamPlan首先利用零样本VLM收集探索性交互数据，而非依赖昂贵的物理环境试错。我们证明，这种次优数据足以训练动作条件视频生成模型，该模型能隐式捕捉复杂的现实世界物理规律。随后，通过优势比策略优化（ORPO）方法，在视频世界模型的“想象空间”中对VLM规划器进行完整微调。借助这些虚拟试错过程，物理知识和任务特定知识得以高效注入VLM。实验结果表明，DreamPlan成功弥合了语义推理与物理具身之间的鸿沟，在无需大规模现实数据收集的情况下显著提升了操作成功率。项目页面详见 https://psi-lab.ai/DreamPlan/。

---

### 7. DexGrasp-Zero: A Morphology-Aligned Policy for Zero-Shot Cross-Embodiment Dexterous Grasping

- **作者**: Yuliang Wu, Yanhan Lin, WengKit Lao, Yuhao Lin, Yi-Lin Wei, Wei-Shi Zheng, Ancong Wu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.16806v2)
- **发表日期**: 2026-03-17
- **匹配关键词**: dexterous grasping
- **arXiv**: [2603.16806v2](http://arxiv.org/abs/2603.16806v2)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 为满足日益多样化的灵巧手硬件需求，开发无需重复学习即可实现零样本跨本体抓取策略至关重要。由于异构手部运动学与物理约束的差异，跨本体对齐面临严峻挑战。现有方法通常通过预测中间运动目标并重定向至各本体，但可能引入误差并违反特定本体的物理限制，从而阻碍跨异构手型的技能迁移。为突破这些局限，我们提出DexGrasp-Zero策略，通过从多本体数据中学习通用抓取技能，实现向未见手型的零样本迁移。我们首先提出形态对齐图表示法，将各手型的关键运动学节点映射至解剖学基础节点，并为每个节点配备三轴正交运动基元，实现跨形态的结构与语义对齐。基于此图表示法，我们设计形态对齐图卷积网络（MAGCN）进行策略学习的图编码。该网络融合物理属性注入机制，将手部特定物理约束整合至图特征中，实现对不同连杆长度与驱动限制的自适应补偿，从而达成精准稳定的抓取。在YCB数据集上的大量仿真实验表明，我们的策略通过在四种异构手型（Allegro、Shadow、Schunk、Ability）上联合训练，在未见硬件（LEAP、Inspire）上实现85%的零样本成功率，较现有最优方法提升59.5%。真实世界实验进一步在三个机器人平台（LEAP、Inspire、Revo2）验证策略有效性，在未见物体上取得82%的平均成功率。

---

### 8. Beyond Cybathlon: On-demand Quadrupedal Assistance for People with Limited Mobility

- **作者**: Carmen Scheidemann, Andrei Cramariuc, Changan Chen, Jia-Ruei Chiu, Marco Hutter
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.16772v1)
- **发表日期**: 2026-03-17
- **匹配关键词**: mobile manipulation, navigation
- **arXiv**: [2603.16772v1](http://arxiv.org/abs/2603.16772v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 背景：辅助机器人有潜力提升因行动受限或需依赖轮椅而需要日常护理者的独立性。当前将机械臂安装在电动轮椅上的解决方案虽能提供有限的额外活动能力，但代价是增加了设备体积并降低了轮椅的操控灵活性。

方法：我们提出一种按需服务的四足辅助机器人系统，采用共享自主控制方式，将半自主任务执行与人工远程操作相结合。得益于系统的移动特性，它能在需要时随时协助操作者，并独立执行自主任务，同时不限制操作者的行动自由。我们实现了拾取放置任务的自动化，以及通过具备语义感知和避障功能的导航系统实现机器人在环境中的自主移动。针对远程操作，我们开发了一种口部操纵杆界面，使行动受限的操作者能够精确控制机器人末端执行器进行精细操作。

结果：我们在《2024年辅助机器人竞赛》中展示了该系统，并在家庭实验环境中进行了验证，测量了任务完成时间和用户满意度。研究发现我们的系统能够协助完成多种任务，包括需要灵巧操作的任务。用户研究证实了增加机器人自主性可减轻操作者精神负担的预期。

结论：我们提出了一种灵活的系统，通过使轮椅使用者能够在无外部支持的情况下解决移动操作问题，有望帮助他们在日常生活中保持独立性。在主观评价指标上，我们取得了与先前先进技术相当的结果，同时为操作者提供了更高的自主性和更强的操作灵活性。

---

### 9. Dexterous grasp data augmentation based on grasp synthesis with fingertip workspace cloud and contact-aware sampling

- **作者**: Liqi Wu, Haoyu Jia, Kento Kawaharazuka, Hirokazu Ishida, Kei Okada
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.16609v1)
- **发表日期**: 2026-03-17
- **匹配关键词**: grasp synthesis
- **arXiv**: [2603.16609v1](http://arxiv.org/abs/2603.16609v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 机器人抓取是机器人应用中的基础且关键环节，高效抓取往往是各类任务执行的起点。随着神经网络的快速发展，数据驱动的机器人抓取方法已成为主流。然而，如何高效生成用于训练的抓取数据集仍是当前瓶颈。加之机器人手部结构的多样性，使得设计具有普适性的抓取生成方法更为复杂。本研究提出一种基于遥操作的框架，通过采集少量抓取姿态示范数据，并利用指尖接触感知的采样式抓取生成器（FSG）进行数据增强。基于示范抓取姿态，我们提出AutoWS方法，可自动生成机器人指尖的结构化工作空间点云，将手部结构信息直接嵌入点云中，从而省去逆运动学计算环节。在YCB物体抓取实验中，本方法在生成速度与有效姿态生成率方面均显著优于现有方法。该框架支持任意结构手部的实时抓取生成，结合示范数据可产生类人化抓取动作，为数据驱动的抓取训练提供了高效鲁棒的数据增强工具。

---

