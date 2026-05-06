# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-05-06 08:03

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 3/20 篇提供

**🌟 Highlight**: 9 篇 | **📌 Poster**: 11 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. MolmoAct2: Action Reasoning Models for Real-world Deployment

- **作者**: Haoquan Fang, Jiafei Duan, Donovan Clay, Sam Wang, Shuo Liu, Weikai Huang, Xiang Fan, Wei-Chuan Tsai, Shirui Chen, Yi Ru Wang, Shanli Xing, Jaemin Cho, Jae Sung Park, Ainaz Eftekhar, Peter Sushko, Karen Farley, Angad Wadhwa, Cole Harrison, Winson Han, Ying-Chun Lee, Eli VanderBilt, Rose Hendrix, Suveen Ellawela, Lucas Ngoo, Joyce Chai, Zhongzheng Ren, Ali Farhadi, Dieter Fox, Ranjay Krishna
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.02881v1)
- **发表日期**: 2026-05-04
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2605.02881v1](http://arxiv.org/abs/2605.02881v1)
- **📥 PDF**: 已下载至本地 (`2605.02881v1_MolmoAct2_Action_Reasoning_Models_for_Real-world_Deployment.pdf`)
- **🔓 开源**: MODEL, PROJECT_PAGE
- **中文摘要**: 视觉-语言-动作（VLA）模型旨在为机器人提供通用的单一控制器，但当前的系统在实际部署的关键指标上仍存在不足。前沿模型封闭，开源替代方案依赖昂贵硬件，增强推理的策略因延迟过高而难以实现基础能力，微调后的成功率也未能达到可靠使用的阈值。我们提出MolmoAct2，一个为实际部署构建的完全开源动作推理模型，在五个维度上对其前身进行了改进。我们引入MolmoER，一个专为空间与具身推理设计的VLM骨干网络，采用“先专精后演练”的训练方法，在330万样本的语料库上完成训练。我们发布了三个覆盖中低端平台的新数据集，包括MolmoAct2-BimanualYAM——包含720小时遥操作双臂轨迹，是迄今为止最大的开源双臂数据集，以及经过质量筛选的Franka（DROID）和SO100/101子集。我们提供OpenFAST，一个在五种具身形态的百万级轨迹上训练的开源权重、开源数据动作分词器。我们重新设计了架构，通过逐层KV缓存条件将流匹配连续动作专家模块嫁接至离散分词VLM上。最后，我们提出MolmoThink，一种自适应深度推理变体，仅对时间步间变化的场景区域重新预测深度标记，以极低的延迟保留几何基础能力。在迄今为止任何开源VLA最广泛的实证研究中（涵盖7个仿真与真实世界基准），MolmoAct2优于包括Pi-05在内的强基线模型，而MolmoER在13个具身推理基准上超越了GPT-5和Gemini Robotics ER-1.5。我们开源模型权重、训练代码及完整训练数据。项目页面：https://allenai.org/blog/molmoact2

---

### 2. Seeing Realism from Simulation: Efficient Video Transfer for Vision-Language-Action Data Augmentation

- **作者**: Chenyu Hui, Xiaodi Huang, Siyu Xu, Yunke Wang, Shan You, Fei Wang, Tao Huang, Chang Xu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.02757v1)
- **发表日期**: 2026-05-04
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2605.02757v1](http://arxiv.org/abs/2605.02757v1)
- **📥 PDF**: 已下载至本地 (`2605.02757v1_Seeing_Realism_from_Simulation_Efficient_Video_Transfer_for_Vision-Language-Action_Data_Augmentation.pdf`)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/nanfangxiansheng/Seeing-Realism-from-Simulation.
- **中文摘要**: 视觉-语言-动作（VLA）模型通常依赖大规模真实世界视频，而仿真数据虽然采集成本低廉且易于并行化，却常因显著的视觉域差异和有限的环境多样性导致真实世界泛化能力薄弱。我们提出一种高效视频增强框架，可将仿真VLA视频转化为逼真的训练视频，同时保留任务语义和动作轨迹。该流程通过视频语义分割和视频描述技术从仿真中提取结构化条件，重写描述以丰富环境多样性，并利用条件视频迁移模型合成逼真视频。为实现规模化增强，我们引入扩散特征复用机制，通过跨相邻时间步复用视频令牌加速生成，并设计核心集采样策略，在有限计算资源下识别紧凑无冗余的子集进行增强。在Robotwin 2.0、LIBERO、LIBERO-Plus及真实机器人平台上的大量实验表明该方法具有持续改进效果。例如，我们的方法使RDT-1B在Robotwin 2.0上提升8%，在更具挑战性的LIBERO-Plus基准测试中使$π_0$提升5.1%。代码开源地址：https://github.com/nanfangxiansheng/Seeing-Realism-from-Simulation。

---

### 3. Latent Bridge: Feature Delta Prediction for Efficient Dual-System Vision-Language-Action Model Inference

- **作者**: Yudong Liu, Yuan Li, Zijia Tang, Yuxi Zheng, Yueqian Lin, Qinsi Wang, Yi Li, Shuangjun Liu, Shuai Zhang, Taotao Jing, Dashan Gao, Ning Bi, Jingwei Sun, Yiran Chen, Hai Li
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.02739v1)
- **发表日期**: 2026-05-04
- **匹配关键词**: vision-language-action model, vision-language-action, VLA
- **arXiv**: [2605.02739v1](http://arxiv.org/abs/2605.02739v1)
- **📥 PDF**: 已下载至本地 (`2605.02739v1_Latent_Bridge_Feature_Delta_Prediction_for_Efficient_Dual-System_Vision-Language-Action_Model_Infere.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 双系统视觉-语言-动作（VLA）模型在机器人操作任务中达到了最先进水平，但其性能受限于视觉-语言模型（VLM）主干网络——该网络必须在每个控制步骤中执行推理，同时产生时间冗余特征。我们提出潜桥模型（Latent Bridge），这是一种轻量级模型，能够预测不同时间步之间VLM输出的变化量，使得动作头可以基于预测输出运行，而昂贵的VLM主干网络仅需周期性调用。我们在两种架构不同的VLA模型上实例化了潜桥模型：GR00T-N1.6（特征空间桥接）和π0.5（KV缓存桥接），证明了该方法可泛化至不同VLA设计。我们的任务无关型DAgger训练流程无需修改即可跨基准测试迁移。在四个LIBERO任务套件、24项RoboCasa厨房任务以及ALOHA仿真转移立方体任务中，潜桥模型在减少50-75% VLM调用次数的同时实现了95-100%的性能保持，每轮任务净加速比达1.65-1.73倍。

---

### 4. CoRAL: Contact-Rich Adaptive LLM-based Control for Robotic Manipulation

- **作者**: Berk Çiçek, Mert K. Er, Özgür S. Öğüz
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.02600v1)
- **发表日期**: 2026-05-04
- **匹配关键词**: contact-rich manipulation, VLA
- **arXiv**: [2605.02600v1](http://arxiv.org/abs/2605.02600v1)
- **📥 PDF**: 已下载至本地 (`2605.02600v1_CoRAL_Contact-Rich_Adaptive_LLM-based_Control_for_Robotic_Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 尽管大型语言模型（LLMs）和视觉语言模型（VLMs）在高层次推理与语义理解方面展现出卓越能力，但由于缺乏显式的物理基础且无法执行自适应控制，将其直接应用于富含接触的操作任务仍面临挑战。为弥合这一差距，我们提出CoRAL（基于LLM的自适应接触丰富控制）模块化框架，通过将高层推理与低层控制解耦实现零样本规划。与黑箱策略不同，CoRAL并非将LLM用作直接控制器，而是将其作为成本函数设计者，为基于采样的运动规划器（MPPI）合成具有上下文感知能力的目标函数。针对视觉数据中物理参数的模糊性，我们引入神经符号自适应循环：视觉语言模型为环境动力学（如质量与摩擦系数估计）提供语义先验，随后通过在线系统辨识实时显式优化这些参数，同时LLM基于交互反馈迭代调整成本函数结构以修正策略性错误。此外，基于检索的记忆单元使系统能够在重复性任务中复用成功策略。这种分层架构通过将高层语义推理与反应式执行解耦，确保实时控制稳定性，有效弥合了LLM缓慢推理与动态接触需求之间的鸿沟。我们在仿真与真实硬件平台上，针对利用外部接触沿墙壁翻转物体等新颖挑战性任务验证了CoRAL的性能。实验表明，在未见过的富含接触场景中，CoRAL通过自适应物理理解能力，将成功率平均提升超过50%，显著优于当前最先进的VLA与基于基础模型的规划器基线方法，并有效处理了仿真到现实的迁移差距。

---

### 5. Natural Gradient Bayesian Filtering: Geometry-Aware Filter for Dynamical Systems

- **作者**: Chang Liu, Wenhan Cao, Zeju Sun, Tianyi Zhang, Jiayu Yuan, Yi Zeng, Ting Yuan, Yao Lyu, Wei Wu, Stephen Shing-Toung Yau, Shengbo Eben Li
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.02306v1)
- **发表日期**: 2026-05-04
- **匹配关键词**: localization and mapping
- **arXiv**: [2605.02306v1](http://arxiv.org/abs/2605.02306v1)
- **📥 PDF**: 已下载至本地 (`2605.02306v1_Natural_Gradient_Bayesian_Filtering_Geometry-Aware_Filter_for_Dynamical_Systems.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 贝叶斯滤波是航空航天系统等复杂系统中状态估计的基石，但其精确解仅适用于线性高斯模型。在实际应用中，非线性系统通过可处理的近似方法处理，其中扩展卡尔曼滤波和无迹卡尔曼滤波等高斯滤波器是最广泛使用的方法之一。本教程从信息几何的视角重新审视高斯滤波，将预测和测量更新步骤视为状态分布上的推断过程。在此框架下，我们引入了一种几何感知的高斯滤波方法，该方法利用高斯分布统计流形上的自然梯度下降。由此产生的自然梯度高斯近似（NANO）滤波器迭代优化后验均值和协方差，同时尊重高斯族的内在几何结构并保持协方差矩阵的正定性。我们进一步揭示了与经典卡尔曼滤波的基本联系，表明在线性高斯情况下，单步自然梯度更新即可精确恢复卡尔曼测量更新。通过代表性非线性估计问题的案例研究，包括卫星姿态估计、同步定位与地图构建，以及四足机器人和人形机器人等机器人系统的状态估计，展示了所提出框架的实际意义。

---

### 6. Change-Robust Online Spatial-Semantic Topological Mapping

- **作者**: Jiaming Wang, Jizhuo Chen, Diwen Liu, Atharva Ghotavadekar, Jiaxuan Da, Linh Kästner, Harold Soh
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.02227v1)
- **发表日期**: 2026-05-04
- **匹配关键词**: navigation, object-goal navigation
- **arXiv**: [2605.02227v1](http://arxiv.org/abs/2605.02227v1)
- **📥 PDF**: 已下载至本地 (`2605.02227v1_Change-Robust_Online_Spatial-Semantic_Topological_Mapping.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 自主机器人需要具备应对环境变化的鲁棒空间-语义推理能力：即利用空间和语义知识，在环境变化的情况下决定前往何处、如何抵达以及确定自身位置。现有方法通常将语义信息附加到基于SLAM构建的度量地图上，但这些流程在面对外观变化和场景动态时较为脆弱，会导致数据关联和重定位性能下降。我们提出一种鲁棒变化的在线空间-语义（CROSS）表示方法，该方法用基于RGB-D关键帧的在线位姿感知拓扑图替代全局一致的度量基底。系统通过连续SE(3)空间中的序贯假设检验，显式处理感知模糊性。我们的估计器维持对位姿的有界高斯混合置信度，从而能够原则性地处理闭环检测和机器人绑架事件。在严重外观变化条件下（包括真实机器人目标导向导航任务中光照变化和家具重排）的实验表明，该方法相比基于SLAM和拓扑的基线方法具有更强的鲁棒性，同时在感知混淆情况下仍能保持安全性。

---

### 7. VILAS: A VLA-Integrated Low-cost Architecture with Soft Grasping for Robotic Manipulation

- **作者**: Zijian An, Hadi Khezam, Bill Cai, Ran Yang, Shijie Geng, Yiming Feng, Yue, Zheng, Lifeng Zhou
- **单位**: Luna; Luna; Luna...
- **发表日期**: 2026-05-03
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2605.02037v1](http://arxiv.org/abs/2605.02037v1)
- **📥 PDF**: 已下载至本地 (`2605.02037v1_VILAS_A_VLA-Integrated_Low-cost_Architecture_with_Soft_Grasping_for_Robotic_Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出了VILAS——一个完全低成本、模块化的机器人操作平台，旨在支持端到端视觉-语言-动作（VLA）策略的学习与部署，并可在可负担的硬件上运行。该系统集成了Fairino FR5协作臂、Jodell RG52-50电动夹爪和双摄像头感知模块，通过基于ZMQ的通信架构实现统一协调，在单一框架内无缝衔接遥操作、数据采集和策略部署。为在不依赖显式力传感的情况下安全操作易碎物体，我们设计了一种基于剪纸结构的柔性顺应夹爪扩展件，该扩展件在受压载荷下产生可预测形变，从而实现对脆弱目标的温和且可重复的接触。我们在VILAS平台上部署并评估了三种最先进的VLA模型：pi_0、pi_0.5和GR00T N1.6。所有模型均使用通过遥操作流程采集的相同演示数据集，从公开发布的预训练检查点进行微调。在葡萄抓取任务上的实验验证了所提系统的有效性，证明低成本模块化硬件能够成功训练并部署具备能力的操作策略。我们的结果进一步为当前VLA模型在真实环境中的部署特性提供了实践性见解。

---

### 8. Phone2Act: A Low-Cost, Hardware-Agnostic Teleoperation System for Scalable VLA Data Collection

- **作者**: Om Mandhane, Bipin Yadav, Sangeetha Prasanna Ram, Gopalakrishnan Narayanan
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.01948v1)
- **发表日期**: 2026-05-03
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2605.01948v1](http://arxiv.org/abs/2605.01948v1)
- **📥 PDF**: 已下载至本地 (`2605.01948v1_Phone2Act_A_Low-Cost,_Hardware-Agnostic_Teleoperation_System_for_Scalable_VLA_Data_Collection.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 收集用于视觉-语言-动作（VLA）模型训练的多样化、高质量操作数据，对许多研究团队而言仍成本高昂，因为现有遥操作框架依赖专用硬件或与特定机器人平台紧密耦合。我们提出Phone2Act——一种低成本、硬件无关的遥操作框架，通过Google ARCore将普通智能手机转化为六自由度机器人控制器。该框架基于模块化ROS 2架构，通过可互换桥接节点将控制逻辑与硬件细节解耦，无需修改代码即可支持从工业协作机器人到低成本双臂机械臂等平台。通用记录器同步多摄像头RGB流与机器人状态反馈，并原生导出为LeRobot数据集格式，省去后处理步骤，实现即时VLA微调。我们通过收集130个演示片段微调GR00T-N1.5验证该框架，在实体Dobot CR5上执行真实多阶段拾取放置任务时，成功率达90%。

---

### 9. Anticipation-VLA: Solving Long-Horizon Embodied Tasks via Anticipation-based Subgoal Generation

- **作者**: Zhilong Zhang, Wenyu Luo, Haonan Wang, Yifei Sheng, Yidi Wang, Hanyuan Guo, Haoxiang Ren, Xinghao Du, Yuhan Che, Tongtong Cao, Lei Yuan, Yang Yu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.01772v1)
- **发表日期**: 2026-05-03
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2605.01772v1](http://arxiv.org/abs/2605.01772v1)
- **📥 PDF**: 已下载至本地 (`2605.01772v1_Anticipation-VLA_Solving_Long-Horizon_Embodied_Tasks_via_Anticipation-based_Subgoal_Generation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型已成为具身智能领域的重要范式，使机器人能够根据自然语言指令和当前视觉输入执行任务。然而，现有VLA模型在长时域任务中因误差累积而表现不佳。现有方法将任务分解为固定粒度的子任务，无法适应执行状态变化的复杂性，限制了其在长时域任务中的鲁棒性。为解决这一问题，我们提出预测模型（Anticipation Model），该模型能够自适应且递归地生成未来子目标。随着任务推进，该模型持续调整未来子目标以响应动态变化，从而构建更可靠的规划路径。基于此概念，我们提出Anticipation-VLA——一种分层VLA模型，通过预测模型生成可执行的子目标来指导VLA策略执行。我们通过微调统一多模态模型（UMM）实现高层子目标生成，并采用目标条件化VLA策略执行底层动作。在仿真和真实机器人任务中的实验表明，Anticipation-VLA的有效性，凸显了自适应递归子目标生成对鲁棒策略执行的重要性。

---

## 📌 Poster

*其他相关研究*

---

### 1. Semantic Risk-Aware Heuristic Planning for Robotic Navigation in Dynamic Environments: An LLM-Inspired Approach

- **作者**: Hamza Ahmed Durrani, Rafay Suleman Durrani
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.02862v1)
- **发表日期**: 2026-05-04
- **匹配关键词**: robot navigation, navigation, path planning
- **arXiv**: [2605.02862v1](http://arxiv.org/abs/2605.02862v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 将大语言模型推理原理融入经典机器人路径规划，已成为一个快速发展的研究方向。本文提出一种语义风险感知启发式（SRAH）规划器，将受大语言模型启发的代价函数（用于惩罚几何拥挤或高风险区域）编码至A$^*$搜索框架中，并增加动态障碍物检测时的闭环重规划功能。我们在一个静态障碍物密度为20%、包含随机动态障碍物的$15{\times}15$网格世界中，通过200次随机试验，将SRAH与两种基线方法——带重规划的广度优先搜索（BFS）和不带重规划的贪婪启发式算法——进行对比评估。SRAH的任务成功率达到62.0%，相较于BFS（56.5%）相对提升9.7%，并大幅优于贪婪算法（4.0%）。我们进一步分析了规划开销、路径效率与故障恢复次数之间的权衡关系，并通过障碍物密度消融实验证明，语义代价塑形能在不同难度的环境中持续改善导航性能。研究结果表明，即使是轻量级的、受大语言模型启发的启发式方法，也能为自主机器人导航带来显著的安全性与鲁棒性提升。

---

### 2. LiDAR Teach, Radar Repeat: Robust Cross-Modal Navigation in Degenerate and Varying Environments

- **作者**: Renxiang Xiao, Yichen Chen, Yuanfan Zhang, Qianyi Shao, Yushuai Chen, Yuxuan Han, Yunjiang Lou, Liang Hu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.02809v1)
- **发表日期**: 2026-05-04
- **匹配关键词**: long-term autonomy, navigation
- **arXiv**: [2605.02809v1](http://arxiv.org/abs/2605.02809v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 长期自主导航要求系统在动态与静态变化的环境以及恶劣天气条件下具备稳健的导航能力。示教-重复（T&R）导航通过避免持续全局建图的需求，提供了一种可靠且经济高效的解决方案；然而，现有T&R系统缺乏系统性方案来应对天气退化、瞬时动态变化及结构变更等多种环境变化。本文提出LTR$^2$——首个跨模态、跨平台的激光雷达-示教-雷达-重复系统，系统性地解决了上述挑战。LTR$^2$在示教阶段利用激光雷达捕获正常条件下的精确结构信息，在重复阶段采用4D毫米波雷达实现环境退化下的稳健运行。为将稀疏且含噪的前视4D雷达数据与密集精确的全向3D激光雷达数据对齐，我们引入跨模态配准（CMR）网络，该网络联合利用基于多普勒的运动先验以及激光雷达强度与雷达功率密度的物理规律。此外，我们提出一种自适应微调策略，基于定位误差增量更新CMR网络，无需真值标签即可实现长期适应静态环境变化。实验表明，所提出的CMR网络在公开数据集上达到了跨模态配准的最优性能。随后，我们在三个机器人平台上对LTR$^2$进行了大规模长期部署验证（6个月内累计行驶40余公里），涵盖夜间烟雾等挑战性条件。实验结果与消融研究证明，该系统在厘米级精度下对多种环境干扰具有强鲁棒性，显著优于现有方法。

---

### 3. DynoSLAM: Dynamic SLAM with Generative Graph Neural Networks for Real-World Social Navigation

- **作者**: Danil Tokhchukov, Veronika Morozova, Gonzalo Ferrer
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.02759v1)
- **发表日期**: 2026-05-04
- **匹配关键词**: social navigation, localization and mapping, navigation, robot navigation
- **arXiv**: [2605.02759v1](http://arxiv.org/abs/2605.02759v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 传统的同步定位与地图构建（SLAM）算法严重依赖静态环境假设，这极大限制了其在存在行人等移动实体的真实空间中的适用性。本文提出DynoSLAM——一种紧耦合的动态图SLAM架构，该架构将具有社会感知能力的图神经网络（GNN）直接集成到因子图优化中。与采用刚性匀速启发式规则或确定性单智能体神经先验的传统方法不同，我们的框架将行人运动预测建模为随机世界模型。通过利用训练好的GNN进行蒙特卡洛展开，我们捕捉人类交互的多模态认知不确定性，并通过动态马氏距离因子将其嵌入SLAM图。通过大量仿真实验证明，这种随机公式不仅能保持高精度的回溯跟踪，还能避免由确定性"argmax问题"导致的优化失败。最终，提取未来行人状态的经验均值和协方差矩阵，为下游局部规划器提供了数学严谨的概率安全包络，使机器人能够在密集拥挤环境中实现具有预见性且无碰撞的自主导航。

---

### 4. AnchorD: Metric Grounding of Monocular Depth Using Factor Graphs

- **作者**: Simon Dorer, Martin Büchner, Nick Heppert, Abhinav Valada
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.02667v1)
- **发表日期**: 2026-05-04
- **匹配关键词**: navigation
- **arXiv**: [2605.02667v1](http://arxiv.org/abs/2605.02667v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: CODE
- **中文摘要**: 密集且精确的深度估计对于机器人操作、抓取和导航至关重要，然而当前可用的深度传感器在透明、镜面及一般非朗伯表面上容易产生误差。为缓解这些误差，大规模单目深度估计方法提供了强大的结构先验，但其预测结果在公制单位下可能存在偏差或尺度错误，限制了其在机器人领域的直接应用。因此，本文提出一种无需训练的深度锚定框架，通过因子图优化将深度基础模型中的单目深度估计先验锚定到原始传感器深度上。该方法采用分块仿射对齐，在保留细粒度几何结构与不连续性的同时，将单目预测局部锚定到公制真实世界深度中。为促进在挑战性真实场景下的评估，我们引入了一个基准数据集，其中包含非朗伯物体场景下密集的全场景真实深度。该真实深度通过哑光反射喷雾与多相机融合获得，克服了以往数据集仅依赖基于CAD的物体标注的局限性。跨多种传感器与领域的广泛评估表明，该方法无需任何（重新）训练即可持续提升深度性能。我们已在https://anchord.cs.uni-freiburg.de公开实现代码。

---

### 5. A Semantic Autonomy Framework for VLM-Integrated Indoor Mobile Robots: Hybrid Deterministic Reasoning and Cross-Robot Adaptive Memory

- **作者**: Bogdan Felician Abaza, Andrei-Alexandru Staicu, Cristian Vasile Doicin
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.02525v1)
- **发表日期**: 2026-05-04
- **匹配关键词**: navigation
- **arXiv**: [2605.02525v1](http://arxiv.org/abs/2605.02525v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 自主室内移动机器人能够利用ROS 2 Navigation 2等成熟框架可靠地导航至度量坐标，但缺乏解读表达意图而非位置的自然语言指令的能力。视觉-语言模型提供了弥合这一差距所需的语义推理能力，但其推理延迟（在消费级硬件上每次决策需2-9秒）和逐会话遗忘问题限制了实际部署。本文提出语义自主栈——一个面向语义自主室内导航的六层参考框架，并在搭载现成边缘硬件的实体机器人上验证了包含混合确定性-VLM推理与跨机器人自适应记忆的完整实例。七步参数解析器可在不调用语言模型、摄像头或GPU的情况下，于0.1毫秒内处理88%的指令；仅真正存在歧义的指令才会升级至VLM推理。具有显式范围分类法（全局环境知识、操作员偏好、机器人能力）的五类语义记忆框架实现了跨会话学习与跨机器人知识迁移：通过VLM交互在单台机器人上习得的偏好被提升为确定性解析，并通过共享编译摘要迁移至第二台机器人，实测延迟降低103,000倍。在两台定制差分驱动机器人上进行的82项场景级决策与三轮会话实验验证表明：语义迁移准确率达100%（33/33，95%置信区间[0.894, 1.000]），语义解析准确率100%，且具备多机器人并发操作可行性——所有功能均在无板载GPU的树莓派5平台上实现，无需任何训练数据。

---

### 6. Visibility-Aware Mobile Grasping in Dynamic Environments

- **作者**: Tianrun Hu, Anxing Xiao, David Hsu, Hanbo Zhang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.02487v1)
- **发表日期**: 2026-05-04
- **匹配关键词**: mobile manipulator, active perception, exploration
- **arXiv**: [2605.02487v1](http://arxiv.org/abs/2605.02487v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 本文研究了机器人在动态未知环境中、视野受限条件下进行移动抓取的问题。核心挑战在于：在满足可见性约束的高维构型空间中，机器人需要在“环顾四周”以降低环境不确定性与“移动身体”以推进任务进程之间做出固有权衡。现有方法通常假设环境已知或静态，并将这两个目标解耦处理，导致当未观测到的动态障碍物在操作过程中与机器人路径相交时，无法保证安全性。本文提出了一种统一的移动抓取系统，包含两个核心组件：（1）迭代式低层全身规划器，结合速度感知主动感知机制，实现动态环境的安全导航；（2）基于行为树的分层高层规划器，通过自适应生成子目标引导机器人进行探索并应对运行时故障。我们在400个随机仿真场景及Fetch移动操作平台的实际部署中进行了实验验证。结果表明，该系统在未知静态和动态环境中的成功率分别达到68.8%和58.0%，相比\nam方法，在两类未知环境中成功率分别提升22.8%和18.0%，同时碰撞安全性得到显著改善。

---

### 7. Feedback Motion Planning for Stochastic Nonlinear Systems with Signal Temporal Logic Specifications

- **作者**: Liqian Ma, Zishun Liu, Glen Chou, Yongxin Chen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.02361v1)
- **发表日期**: 2026-05-04
- **匹配关键词**: motion planning
- **arXiv**: [2605.02361v1](http://arxiv.org/abs/2605.02361v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 本文研究了信号时序逻辑（STL）规范下连续时间随机非线性系统的反馈运动规划问题。我们提出了一种框架，用于合成机会约束STL轨迹优化问题的控制策略，其目标是确保闭环随机系统以高概率（例如99.99%）满足给定的STL公式。该方法基于谓词侵蚀策略，将难以处理的随机问题转化为具有收紧STL公式约束的确定性STL轨迹优化问题。侵蚀量由概率可达管（PRT）决定，该管界定了随机轨迹与相关标称轨迹之间的偏差。为计算此类边界，我们利用收缩理论与反馈设计，开发了多种跟踪控制器。由此形成了一套完整的反馈运动规划流程，可通过数值优化实现。通过在多个机器人系统上的仿真实验以及真实四足机器人的实际测试，我们验证了所提框架的有效性与通用性，结果表明该方法相比代表性基线方法具有更低的保守性，并能实现更高的规范满足概率。

---

### 8. ShapeGrasp: Simultaneous Visuo-Haptic Shape Completion and Grasping for Improved Robot Manipulation

- **作者**: Lukas Rustler, Matej Hoffmann
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.02347v1)
- **发表日期**: 2026-05-04
- **匹配关键词**: grasp planning
- **arXiv**: [2605.02347v1](http://arxiv.org/abs/2605.02347v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 人类通过结合初始视觉估计与交互过程中的触觉和本体感觉反馈来抓取陌生物体。我们提出ShapeGrasp方法，实现了这一策略的机器人化。该方法构建了迭代式抓取与补全流程，将隐式表面的视觉-触觉形状补全（从部分信息生成完整3D形状）与基于物理的抓取规划相结合。通过单张RGB-D图像，ShapeGrasp推断出完整形状（点云或三角网格），经刚体仿真生成候选抓取方案，并执行最优可行抓取。每次抓取尝试都会产生额外的几何约束——触觉表面接触点及夹爪占据空间——这些信息被融合以更新物体形状。若抓取失败，则利用修正后的形状重新估计位姿并执行二次抓取。我们在真实环境中使用两种不同机器人与夹爪进行验证。据我们所知，这是首个在真实抓取后更新形状表征的方法。在两种夹爪测试中（三指夹爪抓取成功率84%，两指夹爪91%），本方法均优于基线方案，同时所有评估指标下的3D形状重建质量均得到提升。

---

### 9. Do We Really Need Immediate Resets? Rethinking Collision Handling for Efficient Robot Navigation

- **作者**: Shanze Wang, Xinming Zhang, Siwei Cheng, Xianghui Wang, Hailong Huang, Wei Zhang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.02192v1)
- **发表日期**: 2026-05-04
- **匹配关键词**: exploration, navigation, robot navigation
- **arXiv**: [2605.02192v1](http://arxiv.org/abs/2605.02192v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 一次碰撞是否必然导致整个导航回合终止？在大多数用于机器人导航的深度强化学习（DRL）框架中，这仍是标准做法：每次碰撞都会立即触发全局环境重置，并作为完整的任务失败受到惩罚。尽管部署过程中的碰撞自然意味着任务失败，但在训练期间采用相同处理方式会阻碍智能体探索具有挑战性的障碍物配置，从而减缓早期训练阶段的学习进度。本研究挑战了这一惯例，提出了一种多碰撞重置预算（MCB）框架，该框架将局部碰撞终止与全局环境重置解耦，允许智能体在同一回合内重试困难配置。在多个模拟和真实机器人平台上的实验表明，该框架加速了早期探索，并在成功率和导航效率上均优于传统的单次碰撞重置基线，其中较小的碰撞预算带来了最大的性能提升。

---

### 10. Sampling-Based Control via Entropy-Regularized Optimal Transport

- **作者**: Vincent Pacelli, Akash Ratheesh, Evangelos A. Theodorou
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.02147v1)
- **发表日期**: 2026-05-04
- **匹配关键词**: navigation
- **arXiv**: [2605.02147v1](http://arxiv.org/abs/2605.02147v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 基于采样的模型预测控制方法（如MPPI和CEM）对于非线性机器人系统的实时控制至关重要，尤其在非连续动力学导致无法使用基于梯度的优化方法时。然而，这些方法源于信息论目标函数，忽略了控制问题的几何结构，导致在代价函数复杂时出现模式平均等病态行为。我们提出OT-MPC——一种基于采样的算法，通过熵正则化的最优传输公式克服了这些局限。通过计算候选控制序列与低成本提议之间的最优耦合，OT-MPC将候选解向邻近有前景的样本优化，同时协调整体更新以保持解空间的覆盖性。我们利用Sinkhorn算法推导出闭式、无梯度的更新公式，实现了实时性能。在导航、操作和运动任务上的实验表明，该方法相比现有方法具有更高的成功率。

---

### 11. Robotic Desk Organization: A Multi-Primitive Approach to Manipulating Heterogeneous Objects via Environmental Constraints

- **作者**: Yi Dong. Yangjun Liu, Jinjun Duan, Yang Li, Zhendong Dai
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.02135v1)
- **发表日期**: 2026-05-04
- **匹配关键词**: object manipulation
- **arXiv**: [2605.02135v1](http://arxiv.org/abs/2605.02135v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 桌面整理对服务机器人而言仍具挑战性，原因在于物体种类多样且操作目标各异（如收集与堆叠）。本文提出了一种面向任务的框架，用于整理桌面上的平面刚性与可变形物体。我们开发了一套感知流程，通过引入非常规桌面物品扩充现有数据集，实现基于几何的位姿与关键点估计，同时检测桌面边缘等环境约束。为应对多样化操作需求，研究采用了环境辅助基元：基于接触抓取的小物体操作、基于边缘推抓的平面刚性物体操作，以及基于杠杆原理的平面可变形物体抓取。这些基元利用环境约束与物体间约束提升鲁棒性。我们设计了任务规划器，将这些基元整合至多物体整理流程中。充分的真实世界实验验证了该框架的有效性与鲁棒性。本研究为平面刚性与可变形物体提供了实用操作基元，凸显了环境约束与物体间约束在复杂多物体操作任务中的关键作用。相关代码与视频已在线公开。

---

