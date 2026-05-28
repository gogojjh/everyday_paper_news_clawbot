# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-05-28 08:03

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 5/20 篇提供

**🌟 Highlight**: 13 篇 | **📌 Poster**: 7 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. Riding the Shifting Potential: When Reactive Control Suffices for Multi-Goal Behavior

- **作者**: Vito Mengers, Oliver Brock
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.27314v1)
- **发表日期**: 2026-05-26
- **匹配关键词**: diffusion policy, navigation
- **arXiv**: [2605.27314v1](http://arxiv.org/abs/2605.27314v1)
- **📥 PDF**: 已下载至本地 (`2605.27314v1_Riding_the_Shifting_Potential_When_Reactive_Control_Suffices_for_Multi-Goal_Behavior.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 反应式控制通常被认为不足以应对多目标任务，因为相互冲突的目标会导致局部极小值问题。我们认为这一局限性并非固有缺陷，而是源于无法反映目标当前交互方式的静态编码。我们通过引入零空间投影来扩展基于图的世界模型中编码的交互结构：通过将低优先级梯度投影到高优先级梯度的零空间，在冲突产生处解决冲突，而优先级则根据当前状态持续确定。我们在两个以目标冲突为核心问题的领域验证了该方法：在非凸障碍物导航中（静态势场方法在此根本失效），以及非凸物体的平面推动任务中——我们的方法在一百种配置下实现了100%的成功率，而最速下降基线方法为0%，扩散策略方法约为55%，且无需演示或重新训练。相同的公式可直接迁移至具备额外感知与运动学约束的真实机器人，并通过相同机制适应这些约束。

---

### 2. FineVLA: Fine-Grained Instruction Alignment for Steerable Vision-Language-Action Policies

- **作者**: Xintong Hu, Xuhong Huang, Jinyu Zhang, Yutong Yao, Yuchong Sun, Qiuyue Wang, Mingsheng Li, Sicheng Xie, Yitao Liu, Junhao Chen, Yixuan Chen, Yingming Zheng, Shuai Bai, Tao Yu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.27284v1)
- **发表日期**: 2026-05-26
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2605.27284v1](http://arxiv.org/abs/2605.27284v1)
- **📥 PDF**: 已下载至本地 (`2605.27284v1_FineVLA_Fine-Grained_Instruction_Alignment_for_Steerable_Vision-Language-Action_Policies.pdf`)
- **🔓 开源**: PROJECT_PAGE, CODE
- **中文摘要**: 视觉-语言-动作（VLA）模型正日益被期望不仅能完成机器人任务，还能遵循人类关于任务执行方式的指令。然而，现有的机器人数据集通常将轨迹与粗略的目标级语言配对，忽略了诸如活动臂、接近方向和接触区域等执行关键细节。这限制了可引导策略学习和机器人视频理解。我们提出FineVLA，一个面向动作对齐的细粒度VLA监督的开放框架。该框架包括：（1）一个数据构建工具，统一了来自10个开源机器人数据集的972,247条轨迹（涵盖85K个任务），并构建了FineVLA-Data——一个包含47,159条细粒度轨迹的人工验证数据集；（2）一个包含500个视频、10,816个原子事实和1,030个VQA问题的保留基准测试；（3）一个面向机器人领域的专用VLM标注器，用于可扩展的细粒度标注；（4）一个使用细粒度与原始目标级指令的受控混合训练的可引导VLA策略。我们的实验得出三项发现。首先，细粒度监督不会牺牲目标级成功率：在不同设置下，仅使用细粒度指令相比仅使用原始指令，成功率提升了1.4至8.1个百分点。其次，细粒度指令与原始指令具有互补性，呈现一致的倒U型趋势，在细粒度与原始指令比例为1:2至1:1时达到峰值。最佳混合设置在RoboTwin仿真中达到86.8%/82.5%，在真实世界双臂操作中达到62.7/100（相比之下，仅使用原始指令为49.9）。第三，细粒度监督提升了可引导控制能力：真实世界中最大的提升出现在姿态（+23）、颜色（+18）和接近方向（+18）上——这些正是目标级指令无法提供指导的因素。总体而言，细粒度语言应增强目标级指令：在指定"实现什么"的同时，明确"如何执行"。项目页面：https://finevla.xlang.ai/

---

### 3. Towards Shared Embodied Intelligence in Humanoid Robots through Optimization Development and Testing of the Human Aware ergoCub Robot

- **作者**: Carlotta Sartore, Mohamed Elobaid, Lorenzo Rapetti, Giulio Romualdi, Stefano Dafarra, Nicola A. Piga, Ines Sorrentino, Paolo Maria Vicecone, Silvio Traversaro, Ugo Pattacini, Luca Fiorio, Francesco Draicchio, Giovanna Tranfo, Lorenzo Natale, Marco Maggiali, Daniele Pucci
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.26991v1)
- **发表日期**: 2026-05-26
- **匹配关键词**: human-robot interaction
- **arXiv**: [2605.26991v1](http://arxiv.org/abs/2605.26991v1)
- **📥 PDF**: 已下载至本地 (`2605.26991v1_Towards_Shared_Embodied_Intelligence_in_Humanoid_Robots_through_Optimization_Development_and_Testing.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 协作是人类行为的核心，使人类能够完成超出个体能力范围的任务。这种能力源于通过对他人的内部表征来协调行动，这一概念被称为共享智能。此外，人类具有身体特征和认知能力，这些特征和能力会根据环境进行优化，这种现象被称为具身认知。设计能够与人类安全有效协作的人形机器人需要统一这些原则。本文提出了一种整合共享智能与具身认知的架构，使机器人能够与人类进行物理协作。在该架构中，机器人硬件和控制针对人类指标进行了优化，并利用了人体表征和运动智能。最终目标是实现一种共享具身智能的形式。具体而言，我们的架构根据人体工效学指标优化了机器人硬件和物理智能参数。这是通过将人机交互建模为硬件配置的函数，并将人体模型嵌入机器人的物理智能中来实现的。作为具体实现，我们展示了人形机器人ergoCub，其形态和控制已针对与人类的协作任务进行了优化。我们的方法为设计在硬件和物理智能层面优先考虑人体工效学的人形机器人提供了框架，可应用于工业机器人和辅助机器人领域。

---

### 4. OSMa-Bench++: Toward Open-Ended Benchmarking of Semantic Mapping for Manipulation with Prompt-Generated Synthetic Scenes

- **作者**: Regina Kurkova, Maxim Popov, Sergey Kolyubin
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.26831v1)
- **发表日期**: 2026-05-26
- **匹配关键词**: navigation
- **arXiv**: [2605.26831v1](http://arxiv.org/abs/2605.26831v1)
- **📥 PDF**: 已下载至本地 (`2605.26831v1_OSMa-Bench++_Toward_Open-Ended_Benchmarking_of_Semantic_Mapping_for_Manipulation_with_Prompt-Generat.pdf`)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/be2rlab/OSMa-Bench-v2.
- **中文摘要**: 语义映射方法越来越多地被用作下游机器人推理与操作任务的中间场景表征，然而其评估仍主要依赖于固定基准数据集，这些数据集对操作相关边缘场景的覆盖有限。本研究将OSMa-Bench扩展为可通过提示生成合成室内场景的可控基准测试框架。我们的流程可自动生成场景描述，通过SceneSmith合成对应环境，并将生成的资源适配为OSMa-Bench兼容的仿真格式。该适配过程需要构建一个复杂的中间层，包括语义标准化、材质与纹理修复、着色器回退策略、地面处理、导航设置及受控光照配置。该方案的关键优势在于：原始场景生成提示可预先获知，因此能作为目标场景的辅助语义规范。我们利用这一特性，在OSMa-Bench的VQA组件中新增了基于提示的问答类别。最终框架支持在杂乱环境、小物体、局部遮挡及光照变化等条件下对语义场景表征进行定向压力测试，使基准测试更具可扩展性，并更好地契合下游操作需求。我们的代码已开源：https://github.com/be2rlab/OSMa-Bench-v2

---

### 5. Can VLA Models Learn from Real-World Data Continually without Forgetting?

- **作者**: Jiarun Zhu, Yijun Hong, Xiaoquan Sun, Zetian Xu, Mingqi Yuan, Zhiyong Wang, Wenjun Zeng, Jiayu Chen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.26820v1)
- **发表日期**: 2026-05-26
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2605.26820v1](http://arxiv.org/abs/2605.26820v1)
- **📥 PDF**: 已下载至本地 (`2605.26820v1_Can_VLA_Models_Learn_from_Real-World_Data_Continually_without_Forgetting?.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型为通用机器人技术提供了极具前景的基础。然而，要在现实场景中成功部署这些模型，需要具备持续获取新技能同时保留已学行为的能力。尽管已有开创性研究在狭窄的模拟环境中探索了VLA模型的持续学习，但在真实条件下这一挑战仍鲜有深入探究。为弥补这一不足，我们构建了一个包含四项连续操作任务的真实世界持续学习数据集，涵盖刚体拾放、接触式按压及可变形物体折叠等操作。基于该数据集开展的综合实验表明，当VLA模型从异构的真实世界演示中持续学习时，会遭受显著的灾难性遗忘。我们进一步系统评估了经验回放机制，并揭示了决定其成功的关键实施要素。综上所述，本研究首次对真实世界中的VLA持续学习进行了实证研究，并为部署长周期机器人策略提供了实践指导。

---

### 6. DelowlightSplat: Feed-Forward Gaussian Splatting for Lowlight 3D Scene Reconstruction

- **作者**: Fuzhen Jiang, Zengtian Xie, Zhuoran Li
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.26629v1)
- **发表日期**: 2026-05-26
- **匹配关键词**: gaussian splatting, 3D reconstruction, 3d reconstruction
- **arXiv**: [2605.26629v1](http://arxiv.org/abs/2605.26629v1)
- **📥 PDF**: 已下载至本地 (`2605.26629v1_DelowlightSplat_Feed-Forward_Gaussian_Splatting_for_Lowlight_3D_Scene_Reconstruction.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 基于稀疏位姿图像的新视角合成与三维重建是机器人技术和增强现实/虚拟现实的核心。然而，前馈式三维高斯重建在弱光条件下会因噪声、色偏及不可靠的对应关系而失效。我们提出DelowlightSplat——一种面向弱光环境的前馈式高斯泼溅框架，用于生成清晰的新视角渲染。通过仅退化上下文视图而保持目标视图清晰，我们构建了可控的多视角弱光基准。我们引入轻量级弱光适配器进行残差增强以提升可匹配性，并将其与基于代价体的多视角推理相结合，直接预测清晰的三维高斯体。实验表明，DelowlightSplat在弱光条件下显著优于此前的前馈式方法与两阶段流水线。

---

### 7. R5DGS: Semantic-Aware 4D Gaussian Splatting with Rigid Body Constraints for Efficient Dynamic Scene Reconstruction

- **作者**: Denis Gridusov, Maxim Popov, Sergey Kolyubin
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.25909v1)
- **发表日期**: 2026-05-25
- **匹配关键词**: gaussian splatting
- **arXiv**: [2605.25909v1](http://arxiv.org/abs/2605.25909v1)
- **📥 PDF**: 已下载至本地 (`2605.25909v1_R5DGS_Semantic-Aware_4D_Gaussian_Splatting_with_Rigid_Body_Constraints_for_Efficient_Dynamic_Scene_R.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 从多视角视频重建和预测动态三维场景是机器人、增强现实/虚拟现实及数字孪生的基础任务。近期基于物理信息的3D高斯泼溅方法在帧外推方面取得了显著进展，但缺乏语义感知能力且计算开销较大。我们提出R5DGS框架，通过紧凑的身份编码向量增强物理驱动的4D高斯表征，实现高斯体与物体的精确关联。通过构建基于CLIP的离线物体查找表，支持开放词汇文本提示，可在任意时间戳和视角下检索并渲染特定物体的高斯体。此外，我们提出刚体推理约束，仅对物体质心进行物理动力学预测与积分，并通过相对变换将运动传播至关联高斯体。该优化在外推阶段实现11 FPS的加速，同时保持轨迹合理性。

---

### 8. OASIS: Observation-Action Space Alignment via SE(3) Trajectory Prediction for Robotic Manipulation

- **作者**: Xinzhe Chen, Sihua Ren, Liqi Huang, Haowen Sun, Mingyang Li, Xingyu Chen, Zeyang Liu, Xuguang Lan
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.25829v1)
- **发表日期**: 2026-05-25
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2605.25829v1](http://arxiv.org/abs/2605.25829v1)
- **📥 PDF**: 已下载至本地 (`2605.25829v1_OASIS_Observation-Action_Space_Alignment_via_SE(3)_Trajectory_Prediction_for_Robotic_Manipulation.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://npuhandsome.github.io/OASIS_web.
- **中文摘要**: 近期，视觉-语言-动作（VLA）模型与世界动作模型（WAMs）通过利用辅助空间特征或未来视觉状态预测来丰富中间表征，从而推动了机器人操作技术的发展。然而，这些表征大多局限于观测空间，未能共享动作空间的刚体几何特性，迫使动作解码器隐式地恢复该几何结构。为此，我们提出OASIS——一种通过$SE(3)$末端执行器轨迹预测实现中间表征与动作空间对齐的视觉运动策略。OASIS将融合视觉语言与度量深度特征的3D感知编码器与生成相机坐标系末端执行器轨迹的$SE(3)$轨迹预测器相结合。在预测器经位姿监督的隐状态条件下，动作解码器可生成符合刚体运动的动作片段。在仿真与真实世界实验中，OASIS在成功率和分布外泛化能力上均优于VLA与WAM基线方法。项目页面详见https://npuhandsome.github.io/OASIS_web。

---

### 9. Rethinking VLM Representation for VLA Initialization

- **作者**: Weifeng Lin, Siyuan Huang, Hao Li, Tingwei Chen, Ruichuan An, Xinyu Wei, Jianbo Liu, Hongsheng Li
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.25802v1)
- **发表日期**: 2026-05-25
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2605.25802v1](http://arxiv.org/abs/2605.25802v1)
- **📥 PDF**: 已下载至本地 (`2605.25802v1_Rethinking_VLM_Representation_for_VLA_Initialization.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型广泛采用预训练的视觉-语言模型（VLM）作为策略主干，但何种预训练VLM表征对VLA初始化有效仍不明确。本文从三个维度将VLA初始化作为受控表征设计问题进行研究：能力层面的具身VQA监督、参数更新策略及机器人数据预训练。实验表明，原始预训练VLM表征是动作性能的关键来源。然而，具身VQA适配并未带来统一增益：其效果取决于下游瓶颈，且不同能力域的增益并非简单叠加。在更新策略方面，LoRA比全参数微调能提供更可靠的初始化，表明过度重塑预训练表征会削弱VLA初始化效果。机器人数据预训练可进一步改善VLA初始化，其中基于LoRA的分阶段训练方案获得最强变体。这些发现共同表明，有效的VLM-to-VLA适配应在注入与动作相关的具身和机器人轨迹信号的同时，保留对动作学习仍有用的预训练VLM表征。

---

### 10. HumanFlow -- Diffusion-Driven MAV Navigation Among Humans via Tightly-Coupled Motion Tracking, Forecasting, and Control

- **作者**: Simon Schaefer, Joshua Näf, Stefan Leutenegger ⭐
  - **高亮作者**: Stefan Leutenegger
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.25685v1)
- **发表日期**: 2026-05-25
- **匹配关键词**: social navigation, navigation
- **arXiv**: [2605.25685v1](http://arxiv.org/abs/2605.25685v1)
- **📥 PDF**: 已下载至本地 (`2605.25685v1_HumanFlow_--_Diffusion-Driven_MAV_Navigation_Among_Humans_via_Tightly-Coupled_Motion_Tracking,_Forec.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 在三维场景环境中对人类进行鲁棒且精确的感知，对于将机器人融入日常生活环境至关重要。然而，现有方法往往难以预测与周围场景一致的合理且准确的人体运动估计，尤其是在存在严重遮挡或部分可见性的情况下。这可能限制机器人操作的安全性和效率。我们提出HumanFlow，这是一种以三维场景上下文为条件的潜在扩散模型，统一了人体运动跟踪与预测。研究表明，我们的运动模型在包括严重遮挡在内的挑战性条件下，能够生成平滑且准确的预测，在跟踪精度上超越现有最优方法，同时效率显著提升。此外，我们展示了如何通过将基于流匹配的近似MPC策略以这些表示为条件，使HumanFlow的潜在空间与控制系统紧密耦合。我们在仿真环境中利用真实人体轨迹验证了该策略在微型飞行器（MAV）社交导航中的表现，证明即使在人体部分可见的情况下，该策略仍能实现卓越的导航性能并保持无碰撞状态。

---

### 11. G-DRAGON: Geospatial Reasoning and Dynamic Planning for Retrieval-Augmented Outdoor Navigation

- **作者**: Dongzhihan Wang, Yi Du, Jianan Sun, Yuan Xue, Yingchen Zhang, Bing Xiao, Chen Wang, Liang Xu ⭐
  - **高亮作者**: Chen Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.25646v1)
- **发表日期**: 2026-05-25
- **匹配关键词**: VLN, navigation, exploration
- **arXiv**: [2605.25646v1](http://arxiv.org/abs/2605.25646v1)
- **📥 PDF**: 已下载至本地 (`2605.25646v1_G-DRAGON_Geospatial_Reasoning_and_Dynamic_Planning_for_Retrieval-Augmented_Outdoor_Navigation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 在大型户外环境中运行的自主地面机器人需要同时具备鲁棒的长距离导航能力和精细的"最后一英里"探索能力。当前视觉语言导航（VLN）的进展在短距离任务中表现良好，但缺乏长距离任务所需的地理空间基础。部分基于OpenStreetMap（OSM）的方法依赖云端大语言模型（LLM），容易产生事实性幻觉，且无法根据人类指令进行"最后一英里"探索。为解决这些挑战，我们提出G-DRAGON——一种面向户外开放世界导航的检索增强框架。该框架通过基于轻量级LLM的生成式检索，将自然语言指令映射到带版本控制的本地OSM实体，从而为全局路径规划提供精确坐标。高层规划模块将全局拓扑路径与SLAM系统衔接，将地理空间航点投影到机器人可导航坐标系中。针对"最后一英里"，该框架切换至基于前沿探索和开放集语义体素映射的机制，以定位开放词汇目标。仿真实验表明，我们的框架优于现有最优基线方法。此外，我们在未见过的真实城市环境中使用无人地面车辆（UGV）验证系统，成功完成了轨迹长达500米的人员搜索任务。

---

### 12. Safety-Critical Whole-Body Control for Humanoid Robots via Input-to-State Safe Control Barrier Functions

- **作者**: Kwanwoo Lee, Sanghyuk Park, Gyeongjae Park, Myeong-Ju Kim, Jaeheung Park
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.25546v1)
- **发表日期**: 2026-05-25
- **匹配关键词**: obstacle avoidance
- **arXiv**: [2605.25546v1](http://arxiv.org/abs/2605.25546v1)
- **📥 PDF**: 已下载至本地 (`2605.25546v1_Safety-Critical_Whole-Body_Control_for_Humanoid_Robots_via_Input-to-State_Safe_Control_Barrier_Funct.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://kwlee365.github.io/SafeWBC-Website/
- **中文摘要**: 安全关键控制对于在复杂人类中心环境中运行的仿人机器人至关重要，在真实机器人运行过程中必须满足关节限位、自碰撞规避、障碍物规避及工作空间边界等物理安全约束。然而，现有方法仍存在局限性，因为当存在模型不确定性、轨迹跟踪误差和外部扰动等未知干扰时，运动学安全保障能力可能下降。本文提出一种基于输入-状态安全控制屏障函数（ISSf-CBFs）的仿人机器人分层安全关键全身控制框架。该架构集成了运动学级全身控制器（KinWBC）、ISSf-CBF安全滤波器与动力学级全身控制器（DynWBC）。KinWBC根据优先级任务生成标称关节运动参考；ISSf-CBF滤波器在满足有界扰动下运动学安全约束的前提下最小化修正这些参考；DynWBC在跟踪滤波后参考的同时确保全身动力学可行性与接触稳定性。安全约束施加于全身运动学模型，并通过保守调节ISSf-CBF参数，使得所得运动学安全保障能够传递至存在未知扰动的全阶仿人动力学系统。仿真与真实机器人实验表明，所提框架在模型失配情况下提升了安全裕度，并在行走、遥操作及单腿平衡手部控制过程中实时可靠地强制执行多重安全约束。项目网站：https://kwlee365.github.io/SafeWBC-Website/

---

### 13. EXPO-FT: Sample-Efficient Reinforcement Learning Finetuning for Vision-Language-Action Models

- **作者**: Perry Dong, Kuo-Han Hung, Tian Gao, Dorsa Sadigh, Chelsea Finn ⭐
  - **高亮作者**: Chelsea Finn
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.25477v1)
- **发表日期**: 2026-05-25
- **匹配关键词**: vision-language-action, vision-language-action model, VLA
- **arXiv**: [2605.25477v1](http://arxiv.org/abs/2605.25477v1)
- **📥 PDF**: 已下载至本地 (`2605.25477v1_EXPO-FT_Sample-Efficient_Reinforcement_Learning_Finetuning_for_Vision-Language-Action_Models.pdf`)
- **🔓 开源**: CODE
- **中文摘要**: 高效可靠地学习新任务的能力一直是机器人学领域的根本性挑战。视觉-语言-动作（VLA）模型在多种操作任务中展现出强大的泛化能力，但预训练策略始终无法达到实际部署所需的可靠性。强化学习（RL）微调为弥合这一差距提供了有前景的路径，然而现有方法要么完全从头训练而未能充分利用预训练先验知识，要么在微调VLA模型时无法达到实际部署所需的样本效率与成功率。我们提出EXPO-FT系统，通过稳定且样本高效的强化学习微调预训练VLA策略，成功填补了这一空白。该系统解决了一系列具有挑战性的操作任务，包括：串接灯串并插入插头使其点亮、将台球击入球袋、将花朵插入酒瓶——每项任务都需要高精度、动态动作与对多变初始状态的鲁棒性相结合。我们的系统在所有评估任务中均实现完美表现（30/30次成功），平均仅需19.1分钟的在线机器人数据，性能优于此前从零开始的强化学习方法与VLA微调方法。我们开源了代码库，旨在推动机器人领域VLA模型强化学习微调技术的更广泛应用。

---

## 📌 Poster

*其他相关研究*

---

### 1. YOLO26-RipeLoc Lite: A lightweight architecture for tomato ripeness detection and picking point localization in greenhouse robotic harvesting

- **作者**: Rajmeet Singh, Manveen Kaur, Shahpour Alirezaee, Irfan Hussain
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.27129v1)
- **发表日期**: 2026-05-26
- **匹配关键词**: grasp planning
- **arXiv**: [2605.27129v1](http://arxiv.org/abs/2605.27129v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 在温室番茄生产中，自动化采摘需要准确检测成熟番茄、进行成熟度分类，并精确定位机器人末端执行器的采摘点。本文提出YOLO26-RipeLoc Lite，一种基于YOLO26的轻量级深度学习架构，用于同步实现温室番茄的检测、成熟度分类和中心点定位。该模型引入三项改进：（1）采用深度可分离卷积的轻量级特征金字塔网络（LFPN），实现高效多尺度融合；（2）具有双池化和可学习成熟度偏置向量的成熟度感知注意力模块（RAAM），增强颜色纹理区分能力；（3）采用共享卷积和集成中心点回归分支的紧凑检测头（CDH），直接支持抓取规划。模型在来自阿联酋阿布扎比SILAL温室的1500张图像（含6227个实例，其中成熟3566个、未成熟2661个）自定义数据集上评估。YOLO26-RipeLoc Lite在仅使用2.38M参数的情况下，mAP@0.5达到92.9%（成熟95.2%，未成熟90.6%），在所有评估架构中取得最高精度（95.2%）。采用30%训练后批归一化剪枝可将参数降至约1.8M，且精度损失可忽略。消融实验证实，温室感知HSV增强带来最大性能提升（+2.02个百分点mAP@50），骨干网络冻结达到峰值精度（93.8%），三阶段渐进解冻获得最佳定位质量（mAP@50:95为64.6%）。与YOLOv8n/s、YOLO11n/s、YOLO12n/s及YOLO26s的对比验证了其优越的精度-效率平衡：相比YOLO12n精度提升2.9个百分点，参数减少7.0%，并集成中心点定位功能以支持机器人末端执行器引导。

---

### 2. A Bioinspired Underwater Robot with a Latch-Mediated Soft Bistable Mechanism

- **作者**: Chongze Bi, Wenjie Wu, Zonghao Zuo, Li Wen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.26936v1)
- **发表日期**: 2026-05-26
- **匹配关键词**: HRI, exploration
- **arXiv**: [2605.26936v1](http://arxiv.org/abs/2605.26936v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 近几十年来，水下机器人技术取得了显著进展。然而，微型水下机器人的发展仍受限于传统能源的低能量密度。自然界提供了极具启发性的解决方案——螳螂虾和跳蚤等生物利用闩锁介导的弹簧驱动系统，通过解耦的能量储存与释放机制实现快速运动。尽管对闩锁介导弹簧驱动系统已有广泛研究，但如何在简单紧凑的结构中复现这种快速非对称驱动仍具挑战。本研究提出了一种仿生软体双稳态驱动器，其集成闩锁机构可通过单电机实现非对称能量输入与释放。结合鳍状结构，该设计实现了高效水下推进与机动控制。实验结果表明，该装置可实现稳定周期性拍动、精准转向，最大推力达0.528牛，冲量0.147牛·秒，垂直位移30毫米。通过调节鳍角，机器人可完成垂直上升、斜向前进和侧向平移等多种运动模式。本研究为紧凑型水下机器人运动控制提供了一种新颖的节能方案，为探索、环境监测与检测等领域的先进仿生设计开辟了新路径。

---

### 3. Manipulating Tangible Virtual Object Dynamics to Promote Learning of Precision Force Generation

- **作者**: Alberto Garzás-Villar, Alba Riera-Cardona, Alexis Derumigny, J. Micah Prendergast, Jane Murray Cramm, Laura Marchal-Crespo
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.26782v1)
- **发表日期**: 2026-05-26
- **匹配关键词**: exploration
- **arXiv**: [2605.26782v1](http://arxiv.org/abs/2605.26782v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 机器人触觉设备与虚拟现实相结合，为训练精细力量生成提供了新机遇——这是中风康复中至关重要却常被忽视的环节。本研究提出，通过操控有形虚拟物体的渲染动力学特性，可在激活体感系统的同时训练精确力量控制。我们开展了一项包含五十名健康参与者的实验，参与者需完成一项模拟冰壶任务：拉伸虚拟弹簧产生目标释放力，将冰壶推送至冰面预定位置。训练过程中，弹簧的力-伸长关系被建模为线性函数或非线性函数（即高斯函数与反对称高斯函数，后者在释放目标力处导数为零）。结果表明，反对称高斯组在训练期间始终比线性组实现更高的力量精度，而高斯组仅在训练后期优于线性组。人格特质分析显示，在高斯动力学条件下，自由精神得分较高者表现更差且任务探索减少，而挑战转化得分较高者则与探索行为增加相关。尽管存在这些训练效应，但不同弹簧类型及人格特质组间的长期保留效果无显著差异。参与者主要依赖习得的目标伸长量而非目标力——在刚度不同但目标力相同的迁移任务中表现可佐证这一点。这些方法虽对体感神经康复具有潜力，但在神经疾病患者测试前需优化以减少对本体感觉线索的依赖。

---

### 4. Look Further: Socially-Compliant Navigation System in Residential Buildings

- **作者**: Akira Shiba, Marina Obata, Nathan Kau, Zoltan Beck, Rishi Shah, Michael Sudano, Sabrina Lee
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.26710v1)
- **发表日期**: 2026-05-26
- **匹配关键词**: social navigation, navigation, human-robot interaction
- **arXiv**: [2605.26710v1](http://arxiv.org/abs/2605.26710v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 移动机器人对行人做出反应的距离，会显著影响人机交互的多个方面。本文聚焦于住宅室内走廊环境中移动配送机器人平台的导航问题。社交导航方法通常侧重于避免令人不适的人机交互，例如机器人侵入他人个人空间的情况。由于研究表明个人空间范围仅为数米，社交导航方法通常专注于化解和解决这些短距离交互。然而，本研究表明，将反应距离扩展至超过八米（远超典型交互距离）时，可以改善人类对机器人运动的感知。我们提出了一种主动变道运动模式及利用该模式在更远距离对行人做出反应的导航系统。该模式包含机器人在走廊中从中央向侧方横向移动的过程，且与迎面而来的行人保持八米距离。

我们开展了一项包含42名参与者的用户研究，从安全性、流畅性和礼貌性三个服务目标评估其对配送机器人的印象。在直走廊场景（正面接近）中，与文献中典型的运动模式（减速、停止及近距离避碰）相比，该模式在三个目标上均表现出显著改善。相比之下，在交叉路口（盲角）场景中，所有方法均未表现出显著优势，参与者对机器人运动模式的偏好呈现多样化。

---

### 5. Provably Safe Motion Planning Under Unknown Disturbances

- **作者**: Ibon Gracia, Qi Heng Ho, Luca Laurenti, Morteza Lahijanian
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.26625v1)
- **发表日期**: 2026-05-26
- **匹配关键词**: motion planning
- **arXiv**: [2605.26625v1](http://arxiv.org/abs/2605.26625v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出了一种可证明安全的、基于采样的运动规划算法，适用于受未知分布随机扰动影响的机器人系统。我们考虑具有线性或可线性化动力学的系统，在存在任意形状障碍物的工作空间中运行，并受状态与控制约束。安全需求被表述为机会约束。该方法利用系统轨迹数据学习一个Wasserstein模糊管，即一系列模糊集，该模糊管能以高置信度包含系统状态分布的轨迹。随后，该模糊管被用于一个概率完备算法中，以构建满足问题约束的基于采样的运动规划树。研究表明，学习多个低维模糊管而非单个高维模糊管，能有效降低保守性并提升可扩展性。此外，我们设计了一种高效的基于赌博机的有效性检查器，在不牺牲概率完备性的前提下显著提升了方法的实际性能。案例研究表明，在严格安全阈值下的杂乱环境中，我们的算法能够找到有效规划方案，性能优于现有最先进方法。

---

### 6. Multi-Robot Box Transport over Different Surfaces with Decentralized Role-based Proportional Control

- **作者**: Aditya Bhatt, Himavarshini Yarragangu, Urvish Shah, Venkata Sai Yaswanth Mohan Thota, Souma Chowdhury
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.26430v1)
- **发表日期**: 2026-05-26
- **匹配关键词**: motion planning
- **arXiv**: [2605.26430v1](http://arxiv.org/abs/2605.26430v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 多机器人协同推运物体的方法在建筑、仓储环境以及灾后废墟清理等领域具有广泛应用。然而，在不同倾斜度和摩擦特性的表面上实现协同运输仍面临独特挑战。针对这些问题，本文提出了一种异步分布式任务与运动规划方法，用于在平坦、上坡和下坡地形中运输不同质量的矩形箱子。这种分布式方法减少了通信、同步和共识需求，并降低了单点故障风险。该方法名为R2P2（基于规则与比例控制原语的角色分配），首先根据所需操作模式（箱子旋转vs平移）的规则为机器人分配角色（如推动、支撑和阻止），随后基于角色采用规则控制或比例速度控制。每个机器人在执行角色和控制时，需观测自身与箱子的位置及朝向。我们在基于NVIDIA IsaacSim构建的仿真器中部署了六机器人团队对R2P2进行评估——结果表明该方法在不同表面摩擦/倾斜度及箱子质量场景下具有泛化能力，且成功率优于标准虚拟领航-跟随方法。此外，通过物理实验成功验证了R2P2：四台TurtleBot机器人执行了1.2公斤箱子的搬运任务。

---

### 7. RCSP: Risk-Sensitive Conjectural Scenario Planning for Safe Dynamic Robot Navigation

- **作者**: Zhengye Han, Quanyan Zhu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.26348v1)
- **发表日期**: 2026-05-25
- **匹配关键词**: robot navigation, navigation
- **arXiv**: [2605.26348v1](http://arxiv.org/abs/2605.26348v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 移动机器人在碰撞之前就可能失败：当前安全的运动速度，可能会使机器人陷入移动障碍物即将关闭的通道。我们研究了这种预测性近失承诺问题，并提出了风险敏感推测性场景规划（RCSP），这是一个规划层，用于评估候选指令在面对合理的短时域障碍物未来状态时的表现。RCSP维护对局部运动推测的轻量级信念，采样未来交互，惩罚高风险尾部，并通过局部安全检查执行。在受控的MuJoCo瓶颈任务中，RCSP规划器在无碰撞的情况下到达目标，相比非自适应预测器，其二次安全性和路径质量点估计更高，但延迟有所增加。在ROS2/Gazebo中，将局部安全层添加到标准Nav2堆栈可减少动态近失故障。在官方DynaBARN/Jackal迁移测试中，调优后的DWA和TEB在严格基准成功率上仍表现更强，揭示了该方法的边界。这些仿真结果表明，RCSP可作为预测性风险模块，在动态瓶颈场景中补充现有导航堆栈。

---

