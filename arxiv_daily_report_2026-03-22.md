# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-03-22 08:04

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 4/20 篇提供

**🌟 Highlight**: 20 篇 | **📌 Poster**: 0 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models

- **作者**: Bryce Grant, Xijia Zhao, Peng Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.19233v1)
- **发表日期**: 2026-03-19
- **匹配关键词**: VLA, vision-language-action model, exploration, vision-language-action
- **arXiv**: [2603.19233v1](http://arxiv.org/abs/2603.19233v1)
- **📥 PDF**: 已下载至本地 (`2603.19233v1_Not_All_Features_Are_Created_Equal_A_Mechanistic_Study_of_Vision-Language-Action_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型将感知、语言和运动控制整合于单一架构，但其如何将多模态输入转化为动作的机制尚不明确。本研究在四个基准测试的394,000+次推演中，对六款参数量级跨越8000万至70亿的模型应用了激活注入、稀疏自编码器（SAEs）和线性探针分析。研究发现：在所有架构中，视觉通路主导动作生成——向无提示推演注入基线激活可复现近乎一致的行为，而跨任务注入则引导机器人朝向源任务位置（X-VLA推演中99.8%与源轨迹吻合），揭示了与场景坐标而非抽象任务表征绑定的空间运动程序。语言敏感性取决于任务结构而非模型设计：当视觉上下文能唯一确定任务时语言被忽略；当多目标共享场景时语言变得关键（X-VLA在错误提示下：\texttt{libero\_goal}任务准确率从94%降至10%，而\texttt{libero\_object}任务保持60-100%）。在三种多通路架构（\pizhalf{}、SmolVLA、GR00T）中，专家通路编码运动程序，而视觉语言模型通路编码目标语义（专家注入引起的行为偏移量是后者的2倍），子空间注入证实二者占据可分离的激活子空间。尽管均值池化能提升X-VLA的动作保真度，但多数架构需要逐令牌SAE处理来保证动作精确性。对比识别技术复原了82个以上操作概念，因果消融实验显示敏感性指标的零效应率在28%-92%间波动，且与表征宽度无关。我们发布\textbf{Action Atlas}平台（https://action-atlas.com），支持对六款模型VLA表征的交互式探索。

---

### 2. MonoArt: Progressive Structural Reasoning for Monocular Articulated 3D Reconstruction

- **作者**: Haitian Li, Haozhe Xie, Junxiang Xu, Beichen Wen, Fangzhou Hong, Ziwei Liu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.19231v1)
- **发表日期**: 2026-03-19
- **匹配关键词**: 3d reconstruction, 3D reconstruction
- **arXiv**: [2603.19231v1](http://arxiv.org/abs/2603.19231v1)
- **📥 PDF**: 已下载至本地 (`2603.19231v1_MonoArt_Progressive_Structural_Reasoning_for_Monocular_Articulated_3D_Reconstruction.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 从单张图像重建铰接式三维物体需要从有限的视觉证据中联合推断物体几何、部件结构及运动参数。核心难点在于运动线索与物体结构的相互纠缠，这使得直接回归铰接参数变得不稳定。现有方法通过多视角监督、基于检索的组装或辅助视频生成来解决这一挑战，但往往以牺牲可扩展性或效率为代价。我们提出MonoArt框架，该框架基于渐进式结构推理构建统一架构。不同于直接从图像特征预测铰接参数，MonoArt在单一架构内逐步将视觉观测转化为规范几何、结构化部件表示和运动感知嵌入。这种结构化推理过程实现了稳定且可解释的铰接推断，无需依赖外部运动模板或多阶段流程。在PartNet-Mobility数据集上的大量实验表明，该方法在重建精度和推理速度上均达到最先进水平。该框架可进一步推广至机器人操作和铰接式场景重建任务。

---

### 3. NavTrust: Benchmarking Trustworthiness for Embodied Navigation

- **作者**: Huaide Jiang, Yash Chaudhary, Yuping Wang, Zehao Wang, Raghav Sharma, Manan Mehta, Yang Zhou, Lichao Sun, Zhiwen Fan, Zhengzhong Tu, Jiachen Li
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.19229v1)
- **发表日期**: 2026-03-19
- **匹配关键词**: VLN, navigation, object-goal navigation
- **arXiv**: [2603.19229v1](http://arxiv.org/abs/2603.19229v1)
- **📥 PDF**: 已下载至本地 (`2603.19229v1_NavTrust_Benchmarking_Trustworthiness_for_Embodied_Navigation.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://navtrust.github.io.
- **中文摘要**: 具身导航主要分为两大类：视觉语言导航（VLN），即智能体通过遵循自然语言指令进行导航；以及目标物体导航（OGN），即智能体导航至指定目标物体。然而，现有研究主要在理想条件下评估模型性能，忽视了现实场景中可能出现的干扰因素。为填补这一空白，我们提出了NavTrust——一个统一的基准测试框架，该系统在真实场景中系统性地对RGB图像、深度信息和指令等输入模态进行干扰处理，并评估其对导航性能的影响。据我们所知，NavTrust是首个在统一框架下对具身导航智能体施加多样化RGB-深度干扰及指令变体的基准测试。通过对七种前沿方法进行广泛评估，我们发现这些方法在现实干扰下均出现显著性能下降，这揭示了当前系统在鲁棒性方面存在的关键缺陷，并为构建更可信赖的具身导航系统提供了改进方向。此外，我们系统评估了四种不同的增强策略，以提升模型对RGB-深度干扰及指令干扰的鲁棒性。我们的基础模型包括Uni-NaVid和ETPNav。通过在真实移动机器人上的部署测试，我们观察到模型对干扰的鲁棒性得到有效提升。项目网站地址为：https://navtrust.github.io。

---

### 4. FASTER: Rethinking Real-Time Flow VLAs

- **作者**: Yuxiang Lu, Zhe Liu, Xianzhe Fan, Zhenya Yang, Jinghua Hou, Junyi Li, Kaixin Ding, Hengshuang Zhao
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.19199v1)
- **发表日期**: 2026-03-19
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2603.19199v1](http://arxiv.org/abs/2603.19199v1)
- **📥 PDF**: 已下载至本地 (`2603.19199v1_FASTER_Rethinking_Real-Time_Flow_VLAs.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 实时执行对于在物理世界中部署视觉-语言-动作（VLA）模型至关重要。现有的异步推理方法主要优化轨迹平滑度，却忽视了响应环境变化的关键延迟问题。本文通过重新审视动作分块策略中的反应机制，系统分析了影响反应时间的因素。研究表明，反应时间遵循由首次动作时间（TTFA）与执行视野共同决定的均匀分布。进一步发现，在基于流的VLA模型中采用恒定调度方案的传统做法效率低下，迫使系统在开始任何动作前必须完成所有采样步骤，从而形成反应延迟的瓶颈。为突破这一限制，我们提出了即时反应快速动作采样（FASTER）方法。通过引入视野感知调度机制，FASTER在流采样过程中自适应地优先处理近期动作，将即时反应的去噪过程压缩十倍（如在$π_{0.5}$和X-VLA模型中）至单步完成，同时保持长视野轨迹的质量。结合流式客户端-服务器架构，FASTER显著降低了实际机器人系统的有效反应延迟，尤其在消费级GPU部署场景中表现突出。包括高动态乒乓球任务在内的真实世界实验证明，FASTER为通用策略提供了前所未有的实时响应能力，能够快速生成精准流畅的运动轨迹。

---

### 5. Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models

- **作者**: Aiden Swann, Lachlain McGranahan, Hugo Buurmeijer, Monroe Kennedy, Mac Schwager
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.19183v1)
- **发表日期**: 2026-03-19
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2603.19183v1](http://arxiv.org/abs/2603.19183v1)
- **📥 PDF**: 已下载至本地 (`2603.19183v1_Sparse_Autoencoders_Reveal_Interpretable_and_Steerable_Features_in_VLA_Models.pdf`)
- **🔓 开源**: PROJECT_PAGE, CODE
  - 链接：http://drvla.github.io
- **中文摘要**: 视觉-语言-动作（VLA）模型已成为通用机器人操作领域的一种前景广阔的方法。然而，其泛化能力并不稳定：虽然这些模型在某些场景下表现优异，但经过微调的变体在面对新物体、新场景和新指令时常常失效。我们运用机制可解释性技术来深入理解VLA模型的内在运作机制。为探究内部表征，我们在VLA隐藏层激活上训练稀疏自编码器（SAE）。SAE学习到一个稀疏字典，其特征作为模型计算的紧凑且可解释的基础。我们发现，提取的SAE特征绝大多数对应于特定训练演示中的记忆序列。然而，部分特征对应着可解释、通用且可操控的运动基元与语义属性，为VLA的泛化能力提供了令人期待的研究视角。我们提出一种度量标准，根据特征是否代表可泛化的可迁移基元或特定情节的记忆来对其进行分类。通过在LIBERO基准测试中的操控实验，我们验证了这些发现。实验表明，单个SAE特征能够因果性地影响机器人行为。操控通用特征可诱导出与其语义一致的行为，并能跨任务和场景应用。这项工作首次从机制层面证明VLA能够学习跨任务和场景的泛化特征。我们观察到，在小规模机器人数据集上进行监督微调会不成比例地放大记忆效应。相比之下，在更大规模、更多样化的数据集（如DROID）上训练或采用知识隔离方法能促进更通用特征的形成。我们提供了开源代码库和用户友好界面，用于激活收集、SAE训练和特征操控。项目页面位于http://drvla.github.io。

---

### 6. From Inference Efficiency to Embodied Efficiency: Revisiting Efficiency Metrics for Vision-Language-Action Models

- **作者**: Zhuofan Li, Hongkun Yang, Zhenyang Chen, Yangxuan Chen, Yingyan, Lin, Chaojian Li
- **单位**: Celine; Celine; Celine...
- **发表日期**: 2026-03-19
- **匹配关键词**: VLA, vision-language-action model, vision-language-action
- **arXiv**: [2603.19131v1](http://arxiv.org/abs/2603.19131v1)
- **📥 PDF**: 已下载至本地 (`2603.19131v1_From_Inference_Efficiency_to_Embodied_Efficiency_Revisiting_Efficiency_Metrics_for_Vision-Language-A.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型近年来通过联合推理视觉、语言和运动模态，使具身智能体能够执行日益复杂的任务。然而，我们发现当前VLA研究中以参数量、浮点运算量或解码吞吐量为表征的“效率”概念，并不能反映其在机器人平台上的实际性能。在现实执行中，效率由系统级具身行为决定，例如任务完成时间、轨迹平滑度、累积关节旋转量和运动能耗。通过对模型压缩、令牌稀疏化和动作序列压缩的对照研究，我们得出若干挑战常规认知的观察：（1）在传统指标下减少计算量的方法，尽管能维持任务成功率，却往往增加端到端执行成本或降低运动质量；（2）系统级具身效率指标揭示了传统评估中隐藏的学习动作策略性能差异；（3）常见的适应方法（如上下文提示或监督微调）对具身效率的提升有限且具有指标特异性。虽然这些方法能降低特定具身效率指标（如急动度或动作频率），但获得的收益可能以其他指标（如更长的完成时间）为代价。综合来看，我们的研究表明传统推理效率指标可能忽略具身执行的重要方面。引入具身效率评估能够更全面地反映策略行为与实际性能，为VLA模型提供更公平、更全面的比较基准。

---

### 7. GHOST: Fast Category-agnostic Hand-Object Interaction Reconstruction from RGB Videos using Gaussian Splatting

- **作者**: Ahmed Tawfik Aboukhadra, Marcel Rogge, Nadia Robertini, Abdalla Arafa, Jameel Malik, Ahmed Elhayek, Didier Stricker
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.18912v1)
- **发表日期**: 2026-03-19
- **匹配关键词**: gaussian splatting, 3d reconstruction, 3D reconstruction
- **arXiv**: [2603.18912v1](http://arxiv.org/abs/2603.18912v1)
- **📥 PDF**: 已下载至本地 (`2603.18912v1_GHOST_Fast_Category-agnostic_Hand-Object_Interaction_Reconstruction_from_RGB_Videos_using_Gaussian_S.pdf`)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/ATAboukhadra/GHOST.
- **中文摘要**: 从单目RGB视频中理解真实的手部-物体交互对于增强现实/虚拟现实、机器人技术和具身人工智能至关重要。现有方法依赖于特定类别的模板或大量计算，但在三维空间中仍会产生物理不一致的手部-物体对齐。我们提出GHOST（高斯手部-物体溅射）框架，这是一种快速、类别无关的框架，利用二维高斯溅射技术重建动态手部-物体交互。GHOST将手部和物体表示为密集且视角一致的高斯圆盘，并引入三项关键创新：（1）几何先验检索与一致性损失函数，用于补全被遮挡的物体区域；（2）抓取感知对齐机制，优化手部平移与物体尺度以确保真实接触；（3）手部感知背景损失函数，避免对受手部遮挡的物体区域进行惩罚。GHOST仅需单段RGB视频即可实现完整、物理一致且可动画化的重建，其运行速度比现有类别无关方法快一个数量级。在ARCTIC、HO3D及野外数据集上的大量实验表明，该方法在三维重建精度和二维渲染质量方面均达到最先进水平，确立了GHOST作为真实手部-物体交互建模的高效稳健解决方案。代码发布于https://github.com/ATAboukhadra/GHOST。

---

### 8. Empathetic Motion Generation for Humanoid Educational Robots via Reasoning-Guided Vision--Language--Motion Diffusion Architecture

- **作者**: Fuze Sun, Lingyu Li, Lekan Dai, Xinyu Fan
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.18771v1)
- **发表日期**: 2026-03-19
- **匹配关键词**: human-robot interaction
- **arXiv**: [2603.18771v1](http://arxiv.org/abs/2603.18771v1)
- **📥 PDF**: 已下载至本地 (`2603.18771v1_Empathetic_Motion_Generation_for_Humanoid_Educational_Robots_via_Reasoning-Guided_Vision--Language--.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 本文提出一种推理引导的视觉-语言-动作扩散框架（RG-VLMD），用于在教育场景中为人形机器人生成指令感知的伴随语音手势。该系统整合了多模态情感估计、教学推理和教学行为条件化动作合成，以实现自适应且语义一致的机器人行为。通过门控专家混合模型从输入文本、视觉和声学特征中预测情感效价/唤醒度，随后经由情感驱动策略映射至离散的教学行为类别。这些信号通过添加潜在约束与辅助动作组监督，以片段级意图和帧级教学调度为条件，驱动基于扩散的动作生成器。与基线扩散模型相比，所提方法能生成更具结构性和区分度的动作模式，运动静态分析与成对距离验证均证实了该优势。生成的动作序列保持物理合理性，并可重定向至NAO机器人实现实时执行。结果表明，推理引导的教学条件化机制能有效提升教育人机交互中手势的可控性与教学表现力。

---

### 9. Scaling Sim-to-Real Reinforcement Learning for Robot VLAs with Generative 3D Worlds

- **作者**: Andrew Choi, Xinjie Wang, Zhizhong Su, Wei Xu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.18532v1)
- **发表日期**: 2026-03-19
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2603.18532v1](http://arxiv.org/abs/2603.18532v1)
- **📥 PDF**: 已下载至本地 (`2603.18532v1_Scaling_Sim-to-Real_Reinforcement_Learning_for_Robot_VLAs_with_Generative_3D_Worlds.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 大型视觉语言模型（VLM）通过强化学习（RL）训练展现出的优异性能，推动了在机器人领域采用类似方法对视觉-语言-动作（VLA）模型进行微调的研究。近期许多工作直接在现实世界中对VLA模型进行微调，以避免处理仿真到现实的差异问题。虽然现实世界中的强化学习规避了仿真到现实的挑战，但它本质上限制了所得VLA模型的泛化能力，因为在物理世界中扩展场景和物体的多样性极其困难。这导致了一个矛盾的结果：将经过广泛预训练的模型转变为一个过度拟合、仅适用于特定场景的策略。相比之下，在仿真环境中训练可以提供多样化的场景，但设计这些场景同样成本高昂。本研究证明，通过利用三维世界生成模型，可以在不牺牲泛化能力且减少人工成本的情况下对VLA模型进行强化学习微调。结合语言驱动的场景设计工具，我们生成了数百个包含独特物体和背景的多样化交互场景，实现了可扩展且高度并行的策略学习。从预训练的模仿基线出发，我们的方法将仿真成功率从9.7%提升至79.8%，同时任务完成时间缩短了1.25倍。通过生成高质量数字孪生结合领域随机化技术，我们进一步展示了成功的仿真到现实迁移能力，将现实世界成功率从21.7%提高到75%，并实现了1.13倍的加速。最后，我们通过消融实验进一步强调了利用三维世界生成模型近乎无限数据资源的优势，结果表明增加场景多样性直接提升了零样本泛化能力。

---

### 10. OnlinePG: Online Open-Vocabulary Panoptic Mapping with 3D Gaussian Splatting

- **作者**: Hongjia Zhai, Qi Zhang, Xiaokun Pan, Xiyu Zhang, Yitong Dong, Huaqi Zhang, Dan Xu, Guofeng Zhang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.18510v1)
- **发表日期**: 2026-03-19
- **匹配关键词**: gaussian splatting, 3D gaussian splatting
- **arXiv**: [2603.18510v1](http://arxiv.org/abs/2603.18510v1)
- **📥 PDF**: 已下载至本地 (`2603.18510v1_OnlinePG_Online_Open-Vocabulary_Panoptic_Mapping_with_3D_Gaussian_Splatting.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 基于在线全景映射的开放词汇场景理解对于具身应用感知和交互环境至关重要。然而，现有方法多为离线系统或缺乏实例级理解能力，限制了其在现实机器人任务中的适用性。本文提出OnlinePG系统，这是一种创新且高效的解决方案，通过在线环境下的3D高斯泼溅技术，实现了几何重建与开放词汇感知的深度融合。技术上，为实现在线全景映射，我们采用滑动窗口下的高效局部到全局处理范式。在构建局部一致性地图时，我们设计了融合几何与语义线索的3D片段聚类图，将滑动窗口内不一致的片段整合为完整实例。随后，通过为局部3D高斯地图构建具有空间属性的显式网格，并借助鲁棒的双向二分3D高斯实例匹配机制，将其融合至全局地图。最终，我们利用3D空间属性网格内融合的视觉语言模型特征实现开放词汇场景理解。在多个主流数据集上的大量实验表明，本方法在保持实时效率的同时，在在线方法中取得了更优的性能表现。

---

### 11. Matryoshka Gaussian Splatting

- **作者**: Zhilin Guo, Boqiao Zhang, Hakan Aktas, Kyle Fogarty, Jeffrey Hu, Nursena Koprucu Aslan, Wenzhao Li, Canberk Baykal, Albert Miao, Josef Bengtson, Chenliang Zhou, Weihao Xia, Cristina Nader Vasconcelos. Cengiz Oztireli
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.19234v1)
- **发表日期**: 2026-03-19
- **匹配关键词**: gaussian splatting, 3D gaussian splatting
- **arXiv**: [2603.19234v1](http://arxiv.org/abs/2603.19234v1)
- **📥 PDF**: 已下载至本地 (`2603.19234v1_Matryoshka_Gaussian_Splatting.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 从单一模型实现可调节保真度的场景渲染能力，即细节层次（LoD），对于三维高斯溅射（3DGS）的实际部署至关重要。现有离散LoD方法仅提供有限的操作点选择，而同期提出的连续LoD方法虽能实现更平滑的缩放，但在全容量渲染时往往出现明显质量下降，使得LoD成为代价高昂的设计决策。我们提出套娃式高斯溅射（MGS），这是一种训练框架，可在不牺牲全容量渲染质量的前提下，为标准3DGS流程实现连续LoD。MGS通过训练获得一组有序的高斯分布集合，使得渲染任意前缀（即前k个溅射点）都能生成连贯的重建结果，其保真度随预算增加而平滑提升。我们的核心思想是随机预算训练：每次迭代采样随机溅射预算，同时优化对应前缀和完整集合。该策略仅需两次前向传播且无需修改架构。在四个基准测试和六个基线模型上的实验表明，MGS在保持主干网络全容量性能的同时，实现了单一模型下连续的速度-质量权衡。对排序策略、训练目标和模型容量的广泛消融实验进一步验证了设计有效性。

---

### 12. DriveTok: 3D Driving Scene Tokenization for Unified Multi-View Reconstruction and Understanding

- **作者**: Dong Zhuo, Wenzhao Zheng, Sicheng Zuo, Siming Yan, Lu Hou, Jie Zhou, Jiwen Lu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.19219v1)
- **发表日期**: 2026-03-19
- **匹配关键词**: vision-language-action model, vision-language-action
- **arXiv**: [2603.19219v1](http://arxiv.org/abs/2603.19219v1)
- **📥 PDF**: 已下载至本地 (`2603.19219v1_DriveTok_3D_Driving_Scene_Tokenization_for_Unified_Multi-View_Reconstruction_and_Understanding.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 随着视觉-语言-动作模型与世界模型在自动驾驶系统中的日益广泛应用，可扩展的图像标记化技术作为视觉模态的接口变得至关重要。然而，现有标记器大多针对单目二维场景设计，应用于高分辨率多视角驾驶场景时存在效率低下与视角间不一致的问题。为此，我们提出DriveTok——一种面向统一多视角重建与理解的高效三维驾驶场景标记器。DriveTok首先从视觉基础模型中提取语义丰富的视觉特征，随后通过三维可变形交叉注意力机制将其转化为场景标记。在解码阶段，我们采用多视角变换器从场景标记重建多视角特征，并通过多头机制实现RGB图像、深度信息及语义内容的重建。此外，我们在场景标记上直接添加三维头部进行三维语义占据预测，以增强空间感知能力。通过多任务训练目标，DriveTok学习到融合语义、几何与纹理信息的统一场景标记，实现高效的多视角标记化。在广泛使用的nuScenes数据集上的大量实验表明，DriveTok生成的场景标记在图像重建、语义分割、深度预测及三维占据预测任务中均表现出优异性能。

---

### 13. Reconstruction Matters: Learning Geometry-Aligned BEV Representation through 3D Gaussian Splatting

- **作者**: Yiren Lu, Xin Ye, Burhaneddin Yaman, Jingru Luo, Zhexiao Xiong, Liu Ren, Yu Yin
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.19193v1)
- **发表日期**: 2026-03-19
- **匹配关键词**: gaussian splatting, 3d reconstruction, 3D reconstruction, 3D gaussian splatting
- **arXiv**: [2603.19193v1](http://arxiv.org/abs/2603.19193v1)
- **📥 PDF**: 已下载至本地 (`2603.19193v1_Reconstruction_Matters_Learning_Geometry-Aligned_BEV_Representation_through_3D_Gaussian_Splatting.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 鸟瞰图（BEV）感知是自动驾驶的基石，它通过融合环视图像提供统一的空间表征，从而支持语义分割、三维目标检测和运动预测等多种下游任务的推理。然而，现有大多数BEV感知框架采用端到端训练范式，将图像特征直接转换至BEV空间，仅通过下游任务监督进行优化。这种处理方式将整个感知过程视为黑箱，往往缺乏显式的三维几何理解与可解释性，导致性能表现欠佳。本文主张显式三维表征对实现精准BEV感知至关重要，并提出Splat2BEV——一个基于高斯泼溅辅助的BEV任务框架。该框架旨在学习兼具语义丰富性与几何精确性的BEV特征表征。我们首先预训练一个高斯生成器，该生成器能够从多视角输入中显式重建三维场景，从而生成几何对齐的特征表征。随后将这些表征投影至BEV空间，作为下游任务的输入。在nuScenes和argoverse数据集上的大量实验表明，Splat2BEV实现了最先进的性能，验证了将显式三维重建融入BEV感知的有效性。

---

### 14. GSMem: 3D Gaussian Splatting as Persistent Spatial Memory for Zero-Shot Embodied Exploration and Reasoning

- **作者**: Yiren Lu, Yi Du, Disheng Liu, Yunlai Zhou, Chen Wang, Yu Yin ⭐
  - **高亮作者**: Chen Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.19137v1)
- **发表日期**: 2026-03-19
- **匹配关键词**: gaussian splatting, exploration, navigation, scene graph, 3D gaussian splatting
- **arXiv**: [2603.19137v1](http://arxiv.org/abs/2603.19137v1)
- **📥 PDF**: 已下载至本地 (`2603.19137v1_GSMem_3D_Gaussian_Splatting_as_Persistent_Spatial_Memory_for_Zero-Shot_Embodied_Exploration_and_Reas.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 有效的具身探索要求智能体能够随时间积累并保持空间知识。然而现有的场景表征方法——如离散场景图或静态视角快照——缺乏"事后可重观测性"。若初始观测未能捕获目标，由此产生的记忆缺失往往无法弥补。为填补这一空白，我们提出**GSMem**框架：基于3D高斯泼溅技术构建的零样本具身探索与推理系统。通过显式参数化连续几何结构与稠密外观特征，3DGS构建了持久化空间记忆，赋予智能体"空间回溯"能力——能够从先前未占据的最优视点渲染逼真新视角。为实现这一功能，GSMem采用并行检索机制，同时利用对象级场景图与语义级语言场。这种互补设计能稳健定位目标区域，使智能体能够"幻构"最优视角以进行高保真视觉语言模型推理。此外，我们提出混合探索策略，将VLM驱动的语义评分与基于3DGS的覆盖度目标相结合，在任务感知探索与几何覆盖之间实现动态平衡。在具身问答与终身导航任务上的大量实验验证了本框架的鲁棒性与有效性。

---

### 15. REST: Receding Horizon Explorative Steiner Tree for Zero-Shot Object-Goal Navigation

- **作者**: Shuqi Xiao, Maani Ghaffari, Chengzhong Xu, Hui Kong
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.18624v1)
- **发表日期**: 2026-03-19
- **匹配关键词**: navigation, object-goal navigation
- **arXiv**: [2603.18624v1](http://arxiv.org/abs/2603.18624v1)
- **📥 PDF**: 已下载至本地 (`2603.18624v1_REST_Receding_Horizon_Explorative_Steiner_Tree_for_Zero-Shot_Object-Goal_Navigation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 零样本目标导向导航任务要求智能体在未经任务特定训练的情况下，于未知环境中寻找目标物体。现有分层式免训练方案虽着力于场景理解（信念构建）与高层决策（策略制定），却忽视了"选项"设计——即从动态演化的信念中生成子目标候选集，并提交给策略进行选择。实践中，选项常被简化为独立评分的孤立路径点：单一目的地掩盖了沿途获取的信息价值；无序候选集模糊了选项间的关联性。我们认为选项空间应构建为路径树结构：完整路径能揭示纯目的地评分机制系统性忽略的途中信息增益；共享路径段构成的树状结构支持由粗到细的大语言模型推理，可在细查叶节点前整体排除或追踪分支，从而将组合爆炸的路径空间压缩为高效层次结构。基于此，我们提出**REST**（滚动时域探索型斯坦纳树）框架：该免训练框架（1）通过在线RGB-D流构建显式开放词汇3D地图；（2）基于采样规划生成以智能体为中心的安全信息路径树作为选项空间；（3）将各分支转化为空间叙事文本，通过思维链式大语言模型推理选择最优路径。在Gibson、HM3D和HSSD基准测试中，REST在成功率方面稳居前列，同时取得最优或次优的路径效率，展现出卓越的效率-成功率平衡性。

---

### 16. MultihopSpatial: Multi-hop Compositional Spatial Reasoning Benchmark for Vision-Language Model

- **作者**: Youngwan Lee, Soojin Jang, Yoorhim Cho, Seunghwan Lee, Yong-Ju Lee, Sung Ju Hwang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.18892v1)
- **发表日期**: 2026-03-19
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2603.18892v1](http://arxiv.org/abs/2603.18892v1)
- **📥 PDF**: 已下载至本地 (`2603.18892v1_MultihopSpatial_Multi-hop_Compositional_Spatial_Reasoning_Benchmark_for_Vision-Language_Model.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 空间推理是视觉语言模型的基础能力，尤其在作为视觉语言动作智能体部署于物理环境时更为关键。然而现有基准测试主要关注基础的单跳关系，忽视了现实场景中至关重要的多跳组合推理与精确视觉定位能力。为此，我们提出MultihopSpatial基准，其包含三项核心贡献：(1) 专为多跳组合空间推理设计的综合性基准，涵盖多空间视角下1至3跳的复杂查询；(2) Acc@50IoU评估指标，通过同时要求答案选择与精确边界框预测来评估推理与视觉定位能力——这对稳健的VLA部署至关重要；(3) MultihopSpatial-Train专用大规模训练语料库，用于培养空间智能。通过对37个前沿VLM的广泛评估，我们获得八项关键发现，表明组合空间推理仍是当前面临的重大挑战。最后我们证明，基于本语料库的强化学习后训练能同时提升VLM的内在空间推理能力与下游具身操作性能。

---

### 17. VGGT-360: Geometry-Consistent Zero-Shot Panoramic Depth Estimation

- **作者**: Jiayi Yuan, Haobo Jiang, De Wen Soh, Na Zhao
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.18943v1)
- **发表日期**: 2026-03-19
- **匹配关键词**: 3d reconstruction, 3D reconstruction
- **arXiv**: [2603.18943v1](http://arxiv.org/abs/2603.18943v1)
- **📥 PDF**: 已下载至本地 (`2603.18943v1_VGGT-360_Geometry-Consistent_Zero-Shot_Panoramic_Depth_Estimation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 本文提出VGGT-360，一种用于零样本几何一致全景深度估计的新型免训练框架。与先前视角独立的免训练方法不同，VGGT-360通过利用类VGGT基础模型固有的三维一致性，将任务重新定义为基于多视图重建三维模型的全景重投影，从而将碎片化的单视图推理统一为连贯的全景理解。为实现稳健精确的估计，VGGT-360集成三个即插即用模块，形成统一的全景-三维-深度框架：（一）不确定性引导自适应投影将全景切片为透视图，以弥合全景输入与VGGT透视先验之间的领域差异。该模块通过基于梯度的不确定性估计，为几何信息贫乏区域分配更密集的视图，从而为VGGT生成几何信息丰富的输入。（二）结构显著性增强注意力通过向注意力层注入结构感知置信度，在三维重建过程中增强VGGT的鲁棒性，引导模型聚焦于几何可靠区域并提升跨视图一致性。（三）相关性加权三维模型校正通过注意力推断的相关性分数对重叠点进行重新加权，优化重建的三维模型，为精确的全景重投影提供一致的几何基础。大量实验表明，VGGT-360在多种分辨率及不同室内外数据集上均优于现有基于训练和免训练的先进方法。

---

### 18. SEAR: Simple and Efficient Adaptation of Visual Geometric Transformers for RGB+Thermal 3D Reconstruction

- **作者**: Vsevolod Skorokhodov, Chenghao Xu, Shuo Sun, Olga Fink, Malcolm Mielle
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.18774v1)
- **发表日期**: 2026-03-19
- **匹配关键词**: 3d reconstruction, 3D reconstruction
- **arXiv**: [2603.18774v1](http://arxiv.org/abs/2603.18774v1)
- **📥 PDF**: 已下载至本地 (`2603.18774v1_SEAR_Simple_and_Efficient_Adaptation_of_Visual_Geometric_Transformers_for_RGB+Thermal_3D_Reconstruct.pdf`)
- **🔓 开源**: GITHUB, CODE
  - 链接：https://www.github.com/Schindler-EPFL-Lab/SEAR.
- **中文摘要**: 基础前馈视觉几何模型通过从海量RGB数据集中学习强场景先验，能够实现准确高效的相机姿态估计与场景重建。然而，当应用于混合传感模态（如RGB-热成像图像）时，其性能会下降。我们观察到，虽然基于RGB数据预训练的视觉几何Transformer在纯热成像重建中表现良好，但在联合处理RGB与热成像模态时难以实现跨模态对齐。为此，我们提出SEAR——一种简单高效的微调策略，可将预训练的几何Transformer适配于多模态RGB-T输入。尽管仅在相对小规模的RGB-T数据集上进行训练，我们的方法在三维重建和相机姿态估计任务上显著优于现有最优方法，所有评估指标均实现大幅提升（例如AUC@30指标提升超过29%），在推理时间开销可忽略不计的前提下，实现了更高细节度与跨模态一致性。值得注意的是，即使在低光照、浓烟等挑战性条件下，SEAR仍能实现可靠的多模态姿态估计与重建。我们通过大量消融实验验证了架构的有效性，阐明了模型实现跨模态对齐的机制。此外，我们提出了一个包含不同时间、视角和光照条件下采集的RGB与热成像序列的新数据集，为未来多模态三维场景重建研究提供了稳健的基准。代码与模型已在https://www.github.com/Schindler-EPFL-Lab/SEAR公开。

---

### 19. From ex(p) to poly: Gaussian Splatting with Polynomial Kernels

- **作者**: Joerg H. Mueller, Martin Winter, Markus Steinberger
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.18707v1)
- **发表日期**: 2026-03-19
- **匹配关键词**: gaussian splatting
- **arXiv**: [2603.18707v1](http://arxiv.org/abs/2603.18707v1)
- **📥 PDF**: 已下载至本地 (`2603.18707v1_From_ex(p)_to_poly_Gaussian_Splatting_with_Polynomial_Kernels.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 近期高斯泼溅（3DGS）技术的研究对原始核函数进行了多种改进，显著提升了算法性能。然而，许多核函数调整与针对原始高斯核优化的现有数据集存在兼容性问题，这给技术推广带来了挑战。本研究通过提出一种新型兼容性核函数来解决该问题，该核函数在保持与现有数据集兼容的同时提升了计算效率。具体而言，我们将原始指数核替换为结合ReLU函数的多项式近似核。这种改进使得高斯函数的筛选机制更为高效，从而在不同3DGS实现方案中均获得性能提升。实验结果表明，新方法在图像质量影响可忽略不计的前提下，实现了4%至15%的性能提升。我们同时提供了新核函数的详细数学分析，并探讨了其在NPU硬件上部署3DGS的潜在优势。

---

### 20. Beyond TVLA: Anderson-Darling Leakage Assessment for Neural Network Side-Channel Leakage Detection

- **作者**: Ján Mikulec, Jakub Breier, Xiaolu Hou
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.18647v1)
- **发表日期**: 2026-03-19
- **匹配关键词**: VLA
- **arXiv**: [2603.18647v1](http://arxiv.org/abs/2603.18647v1)
- **📥 PDF**: 已下载至本地 (`2603.18647v1_Beyond_TVLA_Anderson-Darling_Leakage_Assessment_for_Neural_Network_Side-Channel_Leakage_Detection.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 基于韦尔奇$t$检验的测试向量泄漏评估已成为检测侧信道泄漏的标准工具。然而，当其均值特性在泄漏主要通过高阶分布差异显现时，可能会限制检测的灵敏度。我们的实验表明，这一特性在评估神经网络实现时尤为关键。本研究提出安德森-达林泄漏评估，这是一种应用双样本安德森-达林检验进行泄漏检测的框架。与测试向量泄漏评估不同，安德森-达林泄漏评估检验完整累积分布函数的等价性，不依赖于纯粹的均值偏移模型。

我们在基于MNIST数据集训练、并在ChipWhisperer-Husky评估平台上实现的多层感知机上对安德森-达林泄漏评估进行了验证。实验中考虑了采用乱序执行和随机抖动防护措施的受保护实现。结果表明，相较于测试向量泄漏评估，安德森-达林泄漏评估在少量迹线条件下对受保护实现具有更优的泄漏检测灵敏度。

---

