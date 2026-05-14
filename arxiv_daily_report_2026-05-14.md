# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-05-14 08:03

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 6/20 篇提供

**🌟 Highlight**: 20 篇 | **📌 Poster**: 0 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. SafeManip: A Property-Driven Benchmark for Temporal Safety Evaluation in Robotic Manipulation

- **作者**: Chengyue Huang, Khang Vo Huynh, Sebastian Elbaum, Zsolt Kira, Lu Feng
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.12386v1)
- **发表日期**: 2026-05-12
- **匹配关键词**: vision-language-action
- **arXiv**: [2605.12386v1](http://arxiv.org/abs/2605.12386v1)
- **📥 PDF**: 已下载至本地 (`2605.12386v1_SafeManip_A_Property-Driven_Benchmark_for_Temporal_Safety_Evaluation_in_Robotic_Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 机器人操作通常通过任务成功来评估，但成功完成并不能保证安全执行。许多安全故障是时间性的：机器人在接触污染表面后可能触碰洁净区域，或在物体完全进入容器前提前释放。我们提出SafeManip——一个以属性为导向的基准测试，专门用于评估机器人操作中的时间安全属性，超越了以往主要关注任务完成或单步约束违反的评估方法。SafeManip利用有限迹线性时序逻辑（LTLf）在有限执行轨迹上定义可复用的安全模板，将观测到的执行轨迹映射为符号谓词迹，并通过基于LTLf的监控器进行评估。其属性套件涵盖八类操作安全：碰撞与接触安全、抓取稳定性、释放稳定性、交叉污染、动作起始、机构恢复、物体容纳及封闭空间访问。模板可通过任务特定对象、夹具、区域或技能进行实例化，使相同安全规范能泛化至不同任务与环境。我们在50个RoboCasa365家庭任务中，对六种视觉-语言-动作策略（包括$π_0$、$π_{0.5}$、GR00T及其训练变体）进行了评估。结果表明，即使强模型也常表现出不安全行为。任务成功率的提升并不能可靠转化为更安全的执行：许多成功执行轨迹仍存在安全隐患，而长周期或更复杂的任务会暴露更多违规行为。SafeManip为诊断时间安全故障及衡量超越任务完成的安全成功提供了可复用的评估层。

---

### 2. GuidedVLA: Specifying Task-Relevant Factors via Plug-and-Play Action Attention Specialization

- **作者**: Xiaosong Jia, Bowen Yang, Zuhao Ge, Xian Nie, Yuchen Zhou, Cunxin Fan, Yufeng Li, Yilin Chai, Chao Jing, Zijian Liang, Qingwen Bu, Haidong Cao, Chao Wu, Qifeng Li, Zhenjie Yang, Chenhe Zhang, Hongyang Li, Zuxuan Wu, Junchi Yan, Yu-Gang Jiang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.12369v1)
- **发表日期**: 2026-05-12
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2605.12369v1](http://arxiv.org/abs/2605.12369v1)
- **📥 PDF**: 已下载至本地 (`2605.12369v1_GuidedVLA_Specifying_Task-Relevant_Factors_via_Plug-and-Play_Action_Attention_Specialization.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型旨在通过将动作作为模态融入强大的视觉-语言模型（VLM）中，实现通用的机器人学习。现有VLA模型依赖端到端监督来隐式地使动作解码过程学习任务相关特征。然而，缺乏显式引导时，这些模型常过度拟合虚假关联（如视觉捷径或环境噪声），从而限制其泛化能力。本文提出GuidedVLA框架，旨在手动引导动作生成聚焦于任务相关因素。核心思路是将动作解码器视为功能组件的集合而非单一学习器：通过手动定义的辅助信号监督各个注意力头，使其捕获不同因素。作为初步研究，我们以三种专用注意力头实例化该范式：目标定位、空间几何与时序技能逻辑。在仿真与真实机器人实验中，与强VLA基线相比，GuidedVLA在域内与域外场景中均提升了成功率。最后，我们证明这些专用因素的质量与任务性能正相关，且该机制能产生解耦的高质量特征。研究结果表明，显式引导动作解码器学习是构建更鲁棒、更通用的VLA模型的有前景方向。

---

### 3. SI-Diff: A Framework for Learning Search and High-Precision Insertion with a Force-Domain Diffusion Policy

- **作者**: Yibo Liu, Stanko Oparnica, Simon Shewchun-Jakaitis, Guoyi Fu, Jie Wang, Jun Yang, Anand Jagannathan, Tony Hong-Yau Lo
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.12247v1)
- **发表日期**: 2026-05-12
- **匹配关键词**: diffusion policy
- **arXiv**: [2605.12247v1](http://arxiv.org/abs/2605.12247v1)
- **📥 PDF**: 已下载至本地 (`2605.12247v1_SI-Diff_A_Framework_for_Learning_Search_and_High-Precision_Insertion_with_a_Force-Domain_Diffusion_P.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 接触丰富的装配是机器人技术的基础，但由于相对位姿的不确定性（例如轴孔任务中的错位和小间隙），这一任务面临重大挑战。现有方法通常将搜索与高精度插入分开处理，因为这两类任务涉及不同的动作模式。然而，对于智能装配系统而言，理想的情况是在单一模型中同时支持这两类任务，而无需切换模型或权重。在本工作中，我们提出SI-Diff框架，通过力域扩散策略同时学习搜索与高精度插入。为此，我们引入了一种新的模式调节机制，使策略能够在单一框架下捕捉不同的动作行为。此外，我们开发了一种新的搜索教师策略，能够生成多样化的轨迹。通过基于教师策略提供的成功且高效的演示进行训练，模型学会了从触觉和末端执行器速度观测到有效动作行为的映射。我们进行了充分的实验，结果表明，与最先进的基线方法TacDiffusion相比，SI-Diff将x-y方向错位的容忍度从2毫米扩展至5毫米，同时展现出对未见形状的强零样本迁移能力。

---

### 4. TMRL: Diffusion Timestep-Modulated Pretraining Enables Exploration for Efficient Policy Finetuning

- **作者**: Matthew M. Hong, Jesse Zhang, Anusha Nagabandi, Abhishek Gupta
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.12236v1)
- **发表日期**: 2026-05-12
- **匹配关键词**: exploration, VLA
- **arXiv**: [2605.12236v1](http://arxiv.org/abs/2605.12236v1)
- **📥 PDF**: 已下载至本地 (`2605.12236v1_TMRL_Diffusion_Timestep-Modulated_Pretraining_Enables_Exploration_for_Efficient_Policy_Finetuning.pdf`)
- **🔓 开源**: CODE
  - 链接：https://weirdlabuw.github.io/tmrl/.
- **中文摘要**: 基于强化学习（RL）对预训练机器人策略进行微调时，往往继承了行为克隆（BC）预训练引入的瓶颈——后者生成的狭窄动作分布缺乏下游探索所需的覆盖范围。我们提出一个统一框架，通过桥接BC预训练与RL微调，实现机器人策略高效微调所需的探索能力。我们的预训练方法——上下文平滑预训练（CSP）——将前向扩散噪声注入策略输入，在精确模仿与广泛动作覆盖之间构建连续体。随后通过时间步调制强化学习（TMRL）对预训练策略进行微调，该方法训练智能体在微调过程中通过调节扩散时间步动态调整该条件，从而实现对探索的显式控制。该方法可无缝集成任意策略输入（如状态、三维点云或基于图像的视觉-语言-动作策略），实验表明TMRL能提升RL微调的样本效率。值得注意的是，TMRL可在1小时内完成复杂操作任务的真实世界微调。视频与代码见https://weirdlabuw.github.io/tmrl/。

---

### 5. TriBand-BEV: Real-Time LiDAR-Only 3D Pedestrian Detection via Height-Aware BEV and High-Resolution Feature Fusion

- **作者**: Mohammad Khoshkdahan, Alexey Vinel
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.12220v1)
- **发表日期**: 2026-05-12
- **匹配关键词**: 3d reconstruction, 3D reconstruction
- **arXiv**: [2605.12220v1](http://arxiv.org/abs/2605.12220v1)
- **📥 PDF**: 已下载至本地 (`2605.12220v1_TriBand-BEV_Real-Time_LiDAR-Only_3D_Pedestrian_Detection_via_Height-Aware_BEV_and_High-Resolution_Fe.pdf`)
- **🔓 开源**: CODE
- **中文摘要**: 安全自主代理和移动机器人需要快速实时的三维感知能力，尤其针对行人等弱势道路使用者（VRU）。我们提出一种新的鸟瞰图（BEV）编码方法，将完整的三维激光雷达点云映射为包含三个高度带的轻量级二维BEV张量。通过将三维检测问题显式重构为二维检测问题，我们能够从BEV输出中重建三维边界框。单一网络即可一次性检测汽车、行人和骑行者。主干网络在深层阶段采用区域注意力机制，P1至P4层级间的双向特征融合颈部网络整合上下文与细节信息，检测头通过分布聚焦学习预测带方向角的边界框侧边偏移量，并采用旋转IoU损失函数。训练过程中，我们在通道空间应用小幅垂直重分箱与适度反射率抖动以防止过拟合记忆。三维重建阶段采用四分位距（IQR）滤波器去除噪声与离群激光雷达点。在KITTI数据集上，TriBand-BEV在单张消费级GPU上以49 FPS的帧率，对简单、中等、困难三种难度级别的行人BEV平均精度（AP）分别达到58.7%、52.6%和47.2%，较Complex-YOLO分别提升12.6%、7.5%和3.1%。定性场景显示该方法在遮挡条件下仍能保持稳定检测。该流水线结构紧凑，可直接部署于实时机器人系统。我们的源代码已在GitHub上公开。

---

### 6. Premover: Fast Vision-Language-Action Control by Acting Before Instructions Are Complete

- **作者**: Joonha Park, Jiseung Jeong, Taesik Gong
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.12160v1)
- **发表日期**: 2026-05-12
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2605.12160v1](http://arxiv.org/abs/2605.12160v1)
- **📥 PDF**: 已下载至本地 (`2605.12160v1_Premover_Fast_Vision-Language-Action_Control_by_Acting_Before_Instructions_Are_Complete.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）策略通常是在用户完成输入（打字或说话）后机器人才开始执行动作的假设下进行评估。然而在实际部署中，用户需要数秒时间输入指令，导致策略在交互过程中长时间处于空闲状态。我们提出Premover——一种轻量级模块，可将这段空闲窗口转化为有用的预计算。Premover保持VLA主干网络冻结，附加两个小型投影头（分别处理图像块和语言标记），将主干网络中间层映射到共享空间。由此生成的聚焦图通过模拟器渲染的目标对象分割掩码进行监督，并作为下一步图像标记的逐块重加权因子。通过联合训练流式前缀得到的单一标量就绪阈值，决定策略何时开始执行动作。在LIBERO基准测试套件上，Premover将平均挂钟时间从34.0秒降至29.4秒（降低13.6%），同时保持与完整提示基线相当的成功率（95.1% vs 95.0%）；相比之下，朴素预计算方法成功率骤降至66.4%。

---

### 7. World Action Models: The Next Frontier in Embodied AI

- **作者**: Siyin Wang, Junhao Shi, Zhaoyang Fu, Xinzhe He, Feihong Liu, Chenchen Yang, Yikang Zhou, Zhaoye Fei, Jingjing Gong, Jinlan Fu, Mike Zheng Shou, Xuanjing Huang, Xipeng Qiu, Yu-Gang Jiang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.12090v1)
- **发表日期**: 2026-05-12
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2605.12090v1](http://arxiv.org/abs/2605.12090v1)
- **📥 PDF**: 已下载至本地 (`2605.12090v1_World_Action_Models_The_Next_Frontier_in_Embodied_AI.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作模型在具身策略学习中实现了强大的语义泛化能力，但其学习的是从观察到动作的反应式映射，并未显式建模物理世界在干预下的演化过程。为突破这一局限，越来越多的研究将世界模型（即环境动态预测模型）整合到动作生成流程中。我们将这一新兴范式定义为世界动作模型：一种统一预测性状态建模与动作生成的具身基础模型，其目标在于建立未来状态与动作的联合分布，而非仅关注动作本身。然而，现有研究在架构设计、学习目标和应用场景上仍呈现碎片化特征，缺乏统一的概念框架。本文首先对世界动作模型进行正式定义，厘清其与相关概念的区别，并追溯催生该范式的视觉-语言-动作模型与世界模型研究的基础与早期融合过程。我们将现有方法系统归类为级联式与联合式两类世界动作模型，并根据生成模态、条件机制和动作解码策略进行细分。在此基础上，系统分析支撑世界动作模型发展的数据生态体系，涵盖机器人遥操作、便携式人类演示、仿真环境及互联网级自我中心视频等数据源，并综合梳理围绕视觉保真度、物理常识和动作合理性构建的新型评估协议。本综述首次系统描绘了世界动作模型的研究全景，阐明关键架构范式及其权衡取舍，并指出这一快速发展领域面临的开放挑战与未来机遇。

---

### 8. Learning Action Manifold with Multi-view Latent Priors for Robotic Manipulation

- **作者**: Junjin Xiao, Dongyang Li, Yandan Yang, Shuang Zeng, Tong Lin, Xinyuan Chang, Feng Xiong, Mu Xu, Xing Wei, Zhiheng Ma, Qing Zhang, Wei-Shi Zheng
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.11832v1)
- **发表日期**: 2026-05-12
- **匹配关键词**: vision-language-action, VLA, perception and manipulation
- **arXiv**: [2605.11832v1](http://arxiv.org/abs/2605.11832v1)
- **📥 PDF**: 已下载至本地 (`2605.11832v1_Learning_Action_Manifold_with_Multi-view_Latent_Priors_for_Robotic_Manipulation.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://junjxiao.github.io/Multi-view-VLA.github.io/.
- **中文摘要**: 本文探讨了视觉-语言-动作（VLA）模型在空间感知与操作中面临的挑战。针对单目输入导致的深度模糊问题，我们利用预训练的多视图扩散模型合成潜在新视角，并提出几何引导门控Transformer（G3T），在三维几何引导下对齐多视图特征，同时自适应过滤遮挡噪声。为提升动作学习效率，我们引入动作流形学习（AML），该方法直接在有效动作流形上预测动作，避免对噪声或速度等非结构化目标进行低效回归。在LIBERO、RoboTwin 2.0及真实机器人任务上的实验表明，我们的方法在成功率和鲁棒性上均超越现有最优基线。项目页面：https://junjxiao.github.io/Multi-view-VLA.github.io/。

---

### 9. Mapping Embodied Affective Touch Strategies on a Humanoid Robot

- **作者**: Qiaoqiao Ren, Omar Eldardeer, Francesca Cocchella, Rea Francesco, Alessandra Sciutti, Tony Belpaeme
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.11825v1)
- **发表日期**: 2026-05-12
- **匹配关键词**: HRI, human-robot interaction
- **arXiv**: [2605.11825v1](http://arxiv.org/abs/2605.11825v1)
- **📥 PDF**: 已下载至本地 (`2605.11825v1_Mapping_Embodied_Affective_Touch_Strategies_on_a_Humanoid_Robot.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 人机交互中的情感触觉不仅受情感意图影响，还受机器人具身形态的影响，包括触摸位置、物理约束以及感知的能动性或社会角色。现有的人机交互研究通常只关注一两个孤立的身体部位，限制了对情感触觉如何在整个类人身体上泛化的理解。我们开展了一项研究，让32名参与者与配备全身分布式触觉传感器的iCub机器人互动。参与者在三种条件下表达八种情绪：自由触摸、仅手臂触摸和仅躯干触摸。结果表明，身体区域和空间约束共同塑造了触摸位置和动态。在自由触摸中，参与者偏好社交可及的上半身区域，而较少被触摸的区域则表现出更强的情绪特异性选择。情绪相关的差异在仅手臂触摸中更明显地体现在运动特征上，而在仅躯干触摸中则更明显地体现在压力特征上。即使在相同的粗略身体区域内，触摸策略也无法在自由和受限条件之间直接转移。参与者报告称，互动后与机器人的亲近感增加，约30%的人表示感知到的社会关系发生了变化。这些发现共同表明，情感触觉表达强烈依赖于身体区域，并受具身约束的影响。

---

### 10. See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model

- **作者**: Yixu Feng, Zinan Zhao, Yanxiang Ma, Chenghao Xia, Chengbin Du, Yunke Wang, Chang Xu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.11817v1)
- **发表日期**: 2026-05-12
- **匹配关键词**: vision-language-action, vision-language-action model, VLA
- **arXiv**: [2605.11817v1](http://arxiv.org/abs/2605.11817v1)
- **📥 PDF**: 已下载至本地 (`2605.11817v1_See_What_Matters_Differentiable_Grid_Sample_Pruning_for_Generalizable_Vision-Language-Action_Model.pdf`)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/Fediory/Grid-Sampler.
- **中文摘要**: 视觉-语言-动作（VLA）模型在机器人操作领域展现出显著潜力，但其高昂的计算成本阻碍了实时部署。现有令牌剪枝方法面临根本性权衡：采用剪枝的激进压缩必然丢弃接触点等关键几何细节，导致性能严重下降。这迫使人们做出妥协，限制了可实现的压缩率，进而制约了潜在加速效果。我们认为，打破这一权衡需要将压缩重新构想为视觉编码器中具有几何感知能力的连续令牌重采样。为此，我们提出可微网格采样器（GridS），这是一种即插即用模块，可在VLA中对视觉令牌执行任务感知的连续重采样。通过自适应预测最小显著坐标集，并利用可微插值提取特征，GridS在实现激进压缩（保留原始视觉令牌不足10%）的同时，保留了关键空间信息。在LIBERO基准测试和真实机器人平台上的实验表明，GridS验证了迄今报告的最低可行视觉令牌数量，在成功率无下降的情况下实现了76%的FLOPs缩减。代码已开源至https://github.com/Fediory/Grid-Sampler。

---

### 11. Beyond World-Frame Action Heads: Motion-Centric Action Frames for Vision-Language-Action Models

- **作者**: Huoren Yang, Jianchao Zhao, Hu Yusong, Qiguan Ou, Yuyang Gao, Wei Ke, Yuhang He, SongLin Dong, Zhiheng Ma, Yihong Gong
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.11809v1)
- **发表日期**: 2026-05-12
- **匹配关键词**: vision-language-action, vision-language-action model, VLA
- **arXiv**: [2605.11809v1](http://arxiv.org/abs/2605.11809v1)
- **📥 PDF**: 已下载至本地 (`2605.11809v1_Beyond_World-Frame_Action_Heads_Motion-Centric_Action_Frames_for_Vision-Language-Action_Models.pdf`)
- **🔓 开源**: CODE
- **中文摘要**: 视觉-语言-动作（VLA）模型在更强的主干网络、更广泛的预训练和更大的演示数据集支持下取得了快速发展，但其动作头结构仍高度同质化：大多数模型直接在固定世界坐标系中预测动作指令。我们提出**MCF-Proto**，一种轻量级动作头，为VLA策略配备运动中心动作框架（MCF）和基于原型的动作参数化。在每个时间步，策略预测旋转矩阵$R_t \in SO(3)$，从一组原型中在变换后的局部坐标系中组合动作，并将其映射回世界坐标系进行端到端训练，仅使用标准演示数据而无需辅助监督。这种简单设计诱导出稳定的涌现结构。在没有显式方向标签的情况下，学习到的局部坐标系形成了稳定的几何结构，其轴与演示的末端执行器运动高度兼容。同时，学习表示中的动作变得更加紧凑，变化由更少的主导方向捕获，并通过共享原型更规则地组织。这些结构特性转化为更强的鲁棒性，尤其是在几何扰动下。我们的结果表明，为动作头添加轻量级几何和组合结构可以显著改善VLA策略组织与泛化机器人操作行为的能力。匿名代码仓库已附于补充材料中。

---

### 12. NavOL: Navigation Policy with Online Imitation Learning

- **作者**: Xiaofei Wei, Chun Gu, Li Zhang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.11762v1)
- **发表日期**: 2026-05-12
- **匹配关键词**: navigation, diffusion policy, visual navigation
- **arXiv**: [2605.11762v1](http://arxiv.org/abs/2605.11762v1)
- **📥 PDF**: 已下载至本地 (`2605.11762v1_NavOL_Navigation_Policy_with_Online_Imitation_Learning.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 学习鲁棒的导航策略仍是机器人领域的核心挑战。离线模仿学习存在分布偏移和部署时的累积误差问题，而强化学习则需要奖励函数设计且学习效率低下。本文提出NavOL——一种在线模仿学习范式，通过与模拟器交互并利用在线收集的专家演示数据持续更新策略。基于将局部观测映射为未来路径点的预训练导航扩散策略，NavOL在部署更新循环中训练：部署阶段，策略在模拟器中执行动作，并查询具有全局环境特权信息的全局规划器以获取最优路径片段作为真值轨迹标签；更新阶段，策略在在线采集的观测-轨迹对上进行训练。这种在线模仿循环消除了奖励设计需求，提升了学习效率，并通过在策略自身探索的部署轨迹上训练缓解了分布偏移问题。基于IsaacLab平台，我们利用快速高保真并行渲染技术及相机位姿与起止点对的域随机化，在8块RTX 4090 GPU上横跨50个场景进行规模化训练，每小时可采集超过2000条新轨迹（每条平均超过400步）。同时引入包含预定义起止点的室内视觉导航基准用于零样本泛化测试。在NavDP基准及我们提出的基准等模拟环境中的大量评估，以及精心设计的真实世界实验，均证明了NavOL的有效性，展现出在线模仿学习中的持续性能提升。

---

### 13. RIO: Flexible Real-Time Robot I/O for Cross-Embodiment Robot Learning

- **作者**: Pablo Ortega-Kral, Eliot Xing, Arthur Bucker, Vernon Luk, Junseo Kim, Owen Kwon, Angchen Xie, Nikhil Sobanbabu, Yifu Yuan, Megan Lee, Deepam Ameria, Bhaswanth Ayapilla, Jaycie Bussell, Guanya Shi, Jonathan Francis, Jean Oh ⭐
  - **高亮作者**: Guanya Shi
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.11564v1)
- **发表日期**: 2026-05-12
- **匹配关键词**: vision-language-action, vision-language-action model, VLA
- **arXiv**: [2605.11564v1](http://arxiv.org/abs/2605.11564v1)
- **📥 PDF**: 已下载至本地 (`2605.11564v1_RIO_Flexible_Real-Time_Robot_IO_for_Cross-Embodiment_Robot_Learning.pdf`)
- **🔓 开源**: CODE
  - 链接：https://robot-i-o.github.io
- **中文摘要**: 尽管近期在收集多任务、多形态数据集、设计视觉-语言-动作模型（VLA）训练方案，以及在多种机器人平台上展示这些模型方面做出了努力，但通用跨形态机器人能力在很大程度上仍是一个难以实现的目标。进展受限于碎片化的基础设施：大多数机器人代码高度依赖于用户设定的具体配置，导致用户在尝试复用、回收或共享成果时面临巨大开销。我们提出RIO（机器人输入/输出），这是一个开源的Python框架，提供灵活轻量的组件，用于跨不同硬件平台和形态的机器人控制、遥操作、数据格式化、传感器配置及策略部署。RIO提供的抽象层使用户能够自由选择并切换方案，且只需极少的重新配置工作。我们在三种形态（单臂、双臂、人形）及四种配备不同夹爪和摄像头的硬件平台上，针对VLA部署工作流验证了RIO。利用RIO收集的遥操作数据，我们微调了包括$π_{0.5}$和GR00T在内的先进VLA模型，用于拾取放置、折叠、擦洗碗碟等家务任务。通过开源所有成果，我们希望社区能加速在真实机器人硬件上的学习进程。更多详情请访问：https://robot-i-o.github.io

---

### 14. Offline Policy Evaluation for Manipulation Policies via Discounted Liveness Formulation

- **作者**: Hao Wang, Joshua Bowden, Colton Crosby, Somil Bansal
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.11479v1)
- **发表日期**: 2026-05-12
- **匹配关键词**: vision-language-action, diffusion policy, vision-language-action model
- **arXiv**: [2605.11479v1](http://arxiv.org/abs/2605.11479v1)
- **📥 PDF**: 已下载至本地 (`2605.11479v1_Offline_Policy_Evaluation_for_Manipulation_Policies_via_Discounted_Liveness_Formulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 策略评估是机器人策略开发与部署流程中的基本组成部分。在现代操作系统中，这一问题尤为具有挑战性：奖励通常稀疏，评估展开的任务进程往往是非单调的（因为策略会表现出恢复行为），且评估展开必然具有有限长度。这种有限长度引入了截断偏差，打破了依赖贝尔曼方程/最优性原理的标准方法所基于的无限时域假设。本文提出了一种基于活性贝尔曼算子的稀疏奖励离线策略评估框架。我们的方法将策略评估解释为任务完成问题，并生成一个对有限时域截断具有鲁棒性的保守不动点值函数。我们分析了所提算子的理论性质（包括收缩保证），并展示了它如何在缓解截断偏差的同时编码任务进程。我们在两个模拟操作任务（分别使用视觉-语言-动作模型和扩散策略）以及一个基于人类演示的布料折叠任务上评估了该方法。实验结果表明，我们的方法能更准确地反映任务进展，并显著减少截断偏差，优于TD(0)和蒙特卡洛策略评估等经典基线方法。

---

### 15. RankQ: Offline-to-Online Reinforcement Learning via Self-Supervised Action Ranking

- **作者**: Andrew Choi, Wei Xu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.11151v1)
- **发表日期**: 2026-05-11
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2605.11151v1](http://arxiv.org/abs/2605.11151v1)
- **📥 PDF**: 已下载至本地 (`2605.11151v1_RankQ_Offline-to-Online_Reinforcement_Learning_via_Self-Supervised_Action_Ranking.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 离线到在线强化学习通过利用在线交互前预先收集的数据集来提高样本效率。然而，一个关键挑战是在数据集覆盖有限的大状态-动作空间中学习准确的评论家。为缓解价值高估带来的有害更新，先前方法通过降低分布外动作相对于数据集动作的权重来施加悲观主义。虽然有效，但这本质上起到了行为克隆锚点的作用，当数据集动作次优时会阻碍后续在线策略改进。我们提出RankQ——一种离线到在线的Q学习目标函数，通过自监督的多项排序损失增强时序差分学习，以强制实现结构化动作排序。通过学习相对动作偏好而非统一惩罚未见动作，RankQ塑造Q函数使得动作梯度指向更高质量的行为。在稀疏奖励D4RL基准测试中，RankQ的性能与七种先前方法相当或更优。在基于视觉的机器人学习中，RankQ能够在低数据量场景下对预训练的视觉-语言-动作模型进行有效的离线到在线微调，平均模拟成功率比次优方法高42.7%。在高数据量场景下，RankQ的模拟性能比次优方法提升13.7%，并实现强大的模拟到现实迁移，将真实世界积木堆叠成功率从VLA初始性能的43.1%提升至84.7%。

---

### 16. Forecast-aware Gaussian Splatting for Predictive 3D Representation in Language-Guided Pick-and-Place Manipulation

- **作者**: Kaixin Jia, Jiacheng Xu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.11144v1)
- **发表日期**: 2026-05-11
- **匹配关键词**: gaussian splatting, affordance
- **arXiv**: [2605.11144v1](http://arxiv.org/abs/2605.11144v1)
- **📥 PDF**: 已下载至本地 (`2605.11144v1_Forecast-aware_Gaussian_Splatting_for_Predictive_3D_Representation_in_Language-Guided_Pick-and-Place.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出了一种名为“预测感知高斯泼溅”（Forecast-GS）的预测性三维表示框架，用于语言条件驱动的机器人操作。尽管近期操作系统通过将语言指令映射到机器人可操作空间、价值图或关系关键点约束取得了进展，但它们通常仅基于当前场景进行推理，并未显式建模任务完成状态。当任务成功依赖于在部分观测条件下满足空间与语义目标时，这一局限性尤为关键——机器人必须评估候选动作是否导向可行且符合任务预期的结果。

我们在真实世界的抓取放置操作任务（包括“刀具入盒”、“苹果入碗”和“海绵入盘”）上验证了Forecast-GS。针对每项任务，我们在相同机器人平台与传感配置下，对不同的初始物体布局进行了25次真实环境试验。采用自动候选选择的Forecast-GS在三个任务上分别取得了21/25、23/25和16/25的成功率，优于基线方法ReKep（15/25、19/25和10/25）。在诊断性人工辅助设置下，成功率进一步提升至23/25、24/25和19/25，表明候选生成策略有效，但自动排序仍不完善。这些结果表明，显式预测任务完成时的三维状态能实现更可靠的动作评估，而自动选择与人工辅助选择之间的差距则说明，鲁棒的最终状态排序仍是全自主操作面临的重要挑战。总体而言，Forecast-GS为语言理解、三维感知与机器人操作规划之间提供了可解释的桥梁。

---

### 17. SEVO: Semantic-Enhanced Virtual Observation for Robust VLA Manipulation via Active Illumination and Data-Centric Collection

- **作者**: Tianchonghui Fang, Yuan Zhuang, Fei Miao
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.11114v1)
- **发表日期**: 2026-05-11
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2605.11114v1](http://arxiv.org/abs/2605.11114v1)
- **📥 PDF**: 已下载至本地 (`2605.11114v1_SEVO_Semantic-Enhanced_Virtual_Observation_for_Robust_VLA_Manipulation_via_Active_Illumination_and_D.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）及通过社区工具链在低成本硬件上训练的模仿学习策略，在部署到训练环境之外时常常失败。现有评估（包括原始ACT和SmolVLA基准测试）在受控固定背景下显示出高成功率，但社区实践者报告称，这些策略在新环境中的迁移成功率近乎为零。我们提出SEVO（语义增强虚拟观测），这是一种以数据为中心的方法，在不修改策略架构的前提下提升跨环境操作鲁棒性。SEVO通过三种机制对原始RGB摄像头流进行转换：（1）体固相机，其组合视野覆盖完整操作工作空间；（2）主动红光照明，物理上归一化物体外观；（3）实时YOLO分割叠加，提供背景无关的语义线索。关键的是，我们证明多样化的数据采集协议（在遥操作期间系统性地改变光照、背景和干扰物）是泛化能力的唯一最重要因素。我们以透明水瓶（视觉上与环境融合的物体）为目标，选择简单的拾放任务，在两种移动平台上进行数百次受控真实机器人试验。完整流程在训练环境中使用ACT实现95%的抓取成功率，使用SmolVLA实现83%的成功率，在新环境中分别达到85%和75%。未使用SEVO时，相同策略在训练环境中仅达到75%/70%，在新环境中骤降至30-35%。我们的结果表明，原则性的观测设计及数据采集过程中的环境多样性（而非模型规模扩展）能使低成本机器人在日常家庭环境中可靠运行。

---

### 18. HarmoWAM: Harmonizing Generalizable and Precise Manipulation via Adaptive World Action Models

- **作者**: Qiuxuan Feng, Jiale Yu, Jiaming Liu, Yueru Jia, Zhuangzhe Wu, Hao Chen, Zezhong Qian, Shuo Gu, Peng Jia, Siwei Ma, Shanghang Zhang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.10942v1)
- **发表日期**: 2026-05-11
- **匹配关键词**: exploration, VLA
- **arXiv**: [2605.10942v1](http://arxiv.org/abs/2605.10942v1)
- **📥 PDF**: 已下载至本地 (`2605.10942v1_HarmoWAM_Harmonizing_Generalizable_and_Precise_Manipulation_via_Adaptive_World_Action_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 世界动作模型（WAMs）通过建模物理动力学，已成为机器人控制的一种有前景的范式。当前的WAMs主要遵循两种范式："先想象后执行"方法，即通过视频预测并利用逆动力学推断动作；以及"联合建模"方法，即联合建模动作与视频表征。基于系统性实验，我们观察到这两种范式之间存在根本性权衡：前者显式利用世界模型实现可泛化的状态转换，但缺乏交互精度；后者虽能生成细粒度、时间连贯的动作，却受限于训练分布的探索空间。受此启发，我们提出HarmoWAM——一种端到端的世界动作模型，它充分利用世界模型统一预测控制与反应控制，同时实现可泛化的状态转换与精准操作。具体而言，世界模型提供时空物理先验，用于调控两个互补的动作专家：预测专家利用潜在动力学进行迭代动作生成，反应专家则直接从预测的视觉演化中推断动作。为实现自适应协调，我们提出过程自适应门控机制，自动决定两者切换的时机与位置。这使得世界模型能驱动反应专家扩展探索空间，并让预测专家在任务的不同阶段执行精准交互。为评估性能，我们在六项真实机器人任务中构建了三种训练未见测试环境，涵盖背景、位置与物体语义的变化。值得注意的是，HarmoWAM在这些场景中展现出强大的零样本泛化能力，分别以33%和29%的绝对优势显著超越先前最先进的VLA模型与WAMs。

---

### 19. PriorVLA: Prior-Preserving Adaptation for Vision-Language-Action Models

- **作者**: Xinyu Guo, Bin Xie, Wei Chai, Xianchi Deng, Tiancai Wang, Zhengxing Wu, Xingyu Chen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.10925v1)
- **发表日期**: 2026-05-11
- **匹配关键词**: vision-language-action, vision-language-action model, VLA
- **arXiv**: [2605.10925v1](http://arxiv.org/abs/2605.10925v1)
- **📥 PDF**: 已下载至本地 (`2605.10925v1_PriorVLA_Prior-Preserving_Adaptation_for_Vision-Language-Action_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 大规模预训练使视觉-语言-动作（VLA）模型成为通用机器人操作的理想基础，但将其适配到下游任务仍不可或缺。然而，常见的全参数微调将预训练视为初始化过程，可能导致广泛先验知识向狭窄训练分布模式偏移。我们提出PriorVLA——一种新颖框架，通过保留预训练先验知识并学习如何利用这些知识实现高效适配。PriorVLA将冻结的先验专家作为只读先验知识源，同时训练适配专家完成下游任务特化。专家查询机制从预训练VLM中提取场景先验，并从先验专家中提取运动先验，将两者整合至适配专家以引导适配过程。相较于全参数微调，PriorVLA仅需更新25%的参数。在RoboTwin 2.0、LIBERO及真实世界任务中，PriorVLA的整体性能全面超越全参数微调及当前最优VLA基线模型，在分布外（OOD）与小样本场景下提升最为显著。PriorVLA在RoboTwin 2.0-Hard任务上相较pi0.5提升11个百分点，在LIBERO上达到99.1%的平均成功率。在涵盖八项真实世界任务与两种机器人形态的实验中，PriorVLA使用标准数据达到81%的分布内（ID）成功率与57%的OOD成功率；在每项任务仅提供10条示范数据的情况下，仍能实现48%的ID成功率与32%的OOD成功率，分别超越pi0.5达24和22个百分点。

---

### 20. RoboMemArena: A Comprehensive and Challenging Robotic Memory Benchmark

- **作者**: Huashuo Lei, Wenxuan Song, Huarui Zhang, Jieyuan Pei, Jiayi Chen, Haodong Yan, Han Zhao, Pengxiang Ding, Zhipeng Zhang, Lida Huang, Donglin Wang, Yan Wang, Haoang Li
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.10921v1)
- **发表日期**: 2026-05-11
- **匹配关键词**: VLA
- **arXiv**: [2605.10921v1](http://arxiv.org/abs/2605.10921v1)
- **📥 PDF**: 已下载至本地 (`2605.10921v1_RoboMemArena_A_Comprehensive_and_Challenging_Robotic_Memory_Benchmark.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 记忆是机器人智能的关键组成部分，因为机器人必须依赖过去的观测和行动，在部分可观测环境中完成长期任务。然而，现有的机器人记忆基准测试仍缺乏用于记忆形成的多模态标注，任务覆盖范围和结构复杂度有限，且仅局限于仿真环境，缺乏真实世界评估。为此，我们提出RoboMemArena——一个包含26个任务的大规模基准测试，每个任务的平均轨迹长度超过1000步，其中68.9%的子任务依赖于记忆。其生成流程利用视觉语言模型（VLM）设计和组合子任务，通过原子函数生成完整轨迹，并提供与记忆相关的标注（包括子任务指令和原生关键帧标注），同时配套真实世界的记忆任务以支持物理评估。我们进一步设计了PrediMem——一种双系统视觉语言动作模型（VLA），其中高层VLM规划器管理包含近期缓冲区和关键帧缓冲区的记忆库，并利用预测编码头提升对任务动态变化的敏感性。在RoboMemArena上的大量实验表明，PrediMem优于所有基线方法，并为复杂记忆系统的记忆管理、模型架构和扩展规律提供了深刻见解。

---

