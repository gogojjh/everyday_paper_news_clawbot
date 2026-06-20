# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-06-20 08:02

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 1/20 篇提供

**🌟 Highlight**: 20 篇 | **📌 Poster**: 0 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. MemoryWAM: Efficient World Action Modeling with Persistent Memory

- **作者**: Sizhe Yang, Juncheng Mu, Tianming Wei, Chenhao Lu, Xiaofan Li, Linning Xu, Zhengrong Xue, Zhecheng Yuan, Dahua Lin, Jiangmiao Pang, Huazhe Xu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.20562v1)
- **发表日期**: 2026-06-18
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2606.20562v1](http://arxiv.org/abs/2606.20562v1)
- **📥 PDF**: 已下载至本地 (`2606.20562v1_MemoryWAM_Efficient_World_Action_Modeling_with_Persistent_Memory.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 在现实世界中实现鲁棒的机器人操作，不仅需要理解当前观测，还需要具备记忆与动态建模能力。世界动作模型（WAMs）通过联合建模视觉预测与基于当前及历史观测的动作决策，具备了这些能力，因此成为机器人操作领域极具前景的范式。然而，现有WAMs面临一个根本性权衡：高效推理的方法通常仅依赖近期观测的有限窗口，因此在非马尔可夫环境中表现不佳；而保留长历史信息的方法则会产生随序列长度显著增长的时间与空间成本。为解决这一挑战，我们提出MemoryWAM——一种具备高效持久记忆的世界动作模型。MemoryWAM采用混合记忆设计，融合了近期帧、事件边界锚点帧以及总结长程历史的紧凑要旨标记。通过定制化的注意力机制，该模型既能检索详细的短期上下文，也能获取压缩的长期上下文，从而在降低推理延迟和GPU内存占用的同时支持依赖记忆的决策。在仿真与真实世界的长时域、依赖记忆的操作任务中，MemoryWAM在保持优异计算效率的同时，超越了强大的视觉-语言-动作（VLA）模型及WAM基线方法。

---

### 2. Slow Brain, Fast Planner: Latency-Resilient VLM-Augmented Urban Navigation

- **作者**: Zhenghao "Mark'' Peng, Honglin He, Quanyi Li, Yukai Ma, Bolei Zhou
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.20458v1)
- **发表日期**: 2026-06-18
- **匹配关键词**: vision-language-action, navigation, vision-language-action model
- **arXiv**: [2606.20458v1](http://arxiv.org/abs/2606.20458v1)
- **📥 PDF**: 已下载至本地 (`2606.20458v1_Slow_Brain,_Fast_Planner_Latency-Resilient_VLM-Augmented_Urban_Navigation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 基于学习的行人道导航规划器能够实时生成多样化的候选轨迹，但其评分函数在复杂场景下往往无法选出最优轨迹，导致移动机器人驶入草坪、冲向行人或偏离正确方向——即便同一候选集中存在更优选择。我们将此现象称为"轨迹评分鸿沟"：在真实行人道导航中，基于锚点的规划器首选轨迹与最优候选轨迹之间存在显著差距，这很可能源于规划器高层场景理解能力的局限。我们并未采用端到端的视觉-语言-动作模型替代规划器，而是提出VLM-规划器接口：利用视觉语言模型从规划器生成的候选集中选择轨迹索引，再将其与规划器的初始输出进行融合。然而，视觉语言模型每次查询需耗时1-3秒，无法直接驱动5-20Hz的控制循环。为此，我们提出一种免训练、抗延迟的轨迹级融合层，通过基于指数衰减的几何相似度，将过时的视觉语言模型选择转化为实时规划器评分。在约2000个真实挑战场景（如交叉口、行人交汇）中，相较于规划器的最佳选择，视觉语言模型选择使平均位移误差降低30%，而规划器在常规场景中仍保持竞争力。仿真实验表明，评分融合机制在高达5秒延迟下仍能维持超过80%的成功率。我们已在移动机器人上完成完整系统验证，使其能够在网络延迟多变的校园复杂行人道上自主导航。

---

### 3. Co-VLA: Coordination-Aware Structured Action Modeling for Dual-Arm Vision-Language-Action Systems

- **作者**: Yandong Wang, Jiaqian Yu, Xiongfeng Peng, Lu Xu, Yamin Mao, Weiming Li, Jaewook Yoo, Dongwook Lee, Daehyun Ji, Mingbo Zhao, Chao Zhang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.20285v1)
- **发表日期**: 2026-06-18
- **匹配关键词**: vision-language-action, bimanual manipulation, VLA
- **arXiv**: [2606.20285v1](http://arxiv.org/abs/2606.20285v1)
- **📥 PDF**: 已下载至本地 (`2606.20285v1_Co-VLA_Coordination-Aware_Structured_Action_Modeling_for_Dual-Arm_Vision-Language-Action_Systems.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型在单臂和双臂机器人操作中展现出强大能力。先前研究表明，通过端到端学习，利用大规模视觉-语言骨干网络结合连续动作预测，可以涌现出协调的双臂行为。然而，当双臂任务耦合度增强且执行约束变得关键时，仅凭隐式协调不足以确保行为的可靠性、可解释性和稳定性。

本文提出Co-VLA——一种引入显式结构先验的协调感知双臂操作框架。我们基于最先进的视觉-语言骨干网络实现该方法，用专为双臂协调设计的结构化动作专家（SAE）替代其单一动作预测头。具体而言，我们在动作生成层面引入显式结构，通过模块化协调感知损失函数，根据任务特定结构塑造共享潜变量和残差潜变量：共享潜变量编码任务级协调意图，残差潜变量则捕捉各臂的执行调整。

在部署阶段，潜变量感知控制器（LAC）通过解读学习到的表征，实时调节同步强度、执行不对称性、平滑度及安全约束。LAC在关节指令层面运行，且与标准控制管线兼容，无需力控或阻抗控制。仿真与真实世界基准实验表明，Co-VLA显著优于单一基线模型：在紧密协调任务中成功率提升27%，在分布外真实场景中性能翻倍（从13%提升至27%），任务完成时间缩短达25%。

---

### 4. Finetuning Vision-Language-Action Models Requires Fewer Layers Than You Think

- **作者**: Gia-Binh Nguyen, Trong-Bao Ho, Thien-Loc Ha, Khoa Vo, Philip Lund Møller, Quang T. Nguyen, Long Dinh, Tuan Dam, Vu Duong, Tung M. Luu, Trung Le, Tran Nguyen Le, Minh Vu, An Thai Le, Ngan Le, Daniel Sonntag, James Zou, Jan Peters, Duy M. H. Nguyen, Ngo Anh Vien
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.20246v1)
- **发表日期**: 2026-06-18
- **匹配关键词**: vision-language-action, vision-language-action model, VLA
- **arXiv**: [2606.20246v1](http://arxiv.org/abs/2606.20246v1)
- **📥 PDF**: 已下载至本地 (`2606.20246v1_Finetuning_Vision-Language-Action_Models_Requires_Fewer_Layers_Than_You_Think.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型在海量视频-机器人数据集上预训练后，彻底革新了机器人操作领域，但其数十亿参数的架构在下游微调和实时推理过程中带来了难以承受的计算负担。本工作中，我们揭示了这些连续控制基础策略（如pi_0、GR00T-N1.5）一个高度非平凡的架构特性：尽管在多样化的物理轨迹上训练，它们却表现出严重的逐层表征冗余。为利用这一特性，我们引入了一种完全无需训练的结构压缩流程，避免了现有方法需要加载完整模型来学习优化令牌缩减或动态层选择器的需求。相反，仅通过一次前向传播，利用中心核对齐识别冗余层特征，我们移除孪生层，将VLM主干网络和连续控制策略头的模型深度永久压缩高达50%。这种精简架构的下游微调带来了双重加速效益：训练时间减少40-50%，实时推理速度提升高达30%，同时性能与完整规模的基础模型持平或更优。我们在三个仿真基准（LIBERO、RoboCasa、SimplerEnv）以及横跨4种不同机器人本体的10项多样化真实世界操作任务上全面验证了该方法。这些结果证明，先进的VLA模型所需的层数远少于先前假设，为可扩展的机器人学习提供了一种高度计算高效的范式。

---

### 5. Frequency-Aware Flow Matching for Continuous and Consistent Robotic Action Generation

- **作者**: Jianing Guo, Fangzheng Chen, Zihao Mao, Wong Lik Hang Kenny, Zhenhong Wu, Yu Li, Yishuai Cai, Yuanpei Chen, Yikun Ban, Kai Chen, Qi Dou, Yaodong Yang, Xianglong Liu, Huijie Zhao, Simin Li
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.20135v1)
- **发表日期**: 2026-06-18
- **匹配关键词**: obstacle avoidance, diffusion policy
- **arXiv**: [2606.20135v1](http://arxiv.org/abs/2606.20135v1)
- **📥 PDF**: 已下载至本地 (`2606.20135v1_Frequency-Aware_Flow_Matching_for_Continuous_and_Consistent_Robotic_Action_Generation.pdf`)
- **🔓 开源**: CODE
- **中文摘要**: 流匹配因其在建模复杂、多模态动作分布方面的强大表达能力，与扩散策略等类似方法一起，已成为机器人操作领域的标准范式。然而，现有方法依赖离散化的动作片段，这使得它们难以适应以异构控制频率采集的演示数据，并容易产生时间上不一致的动作，从而降低控制稳定性。本文提出频率感知流匹配（FAFM），该方法能够输出连续且时间一致的动作。为处理异构频率输入，我们利用离散余弦变换（DCT）将离散动作序列转换到频域，对所得系数进行流匹配，并通过余弦基展开重建连续动作。为生成时间一致的动作，我们对一阶时间导数进行正则化以促进动作平滑性。这相当于一种索伯列夫型约束，能够抑制高频误差并防止动作突变。我们的FAFM方法简单，不引入额外网络参数，可应用于独立的流匹配策略和视觉-语言动作模型。在合成玩具基准测试、避障任务、LapGym和LIBERO数据集上，FAFM在成功率、多模态表达能力、运动平滑性、收敛速度、对机械偏差和混合频率输入的鲁棒性方面均有提升。这些优势在真实Franka机器人部署中保持一致。代码已开源：https://anonymous.4open.science/r/FAFM。

---

### 6. Pose6DAug: Physically Plausible Multi-view Object Swapping for Robot Data Augmentation

- **作者**: Jonghoon Lee, Seong Hyeon Park, Byungwoo Jeon, Minha Lee, Jinwoo Shin
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.20118v1)
- **发表日期**: 2026-06-18
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2606.20118v1](http://arxiv.org/abs/2606.20118v1)
- **📥 PDF**: 已下载至本地 (`2606.20118v1_Pose6DAug_Physically_Plausible_Multi-view_Object_Swapping_for_Robot_Data_Augmentation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）策略在通用操作任务中展现出巨大潜力，但当面对外观或几何形状偏离训练分布的新型物体时，这些策略往往表现不佳。常规解决方案是为每个失败案例收集多视角遥操作数据，但这种方法在成本和时间上均难以扩展。我们提出Pose6DAug——一种基于失败驱动的数据增强框架，无需额外数据采集，即可将策略自身的成功回合转化为针对其失败模式的定向演示。核心洞察在于：每个成功回合已编码了物理有效的动作轨迹及校准后的多视角观测数据。通过保留该轨迹并仅替换操作对象，我们即可获得全新且物理可实现的演示。然而，简单的二维视频编辑会破坏多视角一致性与物理合理性，尤其在严重遮挡和第一人称视角场景下。我们的方法直接作用于三维空间，利用时间连贯的六自由度姿态轨迹驱动的显式网格锚定目标物体，确保所有相机视角下几何一致的渲染效果。在基于本方法增强的数据上微调VLA策略后，新型物体上的成功率相较现有最优基线提升16.5%，同时保持分布内性能不变。实验结果表明，多视角物理一致性增强是实现VLA策略可扩展泛化的实用路径。

---

### 7. EventVLA: Event-Driven Visual Evidence Memory for Long-Horizon Vision-Language-Action Policies

- **作者**: Ganlin Yang, Zhangzheng Tu, Yuqiang Yang, Sitong Mao, Junyi Dong, Tianxing Chen, Jiaqi Peng, Jing Xiong, Jiafei Cao, Jifeng Dai, Wengang Zhou, Yao Mu, Tai Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.20092v1)
- **发表日期**: 2026-06-18
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2606.20092v1](http://arxiv.org/abs/2606.20092v1)
- **📥 PDF**: 已下载至本地 (`2606.20092v1_EventVLA_Event-Driven_Visual_Evidence_Memory_for_Long-Horizon_Vision-Language-Action_Policies.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 记忆仍然是长时域机器人操作的关键瓶颈，因为标准的视觉-语言-动作（VLA）策略在任务相关线索随时间被遮挡或不可观测时常常失效。尽管现有的记忆增强方法利用历史上下文，但它们要么遭受严重的信息瓶颈，要么通过解耦的双系统引入高延迟，要么依赖无选择性缓冲区积累大量视觉冗余。为解决这些局限，我们提出EventVLA——一个基于稀疏视觉证据记忆概念的端到端框架，包含两个核心组件：用于保留初始和短期上下文的基础视觉锚点，以及动态关键帧证据记忆（KEM）模块。具体而言，KEM直接从VLA的潜在嵌入中预测未来关键帧概率，以自主捕获并存储稀疏的任务关键视觉事件。这种前瞻驱动机制使策略能够动态评估当前观测的未来因果效用，在视觉证据变得不可观测前保留瞬时信息。此外，我们提出RoboTwin-MeM——一个专门设计用于评估具有交互式视觉证据的非马尔可夫操作任务的诊断性基准。大量评估表明，在17个需要记忆的仿真任务和4个真实世界双臂操作任务中，EventVLA相较于最先进的记忆增强VLA实现了平均成功率提升+40%。

---

### 8. ENPIRE: Agentic Robot Policy Self-Improvement in the Real World

- **作者**: Wenli Xiao, Jia Xie, Tonghe Zhang, Haotian Lin, Letian "Max" Fu, Haoru Xue, Jalen Lu, Yi Yang, Cunxi Dai, Zi Wang, Jimmy Wu, Guanzhi Wang, S. Shankar Sastry, Ken Goldberg, Linxi "Jim" Fan, Yuke Zhu, Guanya Shi ⭐
  - **高亮作者**: Yuke Zhu, Guanya Shi
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.19980v1)
- **发表日期**: 2026-06-18
- **匹配关键词**: tool use
- **arXiv**: [2606.19980v1](http://arxiv.org/abs/2606.19980v1)
- **📥 PDF**: 已下载至本地 (`2606.19980v1_ENPIRE_Agentic_Robot_Policy_Self-Improvement_in_the_Real_World.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 在现实世界中实现灵巧的机器人操作高度依赖人工监督和算法工程，这成为追求通用物理智能的核心瓶颈。尽管新兴的编码智能体能够生成代码来自动化算法搜索，但其成功仍主要局限于数字环境。我们认为，自动化机器人研究缺失的抽象层是一个可重复的物理世界策略改进反馈循环：重置场景、执行策略、验证结果、优化下一次迭代。为弥合这一鸿沟，我们提出ENPIRE框架——一个为编码智能体设计的支撑系统，通过四个核心模块实例化这一物理反馈流程：环境模块（EN）负责自动重置与验证，策略改进模块（PI）启动策略优化，部署模块（R）通过单台或多台并行运行的物理机器人评估策略，进化模块（E）中编码智能体分析日志、查阅文献、改进训练基础设施与算法代码以应对失败模式。这一闭环系统将现实世界的操作学习转化为可控的优化过程，在最小化人工干预的同时，允许对训练方案和智能体变体进行公平的消融实验。在ENPIRE驱动下，前沿编码智能体可自主训练策略，在整理针盒、紧固扎带、工具使用等具有挑战性的灵巧操作任务中实现99%的成功率——当我们在机器人集群中部署智能体团队时，该过程可进一步加速。我们的研究结果揭示了将编码智能体部署到物理世界以自主推进机器人学的实用且可扩展路径。

---

### 9. EquiVLA: A General Framework for Rotationally Equivariant Vision-Language-Action Models

- **作者**: Thien-Loc Ha, Quang-Tan Nguyen, Trong-Bao Ho, Long Dinh, Minh Duc Nguyen, Gia-Binh Nguyen, Pham Tri Quang, Minh N. Vu, Duy M. H. Nguyen, An Thai Le, Ngo Anh Vien
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.19784v1)
- **发表日期**: 2026-06-18
- **匹配关键词**: vision-language-action, vision-language-action model, VLA
- **arXiv**: [2606.19784v1](http://arxiv.org/abs/2606.19784v1)
- **📥 PDF**: 已下载至本地 (`2606.19784v1_EquiVLA_A_General_Framework_for_Rotationally_Equivariant_Vision-Language-Action_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型已成为通用机器人操作领域的强大范式，但其缺乏几何归纳偏置：在特定朝向训练的模型需要大量额外数据才能泛化至不同旋转配置。我们提出\textsc{EquiVLA}——首个面向端到端$\mathrm{SO}(2)$等变VLA模型的通用框架，可适配任何将冻结视觉-语言骨干网络与流匹配扩散Transformer动作头相结合的架构。\textsc{EquiVLA}引入\textsc{EquiPerceptor}，从冻结的ViT特征中生成近似$\mathrm{SO}(2)$等变的视觉表征；以及\textsc{EquiActor}，一个严格$\mathrm{SO}(2)$等变的流匹配扩散Transformer动作头。两者共同构建从相机观测到预测动作序列的近似$\mathrm{SO}(2)$等变链。基于GR00T~N1.5实例化，并在四个LIBERO套件、CALVIN ABCD$\to$D任务以及Mobile ALOHA上的五个真实机器人任务中评估，\textsc{EquiVLA}在LIBERO上达到$92.6\%$平均成功率（基线为$78.1\%$），在CALVIN上平均序列长度为$4.03$（基线为$3.45$），并将真实机器人成功率从$54\%$提升至$72\%$。

---

### 10. Data Standards for Humanoid Robotics: The Missing Infrastructure for Physical AI

- **作者**: Shaoshan Liu, Xiugong Qin, Xuan Wu, Xuan Xia, Ning Ding, Jialu Liu, Jie Tang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.19769v1)
- **发表日期**: 2026-06-18
- **匹配关键词**: human-robot interaction
- **arXiv**: [2606.19769v1](http://arxiv.org/abs/2606.19769v1)
- **📥 PDF**: 已下载至本地 (`2606.19769v1_Data_Standards_for_Humanoid_Robotics_The_Missing_Infrastructure_for_Physical_AI.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 人形机器人的可扩展性不仅取决于模型和硬件，还取决于物理经验能否在机器人、任务、组织及时间维度上实现积累。基于作者在ISO/TC 299/WG 16工作组中参与制定ISO/WD 26264-1《人形机器人数据集——第1部分：通用要求》的工作实践，本文论证了数据标准正在成为物理人工智能的基础设施。我们提出三个核心观点：第一，人形机器人数据是具身交互数据，而非孤立数字样本的集合；有效数据集必须保留机器人本体、动作、任务、场景、执行轨迹与结果之间的关联性。第二，其价值取决于物理一致性：多模态数据流只有在时间同步、坐标系、标定参数、运动学模型、物理单位及同步假设可追溯时才能实现复用。第三，主要瓶颈不仅在于数据稀缺性，更在于高采集成本、数据孤岛及评估标准不统一导致的非累积性数据。我们认为，人形机器人数据标准通过使具身体验可解释、可共享、可追溯、可复用来突破这些瓶颈。通用标准应提供涵盖生命周期管理、元数据、溯源、质量、版本控制及可追溯性的横向基础设施，而能力专项标准则需定义操作、移动、人机交互、认知及未来人形机器人能力的领域语法。当人工智能从屏幕走向具身形态时，数据标准必须从组织数字信息演进为构建物理交互。

---

### 11. Bidirectional Tutoring for Developmental Motor Learning in Robots: Co-Developed Interaction Dynamics Support Stable Learning

- **作者**: Rui Fukushima, Jun Tani
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.19728v1)
- **发表日期**: 2026-06-18
- **匹配关键词**: object manipulation, human-robot interaction
- **arXiv**: [2606.19728v1](http://arxiv.org/abs/2606.19728v1)
- **📥 PDF**: 已下载至本地 (`2606.19728v1_Bidirectional_Tutoring_for_Developmental_Motor_Learning_in_Robots_Co-Developed_Interaction_Dynamics_.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 众所周知，婴儿通过与照料者的密集互动来发展运动技能。尽管这种社会互动对人类发展至关重要，但机器人运动技能学习通常被视为单向过程——机器人被动接受指导者的示范。这忽视了社会互动的关键特性：其本质上是双向的，指导者与学习者会动态适应彼此。在此类互动中，机器人过往经验可能作为先验约束，塑造其与指导者共同发展轨迹的动态。我们假设：双向指导能使此类约束引导形成保持行为连贯性并支持泛化的稳定行为模式，而单向互动因缺乏此类约束会导致更宽泛、更不连贯的行为模式。为验证该假设，我们开展了两项实验：一项涉及实体人形机器人与人类互动完成物体操作任务，另一项采用AI指导者通过自适应干预机制与真实机器人互动，以检验在更受控条件下是否产生类似效应。我们采用基于自由能原理并扩展生成回放的神经网络实现发展学习框架，支持从单次指导事件中稳定地逐序列学习。在两种情境下，双向指导均促进了行为一致性与阶段性泛化，同时机器人对指导者引导的需求逐渐减少。这些结果表明，作为具身化与社会化相结合的方法，双向指导为机器人发展性运动学习提供了有效支架。

---

### 12. DF-ExpEnse: Diffusion Filtered Exploration for Sample Efficient Finetuning

- **作者**: Calvin Luo, Chen Sun, Shuran Song ⭐
  - **高亮作者**: Shuran Song
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.19656v1)
- **发表日期**: 2026-06-17
- **匹配关键词**: exploration
- **arXiv**: [2606.19656v1](http://arxiv.org/abs/2606.19656v1)
- **📥 PDF**: 已下载至本地 (`2606.19656v1_DF-ExpEnse_Diffusion_Filtered_Exploration_for_Sample_Efficient_Finetuning.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 智能机器人决策的自然方法是：从预训练的生成式控制策略（已总结离线经验）出发，将其适配到自主收集的在线经验中。我们提出DF-ExpEnse探索技术，该技术通过提升在线经验收集质量，从而提高微调样本效率。DF-ExpEnse利用生成式控制策略的多模态建模能力，构建一个表达力强且易于评估的候选动作集，随后通过集成评判器网络识别出在质量与高探索兴趣之间取得最佳平衡的动作。在多智能体场景中，DF-ExpEnse进一步支持跨智能体通信，促进群体协同探索。该方法可无缝集成至现有通过强化学习微调预训练生成式控制策略的框架中。实验表明，在多种操作与运动任务中，相较于默认微调方案及其他动作选择策略，DF-ExpEnse始终能提升样本效率。项目主页：https://df-expense.github.io

---

### 13. One Demo is Worth a Thousand Trajectories: Action-View Augmentation for Visuomotor Policies

- **作者**: Chuer Pan, Litian Liang, Dominik Bauer, Eric Cousineau, Benjamin Burchfiel, Siyuan Feng, Shuran Song ⭐
  - **高亮作者**: Shuran Song
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.19586v1)
- **发表日期**: 2026-06-17
- **匹配关键词**: eye-in-hand, gaussian splatting
- **arXiv**: [2606.19586v1](http://arxiv.org/abs/2606.19586v1)
- **📥 PDF**: 已下载至本地 (`2606.19586v1_One_Demo_is_Worth_a_Thousand_Trajectories_Action-View_Augmentation_for_Visuomotor_Policies.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 用于操作的视觉运动策略在建模复杂机器人行为方面展现出显著潜力，但机器人初始配置的微小变化以及未预见的障碍物极易导致观测数据超出分布范围。若缺乏大规模数据采集，这些因素将引发灾难性的执行失败。本研究提出了一种高效的数据增强框架，能够从配备单鱼眼相机的便携式平行夹爪所采集的真实世界眼内演示中，生成视觉逼真的鱼眼图像序列及对应的物理可行动作轨迹。我们引入了一种针对广角鱼眼相机优化的新型高斯溅射公式，用于重建和编辑包含未见过物体的三维场景。通过轨迹优化生成平滑、无碰撞且利于视图渲染的动作轨迹，并从对应新视角渲染视觉观测数据。仿真与真实世界的综合实验表明，我们的增强框架在相同场景及需规避障碍物的增强场景中，均能提升多种操作任务的成功率。

---

### 14. VisDom: Sparse Novel View Synthesis with Visible Domain Constraint

- **作者**: Mariia Gladkova*, Tarun Yenamandra*, Edmond Boyer, Robert Maier, Tony Tung, Daniel Cremers ⭐
  - **高亮作者**: Daniel Cremers
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.20531v1)
- **发表日期**: 2026-06-18
- **匹配关键词**: nerf, gaussian splatting
- **arXiv**: [2606.20531v1](http://arxiv.org/abs/2606.20531v1)
- **📥 PDF**: 已下载至本地 (`2606.20531v1_VisDom_Sparse_Novel_View_Synthesis_with_Visible_Domain_Constraint.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 稀疏视角新视角合成（NVS）因从少量输入视角恢复三维几何的歧义性而仍具挑战性。基于NeRF和高斯泼溅（GS）的方法在密集监督下表现良好，但在稀疏设置中常出现过拟合，产生漂浮伪影和不一致的几何结构。轮廓一致性常被用作正则化项，但效果有限，因为轮廓一致区域可能超出真实物体几何范围。我们提出VisDom——一种无学习几何约束，通过强制最小多视角可见性要求来增强经典雕刻式视觉外壳重建。具体而言，我们将可见域定义为至少被$K$个视角观测到的三维空间子集，并将其作为标准轮廓重建的附加过滤准则。这为稀疏视角设置提供了更强的空间先验。我们通过限制体素采样和指导优化过程中的高斯放置，将VisDom集成到隐式（NeRF）和显式（GS）管线中。在三个具有挑战性的数据集上的实验表明，该方法在稀疏视角NVS中实现了一致性改进，仅需四张输入图像即可实现高质量以物体为中心的重建。我们的方法具有领域无关性，仅需轮廓信息，且不引入任何可学习参数，因此可作为现有方法的简单补充。在GaussianObject基础上应用VisDom进一步提升了Omni3D和MipNeRF360上的性能，同时以22倍更低的训练成本达到或超越其效果。

---

### 15. LIT-GS: LiDAR-Inertial-Thermal Gaussian Splatting for Illumination-Robust Mapping

- **作者**: Shikuan Shi, Chunran Zheng, Jiaming Xu, Tianyong Ye, Tao Yu, Yukang Cui
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.20424v1)
- **发表日期**: 2026-06-18
- **匹配关键词**: gaussian splatting, neural rendering
- **arXiv**: [2606.20424v1](http://arxiv.org/abs/2606.20424v1)
- **📥 PDF**: 已下载至本地 (`2606.20424v1_LIT-GS_LiDAR-Inertial-Thermal_Gaussian_Splatting_for_Illumination-Robust_Mapping.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 高斯溅射技术实现了实时神经渲染，但现有的激光雷达-惯性-视觉（LIV）高斯映射管线在光照变化和纹理缺失场景中仍显脆弱，因其依赖RGB光度线索。我们提出LIT-GS——一种激光雷达-惯性-热高斯溅射框架，将激光雷达导出的平面几何作为显式约束注入位姿/结构优化与高斯优化过程。具体而言，我们利用LIV视觉地图点作为置信度感知的跨模态锚点，建立可靠的热-激光雷达关联，并在弱热监督下将加权激光雷达点-平面残差引入光束法平差，以联合优化相机位姿与三维点。基于优化后的结构，我们进一步引入激光雷达平面正则化的可微溅射目标函数，约束渲染的三维点与局部观测平面对齐，从而缓解低对比度热图像中的表面增厚与结构漂移问题。在自有序列与公开数据集上的实验表明，LIT-GS在几何精度与渲染质量上持续优于基于LIV的最新高斯溅射基线方法，尤其在具有挑战性的光照条件下表现显著提升。

---

### 16. Towards 3D karst underwater scene reconstruction from rotating sonar data

- **作者**: Georgios Evangelos Margaritis, Lionel Lapierre, Simon Rohou, Zhi Yan, Andreas Nüchter, François Goulette
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.20322v1)
- **发表日期**: 2026-06-18
- **匹配关键词**: 3d reconstruction, 3D reconstruction, navigation, exploration
- **arXiv**: [2606.20322v1](http://arxiv.org/abs/2606.20322v1)
- **📥 PDF**: 已下载至本地 (`2606.20322v1_Towards_3D_karst_underwater_scene_reconstruction_from_rotating_sonar_data.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 岩溶含水层提供关键的淡水资源，但由于其复杂且难以理解的地下几何结构，也构成了重大危害。绘制这些环境的地图具有挑战性，因为水下探测的声纳数据稀疏且噪声大，而导航估计存在漂移问题，限制了标准三维重建方法。我们提出了一种从声纳剖面仪重建水下岩溶管道的流程。该方法结合了连续时间SLAM技术以校正轨迹漂移，并采用新颖的两阶段深度学习表面重建方法，生成可用于水文地质分析的沉浸式可导航三维网格。

---

### 17. Lagrange: An Open-Vocabulary, Energy-Based Sparse Framework for Generalized End-to-End Driving

- **作者**: Shihao Ji, HongXi Li, Zihui Song, Mingyu Li
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.20274v1)
- **发表日期**: 2026-06-18
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2606.20274v1](http://arxiv.org/abs/2606.20274v1)
- **📥 PDF**: 已下载至本地 (`2606.20274v1_Lagrange_An_Open-Vocabulary,_Energy-Based_Sparse_Framework_for_Generalized_End-to-End_Driving.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 将端到端自动驾驶扩展到复杂开放世界环境，需要能够泛化到异常场景的感知模型以及能生成运动学有效轨迹的规划器。现有范式在表征效率与泛化能力之间存在显著矛盾。稠密模型（如占据网络）虽具有几何鲁棒性，但面临关键计算瓶颈且难以进行高层语义推理。相反，基于稀疏查询的规划器虽高效却依赖封闭集定义，易受分布外事件影响。尽管近期视觉-语言-动作模型具备开放词汇推理能力，但其自回归离散令牌生成机制与车辆动力学所需的连续高频控制存在根本冲突。为此，我们提出Lagrange——一种基于掩码隐式场的开放词汇计算稀疏驾驶框架。不同于依赖稠密体积重建或封闭集查询机制，Lagrange利用视觉语言模型将类别无关的目标提议编码为连续语义视觉令牌。我们引入意图驱动的掩码交叉注意力模块，通过时间维度过滤无关实体，将注意力令牌解码为定义在空间坐标上的隐式连续能量场。通过将决策制定框架化为该能量场上的拉格朗日作用量最小化问题，我们在执行避障时严格遵循车辆运动学约束。在标准（nuScenes）和长尾（CODA）基准上的广泛离线评估表明，Lagrange为鲁棒、可解释且运动学可行的开放世界自主驾驶建立了有前景的框架。

---

### 18. MirrorDuo: Reflection-Consistent Visuomotor Learning from Mirrored Demonstration Pairs

- **作者**: Zheyu Zhuang, Ruiyu Wang, Giovanni Luca Marchetti, Florian T. Pokorny, Danica Kragic
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.20048v1)
- **发表日期**: 2026-06-18
- **匹配关键词**: diffusion policy
- **arXiv**: [2606.20048v1](http://arxiv.org/abs/2606.20048v1)
- **📥 PDF**: 已下载至本地 (`2606.20048v1_MirrorDuo_Reflection-Consistent_Visuomotor_Learning_from_Mirrored_Demonstration_Pairs.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 基于图像的行为克隆利用来自无处不在的RGB摄像头的演示数据。然而，该方法仍受限于收集多样化演示的成本，尤其是在适应工作空间变化方面。我们提出MirrorDuo——一种基于反射的框架，通过处理图像、本体感知和完整六自由度末端执行器动作元组，为每个原始演示生成镜像对应物，有效实现"收集一次，免费获得双份"。该框架可作为数据增强策略应用于现有学习流程（如标准行为克隆或扩散策略），也可作为反射等变策略网络的结构先验。通过利用原始域与镜像域之间的重叠，当演示在工作空间两侧均匀分布时，MirrorDuo在相同数据预算下实现了显著提升的性能；当演示仅局限于单侧时，MirrorDuo仅需目标配置中零至五个演示即可实现向镜像工作空间的高效技能迁移。

---

### 19. Tri-Info: Generalizable, Interpretable Failure Prediction for VLA Models via Information Theory

- **作者**: Jinghan Yang, Yunchao Zhang, Wang Yuan, Haolun Wan, Jiaming Zhang, Zhengyang Hu, Yanchao Yang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.19998v1)
- **发表日期**: 2026-06-18
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2606.19998v1](http://arxiv.org/abs/2606.19998v1)
- **📥 PDF**: 已下载至本地 (`2606.19998v1_Tri-Info_Generalizable,_Interpretable_Failure_Prediction_for_VLA_Models_via_Information_Theory.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型正被广泛应用于各类任务，但其黑箱特性使得物理交互可能造成不可逆的伤害，因此亟需具备泛化能力和可解释性的故障检测方法。我们发现，成功与失败的执行轨迹在信息论层面存在系统性差异。基于此，我们将VLA控制形式化为闭环信息管道，推导出三重信息论（Tri-Info）信号，用于捕捉动作多样性、时间一致性与状态转移耦合性。在六个VLA模型和三个基准环境中，Tri-Info在领域内性能与最强基线持平。更关键的是，Tri-Info无需重新训练即可跨架构、跨环境及跨越仿真-现实鸿沟迁移，在先前检测器完全失效的真实世界任务中达到83%的准确率。这确立了Tri-Info作为一种简洁而强大的方法，不仅能通过强跨域泛化能力检测故障，还能提供底层故障模式的可解释诊断。

---

### 20. Geometry-Preserving in 3D Gaussian Splatting for LiDAR-Camera Extrinsic Calibration

- **作者**: Kyoleen Kwak, Daeho Kim, Jeong Woon Lee, Hyoseok Hwang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.20103v1)
- **发表日期**: 2026-06-18
- **匹配关键词**: 3D gaussian splatting, gaussian splatting
- **arXiv**: [2606.20103v1](http://arxiv.org/abs/2606.20103v1)
- **📥 PDF**: 已下载至本地 (`2606.20103v1_Geometry-Preserving_in_3D_Gaussian_Splatting_for_LiDAR-Camera_Extrinsic_Calibration.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 精确的激光雷达-相机标定对于鲁棒的多模态感知至关重要。无靶标方法避免了人工设置，但仍受限于判别性跨模态特征的稀缺性。近期方法通过可微分模型重建场景，利用密集光度监督实现外参优化。其中，3D高斯泼溅（3DGS）作为连接激光雷达与相机的几何代理被广泛采用，可在单一可微分框架内实现跨模态融合。然而，由于3DGS最初是为新视角合成设计的，现有方法往往优先考虑渲染质量，导致代理几何偏离真实的激光雷达结构。我们提出一种框架，通过聚合多视角激光雷达观测实现密集深度监督，并阻止光度梯度更新高斯空间参数，从而保持高斯代理的度量几何特性。在公开驾驶数据集上的验证表明，该方法在校准精度上持续优于现有无靶标方法。

---

