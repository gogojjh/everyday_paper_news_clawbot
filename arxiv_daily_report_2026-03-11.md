# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-03-11 08:05

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 4/20 篇提供

**🌟 Highlight**: 15 篇 | **📌 Poster**: 5 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. MetaWorld-X: Hierarchical World Modeling via VLM-Orchestrated Experts for Humanoid Loco-Manipulation

- **作者**: Yutong Shen, Hangxu Liu, Penghui Liu, Jiashuo Luo, Yongkang Zhang, Rex Morvley, Chen Jiang, Jianwei Zhang, Lei Zhang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.08572v1)
- **发表日期**: 2026-03-09
- **匹配关键词**: locomotion and manipulation
- **arXiv**: [2603.08572v1](http://arxiv.org/abs/2603.08572v1)
- **📥 PDF**: 已下载至本地 (`2603.08572v1_MetaWorld-X_Hierarchical_World_Modeling_via_VLM-Orchestrated_Experts_for_Humanoid_Loco-Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 学习类人机器人执行同步移动与操作任务时自然、稳定且具备组合泛化能力的全身控制策略，仍是机器人学领域的核心挑战。现有强化学习方法通常依赖单一整体策略来习得多重技能，这在高自由度系统中常导致技能间梯度干扰与运动模式冲突，使得生成行为频繁出现动作不自然、稳定性受限以及对复杂任务组合泛化能力差等问题。为突破这些局限，我们提出MetaWorld-X——一个面向类人机器人控制的分层世界模型框架。基于分治原则，该方法将复杂控制问题分解为一组专业化专家策略。每个专家通过模仿约束强化学习在人体运动先验指导下进行训练，引入符合生物力学的归纳偏置，确保生成动作的自然性与物理合理性。在此基础上，我们进一步开发了由视觉语言模型监督的智能路由机制，实现语义驱动的专家策略组合。该路由模块依据高层任务语义动态整合专家策略，有效促进多阶段移动操作任务中的组合泛化与自适应执行能力。

---

### 2. AtomVLA: Scalable Post-Training for Robotic Manipulation via Predictive Latent World Models

- **作者**: Xiaoquan Sun, Zetian Xu, Chen Cao, Zonghe Liu, Yihan Sun, Jingrui Pang, Ruijian Zhang, Zhen Yang, Kang Pang, Dingxin He, Mingqi Yuan, Jiayu Chen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.08519v1)
- **发表日期**: 2026-03-09
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2603.08519v1](http://arxiv.org/abs/2603.08519v1)
- **📥 PDF**: 已下载至本地 (`2603.08519v1_AtomVLA_Scalable_Post-Training_for_Robotic_Manipulation_via_Predictive_Latent_World_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型在通用机器人操作任务中展现出巨大潜力。通过强化指令对齐，可显著提升VLA模型执行复杂多步骤行为的能力，这是实现有效控制的关键环节。然而，当前范式在监督微调阶段主要依赖粗粒度的高层任务指令。这种指令对齐的缺失使模型缺乏明确的中间过程指导，导致长周期任务中出现严重的误差累积问题。因此，弥合指令鸿沟并为VLA模型提供可扩展的后训练方法迫在眉睫。为解决这一难题，我们提出\method——首个融合可扩展离线后训练流程的原子化任务感知VLA框架。该框架利用大语言模型将高层演示分解为细粒度的原子子任务，通过预训练的预测世界模型在潜在空间中对候选动作片段进行子任务目标匹配评分，从而有效抑制误差累积，显著提升长周期任务的鲁棒性。此外，该方法支持高效的群体相对策略优化，避免了在实体机器人上进行在线试错的高昂成本。大量仿真实验验证了AtomVLA在干扰环境下保持卓越鲁棒性：相较于基础基准模型，其在LIBERO基准测试中平均成功率高达97.0%，在LIBERO-PRO基准测试中达到48.0%。最后，基于Galaxea R1 Lite平台的实体实验证实了该框架在多样化任务（特别是长周期任务）中的广泛适用性。所有数据集、模型检查点及代码将在本文录用后公开发布，以促进后续研究。

---

### 3. Spherical-GOF: Geometry-Aware Panoramic Gaussian Opacity Fields for 3D Scene Reconstruction

- **作者**: Zhe Yang, Guoqiang Zhao, Sheng Wu, Kai Luo, Kailun Yang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.08503v1)
- **发表日期**: 2026-03-09
- **匹配关键词**: 3D gaussian splatting, gaussian splatting
- **arXiv**: [2603.08503v1](http://arxiv.org/abs/2603.08503v1)
- **📥 PDF**: 已下载至本地 (`2603.08503v1_Spherical-GOF_Geometry-Aware_Panoramic_Gaussian_Opacity_Fields_for_3D_Scene_Reconstruction.pdf`)
- **🔓 开源**: CODE, GITHUB
  - 链接：https://github.com/1170632760/Spherical-GOF.
- **中文摘要**: 全向图像因其宽广的视野在机器人与视觉领域应用日益广泛。然而，将三维高斯泼溅（3DGS）扩展至全景相机模型仍面临挑战，现有方法专为透视投影设计，简单适配常导致畸变与几何不一致问题。本文提出Spherical-GOF——基于高斯不透明度场（GOF）构建的全向高斯渲染框架。区别于基于投影的光栅化方法，Spherical-GOF直接在球面射线空间的单位球体上进行GOF射线采样，实现了全景渲染中射线-高斯相互作用的几何一致性。为提升球面射线投射的效率和鲁棒性，我们推导出用于快速射线-高斯剔除的保守球面边界规则，并引入自适应高斯足迹的球面滤波方案，以应对全景像素采样中的动态畸变。在标准全景基准数据集（OmniBlender与OmniPhotos）上的大量实验表明，本方法在光度质量上具有竞争力，并显著提升了几何一致性：相较于最强基线模型，Spherical-GOF将深度重投影误差降低57%，循环匹配内点率提升21%。定性结果显示更清晰的深度图与更连贯的法向图，且对全景图像旋转具有强鲁棒性。我们进一步在OmniRob数据集上验证了泛化能力，该现实世界机器人全向数据集包含无人机与四足机器人平台，为本研究首次提出。源代码与OmniRob数据集将在https://github.com/1170632760/Spherical-GOF 公开。

---

### 4. Improving Continual Learning for Gaussian Splatting based Environments Reconstruction on Commercial Off-the-Shelf Edge Devices

- **作者**: Ivan Zaino, Matteo Risso, Daniele Jahier Pagliari, Miguel de Prado, Toon Van de Maele, Alessio Burrello
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.08499v1)
- **发表日期**: 2026-03-09
- **匹配关键词**: navigation, gaussian splatting
- **arXiv**: [2603.08499v1](http://arxiv.org/abs/2603.08499v1)
- **📥 PDF**: 已下载至本地 (`2603.08499v1_Improving_Continual_Learning_for_Gaussian_Splatting_based_Environments_Reconstruction_on_Commercial_.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 新颖视角合成（NVS）在边缘机器人领域日益重要，这类应用需要在严格的内存和延迟限制下，为SLAM、导航与巡检任务构建紧凑且可增量更新的三维场景模型。变分贝叶斯高斯泼溅算法通过维护概率化场景模型，实现了对3DGS算法的免回放持续更新，但其高精度计算和庞大的中间张量使得设备端训练难以实现。本研究提出一种精度自适应优化框架，可在不改变变分理论框架的前提下，在资源受限硬件上实现VBGS训练。我们（i）通过性能剖析定位内存/延迟瓶颈，（ii）融合内存密集型内核以减少实体化中间张量，（iii）采用相对误差约束的混合精度搜索自动分配操作级精度。在Blender、Habitat和Replica数据集上的实验表明，优化后的流程在A5000 GPU上将峰值内存从9.44GB降至1.11GB，训练时间从约234分钟缩短至约61分钟，同时保持（部分场景甚至提升）了当前最优VBGS基准的重建质量。我们首次在Jetson Orin Nano商用嵌入式平台上实现了NVS训练，其单帧处理延迟较3DGS降低了19倍。

---

### 5. R2F: Repurposing Ray Frontiers for LLM-free Object Navigation

- **作者**: Francesco Argenziano, John Mark Alexis Marcelo, Michele Brienza, Abdel Hakim Drid, Emanuele Musumeci, Daniele Nardi, Domenico D. Bloisi, Vincenzo Suriani
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.08475v1)
- **发表日期**: 2026-03-09
- **匹配关键词**: navigation, VLN, exploration
- **arXiv**: [2603.08475v1](http://arxiv.org/abs/2603.08475v1)
- **📥 PDF**: 已下载至本地 (`2603.08475v1_R2F_Repurposing_Ray_Frontiers_for_LLM-free_Object_Navigation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 零样本开放词汇物体导航随着大型视觉语言模型和大型语言模型的出现迅速发展，这些模型现已被广泛用作高级决策器而非端到端策略。尽管有效，此类系统在推理时通常依赖迭代式大模型查询，引入了延迟和计算开销，限制了实时部署。为解决这一问题，我们重新利用最近提出的基于前沿探索范式——射线前沿，开发了一种无需LLM的室内开放词汇物体导航框架。虽然射线前沿最初用于通过射线携带的语义线索引导探索，但我们重新将前沿区域解释为显式的方向条件语义假设，作为导航目标。沿超范围射线累积的语言对齐特征被稀疏存储在前沿区域，每个区域维护多个方向嵌入编码可能存在的未见内容。通过这种方式，导航简化为基于嵌入的前沿评分和经典建图与规划流程中的目标追踪，消除了迭代式大模型推理。我们进一步提出R2F-VLN，这是一种通过句法解析和关系验证处理自由形式语言指令的轻量级扩展方案，无需额外VLM或LLM组件。在Habitat仿真环境和真实机器人平台上的实验表明，该方法在保持实时执行的同时实现了具有竞争力的零样本性能，运行速度比基于VLM的替代方案快达6倍。

---

### 6. $Δ$VLA: Prior-Guided Vision-Language-Action Models via World Knowledge Variation

- **作者**: Yijie Zhu, Jie He, Rui Shao, Kaishen Yuan, Tao Tan, Xiaochen Yuan, Zitong Yu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.08361v1)
- **发表日期**: 2026-03-09
- **匹配关键词**: vision-language-action, VLA, vision-language-action model
- **arXiv**: [2603.08361v1](http://arxiv.org/abs/2603.08361v1)
- **📥 PDF**: 已下载至本地 (`2603.08361v1_$Δ$VLA_Prior-Guided_Vision-Language-Action_Models_via_World_Knowledge_Variation.pdf`)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/JiuTian-VL/DeltaVLA.
- **中文摘要**: 近期视觉-语言-动作（VLA）模型通过统一感知、推理与控制能力，显著推动了机器人操作技术的发展。为实现这种集成，现有研究多采用预测范式，通过建模未来视觉状态或世界知识来指导动作生成。然而，这些模型侧重于预测结果而非推理变化的内在过程，而后者对决策行动方式至关重要。为此，我们提出$Δ$VLA框架——一种基于先验引导的建模方法，该框架通过显式的当前世界知识先验来建模世界知识变化以生成动作，而非直接回归绝对化的未来世界状态。具体而言：1）为构建当前世界知识先验，我们提出先验引导的世界知识提取器（PWKE）。该模块在辅助头部和先验伪标签引导下，从视觉输入中提取可操作区域、空间关系及语义线索，从而降低信息冗余。2）在此基础上，为表征世界知识在动作影响下的演化过程，我们提出潜在世界变化量化器（LWVQ）。该模块通过VQ-VAE目标学习离散潜在空间，以编码世界知识变化，将预测任务从全模态转换至紧凑的潜在表示。3）此外，为减少变化建模过程中的干扰，我们设计了条件变化注意力机制（CV-Atten），该机制促进解耦学习并保持知识表示的独立性。在仿真基准测试和真实机器人任务中的大量实验表明，$Δ$VLA在提升效率的同时实现了最先进的性能。代码与真实执行视频已发布于https://github.com/JiuTian-VL/DeltaVLA。

---

### 7. EndoSERV: A Vision-based Endoluminal Robot Navigation System

- **作者**: Junyang Wu, Fangfang Xie, Minghui Zhang, Hanxiao Zhang, Jiayuan Sun, Yun Gu, Guang-Zhong Yang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.08324v1)
- **发表日期**: 2026-03-09
- **匹配关键词**: navigation, robot navigation
- **arXiv**: [2603.08324v1](http://arxiv.org/abs/2603.08324v1)
- **📥 PDF**: 已下载至本地 (`2603.08324v1_EndoSERV_A_Vision-based_Endoluminal_Robot_Navigation_System.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 机器人辅助腔内手术在早期癌症干预中的应用日益广泛。然而，腔内解剖结构中错综复杂、狭窄曲折的路径给机器人导航带来了巨大挑战。基于视觉的导航技术提供了有前景的解决方案，但由于组织形变、体内伪影以及缺乏可用于持续定位的显著标志物，现有定位方法容易产生误差。本文提出了一种新颖的EndoSERV定位方法以应对这些挑战。该方法包含两个主要部分：**SE**段到结构映射与**R**实景到**V**虚拟映射，故得此名。针对长距离复杂腔体结构，我们将其划分为较小的子段并独立估计里程信息。为解决标注数据不足的问题，采用高效迁移技术将真实图像特征映射至虚拟域，从而利用虚拟姿态真值进行训练。EndoSERV的训练阶段包括离线预训练以提取纹理无关特征，以及适应真实场景的在线训练阶段。基于公共数据集和临床数据集的大量实验表明，该方法即使在没有真实姿态标注的情况下仍能保持卓越性能。

---

### 8. SaiVLA-0: Cerebrum--Pons--Cerebellum Tripartite Architecture for Compute-Aware Vision-Language-Action

- **作者**: Xiang Shi, Wenlong Huang, Menglin Zou, Xinhai Sun
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.08124v1)
- **发表日期**: 2026-03-09
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2603.08124v1](http://arxiv.org/abs/2603.08124v1)
- **📥 PDF**: 已下载至本地 (`2603.08124v1_SaiVLA-0_Cerebrum--Pons--Cerebellum_Tripartite_Architecture_for_Compute-Aware_Vision-Language-Action.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 我们通过神经科学启发的三元结构重新审视视觉-语言-动作系统。生物学上，大脑皮层提供稳定的高级多模态先验并保持冻结；脑桥适配器将这些皮层特征与实时本体感觉输入整合，并将意图编译为可执行的指令；小脑模块通过滞后/指数移动平均/温度/熵机制实现快速并行的分类解码以进行在线稳定控制。固定比例调度与两阶段特征缓存使系统具备计算感知与可复现性。受主动注视视觉启发，我们通过标定投影将手腕关注区域几何绑定至末端执行器，提供运动稳定的高分辨率视角，该视角对精细姿态变化敏感，同时与主视角的全局上下文形成互补。

该设计采用模块化架构：仅升级大脑皮层时只需重训练脑桥模块；更换机器人仅需训练小脑模块；纯小脑强化学习可在不触及高层语义的情况下进一步优化控制。作为概念与原型验证论文，我们制定了匹配条件（GPU、分辨率、批次）下的时序协议以验证预期效率提升。初步LIBERO实验表明：在官方N1.5仅头部训练条件下，分离式特征缓存将训练时间从7.5小时缩短至4.5小时，平均成功率从86.5%提升至92.5%；SaiVLA0模型达到99.0%的平均成功率。

---

### 9. Towards Human-Like Manipulation through RL-Augmented Teleoperation and Mixture-of-Dexterous-Experts VLA

- **作者**: Tutian Tang, Xingyu Ji, Wanli Xing, Ce Hao, Wenqiang Xu, Lin Shao, Cewu Lu, Qiaojun Yu, Jiangmiao Pang, Kaifeng Zhang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.08122v1)
- **发表日期**: 2026-03-09
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2603.08122v1](http://arxiv.org/abs/2603.08122v1)
- **📥 PDF**: 已下载至本地 (`2603.08122v1_Towards_Human-Like_Manipulation_through_RL-Augmented_Teleoperation_and_Mixture-of-Dexterous-Experts_.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 尽管视觉-语言-动作模型在机器人操作领域已展现出卓越成效，但其应用范围主要局限于执行简单视觉引导抓放任务的低自由度末端执行器。将这些模型扩展至类人双手灵巧操作——特别是涉及密集接触的手内操作——在高保真数据采集、多技能学习及多模态感知融合方面提出了关键挑战。本文提出一个集成框架以突破这些瓶颈，该框架基于两大核心组件构建。首先，我们推出IMCopilot（手内操作协同系统），这套通过强化学习训练的原子技能集具备双重功能：既可作为简化遥操作数据采集的共享自主辅助系统，又能作为视觉-语言-动作模型可调用的底层执行原语。其次，我们提出MoDE-VLA（灵巧专家混合视觉-语言-动作模型），该架构将异构力觉与触觉模态无缝集成至预训练的视觉-语言-动作主干网络。通过残差注入机制，MoDE-VLA能在保持模型预训练知识完整性的同时实现接触感知精细化。我们在四个复杂度递增的任务上验证了该方法的有效性，实验表明在密集接触的灵巧操作任务中，成功率较基线模型提升达两倍。

---

### 10. Dual-Horizon Hybrid Internal Model for Low-Gravity Quadrupedal Jumping with Hardware-in-the-Loop Validation

- **作者**: Haozhe Xu, Yifei Zhao, Wenhao Feng, Zhipeng Wang, Hongrui Sang, Cheng Cheng, Xiuxian Li, Zhen Yin, Bin He
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.07999v1)
- **发表日期**: 2026-03-09
- **匹配关键词**: exploration
- **arXiv**: [2603.07999v1](http://arxiv.org/abs/2603.07999v1)
- **📥 PDF**: 已下载至本地 (`2603.07999v1_Dual-Horizon_Hybrid_Internal_Model_for_Low-Gravity_Quadrupedal_Jumping_with_Hardware-in-the-Loop_Val.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 在低重力环境下，移动通常通过跳跃实现，然而月球重力下的连续蹦跳仍面临挑战，主要源于长时间空中飞行阶段和稀疏的地面接触。延长的空中飞行时间增加了着陆冲击敏感性，并使得在崎岖行星地形上实现稳定姿态调控变得困难。现有方法主要针对平坦表面的单次跳跃，既缺乏连续地形解决方案，也缺少真实的硬件验证。本研究提出一种双视野混合内部模型，仅通过本体感知实现月球重力下的四足机器人连续跳跃。两个时间编码器捕捉互补的时间尺度：短视野分支通过显式垂直速度估计建模快速垂直动力学，而长视野分支则建模跳跃周期内的水平运动趋势和质心高度演变。融合后的表征使得在月球重力特有的延长空中阶段下实现稳定连续跳跃成为可能。为提供硬件在环验证，我们开发了MATRIX（混合现实自适应机器人集成探索测试平台）——一个通过滑轮配重机制卸载重力、并将虚幻引擎月球地形实时映射至运动平台和跑步机的数字孪生驱动系统。利用MATRIX平台，我们在模拟月球重力的陨石坑类月表地形上，成功演示了四足机器人的连续跳跃能力。

---

### 11. ImprovedGS+: A High-Performance C++/CUDA Re-Implementation Strategy for 3D Gaussian Splatting

- **作者**: Jordi Muñoz Vicente
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.08661v1)
- **发表日期**: 2026-03-09
- **匹配关键词**: 3D gaussian splatting, nerf, gaussian splatting
- **arXiv**: [2603.08661v1](http://arxiv.org/abs/2603.08661v1)
- **📥 PDF**: 已下载至本地 (`2603.08661v1_ImprovedGS+_A_High-Performance_C++CUDA_Re-Implementation_Strategy_for_3D_Gaussian_Splatting.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 三维高斯泼溅（3DGS）技术的最新进展正将研究重心转向重建精度与计算效率的平衡。本研究提出ImprovedGS+，作为ImprovedGS策略的高性能底层重构方案，并原生集成于LichtFeld-Studio框架。通过将高层Python逻辑迁移至硬件优化的C++/CUDA内核，我们显著降低了主机-设备同步开销与训练延迟。该实现引入了长轴分割（LAS）CUDA内核、基于拉普拉斯算子的自定义重要性核（配合非极大值抑制的边缘评分机制）以及自适应指数尺度调度器。在Mip-NeRF360数据集上的实验表明，ImprovedGS+为场景重建建立了新的帕累托最优前沿：在100万参数预算条件下，相比最先进的MCMC基线方法，训练时间缩短26.8%（单次训练节省17分钟），高斯元素使用量减少13.3%，同时保持更优的视觉质量；完整参数版本较ADC基线实现1.28 dB的峰值信噪比提升，且参数量降低38.4%。这些成果验证了ImprovedGS+作为可扩展高速解决方案的有效性，在LichtFeld-Studio生态系统中成功践行了速度、质量与易用性三大核心原则。

---

### 12. HDR-NSFF: High Dynamic Range Neural Scene Flow Fields

- **作者**: Shin Dong-Yeon, Kim Jun-Seong, Kwon Byung-Ki, Tae-Hyun Oh
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.08313v1)
- **发表日期**: 2026-03-09
- **匹配关键词**: neural radiance field, gaussian splatting
- **arXiv**: [2603.08313v1](http://arxiv.org/abs/2603.08313v1)
- **📥 PDF**: 已下载至本地 (`2603.08313v1_HDR-NSFF_High_Dynamic_Range_Neural_Scene_Flow_Fields.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://shin-dong-yeon.github.io/HDR-NSFF/
- **中文摘要**: 真实世界场景的辐射亮度范围通常远超标准相机所能捕捉的动态范围。传统高动态范围成像方法通过融合交替曝光帧实现，但这些方法本质上受限于二维像素级对齐，在动态场景中常导致重影伪影与时间不一致性问题。为解决这些局限，我们提出HDR-NSFF范式——从基于二维的融合转向四维时空建模。该框架通过将场景表征为时空连续函数，从交替曝光的单目视频中重建动态高动态范围辐射场，兼容神经辐射场与基于四维高斯溅射的动态表征方法。这一统一的端到端流程显式建模高动态范围辐射、三维场景流、几何结构与色调映射，确保物理合理性与全局一致性。我们通过以下方式进一步提升鲁棒性：(一)扩展基于语义的光流方法，利用DINO特征实现曝光不变的运动估计；(二)引入生成式先验作为正则化器，以补偿单目拍摄中有限的观测信息及饱和区域导致的数据损失。为评估高动态范围时空视角合成效果，我们首次构建了专为动态高动态范围场景设计的真实世界数据集HDR-GoPro。实验表明，即使在极具挑战性的曝光变化条件下，HDR-NSFF仍能恢复精细的辐射细节与连贯的动态表现，从而在新型时空视角合成任务中达到最先进性能。项目主页：https://shin-dong-yeon.github.io/HDR-NSFF/

---

### 13. Seed2Scale: A Self-Evolving Data Engine for Embodied AI via Small to Large Model Synergy and Multimodal Evaluation

- **作者**: Cong Tai, Zhaoyu Zheng, Haixu Long, Hansheng Wu, Zhengbin Long, Haodong Xiang, Rong Shi, Zhuo Cui, Shizhuang Zhang, Gang Qiu, He Wang, Ruifeng Li, Biao Liu, Zhenzhe Sun, Tao Shen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.08260v1)
- **发表日期**: 2026-03-09
- **匹配关键词**: vision-language-action, exploration, vision-language-action model
- **arXiv**: [2603.08260v1](http://arxiv.org/abs/2603.08260v1)
- **📥 PDF**: 已下载至本地 (`2603.08260v1_Seed2Scale_A_Self-Evolving_Data_Engine_for_Embodied_AI_via_Small_to_Large_Model_Synergy_and_Multimod.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://terminators2025.github.io/Seed2Scale.github.io
- **中文摘要**: 现有数据生成方法存在探索局限、具身鸿沟和低信噪比等问题，导致自我迭代过程中性能下降。为解决这些挑战，我们提出Seed2Scale——一种通过"小模型采集、大模型评估、目标模型学习"的异构协同机制突破数据瓶颈的自演进数据引擎。该引擎仅需四个初始演示样本即可启动，采用轻量级视觉-语言-动作模型SuperTiny作为专用采集器，利用其强归纳偏置在并行环境中实现鲁棒探索。同时引入预训练视觉-语言模型作为验证器，对海量生成轨迹进行自主成败判定与质量评分。Seed2Scale有效缓解模型坍塌现象，确保自演进过程的稳定性。实验结果表明，Seed2Scale展现出显著的扩展潜力：随着迭代推进，目标模型成功率呈现稳健上升趋势，实现131.2%的性能提升。此外，Seed2Scale显著优于现有数据增强方法，为通用具身人工智能的大规模发展提供了可扩展且经济高效的路径。项目主页：https://terminators2025.github.io/Seed2Scale.github.io

---

### 14. FlowTouch: View-Invariant Visuo-Tactile Prediction

- **作者**: Seongjin Bien, Carlo Kneissl, Tobias Jülg, Frank Fundel, Thomas Ressler-Antal, Florian Walter, Björn Ommer, Gitta Kutyniok, Wolfram Burgard ⭐
  - **高亮作者**: Wolfram Burgard
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.08255v1)
- **发表日期**: 2026-03-09
- **匹配关键词**: contact-rich manipulation
- **arXiv**: [2603.08255v1](http://arxiv.org/abs/2603.08255v1)
- **📥 PDF**: 已下载至本地 (`2603.08255v1_FlowTouch_View-Invariant_Visuo-Tactile_Prediction.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 触觉感知对于接触密集型操作任务至关重要。它能提供关于物体几何形状、表面特性和相互作用力的直接反馈，从而增强感知能力并实现精细控制。触觉传感器的一个固有局限是，只有在接触物体时才能获取读数，这限制了其在任务规划和初始执行阶段的应用。通过视觉信息预测触觉信息可以弥补这一不足。常见方法是学习从相机图像到视觉触觉传感器输出的直接映射，但所得模型会高度依赖特定设置及相机捕捉物体接触区域的能力。本研究提出FlowTouch——一种新颖的视角不变视觉触觉预测模型。其核心思想是利用物体的局部三维网格编码丰富信息以预测触觉模式，同时抽象掉场景相关细节。FlowTouch融合了场景重建与基于流匹配的图像生成模型。实验结果表明，FlowTouch能够弥合仿真与现实的差距，并泛化至新的传感器实例。我们进一步证明，生成的触觉图像可用于下游抓握稳定性预测。相关代码、数据集及演示视频已发布于https://flowtouch.github.io/。

---

### 15. SAMoE-VLA: A Scene Adaptive Mixture-of-Experts Vision-Language-Action Model for Autonomous Driving

- **作者**: Zihan You, Hongwei Liu, Chenxu Dang, Zhe Wang, Sining Ang, Aoqi Wang, Yan Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.08113v1)
- **发表日期**: 2026-03-09
- **匹配关键词**: vision-language-action, VLA, vision-language-action model
- **arXiv**: [2603.08113v1](http://arxiv.org/abs/2603.08113v1)
- **📥 PDF**: 已下载至本地 (`2603.08113v1_SAMoE-VLA_A_Scene_Adaptive_Mixture-of-Experts_Vision-Language-Action_Model_for_Autonomous_Driving.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型的最新进展通过利用大语言模型（LLMs）的理解与推理优势，在自动驾驶领域展现出巨大潜力。然而，我们的实证分析表明，直接将现有继承自LLM架构的令牌级混合专家（MoE）机制应用于VLA模型，会导致自动驾驶性能不稳定与安全性下降，这凸显了基于令牌的专家专业化与场景级决策之间存在错配问题。为此，我们提出SAMoE-VLA——一种场景自适应的视觉-语言-动作框架，该框架基于结构化场景表征（而非令牌嵌入）进行专家选择。我们的核心思想是从鸟瞰图（BEV）特征中提取MoE路由信号，该特征封装了交通场景上下文，从而实现对不同驾驶条件定制化的场景依赖型专家加权与融合。此外，为支持跨世界知识、感知、语言与动作的时序一致性推理，我们提出条件跨模态因果注意力机制，将世界状态、语言意图与动作历史整合到统一的因果推理过程中。在nuScenes开环规划数据集与LangAuto闭环基准测试上的大量实验表明，SAMoE-VLA以更少的参数量实现了最先进的性能，超越了现有基于VLA和世界模型的方法。我们的代码即将开源。

---

## 📌 Poster

*其他相关研究*

---

### 1. Diff-Muscle: Efficient Learning for Musculoskeletal Robotic Table Tennis

- **作者**: Wentao Zhao, Jun Guo, Kangyao Huang, Xin Liu, Huaping Liu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.08617v1)
- **发表日期**: 2026-03-09
- **匹配关键词**: exploration
- **arXiv**: [2603.08617v1](http://arxiv.org/abs/2603.08617v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 肌肉骨骼机器人因其卓越的灵活性与灵巧性优势，成为实现具身智能的重要前沿方向。然而，现有研究多局限于相对简单的任务场景，限制了对其多段协调潜能的深入探索。高效学习仍是当前主要挑战，这主要源于高维动作空间与固有的过驱动结构。为应对这些挑战，我们提出Diff-Muscle算法——一种基于微分平坦性的肌肉骨骼机器人控制方法，通过将策略学习从冗余的肌肉激活空间重构至维度显著降低的关节空间。我们进一步采用高度动态的机器人乒乓球任务验证算法性能，提出融合基于运动学的肌肉驱动控制器与高层轨迹规划的层级强化学习框架，使肌肉骨骼机器人能够完成灵巧精准的连续对打。实验结果表明，Diff-Muscle在保持最低肌肉激活水平的同时，其成功率显著优于现有先进基线方法。值得注意的是，该框架成功实现了肌肉骨骼机器人在极具挑战性的双机器人对打场景中完成连续回合击球。

---

### 2. Bilevel Planning with Learned Symbolic Abstractions from Interaction Data

- **作者**: Fatih Dogangun, Burcu Kilic, Serdar Bahar, Emre Ugur
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.08599v1)
- **发表日期**: 2026-03-09
- **匹配关键词**: exploration, object manipulation
- **arXiv**: [2603.08599v1](http://arxiv.org/abs/2603.08599v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 智能体必须在复杂环境中同时处理连续动态与离散表征，才能生成有效规划。先前研究表明，通过机器人无监督探索训练的神经效应预测器可自发形成符号抽象。然而这些方法依赖确定性符号域，缺乏验证生成符号规划的机制，且仅在抽象层面运行，往往难以捕捉环境的连续动态特性。为突破这些局限，我们提出双层神经符号框架：高层通过习得的概率符号规则快速生成候选规划，底层通过习得的连续效应模型验证这些规划并在必要时执行前向搜索。在多物体操控任务中的实验表明，所提出的双层方法优于纯符号方法，能通过验证可靠识别失败规划，其规划性能在统计意义上与连续前向搜索相当，同时通过高效符号推理解决了大多数问题。

---

### 3. The Neural Compass: Probabilistic Relative Feature Fields for Robotic Search

- **作者**: Gabriele Somaschini, Adrian Röfer, Abhinav Valada
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.08544v1)
- **发表日期**: 2026-03-09
- **匹配关键词**: exploration
- **arXiv**: [2603.08544v1](http://arxiv.org/abs/2603.08544v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 物体共现关系为在陌生环境中成功高效地寻找目标提供了关键线索。通常人们会在厨房中寻找杯子，并将冰箱的存在视为身处厨房的证据。这类先验知识也已被应用于智能体设计中，但通常依赖于显式标注数据的学习或语言模型的查询。目前尚不清楚这些关系能否仅通过未标注的观察数据实现隐式学习。本研究针对该问题提出ProReFF模型——一种经过训练的特征场模型，旨在预测从预训练视觉语言模型中获取的特征相对分布。此外，我们引入基于学习的对齐策略，通过将不一致的观测数据整合为连贯的相对分布，实现从未标注且可能存在矛盾的数据中进行训练。针对下游物体搜索任务，我们设计了利用预测特征分布作为语义先验的智能体，引导探索过程指向目标物体高概率出现区域。通过大量实验评估表明：ProReFF能有效捕捉自然场景中有意义的相对特征分布，并揭示所提对齐步骤的实际影响。我们在Matterport3D模拟器中设置100项挑战任务进一步评估搜索智能体性能，与基于特征的基线方法及人类参与者进行对比。实验证明，所提出的智能体搜索效率比最强基线提升20%，最高可达人类表现水平的80%。

---

### 4. EquiBim: Learning Symmetry-Equivariant Policy for Bimanual Manipulation

- **作者**: Zhiyuan Zhang, Aditya Mohan, Seungho Han, Wan Shou, Dongyi Wang, Yu She
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.08541v1)
- **发表日期**: 2026-03-09
- **匹配关键词**: bimanual manipulation
- **arXiv**: [2603.08541v1](http://arxiv.org/abs/2603.08541v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 机器人模仿学习在从演示中学习复杂操作行为方面取得了显著成功。然而，许多现有机器人学习方法未能显式考虑机器人系统的物理对称性，常导致在对称观测条件下产生不对称或不一致的行为。这一局限在双臂操作中尤为突出，因为机器人形态与多数任务结构本身具有双边对称特性。本文提出EquiBim——一种面向双手操作的对称等变策略学习框架，通过在训练中强制实施观测与动作间的双边等变性来应对该问题。我们的方法将物理对称性表述为观测空间与动作空间上的群作用，并对对称变换下的策略预测施加等变约束。该框架具有模型无关性，可无缝集成到多种观测模态与动作表征的模仿学习流程中，包括基于点云和图像的策略，以及末端执行器空间与关节空间参数化方法。我们在具有对称运动学的双臂机器人平台RoboTwin上评估EquiBim，通过仿真实验测试了多种观测与动作配置方案，并进一步在真实世界双臂系统上进行验证。仿真与实体实验结果表明，我们的方法能持续提升分布偏移下的性能与鲁棒性。这些发现表明，显式强化物理对称性为双手机器人学习提供了一种简单而有效的归纳偏置。

---

### 5. FoMo: A Multi-Season Dataset for Robot Navigation in Forêt Montmorency

- **作者**: Matěj Boxan, Gabriel Jeanson, Alexander Krawciw, Effie Daum, Xinyuan Qiao, Sven Lilge, Timothy D. Barfoot, François Pomerleau
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.08433v1)
- **发表日期**: 2026-03-09
- **匹配关键词**: navigation, robot navigation, localization and mapping
- **arXiv**: [2603.08433v1](http://arxiv.org/abs/2603.08433v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 福雷蒙莫朗西（FoMo）数据集是一项为期一年的全面多季节数据采集成果，记录于北方森林环境中。该数据集融合了铺装与非铺装道路的独特组合，并包含显著的环境变化，对现有里程计与SLAM技术流程提出了挑战。数据亮点包括积雪厚度超过1米、传感器前方植被显著生长，以及平台在牵引极限下的运行状态。FoMo数据集共涵盖六条多样化轨迹，总长度超过64公里，全年通过12次部署实现重复采集。数据集包含一台旋转式激光雷达与一台混合固态激光雷达、一台调频连续波雷达、立体相机与广角单目相机采集的全高清图像，以及两台惯性测量单元的数据。地面真值通过后处理安装在无人地面车辆上的三台GNSS接收器及静态GNSS基站数据计算得出。所有序列均附带额外元数据，包括现场气象站每分钟一次的观测记录、相机标定内参及车辆功耗信息。为凸显数据集价值，我们针对激光雷达-惯性、雷达-陀螺仪及视觉-惯性定位建图技术对季节变化的鲁棒性进行了初步评估，结果表明季节变化对现有先进方法的重新定位能力产生显著影响。数据集及开发工具包可通过https://fomo.norlab.ulaval.ca获取。

---

