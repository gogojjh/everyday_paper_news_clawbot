# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-04-23 08:05

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 5/20 篇提供

**🌟 Highlight**: 20 篇 | **📌 Poster**: 0 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. UniT: Toward a Unified Physical Language for Human-to-Humanoid Policy Learning and World Modeling

- **作者**: Boyu Chen, Yi Chen, Lu Qiu, Jerry Bai, Yuying Ge, Yixiao Ge
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.19734v1)
- **发表日期**: 2026-04-21
- **匹配关键词**: VLA
- **arXiv**: [2604.19734v1](http://arxiv.org/abs/2604.19734v1)
- **📥 PDF**: 已下载至本地 (`2604.19734v1_UniT_Toward_a_Unified_Physical_Language_for_Human-to-Humanoid_Policy_Learning_and_World_Modeling.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 人形机器人基础模型的规模化发展受限于机器人数据的稀缺性。海量第一人称人类数据虽提供了可扩展的替代方案，但运动学差异导致的跨具身鸿沟仍是根本性挑战。我们提出UniT（基于视觉锚定的统一潜在动作分词器），该框架构建了人机迁移的统一物理语言。基于"异构运动学具有普适视觉结果"的核心思想，UniT采用三支路交叉重构机制：动作预测视觉以锚定运动学与物理结果，视觉重构动作以过滤无关视觉干扰，同时融合支路将净化后的多模态信息协同编码至具身无关的物理意图共享离散潜空间。我们在两大范式验证UniT：1）策略学习（VLA-UniT）：通过预测统一表征，有效利用多样化人类数据，在人形仿真基准和现实部署中实现最优数据效率与强健分布外泛化，尤以零样本任务迁移为著；2）世界建模（WM-UniT）：通过统一表征作为条件对齐跨具身动力学，实现直接的人机动作迁移。这种对齐确保人类数据可无缝转化为增强的人形视频生成动作可控性。最终，通过诱导高度对齐的跨具身表征（t-SNE可视化实证显示人类与人形特征收敛至共享流形），UniT为将海量人类知识蒸馏为通用人形能力提供了可扩展路径。

---

### 2. Mask World Model: Predicting What Matters for Robust Robot Policy Learning

- **作者**: Yunfan Lou, Xiaowei Chi, Xiaojie Zhang, Zezhong Qian, Chengxuan Li, Rongyu Zhang, Yaoxu Lyu, Guoyu Song, Chuyao Fu, Haoxuan Xu, Pengwei Wang, Shanghang Zhang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.19683v1)
- **发表日期**: 2026-04-21
- **匹配关键词**: diffusion-based policy
- **arXiv**: [2604.19683v1](http://arxiv.org/abs/2604.19683v1)
- **📥 PDF**: 已下载至本地 (`2604.19683v1_Mask_World_Model_Predicting_What_Matters_for_Robust_Robot_Policy_Learning.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 源自大规模视频生成预训练的世界模型已成为通用机器人策略学习的一种有前景范式。然而，标准方法通常专注于高保真RGB视频预测，这可能导致对无关因素的过度拟合，例如动态背景和光照变化。这些干扰因素降低了模型的泛化能力，最终导致控制策略不可靠且脆弱。为解决这一问题，我们提出了掩码世界模型（MWM），该模型利用视频扩散架构来预测语义掩码而非像素的演变。这一转变施加了几何信息瓶颈，迫使模型在过滤视觉噪声的同时捕捉基本的物理动态和接触关系。我们将这一掩码动态主干与基于扩散的策略头无缝集成，以实现稳健的端到端控制。大量评估表明，MWM在LIBERO和RLBench仿真基准测试中表现优异，显著超越了当前最先进的基于RGB的世界模型。此外，真实世界实验和稳健性评估（通过随机令牌剪枝）显示，MWM展现出卓越的泛化能力以及对纹理信息损失的强大恢复力。

---

### 3. Assessing VLM-Driven Semantic-Affordance Inference for Non-Humanoid Robot Morphologies

- **作者**: Jess Jones, Raul Santos-Rodriguez, Sabine Hauert
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.19509v1)
- **发表日期**: 2026-04-21
- **匹配关键词**: affordance, tool use, object manipulation
- **arXiv**: [2604.19509v1](http://arxiv.org/abs/2604.19509v1)
- **📥 PDF**: 已下载至本地 (`2604.19509v1_Assessing_VLM-Driven_Semantic-Affordance_Inference_for_Non-Humanoid_Robot_Morphologies.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉语言模型在理解人-物交互方面展现出卓越能力，但其在非人形机器人系统中的应用仍鲜有探索。本研究旨在探究视觉语言模型能否有效推断与人类形态迥异的机器人的可供性，以填补这些模型在多样化机器人应用部署中的关键空白。我们构建了一个新型混合数据集，该数据集结合了标注的真实世界机器人可供性-物体关系与视觉语言模型生成的合成场景，并对视觉语言模型在多种物体类别和机器人形态下的表现进行了实证分析，揭示了其在可供性推断能力上的显著差异。实验表明，虽然视觉语言模型在非人形机器人形态上展现出良好的泛化能力，但其在不同物体领域的表现存在明显的不一致性。值得注意的是，我们发现所有形态和物体类别中都存在低误报率但高漏报率的一致模式，这表明视觉语言模型倾向于做出保守的可供性预测。分析显示，这种模式在新颖工具使用场景和非传统物体操作中尤为明显，表明要将视觉语言模型有效整合到机器人系统中，需要采用互补性方法以缓解过度保守的行为，同时保持低误报率带来的固有安全优势。

---

### 4. Multimodal embodiment-aware navigation transformer

- **作者**: Louis Dezons, Quentin Picard, Rémi Marsal, François Goulette, David Filliat
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.19267v1)
- **发表日期**: 2026-04-21
- **匹配关键词**: navigation
- **arXiv**: [2604.19267v1](http://arxiv.org/abs/2604.19267v1)
- **📥 PDF**: 已下载至本地 (`2604.19267v1_Multimodal_embodiment-aware_navigation_transformer.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 基于监督学习训练的地面机器人目标导向导航模型展现出良好的零样本迁移能力，但其避障性能在分布偏移（如环境、机器人或传感器配置变化）下仍会下降。我们提出ViLiNT——一种基于注意力机制的多模态目标导航策略，该模型通过融合多平台、多环境的异构数据进行训练，并凭借两大核心特性提升鲁棒性。首先，我们采用Transformer架构融合RGB图像、三维激光雷达点云、目标嵌入向量及机器人本体描述符，以捕捉互补的几何与外观特征。Transformer的输出用于调节扩散模型生成可导航轨迹。其次，利用自动生成的离线标签，我们训练了路径通过性预测模块，用于对扩散模型生成的轨迹进行评分与排序。扩散条件调节与轨迹排序模块均依赖机器人本体标识符，使模型能根据机器人实际尺寸生成并筛选轨迹。在三个仿真环境中，ViLiNT的平均成功率较同等水平的纯视觉基线模型（NoMaD）提升166%。该性能提升在真实场景的障碍场地导航实验中得到了验证。这些结果表明，多模态融合与碰撞预测机制的结合显著增强了越野导航的鲁棒性。

---

### 5. BALTIC: A Benchmark and Cross-Domain Strategy for 3D Reconstruction Across Air and Underwater Domains Under Varying Illumination

- **作者**: Michele Grimaldi, David Nakath, Oscar Pizarro, Jonatan Scharff Willners, Ignacio Carlucho, Yvan R. Petillot
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.19133v1)
- **发表日期**: 2026-04-21
- **匹配关键词**: gaussian splatting, 3d reconstruction, neural radiance field, 3D reconstruction, 3D gaussian splatting
- **arXiv**: [2604.19133v1](http://arxiv.org/abs/2604.19133v1)
- **📥 PDF**: 已下载至本地 (`2604.19133v1_BALTIC_A_Benchmark_and_Cross-Domain_Strategy_for_3D_Reconstruction_Across_Air_and_Underwater_Domains.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 在不同环境条件下实现鲁棒的三维重建仍然是机器人感知领域的关键挑战，尤其在空气与水介质转换的场景中。为此，我们提出了BALTIC——一个旨在系统评估现代三维重建方法在介质与光照变化下性能的受控基准测试平台。该基准包含13个数据集，涵盖两种介质（空气与水）和三种光照条件（环境光、人工光及混合光），并通过运动类型、扫描模式和初始化轨迹的附加变化，形成多样化的序列组合。实验装置采用配备单目相机和HTC Vive追踪器的定制水箱，可实现高精度的真实位姿估计。我们进一步通过将水下图像序列与少量在相似光照条件下拍摄的空中视图相结合，探索跨域重建的可能性。使用COLMAP从轨迹精度和场景几何两个维度评估运动恢复结构重建效果，并将这些重建结果作为神经辐射场与三维高斯泼溅方法的输入。通过对比真实轨迹与空中参考数据评估生成模型，同时采用感知指标和光度指标比较渲染输出。此外，我们进行了色彩恢复分析以评估跨域辐射一致性。实验结果表明：在受控且纹理一致的条件下，经过简单预处理（如白平衡校正）的高斯泼溅方法能达到与专业水下方法相当的性能，但其在更复杂、异质的真实环境中的鲁棒性会有所下降。

---

### 6. A Comparative Evaluation of Geometric Accuracy in NeRF and Gaussian Splatting

- **作者**: Mikolaj Zielinski, Eryk Vykysaly, Bartlomiej Biesiada, Jan Baturo, Mateusz Capala, Dominik Belter
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.18205v1)
- **发表日期**: 2026-04-20
- **匹配关键词**: object manipulation, neural rendering, gaussian splatting, nerf
- **arXiv**: [2604.18205v1](http://arxiv.org/abs/2604.18205v1)
- **📥 PDF**: 已下载至本地 (`2604.18205v1_A_Comparative_Evaluation_of_Geometric_Accuracy_in_NeRF_and_Gaussian_Splatting.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 神经渲染技术的最新进展催生了多种三维场景表示方法。尽管标准计算机视觉指标能够评估生成图像的视觉质量，但它们常常忽略表面几何结构的保真度。这一局限在机器人学领域尤为关键，因为精确的几何结构对于抓取和物体操控等任务至关重要。本文提出了一套专注于几何精度的神经渲染方法评估流程，并构建了包含19个多样化场景的基准测试集。我们的方法能够从表面和形状保真度两个维度系统评估重建方法，从而对传统视觉评估指标形成有效补充。

---

### 7. Unmasking the Illusion of Embodied Reasoning in Vision-Language-Action Models

- **作者**: Haiweng Xu, Sipeng Zheng, Hao Luo, Wanpeng Zhang, Ziheng Xi, Zongqing Lu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.18000v1)
- **发表日期**: 2026-04-20
- **匹配关键词**: VLA, vision-language-action model, vision-language-action
- **arXiv**: [2604.18000v1](http://arxiv.org/abs/2604.18000v1)
- **📥 PDF**: 已下载至本地 (`2604.18000v1_Unmasking_the_Illusion_of_Embodied_Reasoning_in_Vision-Language-Action_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 近期视觉-语言-动作模型在标准机器人测试中取得了令人瞩目的成功率，这增强了对通用物理智能实现的乐观预期。然而最新研究表明，标准测试的成功与真实具身推理能力之间存在系统性错位，引发了对高分是否反映真实认知能力的质疑。为填补这一研究空白，我们提出BeTTER基准测试——一个用于检验机器人策略中真实具身推理能力的诊断性评估框架。该框架通过实施针对性因果干预（如空间布局变换、时序外推）并强制运动学隔离，明确解耦高层推理失败与底层执行限制。系统性评估显示，当前最先进的视觉-语言-动作模型在动态场景中会出现灾难性失效，表现为严重的词汇-运动捷径依赖、行为惯性及语义特征坍缩。机制分析表明，这些症状源于根本性的架构瓶颈——如容量压缩与短视降采样——这些瓶颈系统性地削弱了模型的基础语义表征能力。我们论证了高度静态的评估协议通过允许模型过度拟合感觉运动先验，实际上掩盖了这种表征退化。通过真实机器人实验验证，我们的研究证实这种表征崩溃并非仿真伪影，强调未来视觉-语言-动作范式必须解决高频控制与高层推理之间的结构性矛盾。

---

### 8. Can Explicit Physical Feasibility Benefit VLA Learning? An Empirical Study

- **作者**: Yubai Wei, Chen Wu, Hashem Haghbayan
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.17896v1)
- **发表日期**: 2026-04-20
- **匹配关键词**: VLA, obstacle avoidance, vision-language-action
- **arXiv**: [2604.17896v1](http://arxiv.org/abs/2604.17896v1)
- **📥 PDF**: 已下载至本地 (`2604.17896v1_Can_Explicit_Physical_Feasibility_Benefit_VLA_Learning?_An_Empirical_Study.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作模型将多模态输入直接映射为机器人动作，通常通过大规模模仿学习进行训练。尽管该范式展现出强大性能，但当前主流的VLA训练流程并未显式监督硬性物理约束（如避障或运动学可行性）。因此，物理可行行为背后的几何结构只能从演示数据中隐式推断。本文研究引入显式可行性监督能否为VLA策略提供有效的结构化引导。我们构建了一个基于几何的简易可行性目标，并将其整合到基于扩散的VLA策略训练阶段。为系统验证该思路，我们以障碍物感知操作为切入点，探究几何依赖的物理可行性。实验结果表明：在VLA训练中引入可行性监督能同时提升物理可靠性与整体任务性能，并在低数据场景下增强学习效率。这些发现表明，显式可行性信号能有效补充基于模仿的VLA学习，为开发更可靠的VLA策略提供了新思路。

---

### 9. StableIDM: Stabilizing Inverse Dynamics Model against Manipulator Truncation via Spatio-Temporal Refinement

- **作者**: Kerui Li, Zhe Jing, Xiaofeng Wang, Zheng Zhu, Yukun Zhou, Guan Huang, Dongze Li, Qingkai Yang, Huaibo Huang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.17887v1)
- **发表日期**: 2026-04-20
- **匹配关键词**: VLA
- **arXiv**: [2604.17887v1](http://arxiv.org/abs/2604.17887v1)
- **📥 PDF**: 已下载至本地 (`2604.17887v1_StableIDM_Stabilizing_Inverse_Dynamics_Model_against_Manipulator_Truncation_via_Spatio-Temporal_Refi.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 逆动力学模型（IDMs）将视觉观测映射为底层动作指令，是具身人工智能中数据标注与策略执行的核心组件。然而在机械臂截断这种常见故障模式下，其性能会严重下降——该场景使状态恢复问题不适定并导致控制失稳。我们提出StableIDM，一种时空框架，通过优化视觉输入特征来提升部分可观测条件下的动作预测稳定性。该框架融合了三个互补模块：（1）辅助性机器人中心掩码机制以抑制背景干扰；（2）方向性特征聚合模块实现几何感知的空间推理，沿可见机械臂推断方向提取各向异性特征；（3）时序动态优化模块通过运动连续性平滑修正预测。大量实验验证了本方法的有效性：在AgiBot基准测试中，StableIDM在严重截断情况下将严格动作准确率提升12.1%；在真实机器人回放任务中平均成功率提高9.7%。此外，当解码视频生成规划时，端到端抓取成功率提升11.5%；作为自动标注器使用时，下游视觉语言动作模型的真实机器人任务成功率提升17.6%。这些结果表明，StableIDM为具身人工智能的策略执行与数据生成提供了鲁棒且可扩展的基础架构。

---

### 10. ST-$π$: Structured SpatioTemporal VLA for Robotic Manipulation

- **作者**: Chuanhao Ma, Hanyu Zhou, Shihan Peng, Yan Li, Tao Gu, Luxin Yan
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.17880v1)
- **发表日期**: 2026-04-20
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2604.17880v1](http://arxiv.org/abs/2604.17880v1)
- **📥 PDF**: 已下载至本地 (`2604.17880v1_ST-$π$_Structured_SpatioTemporal_VLA_for_Robotic_Manipulation.pdf`)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/chuanhaoma/ST-pi.
- **中文摘要**: 视觉-语言-动作（VLA）模型在通用机器人任务上已取得显著成功，但在细粒度时空操作方面仍面临挑战。现有方法通常将时空知识嵌入视觉与动作表征中，并直接通过跨模态映射进行步级动作预测。然而，这种时空推理过程大多隐式进行，难以处理具有明确时空边界的多段连续行为。为此，我们提出ST-$π$——一种面向机器人操作的结构化时空VLA模型。该模型基于两项核心设计：1）时空视觉语言模型。我们将四维观测数据与任务指令编码至潜在空间，并输入大语言模型以生成由子任务、空间定位与时间定位构成的因果有序块级动作提示序列。2）时空动作专家模块。在块级动作提示的引导下，我们设计了结构化双生成器指导机制，联合建模空间依赖性与时间因果性，从而预测步级动作参数。在此结构化框架中，视觉语言模型显式规划全局时空行为，动作专家模块则进一步细化局部时空控制。此外，我们构建了带有结构化时空标注的真实世界机器人数据集用于微调。大量实验验证了模型的有效性。代码链接：https://github.com/chuanhaoma/ST-pi。

---

### 11. OFlow: Injecting Object-Aware Temporal Flow Matching for Robust Robotic Manipulation

- **作者**: Kuanning Wang, Ke Fan, Chenhao Qiu, Zeyu Shangguan, Yuqian Fu, Yanwei Fu, Daniel Seita, Xiangyang Xue
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.17876v1)
- **发表日期**: 2026-04-20
- **匹配关键词**: VLA
- **arXiv**: [2604.17876v1](http://arxiv.org/abs/2604.17876v1)
- **📥 PDF**: 已下载至本地 (`2604.17876v1_OFlow_Injecting_Object-Aware_Temporal_Flow_Matching_for_Robust_Robotic_Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 稳健的机器人操作不仅需要预测场景随时间的变化，还需在复杂场景中识别任务相关对象。然而，现有视觉语言动作模型面临两大局限：通常仅基于当前帧执行动作，而未来预测与对象感知推理往往在不同潜在空间中分别学习。我们提出OFlow框架——将对象感知时序流匹配注入视觉语言动作模型，通过在共享语义潜在空间中统一时序预见与对象感知推理，同时解决这两项局限。该方法使用时序流匹配预测未来潜在状态，将其分解为强调物理相关线索、过滤任务无关变化的对象感知表征，并基于这些预测生成连续动作。通过将OFlow集成至视觉语言动作模型流程，我们的方法能在分布偏移下实现更可靠的控制。在LIBERO、LIBERO-Plus、MetaWorld和SimplerEnv基准测试及现实任务中的大量实验表明，对象感知预见能力持续提升系统鲁棒性与任务成功率。

---

### 12. AnyRecon: Arbitrary-View 3D Reconstruction with Video Diffusion Model

- **作者**: Yutian Chen, Shi Guo, Renbiao Jin, Tianshuo Yang, Xin Cai, Yawen Luo, Mingxin Yang, Mulin Yu, Linning Xu, Tianfan Xue
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.19747v1)
- **发表日期**: 2026-04-21
- **匹配关键词**: 3d reconstruction, 3D reconstruction
- **arXiv**: [2604.19747v1](http://arxiv.org/abs/2604.19747v1)
- **📥 PDF**: 已下载至本地 (`2604.19747v1_AnyRecon_Arbitrary-View_3D_Reconstruction_with_Video_Diffusion_Model.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 稀疏视角三维重建对于从随意拍摄中建模场景至关重要，但在非生成式重建领域仍面临挑战。现有基于扩散模型的方法通过合成新视角缓解了这一问题，但这些方法通常仅基于一至两帧捕获画面进行条件生成，这限制了几何一致性，并难以扩展至大规模或多样化场景。我们提出AnyRecon框架，该框架能够从任意无序稀疏输入中实现可扩展的重建，在保持显式几何控制的同时支持灵活的条件基数。为实现长程条件生成，我们的方法通过预置捕获视角缓存构建持久化全局场景记忆，并消除时间压缩以维持大视角变化下的帧级对应关系。除改进生成模型外，我们还发现生成与重建的相互作用对大规模三维场景至关重要。因此，我们引入几何感知条件策略，通过显式三维几何记忆与几何驱动的捕获视角检索，实现生成与重建的耦合。为提升效率，我们结合四步扩散蒸馏与上下文窗口稀疏注意力机制，将二次复杂度降至线性。大量实验证明，该方法能在不规则输入、大视角差异及长轨迹场景下实现鲁棒且可扩展的重建。

---

### 13. TransSplat: Unbalanced Semantic Transport for Language-Driven 3DGS Editing

- **作者**: Yanhui Chen, Jiahong Li, Jingchao Wang, Junyi Lin, Zixin Zeng, Yang Shi
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.19571v1)
- **发表日期**: 2026-04-21
- **匹配关键词**: gaussian splatting, 3D gaussian splatting
- **arXiv**: [2604.19571v1](http://arxiv.org/abs/2604.19571v1)
- **📥 PDF**: 已下载至本地 (`2604.19571v1_TransSplat_Unbalanced_Semantic_Transport_for_Language-Driven_3DGS_Editing.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 语言驱动的3D高斯溅射（3DGS）编辑为VR/AR中复杂场景的修改提供了更便捷的途径。标准流程通常采用两阶段策略：先编辑多个2D视图，再优化3D表示以匹配这些编辑后的观测结果。现有方法主要通过多视图特征融合、注意力过滤或迭代重校准来提升视图一致性，但未能显式解决一个更根本的问题：编辑后的2D证据与3D高斯之间的语义对应关系。为解决这一问题，我们提出TransSplat方法，将语言驱动的3DGS编辑建模为多视图非平衡语义传输问题。具体而言，该方法建立可见高斯与视图特定编辑原型之间的对应关系，从而显式刻画编辑后2D证据与3D高斯的语义关联，并进一步恢复跨视图共享的规范3D编辑场以指导统一的3D外观更新。此外，我们利用传输残差抑制非目标区域的错误编辑，有效缓解编辑泄漏问题并提升局部控制精度。定性与定量实验表明，相较于现有以增强视图一致性为核心的3D编辑方法，TransSplat在局部编辑精度与结构一致性方面均取得更优表现。

---

### 14. Paparazzo: Active Mapping of Moving 3D Objects

- **作者**: Davide Allegro, Shiyao Li, Stefano Ghidoni, Vincent Lepetit
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.19556v1)
- **发表日期**: 2026-04-21
- **匹配关键词**: 3d reconstruction, 3D reconstruction
- **arXiv**: [2604.19556v1](http://arxiv.org/abs/2604.19556v1)
- **📥 PDF**: 已下载至本地 (`2604.19556v1_Paparazzo_Active_Mapping_of_Moving_3D_Objects.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://davidea97.github.io/paparazzo-page/
- **中文摘要**: 当前的三维建图流程通常假设环境是静态的，这限制了其准确捕捉和重建运动物体的能力。为解决这一局限，我们提出了主动运动物体建图这一新任务，要求建图智能体在规划自身轨迹的同时补偿目标的运动。我们提出的Paparazzo方法提供了一种无需学习的解决方案，能够稳健预测目标运动轨迹，识别最具信息量的观测视角，并据此规划自身路径。我们还为此新任务构建了一个综合性基准测试集。通过大量实验证明，与多个强基线方法相比，Paparazzo能显著提升三维重建的完整度与精度，标志着动态场景理解领域迈出了重要一步。项目页面：https://davidea97.github.io/paparazzo-page/

---

### 15. LiveVLN: Breaking the Stop-and-Go Loop in Vision-Language Navigation

- **作者**: Xiangchen Wang, Weiye Zhu, Teng Wang, TianTian Geng, Zekai Zhang, Zhiyuan Qi, Jinyu Yang, Feng Zheng
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.19536v1)
- **发表日期**: 2026-04-21
- **匹配关键词**: navigation, VLN
- **arXiv**: [2604.19536v1](http://arxiv.org/abs/2604.19536v1)
- **📥 PDF**: 已下载至本地 (`2604.19536v1_LiveVLN_Breaking_the_Stop-and-Go_Loop_in_Vision-Language_Navigation.pdf`)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/NIneeeeeem/LiveVLN.
- **中文摘要**: 当前导航系统虽在基准测试中表现优异，但在实际部署中仍常出现明显的启停卡顿现象。这一瓶颈源于感知-推理-执行的循环流程仍存在阻塞：每次获取新观测后，控制器必须等待感知、传输与推理过程完成才能继续运动。因此仅降低动作生成成本无法消除冗余等待。为解决该问题，我们提出LiveVLN——一种无需重新训练即可实现更连续具身导航的框架，通过为预训练的视觉语言模型导航器增加多步动作延续能力。该框架无需为每次完整的感知推理循环暂停，而是将执行过程与新到观测的处理相重叠，使得在现有可执行动作序列耗尽前即可传递更新后的未来动作。这种设计确保运动过程中持续获得可用动作，减少空闲等待时间，实现更流畅的在线执行。该框架在运行时操作，可与兼容的预训练视觉语言模型导航器集成。在R2R与RxR数据集上的实验表明，LiveVLN在保持基准性能的同时，显著减少了等待时间并提升了动作可用性。在实际部署中，该框架将平均任务等待时间降低达77.7%，在StreamVLN和NaVIDA平台上分别缩短任务总耗时12.6%和19.6%，实现了更连贯的部署执行效果。代码已开源：https://github.com/NIneeeeeem/LiveVLN。

---

### 16. An Object-Centered Data Acquisition Method for 3D Gaussian Splatting using Mobile Phones

- **作者**: Yuezhe Zhang, Luqian Bai, Mengting Yu, Lei Wei, Shuai Wan, Yifan Zhang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.19216v1)
- **发表日期**: 2026-04-21
- **匹配关键词**: gaussian splatting, 3D gaussian splatting
- **arXiv**: [2604.19216v1](http://arxiv.org/abs/2604.19216v1)
- **📥 PDF**: 已下载至本地 (`2604.19216v1_An_Object-Centered_Data_Acquisition_Method_for_3D_Gaussian_Splatting_using_Mobile_Phones.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 通过移动设备进行数据采集对3D高斯溅射技术而言仍具挑战性。本研究聚焦于以物体为中心的采集场景，通过提供设备端捕获引导并记录机载传感器信号以供离线重建，实现了可靠的移动端采集。在校准步骤完成后，设备方向将与基准坐标系对齐以获取相对位姿，同时将相机光轴映射至以物体为中心的球面网格，实现统一视点索引。为抑制极区采样偏差，我们实时计算面积加权的球面覆盖度，并据此引导用户移动轨迹。通过对比实验，本方法在自由采集策略与RealityScan应用上展现出显著优势：使用更少输入图像即可获得更优的重建质量。进一步分析表明，所提方法能够在以物体为中心的采集过程中实现更全面、更均匀的视点覆盖。

---

### 17. SketchFaceGS: Real-Time Sketch-Driven Face Editing and Generation with Gaussian Splatting

- **作者**: Bo Li, Jiahao Kang, Yubo Ma, Feng-Lin Liu, Bin Liu, Fang-Lue Zhang, Lin Gao
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.19202v1)
- **发表日期**: 2026-04-21
- **匹配关键词**: gaussian splatting
- **arXiv**: [2604.19202v1](http://arxiv.org/abs/2604.19202v1)
- **📥 PDF**: 已下载至本地 (`2604.19202v1_SketchFaceGS_Real-Time_Sketch-Driven_Face_Editing_and_Generation_with_Gaussian_Splatting.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 三维高斯表示已成为数字头部建模的强大范式，能够实现实时渲染的光照级真实感效果。然而，三维高斯头部模型的直观交互式创建与编辑仍面临挑战。虽然二维草图为实现快速直观的概念设计提供了理想的交互方式，但其具有稀疏性、深度模糊性且缺乏高频外观线索，使得从笔触推断稠密且几何一致的三维高斯结构变得困难——尤其在实时性约束下。为应对这些挑战，我们提出SketchFaceGS，这是首个基于草图驱动的实时生成与编辑光照级真实感三维高斯头部模型的框架。该方法采用前馈式由粗到精的架构：基于Transformer的UV特征预测模块首先从输入草图重建出粗糙但几何一致的UV特征图，随后三维UV特征增强模块通过高频光照级细节对其进行优化，最终生成高保真三维头部模型。针对编辑任务，我们提出结合分层特征融合策略的UV掩码融合技术，实现精确、实时、自由视角的模型修改。大量实验表明，SketchFaceGS在生成保真度与编辑灵活性方面均优于现有方法，仅需单次前向传播即可从草图生成高质量、可编辑的三维头部模型。

---

### 18. SpanVLA: Efficient Action Bridging and Learning from Negative-Recovery Samples for Vision-Language-Action Model

- **作者**: Zewei Zhou, Ruining Yang, Xuewei, Qi, Yiluan Guo, Sherry X. Chen, Tao Feng, Kateryna Pistunova, Yishan Shen, Lili Su, Jiaqi Ma
- **单位**: Tony; Tony; Tony
- **发表日期**: 2026-04-21
- **匹配关键词**: VLA, vision-language-action model, vision-language-action
- **arXiv**: [2604.19710v1](http://arxiv.org/abs/2604.19710v1)
- **📥 PDF**: 已下载至本地 (`2604.19710v1_SpanVLA_Efficient_Action_Bridging_and_Learning_from_Negative-Recovery_Samples_for_Vision-Language-Ac.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型为利用世界知识和推理能力实现自动驾驶提供了一种前景广阔的范式，尤其在长尾场景中表现突出。然而，现有的VLA模型在使用自回归生成框架时，常面临动作生成延迟高的问题，且鲁棒性有限。本文提出SpanVLA，一种新颖的端到端自动驾驶框架，融合了自回归推理与流匹配动作专家模块。首先，SpanVLA引入了一种高效桥接机制，利用VLM的视觉与推理引导，通过基于历史轨迹初始化的流匹配策略高效规划未来轨迹，从而显著降低了推理时间。其次，为进一步提升SpanVLA模型的性能与鲁棒性，我们提出了一种基于GRPO的后训练方法，使VLA模型不仅能从正向驾驶样本中学习，还能学习如何规避典型负向行为并掌握恢复行为。我们还引入了mReasoning——一个专注于复杂、高推理需求场景及负向-恢复样本的新型真实世界驾驶推理数据集。在NAVSIM（v1和v2）上的大量实验证明了SpanVLA模型具有竞争力的性能。此外，跨多样场景的定性结果凸显了我们模型在规划性能与鲁棒性方面的优势。

---

### 19. FASTER: Value-Guided Sampling for Fast RL

- **作者**: Perry Dong, Alexander Swerdlow, Dorsa Sadigh, Chelsea Finn ⭐
  - **高亮作者**: Chelsea Finn
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.19730v1)
- **发表日期**: 2026-04-21
- **匹配关键词**: VLA
- **arXiv**: [2604.19730v1](http://arxiv.org/abs/2604.19730v1)
- **📥 PDF**: 已下载至本地 (`2604.19730v1_FASTER_Value-Guided_Sampling_for_Fast_RL.pdf`)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/alexanderswerdlow/faster
- **中文摘要**: 当前一些性能最强的强化学习算法可能因计算成本过高而难以广泛应用，这些算法通常采用测试时扩展方法，例如采样多个候选动作并选择最优方案。本研究提出FASTER方法，旨在通过追溯动作样本在去噪过程早期的性能增益，实现基于采样的扩散策略测试时扩展优势，同时避免高昂的计算开销。我们的核心思路是将多候选动作的去噪与择优过程建模为马尔可夫决策过程，其目标是在去噪完成前逐步筛选动作候选。基于该MDP框架，我们可以在去噪空间中学习策略与价值函数，用以预测去噪过程中动作候选的后续价值，并在最大化回报的同时进行筛选。该方法具有轻量化特性，可无缝集成至现有生成式强化学习算法中。在在线与批量在线强化学习的复杂长程操控任务中，FASTER持续提升基础策略性能，并在对比方法中取得最佳综合表现。应用于预训练的VLA模型时，FASTER在显著降低训练与推理计算需求的同时，实现了同等性能水平。代码已发布于https://github.com/alexanderswerdlow/faster。

---

### 20. VLA Foundry: A Unified Framework for Training Vision-Language-Action Models

- **作者**: Jean Mercat, Sedrick Keh, Kushal Arora, Isabella Huang, Paarth Shah, Haruki Nishimura, Shun Iwase, Katherine Liu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.19728v1)
- **发表日期**: 2026-04-21
- **匹配关键词**: VLA, vision-language-action model, vision-language-action
- **arXiv**: [2604.19728v1](http://arxiv.org/abs/2604.19728v1)
- **📥 PDF**: 已下载至本地 (`2604.19728v1_VLA_Foundry_A_Unified_Framework_for_Training_Vision-Language-Action_Models.pdf`)
- **🔓 开源**: MODEL, GITHUB, PROJECT_PAGE, HUGGINGFACE, CODE
  - 链接：https://github.com/TRI-ML/vla_foundry, https://huggingface.co/collections/TRI-ML/vla-foundry., https://tri-ml.github.io/vla_foundry.
- **中文摘要**: 我们推出VLA Foundry，这是一个开源框架，将LLM、VLM和VLA训练统一在单一代码库中。当前多数开源VLA项目专注于动作训练阶段，常需整合互不兼容的预训练流程。VLA Foundry则提供具备端到端控制能力的共享训练栈，覆盖从语言预训练到动作专家微调的全流程。该框架既支持从零开始训练，也兼容Hugging Face的预训练骨干模型。为展示框架实用性，我们训练并发布两类模型：第一类通过LLM→VLM→VLA全流程从零训练完成；第二类基于预训练的Qwen3-VL骨干构建。我们在开放数据开源模拟器LBM Eval上评估了两类模型的闭环策略性能，同时改进了模拟器与STEP分析工具的易用性以方便公众使用。在标准评估设定下，我们完全开源的从零训练模型性能与先前闭源工作持平，而采用Qwen3-VL骨干的模型则展现出强大的多任务桌面操作策略性能，显著超越基线水平。VLA Foundry代码库发布于https://github.com/TRI-ML/vla_foundry，所有多任务模型权重已在https://huggingface.co/collections/TRI-ML/vla-foundry开放获取，更多定性演示视频可通过项目网站https://tri-ml.github.io/vla_foundry查看。

---

