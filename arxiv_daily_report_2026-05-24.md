# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-05-24 08:02

**今日新增**: 8 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 3/8 篇提供

**🌟 Highlight**: 6 篇 | **📌 Poster**: 2 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. GesVLA: Gesture-Aware Vision-Language-Action Model Embedded Representations

- **作者**: Wenxuan Guo, Ziyuan Li, Meng Zhang, Yichen Liu, Yimeng Dong, Chuxi Xu, Yunfei Wei, Ze Chen, Erjin Zhou, Jianjiang Feng
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.22812v1)
- **发表日期**: 2026-05-21
- **匹配关键词**: vision-language-action, vision-language-action model, human-robot interaction, VLA
- **arXiv**: [2605.22812v1](http://arxiv.org/abs/2605.22812v1)
- **📥 PDF**: 已下载至本地 (`2605.22812v1_GesVLA_Gesture-Aware_Vision-Language-Action_Model_Embedded_Representations.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://gwxuan.github.io/GesVLA/.
- **中文摘要**: 视觉-语言-动作（VLA）模型通过统一感知与动作，在通用机器人操作中展现出强大潜力。然而，现有VLA系统主要依赖文本指令，在包含多个相似物体的复杂场景中难以解决空间歧义问题。为突破这一局限，我们引入手势作为并行指令模态，并提出手势感知视觉-语言-动作模型（GesVLA）。该方法将手势特征直接编码至潜在空间，使其同时参与高层推理与低层动作生成，并采用双VLM架构实现手势表征与动作策略的紧密耦合。在数据层面，我们通过将手部模型渲染至真实场景图像，构建了可扩展的手势数据生成流水线。该方案在缩小仿真-真实视觉差距的同时，生成了包含多样化运动模式及对应指向标注的丰富数据。此外，我们采用两阶段训练策略，使模型同时具备手势感知与动作预测能力。我们在多个真实机器人任务上评估了该方法，包括用于验证的受控积木操作任务，以及产品与农产品分拣等更实际的应用场景。实验结果表明，融入手势持续提升了目标定位精度与人机交互效率，尤其在复杂杂乱环境中表现显著。项目主页：https://gwxuan.github.io/GesVLA/。

---

### 2. How can reasoning capability empower the AI copilot robot in endoscopic surgery

- **作者**: Guankun Wang, Long Bai, Hongliang Ren
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.22322v1)
- **发表日期**: 2026-05-21
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2605.22322v1](http://arxiv.org/abs/2605.22322v1)
- **📥 PDF**: 已下载至本地 (`2605.22322v1_How_can_reasoning_capability_empower_the_AI_copilot_robot_in_endoscopic_surgery.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 推理能力显著提升了通用领域中的复杂逻辑推理与机器人决策水平。然而，其在基于视觉-语言-动作（VLA）模型实现的人工智能（AI）副手机器人——特别是应用于内镜手术场景中的潜力尚未得到探索。有效的推理应能使AI副手机器人整合多模态线索、解读手术意图并推断隐藏的组织动态，从而减轻术中的不确定性和外科医生的认知负担。若实施得当，由推理驱动的自主性可将AI副手机器人从被动执行者转变为认知协作者，提升临床实践的精准性、安全性与可持续性。

---

### 3. Action with Visual Primitives

- **作者**: Weilong Guo, Yuchen Wang, Renping Zhou, Yunfeng Zhang, Rui Fang, Yue Meng, Wenda Xu, Yuan He, Gao Huang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.22183v1)
- **发表日期**: 2026-05-21
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2605.22183v1](http://arxiv.org/abs/2605.22183v1)
- **📥 PDF**: 已下载至本地 (`2605.22183v1_Action_with_Visual_Primitives.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型已成为通用机器人操作领域颇具前景的范式。当前架构的常见设计是将语言指令与视觉观测通过单次前向传播映射为动作输出。虽然概念简洁，但这种表述将指令理解、空间场景感知和运动控制纠缠在单一学习目标中。其结果是，动作专家必须隐式地重新学习预训练VLM中已具备的认知与感知能力，这既限制了学习效率也制约了泛化能力。我们提出AVP（基于视觉基元的动作）——一种实现视觉基元中心化接口的端到端架构：VLM推断下一阶段目标并生成视觉基元标记，这些标记通过末端执行器运动学监督来调节流匹配动作专家。在通用抓取放置任务的真实机器人实验中，AVP相较pi_0.5将成功率提升27.61%，并优于其他近期方法，在数据效率、空间组合泛化及物体级迁移方面均展现出持续优势。

---

### 4. TacO: Benchmarking Tactile Sensors for Object Manipulation

- **作者**: Anya Zorin, Zilin Si, Myungsun Park, Junsung Park, Alexiy Buynitsky, Sachin Bhadang, Taejun Park, Sohee John Yoon, Yong-Lae Park, Oliver Kroemer, Zeynep Temel, Michael T. Tolley, Sha Yi, Xiaolong Wang ⭐
  - **高亮作者**: Xiaolong Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.21976v1)
- **发表日期**: 2026-05-21
- **匹配关键词**: contact-rich manipulation, object manipulation
- **arXiv**: [2605.21976v1](http://arxiv.org/abs/2605.21976v1)
- **📥 PDF**: 已下载至本地 (`2605.21976v1_TacO_Benchmarking_Tactile_Sensors_for_Object_Manipulation.pdf`)
- **🔓 开源**: PROJECT_PAGE, CODE
- **中文摘要**: 基于视觉的示教学习在使机器人执行操作任务和高级语义推理方面取得了显著成功，但对于复杂、高接触性操作任务仍显不足。尽管学界普遍认同触觉传感能够提升操作性能，但目前缺乏关于何种触觉传感器最适合特定操作任务的实证指导。本文对机器人操作中的触觉传感器进行了系统性的任务驱动评估，并提出了一种基于操作策略性能的传感器选择与评估框架。我们针对四种不同模态的触觉传感器（视觉、声学、磁学、电阻式）分别训练了操作策略，并在三项任务（未知质量物体的抓取放置、物体重定向、插头插入）中进行测试。针对每项任务，我们分析了传感器特性（如空间分辨率、剪切力感知、触觉表征）及材料固有摩擦系数对任务性能的影响。研究结果表明，触觉信息并非以统一方式普遍有益，其有效性强烈依赖于传感器模态、材料属性及具体操作任务。所有触觉传感器、代码、数据及硬件配置均将在项目网站上公开。

---

### 5. Learning to Evolve: Multi-modal Interactive Fields for Robust Humanoid Navigation in Dynamic Environments

- **作者**: Peifeng Jiang, Hong Liu, Jin Jin, Wenshuai Wang, Xia Li
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.21935v1)
- **发表日期**: 2026-05-21
- **匹配关键词**: gaussian splatting, 3D gaussian splatting, navigation
- **arXiv**: [2605.21935v1](http://arxiv.org/abs/2605.21935v1)
- **📥 PDF**: 已下载至本地 (`2605.21935v1_Learning_to_Evolve_Multi-modal_Interactive_Fields_for_Robust_Humanoid_Navigation_in_Dynamic_Environm.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://ziya-jiang.github.io/MIF-homepage/
- **中文摘要**: 面向人形机器人的安全操作导航需要场景记忆，该记忆需在运动引起的感知失真、环境变化以及交互层面的几何安全约束下保持可靠性。现有的语义建图和场景图系统难以直接应用于此类场景，因为它们通常假设稳定的相机轨迹、静态环境或粗略的物体几何结构。我们提出多模态交互场（MIF），这是一种面向人形机器人的系统，在闭环感知-适应流程中集成了置信度感知的语义3D高斯泼溅、差异触发的空间记忆更新以及任务驱动的几何重建。MIF耦合了三个场：抑制步态模糊的不确定性感知3DGS外观场、维护拓扑记忆的空间场，以及支持操作前交互位姿安全（IPS）的几何场。引入差异检测分数，将运动引起的假阳性变化与持久性变化区分开，并仅更新局部不一致区域。在真实动态办公室环境中的Unitree-G1人形机器人上，与静态场景图记忆相比，MIF将非静态环境中的重定位成功率从12%提升至94%，同时通过特征蒸馏将语义记忆占用减少91.4%，实现实际在线操作。项目页面及代码：https://ziya-jiang.github.io/MIF-homepage/

---

### 6. EvoScene-VLA: Evolving Scene Beliefs Inside the Action Decoder for Chunked Robot Control

- **作者**: Chushan Zhang, Ruihan Lu, Jinguang Tong, Xuesong Li, Yikai Wang, Hongdong Li
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.21862v1)
- **发表日期**: 2026-05-21
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2605.21862v1](http://arxiv.org/abs/2605.21862v1)
- **📥 PDF**: 已下载至本地 (`2605.21862v1_EvoScene-VLA_Evolving_Scene_Beliefs_Inside_the_Action_Decoder_for_Chunked_Robot_Control.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 分块视觉-语言-动作（VLA）策略通过仅依赖当前视觉观测来预测多步机器人控制指令。然而，机器人动作会引起接触、遮挡和物体运动，导致后续决策所依赖的几何结构可能在下一视觉更新到来前发生变化。空间VLA改进了当前帧的几何信息，时间VLA则聚合历史帧信息，但两者均未在分块间维护经动作更新的场景先验。我们主张在控制调用间保持持久化的动作更新场景状态，并由此提出EvoScene-VLA框架。其循环场景前缀机制在分块间传递具有几何感知的场景状态。每次调用视觉语言模型（VLM）时，VLM将当前观测的场景信息与上一分块经动作更新的先验信息相结合；动作解码器同时输出下一动作分块和紧凑的场景更新。该更新成为新的先验信息，当下一调用到来时，VLM将基于新观测对其进行校正。因此，每次控制调用都从融合了近期动作与最新视觉证据的场景先验开始。训练阶段，**场景预测器**提供未来场景令牌目标，**几何锚点**将场景槽与冻结的深度和3D教师模型对齐。部署时这两个模块均被移除。在31项RoboTwin任务中，EvoScene-VLA在固定评估中将平均成功率从87.2%提升至89.1%，在随机评估中从86.1%提升至88.5%。在Galaxea R1-Lite实体机器人上，EvoScene-VLA全面超越所有基线方法。

---

## 📌 Poster

*其他相关研究*

---

### 1. Scout-Assisted Planning for Heterogeneous Robot Teams under Partially Known Environments

- **作者**: Hoang-Dung Bui, Abhish Khanal, Raihan Islam Arnob, Gregory J. Stein
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.22693v1)
- **发表日期**: 2026-05-21
- **匹配关键词**: navigation
- **arXiv**: [2605.22693v1](http://arxiv.org/abs/2605.22693v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 在部分已知环境中导航的自主机器人团队，当地面机器人遭遇仅在实际通行时才能发现的阻塞道路时，会面临代价高昂的折返问题。为此我们提出侦察辅助规划框架——一种异构规划方案，其中侦察无人机主动收集环境信息以优化无人地面车辆的导航路径。为将侦察聚焦于最具影响力的路段，我们提出基于信息增益的动作剪枝方法，通过评估候选侦察动作对地面机器人行为的预期影响进行评分。由于精确计算信息增益动作剪枝的代价过高，我们开发了基于图神经网络的模型，该模型可直接从图结构和信念状态预测信息增益值，在不牺牲解质量的前提下将规划时间压缩至实时水平。在三种环境类型上的实验表明，采用信息增益动作剪枝的侦察辅助规划相比加拿大旅行者问题基线可降低地面机器人31.9-37.7%的行驶成本，且相较于基于邻近度的侦察引导方案额外提升8-14%的性能，证实了基于信息增益原则的侦察引导在实际部署中既更高效又具备计算可行性。

---

### 2. A Visitation Grid for Complete Coverage Foraging in Robot Swarms

- **作者**: Qi Arturo Gonzalez, Yifeng Gao, Li Zhang, Qi Lu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.21947v1)
- **发表日期**: 2026-05-21
- **匹配关键词**: exploration
- **arXiv**: [2605.21947v1](http://arxiv.org/abs/2605.21947v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 在大型未知环境中，自主机器人群体对稀疏资源的完整收集仍是一个具有挑战性的问题。以往研究表明，任务总时间中有相当一部分消耗在收集的最后阶段，此时仅剩少量随机散落的资源。因此，现有群体觅食算法（搜索与收集）大多侧重于在有限时间窗口内收集大部分资源，而非提升收集全部资源的末期效率。本文提出一种基于网格的随机觅食策略，通过显著减少冗余访问来加速后期收集。未知搜索区域被划分为网格地图，并由轻量级中央服务器维护。为保持可扩展性，机器人与服务器均在有限内存与计算资源下运行。服务器根据机器人报告的位置更新网格级访问次数，生成探索密度的全局估计。每次觅食任务中，机器人从局部3×3网格邻域内以概率方式选择访问次数最少的区域作为下一搜索目标，从而在保持随机性的同时引导探索偏向未充分访问区域。大量仿真实验表明，该策略始终优于经典的中心放置基线觅食算法（CPFA）。与CPFA相比，本方法将总收集时间缩短最多33%，并在任务末期阶段将收集效率提升超过48%。这些结果表明，该策略对机器人群体近乎完整与完整的资源收集具有鲁棒性、灵活性与可扩展性，可作为有限机载资源下随机群体觅食方法的通用增强方案。

---

