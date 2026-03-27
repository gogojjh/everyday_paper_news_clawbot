# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-03-27 08:05

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 5/20 篇提供

**🌟 Highlight**: 10 篇 | **📌 Poster**: 10 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. TAG: Target-Agnostic Guidance for Stable Object-Centric Inference in Vision-Language-Action Models

- **作者**: Jiaying Zhou, Zhihao Zhan, Ruifeng Zhai, Qinhan Lyu, Hao Liu, Keze Wang, Liang Lin, Guangrun Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.24584v1)
- **发表日期**: 2026-03-25
- **匹配关键词**: VLA, vision-language-action, vision-language-action model
- **arXiv**: [2603.24584v1](http://arxiv.org/abs/2603.24584v1)
- **📥 PDF**: 已下载至本地 (`2603.24584v1_TAG_Target-Agnostic_Guidance_for_Stable_Object-Centric_Inference_in_Vision-Language-Action_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）策略在将语言指令和视觉观察映射为机器人动作方面取得了显著进展，但在存在干扰物的杂乱场景中，其可靠性会下降。通过分析失败案例，我们发现许多错误并非源于不可行的运动，而是由实例级定位失败引起的：策略常常生成看似合理的抓取轨迹，但最终落点略微偏离目标，甚至错误地定位到其他物体实例上。为解决这一问题，我们提出了目标无关引导（TAG），一种简单的推理时引导机制，旨在明确减少VLA策略中由干扰物和外观引起的偏差。受无分类器引导（CFG）的启发，TAG通过对比原始观察和物体擦除观察下的策略预测，并将它们的差异作为残差引导信号，从而增强决策过程中物体证据的影响力。TAG无需修改策略架构，只需极少的训练和推理调整即可与现有VLA策略集成。我们在标准操作基准测试（包括LIBERO、LIBERO-Plus和VLABench）上评估了TAG，结果表明该机制能持续提升在杂乱环境下的鲁棒性，并减少接近失误和错误执行对象的情况。

---

### 2. EndoVGGT: GNN-Enhanced Depth Estimation for Surgical 3D Reconstruction

- **作者**: Falong Fan, Yi Xie, Arnis Lektauers, Bo Liu, Jerzy Rozenblit
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.24577v1)
- **发表日期**: 2026-03-25
- **匹配关键词**: nerf, 3d reconstruction, 3D reconstruction
- **arXiv**: [2603.24577v1](http://arxiv.org/abs/2603.24577v1)
- **📥 PDF**: 已下载至本地 (`2603.24577v1_EndoVGGT_GNN-Enhanced_Depth_Estimation_for_Surgical_3D_Reconstruction.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 可变形软组织的精确三维重建对于手术机器人感知至关重要。然而，低纹理表面、镜面高光和器械遮挡常导致几何连续性断裂，这对现有固定拓扑方法构成挑战。为此，我们提出以几何为中心的EndoVGGT框架，其配备的形变感知图注意力模块能够动态构建特征空间语义图，捕捉相干组织区域间的长程关联。该方法通过静态空间邻域，实现了结构信息在遮挡区域的鲁棒传递，从而增强全局一致性并改善非刚性形变恢复效果。在SCARED数据集上的大量实验表明，本方法显著提升了重建保真度，PSNR指标较现有最优方法提高24.6%，SSIM指标提升9.1%。值得注意的是，EndoVGGT在未见过的SCARED和EndoNeRF数据集上展现出强大的零样本跨域泛化能力，证实了形变感知图注意力模块能够学习领域无关的几何先验。这些结果凸显了动态特征空间建模在实现稳定手术三维重建中的有效性。

---

### 3. Design, Modelling and Characterisation of a Miniature Fibre-Reinforced Soft Bending Actuator for Endoluminal Interventions

- **作者**: Xiangyi Tan, Aoife McDonald-Bowyer, Danail Stoyanov, Agostino Stilli
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.24461v1)
- **发表日期**: 2026-03-25
- **匹配关键词**: VLA
- **arXiv**: [2603.24461v1](http://arxiv.org/abs/2603.24461v1)
- **📥 PDF**: 已下载至本地 (`2603.24461v1_Design,_Modelling_and_Characterisation_of_a_Miniature_Fibre-Reinforced_Soft_Bending_Actuator_for_End.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 微型软体气动执行器对于在高度受限的解剖路径内进行机器人介入至关重要。本研究提出了一种厘米级纤维增强软体执行器的设计与验证方案，该执行器可集成于自然腔道介入诊疗的腔内机器人平台。通过采用多阶段多硬度硅胶浇铸工艺，我们设计了嵌入凯夫拉纤维增强的单腔体结构，在保持密封完整性的同时实现最大弯曲曲率，并基于实验参数化的超弹性材料模型与嵌入式梁增强结构，通过高精度Abaqus有限元模型进行了验证。该半圆柱形执行器外径为18毫米，长度为37.5毫米。研究对比了单螺旋与双螺旋缠绕构型、纤维间距及纤维密度的影响，最终优化的100 SH构型在实验中实现202.9°弯曲角度，仿真中达297.6°，结构稳定性在100千帕压力下保持良好，且纤维增强有效约束了径向膨胀。工作空间评估证实其适用于目标设备集成环境，表明纤维增强策略可有效应用于厘米尺度执行器并保持其性能。

---

### 4. 3D-Mix for VLA: A Plug-and-Play Module for Integrating VGGT-based 3D Information into Vision-Language-Action Models

- **作者**: Bin Yu, Shijie Lian, Xiaopeng Lin, Zhaolong Shen, Yuliang Wei, Haishan Liu, Changti Wu, Hang Yuan, Bailing Wang, Cong Huang, Kai Chen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.24393v1)
- **发表日期**: 2026-03-25
- **匹配关键词**: VLA, vision-language-action, vision-language-action model
- **arXiv**: [2603.24393v1](http://arxiv.org/abs/2603.24393v1)
- **📥 PDF**: 已下载至本地 (`2603.24393v1_3D-Mix_for_VLA_A_Plug-and-Play_Module_for_Integrating_VGGT-based_3D_Information_into_Vision-Language.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型利用多模态大语言模型（MLLMs）实现机器人控制，但近期研究表明，由于主要基于二维数据进行训练，MLLMs的空间智能表现有限，导致在操作任务中三维感知能力不足。虽然现有方法通过引入VGGT等专用三维视觉模型来增强空间理解能力，但这些方法采用多样化的集成机制且缺乏系统性研究，使得最优融合策略尚不明确。我们通过系统性预研，在标准化基准上比较了九种VGGT集成方案，发现基于任务上下文自适应平衡二维语义特征与三维几何特征的语义门控融合机制，在评估的九种融合方案中取得了最优性能。我们提出即插即用模块3D-Mix，该模块可无缝集成至多种VLA架构（GR00T风格与$π$风格）中，无需修改现有MLLM或动作专家组件。在SIMPLER和LIBERO基准上对六个MLLM系列（九种模型变体，参数量2B-8B）的实验表明，3D-Mix能带来稳定的性能提升：在九种GR00T风格变体上，域外（OOD）SIMPLER基准平均提升达+7.0%，为增强VLA系统的空间智能提供了理论完备的解决方案。

---

### 5. SOMA: Strategic Orchestration and Memory-Augmented System for Vision-Language-Action Model Robustness via In-Context Adaptation

- **作者**: Zhuoran Li, Zhiyang Li, Kaijun Zhou, Jinyu Gu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.24060v1)
- **发表日期**: 2026-03-25
- **匹配关键词**: VLA, vision-language-action, vision-language-action model
- **arXiv**: [2603.24060v1](http://arxiv.org/abs/2603.24060v1)
- **📥 PDF**: 已下载至本地 (`2603.24060v1_SOMA_Strategic_Orchestration_and_Memory-Augmented_System_for_Vision-Language-Action_Model_Robustness.pdf`)
- **🔓 开源**: PROJECT_PAGE, CODE, GITHUB
  - 链接：https://github.com/LZY-1021/SOMA.
- **中文摘要**: 尽管视觉-语言-动作（VLA）模型作为通用机器人控制器展现出潜力，但其在分布外（OOD）任务中对感知噪声和环境变化的鲁棒性，因缺乏长期记忆、因果故障归因和动态干预能力而受到根本性限制。为解决这一问题，我们提出SOMA——一种战略编排与记忆增强系统，该系统通过上下文自适应升级冻结的VLA策略，无需参数微调即可实现鲁棒性能。具体而言，SOMA通过在线流程运行，包括对比式双记忆检索增强生成（RAG）、归因驱动的大语言模型（LLM）编排器以及可扩展的模型上下文协议（MCP）干预机制，同时离线记忆整合模块持续将执行轨迹提炼为可靠先验知识。在LIBERO-PRO基准和我们提出的LIBERO-SOMA基准上，对三种骨干模型（pi0、pi0.5和SmolVLA）的实验评估表明，SOMA实现了平均56.6%的绝对成功率提升，其中长时程任务链的绝对改进幅度高达89.1%。项目页面与源代码已发布于：https://github.com/LZY-1021/SOMA。

---

### 6. QuadFM: Foundational Text-Driven Quadruped Motion Dataset for Generation and Control

- **作者**: Li Gao, Fuzhi Yang, Jianhui Chen, Liu Liu, Yao Zheng, Yang Cai, Ziqiao Li
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.24021v1)
- **发表日期**: 2026-03-25
- **匹配关键词**: human-robot interaction
- **arXiv**: [2603.24021v1](http://arxiv.org/abs/2603.24021v1)
- **📥 PDF**: 已下载至本地 (`2603.24021v1_QuadFM_Foundational_Text-Driven_Quadruped_Motion_Dataset_for_Generation_and_Control.pdf`)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/GaoLii/QuadFM.
- **中文摘要**: 尽管四足机器人技术已取得显著进展，但在整合多样化运动、情感表达行为与丰富语言语义的基础运动资源方面仍存在关键缺口——这些要素对于实现敏捷直观的人机交互至关重要。现有四足运动数据集仅涵盖少数动作捕捉基础动作（如行走、小跑、坐下），缺乏具备丰富语言关联的多样化行为。为填补这一空白，我们推出四足基础运动数据集（QuadFM），这是首个面向文本到动作生成与通用运动控制的大规模超高保真数据集。QuadFM包含11,784个精选运动片段，涵盖移动、交互及情感表达行为（如跳舞、伸展、小便），每个片段均配备三层标注——细粒度动作标签、交互场景和自然语言指令，总计35,352条描述，以支持语言条件理解与指令执行。

我们进一步提出Gen2Control RL统一框架，通过联合训练通用运动控制器与文本到动作生成器，实现在边缘硬件上的高效端到端推理。在搭载NVIDIA Orin的四足机器人实体测试中，我们的系统实现了实时动作合成（延迟<500毫秒）。仿真与真实环境测试均显示，系统在保持稳健物理交互的同时能生成逼真多样的运动。该数据集将通过https://github.com/GaoLii/QuadFM开源发布。

---

### 7. SLAT-Phys: Fast Material Property Field Prediction from Structured 3D Latents

- **作者**: Rocktim Jyoti Das, Dinesh Manocha
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.23973v1)
- **发表日期**: 2026-03-25
- **匹配关键词**: 3d reconstruction, 3D reconstruction
- **arXiv**: [2603.23973v1](http://arxiv.org/abs/2603.23973v1)
- **📥 PDF**: 已下载至本地 (`2603.23973v1_SLAT-Phys_Fast_Material_Property_Field_Prediction_from_Structured_3D_Latents.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 准确估算三维资产的材质属性场对于基于物理的仿真、机器人技术及数字孪生生成至关重要。现有基于视觉的方法要么成本高昂且速度缓慢，要么依赖三维信息。我们提出SLAT-Phys——一种端到端方法，可直接从单张RGB图像预测三维资产的空间变化材质属性场，无需显式三维重建。该方法利用预训练三维资产生成模型中的空间结构化潜在特征（该模型编码了丰富的几何与语义先验），并通过训练轻量级神经解码器来估算杨氏模量、密度和泊松比。潜在表征中关于物体几何形状与外观的粗粒度体素布局及语义线索，实现了精确的材质估算。实验表明，相较于现有方法，本方法在预测连续材质参数方面具有可比精度，同时显著减少了计算时间。具体而言，SLAT-Phys在NVIDIA RTXA5000 GPU上处理单个对象仅需9.9秒，且无需重建与体素化预处理。这使处理速度较现有方法提升120倍，实现了从单张图像快速估算材质属性的突破。

---

### 8. A Multimodal Framework for Human-Multi-Agent Interaction

- **作者**: Shaid Hasan, Breenice Lee, Sujan Sarker, Tariq Iqbal
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.23271v1)
- **发表日期**: 2026-03-24
- **匹配关键词**: exploration, human-robot interaction
- **arXiv**: [2603.23271v1](http://arxiv.org/abs/2603.23271v1)
- **📥 PDF**: 已下载至本地 (`2603.23271v1_A_Multimodal_Framework_for_Human-Multi-Agent_Interaction.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 人机交互正日益向多机器人、社会性基础环境发展。现有系统难以将多模态感知、具身表达与协调决策整合到统一框架中，这限制了共享物理空间中自然且可扩展的交互。为此，我们提出一种人机多智能体交互的多模态框架，其中每个机器人作为自主认知体运行，具备整合的多模态感知能力，并依托具身基础进行大语言模型驱动的规划。在团队层面，集中式协调机制通过调控发言轮转与智能体参与度，避免语音重叠与行为冲突。该框架在两个仿人机器人上实现，通过融合语音、手势、视线与移动的交互策略，实现了连贯的多智能体交互。典型交互案例展示了跨智能体的协调多模态推理及基于具身基础的响应。未来工作将聚焦于更大规模的用户研究，并深入探索社会性基础的多智能体交互动态。

---

### 9. Efficient Hybrid SE(3)-Equivariant Visuomotor Flow Policy via Spherical Harmonics for Robot Manipulation

- **作者**: Qinglun Zhang, Shen Cheng, Tian Dan, Haoqiang Fan, Guanghui Liu, Shuaicheng Liu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.23227v1)
- **发表日期**: 2026-03-24
- **匹配关键词**: diffusion policy
- **arXiv**: [2603.23227v1](http://arxiv.org/abs/2603.23227v1)
- **📥 PDF**: 已下载至本地 (`2603.23227v1_Efficient_Hybrid_SE(3)-Equivariant_Visuomotor_Flow_Policy_via_Spherical_Harmonics_for_Robot_Manipula.pdf`)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/zql-kk/E3Flow.
- **中文摘要**: 现有等变方法虽能提升数据效率，但存在计算强度高、依赖单模态输入、与快速采样方法结合时不稳定等问题。本研究提出E3Flow框架，首次成功将高效修正流与稳定的多模态等变学习相统一，突破了等变扩散策略的关键局限。该框架基于球谐函数表示构建，确保严格的SO(3)等变性。我们创新性地引入不变特征增强模块，动态融合点云与图像混合视觉模态，将丰富的视觉线索注入球谐特征。通过在MimicGen数据集的8个操作任务上进行评估，并开展4项真实环境实验验证其物理有效性。仿真结果表明，E3Flow在平均成功率上较当前最优的球面扩散策略提升3.12%，同时实现7倍推理加速，为机器人策略学习在性能、效率与数据效率间建立了新型高效平衡。代码已开源：https://github.com/zql-kk/E3Flow。

---

### 10. Gaze-Regularized Vision-Language-Action Models for Robotic Manipulation

- **作者**: Anupam Pani, Yanchao Yang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.23202v1)
- **发表日期**: 2026-03-24
- **匹配关键词**: VLA, vision-language-action, vision-language-action model
- **arXiv**: [2603.23202v1](http://arxiv.org/abs/2603.23202v1)
- **📥 PDF**: 已下载至本地 (`2603.23202v1_Gaze-Regularized_Vision-Language-Action_Models_for_Robotic_Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 尽管视觉-语言-动作模型已取得进展，但机器人操作在精细任务上仍面临挑战，因为现有模型缺乏主动视觉注意力分配机制。人类注视行为天然编码了意图、规划与执行模式——这为引导机器人感知提供了强大的监督信号。我们提出一种注视正则化训练框架，在不改变模型结构或增加推理开销的前提下，使视觉-语言-动作模型的内部注意力与人类视觉模式对齐。该方法将时序聚合的注视热力图转化为区块级分布，通过KL散度对Transformer注意力进行正则化，从而建立面向任务相关特征的归纳偏置，同时保持部署效率。当集成到现有视觉-语言-动作架构时，我们的方法在多个操作基准测试中实现了4-12%的性能提升。注视正则化模型能以更少的训练步骤达到同等性能，并在光照变化和传感器噪声下保持鲁棒性。除性能指标外，学习到的注意力模式可生成反映人类策略的可视化结果，增强了机器人系统的可信度。此外，该框架无需眼动追踪设备，可直接应用于现有数据集。这些结果表明，人类感知先验能显著加速机器人学习，同时提升任务性能和系统可解释性。

---

## 📌 Poster

*其他相关研究*

---

### 1. A Sensorless, Inherently Compliant Anthropomorphic Musculoskeletal Hand Driven by Electrohydraulic Actuators

- **作者**: Misato Sonoda, Ronan Hinchet, Amirhossein Kazemipour, Yasunori Toshimitsu, Robert K. Katzschmann
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.24357v1)
- **发表日期**: 2026-03-25
- **匹配关键词**: grasp detection
- **arXiv**: [2603.24357v1](http://arxiv.org/abs/2603.24357v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 非结构化环境中的机器人操作需要末端执行器兼具高运动灵活性与物理顺应性。传统刚性手依赖复杂的外部传感器实现安全交互，而电液驱动器为此提供了前景广阔的替代方案。本文提出一种完全由远程Peano-HASEL驱动器驱动的新型肌肉骨骼机器人手架构，该架构专为安全操作优化，涵盖设计、控制与评估全流程。通过将驱动器前移至前臂，我们在保持纤细拟人化外形的同时，实现了抓取界面与电气危险的功能性隔离。针对软体驱动器固有的线性收缩率限制，我们集成1:2滑轮传动机构以机械放大肌腱位移。该系统优先考虑顺应交互而非高负载能力，利用驱动器固有的力限制特性提供高水平本征安全性。此外，HASEL驱动器的自感知特性进一步增强了物理安全性。仅通过监测工作电流，我们无需依赖外部力传感器或编码器即可实现实时抓取检测与闭环接触感知控制。实验结果验证了系统的灵活性与本征安全性，成功展示了多种抓取分类法的执行能力，以及对纸气球等高脆弱物体的无损抓取。这些发现标志着向简化、本质顺应的软体机器人操作迈出了重要一步。

---

### 2. Toward Generalist Neural Motion Planners for Robotic Manipulators: Challenges and Opportunities

- **作者**: Davood Soleymanzadeh, Ivan Lopez-Sanchez, Hao Su, Yunzhu Li, Xiao Liang, Minghui Zheng
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.24318v1)
- **发表日期**: 2026-03-25
- **匹配关键词**: motion planning
- **arXiv**: [2603.24318v1](http://arxiv.org/abs/2603.24318v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 当前先进的通用操作策略已使机器人操作器能够在非结构化的人类环境中部署。然而，这些框架在杂乱环境中表现不佳，主要因为它们依赖辅助模块进行低层运动规划与控制。由于机器人配置空间的高维性以及工作空间中障碍物的存在，运动规划仍然具有挑战性。神经运动规划器通过提供快速推理并有效处理运动规划问题固有的多模态特性，提升了运动规划效率。尽管具备这些优势，现有的神经运动规划器往往难以泛化至未见过的、分布外的规划场景。本文回顾并分析了当前最先进的神经运动规划器，既强调其优势也指出其局限。同时，本文还勾勒了建立能够应对特定领域挑战的通用神经运动规划器的发展路径。有关所评论文献的列表，请访问 https://davoodsz.github.io/planning-manip-survey.github.io/。

---

### 3. Accelerated Spline-Based Time-Optimal Motion Planning with Continuous Safety Guarantees for Non-Differentially Flat Systems

- **作者**: Dries Dirckx, Jan Swevers, Wilm Decré
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.24133v1)
- **发表日期**: 2026-03-25
- **匹配关键词**: motion planning
- **arXiv**: [2603.24133v1](http://arxiv.org/abs/2603.24133v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 为自主移动机器人生成时间最优且无碰撞的轨迹，需要在确保安全性与管理计算复杂度之间进行根本权衡。当前最先进的方法将基于样条的运动规划构建为单一最优控制问题，但由于引入分离超平面参数作为决策变量以实现连续避障，往往面临高昂的计算成本。本文提出一种创新方法，通过将分离超平面的确定与最优控制问题解耦来缓解这一瓶颈。该方法将分离定理视为可通过线性系统或二次规划求解的独立分类问题，从而将超平面参数从优化变量中移除，有效将非凸约束转化为线性约束。实验验证表明，在密集障碍物环境中，这种解耦方法相较于完全耦合方法可将轨迹计算时间减少近60%，同时保持严格的连续安全性保证。

---

### 4. Knowledge-Guided Manipulation Using Multi-Task Reinforcement Learning

- **作者**: Aditya Narendra, Mukhammadrizo Maribjonov, Dmitry Makarov, Dmitry Yudin, Aleksandr Panov
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.24083v1)
- **发表日期**: 2026-03-25
- **匹配关键词**: scene graph, affordance
- **arXiv**: [2603.24083v1](http://arxiv.org/abs/2603.24083v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 本文提出基于知识图谱的大规模多任务模型策略优化框架（KG-M3PO），该框架在部分可观测环境下通过统一感知、知识与策略来实现多任务机器人操作。该方法通过在线构建的三维场景图谱增强以自我为中心的视觉感知，将开放词汇检测结果映射为度量化的关系表征。动态关系机制在每一步更新空间关系、包含关系及可供性关系边，同时通过强化学习目标端到端训练图神经网络编码器，使关系特征直接受控于控制性能表现。多种观测模态（视觉、本体感知、语言及图谱信息）被编码至共享潜在空间，强化学习智能体在此空间驱动控制循环。策略在轻量级图谱查询、视觉输入与本体感知信息的共同条件下运行，形成紧凑且语义丰富的决策状态。

在包含遮挡、干扰物及布局变化的系列操作任务实验中，本方法相较于强基线模型展现出持续优势：基于知识条件的智能体实现了更高的成功率、更强的样本效率，以及对新物体和未见场景配置的更优泛化能力。这些结果印证了结构化、持续维护的世界知识可作为可扩展、可泛化操作任务的强归纳偏置：当知识模块参与强化学习计算图时，关系表征与控制目标形成对齐，从而在部分可观测条件下实现鲁棒的长期行为决策。

---

### 5. Learning What Can Be Picked: Active Reachability Estimation for Efficient Robotic Fruit Harvesting

- **作者**: Nur Afsa Syeda, Mohamed Elmahallawy, Luis Fernando de la Torre, John Miller
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.23679v1)
- **发表日期**: 2026-03-24
- **匹配关键词**: motion planning
- **arXiv**: [2603.23679v1](http://arxiv.org/abs/2603.23679v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: GITHUB
  - 链接：https://github.com/wsu-cyber-security-lab-ai/active-learning.
- **中文摘要**: 农业作为全球健康和经济可持续发展的基石，其高价值作物采收等劳动密集型任务正面临日益严重的劳动力短缺问题。机器人采收系统为此提供了前景广阔的解决方案，但在非结构化果园环境中的部署仍受限于低效的感知-执行流程。现有方法通常依赖复杂的逆运动学或运动规划来判断目标果实是否可达，导致不必要的计算负担与决策延迟。本研究提出一种融合RGB-D感知与主动学习的方法，将可达性判断直接转化为二元决策问题。通过主动学习策略选择性标注最具信息量的可达性样本，在保持高预测精度的同时显著降低标注成本。大量实验表明，该框架能以极少的标注样本实现精准的可达性预测，其准确率较随机采样提升约6-8%，并能高效适应不同果园配置。在评估的多种策略中，基于熵与边界采样的方法在低标注量场景下优于委员会查询和标准不确定性采样，而随着标注数据增加，所有策略均呈现相近性能。这些成果凸显了主动学习在农业机器人任务级感知中的有效性，为替代计算密集型运动学可达性分析提供了可扩展的解决方案。相关代码已发布于https://github.com/wsu-cyber-security-lab-ai/active-learning。

---

### 6. Bio-Inspired Event-Based Visual Servoing for Ground Robots

- **作者**: Maral Mordad, Kian Behzad, Debojyoti Biswas, Noah J. Cowan, Milad Siami
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.23672v1)
- **发表日期**: 2026-03-24
- **匹配关键词**: visual servoing
- **arXiv**: [2603.23672v1](http://arxiv.org/abs/2603.23672v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 生物感知系统具有内在的自适应特性，能够过滤恒定刺激并优先处理相对变化，这很可能提升了计算与代谢效率。受多种动物主动感知行为的启发，本文提出了一种面向地面机器人的新型事件驱动视觉伺服框架。通过采用动态视觉传感器，我们证明：对结构化对数强度变化模式产生的异步事件流施加固定空间核函数，所得净事件通量能够解析地分离出特定运动状态。我们为此事件率估计器建立了广义理论边界，并证明线性与二次空间分布可分别分离出机器人的速度及位置-速度乘积。基于这些特性，我们采用多模式刺激直接合成非线性状态反馈项，完全无需传统状态估计。为克服事件传感在平衡点不可避免的线性可观测性损失，我们提出了一种仿生主动感知极限环控制器。在1/10比例自主地面车辆上的实验验证证实了所提直接感知方法的有效性、极低延迟特性及计算效率。

---

### 7. SIMART: Decomposing Monolithic Meshes into Sim-ready Articulated Assets via MLLM

- **作者**: Chuanrui Zhang, Minghan Qin, Yuang Wang, Baifeng Xie, Hang Li, Ziwei Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.23386v1)
- **发表日期**: 2026-03-24
- **匹配关键词**: articulated object
- **arXiv**: [2603.23386v1](http://arxiv.org/abs/2603.23386v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 高质量可动三维资产对于具身人工智能与物理模拟至关重要，然而当前三维生成技术仍主要聚焦于静态网格模型，导致"模拟就绪"的交互式对象存在明显缺口。现有的大多数可动对象创建方法依赖多阶段流程，各解耦模块间的误差会逐级累积。相比之下，统一的多模态大语言模型为静态资产理解与模拟就绪资产生成提供了单阶段解决方案。但基于密集体素的三维标记化方法会产生冗长的三维标记序列和高昂的内存开销，限制了处理复杂可动对象的可扩展性。为此，我们提出SIMART框架——一个能同步执行部件级分解与运动学预测的统一多模态大语言模型。通过引入稀疏三维VQ-VAE编码器，SIMART将标记数量较密集体素标记减少70%，实现了高保真度的多部件装配。该框架在PartNet-Mobility数据集和开放域AIGC数据集上均达到最先进性能，并成功支持基于物理的机器人仿真应用。

---

### 8. Edge Radar Material Classification Under Geometry Shifts

- **作者**: Jannik Hohmann, Dong Wang, Andreas Nüchter
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.23342v1)
- **发表日期**: 2026-03-24
- **匹配关键词**: navigation
- **arXiv**: [2603.23342v1](http://arxiv.org/abs/2603.23342v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 材料感知能力能够提升机器人的导航与交互性能，尤其在相机与激光雷达性能受限的环境中。本研究提出了一种面向超低功耗边缘设备（TI IWRL6432）的轻量化毫米波雷达材料分类方案，该方案采用紧凑的距离-强度描述符结合多层感知机（MLP）实现实时推理。在标准训练几何条件下，分类器的宏观F1分数可达94.2%，但在实际几何条件变化（包括传感器高度改变与小角度倾斜）时，我们观察到性能显著下降。这些扰动会引发系统性强度缩放及角度依赖性雷达截面积（RCS）效应，导致特征分布偏移，使宏观F1分数降至约68.5%。我们系统分析了这些失效模式，并通过归一化处理、几何增强与运动感知特征等方向，提出了提升系统鲁棒性的实用路径。

---

### 9. Strain-Parameterized Coupled Dynamics and Dual-Camera Visual Servoing for Aerial Continuum Manipulators

- **作者**: Niloufar Amiri, Farrokh Janabi-Sharifi
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.23333v1)
- **发表日期**: 2026-03-24
- **匹配关键词**: visual servoing
- **arXiv**: [2603.23333v1](http://arxiv.org/abs/2603.23333v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 肌腱驱动空中连续体机械臂（TD-ACMs）融合了无人飞行器（UAVs）的高机动性与轻质连续体机器人（CRs）的柔顺特性。现有针对TD-ACMs的耦合动力学建模方法计算成本高昂，且未明确考虑空中平台欠驱动特性。为突破这些局限，本文提出了一种具有欠驱动基座的耦合TD-ACM广义动力学建模方法。该方法将应变参数化的Cosserat杆模型与无人机刚体模型整合至$\mathrm{SE}(3)$上的统一拉格朗日常微分方程（ODE）框架中，从而避免了计算密集的符号推导。基于所建模型，本文进一步提出了一种鲁棒的双摄像头图像视觉伺服（IBVS）控制方案。该控制器有效缓解了传统IBVS的视场（FoV）限制，补偿了由无人机横向动力学引起的姿态相关图像运动，并通过集成底层自适应控制器处理建模不确定性，同时提供形式化的稳定性保证。在紧凑型定制原型机上开展的广泛仿真与实验验证表明，所提框架在实际场景中具有显著的有效性与鲁棒性。

---

### 10. AeroScene: Progressive Scene Synthesis for Aerial Robotics

- **作者**: Nghia Vu, Tuong Do, Dzung Tran, Binh X. Nguyen, Hoan Nguyen, Erman Tjiputra, Quang D. Tran, Hai-Nguyen Nguyen, Anh Nguyen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2603.23224v1)
- **发表日期**: 2026-03-24
- **匹配关键词**: navigation
- **arXiv**: [2603.23224v1](http://arxiv.org/abs/2603.23224v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: CODE
- **中文摘要**: 生成模型已在多个领域展现出显著影响力，但其在机器人领域的场景合成潜力仍未得到充分探索。这一空白在无人机仿真器中尤为明显，当前仿真环境仍高度依赖人工构建，不仅耗时且难以扩展。本研究提出AeroScene——一种用于渐进式三维场景合成的分层扩散模型。该方法通过层次感知标记化和多分支特征提取技术，实现对全局布局与局部细节的协同推理，确保生成场景的物理合理性与语义一致性。这使得AeroScene特别适用于为空中机器人任务（如导航、着陆与栖息）生成逼真场景。我们在新收集的数据集和公共基准测试中进行了广泛实验，证明AeroScene显著优于现有方法。此外，我们利用AeroScene生成了包含1000多个物理就绪、高保真三维场景的大规模数据集，这些场景可直接集成至NVIDIA Isaac Sim仿真平台。最后，我们通过下游无人机导航任务验证了生成环境的实用性。相关代码与数据集已在aioz-ai.github.io/AeroScene/开源。

---

