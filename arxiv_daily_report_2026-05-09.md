# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-05-09 08:03

**今日新增**: 18 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 4/18 篇提供

**🌟 Highlight**: 6 篇 | **📌 Poster**: 12 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation

- **作者**: Yushan Liu, Peibo Sun, Shoujie Li, Yifan Xie, Lingfeng Zhang, Xintao Chao, Shiyuan Dong, Fang Chen, Xiao-Ping Zhang, Wenbo Ding
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.06481v1)
- **发表日期**: 2026-05-07
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2605.06481v1](http://arxiv.org/abs/2605.06481v1)
- **📥 PDF**: 已下载至本地 (`2605.06481v1_OA-WAM_Object-Addressable_World_Action_Model_for_Robust_Robot_Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 世界动作模型（WAMs）通过联合预测场景演变与机器人动作来增强视觉-语言-动作策略，但现有方法通常将预测的世界表示为整体图像、视频令牌或全局隐变量。当指令指向特定物体时，尤其是在物体身份与上下文纠缠的场景偏移下，这些表示难以被动作解码器处理。我们提出OA-WAM——一种面向物体的可寻址世界动作模型，用于实现鲁棒的机器人操作。OA-WAM将每帧分解为N+1个槽状态，包含一个机器人槽和N个物体槽。每个槽包含一个持久化地址向量和一个时变内容向量，并与文本、图像、本体感知及历史动作令牌通过块因果序列融合。世界头预测下一帧槽状态，而流匹配动作头在同一前向传播中解码16步连续动作块。可寻址性通过将跨槽注意力路由至仅含地址的键，并在每个Transformer层重置地址切片来实现，从而在不增加额外令牌的情况下，将"作用于哪个物体"与"该物体当前是什么"分离。OA-WAM在LIBERO（97.8%）和SimplerEnv（79.3%）上匹配强VLA和WAM基线，在最具相关性的LIBERO-Plus几何轴上达到最优性能，并在七轴聚合指标上保持竞争力。因果槽干预测试产生0.87的交换绑定余弦值，而整体基线最多仅为0.09。这些结果表明，可寻址物体状态为场景扰动下的鲁棒世界-动作建模提供了有效接口。

---

### 2. Toward Visually Realistic Simulation: A Benchmark for Evaluating Robot Manipulation in Simulation

- **作者**: Yixin Zhu, Zixiong Wang, Jian Yang, Jin Xie, Jingyi Yu, Jiayuan Gu, Beibei Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.06311v1)
- **发表日期**: 2026-05-07
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2605.06311v1](http://arxiv.org/abs/2605.06311v1)
- **📥 PDF**: 已下载至本地 (`2605.06311v1_Toward_Visually_Realistic_Simulation_A_Benchmark_for_Evaluating_Robot_Manipulation_in_Simulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 对机器人操作策略的可靠仿真评估可作为真实世界性能的高保真代理。现有基准虽涵盖广泛任务类别，但缺乏视觉真实性，导致仿真与现实之间存在巨大领域差距，削弱了基于仿真的评估对真实世界性能预测的可靠性。为缩小仿真到现实的视觉差距，我们通过系统分析分离光照与材质的影响。结果表明，这些因素在几何推理与空间定位中起关键作用，却在现有基准中普遍被忽视。基于此分析，我们提出VISER——一个用于仿真中评估机器人操作的视觉真实基准。VISER包含基于物理渲染（PBR）材质的1000余个3D资产的高保真数据集，以及通过精心布局或生成方式构建的3D场景。为此，我们提出自动化流水线，利用多模态大语言模型（MLLMs）实现材质感知的部件分割与材质检索，支持物理合理资产的可扩展生成。基于高保真3D资产数据集，我们构建了抓取、放置及长周期任务等多样化评估任务，实现视觉-语言-动作（VLA）模型的可扩展、可复现评估。该基准在仿真与真实世界性能间展现出强相关性，不同策略的平均皮尔逊相关系数达0.92。

---

### 3. VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts

- **作者**: Yuhua Jiang, Junjie Lu, Xinyao Qin, Xiaoyu Chen, Kaixin Wang, Feifei Gao, Li Zhao
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.06175v1)
- **发表日期**: 2026-05-07
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2605.06175v1](http://arxiv.org/abs/2605.06175v1)
- **📥 PDF**: 已下载至本地 (`2605.06175v1_VLA-GSE_Boosting_Parameter-Efficient_Fine-Tuning_in_VLA_with_Generalized_and_Specialized_Experts.pdf`)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/YuhuaJiang2002/VLA-GSE
- **中文摘要**: 视觉-语言-动作（VLA）模型继承了预训练视觉-语言骨干网络丰富的视觉语义先验知识，但将其适配到机器人控制任务仍具挑战性。全参数微调（FFT）容易在机器人下游数据上过拟合，并灾难性遗忘预训练的视觉-语言能力。参数高效微调（PEFT）能更好地保留预训练知识，然而现有PEFT方法仍难以有效适配机器人控制任务。为弥补这一不足，我们提出VLA-GSE——一种参数高效的VLA微调框架，在保留PEFT知识保留优势的同时提升控制适配能力。具体而言，VLA-GSE（通用与专用专家）通过谱分解冻结的骨干网络进行初始化，将主导奇异分量分配给通用专家（共享专家），将不相交的残差分量分配给专用专家（路由专家）。这种分解方式在固定可训练参数预算下提升了适配能力。在可比参数预算下，VLA-GSE仅更新全模型参数的2.51%，却持续优于强FFT和PEFT基线方法。该方法在LIBERO-Plus上实现81.2%的平均零样本成功率，在多模态理解基准测试中与LoRA相当地保留了预训练VLM能力，并在多种分布偏移场景下提升了真实世界操作任务的成功率。代码开源地址：https://github.com/YuhuaJiang2002/VLA-GSE

---

### 4. MobileEgo Anywhere: Open Infrastructure for long horizon egocentric data on commodity hardware

- **作者**: Senthil Palanisamy, Abhishek Anand, Satpal Singh Rathor, Pratyush Patnaik, Shubhanshu Khatana
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.05945v1)
- **发表日期**: 2026-05-07
- **匹配关键词**: VLA, vision language action model, vision language action
- **arXiv**: [2605.05945v1](http://arxiv.org/abs/2605.05945v1)
- **📥 PDF**: 已下载至本地 (`2605.05945v1_MobileEgo_Anywhere_Open_Infrastructure_for_long_horizon_egocentric_data_on_commodity_hardware.pdf`)
- **🔓 开源**: CODE
- **中文摘要**: 视觉-语言-动作（VLA）模型的最新进展催生了对大规模自我中心数据集的迫切需求。然而，现有数据集通常受限于短片段时长（通常仅持续数分钟），难以捕捉复杂机器人任务执行所需的长期时间依赖关系。为弥补这一空白，我们提出MobileEgo Anywhere框架，该框架利用商用移动硬件实现鲁棒性超过一小时的自我中心轨迹采集。通过整合现代智能手机的通用传感器套件，我们实现了高保真度的长期相机位姿追踪，有效消除了传统机器人数据采集的高硬件门槛。本文贡献包含三方面：（1）发布包含200小时多样化长片段自我中心数据的新数据集，并实现持续状态追踪；（2）开源支持用户录制自我中心数据的移动应用程序；（3）提供完整处理流水线，将原始移动端采集数据转换为标准化训练格式，服务于VLA模型与基础模型研究。通过推动数据采集流程的民主化，本研究实现了全球多样化环境中大规模长时程数据的获取，加速了可泛化机器人策略的开发进程。

---

### 5. TriRelVLA: Triadic Relational Structure for Generalizable Embodied Manipulation

- **作者**: Hanyu Zhou, Chuanhao Ma, Gim Hee Lee
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.05714v1)
- **发表日期**: 2026-05-07
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2605.05714v1](http://arxiv.org/abs/2605.05714v1)
- **📥 PDF**: 已下载至本地 (`2605.05714v1_TriRelVLA_Triadic_Relational_Structure_for_Generalizable_Embodied_Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型在训练中见过的机器人任务上表现良好，但难以泛化到未见过的场景和物体。其关键局限在于隐式视觉表征，这类表征将物体外观、背景和场景布局纠缠在一起，导致策略对视觉变化敏感。先前研究通过构建结构化中间表征（将视觉内容对象化）提升了迁移能力，但这些表征主要捕捉场景语义而非动作相关关系，导致动作预测仍受外观统计特征制约。我们观察到操作动作依赖于物体-手-任务关系结构，该结构支配着任务需求、机器人状态和物体属性之间的交互。基于此观察，我们提出TriRelVLA——一种面向可泛化具身操作的三元关系VLA框架。该方法包含三个组件：1）从多模态输入中构建显式的物体-手-任务三元表征作为关系基元；2）构建任务导向的关系图：任务引导的交叉注意力形成节点，关系感知图变换器建模节点间交互；3）执行关系条件化动作生成：将关系结构压缩至瓶颈空间并投影到大语言模型中进行动作预测。这种三元关系瓶颈减少了对外观统计特征的依赖，实现了跨场景、物体和任务组合的迁移。我们进一步引入真实世界机器人数据集进行微调。实验表明，该方法在微调任务上表现优异，并在跨场景、跨物体和跨任务泛化方面取得显著提升。

---

### 6. ConsisVLA-4D: Advancing Spatiotemporal Consistency in Efficient 3D-Perception and 4D-Reasoning for Robotic Manipulation

- **作者**: Wei Li, Jizhihui Liu, Li Yixing, Junwen Tong, Rui Shao, Liqiang Nie
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.05126v1)
- **发表日期**: 2026-05-06
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2605.05126v1](http://arxiv.org/abs/2605.05126v1)
- **📥 PDF**: 已下载至本地 (`2605.05126v1_ConsisVLA-4D_Advancing_Spatiotemporal_Consistency_in_Efficient_3D-Perception_and_4D-Reasoning_for_Ro.pdf`)
- **🔓 开源**: CODE
- **中文摘要**: 当前的视觉-语言-动作（VLA）模型主要聚焦于将二维观测映射为动作，但在时空感知与推理方面存在显著局限：1）空间表征通常依赖额外传感器，引入大量计算开销；2）视觉推理通常局限于未来帧预测，缺乏与指令场景的对齐，从而损害时空一致性。为解决上述挑战，我们提出ConsisVLA-4D——一个统一高效的框架，用于增强三维感知与四维推理中的时空一致性。具体而言，我们设计了：1）CV-Aligner，通过过滤指令相关区域并对齐多视角下的物体身份，确保跨视角物体语义一致性；2）CO-Fuser，通过紧凑潜在表征消除跨视角物体间的空间关系歧义，保证跨物体空间几何一致性。在此基础上，我们引入3）CS-Thinker，在动作展开过程中实现跨场景时空一致性。该模块从CV-Aligner的物体语义令牌中学习局部动态的隐式知识，并从CO-Fuser的几何令牌中学习全局深度信息，从而在场景变化下增强高效视觉推理。大量实验表明，得益于高效的时空一致性设计，ConsisVLA-4D在LIBERO基准测试和真实平台上的性能分别提升21.6%和41.5%，推理速度相比OpenVLA分别提升2.3倍和2.4倍。ConsisVLA-4D已开源并公开于。

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
- **中文摘要**: 在机器人操作中，操控可变形线性物体（DLO）极具挑战性，因其具有无限维度的构型空间和复杂的非线性动力学特性。在遥操作中，深度不确定性会阻碍状态感知与反应。为此，本文提出AssistDLO框架——一种面向DLO操作的辅助遥操作框架，该框架融合了实时多视角状态估计、视觉辅助（VA）以及基于控制障碍函数的几何感知共享自主控制器（SA-CBF）。传统共享自主方法通常依赖简单的几何吸引子，可能破坏DLO的几何形态，而SA-CBF作为几何感知漏斗，既能实现精准抓取，又能保留操作员的高层级控制权。通过一项双臂解绳结用户研究（N=22），采用不同长度和刚度的绳索对该框架进行评估。结果表明：辅助效果高度依赖于操作员专业水平与DLO属性。SA-CBF为新手用户带来最显著的增益，作为技能均衡器将任务成功率从71%提升至88%，且对较硬绳索效果更佳。相反，专家用户更偏好视觉辅助，而高柔顺性长绳索从视觉支持中获益多于局部动作辅助。最终，这些发现表明有效的DLO遥操作无法依赖固定策略，凸显了对自适应、用户感知及材料感知的共享自主系统的迫切需求。

---

### 2. Structure-Preserving Gaussian Processes Via Discrete Euler-Lagrange Equations

- **作者**: Jan-Hendrik Ewering, Kathrin Flaßkamp, Niklas Wahlström, Thomas B. Schön, Thomas Seel
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.06246v1)
- **发表日期**: 2026-05-07
- **匹配关键词**: visual servoing
- **arXiv**: [2605.06246v1](http://arxiv.org/abs/2605.06246v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 本文提出拉格朗日高斯过程（LGPs），通过离散受迫欧拉-拉格朗日方程实现动力学系统的概率建模与数据高效学习。关键在于，拉格朗日-达朗贝尔原理（支配动力系统运动的几何结构）在无外力作用下通过构造得以保持。这使得模型能够学习物理一致的动力学特性，克服系统能量中的错误漂移，从而提供稳定的长期预测。本方法的核心是基于离散受迫欧拉-拉格朗日方程与变分离散格式构建的高斯过程条件化线性算子。与现有研究不同，该方法仅通过离散位置快照（即无需获取系统速度或动量）即可学习动力学特性。这对于大量仅能获取位置测量的实际场景（如运动捕捉或视觉伺服应用）具有特殊意义。我们通过多种合成与真实案例（包括具有迟滞特性的真实软体机器人）验证了LGPs的数据效率与泛化能力。实验结果表明，LGPs仅凭稀疏位置数据即可学习具有不确定性量化的物理一致动力学特性，并实现稳定的长期预测。

---

### 3. Plug-and-Play Label Map Diffusion for Universal Goal-Oriented Navigation

- **作者**: Zhixuan Shen, Yijie Zeng, Shengxiang Luo, Tianrui Li, Haonan Luo
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.05960v1)
- **发表日期**: 2026-05-07
- **匹配关键词**: navigation, goal-oriented navigation
- **arXiv**: [2605.05960v1](http://arxiv.org/abs/2605.05960v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 在具身视觉中，目标导向导航（GON）要求机器人在未探索环境中定位特定目标。GON的主要挑战在于需要构建鸟瞰图（BEV）来理解环境，同时定位未观测到的目标。现有基于地图的方法通常采用以自我为中心的语义地图，常面临依赖完整地图或语义关联不一致等挑战。为此，我们提出即插即用的标签地图扩散（PLMD），该方法基于去噪扩散概率模型（DDPM）定义了一种新颖的地图补全扩散模型。PLMD通过基于扩散的补全过程为未观测区域生成障碍物和语义标签，从而在部分观测环境中实现目标定位。此外，它通过利用已知与未知障碍物布局之间的结构一致性，并将障碍物先验融入语义去噪过程，缓解了语义关联不一致的问题。通过用预测标签替代未观测区域，机器人能够准确定位指定目标。大量实验表明，PLMD能够：（I）有效扩展未知地图区域，（II）无缝集成到依赖语义地图的现有导航策略中，（III）在三个GON任务上达到最先进性能。

---

### 4. DexSynRefine: Synthesizing and Refining Human-Object Interaction Motion for Physically Feasible Dexterous Robot Actions

- **作者**: Hyesung Lee, Hyunwoo Jung, Si-Hwan Heo, Sungwook Yang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.05925v1)
- **发表日期**: 2026-05-07
- **匹配关键词**: tool use
- **arXiv**: [2605.05925v1](http://arxiv.org/abs/2605.05925v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 从人-物交互数据学习灵巧操作是遥操作的一种可扩展替代方案，但人-物交互演示数据稀疏且仅提供运动学信息，在形态不匹配和接触丰富的动力学条件下无法直接执行。我们提出DexSynRefine框架，包含三个耦合组件：HOI-MMFP——一种基于任务和物体初始状态条件扩展的运动流形基元，可从稀疏的人-物交互演示中合成协调的手-物轨迹；任务空间残差强化学习策略——在物理层面实现合成参考轨迹的同时继承其运动学结构；接触与动力学自适应模块——通过本体感知历史实现从仿真到真实环境的迁移。在涵盖抓取放置、工具使用和物体重定向的五项灵巧操作任务中，我们的任务空间残差策略在仿真中优于先前的动作表征基线方法，并在真实机器人上成功迁移全部五项任务，相较于运动学重定向方法提升了50-70个百分点。

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
- **中文摘要**: 生成逼真的三维人-物交互（HOI）是从具身智能到虚拟内容创作等应用的基础任务，这需要协调高层语义意图与严格的低层物理约束。现有方法在语义对齐方面表现出色，但在保持精确物体接触方面存在困难。我们发现一个关键现象——**几何遗忘**：随着扩散模型深度增加，语义特征倾向于掩盖物体几何特征，导致模型丧失对物体几何的感知能力。为解决此问题，我们提出MaMi-HOI——一个协调**宏观**运动流畅性与**微观**空间精度的分层框架。首先，为对抗几何遗忘，我们引入几何感知邻近适配器（GAPA），通过显式重新注入密集物体细节进行残差修正，实现精确接触。然而，这种激进的局部强制可能破坏全局动力学，导致动作僵硬。为此，我们提出运动和谐适配器（KHA），主动将全身姿态与空间目标对齐，确保骨架在保持自然性的同时主动适应约束。大量实验验证MaMi-HOI能同时实现自然运动与精确接触。关键的是，该方法将生成能力扩展到具有复杂轨迹的长期任务，有效弥合了三维场景中全局导航与高保真操作之间的鸿沟。代码已开源：https://github.com/DON738110198/MaMi-HOI.git

---

### 6. Contact-Free Grasp Stability Prediction with In-Hand Time-of-Flight Sensors

- **作者**: Kyle DuFrene, Cindy Grimm
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.05461v1)
- **发表日期**: 2026-05-06
- **匹配关键词**: grasp planning
- **arXiv**: [2605.05461v1](http://arxiv.org/abs/2605.05461v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 当前机器人抓取规划方法虽展现出较高成功率，但易受噪声传感器等因素影响而性能下降。已有研究提出基于触觉的抓取稳定性分类器来检测失败，但这些方法需要接触并抓取物体才能实现。我们提出一种无接触式抓取稳定性预测方法，通过在夹爪远端关节安装多区域飞行时间传感器实现。由于无需抓取物体即可进行预测，该方法显著提升了稳定性分类速度，循环频率达15赫兹。我们收集了15种物体的2500余次真实抓取数据用于训练分类器，并对6种未见物体进行抓取尝试（其中3种用于验证与模型选择，3种用于模型测试）。该方法展现出优异的分类性能：验证集准确率达85.5%，测试集准确率达86.0%。

---

### 7. Creative Robot Tool Use by Counterfactual Reasoning

- **作者**: M. Tuluhan Akbulut, Varun Satheesh, Ahmed Jaafar, Alper Ahmetoglu, Shane Parr, Aditya Ganeshan, Shivam Vats, George Konidaris
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.05411v1)
- **发表日期**: 2026-05-06
- **匹配关键词**: tool use
- **arXiv**: [2605.05411v1](http://arxiv.org/abs/2605.05411v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出了一种面向创造性机器人工具使用的因果推理框架，该框架能够准确识别适用于任务的工具，使其超越原有设计目标发挥作用。该框架首先通过在动力学模型中进行模拟实验，发现工具与任务之间的因果关系。我们将因果发现问题解耦为两个互补模块：基于视觉语言模型的特征建议，以及通过目标几何与物理特征扰动生成的反事实工具。随后，根据识别出的因果特征对新型物体进行分类，并通过基于这些因果特征的关键点匹配实现工具使用技能的迁移。通过在动力学模型中重构任务，我们的方法将工具使用建立在物理问题基础上。我们通过以下场景验证该方法：使用不同棍棒够取远处物体、用多样物品从碗中舀取糖果、以及利用不同箱子或板条箱作为垫脚平台从高架取物。基线对比表明，识别因果特征并将其锚定于物理工具属性，能够实现更可靠的工具选择与更强的技能关键点迁移。

---

### 8. A Closed-Form Dual-Barrier CBF Safety Filter for Holonomic Robots on Incrementally Built Occupancy Grid Maps

- **作者**: Himanshu Paudel, Basanta Joshi, Dhirendra Raj Madai, Alina Bartaula, Biman Rimal, Sanjay Neupane
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.05182v1)
- **发表日期**: 2026-05-06
- **匹配关键词**: exploration
- **arXiv**: [2605.05182v1](http://arxiv.org/abs/2605.05182v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出了一种基于双重障碍控制屏障函数（CBF）的安全滤波器，用于在增量构建的占据栅格地图中实现全向机器人的实时安全关键速度控制。当机器人在未知环境中探索时，未测绘区域会引入不可约的不确定性——由于探索边界之外的障碍物几何形状未知，进入此类区域会带来碰撞风险，尤其对于前向传感器而言。为此，我们施加两类约束：避开已测绘障碍物，以及限制进入未探索区域。这两类约束均通过占据栅格的符号距离场解析推导，最终形成闭式安全滤波器，每个控制周期仅需求解一个小型线性系统。在树莓派等资源受限平台上（SLAM与规划已消耗大量算力），本滤波器以极低开销保留计算资源。自适应增益调度策略可在信息丰富区域放松边界约束，在充分测绘区域收紧约束，从而在保障安全的同时提升探索效率。该滤波器在速度空间中作为最小侵入性修正运行，可与任意标称控制器（包括基于学习的方法）组合使用。基于PX4控制四旋翼的硬件飞行实验表明，在多次室内飞行中实现了零碰撞。

---

### 9. Reduced-order Neural Modeling with Differentiable Simulation for High-Detail Tactile Perception

- **作者**: Yuhu Guo, Zhikai Shen, Jiasheng Qu, Chenghao Qian, Yuming Huang, Bin Chen, Guoxing Fang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.05053v1)
- **发表日期**: 2026-05-06
- **匹配关键词**: tactile perception
- **arXiv**: [2605.05053v1](http://arxiv.org/abs/2605.05053v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 触觉感知是灵巧操作的关键，然而模拟高分辨率弹性体变形在计算上仍面临巨大挑战。有限元方法虽能实现高保真度，但需要昂贵的网格重构；而物质点法则受限于粒子与内存之间的权衡。我们提出了一种**降阶神经仿真框架**，将粗粒度MPM动力学与隐式神经解码器相结合，通过紧凑的潜在状态重建亚粒子级别的触觉细节。该框架从高分辨率与低分辨率配对的仿真数据中学习连续变形流形，实现物理一致且可微的推理。与TacIPC相比，我们的方法仿真速度提升超过65%，**内存占用降低40%**，同时保持更优的几何保真度。在触觉渲染与三维表面重建任务中，该方法进一步将精度提升25%，并以更快的推理速度生成逼真的深度图像与表面网格。这些结果表明，所提出的降阶神经模型能够实现高细节、物理可信的触觉仿真，为机器人交互与优化带来显著的效率提升。

---

### 10. Gaze4HRI: Zero-shot Benchmarking Gaze Estimation Neural-Networks for Human-Robot Interaction

- **作者**: Berk Sezer, Ali Görkem Küçük, Erol Şahin, Sinan Kalkan
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.04770v1)
- **发表日期**: 2026-05-06
- **匹配关键词**: human-robot interaction, HRI
- **arXiv**: [2605.04770v1](http://arxiv.org/abs/2605.04770v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 零样本基于外观的三维视线估计通过直接将RGB图像映射到视线向量，在成本效率方面具有显著优势，但其在人机交互场景中的可靠性仍不确定。现有基准测试常忽视人机交互的基本条件，例如视频中动态变化的摄像机视角和移动目标。此外，当前的跨数据集评估普遍存在复杂度差异问题——在多样化数据集上训练的方法往往被用于测试规模显著更小、多样性更低的集合，无法评估真正的鲁棒性。为弥补这些不足，我们提出Gaze4HRI——一个大规模数据集（50+名受试者、3000+段视频、600000+帧），专门针对关键人机交互变量（光照条件、头眼冲突、摄像机与视线目标在视频中的运动）评估当前最优方法的性能。我们的基准测试表明，所有被评估方法至少在一个条件下失效，其中陡峭向下注视被确认为普遍存在的失效点。值得注意的是，基于ETH-X-Gaze数据集训练的PureGaze方法在其余所有条件下均保持独特鲁棒性。这些结果对近期文献中聚焦复杂时空建模与Transformer架构的研究方向提出了挑战。相反，我们的发现表明：以ETH-X-Gaze数据集为代表的大规模数据多样性，是零样本方法在无约束环境中鲁棒性的首要驱动因素；而PureGaze提出的自对抗损失函数进行视线特征净化等增强鲁棒性的框架，则能带来显著的进一步改进。最终，本研究建立了严格的基准测试，为实践者提供实用指南，并重塑未来研究方向。数据集与代码已开源：https://gazeforhri.github.io。

---

### 11. Active Contact Sensing for Robust Robot-to-Human Object Handover

- **作者**: Linfeng Li, Lin Shao, David Hsu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.04610v1)
- **发表日期**: 2026-05-06
- **匹配关键词**: grasp detection
- **arXiv**: [2605.04610v1](http://arxiv.org/abs/2605.04610v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 机器人与人类之间的物体交接是机器人助手的一项基本技能，从在家中递送饮料到在手术室传递手术器械都离不开它。我们期望机器人能够稳健地完成交接——仅在人类牢固抓握后才释放物体，同时忽略偶然的触碰。现有的被动感知方法难以泛化到不同物体和人类行为，因为它们缺乏能够区分不同接触条件（如牢固抓握与偶然触碰）的信息性扰动。我们提出了一种用于稳健交接的主动感知方法：机器人通过施加信息收集动作，并感知由此产生的人类施加力来推断接触状态。牢固抓握会产生多方向的力，而偶然触碰则不会。为了捕捉这一区别，我们使用贝叶斯线性模型对接触状态进行建模：该模型描述了从机器人动作到人类施加力的分段线性映射的分布。该模型能够实现牢固抓握检测和主动信息收集。在包含12名参与者和30种不同刚性物体的实验中，我们的方法实现了97.5%的成功率——比两种常见基线方法高出30%以上。

---

### 12. Autonomous Laparoscope Control through Unified Mechanics-Based Representation of Multimodal Intraoperative Information

- **作者**: Xiaojian Li, Jin Fang, Yudong Shi, Xilin Xiao, Kai Yan, Kang Min, Ling Li, Hua Tang, Hangjie Mo
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2605.04408v1)
- **发表日期**: 2026-05-06
- **匹配关键词**: visual tracking
- **arXiv**: [2605.04408v1](http://arxiv.org/abs/2605.04408v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 持镜机器人能够为外科医生提供稳定的腹腔镜视野，并减轻人类助手的负担。为维持术中理想视野，机器人需根据术中信息持续调整腹腔镜位姿。然而，术中多模态信号（如位置、力/力矩及图像）在物理意义和量纲上存在显著差异，难以构建统一表征并生成可直接用于腹腔镜控制的指令。针对该问题，本文提出一种基于多模态信息统一力学建模的持镜机器人控制方法。首先，我们设计了包含位置、力/力矩及图像等多术中信号源的映射策略，将其统一为操作空间中的等效力旋量表征；其次，采用任务优先级方案，将力旋量分别注入任务空间与零空间，并通过任务优先级投影合成腹腔镜控制指令，从而在单一框架内实现多模态信息的一致表征与协调融合；最后，以术中远程运动中心位置、力/力矩传感器读数及腹腔镜图像为例，构建了用于强制RCM几何约束并降低穿刺点接触力的RCM约束力旋量、实现柔顺拖拽的腹腔镜操控力旋量，以及实现器械自主视觉追踪的器械追踪力旋量。手术体模实验与活体猪实验表明，该方法在维持RCM约束并降低穿刺点持续载荷的同时，支持包括腹腔镜柔顺操控与器械自主追踪在内的多任务操作。

---

