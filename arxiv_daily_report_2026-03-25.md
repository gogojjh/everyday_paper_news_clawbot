# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-03-25 08:04

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 4/20 篇提供

**🌟 Highlight**: 10 篇 | **📌 Poster**: 10 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. DualCoT-VLA: Visual-Linguistic Chain of Thought via Parallel Reasoning for Vision-Language-Action Models

- **作者**: Zhide Zhong, Junfeng Li, Junjie He, Haodong Yan, Xin Gong, Guanyi Zhao, Yingjie Cai, Jiantao Gao, Xu Yan, Bingbing Liu, Yingcong Chen, Liuqing Yang, Haoang Li
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.22280v1)
- **发表日期**: 2026-03-23
- **匹配关键词**: vision-language-action, vision-language-action model, VLA
- **arXiv**: [2603.22280v1](http://arxiv.org/abs/2603.22280v1)
- **📥 PDF**: 已下载至本地 (`2603.22280v1_DualCoT-VLA_Visual-Linguistic_Chain_of_Thought_via_Parallel_Reasoning_for_Vision-Language-Action_Mod.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型能够直接将视觉观察和语言指令映射为机器人动作。虽然这类模型在简单任务中表现良好，但标准的VLA模型在处理需要逻辑规划的复杂多步骤任务以及需要精细空间感知的精确操作时往往存在困难。近期研究尝试引入思维链（CoT）推理机制，赋予VLA模型“先思考后行动”的能力。然而，当前基于CoT的VLA模型面临两个关键局限：1）由于依赖孤立单模态CoT，无法同时捕捉低层视觉细节与高层逻辑规划；2）逐步自回归解码导致推理延迟较高且误差会逐步累积。为突破这些局限，我们提出DualCoT-VLA——一种采用并行推理机制的视觉-语言CoT方法。为实现全面多模态推理，该方法融合了面向底层空间理解的视觉CoT与面向高层任务规划的语言CoT。此外，为克服延迟瓶颈，我们设计了并行CoT机制，通过引入两组可学习的查询标记，将自回归推理转变为单步前向推理。大量实验表明，DualCoT-VLA在LIBERO和RoboCasa GR1基准测试及实际平台中均取得了最先进的性能表现。

---

### 2. UniDex: A Robot Foundation Suite for Universal Dexterous Hand Control from Egocentric Human Videos

- **作者**: Gu Zhang, Qicheng Xu, Haozhe Zhang, Jianhan Ma, Long He, Yiming Bao, Zeyu Ping, Zhecheng Yuan, Chenhao Lu, Chengbo Yuan, Tianhai Liang, Xiaoyu Tian, Maanping Shao, Feihong Zhang, Mingyu Ding, Yang Gao, Hao Zhao, Hang Zhao, Huazhe Xu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.22264v1)
- **发表日期**: 2026-03-23
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2603.22264v1](http://arxiv.org/abs/2603.22264v1)
- **📥 PDF**: 已下载至本地 (`2603.22264v1_UniDex_A_Robot_Foundation_Suite_for_Universal_Dexterous_Hand_Control_from_Egocentric_Human_Videos.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 灵巧操作因真实机器人遥操作数据采集成本高、手部执行器异构性强以及控制维度复杂而持续面临挑战。本文提出UniDex——一个集大规模机器人中心数据集、统一视觉-语言-动作策略及实用人体数据采集系统于一体的机器人基础套件，旨在实现通用灵巧手控制。首先，我们构建了UniDex-Dataset，这是一个包含八种灵巧手（6-24自由度）超过5万条轨迹的机器人中心数据集，数据源自第一人称人类视频数据集。为将人类数据转化为机器人可执行轨迹，我们采用人机协同重定向流程对齐指尖轨迹并保持合理的手物接触，同时通过掩码处理人类手部的显式三维点云数据以缩小运动学与视觉差异。其次，我们提出功能-执行器对齐空间（FAAS），该统一动作空间将功能相似执行器映射至共享坐标，实现跨手型迁移。基于FAAS动作参数化框架，我们训练了UniDex-VLA——一个在UniDex-Dataset上预训练、经任务演示微调的三维视觉-语言-动作策略。此外，我们开发了UniDex-Cap便携采集系统，可同步记录RGB-D数据流与人体手部姿态，并将其转化为机器人可执行轨迹，通过人机数据协同训练降低对高成本机器人演示的依赖。在两种不同手型执行复杂工具使用任务时，UniDex-VLA平均任务完成度达81%，显著超越现有视觉-语言-动作基线模型，同时展现出强大的空间泛化、物体泛化及零样本跨手型泛化能力。UniDex-Dataset、UniDex-VLA与UniDex-Cap共同构成了可扩展的通用灵巧操作基础套件。

---

### 3. ROBOGATE: Adaptive Failure Discovery for Safe Robot Policy Deployment via Two-Stage Boundary-Focused Sampling

- **作者**: Byungjin Kim
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.22126v1)
- **发表日期**: 2026-03-23
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2603.22126v1](http://arxiv.org/abs/2603.22126v1)
- **📥 PDF**: 已下载至本地 (`2603.22126v1_ROBOGATE_Adaptive_Failure_Discovery_for_Safe_Robot_Policy_Deployment_via_Two-Stage_Boundary-Focused_.pdf`)
- **🔓 开源**: CODE
- **中文摘要**: 在工业环境中部署习得的机器人操作策略需要进行严格的部署前验证，然而在高维参数空间中进行穷尽测试是不可行的。我们提出了ROBOGATE这一部署风险管理框架，该框架将基于物理的仿真与两阶段自适应采样策略相结合，以高效发现操作参数空间中的失效边界。第一阶段在8维参数空间中使用拉丁超立方采样（LHS），通过20,000个均匀分布的实验建立粗略的失效态势图。第二阶段采用边界聚焦采样，在30-70%成功率过渡区域集中进行10,000次额外实验，从而实现精确的失效边界映射。利用搭载牛顿物理引擎的NVIDIA Isaac Sim平台，我们在两种机器人实体——Franka Panda（7自由度）和UR5e（6自由度）上对预设的抓放控制器进行了总计30,000次实验评估。我们的逻辑回归风险模型在合并数据集上实现了0.780的AUC值（相较第一阶段单独模型的0.754有所提升），识别出闭式失效边界方程，并揭示了影响两种机器人平台的四个通用危险区域。我们进一步将该框架应用于视觉-语言-动作（VLA）模型评估，其中Octo-Small模型在68个对抗场景中成功率为0.0%，而预设基线模型达到100%——这100个百分点的差距凸显了在工业环境中部署基础模型所面临的挑战。ROBOGATE为开源框架，可在单GPU工作站上运行。

---

### 4. FreeArtGS: Articulated Gaussian Splatting Under Free-moving Scenario

- **作者**: Hang Dai, Hongwei Fan, Han Zhang, Duojin Wu, Jiyao Zhang, Hao Dong
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.22102v1)
- **发表日期**: 2026-03-23
- **匹配关键词**: gaussian splatting, articulated object
- **arXiv**: [2603.22102v1](http://arxiv.org/abs/2603.22102v1)
- **📥 PDF**: 已下载至本地 (`2603.22102v1_FreeArtGS_Articulated_Gaussian_Splatting_Under_Free-moving_Scenario.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://freeartgs.github.io/
- **中文摘要**: 随着增强现实和机器人技术需求的日益增长，对高可扩展性关节物体重建的需求也日益迫切。然而，现有基于离散关节状态或单目视频的重建方法往往需要进行复杂的轴对齐处理，或存在覆盖范围不足的问题，限制了其实际应用。本文提出FreeArtGS，一种在自由移动场景下重建关节物体的新方法，该场景设置简单且具有高可扩展性。FreeArtGS将自由移动部件分割与关节估计及端到端优化相结合，仅需单目RGB-D视频作为输入。通过利用现有点追踪和特征模型的先验知识进行优化，自由移动部件分割模块能够在无约束拍摄条件下根据相对运动识别刚性部件。关节估计模块则校准统一的对象到相机位姿，并从部件分割中稳健地恢复关节类型与轴线。最后，基于3DGS的端到端优化被用于联合重建关节物体的视觉纹理、几何结构和关节角度。我们在两个基准数据集及真实世界自由移动关节物体上进行了实验。结果表明，FreeArtGS在自由移动关节物体重建方面表现优异，同时在传统重建场景中保持高度竞争力，证明其是现实资产生成的实用有效解决方案。项目页面详见：https://freeartgs.github.io/

---

### 5. Do World Action Models Generalize Better than VLAs? A Robustness Study

- **作者**: Zhanguang Zhang, Zhiyuan Li, Behnam Rahmati, Rui Heng Yang, Yintao Ma, Amir Rasouli, Sajjad Pakdamansavoji, Yangzheng Wu, Lingfeng Zhang, Tongtong Cao, Feng Wen, Xingyue Quan, Yingxue Zhang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.22078v1)
- **发表日期**: 2026-03-23
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2603.22078v1](http://arxiv.org/abs/2603.22078v1)
- **📥 PDF**: 已下载至本地 (`2603.22078v1_Do_World_Action_Models_Generalize_Better_than_VLAs?_A_Robustness_Study.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 现实世界中的机器人动作规划具有挑战性，因为它不仅需要理解环境的当前状态，还需预测环境如何随动作演化。视觉-语言-动作模型通过调用动作专家将大规模视觉语言模型重新应用于机器人动作生成，已在多种机器人任务中取得显著成功。然而，其性能仍受限于训练数据范围，对未见场景的泛化能力有限，且易受多样化上下文干扰的影响。近期，世界模型作为视觉-语言-动作模型的替代方案重新受到关注。这类被称为世界动作模型的系统基于在大量视频数据上训练的世界模型构建，能够预测未来状态。通过微调适配，其潜在表征可解码为机器人动作。研究表明，其显式的动态预测能力与从网络规模视频预训练中获得的时空先验相结合，使世界动作模型比视觉-语言-动作模型具有更强的泛化能力。本文对当前先进的视觉-语言-动作策略与最新发布的世界动作模型进行了对比研究，在LIBERO-Plus和RoboTwin 2.0-Plus基准测试中评估了它们在多种视觉与语言干扰下的表现。实验结果表明，世界动作模型展现出强大的鲁棒性：LingBot-VA在RoboTwin 2.0-Plus上达到74.2%的成功率，Cosmos-Policy在LIBERO-Plus上取得82.2%的成功率。虽然如$π_{0.5}$等视觉-语言-动作模型在特定任务中能达到相当的鲁棒性，但通常需要利用多样化机器人数据集和不同学习目标进行大量训练。部分融合视频动态学习的混合方法表现出中等程度的鲁棒性，这凸显了视频先验整合方式的重要性。

---

### 6. VP-VLA: Visual Prompting as an Interface for Vision-Language-Action Models

- **作者**: Zixuan Wang, Yuxin Chen, Yuqi Liu, Jinhui Ye, Pengguang Chen, Changsheng Lu, Shu Liu, Jiaya Jia
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.22003v1)
- **发表日期**: 2026-03-23
- **匹配关键词**: vision-language-action, vision-language-action model, VLA
- **arXiv**: [2603.22003v1](http://arxiv.org/abs/2603.22003v1)
- **📥 PDF**: 已下载至本地 (`2603.22003v1_VP-VLA_Visual_Prompting_as_an_Interface_for_Vision-Language-Action_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作模型通常将视觉观测与语言指令直接映射为机器人控制信号。这种"黑箱"映射机制要求单次前向传播同时完成指令解析、空间定位与底层控制，往往导致空间精度不足且在分布外场景中鲁棒性有限。为解决这些局限，我们提出VP-VLA双系统框架，通过结构化视觉提示接口实现高层推理与底层执行的解耦。具体而言，"系统2规划器"将复杂指令分解为子任务，识别相关目标物体与目标位置。这些空间锚点随后以结构化视觉提示形式直接叠加在视觉观测上，例如十字准线和边界框。在训练过程中，这些提示信息配合新颖的辅助视觉定位目标共同引导"系统1控制器"，使其能够可靠生成精确的底层执行动作。在Robocasa-GR1-Tabletop基准测试与SimplerEnv仿真环境中的实验表明，VP-VLA将成功率分别提升5%与8.3%，超越了包括QwenOFT和GR00T-N1.6在内的竞争基线模型。

---

### 7. Can a Robot Walk the Robotic Dog: Triple-Zero Collaborative Navigation for Heterogeneous Multi-Agent Systems

- **作者**: Yaxuan Wang, Yifan Xiang, Ke Li, Xun Zhang, BoWen Ye, Zhuochen Fan, Fei Wei, Tong Yang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.21723v1)
- **发表日期**: 2026-03-23
- **匹配关键词**: navigation, path planning
- **arXiv**: [2603.21723v1](http://arxiv.org/abs/2603.21723v1)
- **📥 PDF**: 已下载至本地 (`2603.21723v1_Can_a_Robot_Walk_the_Robotic_Dog_Triple-Zero_Collaborative_Navigation_for_Heterogeneous_Multi-Agent_.pdf`)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/triple-zeropp/Triple-zero-robot-agent
- **中文摘要**: 我们提出三重零路径规划（TZPP），这是一个面向异构多机器人系统的协作框架，具备零训练、零先验知识和零仿真的特性。TZPP采用协调者-探索者架构：人形机器人负责任务协调，而四足机器人则借助多模态大语言模型的引导进行环境探索与可行路径识别。我们在宇树G1和Go2机器人平台上实现了TZPP，并在多样化的室内外环境中进行评估测试，包括障碍密集和地标稀疏的场景。实验表明，TZPP展现出稳健的性能、媲美人类的效率以及对未知场景的强大适应能力。通过消除对训练和仿真的依赖，TZPP为异构机器人协作的实际部署提供了可行路径。相关代码与演示视频发布于：https://github.com/triple-zeropp/Triple-zero-robot-agent

---

### 8. RoboAlign: Learning Test-Time Reasoning for Language-Action Alignment in Vision-Language-Action Models

- **作者**: Dongyoung Kim, Sumin Park, Woomin Song, Seungku Kim, Taeyoung Kim, Huiwon Jang, Jinwoo Shin, Jaehyung Kim, Younggyo Seo
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.21341v1)
- **发表日期**: 2026-03-22
- **匹配关键词**: vision-language-action, vision-language-action model, VLA
- **arXiv**: [2603.21341v1](http://arxiv.org/abs/2603.21341v1)
- **📥 PDF**: 已下载至本地 (`2603.21341v1_RoboAlign_Learning_Test-Time_Reasoning_for_Language-Action_Alignment_in_Vision-Language-Action_Model.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 提升多模态大语言模型（MLLMs）的具身推理能力，对于在其基础上构建视觉-语言-动作模型（VLAs）至关重要，这将有助于将多模态理解直接转化为底层动作。为此，近期研究尝试通过视觉问答类型的监督来增强MLLMs的具身推理能力。然而，这些方法被报道会导致VLA性能不稳定，往往仅带来微弱提升甚至产生负面效果。本文提出了一种更系统的MLLM训练框架RoboAlign，能够可靠地提升VLA性能。我们的核心思路是通过零样本自然语言推理生成动作标记，并利用强化学习（RL）优化推理过程以提高动作准确性。由此，RoboAlign弥合了MLLMs中语言与底层动作之间的模态鸿沟，促进了从MLLM到VLA的知识迁移。为验证RoboAlign的有效性，我们在MLLM骨干网络上添加基于扩散模型的动作头来训练VLAs，并在主流机器人基准测试中进行评估。值得注意的是，仅使用不到1%的数据进行监督微调后实施基于RL的对齐，RoboAlign在LIBERO、CALVIN和真实环境中的性能分别比监督微调基线提升了17.5%、18.9%和106.6%。

---

### 9. Dynamic Control Barrier Function Regulation with Vision-Language Models for Safe, Adaptive, and Realtime Visual Navigation

- **作者**: Jeffrey Chen, Rohan Chandra
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.21142v1)
- **发表日期**: 2026-03-22
- **匹配关键词**: navigation, visual navigation
- **arXiv**: [2603.21142v1](http://arxiv.org/abs/2603.21142v1)
- **📥 PDF**: 已下载至本地 (`2603.21142v1_Dynamic_Control_Barrier_Function_Regulation_with_Vision-Language_Models_for_Safe,_Adaptive,_and_Real.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 在动态、非结构化环境中运行的机器人必须在可能受限的感知条件下平衡安全性与效率。虽然控制屏障函数（CBF）通过安全过滤机制提供了理论上的避障保障，但其行为通常由固定参数控制，这些参数在安全场景中可能过于保守，在危险临近时又可能过于宽松。本文提出AlphaAdj——一种从视觉到控制的导航框架，该框架利用第一人称RGB输入实时调整CBF安全过滤器的保守程度。视觉语言模型（VLM）根据当前摄像头视图生成有界标量风险估计值，我们将其映射为动态更新的CBF参数，从而调节安全约束的执行强度。针对实际应用中异步推理和VLM非平凡延迟的问题，我们结合了几何速度感知动态上限机制与陈旧度门控融合策略，并通过轻量级实现方案降低端到端推理开销。我们在多种环境的静态与动态障碍场景中对AlphaAdj进行评估，并与固定参数方案及无上限消融实验进行对比。结果表明，AlphaAdj在保持无碰撞导航的同时，相较于固定参数设置将效率（以路径长度和抵达目标时间为衡量标准）提升最高达18.5%，并较无上限基线方案显著提升了鲁棒性与成功率。

---

### 10. Omni-WorldBench: Towards a Comprehensive Interaction-Centric Evaluation for World Models

- **作者**: Meiqi Wu, Zhixin Cai, Fufangchen Zhao, Xiaokun Feng, Rujing Dang, Bingze Song, Ruitian Tian, Jiashu Zhu, Jiachen Lei, Hao Dou, Jing Tang, Lei Sun, Jiahong Wu, Xiangxiang Chu, Zeming Liu, Kaiqi Huang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.22212v1)
- **发表日期**: 2026-03-23
- **匹配关键词**: 3d reconstruction, 3D reconstruction
- **arXiv**: [2603.22212v1](http://arxiv.org/abs/2603.22212v1)
- **📥 PDF**: 已下载至本地 (`2603.22212v1_Omni-WorldBench_Towards_a_Comprehensive_Interaction-Centric_Evaluation_for_World_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 基于视频的世界模型主要沿着两大范式发展：视频生成与三维重建。然而，现有评估基准要么仅关注生成模型的视觉保真度与文本-视频对齐度，要么依赖静态三维重建指标，本质上忽略了时间动态性。我们认为世界建模的未来在于四维生成——即对空间结构与时间演化的联合建模。在此范式下，核心能力在于交互响应：即准确反映交互行为如何驱动跨时空状态转换的能力。但目前尚无系统性评估这一关键维度的基准框架。为填补这一空白，我们提出Omni-WorldBench——一个专门用于评估四维场景下世界模型交互响应能力的综合性基准。该基准包含两大核心组件：Omni-WorldSuite（覆盖多层级交互与多场景类型的系统性提示集）和Omni-Metrics（基于智能体的评估框架，通过量化交互行为对最终结果及中间状态演化轨迹的因果影响来评估世界建模能力）。我们对跨范式的18个代表性世界模型进行了广泛评估，分析揭示了当前世界模型在交互响应方面的关键局限，为未来研究提供了可操作的见解。Omni-WorldBench将公开发布，以推动交互式四维世界建模领域的发展。

---

## 📌 Poster

*其他相关研究*

---

### 1. DexDrummer: In-Hand, Contact-Rich, and Long-Horizon Dexterous Robot Drumming

- **作者**: Hung-Chieh Fang, Amber Xie, Jennifer Grannen, Kenneth Llontop, Dorsa Sadigh
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.22263v1)
- **发表日期**: 2026-03-23
- **匹配关键词**: exploration
- **arXiv**: [2603.22263v1](http://arxiv.org/abs/2603.22263v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 在机器人领域，实现手内操作、密集接触和长时程灵巧操控仍是一项未解决的挑战。以往关于手部灵巧性的研究通常将这三个挑战分开考虑，未能将其整合到单一复杂任务中。为进一步测试灵巧操控能力，我们提出以击鼓作为灵巧操控的测试平台。击鼓天然融合了所有三项挑战：需要通过手指稳定和调整鼓槌实现手内控制，通过反复敲击鼓面完成密集接触交互，并在切换鼓面和维持节奏演奏时体现长时程协调能力。我们提出DexDrummer——一种在仿真环境中训练并通过仿真到现实迁移的分层以物体为中心的双手机器人击鼓策略。该框架通过结合轨迹规划与残差强化学习修正，降低了纯强化学习的探索难度，实现了鼓面间的快速切换。灵巧操控策略在显式建模手指-鼓槌和鼓槌-鼓面交互的奖励函数指导下，处理密集接触动力学。仿真实验表明，我们的策略能演奏两种音乐风格：多鼓双手机械臂合奏曲目，以及需要更高灵巧性的挑战性技术练习。在仿真双手机械臂任务中，我们灵巧的反应式策略在简单曲目上的F1分数比固定抓握策略提升1.87倍，在困难曲目上提升1.22倍。在现实世界任务中，我们展示了在多鼓配置下的曲目演奏能力。DexDrummer能够以1.0的F1分数演奏训练曲目及其扩展版本。

---

### 2. Closed-Loop Verbal Reinforcement Learning for Task-Level Robotic Planning

- **作者**: Dmitrii Plotnikov, Iaroslav Kolomiets, Dmitrii Maliukov, Dmitrij Kosenkov, Daniia Zinniatullina, Artem Trandofilov, Georgii Gazaryan, Kirill Bogatikov, Timofei Kozlov, Igor Duchinskii, Mikhail Konenkov, Miguel Altamirano Cabrera, Dzmitry Tsetserukou
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.22169v1)
- **发表日期**: 2026-03-23
- **匹配关键词**: navigation
- **arXiv**: [2603.22169v1](http://arxiv.org/abs/2603.22169v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出了一种新的语言强化学习框架，用于在执行不确定性下的移动机器人系统中实现可解释的任务级规划。该框架采用闭环架构，通过与物理环境的交互实现策略的迭代优化。在我们的框架中，可执行的行为树由大型语言模型执行器持续优化，其依据视觉语言模型评判器生成的结构化自然语言反馈——该评判器通过观察物理机器人与执行轨迹产生评估。与传统强化学习不同，语言强化学习中的策略更新直接在符号规划层面进行，无需基于梯度的优化。这使得系统具备透明推理、显式因果反馈和人类可理解的策略演化能力。我们在真实移动机器人上验证了所提框架，该机器人需在执行不确定性下完成多阶段操作与导航任务。实验结果表明，该框架支持可解释的策略改进、对执行失败的闭环适应，并能在物理机器人系统上实现可靠部署。

---

### 3. SafePilot: A Framework for Assuring LLM-enabled Cyber-Physical Systems

- **作者**: Weizhe Xu, Mengyu Liu, Fanxin Kong
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.21523v1)
- **发表日期**: 2026-03-23
- **匹配关键词**: navigation
- **arXiv**: [2603.21523v1](http://arxiv.org/abs/2603.21523v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 大型语言模型（LLM）作为参数规模通常超过百亿的深度学习架构，近年来开始被整合到机器人、工业自动化、自动驾驶系统等多种信息物理系统（CPS）中。其抽象知识与推理能力被应用于路径规划、导航等任务。然而，LLM易产生"幻觉"——即输出内容逻辑连贯但事实错误或情境失当——这一特性给CPS带来了显著挑战，可能导致系统执行不良或不安全行为。为此，本研究致力于通过增强关键属性来确保LLM赋能的CPS可靠性。我们提出SafePilot这一新型分层神经符号框架，该框架能根据属性约束与时间规约为LLM赋能的CPS提供端到端保障。在给定任务及其规约后，SafePilot首先调用配备任务复杂度判别器的分层规划器：若判定任务可管理，则直接交由内置验证机制的LLM任务规划器处理；否则采用分治策略将任务分解为子任务，经独立规划后整合为最终方案。基于LLM的任务规划器将自然语言约束转化为形式化规约，并据此验证LLM输出。若检测到违规，系统会定位缺陷、调整提示词并重新调用LLM，此迭代过程持续至生成有效方案或达到预设阈值。该框架同时支持具有属性约束与时间约束的LLM赋能CPS，并通过两个典型案例研究验证了其有效性与适应性。

---

### 4. HyReach: Vision-Guided Hybrid Manipulator Reaching in Unseen Cluttered Environments

- **作者**: Shivani Kamtikar, Kendall Koe, Justin Wasserman, Samhita Marri, Benjamin Walt, Naveen Kumar Uppalapati, Girish Krishnan, Girish Chowdhary
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.21421v1)
- **发表日期**: 2026-03-22
- **匹配关键词**: motion planning
- **arXiv**: [2603.21421v1](http://arxiv.org/abs/2603.21421v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 随着机器人系统越来越多地在非结构化、杂乱且未经探索的环境中运行，对兼具柔顺性、适应性和精确控制的机械臂需求日益增长。本研究提出了一种实时混合刚柔连续体机械臂系统，专为在复杂环境中实现鲁棒的开世界物体抓取而设计。该系统通过视觉感知与三维场景重建技术，结合形状感知运动规划生成安全轨迹。基于学习的控制器驱动混合臂到达任意目标位姿，充分利用软体段的灵活性，同时保持刚性段的精确性。该系统无需针对特定环境进行重新训练，可直接泛化至新场景。大量真实环境实验表明，该系统在不同杂乱场景中均能保持稳定的抓取性能，误差低于2厘米，凸显了混合机械臂在非结构化环境中实现自适应可靠操作的潜力。

---

### 5. Bayesian Active Object Recognition and 6D Pose Estimation from Multimodal Contact Sensing

- **作者**: Haodong Zheng, Gabriele M. Caddeo, Andrei C. Jalba, Wijnand A. IJsselsteijn, Lorenzo Natale, Raymond H. Cuijpers
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.21410v1)
- **发表日期**: 2026-03-22
- **匹配关键词**: motion planning, exploration
- **arXiv**: [2603.21410v1](http://arxiv.org/abs/2603.21410v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 本文提出一种用于联合物体识别与六维姿态估计的主动触觉探索框架。该方法在贝叶斯推理框架中融合腕部力/力矩传感、GelSight触觉传感与自由空间约束，在主动触觉探索过程中持续维护对物体类别与姿态的置信度估计。通过结合接触与非接触证据，该框架有效降低了联合类别-姿态估计中的歧义性并提升了鲁棒性。为在大规模假设空间实现高效推理，我们采用定制化粒子滤波器，根据新观测数据逐步采样粒子。所得置信度估计进一步用于指导主动探索，在可达性约束下选择信息量最大的后续接触点。为实现有效数据采集，我们开发了运动规划与控制框架，用于规划并执行可行的触觉探索路径，通过触觉伺服处理意外接触及GelSight与物体表面的对准问题。我们在仿真环境及Franka Panda机器人平台上使用11个YCB物体进行评估。实验结果表明，相较于仅使用力/力矩的基线方法，融合触觉与自由空间信息能显著提升识别与姿态估计的准确度与稳定性，同时减少动作执行周期。相关代码、数据集及补充材料将在线发布。

---

### 6. Affordance-Guided Enveloping Grasp Demonstration Toward Non-destructive Disassembly of Pinch-Infeasible Mating Parts

- **作者**: Masaki Tsutsumi, Takuya Kiyokawa, Gen Sako, Kensuke Harada
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.21143v1)
- **发表日期**: 2026-03-22
- **匹配关键词**: affordance
- **arXiv**: [2603.21143v1](http://arxiv.org/abs/2603.21143v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 复杂配合部件的机器人拆卸常使夹持式抓取难以实现，必须采用多指包覆式抓取。然而，在仅依赖二维摄像头数据时，视觉遮挡与几何约束使得示教合适的抓取动作变得困难。为此，我们提出一种可供性引导的遥操作方法，通过物理仿真预生成包覆式抓取方案。这些可供性模板通过反映抓取质量的渐变色进行可视化，以增强操作者的感知能力。仿真实验证明该方法适用于多种部件类型。真实机器人实验验证了基于可供性模板的视觉增强技术能帮助操作者在严苛的视觉与几何约束条件下，有效选择并示教适用于实际拆卸任务的包覆式抓取策略。

---

### 7. 3D-Layout-R1: Structured Reasoning for Language-Instructed Spatial Editing

- **作者**: Haoyu Zhen, Xiaolong Li, Yilin Zhao, Han Zhang, Sifei Liu, Kaichun Mo, Chuang Gan, Subhashree Radhakrishnan
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.22279v1)
- **发表日期**: 2026-03-23
- **匹配关键词**: scene graph
- **arXiv**: [2603.22279v1](http://arxiv.org/abs/2603.22279v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 大型语言模型（LLM）与视觉语言模型（VLM）已展现出卓越的推理能力，但在执行细粒度视觉编辑任务时仍面临空间理解与布局一致性的挑战。本文提出一种结构化推理框架，通过场景图推理实现基于文本条件的空间布局编辑。该模型接收输入场景图与自然语言指令后，在图形结构上进行推理，生成满足文本条件且保持空间连贯性的更新场景图。通过结构化关系表征显式引导推理过程，我们的方法在提升空间关系可解释性的同时增强了控制能力。我们在涵盖排序、空间对齐及房间编辑任务的全新文本引导布局编辑基准上评估了该方法。相较于思维链微调（CoT-SFT）与原始GRPO基线，我们的训练范式在交并比指标上平均提升15%，中心距离误差降低25%。与当前最先进的零样本大型语言模型相比，我们的最优模型实现了高达20%的平均交并比提升，展现出显著增强的空间精度。

---

### 8. CayleyPy-4: AI-Holography. Towards analogs of holographic string dualities for AI tasks

- **作者**: A. Chervov, F. Levkovich-Maslyuk, A. Smolensky, F. Khafizov, I. Kiselev, D. Melnikov, I. Koltsov, S. Kudashev, D. Shiltsov, M. Obozov, S. Krymskii, V. Kirova, E. V. Konstantinova, A. Soibelman, S. Galkin, L. Grunwald, A. Kotov, A. Alexandrov, S. Lytkin, D. Fedoriaka, A. Chevychelov, Z. Kogan, A. Natyrova, L. Cheldieva, O. Nikitina, S. Fironov, A. Vakhrushev, A. Lukyanenko, V. Ilin, D. Gorodkov, N. Bogachev, I. Gaiur, M. Zaitsev, F. Petrov, L. Petrov, T. Gaintseva, A. Gavrilova, M. N. Smirnov, N. Kalinin, A. Khan, K. Jung, H. Mousset, H. Isambert, O. Debeaupuis
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.22195v1)
- **发表日期**: 2026-03-23
- **匹配关键词**: exploration
- **arXiv**: [2603.22195v1](http://arxiv.org/abs/2603.22195v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 这是CayleyPy项目的第四篇论文，该项目将人工智能方法应用于大型图结构的探索。本研究提出该框架下可能存在一种新的离散全息弦对偶形式，并探讨其与人工智能系统及数学领域的关联。许多现代人工智能任务——例如GPT风格语言模型或强化学习系统所处理的问题——可视为预测图上粒子轨迹的直接类比。我们针对一大类凯莱图研究该问题，发现其惊人地允许用离散弦理论进行对偶描述。我们推测此类对偶性可延伸至一系列人工智能系统，从而催生更高效的计算方法。特别地，受AdS/CFT中"复杂度=体积"原理启发，我们提出态的全息弦图像可作为数据嵌入的自然候选方案。

对于对称群S_n的凯莱图，研究结果表明对应的对偶对象是平坦的平面多边形。图的直径等于多边形内部整数点数量乘以n的缩放值。图的顶点可通过全息映射对应多边形内部路径，常规图距离则对应路径下方的面积，从而直接实现"复杂度=体积"范式。我们还在大n极限下发现了连续共形场论与对偶弦存在的证据。通过大量初始案例验证了该图景及对偶性的其他方面。同时，我们提供了新数据集（结合机器学习与传统工具获得），这些数据将有助于在更普遍情形下确立对偶关系。

---

### 9. Seeing is Improving: Visual Feedback for Iterative Text Layout Refinement

- **作者**: Junrong Guo, Shancheng Fang, Yadong Qu, Hongtao Xie
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.22187v1)
- **发表日期**: 2026-03-23
- **匹配关键词**: visual feedback
- **arXiv**: [2603.22187v1](http://arxiv.org/abs/2603.22187v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: GITHUB
  - 链接：https://github.com/FolSpark/VFLM.
- **中文摘要**: 多模态大语言模型（MLLMs）的最新进展使得从自然语言描述自动生成结构化布局成为可能。现有方法通常采用纯代码范式，通过生成代码来表示布局，再由图形引擎渲染生成最终图像。然而，这些方法对渲染后的视觉结果缺乏感知，难以保证可读性与美观性。本文指出视觉反馈是布局生成中的关键因素，并提出视觉反馈布局模型（VFLM）——一个利用视觉反馈进行迭代优化的自我改进框架。VFLM能够执行自适应反思生成，通过视觉信息反思先前问题，并迭代生成输出直至达到满意质量。该框架通过强化学习实现，采用融合OCR准确率的视觉奖励模型。通过仅对最终生成结果进行奖励，我们能够有效激发模型的迭代与反思生成能力。在多个基准测试中的实验表明，VFLM始终优于先进的多模态大语言模型、现有布局模型及纯代码基线方法，证实了视觉反馈对于设计导向多模态大语言模型的关键作用。我们的代码与数据已发布于https://github.com/FolSpark/VFLM。

---

### 10. Cross-Modal Reinforcement Learning for Navigation with Degraded Depth Measurements

- **作者**: Omkar Sawant, Luca Zanatta, Grzegorz Malczyk, Kostas Alexis
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.22182v1)
- **发表日期**: 2026-03-23
- **匹配关键词**: navigation
- **arXiv**: [2603.22182v1](http://arxiv.org/abs/2603.22182v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 本文提出一种跨模态学习框架，利用深度图像与灰度图像的互补信息实现鲁棒导航。我们引入跨模态瓦瑟斯坦自编码器，通过强制跨模态一致性学习共享潜在表征，使系统在深度测量受损时仍能从灰度观测中推断深度相关特征。当深度传感器因光照不足或反光表面等不利条件导致性能下降时，所学习的表征与基于强化学习的策略相结合，可在非结构化环境中实现无碰撞导航。仿真与真实环境实验表明，该方法在深度信息严重退化情况下仍能保持鲁棒性能，并能成功迁移至实际应用场景。

---

