# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-05-07 08:03

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 4/20 篇提供

**🌟 Highlight**: 8 篇 | **📌 Poster**: 12 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. BifrostUMI: Bridging Robot-Free Demonstrations and Humanoid Whole-Body Manipulation

- **作者**: Chenhao Yu, Hongwu Wang, Youhao Hu, Jiachen Zhang, Yuanyuan Li, Shaqi Luo
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.03452v1)
- **发表日期**: 2026-05-05
- **匹配关键词**: whole-body manipulation
- **arXiv**: [2605.03452v1](http://arxiv.org/abs/2605.03452v1)
- **📥 PDF**: 已下载至本地 (`2605.03452v1_BifrostUMI_Bridging_Robot-Free_Demonstrations_and_Humanoid_Whole-Body_Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 高质量数据采集是训练人形全身视觉运动策略的基础基石。当前的数据采集范式主要依赖机器人遥操作，但常受限于硬件可及性有限和操作效率低下的问题。受通用操控接口（UMI）启发，我们提出BifrostUMI——一种专为人形机器人设计的便携、高效且无需机器人的数据采集框架。BifrostUMI利用轻量级VR设备将人类演示捕捉为稀疏关键点轨迹，同时记录腕部视觉数据。这些多模态数据随后用于训练高层策略网络，该网络基于捕获的视觉特征预测未来关键点轨迹。通过稳健的关键点重定向流程，关键点轨迹被精确映射至机器人形态，并通过全身控制器执行。该方法实现了从自然人类演示到人形机器人本体的多样化敏捷行为无缝迁移。我们在两个不同实验场景中验证了所提框架的有效性与通用性。

---

### 2. RLDX-1 Technical Report

- **作者**: Dongyoung Kim, Huiwon Jang, Myungkyu Koo, Suhyeok Jang, Taeyoung Kim, Beomjun Kim, Byungjun Yoon, Changsung Jang, Daewon Choi, Dongsu Han, Donguk Lee, Heeseung Kwon, Hojin Jeon, Jaehyun Kang, Jaekyoung Bae, Jihyuk Lee, Jimin Lee, John Won, Joonwoo Ahn, Junhyeong Park, Junyoung Sung, Kyungmin Lee, Minseong Han, Minsung Yoon, Sejune Joo, Seonil Son, Seungcheol Park, Seunggeun Cho, Seungjun Moon, Seungku Kim, Yonghoon Dong, Yongjin Cho, Youngchan Kim, Chang Hwan Kim, Dohyeon Kim, Hazel Lee, Heecheol Kim, Hensen Ahn, Hyungkyu Ryu, Hyunsoo Choi, Hyunsoo Shin, Jaeheon Jung, Jaewoo Kim, Jinwook Kim, Joochul Chang, Joonsoo Kim, Junghun Park, Jungwoo Park, Junho Cho, Junhyeok Park, Junwon Lee, Kangwook Lee, Kwanghoon Kim, Kyoungwhan Choe, Manoj Bhadu, Nayoung Oh, Sangjun Kim, Sangwoo Kim, Seunghoon Shim, Seunghyun Kim, Seungjun Lee, Seungyup Ka, Sungryol Yang, Wook Jung, Yashu Shukla, Yeonjae Lee, Yeonwoo Bae, Jinwoo Shin
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.03269v1)
- **发表日期**: 2026-05-05
- **匹配关键词**: vision-language-action model, vision-language-action, VLA
- **arXiv**: [2605.03269v1](http://arxiv.org/abs/2605.03269v1)
- **📥 PDF**: 已下载至本地 (`2605.03269v1_RLDX-1_Technical_Report.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 尽管视觉-语言-动作模型（VLAs）凭借从预训练视觉-语言模型中继承的通用智能（即广泛的场景理解与语言条件泛化能力），在实现类人通用机器人策略方面取得了显著进展，但在需要更广泛功能能力（如运动感知、记忆感知决策及物理传感）的复杂现实任务中仍存在不足。为此，我们提出RLDX-1——一种基于多流动作变换器（MSAT）的通用灵巧操作机器人策略。该架构通过模态特定流与跨模态联合自注意力机制整合异构模态，统一了上述功能。RLDX-1进一步将该架构与系统级设计选择相结合，包括为罕见操作场景合成训练数据、针对类人操作特化的学习流程，以及面向实时部署的推理优化。通过实证评估，我们证明RLDX-1在模拟基准测试和需要超越通用能力的广泛功能能力的现实任务中，均持续优于近期前沿VLAs（如π₀.₅和GR00T N1.6）。特别地，RLDX-1在ALLEX人形机器人任务中展现出显著优势，成功率达86.8%，而π₀.₅和GR00T N1.6仅达约40%，凸显了RLDX-1在多样化功能需求下控制高自由度人形机器人的能力。这些结果共同表明，RLDX-1是迈向可靠VLAs以应对复杂、高接触、动态现实世界灵巧操作任务的重要一步。

---

### 3. MolmoAct2: Action Reasoning Models for Real-world Deployment

- **作者**: Haoquan Fang, Jiafei Duan, Donovan Clay, Sam Wang, Shuo Liu, Weikai Huang, Xiang Fan, Wei-Chuan Tsai, Shirui Chen, Yi Ru Wang, Shanli Xing, Jaemin Cho, Jae Sung Park, Ainaz Eftekhar, Peter Sushko, Karen Farley, Angad Wadhwa, Cole Harrison, Winson Han, Ying-Chun Lee, Eli VanderBilt, Rose Hendrix, Suveen Ellawela, Lucas Ngoo, Joyce Chai, Zhongzheng Ren, Ali Farhadi, Dieter Fox, Ranjay Krishna
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.02881v1)
- **发表日期**: 2026-05-04
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2605.02881v1](http://arxiv.org/abs/2605.02881v1)
- **📥 PDF**: 已下载至本地 (`2605.02881v1_MolmoAct2_Action_Reasoning_Models_for_Real-world_Deployment.pdf`)
- **🔓 开源**: MODEL, PROJECT_PAGE
- **中文摘要**: 视觉-语言-动作（VLA）模型旨在为机器人提供单一通用控制器，但当前系统在实际部署的关键标准上仍存在不足。前沿模型封闭，开源替代方案受限于昂贵硬件，增强推理策略因接地性而面临高昂延迟，微调后的成功率仍低于可靠使用的阈值。我们提出MolmoAct2，一个为实际部署构建的完全开源动作推理模型，沿五个维度对其前身进行了改进。我们引入MolmoER，一个专为空间和具身推理设计的VLM骨干网络，采用“先专精后演练”的方法在330万样本语料库上训练。我们发布了三个覆盖中低端平台的新数据集，包括MolmoAct2-BimanualYAM——包含720小时遥操作双臂轨迹，是迄今为止最大的开源双臂数据集，以及经过质量筛选的Franka（DROID）和SO100/101子集。我们提供OpenFAST，一个开源权重、开源数据的动作分词器，在五个具身形态的数百万条轨迹上训练。我们重新设计了架构，通过逐层KV缓存条件将流匹配连续动作专家嫁接至离散分词VLM。最后，我们提出MolmoThink，一种自适应深度推理变体，仅对时间步间变化的场景区域重新预测深度标记，以先前延迟的一小部分保留几何接地性。在迄今为止任何开源VLA最广泛的实证研究中（涵盖7个模拟和真实世界基准），MolmoAct2优于包括Pi-05在内的强基线，而MolmoER在13个具身推理基准上超越GPT-5和Gemini Robotics ER-1.5。我们发布模型权重、训练代码和完整训练数据。项目页面：https://allenai.org/blog/molmoact2

---

### 4. Seeing Realism from Simulation: Efficient Video Transfer for Vision-Language-Action Data Augmentation

- **作者**: Chenyu Hui, Xiaodi Huang, Siyu Xu, Yunke Wang, Shan You, Fei Wang, Tao Huang, Chang Xu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.02757v1)
- **发表日期**: 2026-05-04
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2605.02757v1](http://arxiv.org/abs/2605.02757v1)
- **📥 PDF**: 已下载至本地 (`2605.02757v1_Seeing_Realism_from_Simulation_Efficient_Video_Transfer_for_Vision-Language-Action_Data_Augmentation.pdf`)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/nanfangxiansheng/Seeing-Realism-from-Simulation.
- **中文摘要**: 视觉-语言-动作（VLA）模型通常依赖大规模真实世界视频，而仿真数据尽管采集成本低廉且易于并行化，却常因显著的视觉域差异和有限的环境多样性导致真实世界泛化能力薄弱。我们提出一种高效视频增强框架，可将仿真VLA视频转化为逼真的训练视频，同时保留任务语义与动作轨迹。该流程通过视频语义分割与视频描述技术从仿真中提取结构化条件，重写描述以丰富环境多样性，并利用条件视频迁移模型合成真实感视频。为提升增强的规模化实用性，我们引入扩散特征复用机制，通过跨相邻时间步复用视频令牌加速生成，并设计核心集采样策略，在有限计算资源下识别紧凑无冗余子集进行增强。在Robotwin 2.0、LIBERO、LIBERO-Plus及真实机器人平台上的大量实验表明，该方法持续提升性能。例如，该方法使RDT-1B在Robotwin 2.0上提升8%，并在更具挑战性的LIBERO-Plus基准测试中将$π_0$提升5.1%。代码已开源：https://github.com/nanfangxiansheng/Seeing-Realism-from-Simulation。

---

### 5. Latent Bridge: Feature Delta Prediction for Efficient Dual-System Vision-Language-Action Model Inference

- **作者**: Yudong Liu, Yuan Li, Zijia Tang, Yuxi Zheng, Yueqian Lin, Qinsi Wang, Yi Li, Shuangjun Liu, Shuai Zhang, Taotao Jing, Dashan Gao, Ning Bi, Jingwei Sun, Yiran Chen, Hai Li
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.02739v1)
- **发表日期**: 2026-05-04
- **匹配关键词**: vision-language-action model, vision-language-action, VLA
- **arXiv**: [2605.02739v1](http://arxiv.org/abs/2605.02739v1)
- **📥 PDF**: 已下载至本地 (`2605.02739v1_Latent_Bridge_Feature_Delta_Prediction_for_Efficient_Dual-System_Vision-Language-Action_Model_Infere.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 双系统视觉-语言-动作（VLA）模型在机器人操作任务中达到了最先进的性能，但其性能受限于视觉-语言模型（VLM）主干网络——该网络必须在每个控制步骤执行运算，同时产生时间冗余特征。我们提出潜在桥接（Latent Bridge）这一轻量级模型，用于预测不同时间步之间VLM输出的变化量，使得动作头能够基于预测输出运行，而昂贵的VLM主干网络仅需周期性调用。我们在两种架构不同的VLA模型上实例化了潜在桥接：GR00T-N1.6（特征空间桥接）和π0.5（KV缓存桥接），证明了该方法可泛化至不同VLA设计。我们提出的任务无关型DAgger训练流程无需修改即可跨基准测试迁移。在四个LIBERO任务套件、24个RoboCasa厨房任务以及ALOHA模拟传输立方体任务中，潜在桥接在将VLM调用次数减少50-75%的同时保持了95-100%的性能保留率，实现了每轮1.65-1.73倍的净加速比。

---

### 6. CoRAL: Contact-Rich Adaptive LLM-based Control for Robotic Manipulation

- **作者**: Berk Çiçek, Mert K. Er, Özgür S. Öğüz
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.02600v1)
- **发表日期**: 2026-05-04
- **匹配关键词**: contact-rich manipulation, VLA
- **arXiv**: [2605.02600v1](http://arxiv.org/abs/2605.02600v1)
- **📥 PDF**: 已下载至本地 (`2605.02600v1_CoRAL_Contact-Rich_Adaptive_LLM-based_Control_for_Robotic_Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 尽管大型语言模型（LLMs）和视觉语言模型（VLMs）在高层次推理与语义理解方面展现出卓越能力，但由于缺乏显式的物理基础且无法执行自适应控制，将其直接应用于接触丰富的操控任务仍面临挑战。为弥合这一差距，我们提出CoRAL（基于LLM的自适应接触丰富控制）模块化框架，通过将高层推理与低层控制解耦实现零样本规划。与黑箱策略不同，CoRAL并非将LLM作为直接控制器，而是将其作为成本函数设计器，为基于采样的运动规划器（MPPI）合成具有上下文感知的目标函数。针对视觉数据中物理参数的模糊性问题，我们引入神经符号自适应循环：视觉语言模型为环境动力学（如质量与摩擦系数估计）提供语义先验，这些参数通过在线系统辨识实时显式优化，同时LLM基于交互反馈迭代调整成本函数结构以修正策略性错误。此外，基于检索的记忆单元使系统能在重复任务中复用成功策略。这种分层架构通过将高层语义推理与反应式执行解耦，确保实时控制稳定性，有效弥合了LLM慢速推理与动态接触需求之间的鸿沟。我们在仿真与真实硬件上对CoRAL进行了验证，涵盖利用外部接触实现靠墙翻转物体等新颖挑战性任务。实验表明，在未见过的接触丰富场景中，CoRAL通过自适应物理理解能力有效处理仿真到现实迁移问题，平均成功率较现有最先进的VLA及基础模型规划器基线提升超过50%。

---

### 7. Natural Gradient Bayesian Filtering: Geometry-Aware Filter for Dynamical Systems

- **作者**: Chang Liu, Wenhan Cao, Zeju Sun, Tianyi Zhang, Jiayu Yuan, Yi Zeng, Ting Yuan, Yao Lyu, Wei Wu, Stephen Shing-Toung Yau, Shengbo Eben Li
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.02306v1)
- **发表日期**: 2026-05-04
- **匹配关键词**: localization and mapping
- **arXiv**: [2605.02306v1](http://arxiv.org/abs/2605.02306v1)
- **📥 PDF**: 已下载至本地 (`2605.02306v1_Natural_Gradient_Bayesian_Filtering_Geometry-Aware_Filter_for_Dynamical_Systems.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 贝叶斯滤波是航空航天系统等复杂系统中状态估计的基石，但其精确解仅适用于线性高斯模型。在实际应用中，非线性系统通过可处理的近似方法进行处理，其中扩展卡尔曼滤波和无迹卡尔曼滤波等高斯滤波器是最广泛使用的方法之一。本教程从信息几何的视角重新审视高斯滤波，将预测和测量更新步骤视为状态分布上的推断过程。在此框架下，我们引入了一种几何感知的高斯滤波方法，该方法利用高斯分布统计流形上的自然梯度下降。由此产生的自然梯度高斯近似（NANO）滤波器迭代优化后验均值和协方差，同时尊重高斯族的内在几何结构并保持协方差矩阵的正定性。我们进一步揭示了与经典卡尔曼滤波的基本联系，表明在线性高斯情况下，单步自然梯度更新可精确恢复卡尔曼测量更新。通过代表性非线性估计问题的案例研究（包括卫星姿态估计、同步定位与地图构建，以及四足机器人和人形机器人等机器人系统的状态估计），展示了所提出框架的实际意义。

---

### 8. Change-Robust Online Spatial-Semantic Topological Mapping

- **作者**: Jiaming Wang, Jizhuo Chen, Diwen Liu, Atharva Ghotavadekar, Jiaxuan Da, Linh Kästner, Harold Soh
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.02227v1)
- **发表日期**: 2026-05-04
- **匹配关键词**: object-goal navigation, navigation
- **arXiv**: [2605.02227v1](http://arxiv.org/abs/2605.02227v1)
- **📥 PDF**: 已下载至本地 (`2605.02227v1_Change-Robust_Online_Spatial-Semantic_Topological_Mapping.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 自主机器人需要具备应对环境变化的鲁棒空间-语义推理能力：即利用空间与语义知识，在环境变化的情况下决定去向何处、如何抵达，以及确定自身位置。现有方法通常将语义信息附加到基于SLAM构建的度量地图上，但这些流程在视觉外观变化和场景动态下表现脆弱，导致数据关联与重定位性能下降。我们提出一种抗变化鲁棒的在线空间-语义（CROSS）表示方法，该方法用基于RGB-D关键帧的在线位姿感知拓扑图替代全局一致的度量基底。系统通过连续SE(3)空间中的序贯假设检验，显式处理感知模糊性。我们的估计器维持对位姿的有界高斯混合置信度，从而能够原则性地处理闭环检测与机器人绑架事件。在剧烈外观变化（包括真实机器人目标导向导航中光照变化与家具重排）的实验表明，该方法相比基于SLAM和拓扑的基线方法展现出更强的鲁棒性，同时在感知混淆场景下仍能保持安全性。

---

## 📌 Poster

*其他相关研究*

---

### 1. StateVLM: A State-Aware Vision-Language Model for Robotic Affordance Reasoning

- **作者**: Xiaowen Sun, Matthias Kerzel, Mengdi Li, Xufeng Zhao, Paul Striker, Stefan Wermter
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.03927v1)
- **发表日期**: 2026-05-05
- **匹配关键词**: affordance
- **arXiv**: [2605.03927v1](http://arxiv.org/abs/2605.03927v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: CODE
- **中文摘要**: 视觉-语言模型（VLMs）在各类机器人任务中展现出卓越性能，因其既能感知视觉信息，又能理解自然语言指令。然而，当应用于机器人领域时，VLMs仍受限于大语言模型（LLMs）固有的根本性缺陷：它们在数值推理方面存在困难，尤其是在目标检测和目标状态定位任务中。为探究VLMs中作为回归任务的数值推理问题，我们提出了一种新颖的训练策略，使VLMs适应目标检测与目标状态定位任务。该方法在微调阶段利用边界框解码器输出计算辅助回归损失（ARL），同时在推理阶段保持标准序列预测。基于此训练策略，我们开发了StateVLM（状态感知视觉-语言模型），该模型能够感知并学习细粒度目标表征，包括目标及其状态的精确定位，以及可抓取区域。针对当前缺乏目标状态可供性推理基准的问题，我们推出了开源基准数据集OSAR（目标状态可供性推理），包含1,172个场景、7,746个独立目标及其对应边界框。在适配基准（RefCOCO、RefCOCO+和RefCOCOg）上的对比实验表明，相较于未使用ARL的模型，ARL使模型性能平均提升1.6%。OSAR基准上的实验进一步验证了这一发现：采用ARL的StateVLM相比未使用ARL的模型，性能平均提升5.2%。特别值得注意的是，ARL对于OSAR中复杂的可供性推理任务同样至关重要，它能增强模型输出的一致性。

---

### 2. SigLoMa: Learning Open-World Quadrupedal Loco-Manipulation from Ego-Centric Vision

- **作者**: Shiyi Chen, Haiyi Liu, Mingye Yang, Jiaqi Zhang, Debing Zhang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.03846v1)
- **发表日期**: 2026-05-05
- **匹配关键词**: visual tracking
- **arXiv**: [2605.03846v1](http://arxiv.org/abs/2605.03846v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 设计一个开放世界的四足机器人移动操作系统极具挑战性。传统依赖外部感知的强化学习框架常面临样本效率极低和仿真到现实迁移差距巨大的问题。此外，视觉追踪固有的延迟与高精度浮动基座控制所需的高频响应存在根本性矛盾。因此，现有系统严重依赖昂贵的外部动作捕捉和机外计算。为消除这些依赖，我们提出SigLoMa——一种完全机载、以自我为中心的视觉抓取与放置框架。其核心创新是引入Sigma Points，这是一种轻量级几何感知表征，能确保高可扩展性与原生仿真到现实对齐。为弥合慢速感知与快速控制之间的频率鸿沟，我们设计了以自我为中心的卡尔曼滤波器，提供鲁棒的高频状态估计。在学习方面，我们通过基于提示姿态的主动采样课程缓解样本效率问题，并利用时序编码结合模拟随机游走漂移解决机器人结构视觉盲区。真实世界实验表明，仅依赖5Hz（200毫秒延迟）的开放词汇检测器，SigLoMa即可成功执行多任务动态移动操作，性能媲美专家级人类遥操作。

---

### 3. Feasibility-aware Hybrid Control for Motion Planning under Signal Temporal Logics

- **作者**: Panagiotis Rousseas, Dimos V. Dimarogonas
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.03662v1)
- **发表日期**: 2026-05-05
- **匹配关键词**: motion planning
- **arXiv**: [2605.03662v1](http://arxiv.org/abs/2605.03662v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 本文提出了一种基于混合建模的平面任务与运动规划新方法。通过引入一个离散变量来建模局部约束满足性并实现局部可行性分析，所提出的控制架构将规划与控制设计相统一。同时，在原始非凸且几何结构复杂的机器人工作空间的变换圆盘版本上设计控制障碍函数，从而修正了死锁问题。仿真结果表明，即使在输入饱和的情况下，该方法也能有效处理多个重叠的时空任务。

---

### 4. Uncertainty Estimation in Instance Segmentation of Affordances via Bayesian Visual Transformers

- **作者**: Lorenzo Mur-Labadia, Ruben Martinez-Cantina, Jose J. Guerrero
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.03614v1)
- **发表日期**: 2026-05-05
- **匹配关键词**: human-robot interaction, affordance
- **arXiv**: [2605.03614v1](http://arxiv.org/abs/2605.03614v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 视觉可供性识别图像中具有潜在交互行为的区域，为场景理解提供了全新范式。对可供性的识别能使自主机器人行为更自然，增强人机交互体验，丰富增强现实系统，并有益于假体视觉设备。对于这些应用而言，对可供性区域进行精确且局部的预测（而非生成通用显著性图）至关重要。我们提出了一种基于样本和集成方法进行不确定性估计的可供性实例分割模型。针对这一新任务，我们扩展了基于注意力机制的架构，并通过详细的消融实验展示了各组件的作用。通过比较不同检测结果的分布，我们在语义和空间层面提取了像素级认知不确定性与偶然不确定性。此外，我们提出了一种名为"概率掩膜质量"的新型度量指标，能够对概率性实例分割模型中的语义与空间变化进行综合分析。实验结果表明，贝叶斯模型多子网络的全局共识通过更优的掩膜细化与泛化能力提升了确定性网络性能。这一特性与注意力机制提取的更强特征相结合，在具有挑战性的IIT-Aff数据集上实现了$F_β^w$评分提升7.4个百分点。贝叶斯模型还展现出更好的校准性能，产生更少过度自信的概率估计，并具有更优的不确定性评估。定性结果显示，偶然不确定性主要出现在物体轮廓区域，而认知不确定性则集中于视觉上具有挑战性的像素点，这为神经网络增添了可解释性。

---

### 5. Semantic Risk-Aware Heuristic Planning for Robotic Navigation in Dynamic Environments: An LLM-Inspired Approach

- **作者**: Hamza Ahmed Durrani, Rafay Suleman Durrani
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.02862v1)
- **发表日期**: 2026-05-04
- **匹配关键词**: path planning, robot navigation, navigation
- **arXiv**: [2605.02862v1](http://arxiv.org/abs/2605.02862v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 将大语言模型推理原理与经典机器人路径规划相结合，是当前快速发展的研究方向。本文提出了一种语义风险感知启发式（SRAH）规划器，将受大语言模型启发的代价函数（惩罚几何拥挤或高风险区域）编码到A$^*$搜索框架中，并辅以动态障碍物检测时的闭环重规划。我们在一个静态障碍物密度为20%、存在随机动态障碍物的$15{\times}15$网格世界中，通过200次随机试验，将SRAH与两种基线方法——带重规划的广度优先搜索（BFS）和不带重规划的贪婪启发式算法——进行了对比评估。SRAH的任务成功率达到62.0%，相比BFS（56.5%）相对提升9.7%，并大幅优于贪婪算法（4.0%）。我们进一步分析了规划开销、路径效率与故障恢复次数之间的权衡，并通过障碍物密度消融实验证明，语义代价整形能在不同难度环境中持续改善导航性能。研究结果表明，即使是轻量级的、受大语言模型启发的启发式方法，也能为自主机器人导航带来显著的安全性与鲁棒性提升。

---

### 6. LiDAR Teach, Radar Repeat: Robust Cross-Modal Navigation in Degenerate and Varying Environments

- **作者**: Renxiang Xiao, Yichen Chen, Yuanfan Zhang, Qianyi Shao, Yushuai Chen, Yuxuan Han, Yunjiang Lou, Liang Hu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.02809v1)
- **发表日期**: 2026-05-04
- **匹配关键词**: long-term autonomy, navigation
- **arXiv**: [2605.02809v1](http://arxiv.org/abs/2605.02809v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 长期自主导航要求系统能够在动态与静态变化的环境以及恶劣天气条件下实现稳健运行。示教-重复（T&R）导航通过避免持续全局建图的需求，提供了一种可靠且经济高效的解决方案；然而，现有T&R系统缺乏系统性方案来应对天气退化、瞬时动态变化和结构变更等多种环境变化。本文提出LTR$^2$——首个跨模态、跨平台的激光雷达-示教-雷达-重复系统，系统性地解决了上述挑战。LTR$^2$在示教阶段利用激光雷达捕获正常条件下的精确结构信息，在重复阶段采用4D毫米波雷达实现环境退化下的稳健运行。为将稀疏且含噪的前视4D雷达数据与密集精确的全向3D激光雷达数据对齐，我们引入跨模态配准（CMR）网络，该网络联合利用基于多普勒的运动先验以及激光雷达强度与雷达功率密度的物理规律。此外，我们提出一种自适应微调策略，根据定位误差增量更新CMR网络，无需真值标签即可实现长期适应静态环境变化。实验表明，所提CMR网络在公开数据集上达到跨模态配准的领先性能。随后，我们在三个机器人平台上对LTR$^2$进行大规模长期部署验证（6个月内累计运行40余公里），涵盖夜间烟雾等挑战性条件。实验结果与消融研究显示，该系统在厘米级精度下对多种环境干扰具有强鲁棒性，显著优于现有方法。

---

### 7. DynoSLAM: Dynamic SLAM with Generative Graph Neural Networks for Real-World Social Navigation

- **作者**: Danil Tokhchukov, Veronika Morozova, Gonzalo Ferrer
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.02759v1)
- **发表日期**: 2026-05-04
- **匹配关键词**: social navigation, robot navigation, localization and mapping, navigation
- **arXiv**: [2605.02759v1](http://arxiv.org/abs/2605.02759v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 传统的同步定位与地图构建（SLAM）算法严重依赖静态环境假设，这极大限制了其在存在行人等移动实体的真实空间中的适用性。本文提出DynoSLAM——一种紧耦合的动态图SLAM架构，该架构将具有社交感知能力的图神经网络（GNN）直接集成到因子图优化中。与采用刚性匀速启发式规则或确定性单智能体神经先验的传统方法不同，我们的框架将行人运动预测建模为随机世界模型。通过利用训练好的GNN进行蒙特卡洛展开，我们捕捉人类交互的多模态认知不确定性，并通过动态马氏距离因子将其嵌入SLAM图。大量仿真实验表明，这种随机公式不仅能保持高精度的回溯跟踪，还能避免由确定性"argmax问题"导致的优化失败。最终，提取未来行人状态的经验均值与协方差矩阵，为下游局部规划器提供了数学严谨的概率安全包络，使机器人在密集拥挤环境中能够实现具有预见性且无碰撞的自主导航。

---

### 8. AnchorD: Metric Grounding of Monocular Depth Using Factor Graphs

- **作者**: Simon Dorer, Martin Büchner, Nick Heppert, Abhinav Valada
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.02667v1)
- **发表日期**: 2026-05-04
- **匹配关键词**: navigation
- **arXiv**: [2605.02667v1](http://arxiv.org/abs/2605.02667v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: CODE
- **中文摘要**: 密集且精确的深度估计对于机器人操作、抓取和导航至关重要，然而当前可用的深度传感器在透明、镜面及一般非朗伯表面容易产生误差。为缓解这些误差，大规模单目深度估计方法提供了强大的结构先验，但其预测结果在公制单位下可能存在偏差或尺度错误，限制了其在机器人领域的直接应用。因此，本文提出一种无需训练的深度锚定框架，通过因子图优化将深度基础模型中的单目深度估计先验与原始传感器深度进行对齐。该方法采用分块仿射对齐，在保留精细几何结构与不连续性的同时，将单目预测局部锚定于公制真实世界深度。为促进在复杂真实条件下的评估，我们引入了一个基准数据集，其中包含非朗伯物体场景下的密集全景真实深度。该真实深度通过哑光反射喷雾与多相机融合获取，克服了以往数据集仅依赖基于CAD的物体级标注的局限性。跨多种传感器与领域的广泛评估表明，该方法无需任何（重新）训练即可持续提升深度性能。我们已在https://anchord.cs.uni-freiburg.de公开实现代码。

---

### 9. A Semantic Autonomy Framework for VLM-Integrated Indoor Mobile Robots: Hybrid Deterministic Reasoning and Cross-Robot Adaptive Memory

- **作者**: Bogdan Felician Abaza, Andrei-Alexandru Staicu, Cristian Vasile Doicin
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.02525v1)
- **发表日期**: 2026-05-04
- **匹配关键词**: navigation
- **arXiv**: [2605.02525v1](http://arxiv.org/abs/2605.02525v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 自主室内移动机器人能够利用ROS 2 Navigation 2等成熟框架可靠地导航至度量坐标，但缺乏理解表达意图而非位置的自然语言指令的能力。视觉语言模型提供了弥合这一差距所需的语义推理能力，但其推理延迟（在消费级硬件上每次决策需2-9秒）和逐会话遗忘特性限制了实际部署。本文提出了语义自主栈——一个面向语义自主室内导航的六层参考框架，并在搭载现成边缘硬件的实体机器人上验证了包含混合确定性-VLM推理与跨机器人自适应记忆的完整实例。七步参数解析器可在0.1毫秒内处理88%的指令，无需调用语言模型、摄像头或GPU；仅真正存在歧义的指令才会升级至VLM推理。具有显式范围分类（全局环境知识、操作员偏好、机器人能力）的五类语义记忆框架实现了跨会话学习与跨机器人知识迁移：通过VLM交互在一个机器人上习得的偏好被提升为确定性解析，并通过共享编译摘要迁移至第二个机器人，实测延迟降低103,000倍。在两台定制差速驱动机器人上进行的82项场景级决策与三轮会话实验验证表明：语义迁移准确率达100%（33/33，95%置信区间[0.894, 1.000]），语义解析准确率100%，且支持多机器人并发操作——所有功能均在无板载GPU的树莓派5平台上实现，无需任何训练数据。

---

### 10. Visibility-Aware Mobile Grasping in Dynamic Environments

- **作者**: Tianrun Hu, Anxing Xiao, David Hsu, Hanbo Zhang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.02487v1)
- **发表日期**: 2026-05-04
- **匹配关键词**: mobile manipulator, exploration, active perception
- **arXiv**: [2605.02487v1](http://arxiv.org/abs/2605.02487v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 本文研究了机器人在动态未知环境中受限于有限视场下的移动抓取问题。核心挑战在于：在满足可见性约束的高维构型空间中，机器人需要在“观察”周围环境以降低不确定性，与“移动”身体以推进任务进程之间进行固有权衡。现有方法通常假设环境已知或静态，并将这两个目标解耦，导致当未观测到的动态障碍物在操作过程中与机器人路径相交时，无法保证安全性。本文提出了一种统一的移动抓取系统，包含两个核心组件：（1）一种迭代式低层全身规划器，结合速度感知主动感知机制，实现动态环境的安全导航；（2）一种基于行为树的分层高层规划器，通过自适应生成子目标引导机器人完成探索并应对运行时故障。我们在400个随机仿真场景及Fetch移动操作平台的实际部署中进行了实验验证。结果表明，该系统在未知静态和动态环境中的成功率分别达到68.8%和58.0%，相较于\nam方法，在两类未知环境中成功率分别提升22.8%和18.0%，同时碰撞安全性得到显著改善。

---

### 11. Feedback Motion Planning for Stochastic Nonlinear Systems with Signal Temporal Logic Specifications

- **作者**: Liqian Ma, Zishun Liu, Glen Chou, Yongxin Chen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.02361v1)
- **发表日期**: 2026-05-04
- **匹配关键词**: motion planning
- **arXiv**: [2605.02361v1](http://arxiv.org/abs/2605.02361v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 我们研究了信号时序逻辑（STL）规范下连续时间随机非线性系统的反馈运动规划问题。提出了一种框架，用于合成机会约束STL轨迹优化问题的控制策略，其目标是确保闭环随机系统以高概率（例如99.99%）满足给定的STL公式。该方法基于谓词侵蚀策略，将难以处理的随机问题转化为具有收紧STL公式约束的确定性STL轨迹优化问题。侵蚀量由概率可达管（PRT）决定，该管限定了随机轨迹与关联名义轨迹之间的偏差。为计算此类边界，我们利用收缩理论与反馈设计，开发了多种跟踪控制器。由此形成完整的反馈运动规划流程，可通过数值优化实现。通过在多个机器人系统上的仿真实验以及真实四足机器人的实物实验，我们验证了所提框架的有效性与通用性，结果表明该方法相比代表性基线方法具有更低的保守性，并能实现更高的规范满足概率。

---

### 12. ShapeGrasp: Simultaneous Visuo-Haptic Shape Completion and Grasping for Improved Robot Manipulation

- **作者**: Lukas Rustler, Matej Hoffmann
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.02347v1)
- **发表日期**: 2026-05-04
- **匹配关键词**: grasp planning
- **arXiv**: [2605.02347v1](http://arxiv.org/abs/2605.02347v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 人类通过将初始视觉估计与交互过程中的触觉和本体感觉反馈相结合来抓取不熟悉的物体。我们提出ShapeGrasp方法，这是该策略的机器人实现。该方法构建了一个迭代式抓取与补全流程，将隐式表面的视觉-触觉形状补全（从局部信息生成完整三维形状）与基于物理的抓取规划相结合。通过单张RGB-D图像，ShapeGrasp推断出完整形状（点云或三角网格），经刚体仿真生成候选抓取方案，并执行最优可行抓取。每次抓取尝试都会产生额外的几何约束——触觉表面接触点与夹爪占据空间——这些信息被融合以更新物体形状。抓取失败时，系统利用优化后的形状重新估计位姿并执行二次抓取。我们在真实环境中使用两种不同机器人与夹爪进行验证。据我们所知，这是首个在真实抓取后更新形状表征的方法。两种夹爪均取得优于基准方法的抓取成功率（三指夹爪84%，两指夹爪91%），同时所有评估指标中的三维形状重建质量均得到提升。

---

