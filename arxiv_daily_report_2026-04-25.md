# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-04-25 08:02

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 3/20 篇提供

**🌟 Highlight**: 14 篇 | **📌 Poster**: 6 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. Long-Horizon Manipulation via Trace-Conditioned VLA Planning

- **作者**: Isabella Liu, An-Chieh Cheng, Rui Yan, Geng Chen, Ri-Zhao Qiu, Xueyan Zou, Sha Yi, Hongxu Yin, Xiaolong Wang, Sifei Liu ⭐
  - **高亮作者**: Xiaolong Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.21924v1)
- **发表日期**: 2026-04-23
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2604.21924v1](http://arxiv.org/abs/2604.21924v1)
- **📥 PDF**: 已下载至本地 (`2604.21924v1_Long-Horizon_Manipulation_via_Trace-Conditioned_VLA_Planning.pdf`)
- **🔓 开源**: PROJECT_PAGE
- **中文摘要**: 长时域操作对视觉-语言-动作（VLA）策略仍具挑战性：真实任务具有多步骤、依赖进度且易受复合执行错误影响的特点。我们提出LoHo-Manip模块化框架，通过专用任务管理视觉语言模型（VLM），将短时域VLA执行扩展至遵循长时域指令。该管理器与执行器解耦，并以滚动时域方式被调用：基于当前观测，它预测一个感知进度的剩余计划，该计划结合了（i）具有显式完成+剩余拆分的子任务序列作为轻量级语言记忆，以及（ii）视觉轨迹——一个紧凑的2D关键点轨迹提示，用于指定下一步移动方向和接近目标。执行器VLA通过条件化渲染轨迹进行适配，从而将长时域决策转化为通过跟随轨迹实现的重复局部控制。关键在于，每一步预测剩余计划形成了隐式闭环：失败步骤会持续出现在后续输出中，轨迹随之更新，无需人工设计的恢复逻辑或脆弱的视觉历史缓冲区即可实现自动延续与重新规划。在具身规划、长时域推理、轨迹预测以及仿真与真实Franka机器人端到端操作中的大量实验表明，该方法在长时域成功率、鲁棒性及分布外泛化方面取得了显著提升。项目页面：https://www.liuisabella.com/LoHoManip

---

### 2. X2-N: A Transformable Wheel-legged Humanoid Robot with Dual-mode Locomotion and Manipulation

- **作者**: Yan Ning, Xingzhou Chen, Delong Li, Hao Zhang, Hanfu Gai, Tongyuan Li, Cheng Zhang, Zhihui Peng, Ling Shi
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.21541v1)
- **发表日期**: 2026-04-23
- **匹配关键词**: locomotion and manipulation
- **arXiv**: [2604.21541v1](http://arxiv.org/abs/2604.21541v1)
- **📥 PDF**: 已下载至本地 (`2604.21541v1_X2-N_A_Transformable_Wheel-legged_Humanoid_Robot_with_Dual-mode_Locomotion_and_Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 轮腿机器人结合了轮式运动的高效性与腿式系统的多地形适应能力，能够在连续与离散地形上实现快速移动。然而，传统设计通常采用固定式轮足和有限自由度的髋关节，导致其腿式运动时的稳定性和机动性低于具有平足结构的人形机器人。此外，现有平台大多缺乏配备双臂的完整上半身，限制了其执行灵巧操作任务的能力。

本文提出X2-N——一种具备双模式运动与操作能力的高自由度可变形机器人。该机器人可切换人形与轮腿两种形态，并通过关节重构实现无缝变形。我们进一步提出基于强化学习的全身控制框架，针对该形态实现混合运动、变形与操作的统一控制。通过动态滑行、爬楼梯及包裹递送等系列挑战性任务验证，X2-N展现出高运动效率、强地形适应性及稳定的移动操作性能，凸显其实际部署潜力。

---

### 3. From Noise to Intent: Anchoring Generative VLA Policies with Residual Bridges

- **作者**: Yiming Zhong, Yaoyu He, Zemin Yang, Pengfei Tian, Yifan Huang, Qingqiu Huang, Xinge Zhu, Yuexin Ma
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.21391v1)
- **发表日期**: 2026-04-23
- **匹配关键词**: VLA
- **arXiv**: [2604.21391v1](http://arxiv.org/abs/2604.21391v1)
- **📥 PDF**: 已下载至本地 (`2604.21391v1_From_Noise_to_Intent_Anchoring_Generative_VLA_Policies_with_Residual_Bridges.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 在具身智能领域，连接高层语义理解与底层物理控制始终是一个持续存在的挑战，其根源在于认知与行动之间存在根本性的时空尺度错配。现有生成式视觉-语言-动作（VLA）策略通常采用"从噪声生成"范式，该范式忽视了这一差异，导致优化过程中表征效率低下且条件对齐能力薄弱。本研究提出ResVLA架构，将范式转变为"从意图精炼"。基于机器人运动可自然分解为全局意图与局部动力学的认知，ResVLA利用频谱分析将控制解耦为确定性低频锚点与随机性高频残差。通过将生成过程锚定于预测意图，该模型通过残差扩散桥严格聚焦于局部动力学的精炼。大量仿真实验表明，ResVLA在性能、对语言及机器人形态扰动的鲁棒性方面均达到竞争水平，且收敛速度优于标准生成基线模型。在真实机器人实验中，该模型同样展现出卓越性能。

---

### 4. A Replicable Robotics Awareness Method Using LLM-Enabled Robotics Interaction: Evidence from a Corporate Challenge

- **作者**: S. A. Prieto, M. A. Gopee, Y. Ben Arab, B. García de Soto, J. Esteba, P. Olivera Brizzio
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.21377v1)
- **发表日期**: 2026-04-23
- **匹配关键词**: human-robot collaboration
- **arXiv**: [2604.21377v1](http://arxiv.org/abs/2604.21377v1)
- **📥 PDF**: 已下载至本地 (`2604.21377v1_A_Replicable_Robotics_Awareness_Method_Using_LLM-Enabled_Robotics_Interaction_Evidence_from_a_Corpor.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 大型语言模型正越来越多地被探索作为人类与机器人系统之间的交互界面，但关于此类技术如何不仅用于交互，还能作为结构化手段，在真实组织环境中向非专业用户介绍机器人技术的证据仍然有限。本文介绍并评估了一种基于挑战的机器人认知方法，该方法通过阿联酋AD Ports集团员工参与的、由大语言模型赋能的人形机器人活动得以实施。活动中，参与者使用基于大语言模型控制框架解析的语音指令，在物流启发的任务环境中与人形机器人互动。该活动被设计为团队化、角色驱动的体验，旨在让参与者在无需机器人专业知识的前提下，接触具身人工智能与人机协作。为评估该方法，活动后开放了为期16天的问卷调查，共收集102份回复。结果表明整体反响强烈：满意度高（8.46/10），对机器人与人工智能的兴趣提升（4.47/5），对新兴人机协作形式的理解加深（4.45/5）。直接与机器人互动的参与者还报告了自然交互体验（4.37/5），并强烈感受到随着活动推进交互变得更容易（4.74/5）。与此同时，可靠性和可预测性方面的较低评分，为未来迭代指出了重要的技术与设计挑战。研究结果表明，基于挑战、由大语言模型赋能的人形交互，可成为工业与运营环境中一种有前景且可复制的机器人认知方法。

---

### 5. A Deployable Embodied Vision-Language Navigation System with Hierarchical Cognition and Context-Aware Exploration

- **作者**: Kuan Xu, Ruimeng Liu, Yizhuo Yang, Denan Liang, Tongxing Jin, Shenghai Yuan, Chen Wang, Lihua Xie ⭐
  - **高亮作者**: Chen Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.21363v1)
- **发表日期**: 2026-04-23
- **匹配关键词**: exploration, navigation, VLN
- **arXiv**: [2604.21363v1](http://arxiv.org/abs/2604.21363v1)
- **📥 PDF**: 已下载至本地 (`2604.21363v1_A_Deployable_Embodied_Vision-Language_Navigation_System_with_Hierarchical_Cognition_and_Context-Awar.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 弥合具身智能与嵌入式部署之间的鸿沟仍是智能机器人系统的关键挑战——感知、推理与规划必须在计算、内存、能耗及实时执行的严格约束下协同运作。在视觉语言导航（VLN）领域，现有方法往往面临强推理能力与真实平台高效部署之间的根本性权衡。本文提出一种可部署的具身VLN系统，在真实机器人平台上同时实现了高效率和鲁棒的高层推理能力。为此，我们将系统解耦为三个异步模块：用于连续环境感知的实时感知模块、用于空间语义聚合的记忆整合模块，以及用于高层决策的推理模块。我们通过增量构建认知记忆图来编码场景信息，并将其进一步分解为子图，从而支持视觉语言模型（VLM）的推理。为提升导航效率与精度，我们还利用认知记忆图将探索问题建模为上下文感知的加权旅行修理工问题（WTRP），通过最小化视点的加权等待时间优化导航路径。在仿真环境与真实机器人平台上的大量实验表明，相较于现有VLN方法，本方法在提升导航成功率和效率的同时，能在资源受限硬件上保持实时性能。

---

### 6. How VLAs (Really) Work In Open-World Environments

- **作者**: Amir Rasouli, Yangzheng Wu, Zhiyuan Li, Rui Heng Yang, Xuan Zhao, Charles Eret, Sajjad Pakdamansavoji
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.21192v1)
- **发表日期**: 2026-04-23
- **匹配关键词**: vision-language-action, VLA, vision-language-action model
- **arXiv**: [2604.21192v1](http://arxiv.org/abs/2604.21192v1)
- **📥 PDF**: 已下载至本地 (`2604.21192v1_How_VLAs_(Really)_Work_In_Open-World_Environments.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作模型（VLAs）已广泛应用于机器人领域，在各类操作问题中取得了显著成功。近期，VLAs被用于长时域任务，并在BEHAVIOR1K（B1K）等基准测试中评估其解决复杂家务的能力。此类基准测试的常用评估指标是基于与过程无关的标准满足度计算的成功率或部分得分——即仅考虑物体的最终状态，而不关注导致该状态的事件过程。本文认为，采用此类评估协议既无法反映操作安全性，还可能夸大报告性能，从而削弱未来实际部署的核心挑战。为此，我们对B1K挑战赛中的前沿模型进行了深入分析，从性能可复现性与一致性、策略操作安全性、任务感知能力及任务未完成的关键因素等维度评估策略鲁棒性。进而提出能捕捉安全违规行为的评估协议，以更准确衡量策略在复杂交互场景中的真实性能。最后，我们探讨了现有VLAs的局限性，并展望未来研究方向。

---

### 7. Navigating the Clutter: Waypoint-Based Bi-Level Planning for Multi-Robot Systems

- **作者**: Jiabao Ji, Yongchao Chen, Yang Zhang, Ramana Rao Kompella, Chuchu Fan, Gaowen Liu, Shiyu Chang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.21138v1)
- **发表日期**: 2026-04-22
- **匹配关键词**: VLA, motion planning
- **arXiv**: [2604.21138v1](http://arxiv.org/abs/2604.21138v1)
- **📥 PDF**: 已下载至本地 (`2604.21138v1_Navigating_the_Clutter_Waypoint-Based_Bi-Level_Planning_for_Multi-Robot_Systems.pdf`)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/UCSB-NLP-Chang/navigate-cluster
- **中文摘要**: 在杂乱环境中实现多机器人控制是一项具有挑战性的问题，涉及复杂的物理约束，包括机器人之间的碰撞、机器人与障碍物的碰撞以及不可达运动。在此类场景中成功规划需要在高层次任务规划与低层次运动规划之间进行联合优化，因为任一层次的失败都可能导致物理约束被违反。然而，由于低层次运动轨迹的参数化复杂，且两个规划层次间的信用分配存在模糊性，任务与运动规划的联合优化十分困难。本文提出了一种混合多机器人控制框架，可联合优化任务与运动规划。为有效参数化低层次规划，我们引入了路径点——一种简洁且表达能力强的运动轨迹表示方式。针对信用分配难题，我们采用基于课程学习的训练策略，并改进RLVR算法，使运动规划器能够将运动可行性反馈传递至任务规划器。在密集障碍物环境下最多容纳九台机器人的挑战性多机器人基准测试BoxNet3D-OBS上进行的实验表明，我们的方法在任务成功率上始终优于忽略运动信息的基线方法和基于VLA的基线方法。我们的代码已开源在https://github.com/UCSB-NLP-Chang/navigate-cluster。

---

### 8. Open-H-Embodiment: A Large-Scale Dataset for Enabling Foundation Models in Medical Robotics

- **作者**: Open-H-Embodiment Consortium, :, Nigel Nelson, Juo-Tung Chen, Jesse Haworth, Xinhao Chen, Lukas Zbinden, Dianye Huang, Alaa Eldin Abdelaal, Alberto Arezzo, Ayberk Acar, Farshid Alambeigi, Carlo Alberto Ammirati, Yunke Ao, Pablo David Aranda Rodriguez, Soofiyan Atar, Mattia Ballo, Noah Barnes, Federica Barontini, Filip Binkiewicz, Peter Black, Sebastian Bodenstedt, Leonardo Borgioli, Nikola Budjak, Benjamin Calmé, Fabio Carrillo, Nicola Cavalcanti, Changwei Chen, Haoxin Chen, Sihang Chen, Qihan Chen, Zhongyu Chen, Ziyang Chen, Shing Shin Cheng, Meiqing Cheng, Min Cheng, Zih-Yun Sarah Chiu, Xiangyu Chu, Camilo Correa-Gallego, Giulio Dagnino, Anton Deguet, Jacob Delgado, Jonathan C. DeLong, Kaizhong Deng, Alexander Dimitrakakis, Qingpeng Ding, Hao Ding, Giovanni Distefano, Daniel Donoho, Anqing Duan, Marco Esposito, Shane Farritor, Jad Fayad, Zahi Fayad, Mario Ferradosa, Filippo Filicori, Chelsea Finn, Philipp Fürnstahl, Jiawei Ge, Stamatia Giannarou, Xavier Giralt Ludevid, Frederic Giraud, Aditya Amit Godbole, Ken Goldberg, Antony Goldenberg, Diego Granero Marana, Xiaoqing Guo, Tamás Haidegger, Evan Hailey, Pascal Hansen, Ziyi Hao, Kush Hari, Kengo Hayashi, Jonathon Hawkins, Shelby Haworth, Ortrun Hellig, S. Duke Herrell, Zhouyang Hong, Andrew Howe, Junlei Hu, Ria Jain, Mohammad Rafiee Javazm, Howard Ji, Rui Ji, Jianmin Ji, Zhongliang Jiang, Dominic Jones, Jeffrey Jopling, Britton Jordan, Ran Ju, Michael Kam, Luoyao Kang, Fausto Kang, Siddhartha Kapuria, Peter Kazanzides, Sonika Kiehler, Ethan Kilmer, Ji Woong, Kim, Przemysław Korzeniowski, Chandra Kuchi, Nithesh Kumar, Alan Kuntz, Federico Lavagno, Yu Chung Lee, Hao-Chih Lee, Hang Li, Zhen Li, Xiao Liang, Xinxin Lin, Jinsong Lin, Chang Liu, Fei Liu, Pei Liu, Yun-hui Liu, Wanli Liuchen, Eszter Lukács, Sareena Mann, Miles Mannas, Brett Marinelli, Sabina Martyniak, Francesco Marzola, Lorenzo Mazza, Xueyan Mei, Maria Clara Morais, Luigi Muratore, Chetan Reddy Narayanaswamy, Michał Naskręt, David Navarro-Alarcon, Cyrus Neary, Chi Kit Ng, Christopher Nguan, David Noonan, Ki Hwan Oh, Tom Christian Olesch, Allison M. Okamura, Justin Opfermann, Matteo Pescio, Doan Xuan Viet Pham, Tito Porras, Hongliang Ren, Ariel Rodriguez Jimenez, Ferdinando Rodriguez y Baena, Septimiu E. Salcudean, Asmitha Sathya, Preethi Satish, Lalithkumar Seenivasan, Jiaqi Shao, Yiqing Shen, Yu Sheng, Lucy XiaoYang Shi, Zoe Soulé, Stefanie Speidel, Mingwu Su, Jianhao Su, Idris Sunmola, Kristóf Takács, Yunxi Tang, Patrick Thornycroft, Yu Tian, Jordan Thompson, Mehmet K. Turkcan, Mathias Unberath, Pietro Valdastri, Carlos Vives, Quan Vuong, Martin Wagner, Farong Wang, Wei Wang, Lidian Wang, Chung-Pang Wang, Guankun Wang, Junyi Wang, Erqi Wang, Ziyi Wang, Tanner Watts, Wolfgang Wein, Yimeng Wu, Zijian Wu, Hongjun Wu, Luohong Wu, Jie Ying Wu, Junlin Wu, Victoria Wu, Kaixuan Wu, Mateusz Wójcikowski, Yunye Xiao, Nan Xiao, Wenxuan Xie, Hao Yang, Tianqi Yang, Yinuo Yang, Menglong Ye, Ryan S. Yeung, Nural Yilmaz, Chim Ho Yin, Michael Yip, Rayan Younis, Chenhao Yu, Sayem Nazmuz Zaman, Milos Zefran, Han Zhang, Yuelin Zhang, Yidong Zhang, Yanyong Zhang, Xuyang Zhang, Yameng Zhang, Joyce Zhang, Ning Zhong, Peng Zhou, Haoying Zhou, Xiuli Zuo, Nassir Navab, Mahdi Azizian, Sean D. Huver, Axel Krieger ⭐
  - **高亮作者**: Chelsea Finn
- **单位**: Brian; Brian; Brian...
- **发表日期**: 2026-04-22
- **匹配关键词**: vision-language-action, vision-language-action model
- **arXiv**: [2604.21017v1](http://arxiv.org/abs/2604.21017v1)
- **📥 PDF**: 已下载至本地 (`2604.21017v1_Open-H-Embodiment_A_Large-Scale_Dataset_for_Enabling_Foundation_Models_in_Medical_Robotics.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 自主医疗机器人有望改善患者预后、减轻医护人员工作负担、普及医疗服务并实现超人类精度。然而，自主医疗机器人技术长期受困于一个根本性数据问题：现有医疗机器人数据集规模小、形态单一且极少公开共享，这制约了该领域发展所需的基础模型研发。我们推出Open-H-Embodiment——迄今最大规模的医疗机器人视频与同步运动学开放数据集，涵盖49家以上机构及多种机器人平台，包括CMR Versius、直觉外科达芬奇系统、达芬奇研究套件（dVRK）、Rob Surgical BiTrack、Virtual Incision MIRA、Moon Surgical Maestro及各类定制系统，覆盖手术操作、机器人超声和内窥镜流程。我们通过两个基础模型展示了该数据集的研究价值。GR00T-H是首个面向医疗机器人的开放基础视觉-语言-动作模型，也是唯一能在结构化缝合基准测试中实现全端到端任务完成的评估模型（试验成功率25%，其他模型均为0%），并在包含29步的离体缝合序列中达到64%的平均成功率。我们还训练了Cosmos-H-Surgical-Simulator——首个支持单检查点多形态手术仿真的动作条件世界模型，覆盖九种机器人平台，可为医疗领域提供计算机内策略评估与合成数据生成。这些结果表明，开放的大规模医疗机器人数据采集可作为研究社区的关键基础设施，推动机器人学习、世界建模等领域的突破性进展。

---

### 9. PokeVLA: Empowering Pocket-Sized Vision-Language-Action Model with Comprehensive World Knowledge Guidance

- **作者**: Yupeng Zheng, Xiang Li, Songen Gu, Yuhang Zheng, Shuai Tian, Weize Li, Linbo Wang, Senyu Fei, Pengfei Li, Yinfeng Gao, Zebin Xing, Yilun Chen, Qichao Zhang, Haoran Li, Wenchao Ding
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.20834v1)
- **发表日期**: 2026-04-22
- **匹配关键词**: affordance, VLA, vision-language-action model, vision-language-action
- **arXiv**: [2604.20834v1](http://arxiv.org/abs/2604.20834v1)
- **📥 PDF**: 已下载至本地 (`2604.20834v1_PokeVLA_Empowering_Pocket-Sized_Vision-Language-Action_Model_with_Comprehensive_World_Knowledge_Guid.pdf`)
- **🔓 开源**: CODE, MODEL, PROJECT_PAGE
  - 链接：https://getterupper.github.io/PokeVLA
- **中文摘要**: 视觉-语言-动作（VLA）模型的最新进展为机器人操作开辟了新途径，但现有方法仍存在效率有限、缺乏高层知识与空间感知能力等问题。针对这些挑战，我们提出PokeVLA——一种轻量级且强大的具身操作基础模型，能够有效将视觉语言理解融入动作学习。该框架引入两阶段训练范式：首先，在包含空间定位、功能属性及具身推理任务的240万样本多模态数据集上预训练紧凑型视觉语言模型（PokeVLM）；其次，通过多视角目标感知语义学习、几何对齐及新型动作专家模块，将操作相关表征注入动作空间。大量实验表明，该方法在LIBERO-Plus基准测试及真实场景部署中均达到最优性能，在成功率与多类扰动鲁棒性方面显著超越基线模型。为促进可复现性与社区发展，我们将开源代码、模型权重及预训练数据集构建脚本。项目主页：https://getterupper.github.io/PokeVLA

---

### 10. Temporal Difference Calibration in Sequential Tasks: Application to Vision-Language-Action Models

- **作者**: Shelly Francis-Meretzki, Mirco Mutti, Yaniv Romano, Aviv Tamar
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.20472v1)
- **发表日期**: 2026-04-22
- **匹配关键词**: vision-language-action, VLA, vision-language-action model
- **arXiv**: [2604.20472v1](http://arxiv.org/abs/2604.20472v1)
- **📥 PDF**: 已下载至本地 (`2604.20472v1_Temporal_Difference_Calibration_in_Sequential_Tasks_Application_to_Vision-Language-Action_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 近期，视觉-语言-动作（VLA）模型在机器人领域的进展凸显了在序列任务中可靠不确定性量化的重要性。然而，在此类场景下评估与改进校准效果仍鲜有探索，尤其在仅观测到部分轨迹的情况下。本研究针对片段式任务提出序列校准方法——任务成功置信度在片段执行过程中逐步生成，而最终成功状态在片段结束时判定。我们引入Brier分数的序列扩展形式，并证明在二元结果条件下，其风险最小化函数与VLA策略的价值函数等价。这一关联架起了不确定性校准与强化学习之间的桥梁，使得时序差分（TD）价值估计可作为随时间演化的原则性校准机制。实验表明，在仿真与真实机器人数据上，TD校准相较于现有最优方法显著提升了性能。值得注意的是，与近期采用不同校准技术的研究发现相反，我们证明当采用TD校准时，VLA的单步动作概率可产生具有竞争力的不确定性估计。

---

### 11. A Vision-Language-Action Model for Adaptive Ultrasound-Guided Needle Insertion and Needle Tracking

- **作者**: Yuelin Zhang, Qingpeng Ding, Longxiang Tang, Chengyu Fang, Shing Shin Cheng
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.20347v1)
- **发表日期**: 2026-04-22
- **匹配关键词**: vision-language-action, VLA, vision-language-action model
- **arXiv**: [2604.20347v1](http://arxiv.org/abs/2604.20347v1)
- **📥 PDF**: 已下载至本地 (`2604.20347v1_A_Vision-Language-Action_Model_for_Adaptive_Ultrasound-Guided_Needle_Insertion_and_Needle_Tracking.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 超声（US）引导下的针穿刺是一项关键但具有挑战性的操作，原因在于动态成像条件及针的可视化困难。目前已提出多种自动化针穿刺方法，但这些方法通常依赖手工设计的模块化控制器流程，在复杂情况下性能会下降。本文提出了一种视觉-语言-动作（VLA）模型，用于在机器人超声（RUS）系统上实现自适应且自动化的超声引导针穿刺与跟踪。该框架为针跟踪与针穿刺控制提供了统一方案，能够根据获取的针位置和环境感知实现实时、动态自适应的穿刺调整。为实现实时端到端跟踪，我们提出了一种跨深度融合（CDF）跟踪头，该结构融合了大规模视觉骨干网络中的浅层位置特征与深层语义特征。为使预训练的视觉骨干网络适应跟踪任务，我们引入了一种跟踪条件化（TraCon）寄存器，用于参数高效的特征调节。在针跟踪之后，我们提出了一种不确定性感知控制策略和异步VLA流水线，用于自适应针穿刺控制，确保及时决策以提升安全性和操作效果。在针跟踪与穿刺任务上的大量实验表明，我们的方法始终优于现有最优跟踪器及人工操作，实现了更高的跟踪精度、穿刺成功率提升及操作时间缩短，为基于RUS的智能干预指明了有前景的发展方向。

---

### 12. Cortex 2.0: Grounding World Models in Real-World Industrial Deployment

- **作者**: Adriana Aida, Walid Amer, Katarina Bankovic, Dhruv Behl, Fabian Busch, Annie Bhalla, Minh Duong, Florian Gienger, Rohan Godse, Denis Grachev, Ralf Gulde, Elisa Hagensieker, Junpeng Hu, Shivam Joshi, Tobias Knobloch, Likith Kumar, Damien LaRocque, Keerthana Lokesh, Omar Moured, Khiem Nguyen, Christian Preyss, Ranjith Sriganesan, Vikram Singh, Carsten Sponner, Anh Tong, Dominik Tuscher, Marc Tuscher, Pavan Upputuri
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.20246v1)
- **发表日期**: 2026-04-22
- **匹配关键词**: vision-language-action, contact-rich manipulation, vision-language-action model
- **arXiv**: [2604.20246v1](http://arxiv.org/abs/2604.20246v1)
- **📥 PDF**: 已下载至本地 (`2604.20246v1_Cortex_2.0_Grounding_World_Models_in_Real-World_Industrial_Deployment.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 工业机器人操作需要在不同本体、任务及变化的物体分布中实现可靠的长时域执行。尽管视觉-语言-动作模型展现出强大的泛化能力，但其本质上仍属于反应式系统。这类模型仅根据当前观测优化下一步动作，而不评估未来潜在结果，因此在长时域任务的复合失效模式下表现脆弱。Cortex 2.0将控制范式从反应式转向"规划-执行"：在视觉潜在空间中生成候选未来轨迹，根据预期成功率和效率进行评分，最终仅执行得分最高的候选方案。我们在单臂和双臂操作平台上，针对四种复杂度递增的任务（拾放、物品与垃圾分拣、螺丝分拣、鞋盒拆包）对Cortex 2.0进行评估。该模型在所有任务中均持续超越最先进的视觉-语言-动作基线方法，取得最优结果。在反应式策略失效的非结构化环境中（如重度杂乱、频繁遮挡和接触密集型操作），该系统仍保持可靠性能。这些结果表明，基于世界模型的规划能够在复杂工业环境中稳定运行。

---

### 13. JoyAI-RA 0.1: A Foundation Model for Robotic Autonomy

- **作者**: Tianle Zhang, Zhihao Yuan, Dafeng Chi, Peidong Liu, Dongwei Li, Kejun Hu, Likui Zhang, Junnan Nie, Ziming Wei, Zengjue Chen, Yili Tang, Jiayi Li, Zhiyuan Xiang, Mingyang Li, Tianci Luo, Hanwen Wan, Ao Li, Linbo Zhai, Zhihao Zhan, Xiaodong Bai, Jiakun Cai, Peng Cao, Kangliang Chen, Siang Chen, Yixiang Dai, Shuai Di, Yicheng Gong, Chenguang Gui, Yucheng Guo, Peng Hao, Qingrong He, Haoyang Huang, Kunrui Huang, Zhixuan Huang, Shibo Jin, Yixiang Jin, Anson Li, Dongjiang Li, Jiawei Li, Ruodai Li, Yihang Li, Yuzhen Li, Jiaming Liang, Fangsheng Liu, Jing Long, Mingxi Luo, Xing Pan, Hui Shen, Xiaomeng Tian, Daming Wang, Song Wang, Junwu Xiong, Hang Xu, Wanting Xu, Zhengcheng Yu, He Zhang, Jiyao Zhang, Lin Zhao, Chen Zhou, Nan Duan, Yuzheng Zhuang, Liang Lin
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.20100v2)
- **发表日期**: 2026-04-22
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2604.20100v2](http://arxiv.org/abs/2604.20100v2)
- **📥 PDF**: 已下载至本地 (`2604.20100v2_JoyAI-RA_0.1_A_Foundation_Model_for_Robotic_Autonomy.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 开放世界环境中的机器人自主性从根本上受限于数据多样性不足和跨本体泛化能力薄弱。现有机器人数据集在规模和任务覆盖范围上往往有限，而不同机器人本体间的显著差异阻碍了有效行为知识迁移。为解决这些挑战，我们提出JoyAI-RA——一种专为可泛化机器人操作设计的视觉-语言-动作（VLA）具身基础模型。JoyAI-RA构建了多源多层级预训练框架，整合网络数据、大规模第一人称人类操作视频、仿真生成轨迹及真实机器人数据。通过基于显式动作空间统一的异构多源数据训练，JoyAI-RA有效弥合了本体差异（尤其是人类操作与机器人控制之间的鸿沟），从而增强跨本体行为学习能力。在仿真和真实世界基准测试中，JoyAI-RA均优于现有最先进方法，尤其在需要泛化能力的多样化任务上表现突出。

---

### 14. DualSplat: Robust 3D Gaussian Splatting via Pseudo-Mask Bootstrapping from Reconstruction Failures

- **作者**: Xu Wang, Zhiru Wang, Shiyun Xie, Chengwei Pan, Yisong Chen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.21631v1)
- **发表日期**: 2026-04-23
- **匹配关键词**: 3D gaussian splatting, nerf, gaussian splatting
- **arXiv**: [2604.21631v1](http://arxiv.org/abs/2604.21631v1)
- **📥 PDF**: 已下载至本地 (`2604.21631v1_DualSplat_Robust_3D_Gaussian_Splatting_via_Pseudo-Mask_Bootstrapping_from_Reconstruction_Failures.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 尽管3D高斯泼溅（3DGS）能实现实时逼真渲染，但当训练图像包含破坏多视角一致性的瞬态物体时，其性能会显著下降。现有方法面临循环依赖困境：精确的瞬态检测需要重建良好的静态场景，而干净的重建本身又依赖于可靠的瞬态掩膜。我们提出DualSplat——一种"失败转先验"框架，将首次重建的失败转化为显式先验用于二次重建阶段。我们观察到，仅出现在部分视角中的瞬态物体，在保守初始训练中常表现为不完整碎片。通过结合光度残差、特征不匹配和SAM2实例边界，我们利用这些失败构建物体级伪掩膜。这些伪掩膜随后引导干净的二次3DGS优化，同时轻量级MLP通过从先验监督逐步过渡到自一致性来在线优化掩膜。在RobustNeRF和NeRF On-the-go上的实验表明，DualSplat优于现有基线方法，在瞬态密集场景和瞬态区域展现出特别明显的优势。

---

## 📌 Poster

*其他相关研究*

---

### 1. SLAM as a Stochastic Control Problem with Partial Information: Optimal Solutions and Rigorous Approximations

- **作者**: Ilir Gusija, Fady Alajaji, Serdar Yüksel
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.21693v1)
- **发表日期**: 2026-04-23
- **匹配关键词**: exploration, localization and mapping
- **arXiv**: [2604.21693v1](http://arxiv.org/abs/2604.21693v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 同时定位与地图构建（SLAM）是机器人学中一项基础的状态估计问题，机器人需在准确构建环境地图的同时，确定自身在该地图中的位置。我们通过最优随机控制的视角研究主动SLAM问题，从而将其重新表述为部分信息下的决策问题。在回顾几种常见模型后，我们提出主动SLAM的一般随机控制框架，并对运动、感知与地图表示进行严谨处理。我们引入一种新的探索阶段代价函数，该函数在评估信息采集行为时对状态几何特征进行编码。这一框架被构建为非标准的部分可观测马尔可夫决策过程（POMDP），随后通过分析推导出具有严格理论依据且接近最优的近似解。为实现该分析，我们在适用于广泛机器人应用场景的通用假设下研究了相关正则性条件。针对特定案例，我们开展了大量数值研究，利用标准学习算法学习接近最优的策略。

---

### 2. Full-Body Dynamic Safety for Robot Manipulators: 3D Poisson Safety Functions for CBF-Based Safety Filters

- **作者**: Meg Wilkinson, Gilbert Bahati, Ryan M. Bena, Emily Fourney, Joel W. Burdick, Aaron D. Ames
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.21189v1)
- **发表日期**: 2026-04-23
- **匹配关键词**: HRI
- **arXiv**: [2604.21189v1](http://arxiv.org/abs/2604.21189v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 机器人操作臂的碰撞规避需要在高维构型空间中强制执行全身安全约束。基于控制障碍函数的安全滤波器已被证明能有效实现安全行为，但执行安全操作所需的大量约束会带来理论和计算上的挑战。本文提出了一种利用三维泊松安全函数实现动态环境中操作臂全身碰撞规避的框架。具体而言，根据环境占据数据，我们以指定分辨率对操作臂表面进行采样，并通过庞特里亚金差分法根据该分辨率收缩自由空间。在此缓冲域上，通过求解泊松方程合成全局光滑的控制障碍函数，从而为整个环境生成单一安全函数。该安全函数在每个采样点处进行评估，通过多约束二次规划由实时安全滤波器生成任务空间控制障碍函数约束。我们证明：在缓冲区域内保持采样点安全即可保证整个连续机器人表面的碰撞规避。该框架在动态环境中的七自由度操作臂上得到了验证。

---

### 3. Neuro-Symbolic Manipulation Understanding with Enriched Semantic Event Chains

- **作者**: Fatemeh Ziaeetabar
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.21053v1)
- **发表日期**: 2026-04-22
- **匹配关键词**: affordance
- **arXiv**: [2604.21053v1](http://arxiv.org/abs/2604.21053v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 在人类环境中运行的机器人系统必须推理物体交互如何随时间演变、当前正在执行何种操作以及接下来可能进行何种操作步骤。经典的增强语义事件链（eSECs）提供了可解释的操作关系描述，但主要停留在描述层面，无法直接支持具有不确定性意识的决策制定。本文提出eSEC-LAM这一神经符号框架，将eSECs转化为用于操作理解的显式事件级符号状态。该框架通过置信度感知谓词、功能对象角色、可供性先验、基元级抽象及显著性引导解释线索对经典eSECs进行增强。这些增强符号状态通过确定性谓词提取从基于基础模型的感知前端获得，而当前动作推理与下一基元预测则通过对基元前置/后置条件的轻量级符号推理实现。我们在EPIC-KITCHENS-100、EPIC-KITCHENS VISOR和Assembly101数据集上，从动作识别、下一基元预测、对感知噪声的鲁棒性及解释一致性四个维度评估该框架。实验结果表明，eSEC-LAM在动作识别上具有竞争力，显著提升了下一基元预测性能，在感知条件退化时比经典符号方法和端到端视频基线方法更具鲁棒性，并能基于显式关系证据生成时间一致的解释轨迹。这些发现证明，增强语义事件链不仅可作为操作的可解释描述符，更能作为神经符号动作推理的有效内部状态。

---

### 4. DeVI: Physics-based Dexterous Human-Object Interaction via Synthetic Video Imitation

- **作者**: Hyeonwoo Kim, Jeonghwan Kim, Kyungwon Cho, Hanbyul Joo
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.20841v1)
- **发表日期**: 2026-04-22
- **匹配关键词**: motion planning
- **arXiv**: [2604.20841v1](http://arxiv.org/abs/2604.20841v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 视频生成模型的最新进展使得在广泛场景和物体类别中合成逼真的人-物交互视频成为可能，包括运动捕捉系统难以捕捉的复杂灵巧操作。尽管这些合成视频中蕴含的丰富交互知识为灵巧机器人操作的运动规划提供了巨大潜力，但其有限的物理保真度和纯二维特性使其难以直接作为基于物理的角色控制中的模仿目标。我们提出DeVI（灵巧视频模仿）这一新颖框架，利用文本条件合成视频实现物理合理的灵巧智能体控制，使其能够与未见过的目标物体进行交互。为克服生成式二维线索的不精确性，我们引入混合追踪奖励机制，将三维人体追踪与鲁棒的二维物体追踪相结合。与依赖高质量三维运动学演示的方法不同，DeVI仅需生成视频即可实现跨不同物体和交互类型的零样本泛化。大量实验表明，DeVI在模仿三维人-物交互演示方面优于现有方法，尤其在建模灵巧手-物交互时表现突出。我们进一步验证了DeVI在多物体场景和文本驱动动作多样性中的有效性，展示了将视频作为人-物交互感知运动规划器的优势。

---

### 5. Visual-Tactile Peg-in-Hole Assembly Learning from Peg-out-of-Hole Disassembly

- **作者**: Yongqiang Zhao, Xuyang Zhang, Zhuo Chen, Matteo Leonetti, Emmanouil Spyrakos-Papastavridis, Shan Luo
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.20712v1)
- **发表日期**: 2026-04-22
- **匹配关键词**: exploration
- **arXiv**: [2604.20712v1](http://arxiv.org/abs/2604.20712v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 插孔（PiH）装配是一项基础但具有挑战性的机器人操作任务。尽管强化学习（RL）在解决此类任务中展现出潜力，但需要大量的探索。本文针对PiH任务提出了一种新颖的视觉-触觉技能学习框架，利用其逆任务——拔销（PooH）拆卸——来促进PiH学习。与PiH相比，PooH本质上更简单，因为它仅需克服现有摩擦力而无需精确对准，因此数据收集效率更高。为此，我们将PooH和PiH统一建模为部分可观测马尔可夫决策过程（POMDP），并共享视觉-触觉观测空间。首先训练视觉-触觉PooH策略；其包含运动学、视觉和触觉信息的轨迹经过时间反转和动作随机化处理，为PiH提供专家数据。在策略学习中，视觉感知辅助销孔接近，而触觉测量补偿销孔未对准。跨不同销孔几何形状的实验表明，视觉-触觉策略的接触力比单模态策略低6.4%，且我们的框架在已知物体上平均成功率达87.5%，在未知物体上达77.1%，成功率比直接从头训练PiH策略的RL方法高出18.1%。演示、代码和数据集见https://sites.google.com/view/pooh2pih。

---

### 6. Where are they looking in the operating room?

- **作者**: Keqi Chen, Séraphin Baributsa, Lilien Schewski, Vinkle Srivastav, Didier Mutter, Guido Beldi, Sandra Keller, Nicolas Padoy
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.20574v1)
- **发表日期**: 2026-04-22
- **匹配关键词**: human-robot interaction
- **arXiv**: [2604.20574v1](http://arxiv.org/abs/2604.20574v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 目的：视线追踪（即推断个体注视方向的任务）已在计算机视觉领域得到广泛研究，推动了视觉注意力建模、社交场景理解及人机交互等研究的发展。然而，在手术室这一视觉注意力对手术流程分析至关重要的复杂高风险环境中，视线追踪技术尚未被探索。本研究首次将视线追踪概念引入手术领域，并证明其在理解手术室中的临床角色、手术阶段及团队沟通方面具有巨大潜力。方法：我们通过添加视线追踪标注扩展了4D-OR数据集，同时为Team-OR数据集新增了视线追踪标注及团队沟通活动标注。随后提出基于视线追踪模型的新方法，用于解决临床角色预测、手术阶段识别及团队沟通检测问题。针对角色与阶段识别，我们提出仅依赖视线预测的注视热力图方法；针对团队沟通检测，采用自监督方式训练编码视线片段特征的时空模型，并将特征输入时序活动检测模型。结果：在4D-OR和Team-OR数据集上的实验表明，本方法在所有下游任务中均达到最优性能。量化结果显示，临床角色预测的F1分数为0.92，手术阶段识别为0.95。此外，在团队沟通检测任务中，本方法显著超越现有基线，将此前最佳性能提升超过30%。结论：我们首次将手术室中的视线追踪作为手术数据科学的新研究方向，强调其在计算机辅助干预中推动手术流程分析的巨大潜力。

---

