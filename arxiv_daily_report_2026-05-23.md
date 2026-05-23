# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-05-23 08:02

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 5/20 篇提供

**🌟 Highlight**: 20 篇 | **📌 Poster**: 0 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. GesVLA: Gesture-Aware Vision-Language-Action Model Embedded Representations

- **作者**: Wenxuan Guo, Ziyuan Li, Meng Zhang, Yichen Liu, Yimeng Dong, Chuxi Xu, Yunfei Wei, Ze Chen, Erjin Zhou, Jianjiang Feng
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.22812v1)
- **发表日期**: 2026-05-21
- **匹配关键词**: VLA, vision-language-action model, human-robot interaction, vision-language-action
- **arXiv**: [2605.22812v1](http://arxiv.org/abs/2605.22812v1)
- **📥 PDF**: 已下载至本地 (`2605.22812v1_GesVLA_Gesture-Aware_Vision-Language-Action_Model_Embedded_Representations.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://gwxuan.github.io/GesVLA/.
- **中文摘要**: 视觉-语言-动作（VLA）模型通过统一感知与动作，在通用机器人操作领域展现出巨大潜力。然而，现有VLA系统主要依赖文本指令，在包含多个相似物体的复杂场景中难以解决空间歧义问题。为突破这一局限，我们引入手势作为并行指令模态，并提出手势感知视觉-语言-动作模型（GesVLA）。该方法将手势特征直接编码至潜在空间，使其同时参与高层推理与低层动作生成，并采用双VLM架构实现手势表征与动作策略的紧密耦合。在数据层面，我们通过将手部模型渲染至真实场景图像，构建了可扩展的手势数据生成流水线。该方案在缩小仿真-真实视觉差异的同时，生成了包含多样化运动模式及对应指向标注的丰富数据。此外，我们采用两阶段训练策略，使模型同时具备手势感知与动作预测能力。我们在多个真实机器人任务中评估该方法，包括用于验证的受控积木操作任务，以及产品与农产品分拣等更实际的应用场景。实验结果表明，融入手势能持续提升目标定位精度与人机交互效率，尤其在复杂杂乱环境中表现显著。项目页面：https://gwxuan.github.io/GesVLA/。

---

### 2. How can reasoning capability empower the AI copilot robot in endoscopic surgery

- **作者**: Guankun Wang, Long Bai, Hongliang Ren
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.22322v1)
- **发表日期**: 2026-05-21
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2605.22322v1](http://arxiv.org/abs/2605.22322v1)
- **📥 PDF**: 已下载至本地 (`2605.22322v1_How_can_reasoning_capability_empower_the_AI_copilot_robot_in_endoscopic_surgery.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 推理能力显著提升了通用领域中的复杂逻辑推理与机器人决策能力。然而，在基于视觉-语言-动作（VLA）模型实现的人工智能（AI）副驾驶机器人中，其在内镜手术领域的潜力尚未得到探索。有效的推理应使AI副驾驶机器人能够整合多模态线索、解读手术意图并推断隐藏的组织动态，从而减轻术中不确定性和外科医生的认知负担。若实施得当，推理驱动的自主性可将AI副驾驶机器人从被动执行者转变为认知协作者，提升临床实践中的精准性、安全性与可持续性。

---

### 3. Action with Visual Primitives

- **作者**: Weilong Guo, Yuchen Wang, Renping Zhou, Yunfeng Zhang, Rui Fang, Yue Meng, Wenda Xu, Yuan He, Gao Huang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.22183v1)
- **发表日期**: 2026-05-21
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2605.22183v1](http://arxiv.org/abs/2605.22183v1)
- **📥 PDF**: 已下载至本地 (`2605.22183v1_Action_with_Visual_Primitives.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型已成为通用机器人操作领域颇具前景的范式。当前架构的常见设计是将语言指令与视觉观测映射为单次前向传播中的动作输出。尽管概念上简洁，但这种表述将指令理解、空间场景感知和运动控制纠缠在单一学习目标中。因此，动作专家必须隐式地重新学习预训练VLM中已具备的认知与感知能力，这既限制了学习效率也制约了泛化能力。我们提出AVP（基于视觉基元的动作）——一种实现视觉基元中心化接口的端到端架构：VLM推断下一阶段目标并生成视觉基元标记，这些标记通过末端执行器运动学监督来调节流匹配动作专家。在通用抓取放置任务的真实机器人实验中，AVP相比pi_0.5将成功率提升27.61%，并优于其他近期方法，在数据效率、空间组合泛化及物体级迁移方面均取得一致性增益。

---

### 4. TacO: Benchmarking Tactile Sensors for Object Manipulation

- **作者**: Anya Zorin, Zilin Si, Myungsun Park, Junsung Park, Alexiy Buynitsky, Sachin Bhadang, Taejun Park, Sohee John Yoon, Yong-Lae Park, Oliver Kroemer, Zeynep Temel, Michael T. Tolley, Sha Yi, Xiaolong Wang ⭐
  - **高亮作者**: Xiaolong Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.21976v1)
- **发表日期**: 2026-05-21
- **匹配关键词**: object manipulation, contact-rich manipulation
- **arXiv**: [2605.21976v1](http://arxiv.org/abs/2605.21976v1)
- **📥 PDF**: 已下载至本地 (`2605.21976v1_TacO_Benchmarking_Tactile_Sensors_for_Object_Manipulation.pdf`)
- **🔓 开源**: CODE, PROJECT_PAGE
- **中文摘要**: 基于视觉的示范学习在使机器人执行操作任务和高层语义推理方面取得了显著成功，但在处理复杂的、高接触性操作任务时仍显不足。尽管学界普遍认为触觉传感能够提升操作性能，但目前缺乏关于哪种触觉传感器最适合特定操作任务的实证指导。本文对机器人操作中的触觉传感器进行了系统性的、任务驱动的评估，并提出了一种基于操作策略性能的传感器选择与评估框架。我们针对四种不同模态的触觉传感器（视觉、声学、磁学、电阻式）分别训练了操作策略，并应用于三项任务：未知质量物体的抓取与放置、物体重新定向以及插头插入。针对每项任务，我们分析了传感器特性（如空间分辨率、剪切力感知、触觉表征）及材料固有摩擦对任务性能的影响。研究结果表明，触觉信息并非以统一方式普遍有益，其有效性强烈依赖于传感器模态、材料特性以及具体操作任务。所有触觉传感器、代码、数据及硬件设置将在项目网站上公开提供。

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
- **中文摘要**: 面向人形机器人的安全操作导航需要场景记忆，该记忆需在运动引起的感知畸变、环境变化以及交互层面的几何安全约束下保持可靠性。现有语义建图和场景图系统难以直接部署于此类场景，因其通常假设稳定的相机轨迹、静态环境或粗略的物体几何结构。我们提出多模态交互场（MIF）——一种面向人形机器人的闭环感知-自适应系统，该系统融合了置信度感知的语义3D高斯泼溅、差异触发的空间记忆更新以及任务驱动的几何重建。MIF耦合三个场：抑制步态模糊的不确定性感知3DGS外观场、维持拓扑记忆的空间场，以及支持操作前交互位姿安全的几何场。通过引入差异检测分数，将运动引起的假阳性变化与持续性变化分离，仅更新局部不一致区域。在真实动态办公室环境中使用宇树G1人形机器人进行测试，与静态场景图记忆相比，MIF在非静态环境中的重定位成功率从12%提升至94%，同时通过特征蒸馏将语义记忆占用减少91.4%，实现实际在线运行。项目页面及代码：https://ziya-jiang.github.io/MIF-homepage/

---

### 6. EvoScene-VLA: Evolving Scene Beliefs Inside the Action Decoder for Chunked Robot Control

- **作者**: Chushan Zhang, Ruihan Lu, Jinguang Tong, Xuesong Li, Yikai Wang, Hongdong Li
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.21862v1)
- **发表日期**: 2026-05-21
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2605.21862v1](http://arxiv.org/abs/2605.21862v1)
- **📥 PDF**: 已下载至本地 (`2605.21862v1_EvoScene-VLA_Evolving_Scene_Beliefs_Inside_the_Action_Decoder_for_Chunked_Robot_Control.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 分块视觉-语言-动作（VLA）策略通过仅依赖当前视觉观测来预测多步机器人控制指令。然而，机器人动作会引起接触、遮挡和物体运动，导致后续决策所依赖的几何结构在下一视觉更新到来前可能发生变化。空间型VLA能改进当前帧的几何信息，时序型VLA能聚合历史帧信息，但两者均未能在动作块间维持经动作更新的场景先验。我们提出应在控制调用间保持持久化的动作更新场景状态，并由此构建EvoScene-VLA框架。其循环场景前缀机制可在动作块间传递包含几何感知的场景状态。每次视觉语言模型（VLM）调用时，VLM将当前观测的场景信息与上一动作块产生的动作更新先验进行融合；动作解码器同时输出下一动作块和紧凑的场景更新。该更新成为新的先验，在下一次调用时由VLM根据新观测进行校正。因此，每次控制调用都从融合了近期动作与最新视觉证据的场景先验开始。训练阶段，**场景预测器**提供未来场景标记目标，**几何锚点**将场景槽与冻结的深度和3D教师模型对齐。部署时这两个模块被移除。在31项RoboTwin任务中，EvoScene-VLA在固定评估中将平均成功率从87.2%提升至89.1%，在随机评估中从86.1%提升至88.5%。在Galaxea R1-Lite实体机器人上，EvoScene-VLA全面超越所有基线方法。

---

### 7. PointACT: Vision-Language-Action Models with Multi-Scale Point-Action Interaction

- **作者**: Shizhe Chen, Paul Pacaud, Cordelia Schmid
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.21414v1)
- **发表日期**: 2026-05-20
- **匹配关键词**: vision-language-action model, VLA, vision-language-action
- **arXiv**: [2605.21414v1](http://arxiv.org/abs/2605.21414v1)
- **📥 PDF**: 已下载至本地 (`2605.21414v1_PointACT_Vision-Language-Action_Models_with_Multi-Scale_Point-Action_Interaction.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型通过利用大规模预训练的视觉-语言骨干网络，在通用机器人操作任务中展现出巨大潜力。然而，现有VLA模型主要依赖二维视觉表征，这限制了其对精细几何结构与空间定位的推理能力——而这些能力正是三维环境中实现精准鲁棒操作的关键。本文提出PointACT，一种双系统三维感知VLA策略，将分层三维点云表征直接集成到动作解码过程中。PointACT采用多尺度点-动作交互机制与高效瓶颈窗口自注意力，使动态动作标记能够密集关注局部几何细节与全局场景结构。我们在LIBERO和RLBench基准上评估PointACT，并将其与单系统及双系统VLA基线（包括增强点云输入的变体）进行系统对比。PointACT在两个基准上均实现一致提升：在具有挑战性的RLBench-10Tasks套件中，相较于最先进的预训练VLA，成功率提升10%；当冻结视觉-语言骨干网络并从头训练动作专家模块时，性能增益更为显著。大量消融实验表明，将分层三维几何结构与预训练二维语义表征紧密耦合，是实现鲁棒且具空间感知的机器人控制的关键。我们的研究结果同时凸显了预训练三维表征对三维感知VLA策略的潜在价值。

---

### 8. Humanoid Whole-Body Manipulation via Active Spatial Brain and Generalizable Action Cerebellum

- **作者**: Zhizhao Liang, Yi-Lin Wei, Xuhang Chen, Mu Lin, Yi-Xiang He, Zhexi Luo, Jun-Hui Liu, Kun-Yu Lin, Wei-Shi Zheng
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.21133v1)
- **发表日期**: 2026-05-20
- **匹配关键词**: whole-body manipulation
- **arXiv**: [2605.21133v1](http://arxiv.org/abs/2605.21133v1)
- **📥 PDF**: 已下载至本地 (`2605.21133v1_Humanoid_Whole-Body_Manipulation_via_Active_Spatial_Brain_and_Generalizable_Action_Cerebellum.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 本文探索了空间感知的人形全身操控任务。与桌面场景相比，该任务面临两大关键挑战：1）在具有复杂空间关系的三维环境中，空间理解极具挑战性；2）动作生成难以泛化，有限且昂贵的真实机器人数据限制了数据驱动模型的泛化能力。为解决这些问题，我们提出了一种可泛化的人形移动操控框架，该框架利用多智能体大模型的空间感知与动作生成能力。具体而言，该框架包含两个组件：用于主动空间感知与决策的主动空间大脑，以及用于生成可执行机器人动作的可泛化动作小脑。前者主动感知空间场景，并对任务规划与子任务分解进行决策；后者基于前者的决策生成可执行的机器人动作，无需依赖特定任务的真实机器人数据。为评估该框架，我们从两个维度设计了一系列空间操控任务：评估空间感知与理解能力，以及评估真实机器人任务表现。实验结果表明，该框架在多样化任务与环境中均展现出优异性能。

---

### 9. WiXus: A Wheeled-Legged Robot with Wire-Driven Environmental Utilizing to Integrate Mobility and Manipulation

- **作者**: Shintaro Inoue, Kento Kawaharazuka, Temma Suzuki, Sota Yuzaki, Kei Okada
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.20932v1)
- **发表日期**: 2026-05-20
- **匹配关键词**: object manipulation
- **arXiv**: [2605.20932v1](http://arxiv.org/abs/2605.20932v1)
- **📥 PDF**: 已下载至本地 (`2605.20932v1_WiXus_A_Wheeled-Legged_Robot_with_Wire-Driven_Environmental_Utilizing_to_Integrate_Mobility_and_Mani.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 轮腿式机器人通过在足部安装轮子，并协调轮驱动与腿驱动实现高机动性。这类机器人最初仅作为纯运动平台开发，因此其腿部结构无法在运动之外承担其他功能，例如物体操作或工具使用。本文针对如何通过外部身体支撑将腿部从运动功能中解放出来，从而挖掘其潜在任务执行能力的问题展开研究。为此，我们提出并开发了一种新型机器人WiXus，该机器人融合了轮腿机构与利用外部环境的线驱动机构。所开发的WiXus不仅能够通过轮腿驱动实现平面运动，还能通过协调线驱动与轮腿驱动完成悬崖攀爬等三维机动。此外，通过线驱动悬吊机身，WiXus成功将腿部重新用作机械臂，执行物体操作（如救援玩具狗）和工具使用（如用修枝剪采摘苹果模型）。本研究证明，利用线驱动与环境交互的方法是一种拓展轮腿式机器人操作域的新设计原则。

---

### 10. Mobile UMI: Cross-View Diffusion Policy with Decoupled Kinematics for Mobile Manipulation

- **作者**: Haoran Huang, Haonan Dong, Huixu Dong
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.20894v1)
- **发表日期**: 2026-05-20
- **匹配关键词**: mobile manipulation, diffusion policy, navigation
- **arXiv**: [2605.20894v1](http://arxiv.org/abs/2605.20894v1)
- **📥 PDF**: 已下载至本地 (`2605.20894v1_Mobile_UMI_Cross-View_Diffusion_Policy_with_Decoupled_Kinematics_for_Mobile_Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 移动式模仿学习在便携式演示界面上面临两个相互耦合的瓶颈：运动污染的动作标签，以及在持续移动基座上由推理引发的执行延迟。近期腕戴式接口降低了桌面数据采集的成本，但单一腕部视角无法捕捉基座导航所需的全局上下文。添加身体安装式摄像头会将人类行走与手部运动纠缠在一起。同时，生成式策略引入了数百毫秒的推理延迟，在此期间基座会越过预测路径点，迫使动作拼接处进行反向修正。本文提出Mobile UMI——一种无需硬件的演示框架，通过三个组件解决上述两个瓶颈。首先，双摄像头采集系统在无机器人参与的情况下，记录以胸部为中心的全局上下文和以手腕为中心的局部交互。其次，基于ChArUco的一次性空间锚点统一了胸部与手部的视觉惯性坐标系；随后将手部姿态相对于胸部重新表达，以提取解耦的SE(3)操作轨迹和SE(2)基座轨迹。第三，异步滚动时域执行器执行在线状态匹配：每个生成的动作块与当前物理姿态重新对齐，使过期的路径点在执行前被丢弃。该系统在四项长时域家庭任务上进行了评估，每项任务100次试验的平均成功率达83.8%。与ACT和扩散策略的对比控制实验表明，仅使用胸部相对标签即可缩小大部分差距；在线状态匹配则弥补了剩余差距。这些结果表明，在测试条件下的移动式模仿学习中，显式运动学分解结合状态级延迟对齐，无需对底层策略类别进行架构修改即可提供有效解决方案。

---

### 11. AwareVLN: Reasoning with Self-awareness for Vision-Language Navigation

- **作者**: Wenxuan Guo, Xiuwei Xu, Yichen Liu, Xiangyu Li, Hang Yin, Huangxing Chen, Wenzhao Zheng, Jianjiang Feng, Jie Zhou, Jiwen Lu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.22816v1)
- **发表日期**: 2026-05-21
- **匹配关键词**: VLN, vision-and-language navigation, navigation
- **arXiv**: [2605.22816v1](http://arxiv.org/abs/2605.22816v1)
- **📥 PDF**: 已下载至本地 (`2605.22816v1_AwareVLN_Reasoning_with_Self-awareness_for_Vision-Language_Navigation.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://gwxuan.github.io/AwareVLN/.
- **中文摘要**: 视觉与语言导航（VLN）要求智能体在视觉环境中将语言指令与自身移动相结合。尽管现有最先进方法利用视觉语言模型（VLM）的推理能力进行端到端动作预测，但这些方法往往缺乏对智能体、指令与场景之间关系的显式且可解释的理解。相反，为启发式规划显式构建场景地图虽具直观吸引力，却依赖额外的3D传感器，并阻碍大规模视觉语言预训练。为弥合这一差距，我们提出AwareVLN——一种新型框架，通过赋予导航模型自我感知推理机制，使其能够以完全端到端且数据驱动的方式理解智能体状态与任务进度。本方法包含两项关键创新：（1）结构推理模块，促进空间导向与任务导向的自我感知；（2）配备进度划分的自动数据引擎，实现高效训练。在Habitat模拟器中多个数据集上的大量实验表明，我们的AwareVLN显著优于先前最先进的视觉语言导航方法。项目页面：https://gwxuan.github.io/AwareVLN/。

---

### 12. Sensor2Sensor: Cross-Embodiment Sensor Conversion for Autonomous Driving

- **作者**: Jiahao Wang, Bo Sun, Yijing Bai, Vincent Casser, Songyou Peng, Zehao Zhu, Meng-Li Shih, Xander Masotto, Shih-Yang Su, Kanaad V Parvate, Tiancheng Ge, Linn Bieske, Dragomir Anguelov, Mingxing Tan, Chiyu Max Jiang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.22809v1)
- **发表日期**: 2026-05-21
- **匹配关键词**: gaussian splatting
- **arXiv**: [2605.22809v1](http://arxiv.org/abs/2605.22809v1)
- **📥 PDF**: 已下载至本地 (`2605.22809v1_Sensor2Sensor_Cross-Embodiment_Sensor_Conversion_for_Autonomous_Driving.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 自动驾驶系统（ADS）的稳健训练与验证需要海量且多样化的数据集。自动驾驶车队采集的专有数据虽具有高保真度，但在规模、传感器配置多样性、地理覆盖范围及长尾行为场景方面存在局限。相比之下，来自行车记录仪等野外数据源具有庞大的规模和丰富的多样性，能够捕捉关键的长尾场景和新环境。然而，这些非结构化的野外视频数据与需要结构化多模态传感器输入进行验证和训练的ADS系统不兼容。为弥合这一数据鸿沟，我们提出Sensor2Sensor——一种新型生成式建模范式，可将野外单目行车记录仪视频转化为包含多视角相机图像与激光雷达点云的高保真多模态传感器套件（自动驾驶日志）。核心挑战在于缺乏成对训练数据。我们通过4D高斯泼溅（4DGS）重建与新视角渲染技术，将真实自动驾驶日志转换为行车记录仪风格视频来解决该问题。Sensor2Sensor随后采用扩散架构执行生成式转换。我们对生成传感器数据的保真度和真实感进行了全面的定量评估。通过将具有挑战性的野外互联网视频和行车记录仪影像转化为逼真的多模态数据格式，我们验证了Sensor2Sensor的实际应用价值，进一步为自动驾驶开发解锁了海量外部数据源。

---

### 13. From Abstraction to Instantiation: Learning Behavioral Representation for Vision-Language-Action Model

- **作者**: Bing Hu, Zaijing Li, Rui Shao, Junda Chen, April Hua Liu, Wei-Shi Zheng, Liqiang Nie
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.22671v1)
- **发表日期**: 2026-05-21
- **匹配关键词**: vision-language-action model, VLA, vision-language-action
- **arXiv**: [2605.22671v1](http://arxiv.org/abs/2605.22671v1)
- **📥 PDF**: 已下载至本地 (`2605.22671v1_From_Abstraction_to_Instantiation_Learning_Behavioral_Representation_for_Vision-Language-Action_Mode.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型在分布偏移场景下常出现性能退化，因其难以在不同环境中学习泛化的行为表征。现有方法虽尝试通过以动作为中心的潜变量构建行为表征，但受限于短时域碎片化与静态执行对齐，导致复杂场景中的行为不一致。针对这些局限，我们提出\textbf{BehaviorVLA}框架，通过学习时序连贯的行为表征实现鲁棒操控。该框架包含两个对称组件：（1）\textbf{视觉运动行为编码器（VBE）}，采用基于因果Mamba的架构将长时域轨迹信息聚合为统一行为表征；（2）\textbf{相位条件行为解码器（PBD）}，通过动态对齐任务级先验与实时执行进度，将该表征解码为精确动作。在RoboTwin 2.0、LIBERO和CALVIN上的实验分别取得了58\%、98\%和4.36（平均长度）的最新成功率。值得注意的是，在真实世界的仿真到现实迁移中，BehaviorVLA仅使用50\%的演示数据即达到OpenVLA-OFT的性能，展现出卓越的数据效率与泛化能力。

---

### 14. SpaceDG: Benchmarking Spatial Intelligence under Visual Degradation

- **作者**: Xiaolong Zhou, Yifei Liu, Ziyang Gong, Jiarui Li, Qiyue Zhao, Muyao Niu, Yuanyuan Gao, Le Ma, Xue Yang, Hongjie Zhang, Zhihang Zhong
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.22536v1)
- **发表日期**: 2026-05-21
- **匹配关键词**: 3D gaussian splatting, gaussian splatting
- **arXiv**: [2605.22536v1](http://arxiv.org/abs/2605.22536v1)
- **📥 PDF**: 已下载至本地 (`2605.22536v1_SpaceDG_Benchmarking_Spatial_Intelligence_under_Visual_Degradation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 多模态大语言模型（MLLMs）在空间智能领域取得了快速进展，然而现有的空间推理基准大多假设视觉输入是完美的，忽视了实际部署中常见的图像退化问题，如运动模糊、低光照、恶劣天气、镜头畸变和压缩伪影。这引发了一个根本性问题：当视觉观测不完美时，当前MLLMs的空间智能有多鲁棒？为回答这一问题，我们提出了SpaceDG——首个面向退化感知空间理解的大规模数据集。该数据集基于一个物理驱动的退化合成引擎构建，该引擎将退化形成过程嵌入到3D高斯泼溅（3DGS）渲染中，实现了九种退化类型的逼真模拟。最终数据集包含来自近1000个室内场景的约100万组问答对。我们进一步引入了SpaceDG-Bench，这是一个经人工验证的基准，涵盖11个推理类别和9种视觉退化类型的1102个问题，生成了超过1万个VQA实例。对25个开源和闭源MLLMs的评估表明，视觉退化会持续且显著地损害空间推理能力，暴露出关键的鲁棒性差距。最后，我们证明在SpaceDG上进行微调能显著提升退化鲁棒性，甚至在退化条件下超越人类表现，同时不降低对清晰图像的推理性能，这凸显了退化感知训练对实现鲁棒空间智能的潜力。

---

### 15. WorldKV: Efficient World Memory with World Retrieval and Compression

- **作者**: Jung Yi, Minjae Kim, Paul Hyunbin Cho, Wooseok Jang, Sangdoo Yun, Seungryong Kim
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.22718v1)
- **发表日期**: 2026-05-21
- **匹配关键词**: VLA
- **arXiv**: [2605.22718v1](http://arxiv.org/abs/2605.22718v1)
- **📥 PDF**: 已下载至本地 (`2605.22718v1_WorldKV_Efficient_World_Memory_with_World_Retrieval_and_Compression.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://cvlab-kaist.github.io/WorldKV/
- **中文摘要**: 自回归视频扩散模型已实现实时、基于动作条件的世界生成。然而，维持一个持久的世界——即重新访问先前视角时能生成一致内容——仍是一个未解决的问题。全KV缓存注意力机制能保持这种一致性，但打破了实时性限制：内存占用和注意力成本随生成长度线性增长。滑动窗口推理恢复了吞吐量，但丢弃了长期一致性。我们提出WorldKV，一个无需训练的框架，包含两个组件：世界检索与世界压缩。世界检索将驱逐的KV缓存块存储在GPU/CPU内存中，并通过相机/动作对应关系选择性检索场景相关块，将其重新插入原生注意力窗口而无需重新编码。世界压缩通过关键帧间的键-键相似性剪枝每个块中的冗余令牌，在固定预算下将每块存储减半，以容纳两倍以上的历史信息。在Matrix-Game-2.0和LingBot-World-Fast上，WorldKV在全KV内存保真度下匹配或超越其性能，吞吐量约为其两倍，且无需任何微调即可与基于内存训练的基线方法相媲美。项目页面：https://cvlab-kaist.github.io/WorldKV/

---

### 16. Pre-VLA: Preemptive Runtime Verification for Reliable Vision-Language-Action and World-Model Rollouts

- **作者**: Zhen Sun, Yongjian Guo, Haoran Sun, Luqiao Wang, Wei Lu, Jiachi Ji, Shengzhe Ji, Junwu Xiong, Zhijun Meng
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.22446v1)
- **发表日期**: 2026-05-21
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2605.22446v1](http://arxiv.org/abs/2605.22446v1)
- **📥 PDF**: 已下载至本地 (`2605.22446v1_Pre-VLA_Preemptive_Runtime_Verification_for_Reliable_Vision-Language-Action_and_World-Model_Rollouts.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 尽管大型视觉-语言-动作（VLA）模型和生成式世界模型（WM）推动了长时域具身智能的发展，但其实际部署仍面临基于学习的动作生成中不确定性的挑战。低质量动作可能在执行过程中导致物理故障，或引发具有冗余渲染成本的误导性世界模型推演。为解决该问题，我们提出Pre-VLA——一种统一的运行时验证架构，可在物理执行或世界模型想象之前执行先发制人的动作有效性评估。Pre-VLA采用高效多模态主干网络，结合模态感知池化与轻量级双分支头部结构，为候选动作片段预测安全置信度与基于评论家的优势得分。为应对严重类别不平衡与不稳定的边界决策问题，我们通过结合焦点分类、优势回归与软阈值校准的多任务目标训练Pre-VLA。在部署阶段，双模式先发制人重采样调度器可在有限计算预算下过滤低质量动作并触发自适应重采样。在LIBERO基准上的实验表明，相较于RynnVLA-002，Pre-VLA将四个套件的平均闭环成功率从30.79%提升至37.62%，减少了任务执行步数，实现了每个动作片段183.9毫秒的平均前向验证时间，并缓解了世界模型推演中的误差累积。

---

### 17. Diffusion-guided Generalizable Enhancer for Urban Scene Reconstruction

- **作者**: Henry Che, Jingkang Wang, Yun Chen, Ze Yang, Sivabalan Manivasagam, Raquel Urtasun
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.22420v1)
- **发表日期**: 2026-05-21
- **匹配关键词**: neural rendering
- **arXiv**: [2605.22420v1](http://arxiv.org/abs/2605.22420v1)
- **📥 PDF**: 已下载至本地 (`2605.22420v1_Diffusion-guided_Generalizable_Enhancer_for_Urban_Scene_Reconstruction.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 从真实观测数据中重建城市场景已成为自动驾驶开发与测试的重要工具。尽管现有神经渲染方法能在记录轨迹上实现高保真渲染，但在大视角偏移下其质量显著下降，限制了其在闭环仿真中的应用。近期研究显示，利用扩散模型可提升这些挑战性视角下的渲染质量，并将改进成果蒸馏回三维表征中。然而，这些方法通常需要昂贵的逐场景优化，且蒸馏后的表征仍显脆弱，难以泛化至有限合成视角之外。为解决上述局限，我们提出GenRe——一种面向城市场景重建的扩散引导型通用增强器。GenRe以任意预训练的三维高斯表征为输入，可在数分钟内修复其缺陷。通过跨场景学习蒸馏生成先验，GenRe能高效生成鲁棒且高保真的表征，可靠泛化至未见过的挑战性视角（如车道变更）。实验表明，GenRe在质量与效率上均优于现有方法，并惠及多项下游任务，为自动驾驶提供鲁棒且可扩展的传感器仿真能力。

---

### 18. Spatial Memory for Out-of-Vision Manipulation in Vision-Language-Action

- **作者**: Pengteng Li, Weiyu Guo, He Zhang, Tiefu Cai, Xiao He, Yandong Guo, Hui Xiong
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.22283v1)
- **发表日期**: 2026-05-21
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2605.22283v1](http://arxiv.org/abs/2605.22283v1)
- **📥 PDF**: 已下载至本地 (`2605.22283v1_Spatial_Memory_for_Out-of-Vision_Manipulation_in_Vision-Language-Action.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出了SOMA，一种面向视觉-语言-动作（VLA）模型中视域外操作的空间记忆框架。现有大多数VLA模型隐式假设任务相关物体始终可见，导致当目标超出相机视野时产生脆弱且被动的行为。SOMA通过为VLA配备持久性空间记忆来解决这一局限——该记忆基于可移动头部相机获取的多视角观测构建，使模型能够超越当前视觉截锥体进行推理。该框架包含三个组件：空间记忆构建模块通过扫描将角度级观测聚合为统一的空间语义表征；动态记忆精炼模块随时间维持全局一致性；上下文记忆检索模块在操作过程中激活与指令相关的空间线索。我们在五项具有挑战性的真实世界视域外操作任务上评估SOMA，包括目标物体初始不可见的多步骤和双臂场景。实验结果表明，SOMA不仅提升了任务成功率，还诱导出性质不同的操作行为：更快的目标定位、更少的视角搜索，以及在部分可观测条件下近乎单次抓取的成功率。在RoboCasa GR1和SimplerEnv上的额外实验进一步验证了SOMA记忆设计在传统完全可观测设置下的有效性。代码即将开源。

---

### 19. Flow-based Gaussian Splatting for Continuous-Scale Remote Sensing Image Super-Resolution

- **作者**: Jiangwei Mo, Xi Lu, Hanlin Wu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.22147v1)
- **发表日期**: 2026-05-21
- **匹配关键词**: gaussian splatting
- **arXiv**: [2605.22147v1](http://arxiv.org/abs/2605.22147v1)
- **📥 PDF**: 已下载至本地 (`2605.22147v1_Flow-based_Gaussian_Splatting_for_Continuous-Scale_Remote_Sensing_Image_Super-Resolution.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 高分辨率遥感图像（RSIs）对地球观测应用至关重要，但其获取常受限于传感器限制和成本。近年来，生成式超分辨率（SR）方法，尤其是扩散模型，取得了显著进展。然而，这些方法通常需要40至1000步的缓慢迭代推理，且在连续尺度超分辨率设置中灵活性有限。为解决这些问题，我们提出FlowGS——一种面向遥感图像任意尺度超分辨率的生成式重建框架。FlowGS建模高分辨率与低分辨率图像间的高频细节表征，并通过基于捷径一致性约束的流匹配（FM）学习从噪声到细节先验的连续概率流，从而降低生成复杂度并提升推理效率。此外，我们采用二维高斯泼溅构建连续特征场，实现任意查询位置的灵活重建。实验结果表明，在连续尺度与固定尺度超分辨率设置中，FlowGS均能提供与现有方法相当的感知质量，同时显著提升推理效率。

---

### 20. LVDrive: Latent Visual Representation Enhanced Vision-Language-Action Autonomous Driving Model

- **作者**: Xiaodong Mei, Diankun Zhang, Hongwei Xie, Guang Chen, Hangjun Ye, Dan Xu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.22089v1)
- **发表日期**: 2026-05-21
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2605.22089v1](http://arxiv.org/abs/2605.22089v1)
- **📥 PDF**: 已下载至本地 (`2605.22089v1_LVDrive_Latent_Visual_Representation_Enhanced_Vision-Language-Action_Autonomous_Driving_Model.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型已成为端到端自动驾驶领域极具前景的框架。然而，现有VLA模型通常依赖稀疏的动作监督，未能充分利用其强大的场景理解与推理能力。近期尝试通过世界建模引入密集视觉监督的方法往往过度强调像素级图像重建，忽视了具有语义意义的场景表征学习。为此，本文提出LVDrive——一种面向自动驾驶的潜在视觉表征增强型VLA框架。LVDrive将未来场景预测任务引入VLA范式，在预训练视觉骨干网络的辅助监督下，完全于高级潜在空间中学习未来表征。不同于低效的自回归生成方式，我们在统一嵌入空间中联合建模未来场景与运动预测，通过单次前向传播实现未来感知推理。进一步设计了两阶段轨迹解码策略，显式利用学习到的潜在未来表征优化轨迹生成。在具有挑战性的Bench2Drive基准测试上的大量实验表明，LVDrive在闭环驾驶性能上取得显著提升，全面优于基于动作监督的方法和基于图像重建的世界模型方法。

---

