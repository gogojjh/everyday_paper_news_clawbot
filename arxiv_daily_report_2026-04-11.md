# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-04-11 08:04

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 5/20 篇提供

**🌟 Highlight**: 12 篇 | **📌 Poster**: 8 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. LAMP: Lift Image-Editing as General 3D Priors for Open-world Manipulation

- **作者**: Jingjing Wang, Zhengdong Hong, Chong Bao, Yuke Zhu, Junhan Sun, Guofeng Zhang ⭐
  - **高亮作者**: Yuke Zhu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.08475v1)
- **发表日期**: 2026-04-09
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2604.08475v1](http://arxiv.org/abs/2604.08475v1)
- **📥 PDF**: 已下载至本地 (`2604.08475v1_LAMP_Lift_Image-Editing_as_General_3D_Priors_for_Open-world_Manipulation.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://zju3dv.github.io/LAMP/.
- **中文摘要**: 在开放世界中实现类人泛化能力仍然是机器人操作领域的根本性挑战。现有的基于学习的方法，包括强化学习、模仿学习和视觉-语言-动作模型（VLAs），在面对新任务和未见环境时往往表现不佳。另一条有前景的研究路径是探索能够捕捉细粒度空间与几何关系的通用表征，以支持开放世界操作。虽然大语言模型（LLMs）和视觉语言模型（VLMs）基于语言或标注的二维表征提供了强大的语义推理能力，但其有限的三维感知能力制约了它们在细粒度操作任务中的应用。为此，我们提出LAMP方法，通过将图像编辑技术提升为三维先验知识，提取物体间的三维变换作为连续且具有几何感知的表征。我们的核心洞见在于：图像编辑过程本身编码了丰富的二维空间线索，将这些隐式线索提升至三维变换层面，能为开放世界操作提供细粒度且精确的指导。大量实验表明，该方法能够生成精确的三维变换，并在开放世界操作中实现了强大的零样本泛化能力。项目页面：https://zju3dv.github.io/LAMP/。

---

### 2. ViVa: A Video-Generative Value Model for Robot Reinforcement Learning

- **作者**: Jindi Lv, Hao Li, Jie Li, Yifei Nie, Fankun Kong, Yang Wang, Xiaofeng Wang, Zheng Zhu, Chaojun Ni, Qiuping Deng, Hengtao Li, Jiancheng Lv, Guan Huang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.08168v1)
- **发表日期**: 2026-04-09
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2604.08168v1](http://arxiv.org/abs/2604.08168v1)
- **📥 PDF**: 已下载至本地 (`2604.08168v1_ViVa_A_Video-Generative_Value_Model_for_Robot_Reinforcement_Learning.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作模型通过大规模预训练推动了机器人操作技术的发展，但受限于部分可观测性和延迟反馈，实际部署仍面临挑战。强化学习通过价值函数评估任务进度并指导策略优化来解决这一问题。然而，现有基于视觉语言模型构建的价值模型难以捕捉时序动态，导致长周期任务中的价值估计不可靠。本文提出ViVa——一种视频生成式价值模型，通过改造预训练视频生成器实现价值估计。该模型以当前观测数据和机器人本体感知为输入，联合预测未来本体感知状态及当前状态的标量价值。通过利用预训练视频生成器的时空先验知识，我们的方法将价值估计建立在可预测的具身动态基础上，突破静态快照的局限，实现价值与前瞻能力的本质耦合。将ViVa集成至RECAP系统后，在现实世界箱体装配任务中取得显著提升。三项任务的定性分析证实，ViVa能生成更可靠的价值信号，准确反映任务进度。通过利用视频语料库的时空先验知识，ViVa还能泛化至新物体，彰显了视频生成模型在价值估计领域的应用潜力。

---

### 3. HEX: Humanoid-Aligned Experts for Cross-Embodiment Whole-Body Manipulation

- **作者**: Shuanghao Bai, Meng Li, Xinyuan Lv, Jiawei Wang, Xinhua Wang, Fei Liao, Chengkai Hou, Langzhe Gu, Wanqi Zhou, Kun Wu, Ziluo Ding, Zhiyuan Xu, Lei Sun, Shanghang Zhang, Zhengping Che, Jian Tang, Badong Chen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.07993v1)
- **发表日期**: 2026-04-09
- **匹配关键词**: vision-language-action, whole-body manipulation, VLA
- **arXiv**: [2604.07993v1](http://arxiv.org/abs/2604.07993v1)
- **📥 PDF**: 已下载至本地 (`2604.07993v1_HEX_Humanoid-Aligned_Experts_for_Cross-Embodiment_Whole-Body_Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 人类通过协调的全身控制实现复杂操作，而大多数视觉-语言-动作模型将机器人身体部位视为独立单元，使得高自由度人形机器人控制充满挑战且常不稳定。本文提出HEX框架——一种以状态为中心的双足人形机器人协调操作方案。该框架构建了人形机器人对齐的通用状态表征，支持跨异构实体的可扩展学习，并通过混合专家统一本体感知预测器，从大规模多实体轨迹数据中建模全身协调与时序运动动态。为高效捕捉时序视觉上下文，HEX采用轻量级历史令牌总结过往观测，避免推理过程中重复编码历史图像。进一步通过残差门控融合机制与流匹配动作头，自适应整合视觉-语言线索与本体感知动态以生成动作。在真实世界人形机器人操作任务上的实验表明，HEX在任务成功率与泛化能力上达到最优性能，尤其在快速反应与长时程场景中表现突出。

---

### 4. ReconPhys: Reconstruct Appearance and Physical Attributes from Single Video

- **作者**: Boyuan Wang, Xiaofeng Wang, Yongkang Li, Zheng Zhu, Yifan Chang, Angen Ye, Guosheng Zhao, Chaojun Ni, Guan Huang, Yijie Ren, Yueqi Duan, Xingang Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.07882v1)
- **发表日期**: 2026-04-09
- **匹配关键词**: 3D gaussian splatting, gaussian splatting
- **arXiv**: [2604.07882v1](http://arxiv.org/abs/2604.07882v1)
- **📥 PDF**: 已下载至本地 (`2604.07882v1_ReconPhys_Reconstruct_Appearance_and_Physical_Attributes_from_Single_Video.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 重建具有物理合理性的非刚性物体仍是一项重大挑战。现有方法通过可微分渲染进行逐场景优化，虽能恢复几何结构与动态特性，但需要昂贵的参数调整或人工标注，限制了其实用性与泛化能力。为此，我们提出ReconPhys——首个从前向传播框架，能够从单目视频中联合学习物理属性估计与三维高斯溅射重建。该方法采用通过自监督策略训练的双分支架构，无需真实物理标签。给定视频序列，ReconPhys可同步推断几何形状、外观表现及物理属性。在大规模合成数据集上的实验表明其卓越性能：在预测未来帧方面，本方法达到21.64 PSNR，优于现有优化基准方法的13.27；同时将倒角距离从0.349降至0.004。尤为关键的是，ReconPhys能实现快速推理（<1秒），而现有方法需要数小时，这为机器人学和图形学领域快速生成可直接用于仿真的数字资产提供了便利。

---

### 5. GEAR: GEometry-motion Alternating Refinement for Articulated Object Modeling with Gaussian Splatting

- **作者**: Jialin Li, Bin Fu, Ruiping Wang, Xilin Chen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.07728v1)
- **发表日期**: 2026-04-09
- **匹配关键词**: gaussian splatting, articulated object
- **arXiv**: [2604.07728v1](http://arxiv.org/abs/2604.07728v1)
- **📥 PDF**: 已下载至本地 (`2604.07728v1_GEAR_GEometry-motion_Alternating_Refinement_for_Articulated_Object_Modeling_with_Gaussian_Splatting.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 高保真交互式数字资产对具身智能与机器人交互至关重要，然而铰接物体因其复杂的结构及几何-运动耦合关系，重建工作仍面临挑战。现有方法在几何-运动联合优化中存在不稳定性，且在复杂多关节或分布外物体上的泛化能力有限。为解决这些问题，我们提出GEAR——一种基于高斯溅射表示的EM风格交替优化框架，将几何与运动作为相互依存的组件进行联合建模。GEAR将部件分割视为隐变量，关节运动参数作为显式变量，通过交替优化提升收敛性与几何-运动一致性。为在不牺牲泛化能力的前提下提升部件分割质量，我们利用基础二维分割模型提供多视角部件先验，并采用弱监督约束对隐变量进行正则化。在多个基准测试集及我们新构建的GEAR-Multi数据集上的实验表明，GEAR在几何重建与运动参数估计方面达到最先进水平，尤其在具有多个可动部件的复杂铰接物体上表现突出。

---

### 6. Vision-Language Navigation for Aerial Robots: Towards the Era of Large Language Models

- **作者**: Xingyu Xia, Lekai Zhou, Yujie Tang, Xiaozhou Zhu, Hai Zhu, Wen Yao
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.07705v1)
- **发表日期**: 2026-04-09
- **匹配关键词**: navigation, vision-and-language navigation, VLN
- **arXiv**: [2604.07705v1](http://arxiv.org/abs/2604.07705v1)
- **📥 PDF**: 已下载至本地 (`2604.07705v1_Vision-Language_Navigation_for_Aerial_Robots_Towards_the_Era_of_Large_Language_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 空中视觉语言导航旨在使无人机能够通过将语言与视觉感知相结合，理解自然语言指令并在复杂三维环境中自主导航。本文对该领域进行了批判性分析性综述，特别关注近期大语言模型与视觉语言模型的融合应用。我们首先正式定义空中视觉语言导航问题，并以单指令和对话式交互范式作为基础框架。随后将现有方法归纳为五类体系架构：序列到序列与注意力机制方法、端到端大语言模型/视觉语言模型方法、分层方法、多智能体方法以及对话式导航方法。针对每类方法，我们系统分析了设计原理、技术权衡与报告性能。本文批判性评估了空中视觉语言导航的评估体系，包括数据集、仿真平台和评价指标，并指出其在规模、环境多样性、现实世界关联性及指标覆盖度方面的不足。通过整合跨方法在共享基准上的比较结果，我们深入剖析了离散与连续动作、端到端与分层设计、仿真与现实差距等关键架构权衡。最后凝练出七大开放性挑战：长时程指令关联、视点鲁棒性、可扩展空间表征、连续六自由度动作执行、机载部署、基准标准化及多无人机集群导航，并结合综述中的实证依据为每个方向提出了具体研究路径。

---

### 7. HY-Embodied-0.5: Embodied Foundation Models for Real-World Agents

- **作者**: Tencent Robotics X, HY Vision Team, :, Xumin Yu, Zuyan Liu, Ziyi Wang, He Zhang, Yongming Rao, Fangfu Liu, Yani Zhang, Ruowen Zhao, Oran Wang, Yves Liang, Haitao Lin, Minghui Wang, Yubo Dong, Kevin Cheng, Bolin Ni, Rui Huang, Han Hu, Zhengyou Zhang, Linus, Shunyu Yao
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.07430v1)
- **发表日期**: 2026-04-08
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2604.07430v1](http://arxiv.org/abs/2604.07430v1)
- **📥 PDF**: 已下载至本地 (`2604.07430v1_HY-Embodied-0.5_Embodied_Foundation_Models_for_Real-World_Agents.pdf`)
- **🔓 开源**: GITHUB, CODE
  - 链接：https://github.com/Tencent-Hunyuan/HY-Embodied.
- **中文摘要**: 我们推出HY-Embodied-0.5系列基础模型，这是专为现实世界具身智能体设计的模型家族。为弥合通用视觉语言模型与具身智能体需求之间的差距，我们开发的模型旨在增强具身智能所需的核心能力：时空视觉感知能力，以及面向预测、交互与规划的高级具身推理能力。HY-Embodied-0.5系列包含两个主要变体：面向边缘部署的20亿激活参数高效模型，以及针对复杂推理任务的320亿激活参数强大模型。为支撑具身任务所需的细粒度视觉感知，我们采用混合专家架构实现模态专属计算。通过引入潜在标记，该设计有效增强了模型的感知表征能力。为提升推理能力，我们提出迭代式自我进化的后训练范式。此外，我们采用策略蒸馏技术将大模型的先进能力迁移至小规模变体，从而最大化紧凑模型的性能潜力。在涵盖视觉感知、空间推理与具身理解的22个基准测试中进行的广泛评估证明了我们方法的有效性：MoT-20亿模型在16项基准测试中超越同规模先进模型，而320亿变体则达到与Gemini 3.0 Pro等前沿模型相当的性能。在下游机器人控制实验中，我们依托稳健的视觉语言基础训练出高效的视觉语言动作模型，在真实物理评估中取得显著成果。代码与模型已在https://github.com/Tencent-Hunyuan/HY-Embodied开源。

---

### 8. Mem3R: Streaming 3D Reconstruction with Hybrid Memory via Test-Time Training

- **作者**: Changkun Liu, Jiezhi Yang, Zeman Li, Yuan Deng, Jiancong Guo, Luca Ballan
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.07279v1)
- **发表日期**: 2026-04-08
- **匹配关键词**: 3D reconstruction, 3d reconstruction
- **arXiv**: [2604.07279v1](http://arxiv.org/abs/2604.07279v1)
- **📥 PDF**: 已下载至本地 (`2604.07279v1_Mem3R_Streaming_3D_Reconstruction_with_Hybrid_Memory_via_Test-Time_Training.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://lck666666.github.io/Mem3R/
- **中文摘要**: 流式三维感知技术特别适用于机器人和增强现实领域，这些场景需要高效且稳定地处理长时间视觉流。近期出现的循环模型通过维持固定大小的状态并实现线性时间推理，提供了有前景的解决方案，但由于压缩潜在记忆容量有限，这些模型在长序列中常面临漂移累积和时间遗忘问题。我们提出Mem3R——一种采用混合记忆设计的流式三维重建模型，通过将相机跟踪与几何映射解耦来提升长序列的时间一致性。在相机跟踪方面，Mem3R采用由轻量级多层感知机实现的隐式快速权重记忆，并通过测试时训练进行更新。在几何映射方面，Mem3R维持基于令牌的显式固定大小状态。与CUT3R相比，该设计不仅显著提升了长序列性能，还将模型参数量从7.93亿减少至6.44亿。Mem3R兼容为CUT3R开发的现有即插即用状态更新策略。具体而言，在500至1000帧序列上，与TTT3R集成后相比基础实现将绝对轨迹误差降低达39%。这些改进还延伸至其他下游任务，包括视频深度估计和三维重建，同时保持恒定的GPU内存使用量和相当的推理吞吐量。项目页面：https://lck666666.github.io/Mem3R/

---

### 9. RichMap: A Reachability Map Balancing Precision, Efficiency, and Flexibility for Rich Robot Manipulation Tasks

- **作者**: Yupu Lu, Yuxiang Ma, Jia Pan
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.06778v1)
- **发表日期**: 2026-04-08
- **匹配关键词**: diffusion policy
- **arXiv**: [2604.06778v1](http://arxiv.org/abs/2604.06778v1)
- **📥 PDF**: 已下载至本地 (`2604.06778v1_RichMap_A_Reachability_Map_Balancing_Precision,_Efficiency,_and_Flexibility_for_Rich_Robot_Manipulat.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 本文提出RichMap，一种高精度可达性地图表示方法，旨在为多样化机器人操作任务平衡效率与灵活性。通过优化经典的网格化结构，我们提出一种精简方法，在保持结构灵活性的同时，其性能接近紧凑型地图形式（如RM4D）。该方法利用$\mathbb{S}^2$（或$SO(3)$）的理论容量边界确保严格覆盖，并采用异步流水线实现高效构建。我们通过综合指标验证地图性能，追求高预测精度（$>98\%$）、低误报率（$1\sim2\%$）及快速批量查询（约15$μ$s/次查询）。我们将该框架扩展应用于通过最大均值差异（MMD）度量量化机器人工作空间相似性，并展示基于能量的扩散策略迁移引导方法，在方块推动实验中实现跨实体场景最高达$26\%$的性能提升。

---

### 10. Scal3R: Scalable Test-Time Training for Large-Scale 3D Reconstruction

- **作者**: Tao Xie, Peishan Yang, Yudong Jin, Yingfeng Cai, Wei Yin, Weiqiang Ren, Qian Zhang, Wei Hua, Sida Peng, Xiaoyang Guo, Xiaowei Zhou
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.08542v1)
- **发表日期**: 2026-04-09
- **匹配关键词**: 3D reconstruction, 3d reconstruction
- **arXiv**: [2604.08542v1](http://arxiv.org/abs/2604.08542v1)
- **📥 PDF**: 已下载至本地 (`2604.08542v1_Scal3R_Scalable_Test-Time_Training_for_Large-Scale_3D_Reconstruction.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 本文针对从长视频序列进行大规模三维场景重建的任务展开研究。近期前馈式重建模型通过直接从RGB图像回归三维几何结构，无需显式三维先验或几何约束，已展现出良好效果。然而，由于内存容量有限且难以有效捕捉全局上下文线索，这些方法在长序列处理中往往难以保持重建精度与一致性。相比之下，人类能够自然地利用对场景的全局理解来指导局部感知。受此启发，我们提出了一种新颖的神经全局上下文表示方法，能够高效压缩并保留长距离场景信息，使模型能够利用广泛的上下文线索来提升重建精度与一致性。该上下文表示通过一组轻量级神经子网络实现，这些子网络在测试阶段通过自监督目标快速适配，从而在不显著增加计算开销的情况下大幅提升内存容量。在包括KITTI里程计~\cite{Geiger2012CVPR}和牛津尖塔~\cite{tao2025spires}数据集在内的多个大规模基准测试上的实验表明，我们的方法在处理超大规模场景时具有显著优势，在保持高效性的同时实现了领先的位姿精度和最优的三维重建精度。代码发布于https://zju3dv.github.io/scal3r。

---

### 11. BLaDA: Bridging Language to Functional Dexterous Actions within 3DGS Fields

- **作者**: Fan Yang, Wenrui Chen, Guorun Yan, Ruize Liao, Wanjun Jia, Dongsheng Luo, Kailun Yang, Zhiyong Li, Yaonan Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.08410v1)
- **发表日期**: 2026-04-09
- **匹配关键词**: dexterous grasping, gaussian splatting, VLA, 3D gaussian splatting, affordance
- **arXiv**: [2604.08410v1](http://arxiv.org/abs/2604.08410v1)
- **📥 PDF**: 已下载至本地 (`2604.08410v1_BLaDA_Bridging_Language_to_Functional_Dexterous_Actions_within_3DGS_Fields.pdf`)
- **🔓 开源**: GITHUB, CODE
  - 链接：https://github.com/PopeyePxx/BLaDA.
- **中文摘要**: 在非结构化环境中，功能性灵巧抓取需要语义理解、精确的三维功能定位与物理可解释执行的紧密结合。模块化分层方法相比端到端视觉语言动作模型具有更强的可控性与可解释性，但现有方法仍依赖预定义的功能可供性标签，且缺乏功能性灵巧操作所需的语义-位姿紧密耦合机制。为此，我们提出BLaDA（三维高斯场中语言到灵巧动作的桥梁）——一个可解释的零样本框架，将开放词汇指令转化为功能性灵巧操作的感知与控制约束。BLaDA通过知识引导语言解析模块，首先将自然语言解析为结构化六元组操作约束，建立可解释的推理链条。为实现位姿一致的空间推理，我们提出三角功能点定位模块，利用三维高斯泼溅作为连续场景表征，在三角几何约束下识别功能区域。最后，三维关键点抓取矩阵变换执行模块将这些语义-几何约束解码为物理可行的腕部位姿与手指级指令。在复杂基准测试上的大量实验表明，BLaDA在不同类别与任务的功能可供性定位精度和功能性操作成功率方面均显著优于现有方法。代码将在https://github.com/PopeyePxx/BLaDA公开。

---

### 12. SurfelSplat: Learning Efficient and Generalizable Gaussian Surfel Representations for Sparse-View Surface Reconstruction

- **作者**: Chensheng Dai, Shengjun Zhang, Min Chen, Yueqi Duan
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.08370v1)
- **发表日期**: 2026-04-09
- **匹配关键词**: 3D gaussian splatting, gaussian splatting
- **arXiv**: [2604.08370v1](http://arxiv.org/abs/2604.08370v1)
- **📥 PDF**: 已下载至本地 (`2604.08370v1_SurfelSplat_Learning_Efficient_and_Generalizable_Gaussian_Surfel_Representations_for_Sparse-View_Sur.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 3D高斯溅射（3DGS）在三维场景重建中展现出卓越性能。除新颖视角合成外，该方法在多视角表面重建领域同样展现出巨大潜力。现有研究多采用基于优化的重建流程，能够实现精确完整的表面提取，但通常需要密集的输入视角且单场景优化耗时较长。为突破这些局限，我们提出SurfelSplat——一种前馈式框架，能够从稀疏视角图像生成高效且可泛化的像素对齐高斯面元表征。研究发现，传统前馈结构难以恢复高斯面元的精确几何属性，因为像素对齐基元的空间频率超过了奈奎斯特采样率。为此，我们提出基于奈奎斯特采样定理的跨视角特征聚合模块：首先通过空间采样率引导的低通滤波器调整高斯面元的几何形态，随后将滤波后的面元投影至所有输入视角以获取跨视角特征关联，最后通过专门设计的特征融合网络处理这些关联，从而回归出具有精确几何特征的高斯面元。在DTU重建基准测试中的大量实验表明，我们的模型取得了与前沿方法相当的结果，可在1秒内预测高斯面元，在无需昂贵单场景训练的情况下实现百倍加速。

---

## 📌 Poster

*其他相关研究*

---

### 1. A Soft Robotic Interface for Chick-Robot Affective Interactions

- **作者**: Jue Chen, Alexander Mielke, Kaspar Althoefer, Elisabetta Versace
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.08443v1)
- **发表日期**: 2026-04-09
- **匹配关键词**: exploration
- **arXiv**: [2604.08443v1](http://arxiv.org/abs/2604.08443v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 动物-机器人交互在福利应用中的潜力，取决于动物对机器人代理的社会相关性、非威胁性和潜在吸引力的感知程度（即接受度）。本研究针对刚孵化的雏鸡开发了一种以动物为中心的软体机器人情感交互界面。该软界面通过可控方式提供温暖触感、呼吸节律式形变以及类面部视觉刺激等安全线索。通过视频追踪记录雏鸡自发接近与接触行为，我们评估了雏鸡对交互界面的接受度及雏鸡-机器人互动表现。总体而言，雏鸡持续接近并在界面周围停留时间逐渐增加，表明其对设备具有良好接受度。在不同布局实验中，雏鸡对温暖热刺激表现出强烈偏好，且随时间推移持续增强；类面部视觉线索能引发快速稳定的偏好，显著加速雏鸡对触觉界面的初始接近行为；呼吸节律线索虽未引发明显偏好，但亦未触发回避反应，为后续研究提供了探索空间。这些发现将情感界面概念成功应用于动物-机器人交互领域，证明适宜的软体触感、热刺激与视觉线索能够有效维持早期雏鸡-机器人互动。本研究为动物福利与神经科学研究中的多模态机器人设备设计，建立了可靠的评估范式与安全基准。

---

### 2. A Unified Multi-Layer Framework for Skill Acquisition from Imperfect Human Demonstrations

- **作者**: Zi-Qi Yang, Mehrdad R. Kermani
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.08341v1)
- **发表日期**: 2026-04-09
- **匹配关键词**: HRI, human-robot interaction
- **arXiv**: [2604.08341v1](http://arxiv.org/abs/2604.08341v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 当前用于技能教学的人机交互系统较为零散，现有文献中的方法未能提供一个同时具备高效性、直观性和普适安全性的统一框架。本文提出了一种新颖的分层控制框架，通过在通用机器人柔顺性基础上构建稳健的柔顺式示教学习，从根本上解决了这一关键问题。该框架采用三层递进式互联结构：首先提出一种实时示教学习方法，能够通过单次演示同时学习轨迹与可变阻抗，显著提升教学效率与动作复现精度；其次为确保高质量直观的力导引示教，设计了零空间优化策略，主动管理奇异性并在人类演示过程中提供一致的交互体验；最后为实现广义安全性，提出基础性零空间柔顺方法，使机器人全身能在不干扰主任务执行的前提下，柔顺适应学习完成后的外部交互。这一最终贡献将系统转化为超越末端执行器专用场景的通用人机交互平台。我们在7自由度KUKA LWR机器人上通过全面对比实验验证了完整框架，结果表明该系统为广泛的人机协作任务提供了更安全、更直观、更高效的一体化解决方案。

---

### 3. EMMa: End-Effector Stability-Oriented Mobile Manipulation for Tracked Rescue Robots

- **作者**: Yifei Wang, Hao Zhang, Jidong Huang, Shuohang Fang, Haoyao Chen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.08292v1)
- **发表日期**: 2026-04-09
- **匹配关键词**: mobile manipulator, mobile manipulation
- **arXiv**: [2604.08292v1](http://arxiv.org/abs/2604.08292v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 在救援任务中实现履带式移动机械臂的自主操作，不仅需要确保机器人运动的可达性与安全性，还需满足多样化任务需求下末端执行器操作的稳定性。然而，现有研究在规划与控制层面均忽视了末端执行器的诸多运动特性。本文提出一种面向履带式移动机械臂的运动生成框架，旨在复杂救援场景中实现稳定的末端执行器操作。该框架构建了耦合末端执行器与移动平台状态的协同路径优化模型，并设计了紧凑的代价/约束表达形式以降低非线性程度与计算复杂度。此外，开发了结合前馈补偿与反馈调节的隔离控制方案，以实现机器人的协同路径跟踪。通过在救援场景中进行大量仿真与实物实验证明，所提框架在任务成功率、末端执行器运动稳定性等关键指标上均优于现有先进方法，验证了其在复杂移动操作任务中的有效性与鲁棒性。

---

### 4. Incremental Residual Reinforcement Learning Toward Real-World Learning for Social Navigation

- **作者**: Haruto Nagahisa, Kohei Matsumoto, Yuki Tomita, Yuki Hyodo, Ryo Kurazume
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.07945v1)
- **发表日期**: 2026-04-09
- **匹配关键词**: navigation, social navigation
- **arXiv**: [2604.07945v1](http://arxiv.org/abs/2604.07945v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 随着移动机器人需求的持续增长，社交导航已成为一项关键任务，推动了深度强化学习方法的深入研究。然而，由于不同地区的行人动态和社会规范差异显著，仿真难以全面覆盖所有现实场景。现实世界强化学习——即智能体直接在物理环境中运行并学习——为解决这一问题提供了可行方案。但该方法面临重大挑战，特别是边缘设备计算资源受限与学习效率问题。本研究提出增量残差强化学习方法，该方法将无需经验回放缓冲区或批量更新的轻量级增量学习，与通过仅针对基础策略的残差进行训练以提升学习效率的残差强化学习相结合。仿真实验表明，尽管缺乏经验回放缓冲区，该方法的性能仍与传统基于缓冲区的方法相当，并优于现有增量学习方法。此外，现实世界实验证实，该方法能使机器人通过实际环境学习有效适应先前未接触过的新环境。

---

### 5. CMP: Robust Whole-Body Tracking for Loco-Manipulation via Competence Manifold Projection

- **作者**: Ziyang Cheng, Haoyu Wei, Hang Yin, Xiuwei Xu, Bingyao Yu, Jie Zhou, Jiwen Lu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.07457v1)
- **发表日期**: 2026-04-08
- **匹配关键词**: mobile manipulator
- **arXiv**: [2604.07457v1](http://arxiv.org/abs/2604.07457v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 虽然腿式移动机械臂的解耦控制方案已展现出鲁棒性，但在传感器噪声或不可行用户指令引发的分布外输入情况下，用于追踪全局末端执行器位姿的整体全身控制策略学习仍显脆弱。为在不牺牲任务性能与连续性的前提下提升对这些扰动的鲁棒性，我们提出能力流形投影方法。具体而言，我们采用帧级安全方案，将无限时域安全约束转化为计算高效的单步流形容纳问题。为实现该能力流形的实例化，我们构建下界安全估计器以区分训练分布之外的未掌握意图。随后引入同构潜在空间，使流形几何结构与安全概率对齐，从而实现对任意分布外意图的高效O(1)级无缝防御。实验表明，在基线方法遭遇灾难性失效的典型分布外场景中，能力流形投影方法将生存率提升高达10倍，同时保持低于10%的追踪性能损失。值得注意的是，该系统展现出"尽力而为"的涌现泛化行为，通过遵循能力边界逐步实现分布外目标。实验视频详见：https://shepherd1226.github.io/CMP。

---

### 6. TAMEn: Tactile-Aware Manipulation Engine for Closed-Loop Data Collection in Contact-Rich Tasks

- **作者**: Longyan Wu, Jieji Ren, Chenghang Jiang, Junxi Zhou, Shijia Peng, Ran Huang, Guoying Gu, Li Chen, Hongyang Li
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.07335v1)
- **发表日期**: 2026-04-08
- **匹配关键词**: bimanual manipulation
- **arXiv**: [2604.07335v1](http://arxiv.org/abs/2604.07335v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: CODE
- **中文摘要**: 手持式范式为收集大规模机器人操作演示提供了一种高效直观的方式。然而，通过这类方法实现接触密集型的双手操作仍面临关键挑战，硬件适应性与数据有效性成为主要制约因素。现有硬件设计通常局限于特定夹爪结构，且常在追踪精度与便携性之间难以兼顾。此外，演示过程中缺乏在线可行性检查导致动作复现性较差。更重要的是，当前手持式设备难以在机器人执行过程中收集交互式恢复数据，缺乏鲁棒策略优化所需的真实触觉信息。为弥补这些不足，我们提出TAMEn——一种面向接触密集型任务的触觉感知操作引擎，支持闭环数据采集。该系统采用跨形态可穿戴接口设计，能快速适配异构夹爪。为平衡数据质量与环境多样性，我们构建了双模态采集流程：精度模式借助动作捕捉技术实现高保真演示，便携模式则利用基于VR的追踪技术实现野外采集及触觉可视化恢复遥操作。基于此硬件平台，我们将大规模触觉预训练、任务特异性双手演示和人机协同恢复数据整合为金字塔结构的数据体系，实现闭环策略优化。实验表明，我们的可行性感知流程显著提升了演示复现性，所提出的视觉-触觉学习框架将多种双手操作任务的成功率从34%提升至75%。我们进一步开源硬件设计与数据集，以促进研究可复现性并推动视觉-触觉操作领域的发展。

---

### 7. Robust Quadruped Locomotion via Evolutionary Reinforcement Learning

- **作者**: Brian McAteer, Karl Mason
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.07224v1)
- **发表日期**: 2026-04-08
- **匹配关键词**: exploration
- **arXiv**: [2604.07224v1](http://arxiv.org/abs/2604.07224v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 深度强化学习在四足机器人运动控制领域近期取得显著进展，但仿真环境中训练的策略在环境变化时往往难以迁移。进化强化学习通过将基于梯度的策略优化与群体驱动探索相结合，旨在突破这一局限。本研究在模拟行走任务中评估了四种方法：DDPG、TD3以及两种基于交叉熵的变体CEM-DDPG和CEM-TD3。所有智能体均在平坦地形训练，随后在训练域和未接触过的崎岖地形进行测试。在平坦地面测试中，TD3在标准深度强化学习基线方法中表现最佳，平均奖励达5927.26；而CEM-TD3在训练与评估阶段获得最高综合奖励17611.41。在崎岖地形迁移测试中，深度强化学习方法性能急剧下降：DDPG获得-1016.32奖励，TD3为-99.73，而进化变体则保持了大部分性能。CEM-TD3以19574.33的平均奖励记录展现出最强的迁移性能。这些发现表明，融入进化搜索能有效减少运动控制任务中的过拟合现象，提升策略鲁棒性，尤其在部署环境与训练条件存在差异时效果显著。

---

### 8. Flow Motion Policy: Manipulator Motion Planning with Flow Matching Models

- **作者**: Davood Soleymanzadeh, Xiao Liang, Minghui Zheng
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.07084v1)
- **发表日期**: 2026-04-08
- **匹配关键词**: motion planning
- **arXiv**: [2604.07084v1](http://arxiv.org/abs/2604.07084v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 开环端到端神经运动规划器近期被提出，用于改进机器人操作臂的运动规划。这些方法能够直接从传感器观测进行规划，无需在规划过程中依赖特权碰撞检测器。然而，现有方法在多次运行中对给定工作空间通常仅生成单一轨迹，且未能利用其开环结构进行推理时优化。为突破这一局限，我们提出流运动策略——一种面向机器人操作臂的开环端到端神经运动规划器，该方法通过流匹配方法的随机生成式建模框架，有效捕捉规划数据集中固有的多模态特性。通过对可行轨迹分布进行建模，流运动策略实现了高效的推理时N选优采样。该方法可生成多条端到端候选轨迹，在规划后评估其碰撞状态，并执行首个无碰撞解。我们将流运动策略与代表性采样基及神经运动规划方法进行基准测试。评估结果表明，流运动策略显著提升了规划成功率与效率，验证了随机生成式策略在端到端运动规划及推理时优化中的有效性。实验评估视频可通过此\href{https://zh.engr.tamu.edu/wp-content/uploads/sites/310/2026/03/FMP-Website.mp4}{链接}观看。

---

