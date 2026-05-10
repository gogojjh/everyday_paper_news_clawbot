# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-05-10 08:03

**今日新增**: 14 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 4/14 篇提供

**🌟 Highlight**: 6 篇 | **📌 Poster**: 8 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation

- **作者**: Yushan Liu, Peibo Sun, Shoujie Li, Yifan Xie, Lingfeng Zhang, Xintao Chao, Shiyuan Dong, Fang Chen, Xiao-Ping Zhang, Wenbo Ding
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.06481v1)
- **发表日期**: 2026-05-07
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2605.06481v1](http://arxiv.org/abs/2605.06481v1)
- **📥 PDF**: 已下载至本地 (`2605.06481v1_OA-WAM_Object-Addressable_World_Action_Model_for_Robust_Robot_Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 世界动作模型（WAMs）通过联合预测场景演变与机器人动作来增强视觉-语言-动作策略，但现有方法通常将预测的世界表示为整体图像、视频令牌或全局隐变量。当指令指向特定物体时，尤其是在物体身份与上下文纠缠的场景偏移下，这些表示难以被动作解码器处理。我们提出OA-WAM——一种面向鲁棒机器人操作的可寻址物体世界动作模型。OA-WAM将每帧分解为N+1个槽状态，包含一个机器人槽和N个物体槽。每个槽包含一个持久化地址向量和一个时变内容向量，并与文本、图像、本体感知及历史动作令牌以块因果序列方式融合。世界头预测下一帧槽状态，而流匹配动作头在同一前向过程中解码16步连续动作块。通过仅使用地址键路由跨槽注意力，并在每个Transformer层重置地址切片，可寻址性得以实现——在不增加额外令牌的情况下，将"作用于哪个物体"与"该物体当前是什么"分离。OA-WAM在LIBERO（97.8%）和SimplerEnv（79.3%）上匹配强VLA和WAM基线，在最具相关性的LIBERO-Plus几何轴上达到最优性能，并在七轴综合指标中保持竞争力。因果槽干预测试产生0.87的交换绑定余弦值，而整体基线最高仅为0.09。这些结果表明，可寻址物体状态为场景扰动下的鲁棒世界动作建模提供了有效接口。

---

### 2. Toward Visually Realistic Simulation: A Benchmark for Evaluating Robot Manipulation in Simulation

- **作者**: Yixin Zhu, Zixiong Wang, Jian Yang, Jin Xie, Jingyi Yu, Jiayuan Gu, Beibei Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.06311v1)
- **发表日期**: 2026-05-07
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2605.06311v1](http://arxiv.org/abs/2605.06311v1)
- **📥 PDF**: 已下载至本地 (`2605.06311v1_Toward_Visually_Realistic_Simulation_A_Benchmark_for_Evaluating_Robot_Manipulation_in_Simulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 对机器人操作策略的可靠仿真评估可作为真实世界性能的高保真代理。现有基准虽覆盖广泛任务类别，但缺乏视觉真实性，导致仿真与现实之间存在巨大领域差距，削弱了基于仿真的评估对真实世界性能的预测可靠性。为缩小仿真到现实的视觉差距，我们开展系统性分析以分离光照与材质的影响。结果表明，这些因素在几何推理与空间定位中起关键作用，却常被现有基准所忽视。基于此分析，我们提出VISER——一个用于仿真中评估机器人操作的视觉真实基准。VISER包含基于物理渲染（PBR）材质的1000余个3D资产的高保真数据集，以及通过精心布局或生成方式利用这些资产构建的3D场景。为此，我们提出自动化流水线，借助多模态大语言模型（MLLMs）实现材质感知的部件分割与材质检索，支持物理合理资产的可扩展生成。基于高保真3D资产数据集，我们构建了抓取、放置、长时域任务等多样化评估任务，实现视觉-语言-动作（VLA）模型的可扩展可复现评估。该基准在仿真与真实世界性能间展现出强相关性，不同策略的平均皮尔逊相关系数达0.92。

---

### 3. VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts

- **作者**: Yuhua Jiang, Junjie Lu, Xinyao Qin, Xiaoyu Chen, Kaixin Wang, Feifei Gao, Li Zhao
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.06175v1)
- **发表日期**: 2026-05-07
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2605.06175v1](http://arxiv.org/abs/2605.06175v1)
- **📥 PDF**: 已下载至本地 (`2605.06175v1_VLA-GSE_Boosting_Parameter-Efficient_Fine-Tuning_in_VLA_with_Generalized_and_Specialized_Experts.pdf`)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/YuhuaJiang2002/VLA-GSE
- **中文摘要**: 视觉-语言-动作（VLA）模型继承了预训练视觉-语言骨干网络的丰富视觉语义先验知识，但将其适配到机器人控制仍具有挑战性。全参数微调（FFT）容易在机器人下游数据上过拟合，并导致预训练视觉-语言能力的灾难性遗忘。参数高效微调（PEFT）能更好地保留预训练知识，然而现有PEFT方法仍难以有效适配机器人控制任务。为解决这一难题，我们提出VLA-GSE——一种参数高效的VLA微调框架，在保留PEFT知识保留优势的同时提升控制适配能力。具体而言，VLA-GSE（通用与专用专家）通过谱分解冻结的骨干网络进行初始化，将主导奇异分量分配给通用专家（共享专家），将不相交的残差分量分配给专用专家（路由专家）。这种分解方式在固定可训练参数预算下提升了适配能力。在可比参数预算下，VLA-GSE仅更新全模型参数的2.51%，却持续优于强FFT和PEFT基线方法。该方法在LIBERO-Plus上实现81.2%的平均零样本成功率，在多模态理解基准测试中与LoRA相当地保留预训练VLM能力，并在多种分布偏移场景下提升真实世界操作成功率。代码已开源：https://github.com/YuhuaJiang2002/VLA-GSE

---

### 4. MobileEgo Anywhere: Open Infrastructure for long horizon egocentric data on commodity hardware

- **作者**: Senthil Palanisamy, Abhishek Anand, Satpal Singh Rathor, Pratyush Patnaik, Shubhanshu Khatana
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.05945v1)
- **发表日期**: 2026-05-07
- **匹配关键词**: vision language action, vision language action model, VLA
- **arXiv**: [2605.05945v1](http://arxiv.org/abs/2605.05945v1)
- **📥 PDF**: 已下载至本地 (`2605.05945v1_MobileEgo_Anywhere_Open_Infrastructure_for_long_horizon_egocentric_data_on_commodity_hardware.pdf`)
- **🔓 开源**: CODE
- **中文摘要**: 视觉-语言-动作（VLA）模型的最新进展催生了对大规模自我中心数据集的关键需求。然而，现有数据集通常受限于较短的片段时长（通常仅持续数分钟），难以捕捉复杂机器人任务执行所需的长时域依赖关系。为弥补这一空白，我们提出MobileEgo Anywhere框架——该框架利用商用移动硬件，实现鲁棒且时长超过一小时的自我中心轨迹采集。通过现代智能手机普遍搭载的传感器套件，我们实现了高保真度的长期相机位姿追踪，有效消除了传统机器人数据采集的高硬件门槛。本文贡献包括三方面：（1）发布包含200小时多样化长时自我中心数据的新数据集，并实现持续状态追踪；（2）开源移动端应用程序，使任何用户均可录制自我中心数据；（3）提供完整处理流程，将原始移动端采集数据转换为标准化、可直接用于视觉-语言-动作模型及基础模型研究的训练格式。通过推动数据采集的民主化，本研究实现了全球多样化环境中大规模长时数据的获取，加速了可泛化机器人策略的研发进程。

---

### 5. TriRelVLA: Triadic Relational Structure for Generalizable Embodied Manipulation

- **作者**: Hanyu Zhou, Chuanhao Ma, Gim Hee Lee
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.05714v1)
- **发表日期**: 2026-05-07
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2605.05714v1](http://arxiv.org/abs/2605.05714v1)
- **📥 PDF**: 已下载至本地 (`2605.05714v1_TriRelVLA_Triadic_Relational_Structure_for_Generalizable_Embodied_Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型在训练中见过的机器人任务上表现良好，但难以泛化到未见过的场景和物体。一个关键局限在于其隐式视觉表征，这种表征将物体外观、背景和场景布局纠缠在一起，导致策略对视觉变化敏感。先前研究通过构建结构化中间表征（将视觉内容对象化）来提升迁移能力，但这些表征主要捕捉场景语义而非与动作相关的关联。因此，动作预测仍依赖于外观统计特征。我们观察到操作动作取决于物体-手-任务的关系结构，该结构支配着任务需求、机器人状态和物体属性之间的交互。基于此观察，我们提出TriRelVLA——一种用于可泛化具身操作的三元关系VLA框架。该方法包含三个组成部分：1）从多模态输入中构建显式的物体-手-任务三元表征作为关系基元；2）构建任务导向的关系图，其中任务引导的交叉注意力形成节点，关系感知图变换器建模节点间交互；3）执行关系条件化的动作生成，将关系结构压缩至瓶颈空间并投影到大语言模型中进行动作预测。这种三元关系瓶颈减少了对外观统计特征的依赖，实现了跨场景、物体和任务组合的迁移。我们进一步引入真实世界机器人数据集进行微调。实验表明，该方法在微调任务上表现优异，并在跨场景、跨物体和跨任务泛化中取得显著提升。

---

### 6. NavOne: One-Step Global Planning for Vision-Language Navigation on Top-Down Maps

- **作者**: Dijia Zhan, Jinyi Li, Chenxi Zheng, Shaoyu Huang, Yong Li, Jie Tang, Xuemiao Xu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.06317v1)
- **发表日期**: 2026-05-07
- **匹配关键词**: path planning, VLN, navigation
- **arXiv**: [2605.06317v1](http://arxiv.org/abs/2605.06317v1)
- **📥 PDF**: 已下载至本地 (`2605.06317v1_NavOne_One-Step_Global_Planning_for_Vision-Language_Navigation_on_Top-Down_Maps.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 现有视觉语言导航（VLN）方法通常采用以自我为中心的逐步推理范式，这种模式难以应对误差累积问题且效率受限。尽管近期研究尝试利用预构建的环境地图，但往往依赖增量更新的记忆图或离散路径候选评分机制，这限制了连续空间推理能力并形成离散化瓶颈。我们提出自上而下VLN（TD-VLN），将导航任务重构为基于预构建俯视图的单步全局路径规划问题，并为此构建了全新的R2R-TopDown数据集。为解决该问题，我们引入统一框架NavOne，该框架通过单次端到端前向传播直接预测多模态地图上的密集路径概率。NavOne采用自上而下地图融合器实现多模态地图联合表征，并扩展注意力残差机制实现空间感知深度混合。在R2R-TopDown上的大量实验表明，NavOne在基于地图的VLN方法中达到最优性能，规划阶段速度较现有地图基线方法提升8倍，较自我中心方法提升80倍，实现了高效的全局导航。

---

## 📌 Poster

*其他相关研究*

---

### 1. AssistDLO: Assistive Teleoperation for Deformable Linear Object Manipulation

- **作者**: Berk Guler, Simon Manschitz, Kay Pompetzki, Jan Peters
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.06323v1)
- **发表日期**: 2026-05-07
- **匹配关键词**: object manipulation
- **arXiv**: [2605.06323v1](http://arxiv.org/abs/2605.06323v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 操控可变形线性物体（DLO）是机器人领域的一项挑战，因其具有无限维度的构型空间和复杂的非线性动力学特性。在遥操作中，深度不确定性会阻碍状态感知与响应。为此，本文提出AssistDLO——一种面向DLO操控的辅助遥操作框架，该框架融合了实时多视角状态估计、视觉辅助（VA）以及基于控制障碍函数的几何感知共享自主控制器（SA-CBF）。传统共享自主方法常依赖简单几何吸引子，难以保持DLO几何形态，而SA-CBF作为几何感知漏斗，既能实现精准抓取，又能保留操作员的高层级控制权。通过双手解绳结用户实验（N=22），采用不同长度和刚度的绳索对该框架进行评估。结果表明：辅助效果显著依赖于操作员专业水平与DLO特性。SA-CBF对新手用户增益最大，作为技能均衡器将任务成功率从71%提升至88%，且对刚性绳索效果显著；而专家用户更偏好视觉辅助，高柔顺性长绳索从视觉支持中获得的收益大于局部动作辅助。最终，这些发现表明有效的DLO遥操作无法依赖固定策略，凸显了对自适应、用户感知及材料感知的共享自主系统的迫切需求。

---

### 2. Structure-Preserving Gaussian Processes Via Discrete Euler-Lagrange Equations

- **作者**: Jan-Hendrik Ewering, Kathrin Flaßkamp, Niklas Wahlström, Thomas B. Schön, Thomas Seel
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.06246v1)
- **发表日期**: 2026-05-07
- **匹配关键词**: visual servoing
- **arXiv**: [2605.06246v1](http://arxiv.org/abs/2605.06246v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 本文提出拉格朗日高斯过程（LGPs），通过离散受迫欧拉-拉格朗日方程实现动力学的概率与数据高效学习。关键在于，拉格朗日-达朗贝尔原理（支配动力系统运动的几何结构）在无外力作用下通过构造得以保持。这使得模型能够学习物理一致的动力学特性，克服系统能量中的错误漂移，从而提供稳定的长期预测。本方法的核心在于基于离散受迫欧拉-拉格朗日方程与变分离散格式构建的高斯过程条件化线性算子。与现有研究不同，该方法能够仅从离散位置快照（即无需系统速度或动量数据）学习动力学特性。这对于仅能获取位置测量值的实际场景（如运动捕捉或视觉伺服应用）尤为重要。我们通过多种合成与真实案例（包括具有迟滞特性的真实软体机器人）验证了LGPs的数据效率与泛化能力。实验结果表明，LGPs仅凭稀疏位置数据即可学习具有不确定性量化的物理一致动力学特性，并实现稳定的长期预测。

---

### 3. Plug-and-Play Label Map Diffusion for Universal Goal-Oriented Navigation

- **作者**: Zhixuan Shen, Yijie Zeng, Shengxiang Luo, Tianrui Li, Haonan Luo
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.05960v1)
- **发表日期**: 2026-05-07
- **匹配关键词**: goal-oriented navigation, navigation
- **arXiv**: [2605.05960v1](http://arxiv.org/abs/2605.05960v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 在具身视觉中，目标导向导航（GON）要求机器人在未知环境中定位特定目标。GON的主要挑战在于需要构建鸟瞰图（BEV）以理解环境，同时定位未观测到的目标。现有基于地图的方法通常采用以自我为中心的语义地图，常面临依赖完整地图或语义关联不一致等挑战。为此，我们提出即插即用的标签地图扩散（PLMD），该方法基于去噪扩散概率模型（DDPM）定义了一种新颖的地图补全扩散模型。PLMD通过基于扩散的补全过程为未观测区域生成障碍物和语义标签，从而在部分观测环境中实现目标定位。此外，它利用已知与未知障碍物布局之间的结构一致性，并将障碍物先验融入语义去噪过程，从而缓解语义关联不一致的问题。通过用预测标签替代未观测区域，机器人能够准确定位指定目标。大量实验表明，PLMD（I）有效扩展了未知地图区域，（II）可无缝集成到依赖语义地图的现有导航策略中，（III）在三个GON任务上达到了最先进性能。

---

### 4. DexSynRefine: Synthesizing and Refining Human-Object Interaction Motion for Physically Feasible Dexterous Robot Actions

- **作者**: Hyesung Lee, Hyunwoo Jung, Si-Hwan Heo, Sungwook Yang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.05925v1)
- **发表日期**: 2026-05-07
- **匹配关键词**: tool use
- **arXiv**: [2605.05925v1](http://arxiv.org/abs/2605.05925v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 从人-物交互数据学习灵巧操作是遥操作的一种可扩展替代方案，但人-物交互演示数据稀疏且仅提供运动学层面的动作，在实体不匹配和接触丰富的动力学环境下无法直接执行。我们提出DexSynRefine框架，包含三个耦合组件：HOI-MMFP——基于运动流形基元的任务与物体初始状态条件扩展，可从稀疏的人-物交互演示中合成协调的手-物轨迹；任务空间残差强化学习策略——在继承合成参考运动学结构的同时实现物理层面的落地；接触与动力学自适应模块——通过本体感知历史实现仿真到现实的迁移。在涵盖抓取放置、工具使用和物体重定向的五项灵巧操作任务中，我们的任务空间残差策略在仿真环境中优于先前动作表征基线方法，并在全部五项任务中成功迁移至真实机器人，相较于运动学重定向方法提升50-70个百分点。

---

### 5. MaMi-HOI: Harmonizing Global Kinematics and Local Geometry for Human-Object Interaction Generation

- **作者**: Hao Wang, Shiqi Wang, Qi Liu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.05756v1)
- **发表日期**: 2026-05-07
- **匹配关键词**: navigation
- **arXiv**: [2605.05756v1](http://arxiv.org/abs/2605.05756v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: GITHUB
  - 链接：https://github.com/DON738110198/MaMi-HOI.git
- **中文摘要**: 生成逼真的三维人-物交互（HOI）是从具身智能到虚拟内容创作等应用的基础任务，这需要协调高层语义意图与严格的低层物理约束。现有方法在语义对齐方面表现出色，但在维持精确的物体接触方面存在困难。我们揭示了一个关键发现，称为“几何遗忘”：随着扩散模型深度的增加，语义特征倾向于掩盖物体几何特征，导致模型丧失对物体几何的感知能力。为解决这一问题，我们提出MaMi-HOI，一个协调宏观运动流畅性与微观空间精度的层次化框架。首先，为对抗几何遗忘，我们引入几何感知邻近适配器（GAPA），该适配器显式地重新注入密集的物体细节，执行残差修正以实现精确接触。然而，这种激进的局部强化可能破坏全局动态，导致动作僵硬。为此，我们提出运动和谐适配器（KHA），该适配器主动将全身姿态与空间目标对齐，确保骨架在保持自然性的同时主动适应约束。大量实验验证了MaMi-HOI能够同时实现自然运动与精确接触。关键在于，它还将生成能力扩展到具有复杂轨迹的长期任务，有效弥合了三维场景中全局导航与高保真操作之间的鸿沟。代码已开源：https://github.com/DON738110198/MaMi-HOI.git

---

### 6. Relit-LiVE: Relight Video by Jointly Learning Environment Video

- **作者**: Weiqing Xiao, Hong Li, Xiuyu Yang, Houyuan Chen, Wenyi Li, Tianqi Liu, Shaocong Xu, Chongjie Ye, Hao Zhao, Beibei Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.06658v1)
- **发表日期**: 2026-05-07
- **匹配关键词**: neural rendering
- **arXiv**: [2605.06658v1](http://arxiv.org/abs/2605.06658v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: GITHUB
  - 链接：https://github.com/zhuxing0/Relit-LiVE.
- **中文摘要**: 近期研究表明，大规模视频扩散模型可通过将视频分解为内在场景表征，再在新光照条件下进行前向渲染，从而被重新用作神经渲染器。尽管这一范式前景广阔，但其根本依赖于精确的内在分解——这对真实世界视频而言仍高度不可靠，往往导致重光照过程中出现外观失真、材质破损及时间伪影累积等问题。本文提出Relit-LiVE——一种无需相机位姿先验知识即可生成物理一致、时间稳定结果的视频重光照框架。我们的核心洞察在于：将原始参考图像显式引入渲染流程，使模型能够恢复内在表征中不可避免丢失或损坏的关键场景线索。此外，我们提出新型环境视频预测范式，在单一扩散过程中同步生成重光照视频及与各相机视角对齐的逐帧环境贴图。这种联合预测机制强化了几何-光照对齐，自然支持动态光照与相机运动，在显著提升视频重光照物理一致性的同时，降低了对已知逐帧相机位姿的要求。大量实验表明，Relit-LiVE在合成与真实世界基准测试中均持续优于当前最先进的视频重光照及神经渲染方法。除重光照外，本框架天然支持场景级渲染、材质编辑、物体插入及流式视频重光照等广泛下游应用。项目地址：https://github.com/zhuxing0/Relit-LiVE。

---

### 7. Cross-Modal Navigation with Multi-Agent Reinforcement Learning

- **作者**: Shuo Liu, Xinzichen Li, Christopher Amato
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.06595v1)
- **发表日期**: 2026-05-07
- **匹配关键词**: navigation
- **arXiv**: [2605.06595v1](http://arxiv.org/abs/2605.06595v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 鲁棒具身导航依赖于互补的感官线索。然而，高质量且良好对齐的多模态数据在实践中往往难以获取。训练单一模型同样具有挑战性，因为丰富的多模态输入会引发复杂的表征并显著扩大策略空间。轻量级模态专用智能体之间的跨模态协作为可扩展范式提供了可能。这种协作方式既能实现灵活部署与并行执行，又能保留各模态的优势。本文提出\textbf{CRONA}——一个面向\textbf{跨模态导航}的多智能体强化学习（MARL）框架。CRONA通过利用控制相关的辅助信念和具备全局状态的中心化多模态评论家来提升协作效果。在视觉-声学导航任务上的实验表明，多智能体方法在性能和效率上均显著优于单智能体基线。研究发现：在显著线索下，有限模态的同质协作足以完成短程导航；具备互补模态的异质智能体协作通常高效且有效；而在大型复杂环境中导航则需要更丰富的多模态感知与更强的模型容量。

---

### 8. 3D MRI Image Pretraining via Controllable 2D Slice Navigation Task

- **作者**: Yu Wang, Qingchao Chen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.06487v1)
- **发表日期**: 2026-05-07
- **匹配关键词**: navigation
- **arXiv**: [2605.06487v1](http://arxiv.org/abs/2605.06487v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 自监督预训练已成为从无标注扫描中学习MRI表征的主流方法。然而，现有的大多数训练目标仍将每个扫描主要视为切片、块或体积的静态聚合。我们提出疑问：是否存在一种内在形式的自监督信号，不同于通过将3D体积转换为可控的2D渲染序列来重建掩码块——通过以连续位置、方向和尺度渲染切片，3D体积可转换为密集的视频动作序列，其控制参数即为动作轨迹。我们通过一种动作条件预训练目标来研究这一构想，其中分词器编码切片观测值，潜在动力学模型预测潜在特征的演化过程。在具有代表性的解剖和空间下游任务中，所提出的预训练方法与标准静态体积基线、仅使用分词器的预训练以及无对齐动作的动力学变体进行了对比评估。结果表明，可控的MRI切片导航为从大规模无标注MRI数据集中学习解剖和空间表征提供了有用的互补预训练接口。

---

