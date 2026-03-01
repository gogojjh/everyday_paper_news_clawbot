# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-03-01 08:03

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 5/20 篇提供

**🌟 Highlight**: 14 篇 | **📌 Poster**: 6 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. UniScale: Unified Scale-Aware 3D Reconstruction for Multi-View Understanding via Prior Injection for Robotic Perception

- **作者**: Mohammad Mahdavian, Gordon Tan, Binbin Xu, Yuan Ren, Dongfeng Bai, Bingbing Liu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.23224v1)
- **发表日期**: 2026-02-26
- **匹配关键词**: 3D reconstruction, navigation, 3d reconstruction
- **arXiv**: [2602.23224v1](http://arxiv.org/abs/2602.23224v1)
- **📥 PDF**: 已下载至本地 (`2602.23224v1_UniScale_Unified_Scale-Aware_3D_Reconstruction_for_Multi-View_Understanding_via_Prior_Injection_for_.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出UniScale——一个面向机器人应用、具备统一尺度感知的多视角三维重建框架，该框架通过模块化语义感知设计灵活整合几何先验。在基于视觉的机器人导航中，从原始图像序列中准确提取环境结构对下游任务至关重要。UniScale通过单一前馈网络应对这一挑战，该网络能够从多视角图像中联合估计相机内外参数、尺度不变深度图与点云图以及场景的度量尺度，并可在获得辅助几何先验时选择性融合。通过将全局上下文推理与相机感知特征表示相结合，UniScale能够恢复场景的度量尺度。在已知相机内参的机器人应用场景中，可轻松融入该信息以提升性能；若同时获得相机位姿，则可实现额外增益。这种协同设计使得单一统一模型能够实现鲁棒的度量感知三维重建。值得注意的是，UniScale无需从头训练，且能利用预训练模型中展现的世界先验而无需几何编码策略，这使其特别适合资源受限的机器人团队。我们在多个基准测试中评估UniScale，证明其在不同环境中具有强大的泛化能力和稳定的性能表现。论文录用后我们将公开实现代码。

---

### 2. Latent Gaussian Splatting for 4D Panoptic Occupancy Tracking

- **作者**: Maximilian Luz, Rohit Mohan, Thomas Nürnberg, Yakov Miron, Daniele Cattaneo, Abhinav Valada
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.23172v1)
- **发表日期**: 2026-02-26
- **匹配关键词**: gaussian splatting
- **arXiv**: [2602.23172v1](http://arxiv.org/abs/2602.23172v1)
- **📥 PDF**: 已下载至本地 (`2602.23172v1_Latent_Gaussian_Splatting_for_4D_Panoptic_Occupancy_Tracking.pdf`)
- **🔓 开源**: CODE
- **中文摘要**: 捕捉四维时空环境对于机器人在动态环境中安全可靠运行至关重要。然而，现有方法大多仅解决单方面问题：要么通过边界框提供粗略的几何追踪，要么提供缺乏显式时间关联的详细三维结构（如基于体素的占据栅格）。本研究提出基于潜在高斯泼溅的四维全景占据追踪方法（LaGS），将时空场景理解推向整体化发展方向。该方法融合了基于摄像头的端到端追踪与基于掩码的多视角全景占据预测，并通过创新的潜在高斯泼溅技术，有效解决了多视角信息向三维体素网格高效聚合的关键挑战。具体而言，我们首先将观测数据融合为三维高斯分布，作为三维场景的稀疏点中心潜在表征，随后将聚合特征泼溅至三维体素网格，并通过基于掩码的分割头进行解码。我们在Occ3D nuScenes和Waymo数据集上评估LaGS，在四维全景占据追踪任务中取得了最先进的性能表现。代码已开源：https://lags.cs.uni-freiburg.de/。

---

### 3. DySL-VLA: Efficient Vision-Language-Action Model Inference via Dynamic-Static Layer-Skipping for Robot Manipulation

- **作者**: Zebin Yang, Yijiahao Qi, Tong Xie, Bo Yu, Shaoshan Liu, Meng Li
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.22896v1)
- **发表日期**: 2026-02-26
- **匹配关键词**: vision-language-action, VLA, vision-language-action model
- **arXiv**: [2602.22896v1](http://arxiv.org/abs/2602.22896v1)
- **📥 PDF**: 已下载至本地 (`2602.22896v1_DySL-VLA_Efficient_Vision-Language-Action_Model_Inference_via_Dynamic-Static_Layer-Skipping_for_Robo.pdf`)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/PKU-SEC-Lab/DYSL_VLA.
- **中文摘要**: 视觉-语言-动作（VLA）模型通过融合语言模型的推理能力与视觉模型的三维理解能力，在机器人操作等任务中展现出卓越性能。然而，其高昂的计算成本仍是实际应用中实现实时性能的主要障碍。我们观察到，任务中的动作具有不同程度的重要性：关键步骤需要高精度执行，而次要步骤则可容忍更大误差。基于这一发现，我们提出DySL-VLA框架，通过根据动作重要性动态跳过VLA层级来降低计算成本。DySL-VLA将网络层分为两类：始终执行的信息层和可选择性跳过的增量层。为在不牺牲精度的情况下智能跳过层级，我们设计了先验-后验跳转引导机制来确定层级跳过的时机。同时提出一种跳转感知的两阶段知识蒸馏算法，用于高效地将标准VLA模型训练为DySL-VLA模型。实验表明，在Calvin数据集上，DySL-VLA相比Deer-VLA实现了2.1%的成功长度提升，同时将可训练参数量减少85.7倍，并在同等精度下较RoboFlamingo基线获得3.75倍加速。代码已开源：https://github.com/PKU-SEC-Lab/DYSL_VLA。

---

### 4. GraspLDP: Towards Generalizable Grasping Policy via Latent Diffusion

- **作者**: Enda Xiang, Haoxiang Ma, Xinzhu Ma, Zicheng Liu, Di Huang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.22862v1)
- **发表日期**: 2026-02-26
- **匹配关键词**: diffusion policy, diffusion-based policy
- **arXiv**: [2602.22862v1](http://arxiv.org/abs/2602.22862v1)
- **📥 PDF**: 已下载至本地 (`2602.22862v1_GraspLDP_Towards_Generalizable_Grasping_Policy_via_Latent_Diffusion.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 本文聚焦于提升通过模仿学习习得的操作策略在抓取精度与泛化能力方面的表现。扩散模型驱动的策略学习方法已成为机器人操作任务的主流范式。抓取作为操作中的关键子任务，模仿学习策略执行精确且可泛化抓取的能力值得特别关注。现有抓取模仿学习方法常面临执行精度不足、空间泛化有限及物体泛化能力弱等挑战。为应对这些问题，我们将抓取先验知识融入扩散策略框架：采用隐空间扩散策略，以抓取姿态先验引导动作片段解码，确保生成的运动轨迹紧密贴合可行抓取构型；同时，在扩散过程中引入自监督重构目标以嵌入抓取性先验——在逆向扩散的每一步，通过中间表征反投影抓取性信息，重构腕部相机图像。仿真与真实机器人实验均表明，本方法显著优于基线方法，并展现出强大的动态抓取能力。

---

### 5. ArtPro: Self-Supervised Articulated Object Reconstruction with Adaptive Integration of Mobility Proposals

- **作者**: Xuelu Li, Zhaonan Wang, Xiaogang Wang, Lei Wu, Manyi Li, Changhe Tu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.22666v1)
- **发表日期**: 2026-02-26
- **匹配关键词**: articulated object, gaussian splatting, 3D gaussian splatting
- **arXiv**: [2602.22666v1](http://arxiv.org/abs/2602.22666v1)
- **📥 PDF**: 已下载至本地 (`2602.22666v1_ArtPro_Self-Supervised_Articulated_Object_Reconstruction_with_Adaptive_Integration_of_Mobility_Propo.pdf`)
- **🔓 开源**: MODEL
- **中文摘要**: 重建高保真数字孪生关节物体对于机器人操控和交互仿真等应用至关重要。当前基于可微分渲染框架（如3D高斯泼溅）的自监督方法仍高度依赖初始部件分割结果，其采用启发式聚类或预训练模型的策略常导致优化陷入局部最优，尤其对于复杂多部件物体。为突破这些局限，我们提出ArtPro——一种引入运动假设自适应整合机制的新型自监督框架。该方法首先通过几何特征与运动先验引导的过分割初始化，生成具有合理运动假设的部件提案。在优化过程中，我们通过分析空间邻域间的运动一致性动态合并提案，同时采用碰撞感知的运动剪枝机制防止错误运动估计。在合成与真实物体数据集上的大量实验表明，ArtPro能稳健重建复杂多部件物体，在精度与稳定性上显著超越现有方法。

---

### 6. Rethinking the Practicality of Vision-language-action Model: A Comprehensive Benchmark and An Improved Baseline

- **作者**: Wenxuan Song, Jiayi Chen, Xiaoquan Sun, Huashuo Lei, Yikai Qin, Wei Zhao, Pengxiang Ding, Han Zhao, Tongxin Wang, Pengxu Hou, Zhide Zhong, Haodong Yan, Donglin Wang, Jun Ma, Haoang Li
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.22663v1)
- **发表日期**: 2026-02-26
- **匹配关键词**: navigation and manipulation, mobile manipulation, VLA, vision-language-action model, vision-language-action, navigation
- **arXiv**: [2602.22663v1](http://arxiv.org/abs/2602.22663v1)
- **📥 PDF**: 已下载至本地 (`2602.22663v1_Rethinking_the_Practicality_of_Vision-language-action_Model_A_Comprehensive_Benchmark_and_An_Improve.pdf`)
- **🔓 开源**: CODE
- **中文摘要**: 视觉-语言-动作（VLA）模型已成为通用机器人智能体的重要发展方向。然而，现有VLA模型普遍面临参数量过大、预训练成本过高以及对多样化机器人形态适应性有限等挑战。为提升VLA模型的实用性，本研究提出了一套综合性基准测试体系与改进型基线模型。首先，我们构建了CEBench基准测试平台，该平台涵盖仿真环境与真实世界的多样化机器人形态，并引入领域随机化设计。我们采集了1.44万条仿真轨迹与1600条专家标注的真实世界轨迹，为CEBench的训练提供数据支持。其次，以CEBench为实验平台，我们系统研究了影响VLA实用性的三个关键维度，并得出若干重要发现。基于这些发现，我们提出了LLaVA-VLA模型——一个专为消费级GPU部署设计的轻量化高性能VLA架构。该架构融合了紧凑型视觉语言模型主干网络，具备多视角感知、本体感觉标记化和动作分块处理能力。为摆脱对昂贵预训练的依赖，LLaVA-VLA采用包含后训练与微调的两阶段训练范式。此外，该模型通过扩展动作空间实现了导航与操作任务的统一处理。跨形态实验验证了LLaVA-VLA的泛化能力与多任务适应性，真实世界移动操作实验则使其成为首个端到端的移动操作VLA模型。本研究承诺在论文录用后将开源全部数据集、代码与模型权重，以促进研究可复现性与后续探索。

---

### 7. Metamorphic Testing of Vision-Language Action-Enabled Robots

- **作者**: Pablo Valle, Sergio Segura, Shaukat Ali, Aitor Arrieta
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.22579v1)
- **发表日期**: 2026-02-26
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2602.22579v1](http://arxiv.org/abs/2602.22579v1)
- **📥 PDF**: 已下载至本地 (`2602.22579v1_Metamorphic_Testing_of_Vision-Language_Action-Enabled_Robots.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型是一种多模态机器人任务控制器，它接收指令和视觉输入后，会生成一系列低级控制动作（或运动指令），使机器人能够在物理环境中执行所要求的任务。这些系统从多个角度面临测试预言问题。一方面，每个指令提示都需要定义测试预言，这是一种复杂且难以泛化的方法。另一方面，当前最先进的预言通常捕捉世界的符号表示（例如机器人和物体的状态），从而能够评估任务的正确性，但无法评估其他关键方面，例如搭载VLA的机器人执行任务的质量。本文探讨了蜕变测试（MT）是否能够缓解这一背景下的测试预言问题。为此，我们提出了两种蜕变关系模式和五种蜕变关系，以评估测试输入的变化是否会影响搭载VLA的机器人的原始轨迹。一项涉及五个VLA模型、两个模拟机器人和四个机器人任务的实证研究表明，MT能够通过自动检测多种类型的故障（包括但不限于未完成的任务）有效缓解测试预言问题。更重要的是，所提出的蜕变关系具有泛化性，使得该方法适用于不同的VLA模型、机器人和任务，即使在缺乏测试预言的情况下也是如此。

---

### 8. SignVLA: A Gloss-Free Vision-Language-Action Framework for Real-Time Sign Language-Guided Robotic Manipulation

- **作者**: Xinyu Tan, Ningwei Bai, Harry Gardener, Zhengyang Zhong, Luoyu Zhang, Liuhaichen Yang, Zhekai Duan, Monkgogi Galeitsiwe, Zezhi Tang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.22514v1)
- **发表日期**: 2026-02-26
- **匹配关键词**: human-robot interaction, vision-language-action, VLA
- **arXiv**: [2602.22514v1](http://arxiv.org/abs/2602.22514v1)
- **📥 PDF**: 已下载至本地 (`2602.22514v1_SignVLA_A_Gloss-Free_Vision-Language-Action_Framework_for_Real-Time_Sign_Language-Guided_Robotic_Man.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 据我们所知，我们首次提出了基于手语驱动的视觉-语言-动作框架，以实现直观且包容的人机交互。与传统依赖注释文本作为中间监督的方法不同，该系统采用无注释文本范式，直接将视觉手语手势映射为语义指令。这一设计降低了标注成本，避免了注释文本表示带来的信息损失，实现了更自然、可扩展的多模态交互。

本研究聚焦于实时字母级指拼交互界面，为机器人控制提供稳健、低延迟的通信通道。与大规模连续手语识别相比，字母级交互在安全关键实体环境中具有更高的可靠性、可解释性和部署可行性。所提出的流程通过几何归一化、时序平滑和词汇优化，将连续手势流转化为连贯的语言指令，确保交互的稳定性和一致性。

此外，该框架设计支持未来集成基于Transformer的无注释文本手语模型，实现可扩展的词汇级和句子级语义理解。实验结果表明，该系统在不同交互场景下能有效将手语指令转化为精确的机器人动作。这些成果彰显了该框架在推动可访问、可扩展、多模态实体智能发展方面的潜力。

---

### 9. VGG-T$^3$: Offline Feed-Forward 3D Reconstruction at Scale

- **作者**: Sven Elflein, Ruilong Li, Sérgio Agostinho, Zan Gojcic, Laura Leal-Taixé, Qunjie Zhou, Aljosa Osep
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.23361v1)
- **发表日期**: 2026-02-26
- **匹配关键词**: 3D reconstruction, 3d reconstruction
- **arXiv**: [2602.23361v1](http://arxiv.org/abs/2602.23361v1)
- **📥 PDF**: 已下载至本地 (`2602.23361v1_VGG-T$^3$_Offline_Feed-Forward_3D_Reconstruction_at_Scale.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出了一种可扩展的三维重建模型，旨在解决离线前馈方法的一个关键局限：其计算与内存需求随输入图像数量呈二次方增长。我们的方法基于一个核心发现：这一瓶颈源于场景几何的可变长度键值空间表示。通过测试时训练，我们将该表示提炼为固定规模的多层感知机。VGG-T$^3$（视觉几何基础测试时训练）模型在处理输入视图时具有线性复杂度，与在线模型类似，仅需$54$秒即可完成对$1k$图像集的重建，相比依赖软注意力机制的基线方法实现了$11.6$倍的加速。由于我们的方法保留了全局场景聚合能力，其点云重建误差显著优于其他线性时间复杂度方法。最后，我们通过使用未见图像查询场景表示，展示了模型在视觉定位方面的能力。

---

### 10. PackUV: Packed Gaussian UV Maps for 4D Volumetric Video

- **作者**: Aashish Rai, Angela Xing, Anushka Agarwal, Xiaoyan Cong, Zekun Li, Tao Lu, Aayush Prakash, Srinath Sridhar
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.23040v1)
- **发表日期**: 2026-02-26
- **匹配关键词**: gaussian splatting
- **arXiv**: [2602.23040v1](http://arxiv.org/abs/2602.23040v1)
- **📥 PDF**: 已下载至本地 (`2602.23040v1_PackUV_Packed_Gaussian_UV_Maps_for_4D_Volumetric_Video.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 体积视频提供了沉浸式的4D体验，但在大规模重建、存储和流式传输方面仍面临挑战。现有基于高斯泼溅的方法虽能实现高质量重建，但在长序列处理、时间一致性保持方面存在不足，且难以应对大幅运动与遮挡解除场景。此外，其输出通常与传统视频编码流程不兼容，限制了实际应用。

我们提出PackUV——一种创新的4D高斯表征方法，将全部高斯属性映射至结构化多尺度UV图集序列，实现紧凑的图像原生存储。为从多视角视频适配该表征，我们开发了PackUV-GS时序一致性拟合方法，直接在UV域优化高斯参数。通过流引导的高斯标记与视频关键帧模块，系统能识别动态高斯元素、稳定静态区域，即使在大幅运动和遮挡解除场景下仍能保持时序连贯性。所得UV图集格式首次实现了与标准视频编解码器（如FFV1）的无损兼容，可在现有多媒体基础设施中实现高效流式传输。

为评估长时体积捕捉性能，我们构建了迄今最大的多视角视频数据集PackUV-2B，包含100个序列共20亿帧画面，配备50余台同步摄像机，涵盖大幅运动与高频遮挡解除场景。大量实验表明，本方法在渲染保真度上超越现有基线，并能以稳定质量扩展至30分钟时长的序列处理。

---

### 11. UCM: Unifying Camera Control and Memory with Time-aware Positional Encoding Warping for World Models

- **作者**: Tianxing Xu, Zixuan Wang, Guangyuan Wang, Li Hu, Zhongyi Zhang, Peng Zhang, Bang Zhang, Song-Hai Zhang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.22960v1)
- **发表日期**: 2026-02-26
- **匹配关键词**: 3D reconstruction, 3d reconstruction
- **arXiv**: [2602.22960v1](http://arxiv.org/abs/2602.22960v1)
- **📥 PDF**: 已下载至本地 (`2602.22960v1_UCM_Unifying_Camera_Control_and_Memory_with_Time-aware_Positional_Encoding_Warping_for_World_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 基于视频生成的世界模型在模拟交互环境方面展现出巨大潜力，但长期面临两大核心挑战：场景重访时难以保持内容一致性，以及无法根据用户输入实现精确的相机控制。现有基于显式三维重建的方法常在无边界场景与精细结构建模中丧失灵活性；而依赖历史生成帧的替代方案因缺乏显式空间对应关系，制约了可控性与一致性。为此，我们提出UCM框架，通过时序感知的位置编码扭曲机制，将长期记忆与精确相机控制相统一。为降低计算开销，我们设计了高效的双流扩散Transformer以实现高保真生成。此外，我们提出基于点云渲染的可扩展数据构建策略，模拟场景重访过程，成功在超过50万段单目视频上完成训练。在真实场景与合成数据集上的大量实验表明，UCM在长期场景一致性方面显著优于现有先进方法，同时在高保真视频生成中实现了精确的相机控制能力。

---

### 12. BetterScene: 3D Scene Synthesis with Representation-Aligned Generative Model

- **作者**: Yuci Han, Charles Toth, John E. Anderson, William J. Shuart, Alper Yilmaz
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.22596v1)
- **发表日期**: 2026-02-26
- **匹配关键词**: 3D gaussian splatting, gaussian splatting
- **arXiv**: [2602.22596v1](http://arxiv.org/abs/2602.22596v1)
- **📥 PDF**: 已下载至本地 (`2602.22596v1_BetterScene_3D_Scene_Synthesis_with_Representation-Aligned_Generative_Model.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出BetterScene方法，通过使用极稀疏、无约束的照片来提升多样化真实场景的新视角合成质量。该方法以经过数十亿帧预训练、具备生产就绪性的稳定视频扩散模型为强大骨干网络，旨在推理阶段减少伪影并恢复视角一致的细节。传统方法已开发出类似的基于扩散模型的解决方案来应对新视角合成的这些挑战。尽管已有显著改进，这些方法通常依赖现成的预训练扩散先验，仅对UNet模块进行微调而保持其他组件冻结，即使在引入深度或语义条件等几何感知正则化后，仍会导致细节不一致和伪影问题。为此，我们深入研究了扩散模型的潜在空间，并引入两个核心组件：(1)时间等变性正则化与(2)视觉基础模型对齐表征，二者均应用于稳定视频扩散流程中的变分自编码器模块。BetterScene整合了前馈式3D高斯溅射模型，通过渲染特征作为稳定视频扩散增强器的输入，从而生成连续、无伪影且保持视角一致性的新视图。我们在具有挑战性的DL3DV-10K数据集上进行评估，结果表明该方法相较于现有先进技术展现出更优越的性能。

---

### 13. GSTurb: Gaussian Splatting for Atmospheric Turbulence Mitigation

- **作者**: Hanliang Du, Zhangji Lu, Zewei Cai, Qijian Tang, Qifeng Yu, Xiaoli Liu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.22800v1)
- **发表日期**: 2026-02-26
- **匹配关键词**: gaussian splatting
- **arXiv**: [2602.22800v1](http://arxiv.org/abs/2602.22800v1)
- **📥 PDF**: 已下载至本地 (`2602.22800v1_GSTurb_Gaussian_Splatting_for_Atmospheric_Turbulence_Mitigation.pdf`)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/DuhlLiamz/3DGS_turbulence/tree/main.
- **中文摘要**: 大气湍流会导致像素位移（倾斜）和模糊，从而显著降低图像质量，尤其在远距离成像应用中尤为明显。本文提出了一种新颖的大气湍流抑制框架GSTurb，该框架结合了光流引导的倾斜校正与高斯泼溅技术，用于建模非等晕模糊。该框架利用高斯参数表示倾斜和模糊，并通过多帧优化来提升图像恢复效果。在ATSyn-static数据集上的实验结果表明，本方法具有显著效果，峰值PSNR达到27.67 dB，SSIM为0.8735。与现有最优方法相比，GSTurb将PSNR提升了1.3 dB（增幅4.5%），SSIM提升了0.048（增幅5.8%）。此外，在包括TSRWGAN Real-World和CLEAR在内的真实数据集上，GSTurb均优于现有方法，在定性和定量性能上均展现出显著提升。这些结果证明，结合光流引导的倾斜校正与高斯泼溅技术，能有效增强合成及真实湍流条件下的图像恢复效果。本方法的代码将在https://github.com/DuhlLiamz/3DGS_turbulence/tree/main 公开。

---

### 14. Sapling-NeRF: Geo-Localised Sapling Reconstruction in Forests for Ecological Monitoring

- **作者**: Miguel Ángel Muñoz-Bañón, Nived Chebrolu, Sruthi M. Krishna Moorthy, Yifu Tao, Fernando Torres, Roberto Salguero-Gómez, Maurice Fallon ⭐
  - **高亮作者**: Maurice Fallon
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.22731v1)
- **发表日期**: 2026-02-26
- **匹配关键词**: 3D gaussian splatting, nerf, neural radiance field, gaussian splatting, 3D reconstruction, 3d reconstruction
- **arXiv**: [2602.22731v1](http://arxiv.org/abs/2602.22731v1)
- **📥 PDF**: 已下载至本地 (`2602.22731v1_Sapling-NeRF_Geo-Localised_Sapling_Reconstruction_in_Forests_for_Ecological_Monitoring.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 幼苗是森林再生和整体健康状况的关键指标。然而，现有三维传感方法难以捕捉其精细尺度的结构特征，导致定量评估困难。地面激光扫描仪、移动激光扫描仪或传统摄影测量方法在重建细枝和茂密叶片方面效果不佳，且缺乏长期监测所需的尺度一致性。神经辐射场和三维高斯溅射等隐式三维重建方法虽前景广阔，但无法恢复场景的真实尺度，且缺乏精确地理定位手段。本文提出一种融合神经辐射场、激光雷达同步定位与建图及全球导航卫星系统的技术流程，实现对幼苗可重复、可地理定位的生态监测。该系统采用三级表征框架：（一）利用全球导航卫星系统实现粗略的地球坐标系定位；（二）基于激光雷达的同步定位与建图技术实现厘米级精确定位与重建；（三）通过神经辐射场生成以单株幼苗为中心的高密度重建模型。该方法支持对幼苗性状进行可重复的定量评估与长期监测。在英国牛津怀瑟姆森林和芬兰埃沃森林样地的实验表明，相较于地面激光扫描仪，本系统能更精确地获取茎干高度、分枝模式和叶木比等参数。我们证实可对0.5米至2米高的幼苗进行原位精确测量，获取茎干骨架结构与叶片分布数据，为生态学家分析森林动态提供更丰富的结构性与定量化数据支撑。

---

## 📌 Poster

*其他相关研究*

---

### 1. Evaluating Zero-Shot and One-Shot Adaptation of Small Language Models in Leader-Follower Interaction

- **作者**: Rafael R. Baptista, André de Lima Salgado, Ricardo V. Godoy, Marcelo Becker, Thiago Boaventura, Gustavo J. G. Lahr
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.23312v1)
- **发表日期**: 2026-02-26
- **匹配关键词**: human-robot interaction, HRI
- **arXiv**: [2602.23312v1](http://arxiv.org/abs/2602.23312v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 领导者-跟随者交互是人机交互（HRI）中的重要范式。然而，对于资源受限的移动辅助机器人而言，实时分配角色仍具挑战性。虽然大语言模型（LLMs）在自然交流方面展现出潜力，但其模型规模与延迟问题限制了在设备端的部署。小语言模型（SLMs）提供了潜在的替代方案，但其在人机交互角色分类中的有效性尚未得到系统评估。本文提出了面向领导者-跟随者交流的小语言模型基准测试，通过已发布数据库构建并辅以合成样本增强，创建了能捕捉交互动态特征的新数据集。我们研究了两种适应策略：提示工程与微调，在零样本和单样本交互模式下与未经训练的基线模型进行对比。基于Qwen2.5-0.5B模型的实验表明，零样本微调在保持低延迟（每样本22.2毫秒）的同时实现了稳健的分类性能（准确率86.66%），显著优于基线方法和提示工程策略。但研究也发现单样本模式下存在性能下降现象，这源于增长的上文长度对模型架构容量的挑战。这些发现证明，经过微调的小语言模型能为直接角色分配提供有效解决方案，同时揭示了边缘计算中对话复杂度与分类可靠性之间的关键权衡关系。

---

### 2. SPARR: Simulation-based Policies with Asymmetric Real-world Residuals for Assembly

- **作者**: Yijie Guo, Iretiayo Akinola, Lars Johannsmeier, Hugo Hadfield, Abhishek Gupta, Yashraj Narang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.23253v1)
- **发表日期**: 2026-02-26
- **匹配关键词**: contact-rich manipulation
- **arXiv**: [2602.23253v1](http://arxiv.org/abs/2602.23253v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 机器人装配因其对精确、密集接触操作的要求而长期面临挑战。基于仿真的学习方法虽能开发出稳健的装配策略，但由于仿真与现实的差异，这些策略在实际部署时性能往往下降。相反，现实世界中的强化学习方法虽避免了仿真与现实的差异，却严重依赖人工监督，且对环境变化的泛化能力不足。本研究提出一种混合方法，将仿真训练的基础策略与现实世界的残差策略相结合，以高效适应现实世界的变化。基础策略在仿真环境中通过低层状态观测和密集奖励进行训练，为初始行为提供强先验。残差策略则在现实世界中通过视觉观测和稀疏奖励进行学习，以补偿动力学和传感器噪声的差异。大量现实世界实验表明，我们提出的SPARR方法在多种双部件装配任务中实现了接近完美的成功率。与当前最先进的零样本仿真到现实方法相比，SPARR将成功率提高了38.4%，同时将循环时间减少了29.7%。此外，与严重依赖人工监督的先进现实世界强化学习方法不同，SPARR无需人工专业知识。

---

### 3. Grasp, Slide, Roll: Comparative Analysis of Contact Modes for Tactile-Based Shape Reconstruction

- **作者**: Chung Hee Kim, Shivani Kamtikar, Tye Brady, Taskin Padir, Joshua Migdal
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.23206v1)
- **发表日期**: 2026-02-26
- **匹配关键词**: exploration
- **arXiv**: [2602.23206v1](http://arxiv.org/abs/2602.23206v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 触觉感知使机器人能够通过物理交互获取物体的详细几何信息，从而对基于视觉的方法形成补充。然而，由于物理接触耗时较长，且需要策略性地选择既能最大化信息增益又能最小化物理交互的接触位置，高效获取有用的触觉数据仍然具有挑战性。本文研究了使用具备触觉功能的灵巧手爪时，不同接触模式如何影响物体形状重建。我们比较了三种接触交互模式：抓握释放、手指滑动引起的滑动以及手掌滚动。这些接触模式与信息论探索框架相结合，该框架利用形状补全模型指导后续采样位置。我们的研究结果表明，手指滑动和手掌滚动模式提升了触觉感知效率，从而实现了更快的形状重建收敛速度，在减少34%物理交互的同时将重建精度提高了55%。我们使用配备Inspire-Robots灵巧手爪的UR5e机器人手臂验证了该方法，在基础几何形状物体上均表现出鲁棒性能。

---

### 4. Towards Intelligible Human-Robot Interaction: An Active Inference Approach to Occluded Pedestrian Scenarios

- **作者**: Kai Chen, Yuyao Huang, Guang Chen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.23109v1)
- **发表日期**: 2026-02-26
- **匹配关键词**: human-robot interaction
- **arXiv**: [2602.23109v1](http://arxiv.org/abs/2602.23109v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 被遮挡行人的突然出现是自动驾驶领域面临的关键安全挑战。基于规则的传统方法或纯数据驱动方法难以应对这类长尾场景固有的高度不确定性。为应对这一挑战，我们提出了一种基于主动推理的新型框架，赋予智能体类人的信念驱动机制。该框架利用Rao-Blackwellized粒子滤波器高效估计行人的混合状态。为模拟人类在不确定性下的认知过程，我们引入条件信念重置机制和假设注入技术，显式建模对行人多重潜在意图的信念。规划通过交叉熵方法增强的模型预测路径积分控制器实现，该方法融合了交叉熵方法的高效迭代搜索与模型预测路径积分固有的鲁棒性。仿真实验表明，相较于反应式、基于规则及强化学习的基线方法，我们的方法显著降低了碰撞率，同时展现出可解释的类人驾驶行为，反映了智能体的内部信念状态。

---

### 5. Marinarium: a New Arena to Bring Maritime Robotics Closer to Shore

- **作者**: Ignacio Torroba, David Dorner, Victor Nan Fernandez-Ayala, Mart Kartasev, Joris Verhagen, Elias Krantz, Gregorio Marchesini, Carl Ljung, Pedro Roque, Chelsea Sidrane, Linda Van der Spaa, Nicola De Carli, Petter Ogren, Christer Fuglesang, Jana Tumova, Dimos V. Dimarogonas, Ivan Stenius
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.23053v1)
- **发表日期**: 2026-02-26
- **匹配关键词**: navigation
- **arXiv**: [2602.23053v1](http://arxiv.org/abs/2602.23053v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 本文介绍Marinarium——一个模块化、独立运行的水下研究设施，旨在以资源高效的方式为海事及空间模拟机器人实验提供真实测试平台。该设施集成了全仪器化水下与空中作业空间（可通过可伸缩顶棚扩展至真实天气环境）、SMaRCSim模拟器中的数字孪生系统，并与空间机器人实验室实现深度集成。这些设计均致力于弥合仿真验证、实验室测试与实地作业之间的鸿沟。通过对比现有同类基础设施，我们阐述了该设施如何支撑野外机器人学四大开放研究领域的实验体系：首先利用水池高保真动力学数据，展示基于学习的系统辨识方法在水下航行器应用的潜力；继而通过跨水下、水面、空中的异构机器人集群交会任务，突显多域作业空间的通用性；随后说明如何运用数字孪生技术缩小水下仿真与现实差距；最后通过在平面空间机器人模拟器与中性浮力遥控潜水器上执行时空一致的检测任务，验证水下替代平台在航天器导航验证中的潜力。本研究通过分享Marinarium的设计建造理念与实践经验，旨在为野外机器人学界提供弥合受控环境与真实海上/空间机器人实验间差距的范式参考。

---

### 6. InCoM: Intent-Driven Perception and Structured Coordination for Whole-Body Mobile Manipulation

- **作者**: Jiahao Liu, Cui Wenbo, Haoran Li, Dongbin Zhao
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2602.23024v1)
- **发表日期**: 2026-02-26
- **匹配关键词**: mobile manipulation
- **arXiv**: [2602.23024v1](http://arxiv.org/abs/2602.23024v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 全身移动操控是通用机器人智能体的基础能力，既需要协调控制移动底盘与机械臂，又要在动态变化的视角下保持鲁棒的感知能力。然而现有方法面临两大挑战：底盘与机械臂动作的强耦合性使全身控制优化复杂化，且在移动操控过程中视角变化常导致感知注意力分配失当。我们提出InCoM——一种面向全身移动操控的意图驱动感知与结构化协调框架。该框架通过推断潜在运动意图动态重加权多尺度感知特征，实现阶段性自适应感知注意力分配。为支撑鲁棒的跨模态感知，InCoM进一步引入几何-语义结构化对齐机制以增强多模态对应关系。在控制层面，我们设计了解耦协调流匹配动作解码器，显式建模协调的底盘-机械臂动作生成过程，缓解控制耦合导致的优化难题。在未使用特权感知信息的情况下，InCoM在三个ManiSkill-HAB场景中的成功率分别超越现有最优方法28.2%、26.1%和23.6%，展现出卓越的全身移动操控效能。

---

