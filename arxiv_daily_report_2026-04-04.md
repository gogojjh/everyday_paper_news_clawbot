# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-04-04 08:03

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 9/20 篇提供

**🌟 Highlight**: 11 篇 | **📌 Poster**: 9 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. HyVGGT-VO: Tightly Coupled Hybrid Dense Visual Odometry with Feed-Forward Models

- **作者**: Junxiang Pan, Lipu Zhou, Baojie Chen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.02107v1)
- **发表日期**: 2026-04-02
- **匹配关键词**: 3D reconstruction, 3d reconstruction
- **arXiv**: [2604.02107v1](http://arxiv.org/abs/2604.02107v1)
- **📥 PDF**: 已下载至本地 (`2604.02107v1_HyVGGT-VO_Tightly_Coupled_Hybrid_Dense_Visual_Odometry_with_Feed-Forward_Models.pdf`)
- **🔓 开源**: PROJECT_PAGE, CODE
  - 链接：https://geneta2580.github.io/HyVGGT-VO.io.
- **中文摘要**: 密集视觉里程计（VO）能够提供姿态估计与稠密三维重建，是机器人到增强现实等应用领域的基石。近年来，前馈模型在稠密建图方面展现出卓越能力。然而，当这些模型应用于稠密视觉SLAM系统时，其沉重的计算负担使其仅能在关键帧输出稀疏姿态，仍无法实现实时姿态估计。相比之下，传统稀疏方法虽具备高计算效率和高频姿态输出能力，却缺乏稠密重建功能。为突破这些局限，我们提出HyVGGT-VO——一个将稀疏VO的计算效率与前馈模型稠密重建能力相结合的新型框架。据我们所知，这是首次将传统VO框架与前沿前馈模型VGGT进行紧密耦合的研究。具体而言，我们设计了自适应混合跟踪前端，可动态切换传统光流法与VGGT跟踪头以确保系统鲁棒性。此外，我们引入分层优化框架，联合优化VO姿态与VGGT预测尺度，从而保证全局尺度一致性。相较于现有基于VGGT的方法，本方案处理速度提升约5倍，在室内EuRoC数据集上平均轨迹误差降低85%，在室外KITTI基准测试中误差减少12%。代码将在论文录用后公开。项目页面：https://geneta2580.github.io/HyVGGT-VO.io。

---

### 2. Posterior Optimization with Clipped Objective for Bridging Efficiency and Stability in Generative Policy Learning

- **作者**: Yuhui Chen, Haoran Li, Zhennan Jiang, Yuxing Qin, Yuxuan Wan, Weiheng Liu, Dongbin Zhao
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.01860v1)
- **发表日期**: 2026-04-02
- **匹配关键词**: exploration, VLA
- **arXiv**: [2604.01860v1](http://arxiv.org/abs/2604.01860v1)
- **📥 PDF**: 已下载至本地 (`2604.01860v1_Posterior_Optimization_with_Clipped_Objective_for_Bridging_Efficiency_and_Stability_in_Generative_Po.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://cccedric.github.io/poco/.
- **中文摘要**: 表现力生成模型通过捕捉复杂多模态动作在时间扩展轨迹上的分布，推动了机器人操作技术的发展。然而，由于不稳定性和样本效率低下，通过强化学习对这些策略进行微调仍然具有挑战性。我们提出了一种基于后验优化的裁剪目标框架（POCO），该框架将策略改进构建为针对时序动作块的后验推断问题。通过期望最大化过程，POCO将奖励加权的隐式后验提炼到策略中，无需进行似然估计。此外，POCO采用离线到在线范式，将在线探索锚定在预训练先验上，其模型无关设计可扩展至大型视觉语言动作模型的微调，无需修改架构。在7个仿真基准测试和4个接触密集型现实任务中的评估表明，POCO能防止策略灾难性崩溃，优于最先进的基线方法，并在现实任务中实现了96.7%的成功率。演示视频可在项目网站https://cccedric.github.io/poco/查看。

---

### 3. Realistic Lip Motion Generation Based on 3D Dynamic Viseme and Coarticulation Modeling for Human-Robot Interaction

- **作者**: Sheng Li, Jingcheng Huang, Min Li
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.01756v1)
- **发表日期**: 2026-04-02
- **匹配关键词**: human-robot interaction
- **arXiv**: [2604.01756v1](http://arxiv.org/abs/2604.01756v1)
- **📥 PDF**: 已下载至本地 (`2604.01756v1_Realistic_Lip_Motion_Generation_Based_on_3D_Dynamic_Viseme_and_Coarticulation_Modeling_for_Human-Rob.pdf`)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/yuesheng21/Phoneme-to-Lip-14DOF
- **中文摘要**: 逼真的唇部同步对于人形机器人实现自然的人机非语言交互至关重要。基于这一需求，本文提出了一种基于三维动态视位模型与协同发音建模的唇部运动生成框架。通过分析汉语发音理论，我们基于ARKit标准构建了三维动态视位库，该库提供了连贯的唇部运动先验轨迹。为解决连续语音流中的运动冲突问题，我们开发了包含声韵母解耦与能量调制的协同发音机制。在制定将高维空间唇部运动重定向至人形头部平台14自由度唇部驱动系统的策略后，通过皮尔逊相关系数和平均绝对加加速度指标进行定量消融实验，验证了所提架构的效率和准确性。本研究为人形机器人的语音驱动唇部运动生成提供了一种轻量化、高效率且实用性强的范式。三维动态视位库及实际部署视频已发布于{https://github.com/yuesheng21/Phoneme-to-Lip-14DOF}。

---

### 4. Tex3D: Objects as Attack Surfaces via Adversarial 3D Textures for Vision-Language-Action Models

- **作者**: Jiawei Chen, Simin Huang, Jiawei Du, Shuaihang Chen, Yu Tian, Mingjie Wei, Chao Yu, Zhaoxia Yin
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.01618v1)
- **发表日期**: 2026-04-02
- **匹配关键词**: vision-language-action, vision-language-action model, VLA
- **arXiv**: [2604.01618v1](http://arxiv.org/abs/2604.01618v1)
- **📥 PDF**: 已下载至本地 (`2604.01618v1_Tex3D_Objects_as_Attack_Surfaces_via_Adversarial_3D_Textures_for_Vision-Language-Action_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型在机器人操作任务中展现出强大性能，但其对物理可实现对抗攻击的鲁棒性仍未得到充分探索。现有研究通过语言扰动和二维视觉攻击揭示了系统脆弱性，但这些攻击面要么难以代表真实部署场景，要么在物理真实性上存在局限。相比之下，对抗性三维纹理构成了更具物理可行性和破坏性的威胁，因为它们能自然附着于被操作物体，且更易于在物理环境中部署。然而，将对抗性三维纹理引入VLA系统面临重大挑战：标准三维模拟器无法提供从VLA目标函数到物体外观的可微分优化路径，导致难以实现端到端优化。为此，我们提出前景-背景解耦框架，通过双渲染器对齐实现可微分纹理优化，同时保持原始模拟环境不变。为确保攻击在物理世界长期多视角场景中持续有效，我们进一步提出轨迹感知对抗优化方法，通过行为关键帧优先策略和基于顶点的参数化方案稳定优化过程。基于这些设计，我们构建了Tex3D框架——首个能在VLA模拟环境中实现三维对抗纹理端到端优化的系统。仿真与真实机器人实验表明，Tex3D能在多种操作任务中显著降低VLA模型性能，最高可使任务失败率达到96.7%。我们的实证研究揭示了VLA系统对物理三维对抗攻击的关键脆弱性，强调了鲁棒性感知训练的必要性。

---

### 5. F3DGS: Federated 3D Gaussian Splatting for Decentralized Multi-Agent World Modeling

- **作者**: Morui Zhu, Mohammad Dehghani Tezerjani, Mátyás Szántó, Márton Vaitkus, Song Fu, Qing Yang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.01605v1)
- **发表日期**: 2026-04-02
- **匹配关键词**: 3D reconstruction, 3d reconstruction, gaussian splatting, exploration, 3D gaussian splatting
- **arXiv**: [2604.01605v1](http://arxiv.org/abs/2604.01605v1)
- **📥 PDF**: 已下载至本地 (`2604.01605v1_F3DGS_Federated_3D_Gaussian_Splatting_for_Decentralized_Multi-Agent_World_Modeling.pdf`)
- **🔓 开源**: CODE
- **中文摘要**: 我们提出F3DGS——一个用于去中心化多智能体三维重建的联邦式三维高斯溅射框架。现有三维高斯溅射流程通常假设所有观测数据可集中访问，这限制了其在分布式机器人场景中的应用，因为智能体需独立运行且集中式数据聚合可能受限。直接将集中式训练扩展到多智能体系统会带来通信开销与几何不一致性问题。F3DGS首先通过配准来自多个客户端的局部融合激光雷达点云，构建共享几何骨架以初始化全局三维高斯溅射模型。在联邦优化过程中，高斯位置被固定以保持几何对齐，各客户端仅更新外观相关属性，包括协方差、不透明度与球谐系数。服务器采用可见性感知聚合机制，根据各客户端观测每个高斯的频率对其贡献进行加权，从而解决多智能体探索中固有的部分可观测性挑战。为评估去中心化重建性能，我们收集了包含同步激光雷达、RGB与IMU测量的多序列室内数据集。实验表明，F3DGS在实现跨智能体分布式优化的同时，达到了与集中式训练相当的重建质量。数据集、开发工具包及源代码将公开发布。

---

### 6. Boosting Vision-Language-Action Finetuning with Feasible Action Neighborhood Prior

- **作者**: Haochen Niu, Kanyu Zhang, Shuyu Yin, Qinghai Guo, Peilin Liu, Fei Wen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.01570v1)
- **发表日期**: 2026-04-02
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2604.01570v1](http://arxiv.org/abs/2604.01570v1)
- **📥 PDF**: 已下载至本地 (`2604.01570v1_Boosting_Vision-Language-Action_Finetuning_with_Feasible_Action_Neighborhood_Prior.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 在现实世界的机器人操作中，状态通常允许存在一个近似等效动作的邻域。也就是说，对于每个状态，存在一个可行动作邻域（FAN）而非单一正确动作，在该邻域内的运动会产生难以区分的进展。然而，当前主流的视觉语言动作模型训练方法直接沿袭自语言处理领域，未能利用FAN特性，从而导致泛化能力差和样本效率低下。为突破这一局限，我们提出了一种FAN引导的正则化方法，通过调整模型输出分布以匹配FAN的几何特性。具体而言，我们引入高斯先验来促进预测在优选方向和幅度附近保持局部平滑与单峰性。在强化微调与监督微调的大量实验中，我们的方法在样本效率、分布内场景与分布外场景的成功率方面均取得显著提升。通过与物理操作内在动作容差特性对齐，FAN引导的正则化为实现样本高效、泛化能力强的视觉语言动作模型适配提供了原理清晰且切实可行的解决方案。

---

### 7. Compact Keyframe-Optimized Multi-Agent Gaussian Splatting SLAM

- **作者**: Monica M. Q. Li, Pierre-Yves Lajoie, Jialiang Liu, Giovanni Beltrame
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.00804v1)
- **发表日期**: 2026-04-01
- **匹配关键词**: localization and mapping, gaussian splatting
- **arXiv**: [2604.00804v1](http://arxiv.org/abs/2604.00804v1)
- **📥 PDF**: 已下载至本地 (`2604.00804v1_Compact_Keyframe-Optimized_Multi-Agent_Gaussian_Splatting_SLAM.pdf`)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/lemonci/coko-slam
- **中文摘要**: 高效的多智能体三维建图对于在未知环境中运行的机器人团队至关重要，但稠密表示法会阻碍其在受限通信链路上的实时交换。在多智能体同步定位与建图（SLAM）系统中，通常依赖中央服务器来合并和优化各智能体生成的局部地图。然而，在带宽受限的实际场景中，共享这些大规模地图表示——特别是由高斯泼溅等最新方法生成的地图——成为性能瓶颈。本文提出一种改进的多智能体RGB-D高斯泼溅SLAM框架，在保持地图保真度的同时显著降低通信负载。首先，我们在SLAM系统中引入压缩步骤以消除冗余的三维高斯元素，且不降低渲染质量。其次，该方法无需初始猜测即可执行集中式闭环检测计算，提供两种运行模式：纯渲染深度模式（仅需三维高斯数据）和相机深度模式（通过轻量级深度图像提升配准精度并实现额外的高斯剪枝）。在合成数据集和真实数据集上的评估表明，相较于现有先进方法，两种模式的传输数据量均减少85-95%，使三维高斯多智能体SLAM技术更接近实际场景的应用部署。代码地址：https://github.com/lemonci/coko-slam

---

### 8. Learning Humanoid Navigation from Human Data

- **作者**: Weizhuo Wang, Yanjie Ze, C. Karen Liu, Monroe Kennedy
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.00416v1)
- **发表日期**: 2026-04-01
- **匹配关键词**: navigation
- **arXiv**: [2604.00416v1](http://arxiv.org/abs/2604.00416v1)
- **📥 PDF**: 已下载至本地 (`2604.00416v1_Learning_Humanoid_Navigation_from_Human_Data.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 我们推出EgoNav系统，该系统使仿人机器人能够仅通过5小时人类行走数据的学习，即可穿越多样且未见过的环境，无需任何机器人数据或微调。该系统采用扩散模型预测未来可能轨迹的分布，条件包括历史轨迹、融合色彩、深度与语义信息的360度视觉记忆，以及来自冻结DINOv3骨干网络的视频特征——这些特征能捕捉深度传感器无法察觉的外观线索。通过混合采样方案实现10步去噪的实时推理，并采用滚动时域控制器从预测分布中选择路径。我们通过离线评估验证EgoNav性能，其在避障和多模态覆盖方面均优于基线模型；同时在Unitree G1仿人机器人上进行零样本部署测试，成功穿越未见过的室内外环境。系统自然涌现出等待开门、绕行人群、规避玻璃墙等行为。我们将公开数据集与训练模型。项目网站：https://egonav.weizhuowang.com

---

### 9. Stop Wandering: Efficient Vision-Language Navigation via Metacognitive Reasoning

- **作者**: Xueying Li, Feng Lyu, Hao Wu, Mingliu Liu, Jia-Nan Liu, Guozi Liu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.02318v1)
- **发表日期**: 2026-04-02
- **匹配关键词**: exploration, navigation, VLN
- **arXiv**: [2604.02318v1](http://arxiv.org/abs/2604.02318v1)
- **📥 PDF**: 已下载至本地 (`2604.02318v1_Stop_Wandering_Efficient_Vision-Language_Navigation_via_Metacognitive_Reasoning.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 基于基础模型的无训练视觉语言导航（VLN）智能体能够遵循指令并探索三维环境。然而，现有方法依赖贪婪的前沿选择与被动空间记忆，导致局部振荡和重复访问等低效行为。我们认为这源于元认知能力的缺失：智能体无法监控探索进度、诊断策略失败或进行相应调整。为此，我们提出MetaNav——一种融合空间记忆、历史感知规划与反思校正的元认知导航智能体。空间记忆构建了持久的三维语义地图；历史感知规划通过惩罚重复访问提升效率；反思校正模块能检测停滞状态，并利用大语言模型生成指导未来前沿选择的修正规则。在GOAT-Bench、HM3D-OVON和A-EQA数据集上的实验表明，MetaNav在实现最先进性能的同时，将视觉语言模型查询量降低20.7%，证明元认知推理能显著提升导航的鲁棒性与效率。

---

### 10. UAV-Track VLA: Embodied Aerial Tracking via Vision-Language-Action Models

- **作者**: Qiyao Zhang, Shuhua Zheng, Jianli Sun, Chengxiang Li, Xianke Wu, Zihan Song, Zhiyong Cui, Yisheng Lv, Yonglin Tian
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.02241v1)
- **发表日期**: 2026-04-02
- **匹配关键词**: visual tracking, vision-language-action, vision-language-action model, VLA
- **arXiv**: [2604.02241v1](http://arxiv.org/abs/2604.02241v1)
- **📥 PDF**: 已下载至本地 (`2604.02241v1_UAV-Track_VLA_Embodied_Aerial_Tracking_via_Vision-Language-Action_Models.pdf`)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/Hub-Tian/UAV-Track
- **中文摘要**: 具身视觉跟踪对于无人机执行复杂现实任务至关重要。在具有复杂语义需求的动态城市场景中，视觉-语言-动作模型因其跨模态融合与连续动作生成能力展现出巨大潜力。为在此类环境中建立多模态跟踪基准，我们构建了专用评估基准及大规模数据集，涵盖超过89万帧画面、176项任务和85类多样化目标。针对现有VLA模型存在的时间特征冗余与空间几何先验缺失问题，我们提出改进型VLA跟踪模型UAV-Track VLA。该模型基于$π_{0.5}$架构，引入时序压缩网络以高效捕捉帧间动态特征，同时设计包含空间感知辅助定位头与流匹配动作专家的并行双分支解码器，实现跨模态特征解耦与细粒度连续动作生成。在CARLA仿真系统中的系统性实验验证了本方法卓越的端到端性能：在极具挑战性的远距离行人跟踪任务中，UAV-Track VLA取得61.76%的成功率与269.65帧平均跟踪时长，显著超越现有基线模型；同时展现出对未知环境的强零样本泛化能力，相比原始$π_{0.5}$模型单步推理延迟降低33.4%（至0.0571秒），可实现高效实时无人机控制。数据样本与演示视频详见：https://github.com/Hub-Tian/UAV-Track\_VLA。

---

### 11. UniDriveVLA: Unifying Understanding, Perception, and Action Planning for Autonomous Driving

- **作者**: Yongkang Li, Lijun Zhou, Sixu Yan, Bencheng Liao, Tianyi Yan, Kaixin Xiong, Long Chen, Hongwei Xie, Bing Wang, Guang Chen, Hangjun Ye, Wenyu Liu, Haiyang Sun, Xinggang Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.02190v1)
- **发表日期**: 2026-04-02
- **匹配关键词**: vision-language-action, vision-language-action model, VLA
- **arXiv**: [2604.02190v1](http://arxiv.org/abs/2604.02190v1)
- **📥 PDF**: 已下载至本地 (`2604.02190v1_UniDriveVLA_Unifying_Understanding,_Perception,_and_Action_Planning_for_Autonomous_Driving.pdf`)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/xiaomi-research/unidrivevla
- **中文摘要**: 视觉-语言-行动（VLA）模型近期在自动驾驶领域崭露头角，其通过利用丰富的世界知识提升驾驶系统认知能力的潜力备受瞩目。然而，当前将此类模型应用于驾驶任务时面临空间感知与语义推理之间的关键矛盾。这导致现有VLA系统不得不做出次优妥协：直接采用二维视觉语言模型会限制空间感知能力，而通过三维空间表征增强模型又往往会削弱视觉语言模型原有的推理能力。我们认为，这一矛盾主要源于空间感知与语义推理在共享模型参数中的耦合优化。为突破此局限，我们提出UniDriveVLA——基于混合专家Transformer架构的统一驾驶视觉-语言-行动模型，通过专家解耦机制解决感知与推理的冲突。该模型包含驾驶理解、场景感知和行动规划三大专家模块，通过掩码联合注意力机制实现协同运作。此外，我们结合稀疏感知范式与三阶段渐进式训练策略，在保持语义推理能力的同时显著提升空间感知性能。大量实验表明，UniDriveVLA在nuScenes数据集的开环评估和Bench2Drive的闭环评估中均达到最先进水平。同时，该模型在三维检测、在线建图、运动预测及驾驶导向视觉问答等广泛感知、预测与理解任务中均表现出色，彰显其作为自动驾驶统一模型的广泛适用性。代码与模型已发布于https://github.com/xiaomi-research/unidrivevla。

---

## 📌 Poster

*其他相关研究*

---

### 1. ROS 2-Based LiDAR Perception Framework for Mobile Robots in Dynamic Production Environments, Utilizing Synthetic Data Generation, Transformation-Equivariant 3D Detection and Multi-Object Tracking

- **作者**: Lukas Bergs, Tan Chung, Marmik Thakkar, Alexander Moriz, Amon Göppert, Chinnawut Nantabut, Robert Schmitt
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.02109v1)
- **发表日期**: 2026-04-02
- **匹配关键词**: mobile manipulator
- **arXiv**: [2604.02109v1](http://arxiv.org/abs/2604.02109v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 动态生产环境中的自适应机器人需要具备鲁棒的感知能力，包括六维姿态估计与多目标跟踪。为克服真实数据依赖性、噪声鲁棒性及时空一致性方面的局限，本研究提出一种基于机器人操作系统的激光雷达框架，该框架集成了基于合成数据训练的三维变换等变检测器，并利用中心姿态实现多目标跟踪。通过运动捕捉技术在72种场景下的验证，独立姿态估计的并交比达到62.6%，结合多目标跟踪后提升至83.12%。本激光雷达框架实现了91.12%的高阶跟踪准确率，显著提升了工业移动机械臂激光雷达感知系统的鲁棒性与泛用性。

---

### 2. Cross-Modal Visuo-Tactile Object Perception

- **作者**: Anirvan Dutta, Simone Tasciotti, Claudia Cusseddu, Ang Li, Panayiota Poirazi, Julijana Gjorgjieva, Etienne Burdet, Patrick van der Smagt, Mohsen Kaboli
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.02108v1)
- **发表日期**: 2026-04-02
- **匹配关键词**: tactile perception
- **arXiv**: [2604.02108v1](http://arxiv.org/abs/2604.02108v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 物理属性估计对于安全高效的自主机器人操作至关重要，尤其在接触密集的交互场景中。在此类场景下，视觉与触觉感知能够提供关于物体几何形状、位姿、惯性、刚度及接触动力学（如粘滑行为）的互补信息。然而，这些属性仅能被间接观测，且往往无法精确建模（例如非刚性物体的形变与非线性接触摩擦的耦合作用），使得估计问题本质上具有复杂性，需要在动作执行过程中持续利用视觉-触觉传感信息。现有的视觉-触觉感知框架主要侧重于强制的传感器融合或静态跨模态对齐，较少考虑物体属性相关的不确定性与信念如何随时间演化。受人类多感官感知与主动推理机制启发，我们提出跨模态潜在滤波器（CMLF），用于学习物理物体属性的结构化因果潜在状态空间。CMLF支持视觉与触觉间跨模态先验的双向传递，并通过随时间演化的贝叶斯推理过程整合感官证据。真实机器人实验表明，相较于基线方法，CMLF在不确定条件下提升了潜在物理属性估计的效率和鲁棒性。除性能提升外，该模型展现出与人类感知类似的跨模态耦合现象，包括对跨模态错觉的敏感性以及学习跨感官关联的相似轨迹。这些成果共同为机器人多感官感知实现可泛化、鲁棒且物理一致的跨模态集成迈出了重要一步。

---

### 3. CompassAD: Intent-Driven 3D Affordance Grounding in Functionally Competing Objects

- **作者**: Jingliang Li, Jindou Jia, Tuo An, Chuhao Zhou, Xiangyu Chen, Shilin Shan, Boyu Ma, Bofan Lyu, Gen Li, Jianfei Yang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.02060v1)
- **发表日期**: 2026-04-02
- **匹配关键词**: affordance
- **arXiv**: [2604.02060v1](http://arxiv.org/abs/2604.02060v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 当被告知"切苹果"时，机器人必须选择刀具而非附近的剪刀，尽管两者都具备切割功能。在现实场景中，多个物体可能具有相同的功能特性，但只有特定物体符合当前任务情境。我们将这类情况称为混淆对。然而，现有3D功能感知方法主要通过评估孤立单物体来规避这一挑战，且通常在查询中提供明确的类别名称。本研究提出"意图驱动指令下的多物体功能定位"这一新型3D功能感知范式，要求根据隐含的自然语言意图，在杂乱的多物体点云中针对正确物体预测逐点功能掩码。为探究此问题，我们构建了首个聚焦于可混淆多物体场景中隐含意图的基准测试集CompassAD，涵盖16种功能类型下的30组混淆物体对、6,422个场景及8.8万组查询-答案对。进一步提出CompassNet框架，包含两个专为此任务设计的模块：实例边界交叉注入（ICI）通过约束物体边界内的语言-几何对齐来防止跨物体语义泄露；双层对比优化（BCR）在几何组和点层级实施区分机制，强化目标表面与混淆表面的差异辨识。大量实验表明，该方法在已知与未知查询中均取得最先进性能，机械臂部署实验证实了其在真实世界混淆多物体场景中抓取任务的有效迁移能力。

---

### 4. IndoorCrowd: A Multi-Scene Dataset for Human Detection, Segmentation, and Tracking with an Automated Annotation Pipeline

- **作者**: Sebastian-Ion Nae, Radu Moldoveanu, Alexandra Stefania Ghita, Adina Magda Florea
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.02032v1)
- **发表日期**: 2026-04-02
- **匹配关键词**: human-robot interaction
- **arXiv**: [2604.02032v1](http://arxiv.org/abs/2604.02032v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://sheepseb.github.io/IndoorCrowd/.
- **中文摘要**: 理解人群在室内密集环境中的行为对于监控、智能建筑和人机交互至关重要，但现有数据集很少能大规模捕捉真实世界的室内复杂性。我们推出了IndoorCrowd——一个用于室内人体检测、实例分割和多目标跟踪的多场景数据集，采集自四个校园区域（ACS-EC、ACS-EG、IE-Central、R-Central）。该数据集包含31段视频（以5帧/秒速率采集的9,913帧画面），并提供经人工核验的逐实例分割掩码。我们选取620帧作为控制子集，通过科恩κ系数、平均精度、精确率、召回率和掩码交并比等指标，对比评估了SAM3、GroundingSAM和EfficientGroundingSAM三种基础模型自动标注工具与人工标注的差异。另设2,552帧子集以MOTChallenge格式提供连续身份轨迹，支持多目标跟踪研究。我们采用YOLOv8n、YOLOv26n和RT-DETR-L检测器分别搭配ByteTrack、BoT-SORT和OC-SORT跟踪器建立了检测、分割与跟踪的基准性能。逐场景分析显示：不同场景因人群密度、目标尺度和遮挡程度存在显著难度差异，其中ACS-EC场景以79.3%的高密度帧占比和60.8像素的平均实例尺度成为最具挑战性的场景。项目页面详见https://sheepseb.github.io/IndoorCrowd/。

---

### 5. Bridging Discrete Planning and Continuous Execution for Redundant Robot

- **作者**: Teng Yan, Yue Yu, Yihan Liu, Bingzhuo Zhong
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.02021v1)
- **发表日期**: 2026-04-02
- **匹配关键词**: path planning
- **arXiv**: [2604.02021v1](http://arxiv.org/abs/2604.02021v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 体素网格强化学习因其简洁性和可复现性，在冗余机械臂路径规划中被广泛采用。然而，在七自由度机械臂上直接通过逐点数值逆运动学执行时，常出现步长抖动、关节突变及奇异位形附近不稳定的问题。本研究提出了一种在不修改离散规划器本身的前提下，连接离散规划与连续执行的桥接框架。在规划侧，引入步长归一化的26邻域笛卡尔动作及几何平局决胜机制，以抑制不必要的转向并消除步长振荡。在执行侧，构建了任务优先级阻尼最小二乘逆运动学层，该层将末端执行器位置作为主任务，姿态与关节居中则作为次级任务投影至零空间处理，并结合信赖域截断与关节速度约束。在随机稀疏、中等及密集环境中对七自由度机械臂的测试表明，该桥接框架将密集场景下的规划成功率从约0.58提升至1.00，典型路径长度从约1.53米缩短至1.10米，在保持末端执行器误差低于1毫米的同时，将关节峰值加速度降低超过一个数量级，显著提升了基于体素的强化学习路径在冗余机械臂上的连续执行质量。

---

### 6. Integrated Identification of Collaborative Robots for Robot Assisted 3D Printing Processes

- **作者**: Alessandro Dimauro, Davide Tebaldi, Fabio Pini, Luigi Biagiotti, Francesco Leali
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.01991v1)
- **发表日期**: 2026-04-02
- **匹配关键词**: collaborative robot
- **arXiv**: [2604.01991v1](http://arxiv.org/abs/2604.01991v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 近年来，增材制造与工业机器人技术的融合为复杂零部件生产开辟了新视野，尤其在汽车制造领域。机器人辅助增材制造工艺突破了传统笛卡尔系统的尺寸与运动学限制，实现了非平面沉积并具备更强的几何灵活性。然而，机械臂动态复杂性的增加带来了精度控制与误差预测方面的挑战。本研究提出一种基于模型的系统参数集成辨识方法，涵盖机器人本体、执行机构及控制器。研究表明，即使在协作机器人普遍存在传感与编程局限性的条件下，该集成建模方法仍能建立可靠的动态模型。通过五步集成法完成机械臂动态模型辨识：从几何与惯性分析起步，依次进行摩擦参数与控制器参数辨识，最终完成剩余参数识别。该方法本质上保证了辨识参数的物理一致性。以热塑性挤出工艺中使用的六自由度协作机器人为实际案例，验证了该辨识方法的有效性。实际机器人实验结果与辨识模型结果的高度吻合，展现了机器人辅助3D打印工艺在精度控制与误差预测方面的提升潜力。

---

### 7. Preferential Bayesian Optimization with Crash Feedback

- **作者**: Johanna Menn, David Stenger, Sebastian Trimpe
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.01776v1)
- **发表日期**: 2026-04-02
- **匹配关键词**: exploration
- **arXiv**: [2604.01776v1](http://arxiv.org/abs/2604.01776v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 贝叶斯优化是控制与机器人学中参数学习的一种常用黑箱优化方法。该方法通常需要一个能反映用户优化目标的目标函数。然而在实际应用中，由于性能指标复杂或难以量化，目标函数往往无法直接获取。偏好贝叶斯优化通过两两比较获取人类反馈，克服了这一局限，无需对性能进行显式量化。当将PBO应用于四旋翼飞行器等硬件系统时，设备坠毁可能导致耗时的实验重置、设备损耗或其他不良后果。标准PBO方法无法整合此类坠毁实验的反馈，导致频繁探索易引发实验坠毁的参数。为此我们提出CrashPBO机制，该用户友好型方案允许用户在优化过程中同时表达参数偏好和报告坠毁情况。在合成函数上的基准测试表明，该机制将坠毁率降低63%并提升了数据利用效率。通过在三个机器人平台上的实验，我们证明了CrashPBO具有广泛的适用性和可迁移性，其构建了一个灵活、用户友好的参数学习框架，能够有效整合人类对参数偏好和坠毁情况的反馈。

---

### 8. Hi-LOAM: Hierarchical Implicit Neural Fields for LiDAR Odometry and Mapping

- **作者**: Zhiliu Yang, Jianyuan Zhang, Lianhui Zhao, Jinyu Dai, Zhu Yang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.01720v1)
- **发表日期**: 2026-04-02
- **匹配关键词**: localization and mapping, navigation, robot navigation
- **arXiv**: [2604.01720v1](http://arxiv.org/abs/2604.01720v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 激光雷达里程计与建图（LOAM）是自动驾驶和机器人导航等具身人工智能应用中的关键技术。现有的大多数LOAM框架要么依赖于监督信号，要么缺乏重建保真度，难以准确描绘大规模复杂场景的细节。为克服这些局限，我们提出了一种基于激光雷达传感器的多尺度隐式神经定位与建图框架——Hi-LOAM。该框架以激光雷达点云作为输入数据模态，基于八叉树结构在多级哈希表中学习并存储分层潜在特征，随后在建图过程中通过浅层多层感知机将这些多尺度潜在特征解码为有符号距离值。在姿态估计环节，我们采用无对应关系的扫描到隐式匹配范式来估计最优姿态，并将当前扫描帧注册至子地图中。整个训练过程以自监督方式进行，无需模型预训练，在应用于不同环境时展现出良好的泛化能力。通过在多个真实世界与合成数据集上的大量实验证明，相较于现有先进方法，我们的Hi-LOAM在有效性与泛化能力方面均表现出卓越性能。

---

### 9. AURA: Multimodal Shared Autonomy for Real-World Urban Navigation

- **作者**: Yukai Ma, Honglin He, Selina Song, Wayne Wu, Bolei Zhou
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.01659v1)
- **发表日期**: 2026-04-02
- **匹配关键词**: navigation
- **arXiv**: [2604.01659v1](http://arxiv.org/abs/2604.01659v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: PROJECT_PAGE
- **中文摘要**: 复杂城市环境中的长距离导航高度依赖人工持续操作，易导致操作者疲劳、效率降低及安全隐患。共享自主性——即视觉语言人工智能代理与人类操作者协同操控移动机器——为解决这些问题提供了前景广阔的方案。然而现有共享自主方法通常要求人类与AI在同一行动空间内操作，导致认知负荷较高。本研究提出辅助型城市机器人自主系统（AURA），这是一种新型多模态框架，将城市导航任务分解为高层人类指令与底层AI控制。AURA采用空间感知指令编码器，将多样化人类指令与视觉空间语境进行对齐。为促进模型训练，我们构建了包含遥操作数据与视觉语言描述的大规模数据集MM-CoS。仿真环境与真实场景实验表明，AURA能有效遵循人类指令，降低人工操作强度，提升导航稳定性，同时支持在线自适应。在相似接管条件下，本共享自主框架将接管频率降低超过44%。项目页面提供了演示视频及更多技术细节。

---

