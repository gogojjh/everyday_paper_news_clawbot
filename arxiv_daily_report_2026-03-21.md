# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-03-21 08:04

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 6/20 篇提供

**🌟 Highlight**: 14 篇 | **📌 Poster**: 6 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models

- **作者**: Bryce Grant, Xijia Zhao, Peng Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.19233v1)
- **发表日期**: 2026-03-19
- **匹配关键词**: vision-language-action, vision-language-action model, VLA, exploration
- **arXiv**: [2603.19233v1](http://arxiv.org/abs/2603.19233v1)
- **📥 PDF**: 已下载至本地 (`2603.19233v1_Not_All_Features_Are_Created_Equal_A_Mechanistic_Study_of_Vision-Language-Action_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型将感知、语言和运动控制整合于单一架构，但其如何将多模态输入转化为动作的机制尚不明确。本研究在四个基准测试的394,000+次推演中，对六款参数量级跨越80M至7B的模型应用了激活注入、稀疏自编码器（SAEs）和线性探针分析。研究发现：在所有架构中，视觉通路主导动作生成——向无提示推演注入基线激活可恢复近乎一致的行为，而跨任务注入则引导机器人朝向源任务位置（X-VLA推演中99.8%与源轨迹吻合），揭示了与场景坐标而非抽象任务表征绑定的空间运动程序。语言敏感性取决于任务结构而非模型设计：当视觉上下文能唯一确定任务时语言被忽略；当多目标共享场景时语言变得关键（X-VLA在错误提示下，\texttt{libero\_goal}任务成功率从94%降至10%，而\texttt{libero\_object}任务保持60-100%成功率）。在三种多通路架构（\pizhalf{}、SmolVLA、GR00T）中，专家通路编码运动程序，而视觉语言模型通路编码目标语义（专家注入引起的行为偏移量是后者的2倍），子空间注入证实二者占据可分离的激活子空间。尽管均值池化能提升X-VLA的动作保真度，但逐令牌SAE处理对多数架构的动作保真至关重要。对比识别技术复原了82个以上操作概念，因果消融实验显示零效应率敏感区间为28-92%，且与表征宽度无关。我们发布\textbf{Action Atlas}（https://action-atlas.com）平台，支持对六款模型VLA表征的交互式探索。

---

### 2. MonoArt: Progressive Structural Reasoning for Monocular Articulated 3D Reconstruction

- **作者**: Haitian Li, Haozhe Xie, Junxiang Xu, Beichen Wen, Fangzhou Hong, Ziwei Liu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.19231v1)
- **发表日期**: 2026-03-19
- **匹配关键词**: 3d reconstruction, 3D reconstruction
- **arXiv**: [2603.19231v1](http://arxiv.org/abs/2603.19231v1)
- **📥 PDF**: 已下载至本地 (`2603.19231v1_MonoArt_Progressive_Structural_Reasoning_for_Monocular_Articulated_3D_Reconstruction.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 从单幅图像重建关节化三维物体需要从有限的视觉证据中联合推断物体几何、部件结构和运动参数。核心难点在于运动线索与物体结构的相互纠缠，这使得直接回归关节参数变得不稳定。现有方法通过多视角监督、基于检索的装配或辅助视频生成来解决这一挑战，但往往牺牲了可扩展性或效率。我们提出了MonoArt框架，该框架基于渐进式结构推理构建统一架构。与直接从图像特征预测关节参数不同，MonoArt在单一架构内逐步将视觉观察转化为规范几何、结构化部件表示和运动感知嵌入。这种结构化推理过程无需外部运动模板或多阶段流程即可实现稳定且可解释的关节推断。在PartNet-Mobility数据集上的大量实验表明，该方法在重建精度和推理速度上均达到最先进水平。该框架可进一步推广至机器人操作和关节化场景重建任务。

---

### 3. NavTrust: Benchmarking Trustworthiness for Embodied Navigation

- **作者**: Huaide Jiang, Yash Chaudhary, Yuping Wang, Zehao Wang, Raghav Sharma, Manan Mehta, Yang Zhou, Lichao Sun, Zhiwen Fan, Zhengzhong Tu, Jiachen Li
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.19229v1)
- **发表日期**: 2026-03-19
- **匹配关键词**: navigation, object-goal navigation, VLN
- **arXiv**: [2603.19229v1](http://arxiv.org/abs/2603.19229v1)
- **📥 PDF**: 已下载至本地 (`2603.19229v1_NavTrust_Benchmarking_Trustworthiness_for_Embodied_Navigation.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://navtrust.github.io.
- **中文摘要**: 具身导航主要分为两大类：视觉语言导航（VLN），即智能体通过遵循自然语言指令进行导航；以及目标物体导航（OGN），即智能体导航至指定目标物体。然而，现有研究主要评估模型在理想条件下的性能，忽视了现实场景中可能出现的干扰因素。为填补这一空白，我们提出了NavTrust——一个在真实场景中系统性地对RGB图像、深度信息和指令等输入模态施加干扰，并评估其对导航性能影响的统一基准测试平台。据我们所知，NavTrust是首个在统一框架下将具身导航智能体暴露于多样化RGB-深度干扰及指令变体的基准测试。通过对七种前沿方法进行广泛评估，我们发现这些方法在现实干扰下均出现显著性能下降，这揭示了当前系统在鲁棒性方面存在的关键不足，并为构建更可信的具身导航系统提供了改进方向。此外，我们系统评估了四种不同的增强策略，以提升模型对RGB-深度干扰和指令干扰的鲁棒性。我们的基础模型包括Uni-NaVid和ETPNav。在真实移动机器人上的部署实验表明，这些策略有效提升了系统对干扰的鲁棒性。项目网站为：https://navtrust.github.io。

---

### 4. FASTER: Rethinking Real-Time Flow VLAs

- **作者**: Yuxiang Lu, Zhe Liu, Xianzhe Fan, Zhenya Yang, Jinghua Hou, Junyi Li, Kaixin Ding, Hengshuang Zhao
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.19199v1)
- **发表日期**: 2026-03-19
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2603.19199v1](http://arxiv.org/abs/2603.19199v1)
- **📥 PDF**: 已下载至本地 (`2603.19199v1_FASTER_Rethinking_Real-Time_Flow_VLAs.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 实时执行对于在物理世界中部署视觉-语言-动作（VLA）模型至关重要。现有的异步推理方法主要优化轨迹平滑度，却忽视了响应环境变化的关键延迟问题。本文通过重新审视动作分块策略中的响应机制，系统分析了影响响应时间的因素。研究表明，响应时间遵循由首次动作时间（TTFA）与执行视野共同决定的均匀分布。进一步发现，在基于流的VLA模型中采用恒定调度方案的传统做法效率低下，迫使系统在开始任何动作前必须完成所有采样步骤，从而形成响应延迟的瓶颈。为突破这一限制，我们提出即时响应快速动作采样（FASTER）方法。通过引入视野感知调度机制，FASTER在流采样过程中自适应地优先处理近期动作，将即时响应的去噪过程压缩十倍（如在$π_{0.5}$和X-VLA中）至单步完成，同时保持长视野轨迹的质量。结合流式客户端-服务器架构，FASTER显著降低了真实机器人系统的有效响应延迟，尤其在消费级GPU部署场景中表现突出。包括高动态乒乓球任务在内的真实世界实验证明，FASTER为通用策略提供了前所未有的实时响应能力，能够快速生成精准流畅的运动轨迹。

---

### 5. Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models

- **作者**: Aiden Swann, Lachlain McGranahan, Hugo Buurmeijer, Monroe Kennedy, Mac Schwager
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.19183v1)
- **发表日期**: 2026-03-19
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2603.19183v1](http://arxiv.org/abs/2603.19183v1)
- **📥 PDF**: 已下载至本地 (`2603.19183v1_Sparse_Autoencoders_Reveal_Interpretable_and_Steerable_Features_in_VLA_Models.pdf`)
- **🔓 开源**: PROJECT_PAGE, CODE
  - 链接：http://drvla.github.io
- **中文摘要**: 视觉-语言-动作（VLA）模型已成为通用机器人操作领域的一种前景广阔的方法。然而，其泛化能力并不稳定：尽管这些模型在某些场景下表现优异，但经过微调的变体往往难以应对新物体、新场景和新指令。我们运用机制可解释性技术深入探究VLA模型的内在运行机制。为探查内部表征，我们在VLA隐藏层激活上训练稀疏自编码器（SAEs）。SAEs学习到的稀疏字典特征可作为模型计算过程的紧凑可解释基础。研究发现，绝大多数提取的SAE特征对应于特定训练演示中的记忆序列，但部分特征呈现出可解释、通用且可操控的运动基元与语义属性，为VLA的泛化能力提供了积极线索。我们提出一种特征分类度量标准，用以区分特征表征的是可泛化迁移基元还是任务特定记忆。通过在LIBERO基准测试中的操控实验验证了这些发现，证明单个SAE特征能因果影响机器人行为。操控通用特征可激发符合其语义含义的行为，并能跨任务与场景应用。这项研究首次从机制层面证明VLA具备跨任务与场景学习泛化特征的能力。我们观察到，在小规模机器人数据集上进行监督微调会过度强化记忆效应，而在更大规模多样化数据集（如DROID）上训练或采用知识隔离机制则能促进更通用特征的形成。我们开源了包含激活收集、SAE训练和特征操控功能的代码库及用户友好界面，项目页面详见http://drvla.github.io。

---

### 6. From Inference Efficiency to Embodied Efficiency: Revisiting Efficiency Metrics for Vision-Language-Action Models

- **作者**: Zhuofan Li, Hongkun Yang, Zhenyang Chen, Yangxuan Chen, Yingyan, Lin, Chaojian Li
- **单位**: Celine; Celine; Celine...
- **发表日期**: 2026-03-19
- **匹配关键词**: vision-language-action, VLA, vision-language-action model
- **arXiv**: [2603.19131v1](http://arxiv.org/abs/2603.19131v1)
- **📥 PDF**: 已下载至本地 (`2603.19131v1_From_Inference_Efficiency_to_Embodied_Efficiency_Revisiting_Efficiency_Metrics_for_Vision-Language-A.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作模型通过联合推理视觉、语言与运动模态，近期使具身智能体能够执行日益复杂的任务。然而我们发现，当前VLA研究中以参数量、浮点运算量或解码吞吐量为表征的"效率"概念，并不能反映其在机器人平台上的实际表现。在现实执行场景中，效率由系统级具身行为决定，包括任务完成时间、轨迹平滑度、关节累计旋转量和运动能耗等。通过对模型压缩、令牌稀疏化和动作序列压缩的对照研究，我们获得了若干挑战常规认知的发现：（1）在传统指标下降低计算量的方法，尽管能维持任务成功率，却往往增加端到端执行成本或降低运动质量；（2）系统级具身效率指标揭示了传统评估中难以察觉的学习动作策略性能差异；（3）上下文提示或监督微调等常见适应方法对具身效率的提升有限且具有指标特异性——虽然能降低急动度或动作频率等目标指标，但可能以延长完成时间等其他指标为代价。综合而言，传统推理效率指标可能忽略具身执行的重要维度，而引入具身效率评估能为策略行为与实用性能提供更完整的视角，实现更公平全面的VLA模型比较。

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
- **中文摘要**: 从单目RGB视频中理解真实的手-物交互对于增强现实/虚拟现实、机器人技术和具身人工智能至关重要。现有方法依赖特定类别的模板或大量计算，但在三维空间中仍会产生物理不一致的手-物对齐。我们提出GHOST（高斯手-物溅射）框架，这是一种快速、类别无关的解决方案，利用二维高斯溅射技术重建动态手-物交互。GHOST将手部和物体表示为密集且视角一致的高斯圆盘，并引入三项关键创新：（1）通过几何先验检索与一致性损失补全被遮挡的物体区域；（2）采用抓取感知对齐机制优化手部平移与物体尺度，确保真实接触；（3）设计手部感知背景损失函数，避免对受手部遮挡的物体区域进行错误惩罚。GHOST仅需单段RGB视频即可实现完整、物理一致且可动画化的重建，其运行速度比现有类别无关方法快一个数量级。在ARCTIC、HO3D及真实场景数据集上的大量实验表明，该方法在三维重建精度和二维渲染质量方面均达到最先进水平，确立了GHOST作为真实手-物交互建模的高效稳健解决方案。代码已开源：https://github.com/ATAboukhadra/GHOST。

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
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2603.18532v1](http://arxiv.org/abs/2603.18532v1)
- **📥 PDF**: 已下载至本地 (`2603.18532v1_Scaling_Sim-to-Real_Reinforcement_Learning_for_Robot_VLAs_with_Generative_3D_Worlds.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 大型视觉语言模型（VLM）通过强化学习（RL）训练展现出的优异性能，推动了在机器人领域采用类似方法对视觉-语言-动作（VLA）模型进行微调的研究。近期许多工作直接在现实世界中对VLA模型进行微调，以避免处理仿真到现实的差异问题。虽然现实世界中的强化学习规避了仿真到现实的挑战，但它本质上限制了所得VLA模型的泛化能力，因为在物理世界中扩展场景和物体的多样性极其困难。这导致了一个矛盾的结果：将经过广泛预训练的模型转变为一个过度拟合、仅适用于特定场景的策略。相比之下，在仿真环境中训练可以提供多样化的场景，但设计这些场景同样成本高昂。本研究证明，通过利用三维世界生成模型，可以在不牺牲泛化能力且减少人工成本的情况下对VLA模型进行强化学习微调。结合语言驱动的场景设计工具，我们生成了数百个包含独特物体和背景的多样化交互场景，实现了可扩展且高度并行的策略学习。从预训练的模仿基线出发，我们的方法将仿真成功率从9.7%提升至79.8%，同时任务完成时间缩短了1.25倍。通过生成高质量数字孪生结合领域随机化技术，我们进一步展示了成功的仿真到现实迁移能力，将现实世界成功率从21.7%提高至75%，并实现了1.13倍的加速。最后，我们通过消融实验强调了利用三维世界生成模型近乎无限数据资源的优势，证明增加场景多样性可直接提升零样本泛化性能。

---

### 10. OnlinePG: Online Open-Vocabulary Panoptic Mapping with 3D Gaussian Splatting

- **作者**: Hongjia Zhai, Qi Zhang, Xiaokun Pan, Xiyu Zhang, Yitong Dong, Huaqi Zhang, Dan Xu, Guofeng Zhang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.18510v1)
- **发表日期**: 2026-03-19
- **匹配关键词**: 3D gaussian splatting, gaussian splatting
- **arXiv**: [2603.18510v1](http://arxiv.org/abs/2603.18510v1)
- **📥 PDF**: 已下载至本地 (`2603.18510v1_OnlinePG_Online_Open-Vocabulary_Panoptic_Mapping_with_3D_Gaussian_Splatting.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 基于在线全景映射的开放词汇场景理解对于具身应用感知和交互环境至关重要。然而，现有方法多为离线系统或缺乏实例级理解能力，限制了其在现实机器人任务中的应用。本文提出OnlinePG系统，这是一种创新且高效的解决方案，通过在线环境下的三维高斯泼溅技术，实现了几何重建与开放词汇感知的深度融合。技术上，为实现在线全景映射，我们采用基于滑动窗口的局部到全局高效处理范式。在构建局部一致性地图时，我们设计了融合几何与语义线索的三维片段聚类图，将滑动窗口内不一致的片段整合为完整实例。随后通过为局部三维高斯地图构建具有空间属性的显式网格，并借助鲁棒的双向二分三维高斯实例匹配机制，将其融合至全局地图。最终，我们利用三维空间属性网格内融合的视觉语言模型特征实现开放词汇场景理解。在多个主流数据集上的大量实验表明，本方法在保持实时效率的同时，在在线方法中取得了更优的性能表现。

---

### 11. Shifting Uncertainty to Critical Moments: Towards Reliable Uncertainty Quantification for VLA Model

- **作者**: Yanchuan Tang, Taowen Wang, Yuefei Chen, Boxuan Zhang, Qiang Guan, Ruixiang Tang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.18342v1)
- **发表日期**: 2026-03-18
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2603.18342v1](http://arxiv.org/abs/2603.18342v1)
- **📥 PDF**: 已下载至本地 (`2603.18342v1_Shifting_Uncertainty_to_Critical_Moments_Towards_Reliable_Uncertainty_Quantification_for_VLA_Model.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作模型通过将视觉观察与语言指令映射为底层动作，实现了通用机器人策略，但这类模型往往缺乏可靠的自我评估能力。现有方法通常计算令牌级不确定性信号，并在整个执行过程中取平均值。然而在连续控制任务中，均值聚合可能稀释短暂但安全关键的不确定性峰值：成功执行轨迹可能因良性噪声或非关键微调包含局部高熵片段，而失败轨迹在多数时间步可能呈现低熵特征，仅在故障发生前出现短暂峰值。我们提出一种预测执行成功与失败的统一不确定性量化方法，该方法具有三个创新点：（1）采用基于最大值的滑动窗口池化以保留瞬态风险信号；（2）通过运动感知稳定性加权强化与不稳定行为相关的高频动作振荡；（3）借助贝叶斯优化进行自由度自适应校准，以优先处理运动学关键轴。在LIBERO基准测试中的实验表明，该方法显著提升了故障预测准确率，并生成更可靠的故障检测信号，可为下游人机协同干预提供支持。

---

### 12. Proprioceptive-only State Estimation for Legged Robots with Set-Coverage Measurements of Learned Dynamics

- **作者**: Abhijeet M. Kulkarni, Ioannis Poulakakis, Guoquan Huang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.18308v1)
- **发表日期**: 2026-03-18
- **匹配关键词**: navigation
- **arXiv**: [2603.18308v1](http://arxiv.org/abs/2603.18308v1)
- **📥 PDF**: 已下载至本地 (`2603.18308v1_Proprioceptive-only_State_Estimation_for_Legged_Robots_with_Set-Coverage_Measurements_of_Learned_Dyn.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 仅依赖本体感知的状态估计对足式机器人具有吸引力，因其计算成本较低且不受感知退化条件的影响。关节级测量数据的历史记录蕴含着丰富信息，可用于推断系统动态特性并生成导航测量值。现有方法通常在高斯噪声假设下，通过学习的测量模型生成此类估计值并与惯性测量单元数据融合。然而，在训练数据有限的情况下，该假设极易失效，导致估计结果不一致并可能产生发散。本研究提出一种足式机器人专用纯本体感知状态估计框架，采用不预设任何分布特性的集合覆盖描述来表征测量噪声。我们开发了一种实用且计算成本较低的方法，可在高斯滤波器中系统化地运用这些集合覆盖测量值。通过仿真实验和两个真实四足机器人数据集的验证表明：与高斯基线方法相比，所提方法在真实噪声场景下能保持估计一致性且不易产生漂移现象。

---

### 13. GoalVLM: VLM-driven Object Goal Navigation for Multi-Agent System

- **作者**: MoniJesu James, Amir Atef Habel, Aleksey Fedoseev, Dzmitry Tsetserokou
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.18210v1)
- **发表日期**: 2026-03-18
- **匹配关键词**: navigation, exploration, object-goal navigation
- **arXiv**: [2603.18210v1](http://arxiv.org/abs/2603.18210v1)
- **📥 PDF**: 已下载至本地 (`2603.18210v1_GoalVLM_VLM-driven_Object_Goal_Navigation_for_Multi-Agent_System.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 传统目标导航通常局限于地面机器人及封闭式物体词汇集。现有多智能体方法依赖于与固定类别集绑定的预计算概率图，无法在测试时泛化至新目标。

我们提出GoalVLM——一个面向零样本开放词汇目标导航的协作式多智能体框架。该框架将视觉语言模型直接集成至决策循环，结合支持文本提示检测与分割的SAM3模型，以及用于空间推理的SpaceOM模块，使智能体能够解析自由形式语言目标，并通过零样本语义先验对探索边界进行评分而无需重新训练。每个智能体通过深度投影体素渲染构建鸟瞰语义地图，同时目标投影器通过标定深度将检测结果反向投影至地图，实现可靠的目标定位。约束引导推理层通过结构化提示链（场景描述、房间类型分类、感知门控、多边界排序）评估探索边界，将常识先验注入探索过程。

我们在GOAT-Bench val_unseen数据集（包含360个多子任务场景、1032个序列化目标导航子任务及HM3D场景）上评估GoalVLM，每个场景需导航至5-7个开放词汇目标链。采用双智能体的GoalVLM实现55.8%的子任务成功率和18.3%的路径长度加权成功率，与最先进方法表现相当且无需任务特定训练。消融实验证实了视觉语言模型引导的边界推理与深度投影目标定位机制的有效性。

---

### 14. GMT: Goal-Conditioned Multimodal Transformer for 6-DOF Object Trajectory Synthesis in 3D Scenes

- **作者**: Huajian Zeng, Abhishek Saroha, Daniel Cremers, Xi Wang ⭐
  - **高亮作者**: Daniel Cremers
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.17993v1)
- **发表日期**: 2026-03-18
- **匹配关键词**: object manipulation
- **arXiv**: [2603.17993v1](http://arxiv.org/abs/2603.17993v1)
- **📥 PDF**: 已下载至本地 (`2603.17993v1_GMT_Goal-Conditioned_Multimodal_Transformer_for_6-DOF_Object_Trajectory_Synthesis_in_3D_Scenes.pdf`)
- **🔓 开源**: PROJECT_PAGE
- **中文摘要**: 在三维环境中合成可控的六自由度物体操作轨迹对于实现机器人与复杂场景交互至关重要，但由于需要精确的空间推理、物理可行性及多模态场景理解，该任务仍具挑战性。现有方法多依赖二维或局部三维表征，限制了其对完整场景几何结构的捕捉能力，并制约了轨迹精度。本文提出GMT——一种多模态Transformer框架，通过联合利用三维边界框几何、点云上下文、语义物体类别及目标末端姿态，生成真实且目标导向的物体运动轨迹。该模型将轨迹表示为连续的六自由度姿态序列，并采用定制化的条件融合策略，整合几何、语义、上下文及目标导向信息。在合成与真实场景基准测试中的大量实验表明，GMT在空间精度与姿态控制方面显著优于CHOIS、GIMO等当前最优的人体运动与人-物交互基线方法。本方法为基于学习的操作规划建立了新基准，并展现出对多样化物体及杂乱三维环境的强大泛化能力。项目页面：https://huajian-zeng.github.io/projects/gmt/。

---

## 📌 Poster

*其他相关研究*

---

### 1. OmniVTA: Visuo-Tactile World Modeling for Contact-Rich Robotic Manipulation

- **作者**: Yuhang Zheng, Songen Gu, Weize Li, Yupeng Zheng, Yujie Zang, Shuai Tian, Xiang Li, Ruihai Wu, Ce Hao, Chen Gao, Si Liu, Haoran Li, Yilun Chen, Shuicheng Yan, Wenchao Ding
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.19201v1)
- **发表日期**: 2026-03-19
- **匹配关键词**: contact-rich manipulation
- **arXiv**: [2603.19201v1](http://arxiv.org/abs/2603.19201v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: PROJECT_PAGE, CODE
  - 链接：https://mrsecant.github.io/OmniVTA.
- **中文摘要**: 接触密集型操作任务（如擦拭与装配）需要精确感知接触力、摩擦力变化及状态转换，这些信息仅靠视觉难以可靠推断。尽管视觉触觉操作研究日益受到关注，但其发展仍受制于两大瓶颈：现有数据集规模有限且任务覆盖狭窄，且当前方法仅将触觉信号视为被动观测，未能利用其建模接触动力学或实现显式闭环控制。本文提出\textbf{OmniViTac}——一个大规模视觉-触觉-动作数据集，涵盖86项任务、100余种物体的21,000余条轨迹数据，并按六类物理交互模式进行组织。基于此数据集，我们构建了\textbf{OmniVTA}框架：一种基于世界模型的视觉触觉操作框架，集成四个紧密耦合的模块：自监督触觉编码器、用于预测短时域接触演化的双流视觉-触觉世界模型、生成动作的接触感知融合策略，以及能以60Hz频率通过闭环校正预测与观测触觉信号偏差的反射控制器。在全部六类交互场景的真实机器人实验中，OmniVTA均优于现有方法，并对未见物体及几何构型展现出良好泛化能力，证实了预测性接触建模与高频触觉反馈相结合在接触密集型操作中的价值。所有数据、模型及代码均将通过项目网站https://mrsecant.github.io/OmniVTA公开。

---

### 2. Meanings and Measurements: Multi-Agent Probabilistic Grounding for Vision-Language Navigation

- **作者**: Swagat Padhan, Lakshya Jain, Bhavya Minesh Shah, Omkar Patil, Thao Nguyen, Nakul Gopalan
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.19166v1)
- **发表日期**: 2026-03-19
- **匹配关键词**: navigation
- **arXiv**: [2603.19166v1](http://arxiv.org/abs/2603.19166v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 与人类协作的机器人必须将自然语言目标转化为可执行、物理上可落地的决策。例如，执行"走到冰箱右侧两米处"这类指令时，需要在三维场景中实现对语义指代、空间关系和度量约束的精准理解。尽管当前视觉语言模型展现出强大的语义理解能力，但其设计初衷并未包含对物理空间中度量约束的推理机制。本研究通过实证分析发现，基于前沿视觉语言模型的语义理解方法在处理复杂度量-语义混合语言查询时存在明显局限。为此，我们提出多智能体概率理解框架，该智能体框架将语言查询解构为结构化子组件，通过查询视觉语言模型实现对每个组件的语义理解，随后通过概率合成机制将这些理解结果整合为三维空间中度量一致的可执行决策。在HM-EQA基准测试中，MAPG框架相较于现有基线模型展现出持续的性能提升。此外，我们创建了专门评估度量-语义目标理解能力的新基准MAPG-Bench，以填补现有语言理解评估体系的空白。通过真实机器人演示实验，我们进一步证明当具备结构化场景表征时，MAPG框架能够实现从仿真环境到现实场景的有效迁移。

---

### 3. Tendon-Actuated Robots with a Tapered, Flexible Polymer Backbone: Design, Fabrication, and Modeling

- **作者**: Harald Minde Hansen, Nandita Gallacher, Nicholas B. Andrews, Kristin Y. Pettersen, Jan Tommy Gravdahl, Mario di Castro
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.19124v1)
- **发表日期**: 2026-03-19
- **匹配关键词**: exploration
- **arXiv**: [2603.19124v1](http://arxiv.org/abs/2603.19124v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 本文介绍了采用热塑性聚氨酯（TPU）材料构建的柔性锥形骨架结构，通过肌腱驱动的三维打印连续体机器人的设计、建模与制造方法。该可扩展设计方案集成了电子元件基座，能够通过驱动器和压缩载荷传感器实现肌腱张力的直接控制与感知。与许多单功能、高成本的连续体机器人不同，本设计优先考虑可定制性、快速组装和低成本，同时通过几何锥度设计实现高曲率运动和增强的末端柔顺性，从而支持广泛的柔顺机器人检测与操作任务。基于科瑟拉杆理论，我们采用牛顿力学方法建立了锥形骨架的广义正向运动静力学模型，将现有肌腱驱动科瑟拉杆公式扩展至显式考虑空间变化的骨架截面几何特征。该模型能够捕捉锥度引起的梯度刚度分布，并支持根据几何设计参数对构型空间进行系统性探索。我们重点分析了骨架锥角如何影响机器人的构型空间与可操作性。通过运动捕捉数据验证，在采用线性搜索法校准杨氏模量以最小化建模误差后，模型实现了厘米级的形状预测精度。我们还展示了将内窥镜夹钳沿连续体机器人布设并安装于六自由度机械臂上实现的遥操作抓取功能。研究提供了参数化的iLogic/CAD脚本用于快速几何生成与缩放。该框架为采用熔融沉积成型三维打印机制造的锥形肌腱驱动连续体机器人，建立了一条从参数化设计到可控肌腱驱动的简洁、快速且可复现的技术路径。

---

### 4. MERGE: Guided Vision-Language Models for Multi-Actor Event Reasoning and Grounding in Human-Robot Interaction

- **作者**: Joerg Deigmoeller, Nakul Agarwal, Stephan Hasler, Daniel Tanneberg, Anna Belardinelli, Reza Ghoddoosian, Chao Wang, Felix Ocker, Fan Zhang, Behzad Dariush, Michael Gienger
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.18988v1)
- **发表日期**: 2026-03-19
- **匹配关键词**: human-robot interaction, HRI
- **arXiv**: [2603.18988v1](http://arxiv.org/abs/2603.18988v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: GITHUB
- **中文摘要**: 我们提出MERGE系统，用于在动态人机群体交互中实现参与者、物体和事件的情境化定位。在此类场景中，有效协作需要建立在持续的人员与物体表征以及事件片段化抽象基础上的情境感知一致性。MERGE通过独特识别参与者（人类或机器人）与物体的物理实例，并将其组织为"参与者-动作-物体"关系结构，确保跨交互过程的时间一致性。该系统的核心在于融合视觉语言模型与感知流水线：轻量级流式处理模块持续分析视觉输入以检测变化，仅在必要时选择性调用视觉语言模型。这种解耦设计在保持视觉语言模型推理能力和零样本泛化优势的同时，显著提升效率，既避免了逐帧标注的高昂成本与延迟问题，也解决了由此产生的碎片化及滞后输出。针对多参与者协作场景缺乏合适基准测试的现状，我们推出GROUND数据集，该数据集提供多人交互及人机交互的细粒度情境标注。实验表明，在该数据集上我们的方法将平均定位分数提升至纯视觉语言模型基线（包括GPT-4o、GPT-5和Gemini 2.5 Flash）的2倍，同时将运行时间缩短至1/4。代码与数据已发布于www.github.com/HRI-EU/merge。

---

### 5. ROFT-VINS: Robust Feature Tracking-based Visual-Inertial State Estimation for Harsh Environment

- **作者**: Sanghyun Park, Soohee Han
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.18746v1)
- **发表日期**: 2026-03-19
- **匹配关键词**: localization and mapping
- **arXiv**: [2603.18746v1](http://arxiv.org/abs/2603.18746v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: SLAM（即时定位与地图构建）与里程计是利用一个或多个传感器来估计机器人、汽车等移动设备位置的重要系统。尤其在基于摄像头的SLAM或里程计中，有效追踪视觉特征至关重要，因为它直接影响系统性能。本文提出一种利用深度学习在单目摄像头图像中稳健追踪视觉特征的方法。该方法即使在纹理缺失的环境和光照快速变化的场景中也能可靠运行。此外，我们通过将所提方法集成至常用的视觉惯性里程计系统VINS-Fusion（单目-惯性版本）中，对其性能进行了评估。

---

### 6. CSSDF-Net: Safe Motion Planning Based on Neural Implicit Representations of Configuration Space Distance Field

- **作者**: Haohua Chen, Yixuan Zhou, Yifan Zhou, Hesheng Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.18669v1)
- **发表日期**: 2026-03-19
- **匹配关键词**: motion planning, implicit representation
- **arXiv**: [2603.18669v1](http://arxiv.org/abs/2603.18669v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 在非结构化环境中进行高维机械臂操作，需要一种可微分、与场景无关的距离查询机制来指导安全运动生成。现有几何碰撞检测器通常不可微分，而基于工作空间的隐式距离模型则受限于高度非线性的工作空间-构型映射关系，常面临收敛困难的问题；此外，自碰撞与环境碰撞通常被作为独立约束分别处理。我们提出构型空间符号距离场网络（CSSDF-Net），该网络直接在构型空间中学习连续符号距离场，在统一的安全几何框架下提供关节空间距离与梯度查询。为实现无需环境特定重训练的零样本泛化能力，我们设计了基于空间哈希的数据生成流程，该流程编码以机器人为中心的几何先验知识，并支持对任意障碍物点集的风险构型进行高效检索。学习得到的距离场被集成至安全约束轨迹优化与滚动时域模型预测控制中，同时支持离线规划与在线反应式避障。在平面机械臂与7自由度机械臂上的实验表明，该方法具有稳定的梯度特性，能在静态与动态场景中实现有效避障，且对大规模点云查询具备实用级推理延迟，支持在未见环境中进行部署。

---

