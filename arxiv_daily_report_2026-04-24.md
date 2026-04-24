# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-04-24 08:03

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 2/20 篇提供

**🌟 Highlight**: 11 篇 | **📌 Poster**: 9 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. PokeVLA: Empowering Pocket-Sized Vision-Language-Action Model with Comprehensive World Knowledge Guidance

- **作者**: Yupeng Zheng, Xiang Li, Songen Gu, Yuhang Zheng, Shuai Tian, Weize Li, Linbo Wang, Senyu Fei, Pengfei Li, Yinfeng Gao, Zebin Xing, Yilun Chen, Qichao Zhang, Haoran Li, Wenchao Ding
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.20834v1)
- **发表日期**: 2026-04-22
- **匹配关键词**: vision-language-action model, vision-language-action, VLA, affordance
- **arXiv**: [2604.20834v1](http://arxiv.org/abs/2604.20834v1)
- **📥 PDF**: 已下载至本地 (`2604.20834v1_PokeVLA_Empowering_Pocket-Sized_Vision-Language-Action_Model_with_Comprehensive_World_Knowledge_Guid.pdf`)
- **🔓 开源**: CODE, MODEL, PROJECT_PAGE
  - 链接：https://getterupper.github.io/PokeVLA
- **中文摘要**: 近期，视觉-语言-动作（VLA）模型的最新进展为机器人操作开辟了新途径，但现有方法仍存在效率有限、缺乏高层知识与空间感知能力等问题。针对这些挑战，我们提出PokeVLA——一种轻量级且功能强大的具身操作基础模型，能够有效将视觉语言理解融入动作学习。该框架采用两阶段训练范式：首先，在包含240万样本的精选多模态数据集上预训练紧凑型视觉语言模型（PokeVLM），该数据集涵盖空间定位、功能属性及具身推理任务；其次，通过多视角目标感知语义学习、几何对齐及新型动作专家模块，将操作相关表征注入动作空间。大量实验表明，该方法在LIBERO-Plus基准测试及真实场景部署中均达到最优性能，在成功率及多种扰动下的鲁棒性方面显著优于同类基线模型。为促进可复现性与社区发展，我们将开源代码、模型权重及精选预训练数据集脚本。项目主页：https://getterupper.github.io/PokeVLA

---

### 2. Temporal Difference Calibration in Sequential Tasks: Application to Vision-Language-Action Models

- **作者**: Shelly Francis-Meretzki, Mirco Mutti, Yaniv Romano, Aviv Tamar
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.20472v1)
- **发表日期**: 2026-04-22
- **匹配关键词**: vision-language-action model, vision-language-action, VLA
- **arXiv**: [2604.20472v1](http://arxiv.org/abs/2604.20472v1)
- **📥 PDF**: 已下载至本地 (`2604.20472v1_Temporal_Difference_Calibration_in_Sequential_Tasks_Application_to_Vision-Language-Action_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 近期，视觉-语言-动作（VLA）模型在机器人领域的进展凸显了在序列任务中进行可靠不确定性量化的重要性。然而，在此类场景中评估和改进校准效果仍鲜有探索，尤其在仅能观测到部分轨迹的情况下。本研究针对片段式任务提出序列校准方法——任务成功置信度在片段执行过程中逐步生成，而成功与否在片段结束时判定。我们引入Brier分数的序列扩展形式，并证明在二元结果条件下，其风险最小化函数与VLA策略的价值函数等价。这一发现将不确定性校准与强化学习联系起来，使得时序差分（TD）价值估计可作为随时间演化的原则性校准机制。实验表明，在仿真数据和真实机器人数据上，TD校准相较于现有最优方法能显著提升性能。值得注意的是，与近期采用不同校准技术的研究结论相反，我们发现当使用TD方法进行校准时，VLA模型单步动作概率可产生具有竞争力的不确定性估计。

---

### 3. A Vision-Language-Action Model for Adaptive Ultrasound-Guided Needle Insertion and Needle Tracking

- **作者**: Yuelin Zhang, Qingpeng Ding, Longxiang Tang, Chengyu Fang, Shing Shin Cheng
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.20347v1)
- **发表日期**: 2026-04-22
- **匹配关键词**: vision-language-action model, vision-language-action, VLA
- **arXiv**: [2604.20347v1](http://arxiv.org/abs/2604.20347v1)
- **📥 PDF**: 已下载至本地 (`2604.20347v1_A_Vision-Language-Action_Model_for_Adaptive_Ultrasound-Guided_Needle_Insertion_and_Needle_Tracking.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 超声引导下的针穿刺是一项关键但具有挑战性的操作，其难点在于动态成像条件及针尖可视化困难。现有自动穿刺方法多依赖手工设计的模块化控制器流程，在复杂场景下性能显著下降。本文提出一种面向机器人超声系统的视觉-语言-动作模型，用于实现自适应、自动化的超声引导针穿刺与追踪。该框架为针追踪与穿刺控制提供了统一方案，能够基于实时获取的针尖位置和环境感知动态调整穿刺策略。为实现实时端到端追踪，我们提出跨深度融合追踪头，通过整合大规模视觉骨干网络的浅层位置特征与深层语义特征。为适配预训练视觉骨干网络至追踪任务，引入追踪条件寄存器实现参数高效的特征调节。在针追踪之后，提出不确定性感知控制策略与异步视觉-语言-动作流水线，实现自适应穿刺控制，确保决策及时性以提升安全性与操作效果。在针追踪与穿刺的广泛实验中，本方法持续优于现有最优追踪器及人工操作，实现了更高的追踪精度、穿刺成功率与更短的操作时间，为基于机器人超声的智能介入治疗指明了发展方向。

---

### 4. Cortex 2.0: Grounding World Models in Real-World Industrial Deployment

- **作者**: Adriana Aida, Walida Amer, Katarina Bankovic, Dhruv Behl, Fabian Busch, Annie Bhalla, Minh Duong, Florian Gienger, Rohan Godse, Denis Grachev, Ralf Gulde, Elisa Hagensieker, Junpeng Hu, Shivam Joshi, Tobias Knoblauch, Likith Kumar, Damien LaRocque, Keerthana Lokesh, Omar Moured, Khiem Nguyen, Christian Preyss, Ranjith Sriganesan, Vikram Singh, Carsten Sponner, Anh Tong, Dominik Tuscher, Marc Tuscher, Pavan Upputuri
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.20246v1)
- **发表日期**: 2026-04-22
- **匹配关键词**: contact-rich manipulation, vision-language-action, vision-language-action model
- **arXiv**: [2604.20246v1](http://arxiv.org/abs/2604.20246v1)
- **📥 PDF**: 已下载至本地 (`2604.20246v1_Cortex_2.0_Grounding_World_Models_in_Real-World_Industrial_Deployment.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 工业机器人操作需要在不同本体、任务及变化的物体分布中实现可靠的长时域执行。尽管视觉-语言-动作模型展现出强大的泛化能力，但其本质上仍属于反应式系统。由于仅基于当前观测优化下一步动作而不评估潜在未来状态，这类模型在面对长时域任务的复合故障模式时显得脆弱。Cortex 2.0系统从反应式控制转向"规划-执行"范式：在视觉隐空间中生成候选未来轨迹，根据预期成功率和效率进行评分，最终仅执行得分最高的候选方案。我们在单臂和双臂操作平台上对Cortex 2.0进行了评估，涵盖四种复杂度递增的任务：拾放操作、物品与垃圾分拣、螺丝分拣以及鞋盒拆包。Cortex 2.0在所有任务中均持续超越最先进的视觉-语言-动作基线模型，取得最优结果。在反应式策略失效的非结构化环境中（如重度杂乱、频繁遮挡及接触密集型操作），该系统仍保持可靠性能。这些结果表明，基于世界模型的规划能够在复杂工业环境中稳定运行。

---

### 5. JoyAI-RA 0.1: A Foundation Model for Robotic Autonomy

- **作者**: Tianle Zhang, Zhihao Yuan, Dafeng Chi, Peidong Liu, Dongwei Li, Kejun Hu, Likui Zhang, Junnan Nie, Ziming Wei, Zengjue Chen, Yili Tang, Jiayi Li, Zhiyuan Xiang, Mingyang Li, Tianci Luo, Hanwen Wan, Ao Li, Linbo Zhai, Zhihao Zhan, Yuzheng Zhuang, Liang Lin, Xiaodong Bai, Jiakun Cai, Peng Cao, Kangliang Chen, Siang Chen, Yixiang Dai, Shuai Di, Nan Duan, Yicheng Gong, Chenguang Gui, Yucheng Guo, Peng Hao, Qingrong He, Haoyang Huang, Kunrui Huang, Zhixuan Huang, Shibo Jin, Yixiang Jin, Anson Li, Dongjiang Li, Jiawei Li, Ruodai Li, Yihang Li, Yuzhen Li, Jiaming Liang, Fangsheng Liu, Jing Long, Mingxi Luo, Xing Pan, Hui Shen, Xiaomeng Tian, Daming Wang, Song Wang, Junwu Xiong, Hang Xu, Wanting Xu, Zhengcheng Yu, He Zhang, Jiyao Zhang, Lin Zhao, Chen Zhou
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.20100v1)
- **发表日期**: 2026-04-22
- **匹配关键词**: vision-language-action, VLA
- **arXiv**: [2604.20100v1](http://arxiv.org/abs/2604.20100v1)
- **📥 PDF**: 已下载至本地 (`2604.20100v1_JoyAI-RA_0.1_A_Foundation_Model_for_Robotic_Autonomy.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 开放世界环境中的机器人自主性从根本上受到数据多样性不足和跨本体泛化能力差的限制。现有机器人数据集在规模和任务覆盖范围上往往有限，而不同机器人本体间的显著差异阻碍了有效行为知识的迁移。为解决这些挑战，我们提出JoyAI-RA——一种专为可泛化机器人操作设计的视觉-语言-动作（VLA）具身基础模型。JoyAI-RA构建了多源多层级预训练框架，整合网络数据、大规模第一人称人类操作视频、仿真生成轨迹及真实机器人数据。通过基于显式动作空间统一的异构多源数据训练，JoyAI-RA有效弥合了本体差异（尤其是人类操作与机器人控制之间的鸿沟），从而增强跨本体行为学习能力。在仿真与真实世界基准测试中，JoyAI-RA均优于现有最先进方法，尤其在需要泛化能力的多样化任务上表现突出。

---

### 6. EmbodiedMidtrain: Bridging the Gap between Vision-Language Models and Vision-Language-Action Models via Mid-training

- **作者**: Yiyang Du, Zhanqiu Guo, Xin Ye, Liu Ren, Chenyan Xiong
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.20012v1)
- **发表日期**: 2026-04-21
- **匹配关键词**: vision-language-action model, vision-language-action, VLA
- **arXiv**: [2604.20012v1](http://arxiv.org/abs/2604.20012v1)
- **📥 PDF**: 已下载至本地 (`2604.20012v1_EmbodiedMidtrain_Bridging_the_Gap_between_Vision-Language_Models_and_Vision-Language-Action_Models_v.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作模型（VLAs）从视觉-语言模型（VLMs）继承了视觉和语言能力，然而大多数VLAs基于现成的VLMs构建，这些VLMs并未针对具身领域进行适配，从而限制了其下游性能。在本工作中，我们提出EmbodiedMidtrain方法以弥合VLMs与VLAs之间的差距。首先，我们刻画了两者之间的数据分布差异，表明VLA数据占据与更广泛的VLM分布高度分离的紧凑区域，而VLM数据源内部及之间的对齐程度存在显著差异。接着，我们构建了一个中期训练数据引擎，利用轻量级可学习邻近性估计器从大规模VLM数据池中筛选出与VLA最对齐的候选数据，并在下游VLA微调前对VLM进行基于此精选混合数据的中期训练。在三个机器人操作基准上的实验表明，中期训练能够持续提升不同VLM骨干网络的性能，达到与使用更大模型规模和训练预算的专家级VLAs及现成VLMs相竞争的结果。进一步分析揭示，中期训练为VLA微调提供了更强的初始化，其增益从训练初期即显现并随训练过程持续扩大。此外，该数据引擎同时捕捉了数据集层面和样本层面的对齐信号，在保持VLM数据多样性的同时，更偏好空间推理任务而非文本中心任务。我们将公开发布所有代码、数据和模型以供未来研究。

---

### 7. UniT: Toward a Unified Physical Language for Human-to-Humanoid Policy Learning and World Modeling

- **作者**: Boyu Chen, Yi Chen, Lu Qiu, Jerry Bai, Yuying Ge, Yixiao Ge
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.19734v1)
- **发表日期**: 2026-04-21
- **匹配关键词**: VLA
- **arXiv**: [2604.19734v1](http://arxiv.org/abs/2604.19734v1)
- **📥 PDF**: 已下载至本地 (`2604.19734v1_UniT_Toward_a_Unified_Physical_Language_for_Human-to-Humanoid_Policy_Learning_and_World_Modeling.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 扩展人形机器人基础模型的规模受到机器人数据稀缺的瓶颈制约。尽管海量第一人称人类数据提供了可扩展的替代方案，但由于运动学差异，跨形态鸿沟的弥合仍是一项根本性挑战。我们提出UniT（基于视觉锚定的统一潜在动作分词器），该框架为从人类到人形机器人的迁移建立了统一的物理语言。基于"异构运动学共享普适视觉结果"这一核心理念，UniT采用三分支交叉重建机制：动作分支通过预测视觉结果将运动学锚定至物理输出，视觉分支通过重建动作滤除无关视觉干扰，融合分支则将这两种纯化模态协同映射至与形态无关的共享离散潜在意图空间。我们在两种范式下验证UniT：1）策略学习（VLA-UniT）：通过预测这些统一分词，有效利用多样化人类数据，在人形机器人仿真基准和真实部署中实现最先进的数据效率与鲁棒分布外泛化，尤其展现出零样本任务迁移能力。2）世界建模（WM-UniT）：以统一分词为条件对齐跨形态动力学，实现从人类到人形机器人的直接动作迁移。这种对齐确保人类数据无缝转化为增强的人形机器人视频生成动作可控性。最终，通过诱导高度对齐的跨形态表征（t-SNE可视化实证表明人类与人形机器人特征收敛至共享流形），UniT为将海量人类知识提炼为通用人形机器人能力提供了可扩展路径。

---

### 8. Mask World Model: Predicting What Matters for Robust Robot Policy Learning

- **作者**: Yunfan Lou, Xiaowei Chi, Xiaojie Zhang, Zezhong Qian, Chengxuan Li, Rongyu Zhang, Yaoxu Lyu, Guoyu Song, Chuyao Fu, Haoxuan Xu, Pengwei Wang, Shanghang Zhang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.19683v2)
- **发表日期**: 2026-04-21
- **匹配关键词**: diffusion-based policy
- **arXiv**: [2604.19683v2](http://arxiv.org/abs/2604.19683v2)
- **📥 PDF**: 已下载至本地 (`2604.19683v2_Mask_World_Model_Predicting_What_Matters_for_Robust_Robot_Policy_Learning.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 基于大规模视频生成预训练的世界模型，已成为通用机器人策略学习的一种有前景的范式。然而，标准方法通常侧重于高保真RGB视频预测，这可能导致模型过度拟合动态背景和光照变化等无关因素。这些干扰降低了模型的泛化能力，最终导致不可靠且脆弱的控制策略。为解决这一问题，我们提出了掩码世界模型（MWM），该模型利用视频扩散架构预测语义掩码的演化而非像素变化。这一转变引入了几何信息瓶颈，迫使模型在过滤视觉噪声的同时捕捉基本的物理动力学和接触关系。我们将这一掩码动力学主干与基于扩散的策略头无缝集成，以实现鲁棒的端到端控制。大量评估表明，MWM在LIBERO和RLBench仿真基准上具有显著优势，其性能大幅超越当前最先进的基于RGB的世界模型。此外，真实世界实验和鲁棒性评估（通过随机令牌剪枝）显示，MWM展现出卓越的泛化能力以及对纹理信息丢失的强鲁棒性。

---

### 9. Assessing VLM-Driven Semantic-Affordance Inference for Non-Humanoid Robot Morphologies

- **作者**: Jess Jones, Raul Santos-Rodriguez, Sabine Hauert
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.19509v1)
- **发表日期**: 2026-04-21
- **匹配关键词**: object manipulation, tool use, affordance
- **arXiv**: [2604.19509v1](http://arxiv.org/abs/2604.19509v1)
- **📥 PDF**: 已下载至本地 (`2604.19509v1_Assessing_VLM-Driven_Semantic-Affordance_Inference_for_Non-Humanoid_Robot_Morphologies.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言模型（VLMs）在理解人-物交互方面展现出卓越能力，但其在非人形形态机器人系统中的应用仍鲜有探索。本研究探究VLMs能否有效推断具有与人类根本不同形态的机器人的可供性，填补了这些模型在多样化机器人应用部署中的关键空白。我们提出一种新型混合数据集，将标注的真实世界机器人可供性-物体关系与VLM生成的合成场景相结合，并对多个物体类别和机器人形态下的VLM性能进行实证分析，揭示了可供性推断能力的显著差异。实验表明，虽然VLMs对非人形机器人形态展现出有前景的泛化能力，但其在不同物体领域的表现存在显著不一致性。关键的是，我们发现在所有形态和物体类别中普遍存在低假阳性率但高假阴性率的一致模式，表明VLMs倾向于保守的可供性预测。分析显示，这种模式在新颖工具使用场景和非常规物体操作中尤为突出，这表明将VLMs有效集成到机器人系统中需要采用互补方法，在保持低假阳性率固有安全优势的同时，缓解过度保守的行为。

---

### 10. Multimodal embodiment-aware navigation transformer

- **作者**: Louis Dezons, Quentin Picard, Rémi Marsal, François Goulette, David Filliat
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.19267v1)
- **发表日期**: 2026-04-21
- **匹配关键词**: navigation
- **arXiv**: [2604.19267v1](http://arxiv.org/abs/2604.19267v1)
- **📥 PDF**: 已下载至本地 (`2604.19267v1_Multimodal_embodiment-aware_navigation_transformer.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 基于监督学习训练的地面机器人目标导向导航模型展现出良好的零样本迁移能力，但其避障性能在分布偏移（如环境、机器人或传感器配置变化）下会显著下降。我们提出ViLiNT——一种基于注意力机制的多模态目标导航策略，该策略利用来自多平台和多环境的异构数据进行训练，通过两个关键特性提升鲁棒性。首先，我们采用Transformer架构融合RGB图像、3D激光雷达点云、目标嵌入向量及机器人本体描述符，以捕获互补的几何与外观线索。Transformer输出用于调节生成可导航轨迹的扩散模型。其次，利用自动生成的离线标签，我们训练路径通畅度预测头，用于对扩散模型生成的轨迹进行评分和排序。扩散调节机制与轨迹排序头均依赖于机器人本体令牌，使模型能够根据机器人尺寸生成并选择轨迹。在三个模拟环境中，ViLiNT的平均成功率较当前最先进的纯视觉基线模型（NoMaD）提升166%。通过部署在障碍物场地的巡视车实际测试，该性能提升得到验证。这些结果表明，多模态融合与碰撞预测机制的结合可显著提升越野导航的鲁棒性。

---

### 11. BALTIC: A Benchmark and Cross-Domain Strategy for 3D Reconstruction Across Air and Underwater Domains Under Varying Illumination

- **作者**: Michele Grimaldi, David Nakath, Oscar Pizarro, Jonatan Scharff Willners, Ignacio Carlucho, Yvan R. Petillot
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.19133v1)
- **发表日期**: 2026-04-21
- **匹配关键词**: neural radiance field, 3D reconstruction, gaussian splatting, 3D gaussian splatting, 3d reconstruction
- **arXiv**: [2604.19133v1](http://arxiv.org/abs/2604.19133v1)
- **📥 PDF**: 已下载至本地 (`2604.19133v1_BALTIC_A_Benchmark_and_Cross-Domain_Strategy_for_3D_Reconstruction_Across_Air_and_Underwater_Domains.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 在不同环境条件下实现鲁棒的三维重建，对于机器人感知而言仍是一项关键挑战，尤其是在空气与水体之间过渡的场景中。为此，我们提出BALTIC——一个受控基准测试集，旨在系统评估现代三维重建方法在介质与光照变化下的表现。该基准包含13个数据集，涵盖两种介质（空气和水）及三种光照条件（环境光、人造光和混合光），并引入运动类型、扫描模式和初始化轨迹的额外变化，从而形成多样化的序列集合。我们的实验装置配备定制水箱、单目相机和HTC Vive追踪器，能够实现精确的真实姿态估计。此外，我们通过将水下图像序列与少量在相似光照条件下捕获的空气视图相结合，进一步研究了跨域重建问题。我们利用COLMAP从轨迹精度和场景几何两方面评估运动恢复结构（SfM）重建效果，并将这些重建结果作为神经辐射场（NeRF）和三维高斯泼溅（3D Gaussian Splatting）方法的输入。最终模型通过与真实轨迹及空气参考数据进行对比评估，同时使用感知指标和光度指标比较渲染输出。此外，我们进行了颜色恢复分析以评估跨域的辐射一致性。结果表明，在受控且纹理一致的条件下，采用简单预处理（如白平衡校正）的高斯泼溅方法可达到与专用水下方法相当的性能，但其鲁棒性在更复杂、异质的真实环境中会有所下降。

---

## 📌 Poster

*其他相关研究*

---

### 1. DeVI: Physics-based Dexterous Human-Object Interaction via Synthetic Video Imitation

- **作者**: Hyeonwoo Kim, Jeonghwan Kim, Kyungwon Cho, Hanbyul Joo
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.20841v1)
- **发表日期**: 2026-04-22
- **匹配关键词**: motion planning
- **arXiv**: [2604.20841v1](http://arxiv.org/abs/2604.20841v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 视频生成模型的最新进展使得在广泛场景和物体类别中合成逼真的人-物交互视频成为可能，包括运动捕捉系统难以捕捉的复杂灵巧操作。尽管这些合成视频中蕴含的丰富交互知识为灵巧机器人操作的运动规划提供了巨大潜力，但其有限的物理保真度和纯二维特性使其难以直接作为基于物理的角色控制中的模仿目标。我们提出DeVI（灵巧视频模仿）——一种新颖框架，利用文本条件合成视频实现与未见目标物体交互的物理合理灵巧智能体控制。为克服生成式二维线索的不精确性，我们引入混合跟踪奖励机制，将三维人体跟踪与鲁棒的二维物体跟踪相结合。与依赖高质量三维运动学演示的方法不同，DeVI仅需生成视频即可实现跨不同物体和交互类型的零样本泛化。大量实验表明，DeVI在模仿三维人-物交互演示方面优于现有方法，尤其在建模灵巧手-物交互时表现突出。我们进一步在多物体场景和文本驱动动作多样性中验证了DeVI的有效性，展示了将视频作为具备人-物交互感知能力的运动规划器的优势。

---

### 2. Visual-Tactile Peg-in-Hole Assembly Learning from Peg-out-of-Hole Disassembly

- **作者**: Yongqiang Zhao, Xuyang Zhang, Zhuo Chen, Matteo Leonetti, Emmanouil Spyrakos-Papastavridis, Shan Luo
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.20712v1)
- **发表日期**: 2026-04-22
- **匹配关键词**: exploration
- **arXiv**: [2604.20712v1](http://arxiv.org/abs/2604.20712v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 插孔（PiH）装配是一项基础但具有挑战性的机器人操作任务。尽管强化学习（RL）在解决此类任务中展现出潜力，但其需要大量的探索。本文提出了一种新颖的视觉-触觉技能学习框架，通过利用其逆任务——即拔销（PooH）拆卸——来促进PiH学习。与PiH相比，PooH本质上更简单，因为它只需克服现有摩擦力而无需精确对准，从而使得数据收集更加高效。为此，我们在统一环境中将PooH和PiH均建模为部分可观测马尔可夫决策过程（POMDP），并共享视觉-触觉观测空间。首先训练视觉-触觉PooH策略；其包含运动学、视觉和触觉信息的轨迹被时间反转并随机化动作，为PiH提供专家数据。在策略学习中，视觉感知辅助销-孔接近，而触觉测量补偿销-孔未对准。跨不同销-孔几何形状的实验表明，视觉-触觉策略的接触力比单模态策略低6.4%，且我们的框架在已知物体上平均成功率达87.5%，在未知物体上达77.1%，比从头训练PiH策略的直接RL方法成功率高出18.1%。演示、代码和数据集可在https://sites.google.com/view/pooh2pih获取。

---

### 3. Where are they looking in the operating room?

- **作者**: Keqi Chen, Séraphin Baributsa, Lilien Schewski, Vinkle Srivastav, Didier Mutter, Guido Beldi, Sandra Keller, Nicolas Padoy
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.20574v1)
- **发表日期**: 2026-04-22
- **匹配关键词**: human-robot interaction
- **arXiv**: [2604.20574v1](http://arxiv.org/abs/2604.20574v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 目的：视线跟随（即推断个体注视方向的任务）已在计算机视觉领域得到广泛研究，推动了视觉注意力建模、社交场景理解及人机交互等研究的发展。然而，在手术室这一视觉注意力对手术流程分析具有重要作用的复杂高风险环境中，视线跟随技术尚未被探索。本研究首次将视线跟随概念引入手术领域，并证明其在理解手术室中临床角色、手术阶段及团队沟通方面的巨大潜力。方法：我们为4D-OR数据集扩展了视线跟随标注，并为Team-OR数据集新增了视线跟随及团队沟通活动标注。随后提出基于视线跟随模型的新方法，用于临床角色预测、手术阶段识别及团队沟通检测。针对角色与阶段识别，我们提出仅依赖视线预测的视线热力图方法；针对团队沟通检测，我们以自监督方式训练时空模型编码基于视线的片段特征，并将特征输入时序活动检测模型。结果：在4D-OR和Team-OR数据集上的实验表明，我们的方法在所有下游任务中均达到最优性能。量化结果显示，该方法在临床角色预测中F1分数达0.92，手术阶段识别达0.95。此外，在团队沟通检测中，该方法显著超越现有基线，将此前最佳性能提升超过30%。结论：我们首次将手术室中的视线跟随作为手术数据科学的新研究方向，凸显其在计算机辅助干预中推动手术流程分析的巨大潜力。

---

### 4. VTouch++: A Multimodal Dataset with Vision-Based Tactile Enhancement for Bimanual Manipulation

- **作者**: Qianxi Hua, Xinyue Li, Zheng Yan, Yang Li, Chi Zhang, Yongyao Li, Yufei Liu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.20444v1)
- **发表日期**: 2026-04-22
- **匹配关键词**: bimanual manipulation
- **arXiv**: [2604.20444v1](http://arxiv.org/abs/2604.20444v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 近年来，具身智能技术发展迅速，但双臂操作——尤其是在高接触性任务中——仍面临挑战。这主要源于缺乏具备丰富物理交互信号、系统化任务组织及充足规模的数据集。为解决上述局限，我们提出VTOUCH数据集。该数据集通过基于视觉的触觉感知技术提供高保真物理交互信号，采用矩阵式任务设计实现系统性学习，并构建覆盖真实场景与需求驱动场景的自动化数据采集流程以确保可扩展性。为验证数据集有效性，我们开展了跨模态检索的定量实验及真实机器人评估。最终，通过跨多机器人、多策略、多任务的泛化推理，我们展示了其在真实场景中的实际性能。

---

### 5. Bimanual Robot Manipulation via Multi-Agent In-Context Learning

- **作者**: Alessio Palma, Indro Spinelli, Vignesh Prasad, Luca Scofano, Yufeng Jin, Georgia Chalvatzaki, Fabio Galasso
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.20348v1)
- **发表日期**: 2026-04-22
- **匹配关键词**: bimanual manipulation
- **arXiv**: [2604.20348v1](http://arxiv.org/abs/2604.20348v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 语言模型（LLMs）已成为具身控制领域的强大推理引擎。特别是，上下文学习（ICL）使现成的纯文本LLMs能够预测机器人动作，无需任何任务特定训练，同时保持其泛化能力。将ICL应用于双臂操作仍具挑战性，因为高维联合动作空间和紧密的臂间协调约束会迅速超出标准上下文窗口的容量。为此，我们提出BiCICLe（双臂协调上下文学习），这是首个使标准LLMs无需微调即可执行少样本双臂操作的框架。BiCICLe将双臂控制建模为多智能体领导者-跟随者问题，将动作空间解耦为顺序的、条件化的单臂预测。这自然延伸出"双臂辩论"——一种迭代优化过程，并引入第三个LLM作为裁判，评估并选择最合理的协调轨迹。在TWIN基准的13个任务上评估，BiCICLe实现了高达71.1%的平均成功率，比最佳无训练基线高出6.7个百分点，并超越了大多数监督方法。我们还在新任务上展示了强大的少样本泛化能力。

---

### 6. AdaTracker: Learning Adaptive In-Context Policy for Cross-Embodiment Active Visual Tracking

- **作者**: Kui Wu, Hao Chen, Jinzhu Han, Haijun Liu, Churan Wang, Yizhou Wang, Zhoujun Li, Si Liu, Fangwei Zhong
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.20305v1)
- **发表日期**: 2026-04-22
- **匹配关键词**: visual tracking
- **arXiv**: [2604.20305v1](http://arxiv.org/abs/2604.20305v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 实现跨不同机器人平台的统一主动视觉跟踪模型具有挑战性，因为不同平台的物理约束和运动动力学差异显著。现有方法通常为每种机器人形态单独训练模型，导致可扩展性差且泛化能力有限。为此，我们提出AdaTracker——一种自适应上下文策略学习框架，能够稳健地跟踪不同机器人形态的目标。我们的核心创新在于通过"形态上下文编码器"显式建模形态特定约束，该编码器从历史数据中推断形态约束。这种上下文表征动态调节"上下文感知策略"，使其能够以零样本方式为未见过的机器人形态推断最优控制动作。为增强鲁棒性，我们引入两个辅助目标函数以确保准确的上下文识别与时间一致性。仿真与真实世界实验表明，AdaTracker在跨形态泛化、样本效率及零样本适应方面显著优于现有最优方法。

---

### 7. LLM-Guided Safety Agent for Edge Robotics with an ISO-Compliant Perception-Compute-Control Architecture

- **作者**: Xu Huang, Ruofan Zhang, Lu Cheng, Yuefeng Song, Xu Huang, Huayu Zhang, Sheng Yin, Anyang Liang, Chen Qian, Yin Zhou, Xiaoyun Yuan, Yuan Cheng
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.20193v1)
- **发表日期**: 2026-04-22
- **匹配关键词**: human-robot interaction
- **arXiv**: [2604.20193v1](http://arxiv.org/abs/2604.20193v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 在人机交互中确保功能安全具有挑战性，因为人工智能感知本质上是概率性的，而工业标准要求确定性行为。我们提出了一种基于LLM引导的边缘机器人安全代理，构建于符合ISO标准的低延迟感知-计算-控制架构之上。该方法将自然语言安全规范转化为可执行谓词，并通过冗余异构边缘运行时进行部署。为实现边缘约束下的容错闭环执行，我们采用对称双模冗余设计，通过并行独立执行实现低延迟感知、计算与控制。我们在双RK3588平台上构建原型系统，并在代表性人机交互场景中进行评估。结果表明，该方案利用高性价比硬件，为达到ISO 13849 Category 3和PL d标准提供了切实可行的边缘实现路径，支持安全关键型具身AI的实际部署。

---

### 8. Toward Safe Autonomous Robotic Endovascular Interventions using World Models

- **作者**: Harry Robertshaw, Nikola Fischer, Han-Ru Wu, Andrea Walker Perez, Weiyuan Deng, Benjamin Jackson, Christos Bergeles, Alejandro Granados, Thomas C Booth
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.20151v1)
- **发表日期**: 2026-04-22
- **匹配关键词**: navigation
- **arXiv**: [2604.20151v1](http://arxiv.org/abs/2604.20151v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 自主机械取栓（MT）因血管几何结构高度多变以及对精准实时控制的需求而面临重大挑战。尽管强化学习（RL）已成为实现血管内导航自动化的有前景范式，但现有方法在面对不同患者解剖结构或长距离导航任务时，往往表现出有限的鲁棒性。本研究探索了一种基于世界模型的自主血管内导航框架，该框架建立在TD-MPC2（一种融合规划与学习动力学的基于模型的强化学习方法）之上。我们训练了一个TD-MPC2智能体，使其在多个导航任务中应对未接触过的患者特异性血管结构，并将其性能与当前最先进的软演员-评论家（SAC）算法智能体进行对比评估。两种方法均在透视引导下，利用患者特异性血管模型进行了体外验证。在仿真实验中，TD-MPC2的平均成功率显著高于SAC（58% vs. 36%，p < 0.001），平均尖端接触力为0.15 N，远低于建议的1.5 N血管破裂阈值。体外实验中，TD-MPC2的平均成功率（68%）与SAC（60%）相当，但TD-MPC2以更长的操作时间（p < 0.001）为代价，实现了更优的路径比（p = 0.017）。综合而言，这些结果首次展示了自主MT导航在未接触过的计算机模拟数据与透视引导体外实验中的双重验证，凸显了世界模型在实现安全且可泛化的AI辅助血管内介入治疗中的潜力。

---

### 9. Multi-modal Reasoning with LLMs for Visual Semantic Arithmetic

- **作者**: Chuou Xu, Liya Ji, Qifeng Chen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.19567v1)
- **发表日期**: 2026-04-21
- **匹配关键词**: human-robot interaction
- **arXiv**: [2604.19567v1](http://arxiv.org/abs/2604.19567v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: CODE
- **中文摘要**: 强化学习（RL）作为后训练方法，对于提升大型语言模型（LLMs）在编程和数学领域的推理能力至关重要。然而，它们在视觉语义算术（即从图像中推断关系）方面的能力仍未被充分探索。经典的文本类比“国王”-“男人”+“女人”=“女王”展示了关系推理，但将文本替换为“国王”和“男人”的图像后，性能显著下降，因为这需要常识知识以及从无关的视觉细节中提取简洁概念。这种能力对于非结构化环境中的服务机器人和家用机器人至关重要，因为这些机器人必须推断物体、智能体和动作之间的语义关系。在厨房场景中，从图像中识别出“粉末”和“蛋糕”通过“由……制成”相关联，将符号关系扎根于感知，从而实现工具替换、任务泛化和改进的语义推理。先前的工作通过向量算术后解码图像特征来尝试语义算术，但存在模态差距且缺乏系统评估。在本文中，我们提出了两个新任务：两项减法和三项运算，并构建了图像关系对数据集（IRPD）用于基准测试。我们进一步提出了语义算术强化微调（SAri-RFT），该方法使用可验证函数和群体相对策略优化（GRPO）对大型视觉语言模型（LVLMs）进行后训练。我们的方法在IRPD和真实世界的Visual7W-Telling数据集上取得了最先进的结果。通过赋予LVLMs强大的跨模态关系推理能力，本研究提升了家用机器人在感知中扎根符号推理的能力，从而增强了复杂环境中的决策、工具适应性以及人机交互。数据集和源代码已在补充材料中提供。

---

