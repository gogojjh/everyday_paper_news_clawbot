# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-06-18 08:05

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 5/20 篇提供

**🌟 Highlight**: 19 篇 | **📌 Poster**: 1 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. Uncertainty Quantification for Flow-Based Vision-Language-Action Models

- **作者**: Ralf Römer, Maximilian Seeliger, Saida Liu, Ben Sturgis, Marco Bagatella, Daniel Marta, Andreas Krause, Angela P. Schoellig
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.18043v1)
- **发表日期**: 2026-06-16
- **匹配关键词**: vision-language-action, VLA, vision-language-action model
- **arXiv**: [2606.18043v1](http://arxiv.org/abs/2606.18043v1)
- **📥 PDF**: 已下载至本地 (`2606.18043v1_Uncertainty_Quantification_for_Flow-Based_Vision-Language-Action_Models.pdf`)
- **🔓 开源**: PROJECT_PAGE
- **中文摘要**: 视觉-语言-动作模型（VLAs）将视觉-语言骨干网络与通过流匹配在大规模机器人数据集上训练的生成式动作头相结合。尽管这类模型在机器人操作任务中展现出强大的实证性能，但它们缺乏量化预测置信度以及检测动作可能不可靠的机制。这对其在非平稳环境中的实际部署构成了关键限制——模型不可避免地会遇到超出预训练分布的场景，并可能在无预警的情况下失效。为解决这一问题，我们通过利用小集成模型的速度场不一致性（VFD），推导出一种在流匹配模型中量化认知不确定性的高效方法。我们成功地将这种不确定性估计用于部署期间的故障检测以及基于流的VLA主动微调。为此，我们提出SAVE框架——一种不确定性引导的主动多任务微调方法，可减少将VLA适配至新任务所需的高成本专家演示次数。通过在LIBERO基准上的大量实验，我们证明：VFD能生成更优校准的不确定性估计以预测下游性能，在故障检测中表现优异，且SAVE的不确定性引导数据采集相比基线方法至少减少22%的样本需求。总之，我们的研究表明，量化基于流的VLA中的认知不确定性能同时提升故障感知能力与模型适应性。项目网站：tum-lsy.github.io/uq_vla/。

---

### 2. ThinkingVLA: Interleaved Vision and Language Reasoning for Robotic Manipulation

- **作者**: Tianyi Lu, Hui Zhang, Zijie Diao, Junke Wang, Shengqi Xu, Xingyao Lin, Guojin Zhong, Ziyi Ye, Peng Wang, Zuxuan Wu, Yu-Gang Jiang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.17937v1)
- **发表日期**: 2026-06-16
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2606.17937v1](http://arxiv.org/abs/2606.17937v1)
- **📥 PDF**: 已下载至本地 (`2606.17937v1_ThinkingVLA_Interleaved_Vision_and_Language_Reasoning_for_Robotic_Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 大多数视觉-语言-动作（VLA）模型直接将观测映射到动作，缺乏显式推理能力，限制了其在需要密集推理的长时域任务中的表现。为解决这一问题，现有方法采用思维链（CoT）推理来实现子目标分解和空间预判。然而，这些方法缺乏统一的跨模态推理架构，且未能显式融入基于目标状态的逆向推理能力。我们认为操作规划天然可分解为两个过程：预测（预判下一视觉状态）与逆向动力学（推断达成该状态所需的动作）。连接二者需要一种统一的、在单一生成过程中交错进行文本与视觉推理的自回归架构。为此，我们提出\textbf{ThinkingVLA}——一种在统一混合Transformer架构中实现上述分解的生成模型。ThinkingVLA包含：前向CoT，用于识别即时子目标并引导视觉预测；预测图像作为目标状态，为逆向CoT提供基础，该逆向CoT基于预测图像推理空间关系与动作意图；最终动作则基于完整的推理上下文生成。在仿真与真实世界基准上的大量实验表明，ThinkingVLA持续优于现有最优基线方法，尤其在长时域操作任务中表现显著提升。

---

### 3. MoonSplat: Monocular Online Gaussian Splatting with Sim(3) Global Optimization

- **作者**: Guo Pu, Yixuan Han, Haofeng Li, Yao Zhang, Hui Zhou, Zhouhui Lian
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.17935v1)
- **发表日期**: 2026-06-16
- **匹配关键词**: 3D gaussian splatting, 3D reconstruction, 3d reconstruction, gaussian splatting
- **arXiv**: [2606.17935v1](http://arxiv.org/abs/2606.17935v1)
- **📥 PDF**: 已下载至本地 (`2606.17935v1_MoonSplat_Monocular_Online_Gaussian_Splatting_with_Sim(3)_Global_Optimization.pdf`)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/TrickyGo/MoonSplat.
- **中文摘要**: 基于单目图像序列的在线三维重建是一个具有挑战性且持续活跃的研究课题。三维高斯泼溅（3DGS）凭借其高质量实时渲染能力，使在线三维重建能够以更强的表现力表征密集场景，从而在机器人、AR/VR等广泛领域展现出巨大潜力。然而，现有在线3DGS方法仍面临关键挑战：因缺乏全局优化导致的相机位姿估计脆弱性，以及在大规模或长序列场景中的低优化效率。针对这些问题，我们提出了一种融合全局$\text{Sim}(3)$优化的鲁棒高效在线体素化3DGS重建框架，该框架能够实现可靠的相机追踪，并对相机位姿与体素化3DGS进行高效的全局闭环优化。为加速体素化3DGS的收敛，我们进一步引入颜色残差学习策略，该策略不仅提升了优化速度，还增强了渲染质量。在多种室内外数据集上的大量实验表明，我们的方法在相机位姿估计精度与渲染质量方面均达到最优水平，同时保持实时效率。此外，我们基于所提方法开发并部署了真实世界的无人机主动重建系统，验证了该方法在实际在线三维重建任务中的鲁棒性与泛化能力。代码与数据已开源至https://github.com/TrickyGo/MoonSplat。

---

### 4. Qwen-RobotManip Technical Report: Alignment Unlocks Scale for Robotic Manipulation Foundation Models

- **作者**: Haoqi Yuan, Zhixuan Liang, Anzhe Chen, Ye Wang, Haoyang Li, Pei Lin, Yiyang Huang, Zixing Lei, Tong Zhang, Jiazhao Zhang, Jie Zhang, Jingyang Fan, Gengze Zhou, Qihang Peng, Chenxu Lv, Xiaoyue Chen, An Yang, Fei Huang, Junyang Lin, Dayiheng Liu, Jingren Zhou, Chenfei Wu, Xiong-Hui Chen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.17846v1)
- **发表日期**: 2026-06-16
- **匹配关键词**: vision-language-action
- **arXiv**: [2606.17846v1](http://arxiv.org/abs/2606.17846v1)
- **📥 PDF**: 已下载至本地 (`2606.17846v1_Qwen-RobotManip_Technical_Report_Alignment_Unlocks_Scale_for_Robotic_Manipulation_Foundation_Models.pdf`)
- **🔓 开源**: CODE
- **中文摘要**: 语言与多模态基础模型通过统一的数据格式对齐异构数据，并借助大规模训练实现了强大的泛化能力。本报告探究该扩展策略能否应用于机器人操作领域以实现真正的泛化。这一挑战在于：与文本数据不同，操作数据天然具有异构性、采集成本高昂且多样性有限，使得数据对齐与规模化扩展难以同步实现。我们提出基于Qwen-VL构建的通用视觉-语言-动作基础模型Qwen-RobotManip。该模型创新性地引入跨表征、运动和行为维度的统一对齐框架，使大规模多源训练从相互冲突转变为协同增效。这种对齐能力使Qwen-RobotManip能够吸收此前训练范式无法承载规模的操作数据。通过人机合成流水线，我们将15个平台上的第一人称手部演示转化为机器人轨迹，并采用严格的数据筛选流程协调异构数据集。仅使用开源数据集和人类视频（无需专有数据采集），Qwen-RobotManip构建了约38,100小时的预训练语料库，展现出包括零样本指令跟随、扰动鲁棒性、反应式错误恢复及跨本体迁移在内的涌现泛化能力。研究发现标准基准无法有效评估预训练质量，因此我们采用包含RoboCasa365、LIBERO-Plus、EBench、RoboTwin-Clean2Rand、RoboTwin-IF和RoboTwin-XE在内的分布外测试场景。Qwen-RobotManip在所有分布外场景中显著超越包括π0.5在内的先前最优模型，在RoboChallenge中以20%的相对提升位列第一，并在AgileX ALOHA、Franka、UR和ARX等真实机器人平台上完成验证。

---

### 5. MuseVLA: An Adaptive Multimodal Sensing Vision-Language-Action Model for Robotic Manipulation

- **作者**: Xingyuming Liu, Ruichun Ma, Heyu Guo, Qixiu Li, Qingwen Yang, Lin Luo, Shiqi Jiang, Chenren Xu, Jiaolong Yang, Baining Guo
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.17598v1)
- **发表日期**: 2026-06-16
- **匹配关键词**: vision-language-action, VLA, vision-language-action model
- **arXiv**: [2606.17598v1](http://arxiv.org/abs/2606.17598v1)
- **📥 PDF**: 已下载至本地 (`2606.17598v1_MuseVLA_An_Adaptive_Multimodal_Sensing_Vision-Language-Action_Model_for_Robotic_Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 人类天生利用多种感知模态与物理世界交互，而大多数用于机器人的视觉-语言-动作（VLA）模型仅依赖RGB观测。这限制了它们感知难以或无法从RGB相机推断的物理属性（如温度、声音或雷达响应）的能力。我们提出MuseVLA，一种自适应多模态感知VLA模型，将新型传感器作为机器人操作的按需工具集成。给定任务指令和视觉上下文，MuseVLA首先生成一个传感器令牌和目标描述，选择要调用的感知模态及关注对象，类似于带参数的函数调用。随后，它将选定的传感器测量值转换为接地传感器图像，这是一种统一的中间表示，用于编码异构读数以进行多模态融合和动作生成。这种设计将传感器特定处理与VLA主干解耦，实现了多种模态的高效集成。为减少对昂贵多感官机器人数据集的需求，我们进一步引入数据合成流程，用接地传感器图像增强现有RGB视频数据集，从而实现对未见传感器引导任务的泛化。我们在真实机器人上评估MuseVLA，涉及需要多模态感知输入的挑战性灵巧手操作任务，包括温度引导的拾取与放置、音频驱动的物体搜索以及雷达辅助的隐藏物体检索。MuseVLA平均成功率达80.6%，显著优于仅RGB和多感官VLA基线，并在未见任务上展现出强大的零样本能力。

---

### 6. RICH-SLAM: Radar SLAM with Incremental and Continuous Hilbert Mapping

- **作者**: Bingbing Zhang, Huan Yin, Yang Xu, Shuo Liu, Shaojie Shen, Fumin Zhang, Wen Xu ⭐
  - **高亮作者**: Shaojie Shen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.17534v1)
- **发表日期**: 2026-06-16
- **匹配关键词**: localization and mapping
- **arXiv**: [2606.17534v1](http://arxiv.org/abs/2606.17534v1)
- **📥 PDF**: 已下载至本地 (`2606.17534v1_RICH-SLAM_Radar_SLAM_with_Incremental_and_Continuous_Hilbert_Mapping.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 基于雷达传感器的同步定位与地图构建技术，因雷达在恶劣天气和光照条件下固有的鲁棒性而日益受到关注。然而，与激光雷达和视觉数据相比，雷达测量值具有稀疏性和噪声特性，这给实现密集、连续且一致的地图表示带来了重大挑战。本文提出RICH-SLAM雷达同步定位与地图构建框架，旨在解决上述挑战。该方法采用基于Rao-Blackwellized粒子滤波的后端系统，通过粒子滤波进行位姿估计，并利用卡尔曼滤波实现地图更新。我们提出了一种增量式希尔伯特空间降秩高斯过程建图策略，能够在稀疏雷达输入条件下实现连续且具有不确定性感知的地图表示。进一步引入后验感知粒子加权方案，通过利用地图参数的完整后验分布实现更稳健的似然评估。在自采集数据集和公开ColoRadar数据集上的实验表明，RICH-SLAM能够从稀疏雷达测量中构建连续占据地图，并支持移动机器人的不确定性感知规划。

---

### 7. GASE: Gaussian Splatting-Based Automated System for Reconstructing Embodied-Simulation Environments

- **作者**: Jiawei Zhang, Yiming Yan, Chao Liang, Nuo Xu, Seson Sun, Qichen Zhang, Yuhao Xu, Yantai Yang, Yingqiao Wang, Qin Jin, Zhipeng Zhang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.17520v1)
- **发表日期**: 2026-06-16
- **匹配关键词**: navigation, gaussian splatting
- **arXiv**: [2606.17520v1](http://arxiv.org/abs/2606.17520v1)
- **📥 PDF**: 已下载至本地 (`2606.17520v1_GASE_Gaussian_Splatting-Based_Automated_System_for_Reconstructing_Embodied-Simulation_Environments.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 在现实世界中训练具身智能体需要熟练的操作人员和昂贵的硬件设备。仿真环境通过支持大规模、低成本的增强数据，提供了一种极具吸引力的替代方案。因此，快速构建高保真仿真场景并最小化仿真到现实的差距，已成为机器人学习中的关键目标。尽管基于重建的方法能提供卓越的视觉质量，但当前的工作流程受限于低效的数据采集和欠佳的前景物体提取效果。为此，我们提出GASE——一种高度自动化的仿真场景构建系统。GASE利用全景相机阵列的多视角视频流实现快速环境扫描。为确保高质量资产生成，我们的流程引入了一种基于相机姿态的策略，能够在二维域中稳健地跨帧提取物体，随后进行高保真场景修复。前景物体与静态背景分别独立重建，并无缝导入物理模拟器用于策略训练。大量实验表明，GASE在分割精度上比现有基于3D高斯的方法提升超过10%，同时实现了最先进的修复质量。此外，在操作与导航任务中的真实机器人部署显示，与纯真实数据训练的策略相比，性能差距低于10%。这些结果证实GASE为弥合仿真到现实差距提供了高效且有效的解决方案。代码将开源。

---

### 8. GeneralVLA-2: Geometry-Aware Reconstruction and Governed Memory for Robot Planning

- **作者**: Haoyu Wang, Guoqing Ma, Zeyu Zhang, Yandong Guo, Boxin Shi, Hao Tang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.17480v1)
- **发表日期**: 2026-06-16
- **匹配关键词**: vision-language-action, 3d reconstruction, 3D reconstruction, VLA
- **arXiv**: [2606.17480v1](http://arxiv.org/abs/2606.17480v1)
- **📥 PDF**: 已下载至本地 (`2606.17480v1_GeneralVLA-2_Geometry-Aware_Reconstruction_and_Governed_Memory_for_Robot_Planning.pdf`)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/AIGeeksGroup/GeneralVLA-2., https://aigeeksgroup.github.io/GeneralVLA-2.
- **中文摘要**: 通用视觉-语言-动作系统需要以物体为中心的3D证据和可复用的操作经验来规划可靠的机器人轨迹。GeneralVLA提供了一种分层接口，可将语言和RGB-D观测转化为3D末端执行器路径，但仍存在两个瓶颈。首先，单目SAM3D风格的物体重建可能会产生姿态和未见几何结构的幻觉，而操作任务在拥有校准的多视角观测时，能从稳定的物体形状中获益。其次，原始的KnowledgeBank主要检索语义相似的片段并追加新知识，这使得难以控制记忆质量、冲突、置信度和几何相关性。针对第一个挑战，我们引入了GeoFuse-MV3D——一种几何先验引导的MV-SAM3D重建分支，它通过输入视角掩码验证外部几何线索，应用软视觉外壳支持，执行轴对齐精炼，并在保留外观的同时仅融合几何信息。针对第二个挑战，我们将KnowledgeBank升级为一个受控的长期记忆系统，包含显式的质量、置信度、生命周期、验证器和冲突元数据，以及面向精度的检索机制。最后，我们在GSO-30上评估了重建分支，在Terminal-Bench 2.0和SWE-Bench Verified上评估了记忆模块；GeoFuse-MV3D相比MV-SAM3D基线，将CD和LPIPS分别降低了2.20%和2.02%，同时将PSNR和SSIM分别提升了2.36%和1.03%；KnowledgeBank在Terminal-Bench SR上相比ReasoningBank提升了4.53%，在SWE-Bench解决率上提升了3.73%，同时将AS分别降低了4.95%和5.65%。代码：https://github.com/AIGeeksGroup/GeneralVLA-2。网站：https://aigeeksgroup.github.io/GeneralVLA-2。

---

### 9. WeaveLA: Event Driven Cross-Subtask Latent Memory Weaving for Repetitive Robot Manipulation

- **作者**: Shoujing Zhu, Zhenyang Liu, Fungmiu Wang, Jiafeng Wang, Bo Yue, Guiliang Liu, Simo Wu, Xiangyang Xue, Taiping Zeng
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.17463v1)
- **发表日期**: 2026-06-16
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2606.17463v1](http://arxiv.org/abs/2606.17463v1)
- **📥 PDF**: 已下载至本地 (`2606.17463v1_WeaveLA_Event_Driven_Cross-Subtask_Latent_Memory_Weaving_for_Repetitive_Robot_Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）策略在单步操作中取得了显著成效，但其脆弱性恰恰体现在每个阶段依赖于前一阶段完成结果这一环节。核心问题在于结构性缺陷：短窗口VLA缺乏显式通道来跨子任务边界传递信息，而现有记忆增强变体要么每帧写入、从演示阶段检索，或在子目标事件触发时激活，却未执行显式的子任务间交接至动作专家。我们提出子目标完成事件作为跨子任务记忆交接的自然时间单元，并设计WeaveLA（面向视觉-语言-动作策略的潜记忆编织架构）——一种跨子任务记忆接口。该接口在冻结的VLA主干上，通过查询驱动的注意力池化将每个已完成片段压缩为潜变量令牌，并直接路由至下一子任务的动作生成路径。这种事件触发、面向动作侧的设计在保持基础策略短窗口接口的同时，增加了轻量级跨子任务通道。基于RoboMME平台以π₀.₅为主干的层次化评估显示，WeaveLA的增益精准作用于需要该通道的场景：在最具挑战性的重复切片任务（SwingXtimes，N=3）中，成功率从0%提升至47.8%，而单次执行场景保持不变。逐回合配对分析证实，增益仅限于因果结构需要跨子任务信息的任务。

---

### 10. Improving and Evaluating Hand-Object Interaction Detection

- **作者**: Ahmad Darkhalil, Dima Damen, David Fouhey
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.17384v1)
- **发表日期**: 2026-06-16
- **匹配关键词**: 3D reconstruction, 3d reconstruction
- **arXiv**: [2606.17384v1](http://arxiv.org/abs/2606.17384v1)
- **📥 PDF**: 已下载至本地 (`2606.17384v1_Improving_and_Evaluating_Hand-Object_Interaction_Detection.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 理解手部及其直接或通过工具交互的物体，是从动作感知到三维重建及机器人技术等任务的关键步骤。本文在手-物交互（HOI）理解领域做出了多项贡献：（1）提出HOI-DETR新框架，将手-物交互与物-物交互引入Co-DETR架构，构建了当前最先进的方法；（2）构建了包含4个不同数据集的综合HOI评估套件，其中包含基于HD-EPIC数据集衍生的视频基准及改进Hands23基准的新标注；（3）训练得到的模型检查点在Hands23、HOIST、FineBio和HD-EPIC数据集上显著提升了现有技术水平，其中在Hands23和FineBio上的平均精度（mAP）提升超过20个百分点。消融实验验证了各模型组件的贡献。

---

### 11. VISTA: Scale-Aware Visual Navigation via Action History Conditioning

- **作者**: Maeva Guerrier, Koki Kobayashi, Simon Roy, Jana Pavlasek, Giovanni Beltrame
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.17294v1)
- **发表日期**: 2026-06-15
- **匹配关键词**: navigation, visual navigation, learned navigation
- **arXiv**: [2606.17294v1](http://arxiv.org/abs/2606.17294v1)
- **📥 PDF**: 已下载至本地 (`2606.17294v1_VISTA_Scale-Aware_Visual_Navigation_via_Action_History_Conditioning.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉导航基础模型（VNMs）有望实现端到端学习的导航策略，能够在不同载体和环境间进行零样本部署。为保持通用性，许多基于视觉的导航模型会预测归一化动作。然而，这种归一化引入了一个关键的部署缺陷：对同一归一化轨迹应用不同的缩放因子会改变其物理几何形态，从而降低导航性能并增加碰撞风险。我们通过将模型条件设定为归一化动作历史与图像观测相结合来解决这一缺陷，为模型预测与机器人实际物理位移之间的关系提供显式上下文。此外，当前VNMs在缺乏显著特征的视觉重复环境中往往表现不佳。为解决此问题，我们集成了DINOv3编码器，其更丰富的表征能力使模型能够捕捉观测之间的空间与几何维度。VISTA对分布外环境具有鲁棒泛化能力，在户外、森林和办公室场景的零样本实际部署中实现了100%的目标预测准确率，平均穿越95%的检查点，展现了在未知环境中一致的路径跟踪能力。

---

### 12. ACE-Ego-0: Unifying Egocentric Human and Robotic Data for VLA Pretraining

- **作者**: Hao Li, Ganlong Zhao, Yufei Liu, Haotian Hou, Guoquan Ye, Tongyan Fang, Chunxiao Liu, Siyuan Huang, Jianbo Liu, Xiaogang Wang, Hongsheng Li
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.17200v1)
- **发表日期**: 2026-06-15
- **匹配关键词**: bimanual manipulation, VLA, vision-language-action
- **arXiv**: [2606.17200v1](http://arxiv.org/abs/2606.17200v1)
- **📥 PDF**: 已下载至本地 (`2606.17200v1_ACE-Ego-0_Unifying_Egocentric_Human_and_Robotic_Data_for_VLA_Pretraining.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型受益于大规模、多样化的具身数据，但机器人轨迹数据的采集成本高昂且劳动密集。最新研究表明，大规模第一人称人类视频在预训练中提供了互补的真实世界监督信号。然而，由于动作空间、具身结构、时间动态和标注质量存在差异，人类与机器人数据的联合训练仍面临挑战。本文提出ACE-EGO-0，一个统一利用异构数据源的VLA预训练框架。为从第一人称人类视频中提取大规模预训练监督信号，我们构建了可扩展的第一人称视频到动作流水线，将原始人类视频转化为机器人格式的伪动作轨迹。为使这些标签与机器人演示可比，ACE-EGO-0采用基于相机空间动作、形态条件约束和时间对齐动作分块的统一动作表征。为稳健利用第一人称人类视频中带噪声的伪动作监督信号，我们设计了可靠性感知训练目标，并引入人类辅助损失函数，将监督聚焦于可靠信号。我们在4.53K小时机器人及仿真数据与1.48K小时伪动作标注的第一人称人类数据上实例化ACE-EGO-0。实验表明，在可靠性感知加权下融入大规模人类监督信号，能持续提升统一联合预训练和有监督微调的性能。ACE-EGO-0在RoboCasa GR1 TableTop和RoboTwin 2.0基准上达到最优性能，并展现出向真实世界双臂操作任务的有效迁移能力。

---

### 13. T-Rex: Tactile-Reactive Dexterous Manipulation

- **作者**: Dantong Niu, Zhuoyang Liu, Zekai Wang, Boning Shao, Zhao-Heng Yin, Anirudh Pai, Yuvan Sharma, Stefano Saravalle, Ruijie Zheng, Jing Wang, Ryan Punamiya, Mengda Xu, Yuqi Xie, Yunfan Jiang, Letian Fu, Konstantinos Kallidromitis, Matteo Gioia, Junyi Zhang, Jiaxin Ge, Haiwen Feng, Fabio Galasso, Wei Zhan, David M. Chan, Yutong Bai, Roei Herzig, Jiahui Lei, Fei-Fei Li, Ken Goldberg, Jitendra Malik, Pieter Abbeel, Yuke Zhu, Danfei Xu, Jim, Fan, Trevor Darrell ⭐
  - **高亮作者**: Yuke Zhu
- **单位**: Linxi; Linxi; Linxi...
- **发表日期**: 2026-06-15
- **匹配关键词**: vision-language-action, VLA, object manipulation
- **arXiv**: [2606.17055v1](http://arxiv.org/abs/2606.17055v1)
- **📥 PDF**: 已下载至本地 (`2606.17055v1_T-Rex_Tactile-Reactive_Dexterous_Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 对触觉信号做出动态响应的能力，长期以来一直被认为是实现类人敏捷灵巧操作的关键。然而，当前基于学习的机器人操作视觉-语言-动作（VLA）模型通常要么忽略触觉模态，要么局限于使用静态线索的编码器——这在一定程度上是由于多样化训练数据和标准化评估的匮乏、现有VLA模型的架构限制，以及静态触觉编码器的局限性所致。本文通过解决上述所有限制，推动了触觉反应式操作的前沿发展。我们提出了一种大规模、100小时的触觉丰富数据集，该数据集通过一种新颖且数据高效的方法收集，优先关注基础运动基元。为了在不牺牲现有VLA模型能力的前提下有效利用天然高频触觉信号，我们引入了一种可变速率混合Transformer（MoT）架构，并配备了一种新型时序触觉VQ-VAE编码器。我们在12项需要精细力控制和可变形物体操作的任务中验证了触觉反应式策略的有效性，相较于最强基线方法，平均成功率提升了30%以上。

---

### 14. Geometric Action Model for Robot Policy Learning

- **作者**: Jisang Han, Seonghu Jeon, Jaewoo Jung, René Zurbrügg, Honggyu An, Tifanny Portela, Marco Hutter, Marc Pollefeys, Seungryong Kim, Sunghwan Hong ⭐
  - **高亮作者**: Marc Pollefeys
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.17046v1)
- **发表日期**: 2026-06-15
- **匹配关键词**: vision-language-action, VLA, vision-language-action model, contact-rich manipulation
- **arXiv**: [2606.17046v1](http://arxiv.org/abs/2606.17046v1)
- **📥 PDF**: 已下载至本地 (`2606.17046v1_Geometric_Action_Model_for_Robot_Policy_Learning.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 通用型机器人策略必须遵循用户指令，同时推理物体、摄像头和机器人动作在三维物理世界中的交互方式。近期出现的视觉-语言-动作模型（VLA）和视频世界-动作模型（WAM）虽然继承了大规模基础模型强大的语义或时间先验知识，但其运作仍主要基于二维图像帧或二维衍生潜在空间，导致接触密集型操作所需的三维几何信息被隐式处理。我们提出几何动作模型（GAM），这是一种语言条件化的操作策略，直接复用预训练的几何基础模型（GFM）作为感知、时间预测和动作解码的共享基座。GAM在GFM中间层进行拆分：浅层作为观测编码器，在拆分层插入因果未来预测器，基于语言、本体感知和动作历史预测未来潜在标记。预测的未来标记随后通过剩余GFM模块进行特征传播与解码，使单一骨干网络同时生成未来几何结构与动作。这种设计通过最小化架构修改，赋予GFM语言条件化的时间世界建模能力，同时保留其丰富的几何先验知识。在广泛的仿真与真实机器人操作基准测试中，GAM相比当前基础模型规模的基线方法，展现出更高的精度、鲁棒性、速度与轻量化优势。

---

### 15. Hierarchical Advantage Weighting for Online RL Fine-Tuning of VLAs from Sparse Episode Outcomes

- **作者**: Tongyan Fang, Siyuan Huang, Naiyu Fang, Ganlong Zhao, Zhongjin Luo, Jianbo Liu, Xiaogang Wang, Ying Dong, Hongsheng Li
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.17043v1)
- **发表日期**: 2026-06-15
- **匹配关键词**: VLA
- **arXiv**: [2606.17043v1](http://arxiv.org/abs/2606.17043v1)
- **📥 PDF**: 已下载至本地 (`2606.17043v1_Hierarchical_Advantage_Weighting_for_Online_RL_Fine-Tuning_of_VLAs_from_Sparse_Episode_Outcomes.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 当预训练的视觉-语言-动作（VLA）策略通过在线强化学习进行微调时，每次交互回合仅产生一个二元结果（成功或失败），但策略更新需要每个时间步的监督信号。现有方法通常将这种稀疏结果简化为单个标量奖励或优势信号，这混淆了不同形式的逐时间步反馈，并且在基本任务成功变得可实现后提供的指导有限。首先，单个标量信号混淆了可行性和效率这两个目标；一旦基本成功实现，二元标签无法提供梯度来区分高效完成与缓慢完成。其次，真实世界的交互混合了自主和干预片段；简单地将回合结果跨这些边界分配会导致错误的信用分配。为解决这些问题，我们提出分层优势加权行为克隆（HABC），该方法在不同数据子集上为这两个目标训练独立的评论家头，并通过状态自适应平衡组合其输出。状态自适应门控$g_t$合并它们的单步优势，在成功不确定时优先考虑可行性，仅在可行性高时转向效率，并将结果转换为策略损失上的逐时间步权重。干预感知的信用分配进一步将结果标签限制在当前策略执行的片段上，防止监督信号跨干预边界泄露。在三个接触密集型双臂任务的真实机器人实验中，HABC将监督微调（SFT）基线从36%、44%和12%的成功率提升至92%、88%和38%。

---

### 16. R2RDreamer: 3D-aware Data Augmentation for Spatially-generalized 2D Manipulation Policies

- **作者**: Xiuwei Xu, Haowen Sun, Angyuan Ma, Yiwei Zhang, Zhenyu Wu, Xiaofeng Wang, Bingyao Yu, Zheng Zhu, Jie Zhou, Jiwen Lu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.17040v1)
- **发表日期**: 2026-06-15
- **匹配关键词**: vision-language-action
- **arXiv**: [2606.17040v1](http://arxiv.org/abs/2606.17040v1)
- **📥 PDF**: 已下载至本地 (`2606.17040v1_R2RDreamer_3D-aware_Data_Augmentation_for_Spatially-generalized_2D_Manipulation_Policies.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 空间泛化对于通过模仿学习获得的操控策略至关重要，但实现这一目标通常需要跨不同物体姿态、机器人配置和相机视角的多样化演示数据。基于少量源演示的数据增强为昂贵的数据采集提供了实用替代方案。基于仿真的增强方法可生成可控变化，但需要复杂的环境和物体设置，且可能引入仿真到现实的差距。近期基于真实到真实的方法通过联合编辑真实演示中的3D观测和动作轨迹来规避这些问题，但仍依赖强大的3D场景解析和几何补全，且生成的观测通常针对3D点云策略而非基于RGB的2D策略。我们提出R2RDreamer，一种保持3D动作-观测编辑几何一致性的同时将视觉补全迁移至2D视频空间的真实到真实演示增强框架。具体而言，R2RDreamer首先通过编辑共享3D坐标系中的不完整物体点云和末端执行器轨迹执行轻量级3D增强；随后将编辑后的场景通过遮挡感知推理投影至掩膜图像空间的控制视频，并利用密集控制图像到视频模型补全时间连贯的RGB观测。在空间偏移操控任务上对2D扩散策略和视觉-语言-动作策略的实验表明，R2RDreamer能从有限源演示中提升空间泛化能力，分析结果验证了3D编辑、遮挡感知投影和视频补全的贡献。

---

### 17. ROVE: Unlocking Human Interventions for Humanoid Manipulation via Reinforcement Learning

- **作者**: Wei Xiao, Weiliang Tang, Yuying Ge, Hui Zhou, Yao Mu, Li Zhang, Yixiao Ge
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.17011v1)
- **发表日期**: 2026-06-15
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2606.17011v1](http://arxiv.org/abs/2606.17011v1)
- **📥 PDF**: 已下载至本地 (`2606.17011v1_ROVE_Unlocking_Human_Interventions_for_Humanoid_Manipulation_via_Reinforcement_Learning.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 人类干预为视觉-语言-动作（VLA）模型的后训练提供了关键的修正信号。然而，由于复杂的全身运动学与灵巧手控制，实现无缝的人形干预是一项艰巨的系统性挑战。因此，收集到的干预轨迹往往并非最优，而依赖人类干预作为专家监督的方法可能会吸收犹豫、低效甚至错误的动作。为同时解决系统与算法层面的挑战，我们提出ROVE——一种基于强化学习的人形VLA后训练框架，可应对不完美的人类干预。首先，ROVE引入了一种人在环流水线，能够收集人形操作的部署与干预数据。其次，它利用乐观价值估计（OVE）从混合质量轨迹中优先提取高价值行为。为进一步增强价值估计的鲁棒性，我们融入跨具身人类经验视频，为长尾失败与恢复模式提供丰富的监督信号。由此生成的评论家网络可提供信息丰富的优势信号，引导VLA执行器聚焦于高价值行为，而非不加区分地模仿所有动作。在具有挑战性的真实世界接触密集与精细人形操作任务中，ROVE优于基于经验学习的基线方法，并在多轮部署-干预迭代中持续提升性能。

---

### 18. Binary Tracking for Spatial QA and Navigation with Open Vision-Language Models

- **作者**: Dongbin Na, Chanwoo Kim, Soonbin Rho, Giyun Choi, Gangbok Lee, Dooyoung Hong
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.16902v1)
- **发表日期**: 2026-06-15
- **匹配关键词**: navigation, exploration
- **arXiv**: [2606.16902v1](http://arxiv.org/abs/2606.16902v1)
- **📥 PDF**: 已下载至本地 (`2606.16902v1_Binary_Tracking_for_Spatial_QA_and_Navigation_with_Open_Vision-Language_Models.pdf`)
- **🔓 开源**: CODE, GITHUB
  - 链接：https://github.com/ndb796/BinaryTracking
- **中文摘要**: 本工作针对服务机器人在长距离自我中心路径中的空间问答问题展开研究。当系统接收到诸如“回家路上哪里能找到干洗店？”的查询时，会返回一个下游导航模块可执行的度量坐标。现有空间问答方法通常依赖基于GPT-4o等闭源模型构建的检索增强代理进行路径探索。然而，由于网络不稳定、通信延迟和部署成本等因素，现实环境中运行的机器人往往无法可靠依赖在线闭源模型。这催生了对基于开源方案、可在机器人本体运行的空间问答方法的需求，但现有相关研究仍十分有限。本文提出BinTrack——一种简洁高效的全开源空间定位代理，该代理利用机器人轨迹的时间顺序特性，通过在查询中识别的两个锚定地标之间的轨迹段执行二分搜索。相较于其他开源实现，该方法将整体准确率提升高达22.8%，甚至在SpaceLocQA基准测试的全局类别中达到与GPT-4o等强推理代理所报告的闭源模型结果相当的水平——该类别是目前最具挑战性的设置。此外，其优化推理策略相较先前方法持续实现1.5倍以上的推理加速。最后，本工作发布GangnamLoop——一个通过在实际公共街道部署真实四足机器人并采用匿名化策略采集的新型实用多行程户外基准数据集。该数据集在不同室外条件下重访相同地点，并将机器人的低视角与人类主人的视角进行配对。源代码和数据集已公开于https://github.com/ndb796/BinaryTracking。

---

### 19. SGM-SLAM: Scene Graph Matching for Data-Efficient Distributed SLAM

- **作者**: Yewei Huang, Tixiao Shan, Abhinav Rajvanshi, Niluthpol Chowdhury Mithun, Yaxuan Li, Brendan Englot, Han-Pang Chiu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.16881v1)
- **发表日期**: 2026-06-15
- **匹配关键词**: scene graph, localization and mapping
- **arXiv**: [2606.16881v1](http://arxiv.org/abs/2606.16881v1)
- **📥 PDF**: 已下载至本地 (`2606.16881v1_SGM-SLAM_Scene_Graph_Matching_for_Data-Efficient_Distributed_SLAM.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出了一种面向配备激光雷达、相机和惯性传感器的机器人团队的高效数据分布式同步定位与建图（SLAM）框架。该框架利用场景图匹配来识别机器人间的测量约束。与依赖特征级匹配的现有方法不同，本框架首次仅通过物体标签和质心实现场景图匹配。我们的方法通过融合RGB-激光雷达点云构建场景图，生成语义分割点云层和离散有界物体层，并同步估计机器人轨迹。通过相邻机器人间交换和匹配物体数据，协作完成场景图匹配。为最大化通信效率，我们采用多步数据交换与优化流程。通过仿真实验及腿式机器人在室内外环境采集的真实数据集，验证了该方法的有效性与高效性。

---

## 📌 Poster

*其他相关研究*

---

### 1. Qwen-RobotNav Technical Report: A Scalable Navigation Model Designed for an Agentic Navigation System

- **作者**: Jiazhao Zhang, Gengze Zhou, Hale Yin, Yiyang Huang, Zixing Lei, Qihang Peng, Haoqi Yuan, Jie Zhang, Xudong Guo, Xiaoyue Chen, An Yang, Fei Huang, Junyang Lin, Dayiheng Liu, Jingren Zhou, Zhuoyuan Yu, Jingyang Fan, Zhixuan Liang, Pei Lin, Ye Wang, Anzhe Chen, Kun Yan, Xiao Xu, Jiahao Li, Lulu Hu, Minying Zhang, Shurui Li, Wenhu Xiao, Shuai Bai, Xuancheng Ren, Chenxu Lv, Chenfei Wu, Xiong-Hui Chen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.18112v1)
- **发表日期**: 2026-06-16
- **匹配关键词**: navigation
- **arXiv**: [2606.18112v1](http://arxiv.org/abs/2606.18112v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 智能体导航系统需要一个基础导航模型，其观测策略可在推理时进行外部重构，因为指令跟随、目标搜索、目标追踪和自动驾驶共享相同的感知规划主干网络，但对视觉流的处理方式却有着根本不同的需求。我们提出Qwen-RobotNav，这是一个基于Qwen-RobotNav构建的可扩展导航模型，通过一个具有两个互补维度的参数化接口解决上述问题：多个任务模式用于选择导航行为，以及可控的观测参数（如令牌预算、每相机权重）用于控制视觉历史的编码方式。通过训练时对所有参数进行随机化处理，Qwen-RobotNav能够适应任何推理时的配置，且无需对Qwen-RobotNav主干网络进行任何架构修改。我们在1560万个样本上训练Qwen-RobotNav；与视觉语言数据联合训练可防止仅使用轨迹训练时出现的退化为反应式动作序列映射器的问题。参数化接口还使Qwen-RobotNav成为智能体系统的天然构建模块：对于长时域场景，上层规划器将目标分解为子任务，并在任务过程中动态切换Qwen-RobotNav的任务模式和上下文策略，通过重复调用同一模型组合出复杂行为。大量实验表明，Qwen-RobotNav在主要导航基准测试中均取得了新的最优结果。该模型在参数规模从2B扩展到8B时展现出良好的可扩展性，联合多任务训练形成了跨任务族迁移的共享空间规划基础，并在不同环境中对真实世界机器人展现出强大的零样本泛化能力。

---

