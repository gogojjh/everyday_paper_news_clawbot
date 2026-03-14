# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-03-14 08:05

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 4/20 篇提供

**🌟 Highlight**: 11 篇 | **📌 Poster**: 9 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. SaPaVe: Towards Active Perception and Manipulation in Vision-Language-Action Models for Robotics

- **作者**: Mengzhen Liu, Enshen Zhou, Cheng Chi, Yi Han, Shanyu Rong, Liming Chen, Pengwei Wang, Zhongyuan Wang, Shanghang Zhang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.12193v1)
- **发表日期**: 2026-03-12
- **匹配关键词**: active perception, perception and manipulation, vision-language-action model, vision-language-action
- **arXiv**: [2603.12193v1](http://arxiv.org/abs/2603.12193v1)
- **📥 PDF**: 已下载至本地 (`2603.12193v1_SaPaVe_Towards_Active_Perception_and_Manipulation_in_Vision-Language-Action_Models_for_Robotics.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://lmzpai.github.io/SaPaVe
- **中文摘要**: 主动感知与操作是机器人在复杂场景中实现交互的关键能力。现有方法难以将语义驱动的主动感知与鲁棒、视角无关的执行能力相统一。我们提出SaPaVe框架，通过数据高效的方式端到端联合学习这两项能力。该方法将相机控制与机械臂操作动作解耦而非置于共享动作空间，并采用自底向上的训练策略：首先在大规模数据集上训练语义相机控制，随后利用混合数据联合优化两类动作。为支撑该框架，我们构建了包含20万组图像-语言-相机运动对的ActiveViewPose-200K数据集用于语义相机运动学习，并设计了3D几何感知模块以提升动态视角下的执行鲁棒性。同时我们推出首个超越固定视角设置的主动操作评估基准ActiveManip-Bench。在仿真与真实环境的大量实验表明，SaPaVe在现实任务中成功率最高可提升31.25%，显著优于GR00T N1、\(π_0\)等近期视觉-语言-动作模型。这些结果证明，通过解耦但协调的训练策略实现紧密耦合的感知与执行，能够促成高效且可泛化的主动操作。项目页面：https://lmzpai.github.io/SaPaVe

---

### 2. Concurrent Prehensile and Nonprehensile Manipulation: A Practical Approach to Multi-Stage Dexterous Tasks

- **作者**: Hao Jiang, Yue Wu, Yue Wang, Gaurav S. Sukhatme, Daniel Seita
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.11655v1)
- **发表日期**: 2026-03-12
- **匹配关键词**: diffusion policy
- **arXiv**: [2603.11655v1](http://arxiv.org/abs/2603.11655v1)
- **📥 PDF**: 已下载至本地 (`2603.11655v1_Concurrent_Prehensile_and_Nonprehensile_Manipulation_A_Practical_Approach_to_Multi-Stage_Dexterous_T.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 灵巧手能够实现并行的抓取与非抓取操作，例如在持握一个物体的同时与另一个物体交互，这种能力在日常任务中至关重要，但在机器人领域尚未得到充分探索。学习此类长时程、高接触的多阶段行为具有挑战性，因为收集演示数据成本高昂，且端到端策略需要大量数据才能适应不同物体几何形状和摆放位置。我们提出DexMulti方法，这是一种样本高效的现实世界灵巧多任务操作方案，通过将演示分解为具有明确时间边界的以物体为中心的技能。不同于学习单一整体策略，我们的方法根据当前物体几何特征检索已演示技能，利用跟踪质心与偏航角的不确定性感知估计器将其与观测到的物体状态对齐，并通过"检索-对齐-执行"范式实现技能执行。我们在两个灵巧手平台（Allegro与LEAP）上对三种需要并行操作的多阶段任务（抓取+拉动、抓取+开启、抓取+抓取）进行了1000余次真实环境测试。该方法在训练物体上仅需每个物体3-4次演示即达到平均66%的成功率，性能超越扩散策略基线2-3倍且所需演示数据大幅减少。实验结果表明，该方法对未见物体及±25厘米范围内的空间变化均展现出鲁棒的泛化能力。

---

### 3. RoboClaw: An Agentic Framework for Scalable Long-Horizon Robotic Tasks

- **作者**: Ruiying Li, Yunlang Zhou, YuYao Zhu, Kylin Chen, Jingyuan Wang, Sukai Wang, Kongtao Hu, Minhui Yu, Bowen Jiang, Zhan Su, Jiayao Ma, Xin He, Yongjian Shen, Yangyang, Guanghui Ren, Maoqing Yao, Wenhao Wang, Yao Mu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.11558v1)
- **发表日期**: 2026-03-12
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2603.11558v1](http://arxiv.org/abs/2603.11558v1)
- **📥 PDF**: 已下载至本地 (`2603.11558v1_RoboClaw_An_Agentic_Framework_for_Scalable_Long-Horizon_Robotic_Tasks.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）系统在语言驱动的机器人操作方面展现出巨大潜力，但将其扩展至长周期任务仍面临挑战。现有技术流程通常将数据收集、策略学习与部署执行相分离，导致高度依赖人工环境重置且多策略执行脆弱。我们提出RoboClaw——一个智能机器人框架，在单一VLM驱动控制器下统一数据收集、策略学习与任务执行。在策略层面，RoboClaw创新性地引入纠缠动作对（EAP），通过将正向操作行为与逆向恢复动作耦合，形成自主数据收集的自重置循环。该机制能以最少人工干预实现持续的在线策略数据采集与迭代策略优化。在部署阶段，同一智能体执行高层推理并动态编排已学习的策略基元，以完成长周期任务。通过保持数据收集与任务执行阶段上下文语义的一致性，RoboClaw减少了两个阶段间的错配，提升了多策略鲁棒性。真实场景操作实验表明，相比传统开环流程，该系统在提升稳定性与可扩展性的同时，显著降低了机器人全生命周期中的人力投入——在长周期任务上成功率较基线方法提升25%，人力时间投入减少53.7%。

---

### 4. Vision-Based Hand Shadowing for Robotic Manipulation via Inverse Kinematics

- **作者**: Hendrik Chiche, Antoine Jamme, Trevor Rigoberto Martinez
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.11383v1)
- **发表日期**: 2026-03-11
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2603.11383v1](http://arxiv.org/abs/2603.11383v1)
- **📥 PDF**: 已下载至本地 (`2603.11383v1_Vision-Based_Hand_Shadowing_for_Robotic_Manipulation_via_Inverse_Kinematics.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 低成本机械臂的遥操作因人体手部关节动作映射至机器人关节指令的复杂性而面临挑战。本文提出一种基于单目第一视角RGB-D相机的离线手部动作捕捉与重定向流程，该相机搭载于3D打印眼镜框架。流程通过MediaPipe Hands算法检测每只手21个关键点，借助深度感知将其反投影至三维空间，转换至机器人坐标系后，在PyBullet物理引擎中采用阻尼最小二乘法求解逆运动学问题，从而生成六自由度SO-ARM101机器人的关节指令。夹爪控制器通过四级递补机制将拇指-食指几何关系映射为抓取开合度。所有动作先在物理仿真环境中预演，再通过LeRobot框架在实体机器人上复现。我们在结构化抓放基准测试（5格托盘，每格10次抓取）中评估逆运动学重定向流程，取得90%的成功率，并与四种基于领导者-跟随者遥操作数据训练的视觉-语言-动作策略（ACT、SmolVLA、pi0.5、GR00T N1.5）进行对比。同时，在非结构化现实场景（杂货店、药店）中测试该流程，因环境物体遮挡手部导致成功率降至9.3%（N=75），这既展现了无标记解析式重定向技术的潜力，也揭示了其当前局限性。

---

### 5. Learning to Assist: Physics-Grounded Human-Human Control via Multi-Agent Reinforcement Learning

- **作者**: Yuto Shibata, Kashu Yamazaki, Lalit Jayanti, Yoshimitsu Aoki, Mariko Isogawa, Katerina Fragkiadaki
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.11346v1)
- **发表日期**: 2026-03-11
- **匹配关键词**: exploration
- **arXiv**: [2603.11346v1](http://arxiv.org/abs/2603.11346v1)
- **📥 PDF**: 已下载至本地 (`2603.11346v1_Learning_to_Assist_Physics-Grounded_Human-Human_Control_via_Multi-Agent_Reinforcement_Learning.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 人形机器人具有改变日常服务和护理应用的巨大潜力。尽管物理引擎中的通用运动跟踪技术（GMT）的最新进展已使虚拟角色和人形机器人能够复现广泛的人类动作，但这些行为主要局限于无接触的社交互动或孤立运动。相比之下，辅助场景需要持续关注人类伙伴，并快速适应其不断变化的姿势和动态。本文提出将紧密互动、力量交换的人-人运动序列模仿建模为一个多智能体强化学习问题。我们在物理模拟器中联合训练支持者（助手）智能体和接收者智能体的伙伴感知策略，以跟踪辅助运动参考。为使该问题易于处理，我们引入了一种伙伴策略初始化方案，该方案从单人类运动跟踪控制器转移先验知识，极大地改进了探索过程。我们进一步提出动态参考重定向和接触促进奖励机制，使助手的参考运动适应接收者的实时姿态，并鼓励具有物理意义的支撑行为。研究表明，AssistMimic是首个能够在既定基准上成功跟踪辅助互动运动的方法，证明了多智能体强化学习框架在物理基础和社交感知的人形机器人控制中的优势。

---

### 6. PPGuide: Steering Diffusion Policies with Performance Predictive Guidance

- **作者**: Zixing Wang, Devesh K. Jha, Ahmed H. Qureshi, Diego Romeres
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.10980v1)
- **发表日期**: 2026-03-11
- **匹配关键词**: diffusion policy
- **arXiv**: [2603.10980v1](http://arxiv.org/abs/2603.10980v1)
- **📥 PDF**: 已下载至本地 (`2603.10980v1_PPGuide_Steering_Diffusion_Policies_with_Performance_Predictive_Guidance.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 扩散策略已被证明在学习机器人操作的复杂多模态行为方面非常高效。然而，生成动作序列中的误差会随时间累积，可能导致任务失败。现有方法通过增加专家示范数据或学习预测性世界模型来缓解这一问题，但这些方案可能带来较高的计算成本。我们提出性能预测引导框架——一种基于分类器的轻量级框架，能在推理阶段引导预训练的扩散策略避开失败模式。该框架采用新颖的自监督流程：通过基于注意力的多示例学习技术，自动识别策略运行轨迹中与任务成败相关的观测-动作片段，并基于这些自标注数据训练性能预测器。在推理过程中，该预测器通过实时梯度引导策略生成更稳健的动作序列。我们在Robomimic和MimicGen基准测试的多样化任务中验证了所提框架，实验结果表明该方法能持续提升任务执行性能。

---

### 7. RL-Augmented MPC for Non-Gaited Legged and Hybrid Locomotion

- **作者**: Andrea Patrizi, Carlo Rizzardo, Arturo Laurenzi, Francesco Ruscelli, Luca Rossini, Nikos G. Tsagarakis
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.10878v1)
- **发表日期**: 2026-03-11
- **匹配关键词**: navigation
- **arXiv**: [2603.10878v1](http://arxiv.org/abs/2603.10878v1)
- **📥 PDF**: 已下载至本地 (`2603.10878v1_RL-Augmented_MPC_for_Non-Gaited_Legged_and_Hybrid_Locomotion.pdf`)
- **🔓 开源**: CODE, GITHUB
  - 链接：https://github.com/AndrePatri/AugMPC.
- **中文摘要**: 我们提出了一种显式接触的分层架构，将强化学习（RL）与模型预测控制（MPC）相结合，其中高层RL智能体向低层运动MPC提供步态和导航指令。通过在仿真环境中通过试错学习非周期性步态，该架构将接触时序的组合负担从MPC中卸载。研究表明，仅需最小化的奖励设置和有限的调参即可获得有效策略。我们在仿真环境中验证了该架构在50公斤至120公斤不同机器人平台及多种MPC实现中的适用性，观察到在平坦地形腿式与混合式运动中非周期性步态和时序适应的涌现，并进一步证明了其在非平坦地形中的扩展能力。在所有平台上，我们实现了无需域随机化的零样本仿真到仿真迁移，并在120公斤轮腿式人形机器人Centauro上进一步展示了无需域随机化的零样本仿真到现实迁移。我们的软件框架与评估结果已公开于https://github.com/AndrePatri/AugMPC。

---

### 8. FG-CLTP: Fine-Grained Contrastive Language Tactile Pretraining for Robotic Manipulation

- **作者**: Wenxuan Ma, Chaofan Zhang, Yinghao Cai, Guocai Yao, Shaowei Cui, Shuo Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.10871v1)
- **发表日期**: 2026-03-11
- **匹配关键词**: vision-language-action, contact-rich manipulation, VLA
- **arXiv**: [2603.10871v1](http://arxiv.org/abs/2603.10871v1)
- **📥 PDF**: 已下载至本地 (`2603.10871v1_FG-CLTP_Fine-Grained_Contrastive_Language_Tactile_Pretraining_for_Robotic_Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 近期将触觉感知整合到视觉-语言-动作模型中的研究进展，已展现出对机器人感知能力的变革性潜力。然而，现有触觉表征主要依赖定性描述符（如纹理），忽略了力的大小、接触几何形态及主轴方向等定量接触状态，而这些对精细化操作至关重要。为填补这一空白，我们提出细粒度对比语言触觉预训练框架FG-CLTP。我们首先构建了一个包含超10万组触觉三维点云-语言对的新型数据集，该数据集从传感器视角显式捕捉多维接触状态。随后设计离散化数值标记机制实现定量-语义对齐，将显式物理度量有效注入多模态特征空间。所提出的FG-CLTP模型在分类任务中达到95.9%的准确率，回归误差较现有最优方法降低52.6%。三维点云表征的融合构建了传感器无关的基础框架，其仿真到现实的迁移误差仅为3.5%。基于此细粒度表征，我们进一步开发了由流匹配策略驱动的三维触觉-语言-动作架构，实现多模态推理与控制。大量实验表明，该框架在密集接触操作任务中显著优于现有基线方法，为触觉-语言-动作模型提供了稳健且可泛化的基础。

---

### 9. Node-RF: Learning Generalized Continuous Space-Time Scene Dynamics with Neural ODE-based NeRFs

- **作者**: Hiran Sarkar, Liming Kuang, Yordanka Velikova, Benjamin Busam
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.12078v1)
- **发表日期**: 2026-03-12
- **匹配关键词**: neural radiance field, nerf
- **arXiv**: [2603.12078v1](http://arxiv.org/abs/2603.12078v1)
- **📥 PDF**: 已下载至本地 (`2603.12078v1_Node-RF_Learning_Generalized_Continuous_Space-Time_Scene_Dynamics_with_Neural_ODE-based_NeRFs.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 从视觉观测中预测场景动态具有挑战性。现有方法仅能捕捉观测边界内的动态，难以在训练序列范围之外进行有效外推。Node-RF（基于神经常微分方程的神经辐射场）通过将神经常微分方程与动态神经辐射场相结合，克服了这一局限，实现了连续时空表征，能够在恒定内存成本下泛化至观测轨迹之外。该系统从视觉输入中学习隐式场景状态，通过常微分方程求解器实现状态随时间演化，并借助微分运算传播特征嵌入。基于神经辐射场的渲染器通过解析计算得到的嵌入特征，可合成任意视角以实现长程外推。通过对具有共享动态特性的多组运动序列进行训练，该方法能够泛化至未观测条件。实验表明，Node-RF无需显式模型即可表征抽象系统行为，并能识别未来预测的关键节点。

---

### 10. AstroSplat: Physics-Based Gaussian Splatting for Rendering and Reconstruction of Small Celestial Bodies

- **作者**: Jennifer Nolan, Travis Driver, John Christian
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.11969v1)
- **发表日期**: 2026-03-12
- **匹配关键词**: gaussian splatting, navigation, neural scene representation
- **arXiv**: [2603.11969v1](http://arxiv.org/abs/2603.11969v1)
- **📥 PDF**: 已下载至本地 (`2603.11969v1_AstroSplat_Physics-Based_Gaussian_Splatting_for_Rendering_and_Reconstruction_of_Small_Celestial_Bodi.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 基于图像的表面重建与表征对小天体（如小行星）探测任务至关重要，它为任务规划、导航和科学分析提供关键信息。高斯溅射技术的最新进展实现了高保真度的神经场景表征，但通常依赖于球谐光照强度参数化方法——这种方法严格基于表观建模，未能显式表达材质属性或光与表面的相互作用。我们提出AstroSplat框架，这是一种基于物理的高斯溅射方法，通过整合行星反射率模型，提升了对小天体表面原位图像的自主重建与光度表征能力。该框架在美国宇航局"黎明号"任务拍摄的真实图像上得到验证，相较于传统的球谐参数化方法，展现出更优越的渲染性能与表面重建精度。

---

### 11. CEI-3D: Collaborative Explicit-Implicit 3D Reconstruction for Realistic and Fine-Grained Object Editing

- **作者**: Yue Shi, Rui Shi, Yuxuan Xiong, Bingbing Ni, Wenjun Zhang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.11810v1)
- **发表日期**: 2026-03-12
- **匹配关键词**: 3d reconstruction, implicit representation, 3D reconstruction
- **arXiv**: [2603.11810v1](http://arxiv.org/abs/2603.11810v1)
- **📥 PDF**: 已下载至本地 (`2603.11810v1_CEI-3D_Collaborative_Explicit-Implicit_3D_Reconstruction_for_Realistic_and_Fine-Grained_Object_Editi.pdf`)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/shiyue001/CEI-3D.
- **中文摘要**: 现有三维编辑方法因其重建网络的高度集成性，常导致编辑结果失真且不够精细。为解决这一难题，本文提出CEI-3D——一个面向编辑任务的重建流程，旨在实现真实且细粒度的三维编辑。具体而言，我们设计了一种显隐协同的重建方法，通过隐式符号距离函数网络与差异化采样、局部可控的操作点集合共同表征目标物体。隐式网络提供平滑连续的几何先验，而显式操作点则实现局部控制，使全局三维结构与用户指定的局部编辑区域能够相互引导。为独立控制操作点的各属性，我们设计了物理属性解耦模块，将操作点的颜色信息分解为独立的物理属性。该模块还采用双漫反射反照率网络，通过独立分支分别处理编辑区域与非编辑区域，从而避免编辑操作产生非预期的相互干扰。基于解耦后的显隐协同重建表示，我们进一步提出空间感知编辑模块，支持对相关操作点进行分区调整。该模块采用基于跨视图传播的三维分割策略，帮助用户高效编辑目标部件的特定物理属性。在真实与合成数据集上的大量实验表明，相较于现有最优方法，本方法能以更短的编辑时间获得更真实、更精细的编辑效果。代码已开源：https://github.com/shiyue001/CEI-3D。

---

## 📌 Poster

*其他相关研究*

---

### 1. RADAR: Closed-Loop Robotic Data Generation via Semantic Planning and Autonomous Causal Environment Reset

- **作者**: Yongzhong Wang, Keyu Zhu, Yong Zhong, Liqiong Wang, Jinyu Yang, Feng Zheng
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.11811v1)
- **发表日期**: 2026-03-12
- **匹配关键词**: object manipulation
- **arXiv**: [2603.11811v1](http://arxiv.org/abs/2603.11811v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 大规模物理交互数据的获取作为现代机器人学习的关键前提，正因人工参与式采集模式的高昂成本与可扩展性限制而遭遇严重瓶颈。为突破此障碍，我们提出机器人鲁棒自主数据采集系统（RADAR）——一个完全自主的闭环数据生成引擎，彻底消除了采集周期中的人工干预。该系统通过四模块流水线优雅地分解认知负荷：以2-5个三维人体演示作为几何先验，视觉语言模型首先通过精确的语义对象定位与技能检索，生成与场景相关的任务序列；随后，图神经网络策略通过上下文模仿学习将这些子任务转化为物理动作；执行完成后，视觉语言模型通过结构化视觉问答流程进行自动化成功评估；最后，为突破人工重置的瓶颈，有限状态机协调自主环境重置与非对称数据路由机制。该系统通过严格遵循后进先出因果序列的正反向同步规划，能无缝恢复非结构化工作空间，并从执行故障中稳健恢复。这种持续的大脑-小脑协同作用将数据采集转化为自我维持的过程。大量实验验证了RADAR的卓越泛化能力：在仿真环境中，本框架在复杂长周期任务上达成高达90%的成功率，轻松解决传统基线方法性能趋近于零的挑战；在现实场景部署中，系统通过少量样本适应即可可靠执行多样化、高接触密度的技能（如可变形物体操控），且无需领域特定微调，为机器人数据采集提供了高度可扩展的范式。

---

### 2. HiSync: Spatio-Temporally Aligning Hand Motion from Wearable IMU and On-Robot Camera for Command Source Identification in Long-Range HRI

- **作者**: Chengwen Zhang, Chun Yu, Borong Zhuang, Haopeng Jin, Qingyang Wan, Zhuojun Li, Zhe He, Zhoutong Ye, Yu Mei, Chang Liu, Weinan Shi, Yuanchun Shi
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.11809v1)
- **发表日期**: 2026-03-12
- **匹配关键词**: HRI, human-robot interaction
- **arXiv**: [2603.11809v1](http://arxiv.org/abs/2603.11809v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 远距离人机交互（HRI）领域仍待深入探索。其中，命令源识别（CSI）——即确定指令发出者——因多用户场景及远距离导致的传感器模糊性而尤为困难。本研究提出HiSync光学-惯性融合框架，通过将机器人搭载摄像机的光流数据与佩戴于手部的惯性测量单元（IMU）信号进行对齐，将手部运动作为绑定线索。我们首先构建了用户自定义手势集（N=12），并在远距离多用户HRI场景中采集了多模态指令手势数据集（N=38）。HiSync从摄像机与IMU数据中提取频域手部运动特征，通过训练的CSINet网络对IMU读数降噪、实现多模态时序对齐，并采用距离感知多窗口融合机制计算细微自然手势的跨模态相似度，从而实现鲁棒的CSI。在34米范围内的三人交互场景中，HiSync达到92.32%的CSI准确率，较现有最优方法提升48.44%。该系统在真实机器人部署中得到验证。通过实现可靠且自然的命令源识别，HiSync为公共空间人机交互提供了实用基础模块与设计指南。

---

### 3. Coupling Tensor Trains with Graph of Convex Sets: Effective Compression, Exploration, and Planning in the C-Space

- **作者**: Gerhard Reinerth, Riddhiman Laha, Marcello Romano
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.11658v1)
- **发表日期**: 2026-03-12
- **匹配关键词**: exploration, motion planning
- **arXiv**: [2603.11658v1](http://arxiv.org/abs/2603.11658v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出TANGO（张量与图优化）——一种创新的运动规划框架，该框架将基于张量的压缩技术与结构化图优化相结合，以实现高效且可扩展的轨迹生成。尽管基于优化的规划器（如凸集图GCS）为生成平滑最优轨迹提供了强大工具，但它们通常依赖于对高维构型空间进行预定义的凸特性描述，这一要求对于通用机器人任务往往难以实现。TANGO通过采用张量链分解技术，以压缩形式近似表示可行构型空间，从而实现对任务相关区域的快速发现与估计。这些区域随后被嵌入到类GCS结构中，支持在遵循系统约束与环境复杂性的前提下进行几何感知的运动规划。通过将张量压缩与结构化图推理相结合，TANGO不仅实现了高效的几何感知运动规划，还为未来机器人系统中构型空间的更具表现力与可扩展性表征奠定了基础。在平面机器人与真实机器人上的严格仿真实验，验证了我们在有效压缩与高质量轨迹生成方面的优势。

---

### 4. A Hybrid Neural-Assisted Unscented Kalman Filter for Unmanned Ground Vehicle Navigation

- **作者**: Gal Versano, Itzik Klein
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.11649v1)
- **发表日期**: 2026-03-12
- **匹配关键词**: navigation, autonomous navigation
- **arXiv**: [2603.11649v1](http://arxiv.org/abs/2603.11649v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 现代无人地面车辆的自主导航依赖于多种估计器来融合惯性传感器与全球导航卫星系统测量数据。然而，固定噪声协方差矩阵往往难以适应动态变化的实际环境条件。本研究提出一种混合估计框架，将经典状态估计原理与现代深度学习方法相结合。该框架不改变无迹卡尔曼滤波的基本方程，而是通过专门设计的深度神经网络直接从原始惯性和GNSS测量数据中预测过程噪声与测量噪声的不确定性。我们采用仿真到现实的训练策略，仅使用仿真数据进行模型训练。这种方法既能提供完美的地面真实数据，又避免了大量实际数据采集的负担。为评估所提方法并检验其泛化能力，我们采用来自三个数据集的160分钟测试集进行验证，每个数据集包含不同类型的车辆（越野车、乘用车和移动机器人）、惯性传感器、路面状况及环境条件。实验结果表明，在三个数据集上，相较于基于自适应模型的方法，本方法实现了$12.7\%$的位置精度提升，从而为无人地面车辆导航任务提供了更具扩展性和鲁棒性的解决方案。

---

### 5. From Pets to Robots: MojiKit as a Data-Informed Toolkit for Affective HRI Design

- **作者**: Liwen He, Pingting Chen, Ziheng Tang, Yixiao Liu, Jihong Jeung, Teng Han, Xin Tong
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.11632v1)
- **发表日期**: 2026-03-12
- **匹配关键词**: HRI
- **arXiv**: [2603.11632v1](http://arxiv.org/abs/2603.11632v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 为动物仿生社交机器人设计情感行为常依赖直觉与个人经验，导致设计成果零散化。为提供更系统化的指导，我们首先对人类与宠物互动视频进行编码分析，通过文献研究和访谈验证洞察，并创建了结构化参考卡片以系统呈现宠物仿生情感交互的设计维度。在此基础上，我们开发了MojiKit工具包，该工具包整合了参考卡片、仿生机器人原型（MomoBot）以及行为控制工作室。通过对18名参与者开展协同创作工作坊评估，我们发现MojiKit帮助参与者基于自身宠物经验之外设计了35种情感交互模式，同时零代码工作室降低了技术门槛并增强了创作自主性。本研究的贡献包括：为宠物仿生人机情感交互设计提供数据驱动的结构化资源，构建连接参考资料与动手实践的集成工具包，并通过实证研究证明MojiKit如何帮助用户系统化地创造更丰富多元的情感机器人行为。

---

### 6. SVLL: Staged Vision-Language Learning for Physically Grounded Embodied Task Planning

- **作者**: Yuyuan Yang, Junkun Hong, Hongrong Wang, Honghao Cai, Xunpeng Ren, Ge Wang, Mingcong Lei, Shenhao Yan, Jiahao Yang, Chengsi Yao, Xi Li, Yiming Zhao, Yatong Han, Jinke Ren
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.11563v1)
- **发表日期**: 2026-03-12
- **匹配关键词**: affordance
- **arXiv**: [2603.11563v1](http://arxiv.org/abs/2603.11563v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: CODE
- **中文摘要**: 具身任务规划要求视觉语言模型生成既在视觉上具有基础性，又在时间上保持因果连贯的动作序列。然而，现有的训练范式面临一个关键权衡：联合端到端训练常导致过早的时间绑定，而标准的强化学习方法则存在优化不稳定的问题。为弥合这一差距，我们提出了分阶段视觉语言学习（SVLL），这是一个统一的三阶段框架，旨在实现稳健且基于物理现实的具身规划。在前两个阶段，SVLL将空间基础与时间推理解耦，在引入序列动作历史之前建立稳健的视觉依赖。在最后阶段，我们发现标准直接偏好优化（DPO）存在一个关键局限——其纯相对性：仅优化获胜与失败轨迹之间的偏好差距，而忽略最优路径的绝对似然约束，这常导致不安全或幻觉行为。为解决这一问题，我们进一步引入偏置DPO（Bias-DPO），这是一种新颖的对齐目标，通过显式最大化真实动作的似然性，同时惩罚过度自信的幻觉，从而注入对专家轨迹的归纳偏置。通过将策略锚定在专家流形上并缓解因果错位，由Bias-DPO驱动的SVLL确保严格遵循环境可供性，并有效抑制物理上不可能的捷径。最后，在交互式AI2-THOR基准测试和真实世界机器人部署中的大量实验表明，SVLL在任务成功率上优于最先进的开源模型（如Qwen2.5-VL-7B）和闭源模型（如GPT-4o、Gemini-2.0-flash），同时显著减少了物理约束违反情况。

---

### 7. CoViLLM: An Adaptive Human-Robot Collaborative Assembly Framework Using Large Language Models for Manufacturing

- **作者**: Jiabao Zhao, Jonghan Lim, Hongliang Li, Ilya Kovalenko
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.11461v1)
- **发表日期**: 2026-03-12
- **匹配关键词**: human-robot collaboration
- **arXiv**: [2603.11461v1](http://arxiv.org/abs/2603.11461v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 随着大规模定制需求的日益增长，依赖规则化操作的传统制造机器人缺乏适应定制化或新型产品变体的灵活性。人机协作通过结合人类的多功能性和决策能力，已展现出提升系统适应性的潜力。然而，现有的人机协作框架通常依赖于预定义的感知-操作流程，限制了其针对新产品装配自主生成任务规划的能力。本研究提出CoViLLM——一种自适应人机协作装配框架，支持定制化及先前未见产品的装配任务。该框架融合了基于深度摄像头的物体定位技术用于位置估计、操作员分类机制用于识别新组件，并利用大型语言模型根据自然语言指令生成装配任务规划。该框架在NIST装配任务板上针对已知产品、定制化产品及新产品场景进行了验证。实验结果表明，所提出的框架通过将人机协作拓展至预定义产品和任务设置之外，实现了灵活的协同装配能力。

---

### 8. Enhancing Lightweight Vision Language Models through Group Competitive Learning for Socially Compliant Navigation

- **作者**: Xinyu Zhang, Atsushi Konno, Toshihiko Yamasaki, Ling Xiao
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.11447v1)
- **发表日期**: 2026-03-12
- **匹配关键词**: navigation, robot navigation, social navigation
- **arXiv**: [2603.11447v1](http://arxiv.org/abs/2603.11447v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 社交机器人导航需要场景语义与人类社交规范的高度融合。视觉语言模型（VLM）的规模扩展通常能提升社交合规导航的推理与决策能力，但模型增大伴随显著计算开销，限制了其在实时机器人部署中的适用性。反之，轻量级VLM虽能实现高效推理，却在复杂社交环境中表现出较弱的推理决策能力。如何兼顾强大推理能力与高效运行仍是开放挑战。为弥合这一差距，我们提出群体竞争学习（GCL）策略，旨在增强轻量级VLM的能力。该策略通过引入群体竞争目标（GCO）协调全局语义与分布正则化，并采用非对称群体优化（AGO）探索模型性能上限。在社交导航基准测试中的实证评估表明，GCL显著提升了VLM性能：Qwen2.5-VL-3B学习模型与Qwen3-VL-4B引导模型分别实现0.968和0.914的F1分数，较原始监督微调（SFT）提升40%和12%。值得注意的是，原始SFT下3B模型原本落后于8B模型（F1分数0.692对0.755），而通过GCL策略，3B模型反超8B基线模型达28%。这些结果表明，GCL为实现实际部署中高精度与计算效率的平衡提供了有效解决方案。

---

### 9. A Causal Approach to Predicting and Improving Human Perceptions of Social Navigation Robots

- **作者**: Maximilian Diehl, Nathan Tsoi, Gustavo Chavez, Karinne Ramirez-Amaro, Marynel Vázquez
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.11290v1)
- **发表日期**: 2026-03-11
- **匹配关键词**: navigation, HRI, social navigation
- **arXiv**: [2603.11290v1](http://arxiv.org/abs/2603.11290v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 随着移动机器人在人类环境中的部署日益增多，使其能够预测人类对其的感知对于实现社会适应性导航至关重要。预测感知面临两大挑战：(1)人机交互预测模型必须从有限数据中学习；(2)所获模型需具备可解释性以确保安全有效交互。当机器人被感知为能力不足时（例如机器人突然停止或偏离目标转向），可解释性尤为重要——这使机器人能够解释其推理逻辑并识别可控因素以提升表现，此时需要因果推理而非关联推理。为应对这些挑战，我们提出一种因果贝叶斯网络，旨在预测人类如何感知移动机器人的能力及其在导航过程中如何解读机器人意图。此外，我们引入一种创新方法，通过基于因果模型的组合搜索来识别更优导航行为，从而提升机器人感知能力。该方法在实现与前沿方法相当或更优预测性能（二元评估中能力与意图预测的F1分数分别达0.78和0.75）的同时，增强了可解释性并生成反事实机器人运动。为进一步评估本方法提升机器人感知能力的效果，我们开展了在线评估实验，用户通过5点李克特量表对机器人行为进行评分。统计数据显示，本方法将低能力机器人行为的感知能力显著提升了83%。

---

