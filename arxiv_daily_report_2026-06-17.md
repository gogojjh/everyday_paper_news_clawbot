# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-06-17 08:02

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 2/20 篇提供

**🌟 Highlight**: 20 篇 | **📌 Poster**: 0 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. T-Rex: Tactile-Reactive Dexterous Manipulation

- **作者**: Dantong Niu, Zhuoyang Liu, Zekai Wang, Boning Shao, Zhao-Heng Yin, Anirudh Pai, Yuvan Sharma, Stefano Saravalle, Ruijie Zheng, Jing Wang, Ryan Punamiya, Mengda Xu, Yuqi Xie, Yunfan Jiang, Letian Fu, Konstantinos Kallidromitis, Matteo Gioia, Junyi Zhang, Jiaxin Ge, Haiwen Feng, Fabio Galasso, Wei Zhan, David M. Chan, Yutong Bai, Roei Herzig, Jiahui Lei, Fei-Fei Li, Ken Goldberg, Jitendra Malik, Pieter Abbeel, Yuke Zhu, Danfei Xu, Jim, Fan, Trevor Darrell ⭐
  - **高亮作者**: Yuke Zhu
- **单位**: Linxi; Linxi; Linxi...
- **发表日期**: 2026-06-15
- **匹配关键词**: VLA, vision-language-action, object manipulation
- **arXiv**: [2606.17055v1](http://arxiv.org/abs/2606.17055v1)
- **📥 PDF**: 已下载至本地 (`2606.17055v1_T-Rex_Tactile-Reactive_Dexterous_Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 对触觉信号做出动态响应的能力，长期以来一直被视为实现人类级灵巧操作的关键。然而，当前基于学习的机器人操作视觉-语言-动作（VLA）模型，要么完全忽略触觉模态，要么局限于使用静态线索的编码器——这在一定程度上是由于多样化训练数据和标准化评估的匮乏、现有VLA模型的架构限制，以及静态触觉编码器的局限性所致。本文通过解决上述所有限制，推动了触觉反应式操作的前沿发展。我们提出了一种大规模、100小时的触觉丰富数据集，该数据集通过一种新颖且数据高效的方法收集，优先关注基础运动基元。为了在不牺牲现有VLA模型能力的前提下有效利用天然高频触觉信号，我们引入了一种可变速率混合变换器（MoT）架构，并配备了一种新型时序触觉VQ-VAE编码器。我们在12项需要精细力控制与可变形物体操作的任务中，验证了触觉反应式策略的有效性，其平均成功率比最强基线高出30%以上。

---

### 2. Geometric Action Model for Robot Policy Learning

- **作者**: Jisang Han, Seonghu Jeon, Jaewoo Jung, René Zurbrügg, Honggyu An, Tifanny Portela, Marco Hutter, Marc Pollefeys, Seungryong Kim, Sunghwan Hong ⭐
  - **高亮作者**: Marc Pollefeys
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.17046v1)
- **发表日期**: 2026-06-15
- **匹配关键词**: VLA, vision-language-action, contact-rich manipulation, vision-language-action model
- **arXiv**: [2606.17046v1](http://arxiv.org/abs/2606.17046v1)
- **📥 PDF**: 已下载至本地 (`2606.17046v1_Geometric_Action_Model_for_Robot_Policy_Learning.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 通用型机器人策略必须遵循用户指令，同时推理物体、摄像头和机器人动作在三维物理世界中的交互方式。当前的视觉-语言-动作模型（VLA）和视频世界-动作模型（WAM）虽然继承了大规模基础模型强大的语义或时间先验知识，但它们仍主要基于二维图像帧或二维衍生潜空间运行，导致接触密集型操作所需的三维几何信息被隐式处理。为此，我们提出几何动作模型（GAM）——一种语言条件化的操作策略，该模型直接复用预训练的几何基础模型（GFM）作为感知、时间预测和动作解码的共享基础架构。GAM在GFM中间层进行分割：浅层网络作为观测编码器，在分割层插入的因果未来预测器基于语言、本体感知和动作历史预测未来潜特征。这些预测的未来特征随后通过剩余GFM模块进行特征传播与解码，使单一骨干网络能够同时生成未来几何结构与动作。这种设计通过最小化架构修改，赋予GFM语言条件化的时间世界建模能力，同时保留其丰富的几何先验知识。在涵盖仿真与真实机器人操作的广泛基准测试中，GAM相比当前基础模型规模的基线方法，展现出更高的精度、更强的鲁棒性、更快的速度以及更轻量的架构。

---

### 3. Hierarchical Advantage Weighting for Online RL Fine-Tuning of VLAs from Sparse Episode Outcomes

- **作者**: Tongyan Fang, Siyuan Huang, Naiyu Fang, Ganlong Zhao, Zhongjin Luo, Jianbo Liu, Xiaogang Wang, Ying Dong, Hongsheng Li
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.17043v1)
- **发表日期**: 2026-06-15
- **匹配关键词**: VLA
- **arXiv**: [2606.17043v1](http://arxiv.org/abs/2606.17043v1)
- **📥 PDF**: 已下载至本地 (`2606.17043v1_Hierarchical_Advantage_Weighting_for_Online_RL_Fine-Tuning_of_VLAs_from_Sparse_Episode_Outcomes.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 当预训练的视觉-语言-动作（VLA）策略通过在线强化学习进行微调时，每次交互回合仅产生一个二元结果（成功或失败），但策略更新需要逐时间步的监督信号。现有方法通常将这种稀疏结果简化为单个标量奖励或优势信号，这混淆了不同形式的逐时间步反馈，并且在基本任务成功可实现后提供的指导有限。首先，单个标量信号混淆了可行性和效率两个目标；一旦实现基本成功，二元标签无法提供区分高效完成与缓慢完成的梯度。其次，真实世界交互混合了自主执行和人工干预片段；简单地将回合结果跨越这些边界分配会导致错误的信用分配。为解决这些问题，我们提出分层优势加权行为克隆（HABC），该方法针对这两个目标在不同数据子集上训练独立的评论家网络，并通过状态自适应平衡组合其输出。状态自适应门控$g_t$融合它们的单步优势，在成功不确定时优先考虑可行性，仅在可行性高时转向效率，并将结果转换为策略损失中逐时间步的权重。干预感知的信用分配进一步将结果标签限制在当前策略执行的片段上，防止监督信号跨越干预边界泄露。在三个接触密集型双臂任务的真实机器人实验中，HABC将监督微调（SFT）基线从36%、44%和12%的成功率分别提升至92%、88%和38%。

---

### 4. R2RDreamer: 3D-aware Data Augmentation for Spatially-generalized 2D Manipulation Policies

- **作者**: Xiuwei Xu, Haowen Sun, Angyuan Ma, Yiwei Zhang, Zhenyu Wu, Xiaofeng Wang, Bingyao Yu, Zheng Zhu, Jie Zhou, Jiwen Lu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.17040v1)
- **发表日期**: 2026-06-15
- **匹配关键词**: vision-language-action
- **arXiv**: [2606.17040v1](http://arxiv.org/abs/2606.17040v1)
- **📥 PDF**: 已下载至本地 (`2606.17040v1_R2RDreamer_3D-aware_Data_Augmentation_for_Spatially-generalized_2D_Manipulation_Policies.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 空间泛化对于模仿学习的操作策略至关重要，但实现这一目标通常需要跨不同物体姿态、机器人配置和相机视角的大规模演示数据。从少量源演示中进行数据增强，为成本高昂的真实世界数据采集提供了一种实用替代方案。基于仿真的增强可以产生可控变化，但需要复杂的环境和物体设置，并可能引入仿真到现实的差距。近期实到实方法通过联合编辑真实演示的3D观测和动作轨迹避免了这些问题，但仍依赖强大的3D场景解析和几何补全，且通常生成针对3D点云策略而非基于RGB的2D策略的观测。我们提出R2RDreamer，一种实到实演示增强框架，在保持3D动作-观测编辑几何一致性的同时，将视觉补全迁移至2D视频空间。具体而言，R2RDreamer首先通过编辑共享3D帧中的不完整物体点云和末端执行器轨迹执行轻量级3D增强；随后将编辑后的场景通过遮挡感知推理投影至掩码图像空间控制视频，并利用密集控制图像到视频模型生成时间连贯的RGB观测。在空间偏移操作任务上，针对2D扩散策略和视觉-语言-动作策略的实验表明，R2RDreamer能从有限源演示中提升空间泛化能力，分析验证了3D编辑、遮挡感知投影和视频补全的贡献。

---

### 5. ROVE: Unlocking Human Interventions for Humanoid Manipulation via Reinforcement Learning

- **作者**: Wei Xiao, Weiliang Tang, Yuying Ge, Hui Zhou, Yao Mu, Li Zhang, Yixiao Ge
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.17011v1)
- **发表日期**: 2026-06-15
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2606.17011v1](http://arxiv.org/abs/2606.17011v1)
- **📥 PDF**: 已下载至本地 (`2606.17011v1_ROVE_Unlocking_Human_Interventions_for_Humanoid_Manipulation_via_Reinforcement_Learning.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 人类干预为视觉-语言-动作（VLA）模型的后训练提供了关键的修正信号。然而，由于复杂的全身运动学和灵巧手控制，实现无缝的人形干预是一项艰巨的系统挑战。因此，收集到的干预轨迹往往并非最优，依赖人类干预作为专家监督的方法可能会吸收犹豫、低效甚至错误的动作。为解决系统和算法两方面的挑战，我们提出ROVE——一种基于强化学习的人形VLA后训练框架，能够处理不完美的人类干预。首先，ROVE引入了一个人在环的流程，能够收集人形操作中的部署和干预数据。其次，它利用乐观价值估计（OVE）从混合质量的轨迹中优先选择高价值行为。为进一步增强价值估计的鲁棒性，我们融入跨形态的人类经验视频，为长尾失败和恢复模式提供丰富的监督信号。由此产生的评论家模型能够输出信息丰富的优势信号，引导VLA执行器聚焦于高价值行为，而非不加区分地模仿所有动作。在具有挑战性的真实世界接触密集且精细的人形操作任务中，ROVE优于基于经验学习的基线方法，并在多次部署-干预迭代中持续提升性能。

---

### 6. Binary Tracking for Spatial QA and Navigation with Open Vision-Language Models

- **作者**: Dongbin Na, Chanwoo Kim, Soonbin Rho, Giyun Choi, Gangbok Lee, Dooyoung Hong
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.16902v1)
- **发表日期**: 2026-06-15
- **匹配关键词**: exploration, navigation
- **arXiv**: [2606.16902v1](http://arxiv.org/abs/2606.16902v1)
- **📥 PDF**: 已下载至本地 (`2606.16902v1_Binary_Tracking_for_Spatial_QA_and_Navigation_with_Open_Vision-Language_Models.pdf`)
- **🔓 开源**: CODE, GITHUB
  - 链接：https://github.com/ndb796/BinaryTracking
- **中文摘要**: 本研究针对服务机器人在长距离自我中心路径中的空间问答问题。当收到诸如"回家路上哪里能找到干洗店？"的查询时，系统会返回下游导航组件可执行的度量坐标。现有空间问答方法通常利用基于GPT-4o等闭源模型的检索增强代理进行路径探索。然而，由于网络不稳定、通信延迟和部署成本等因素，现实环境中运行的机器人往往无法可靠依赖在线闭源模型。这催生了对基于开源的空间问答方法的需求——这类方法可在机器人本体上运行，但现有相关研究仍十分有限。本文提出BinTrack，一种简洁高效的全开源空间定位代理，利用机器人轨迹的时间顺序特性。该方法在查询中识别出的两个锚定地标之间，对轨迹片段执行二分搜索。相较于其他开源实现，其整体准确率提升高达22.8%，甚至在SpaceLocQA基准测试的全局类别中达到与GPT-4o等闭源模型报告结果相当的水平——该类别作为最具挑战性的设置，此前一直需要GPT-4o这类强推理代理。此外，其优化的推理策略相较先前方法持续实现超过1.5倍的推理加速。最后，本研究发布GangnamLoop——通过在实际公共街道部署真实四足机器人并采用匿名化策略采集的新型实用多行程户外基准数据集。该数据集在不同户外条件下重访相同地点，并将机器人的低视角与人类主人的视角进行配对。源代码与数据集已公开于https://github.com/ndb796/BinaryTracking。

---

### 7. SGM-SLAM: Scene Graph Matching for Data-Efficient Distributed SLAM

- **作者**: Yewei Huang, Tixiao Shan, Abhinav Rajvanshi, Niluthpol Chowdhury Mithun, Yaxuan Li, Brendan Englot, Han-Pang Chiu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.16881v1)
- **发表日期**: 2026-06-15
- **匹配关键词**: scene graph, localization and mapping
- **arXiv**: [2606.16881v1](http://arxiv.org/abs/2606.16881v1)
- **📥 PDF**: 已下载至本地 (`2606.16881v1_SGM-SLAM_Scene_Graph_Matching_for_Data-Efficient_Distributed_SLAM.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出了一种面向配备激光雷达、相机和惯性传感器的机器人团队的数据高效分布式同步定位与建图（SLAM）框架。该框架利用场景图匹配来识别机器人间的测量约束。与依赖特征级匹配的现有方法不同，我们的框架首次仅使用物体标签和质心进行场景图匹配。该方法通过融合RGB-激光雷达点云构建场景图，生成语义分割点云层和离散有界物体层，以辅助估计机器人轨迹。场景图匹配通过相邻机器人间交换和匹配物体数据协作完成。为最大化通信效率，我们采用多步数据交换与优化流程。通过仿真实验以及腿足机器人在室内外环境中采集的真实数据集，验证了该方法的有效性和高效性。

---

### 8. MVM-IOD: An Industrial Object-Centric Benchmark Dataset for the Evaluation of 3D Reconstruction Methods

- **作者**: Robert Langendörfer, Markus Hillemann, Markus Ulrich
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.16638v1)
- **发表日期**: 2026-06-15
- **匹配关键词**: 3D reconstruction, 3d reconstruction, gaussian splatting
- **arXiv**: [2606.16638v1](http://arxiv.org/abs/2606.16638v1)
- **📥 PDF**: 已下载至本地 (`2606.16638v1_MVM-IOD_An_Industrial_Object-Centric_Benchmark_Dataset_for_the_Evaluation_of_3D_Reconstruction_Metho.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 三维物体重建与相机位姿估计在工业应用中充满挑战，因为误差代价高昂且计算时间通常有限。典型工业物体的复杂性进一步增加了这些任务的难度。现有的大多数相关数据集并未描绘真实的工业场景。为此，我们提出了机器视觉测量工业物体数据集（MVM-IOD）。通过将安装在工业机器人臂末端执行器上的相机沿半球轨迹环绕物体移动，系统性地采集了典型工业物体的图像。MVM-IOD包含参考相机位姿和参考三维点云，以及9个物体在2种背景选择下获取的RGB图像，共形成18个场景，可评估所有基于图像的三维重建、相机位姿估计或场景新视角合成方法。基于MVM-IOD，我们全面评估了当前最先进的三维重建与相机位姿估计方法，包括运动恢复结构、多视图立体视觉、近期前馈方法（视觉几何基础Transformer、π3）以及二维高斯泼溅法，并将实验结果作为未来研究的基准。实验表明，类似我们的采集设置会为前馈方法生成分布外图像，导致点云和相机位姿效果欠佳。但通过简单的预处理步骤，可使这些分布外图像更接近训练数据分布。因此，在特定工业应用中，应谨慎使用前馈方法。

---

### 9. WaveSync: Constrained Wavefront Optimization for Synchronized Co-Speech Gestures in Humanoid Robots

- **作者**: Thang Tran Viet, Thanh Nguyen Canh, Gia Huy Uong, Phuc Van Dinh, Tan Viet Tuyen Nguyen, Xiem HoangVan, Nak Young Chong
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.16600v1)
- **发表日期**: 2026-06-15
- **匹配关键词**: motion planning, human-robot interaction
- **arXiv**: [2606.16600v1](http://arxiv.org/abs/2606.16600v1)
- **📥 PDF**: 已下载至本地 (`2606.16600v1_WaveSync_Constrained_Wavefront_Optimization_for_Synchronized_Co-Speech_Gestures_in_Humanoid_Robots.pdf`)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/pairs-lab/WaveSync
- **中文摘要**: 富有表现力的伴随言语手势对于自然的人机交互至关重要，但在实体人形机器人上生成这些手势却十分困难，因为手势动作必须与言语重音对齐，同时满足严格的运动学和动力学约束。与虚拟化身不同，人形机器人无法自由执行快速或重叠的运动，这使得单词级别的同步与硬件安全的运动规划成为一个耦合问题。我们提出了\textbf{WaveSync}，一种混合框架，其中大语言模型将对话回应分解为结构化的语义模式，并为每个单词分配重要性权重，构建连续的语义重要性波。手势轨迹通过动态运动基元进行塑造，在增强表现力的同时确保运动学可行性。波前优化阶段通过峰值对齐实现手势与言语的同步，并通过手势时长压缩和前向传播解决残留的运动学冲突。基于五个对话场景的实验评估表明，我们的方法实现了高同步精度，并在客观和主观评价中均优于三种基线方法。WaveSync中的每个组件在生成富有表现力、语义合理且符合运动学约束的手势中都发挥着必要作用。代码、资源和视频可在\href{https://github.com/pairs-lab/WaveSync}{WaveSync}获取。

---

### 10. PROSE: Training-Free Egocentric Scene Registration with Vision-Language Models

- **作者**: Zhiang Chen, Nahyuk Lee, Boyang Sun, Taein Kwon, Marc Pollefeys, Zuria Bauer, Sunghwan Hong ⭐
  - **高亮作者**: Marc Pollefeys
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.16569v1)
- **发表日期**: 2026-06-15
- **匹配关键词**: scene graph
- **arXiv**: [2606.16569v1](http://arxiv.org/abs/2606.16569v1)
- **📥 PDF**: 已下载至本地 (`2606.16569v1_PROSE_Training-Free_Egocentric_Scene_Registration_with_Vision-Language_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 将同一室内空间在不同时间拍摄的两段影像进行配准，是机器人和增强现实系统实现持久空间记忆的基础，但该任务的实际版本是以自我为中心的，且最具可扩展性的形式仅依赖RGB图像。头戴式摄像头会产生模糊、快速移动且部分重叠的视角，从中难以恢复密集几何结构。经典配准方法依赖该场景所缺乏的清晰点云，而基于学习的场景图方法则需要预先构建或标注的图结构以及训练好的匹配器——我们发现后者在自我中心数据中表现脆弱。我们另辟蹊径，利用预训练的视觉-语言模型同时实现场景理解与跨扫描匹配。提出的PROSE（提示式场景配准）方法，通过现成的基础模型（用于几何、分割和语言）将每段RGB序列提升为对象级3D场景图，随后用同一VLM通过提示匹配两段RGB序列中的对象实例。为使匹配易于处理且可靠，我们以对象高度作为先验，通过成对的相同/不同查询验证每个候选匹配，再为每个匹配对象假设候选变换并选择几何一致性最强的结果求解刚体变换。PROSE无需新增可学习参数，也不依赖深度传感器、训练或标注图。在自我中心的Aria数字孪生和Aria日常活动基准测试中，该方法在真实点云和RGB重建点云上的配准精度均超越几何方法和基于学习的场景图基线，且其生成的场景图可直接迁移至下游任务。

---

### 11. RHO: Your Coding Agent is Secretly a Roboticist

- **作者**: Karim Elmaaroufi, Justin Svegliato, Sarunas Kalade, Graham Schelle, Sanjit A. Seshia, Matei Zaharia
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.16458v1)
- **发表日期**: 2026-06-15
- **匹配关键词**: VLA
- **arXiv**: [2606.16458v1](http://arxiv.org/abs/2606.16458v1)
- **📥 PDF**: 已下载至本地 (`2606.16458v1_RHO_Your_Coding_Agent_is_Secretly_a_Roboticist.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 代码即策略（CaP）已证明，大语言模型（LLM）能够通过组合感知、规划与控制原语编写代码来解决机器人任务。然而，现有CaP系统在测试阶段依赖多轮代码生成循环，这通常难以满足实时机器人控制需求。我们提出机器人控制框架优化（RHO）这一新范式：在训练阶段，支持工具调用的编码智能体能够提出并搜索可解释的神经符号化多文件策略仓库（仓库即策略），这些仓库组合了上述原语，而非依赖单一提示、函数或文件。RHO基于环境奖励与执行结果的反思性反馈进行搜索，而非依赖遥操作演示。在LIBERO-PRO等受扰动的拾放场景中，OpenVLA得分为0.0%，π₀.₅平均得分为12.83%，而RHO在相同低层原语下达到45.0%的成功率，比最强多轮智能体系统高2.5倍，比π₀.₅高3.5倍。在Robosuite基准上，RHO以70.0%的成功率创下新纪录，超越此前多轮方法68.29%的记录——且采用单轮执行，部署时无需LLM修正代码。当LLM用于控制循环时（如RAI的O3DE基准），RHO优化了部署智能体的多文件提示、工具与控制代码框架，使保留测试成功率从23.5%提升至44.3%，同时减少20%的时钟时间与27%的工具调用次数。

---

### 12. SemGeoNav:A Safety-Guided Visual Navigation Approach with Semantic Reasoning and Geometric Planning

- **作者**: Yu Liu, Zongyang Chen, Yan Guo, Chao Liu, Xianfei Pan
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.16400v1)
- **发表日期**: 2026-06-15
- **匹配关键词**: obstacle avoidance, visual navigation, navigation
- **arXiv**: [2606.16400v1](http://arxiv.org/abs/2606.16400v1)
- **📥 PDF**: 已下载至本地 (`2606.16400v1_SemGeoNavA_Safety-Guided_Visual_Navigation_Approach_with_Semantic_Reasoning_and_Geometric_Planning.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 基于学习的视觉导航技术提升了语义目标到达能力。然而，由于纯端到端模型的黑箱特性，其往往缺乏显式几何约束，导致在开放环境中避障行为不可预测且不可靠。相比之下，传统几何规划器虽能确保安全性，却难以处理高维视觉目标。为解决这些局限，我们提出SemGeoNav——一种新颖的分层视觉导航框架。该框架将端到端模型的高层语义推理与基于几何方法的可靠局部规划能力紧密融合，在显著提升避障性能的同时实现鲁棒的图像导航。此外，我们引入时序轨迹平滑机制以确保机器人运动的连续性与稳定性。我们在真实环境中对宇树Go2四足机器人进行了SemGeoNav评估。结果表明，SemGeoNav在成功率和导航时间上均优于ViNT、NoMaD等现有代表性方法。

---

### 13. Learned Image Compression for Vision-Language-Action Models

- **作者**: Hyeonjun Kim, Jegwang Ryu, Sangbeom Ha, Junhyeok Lee, Jun-Hyuk Kim, Hyemin Ahn, Jaeho Lee
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.16253v1)
- **发表日期**: 2026-06-15
- **匹配关键词**: VLA, vision-language-action, vision-language-action model
- **arXiv**: [2606.16253v1](http://arxiv.org/abs/2606.16253v1)
- **📥 PDF**: 已下载至本地 (`2606.16253v1_Learned_Image_Compression_for_Vision-Language-Action_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉-语言-动作（VLA）模型日益依赖高频多摄像头观测，这使得视觉通信成为带宽受限或分布式部署场景中实时机器人控制的主要瓶颈。然而，现有图像与视频编解码器旨在保留通用视觉保真度，而非下游VLA策略的控制性能。本文提出SPARC（空间自适应码率控制）框架——一种专为VLA驱动型机器人设计的可学习图像压缩方法。我们的关键发现是：视觉信息的重要性在不同摄像头视角及图像空间区域间存在显著差异。基于此，SPARC采用轻量级时序掩码选择器，根据任务相关性自适应分配潜在表征的码率，同时利用时序上下文信息。我们进一步引入倾斜率损失，通过降低基于熵的目标函数过度抑制罕见但任务关键型视觉模式的倾向，从而稳定训练过程。在RoboCasa365、VLABench和LIBERO等多个机器人基准测试中的实验表明，在相同码率预算下，SPARC始终比传统图像/视频编解码器及近期可学习压缩方法取得更强的控制性能。此外，我们在远程控制场景中验证了实际部署优势——该方法显著改善了码率与成功率之间的权衡关系。

---

### 14. ATHENA: Accelerated Multi-Task Heterogeneous Influence Functions for Robot Data Curation

- **作者**: Tao Xu, Jiaxin Wang, Runhao Zhang, Jiayi Guan, Xianchao Zeng, Weixi Song, Xinyu Zhou, Zhetao Chen, Guang Chen, Yong-Lu Li
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.16208v1)
- **发表日期**: 2026-06-15
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2606.16208v1](http://arxiv.org/abs/2606.16208v1)
- **📥 PDF**: 已下载至本地 (`2606.16208v1_ATHENA_Accelerated_Multi-Task_Heterogeneous_Influence_Functions_for_Robot_Data_Curation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 在机器人模仿学习中，影响函数为量化每条示范对机器人任务结果的影响提供了理论依据，但将其扩展到十亿参数级别的视觉-语言-动作（VLA）模型时，受限于计算瓶颈和多任务处理瓶颈。为此，我们提出ATHENA——一个专为十亿参数规模多任务VLA数据筛选设计的影响函数框架。具体而言，该框架利用线性层梯度的克罗内克结构降低投影成本，并通过秩为r的随机截断近似方法逼近密集海森矩阵求逆，实现约313.4倍的影响计算加速。此外，ATHENA构建了全局与局部交互影响机制，以平衡50个联合训练任务间的数据筛选。在涵盖9.34小时和6.90小时示范数据的RoboTwin 2.0仿真及真实机器人部署评估中，ATHENA仅使用50%仿真示范数据和66.7%真实机器人任务数据，即可达到或超越全数据联合微调的性能。总体而言，ATHENA证明了其在十亿参数多任务VLA微调中数据筛选的有效性。

---

### 15. Scaling Short-Term Memory of Visuomotor Policies for Long-Horizon Tasks

- **作者**: Rutav Shah, Rajat Kumar Jenamani, Xiaohan Zhang, Lingfeng Sun, Roberto Martín-Martín, Yuke Zhu, Deva Ramanan, Karl Schmeckpeper ⭐
  - **高亮作者**: Yuke Zhu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.16178v1)
- **发表日期**: 2026-06-15
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2606.16178v1](http://arxiv.org/abs/2606.16178v1)
- **📥 PDF**: 已下载至本地 (`2606.16178v1_Scaling_Short-Term_Memory_of_Visuomotor_Policies_for_Long-Horizon_Tasks.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 许多机器人任务都需要短期记忆，无论是取回一个不再可见的物体，还是在设定时间后关闭电器。然而，大多数通过模仿学习训练的视觉运动策略仅依赖即时感官输入，而不利用过往经验来指导决策。我们提出PRISM，一种基于Transformer架构的视觉运动策略，通过两个关键组件有效利用短期记忆：（i）门控注意力机制，它过滤检索到的信息以抑制无关细节，通过减少历史信息与当前动作预测之间的虚假相关性来提升性能；（ii）层次化架构，首先将局部信息压缩为紧凑令牌，再整合这些令牌以捕捉时间上延展的依赖关系，从而优化计算和内存占用。这些机制共同使视觉运动策略的短期记忆可扩展至两分钟。为系统评估视觉运动控制中的记忆能力，我们引入ReMemBench——一个包含八项多样化家务操作任务的基准测试，涵盖四类短期记忆场景——旨在促进通用记忆机制的发展，而非孤立的、针对特定任务的解决方案。PRISM始终优于先前的工作，包括循环架构、Transformer及其变体——相较于最强基线实现了5%至12%的绝对提升。在RoboCasa和LIBERO基准测试中，尽管未利用任何大规模预训练，PRISM相较于无记忆变体以及GR00T-N1-3B和OpenVLA等微调视觉-语言-动作基线，仍实现了11%至15%的绝对提升。PRISM与ReMemBench共同为开发与评估可扩展至长时域任务的短期记忆增强型视觉运动策略奠定了基础。更多资料请访问https://shahrutav.github.io/short-term-memory。

---

### 16. SidewalkBench: Benchmarking Visual Navigation on Urban Sidewalks

- **作者**: Zhizheng Liu, Honglin He, Vivek Alumootil, Akshat Pandya, Brad Squicciarini, Wayne Wu, Bolei Zhou
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.16953v1)
- **发表日期**: 2026-06-15
- **匹配关键词**: visual navigation, navigation
- **arXiv**: [2606.16953v1](http://arxiv.org/abs/2606.16953v1)
- **📥 PDF**: 已下载至本地 (`2606.16953v1_SidewalkBench_Benchmarking_Visual_Navigation_on_Urban_Sidewalks.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 城市人行道导航面临复杂结构布局、动态行人行为及长距离行进等显著挑战。尽管近期视觉导航模型提供了有前景的解决方案，但缺乏统一基准阻碍了量化与可重复评估。为填补这一空白，我们提出SidewalkBench——专为城市人行道视觉导航设计的综合基准。该基准基于NVIDIA Isaac Sim构建，通过GPU加速模拟多样化、高保真的人行道环境，涵盖程序化生成场景与真实扫描场景。我们进一步为场景注入丰富的、基于事件的反应式行人行为及灵活高效的动画系统，从而在真实世界设定下实现标准化模型评估。我们在330个单元测试场景、800个行人反应场景及105个长时域场景中，对9种视觉导航模型进行了全面评估。研究结果表明，行人交互与长时域鲁棒性仍是现有模型的关键瓶颈，而利用合成数据扩展人行道训练正成为极具前景的解决方案。

---

### 17. CrossMaps: Confidence-Aware Open-Vocabulary Semantic Mapping for Rover Navigation

- **作者**: Jan-Niklas Klein, Sona Ghahremani, Christian Medeiros Adriano, Holger Giese
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.16935v1)
- **发表日期**: 2026-06-15
- **匹配关键词**: navigation
- **arXiv**: [2606.16935v1](http://arxiv.org/abs/2606.16935v1)
- **📥 PDF**: 已下载至本地 (`2606.16935v1_CrossMaps_Confidence-Aware_Open-Vocabulary_Semantic_Mapping_for_Rover_Navigation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 月球车依靠感知系统维护空间地图，该地图同时编码物体信息和传感器质量（如测距可靠性、光照伪影、数据密度），从而在部分可观测条件下指导数据融合、嵌入更新和导航。为研究这种感知-导航耦合过程，我们提出CrossMaps——一种实时置信感知开放词汇语义建图流程，能够从RGB-D数据构建可语言查询的地图。基于VLMaps类方法，CrossMaps将多尺度CLIP嵌入与置信感知融合技术相结合，并采用包含短期记忆（STM）和长期记忆（LTM）的双记忆架构。STM利用几何、语义和时间置信度线索聚合含噪视觉观测，而高置信度且空间一致的单元则被提升至LTM作为持久语义地标。该系统专为搭载Jetson Orin的无人地面车与SLAM协同部署而设计，可实时运行并生成语义热力图，通过自然语言查询引导月球车导航。

---

### 18. Local-GS: Accelerating 3D Gaussian Splatting via Tile-Local Warp Coherence

- **作者**: Yang Luo, Yan Gong, Yongsheng Gao, Jie Zhao, Xinyu Zhang, Huaping Liu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.16566v1)
- **发表日期**: 2026-06-15
- **匹配关键词**: 3D gaussian splatting, gaussian splatting
- **arXiv**: [2606.16566v1](http://arxiv.org/abs/2606.16566v1)
- **📥 PDF**: 已下载至本地 (`2606.16566v1_Local-GS_Accelerating_3D_Gaussian_Splatting_via_Tile-Local_Warp_Coherence.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 三维高斯溅射（3DGS）通过将场景表示为各向异性三维高斯原语的密集集合，显著推进了实时新视角合成技术。然而，高斯原语的不规则空间分布常导致GPU利用率低下，因为线程束发散和冗余计算会降低渲染性能。为此，我们提出Local-GS——一种线程束协同渲染范式，该范式基于SIMT（单指令多线程）执行边界而非场景几何结构来组织高斯原语。具体而言，我们设计了三个线程束协同阶段：提升阶段在瓦片级别预计算共享参数，剔除阶段丢弃无贡献的线程束，混合阶段用统一指令流替代逐像素分支。在多个数据集的广泛基准测试中，Local-GS在保持质量的同时提升了效率。作为即插即用的优化方案，它为所有测试基线提供了额外性能增益，在Deep Blending场景中最终实现了7.76倍的加速。

---

### 19. APEX: Adaptive Policy Execution for Precise Manipulation

- **作者**: Mengfei Zhao, Chenxi Jiang, Tuo An, Jindou Jia, Jianfei Yang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.16504v1)
- **发表日期**: 2026-06-15
- **匹配关键词**: VLA, vision-language-action
- **arXiv**: [2606.16504v1](http://arxiv.org/abs/2606.16504v1)
- **📥 PDF**: 已下载至本地 (`2606.16504v1_APEX_Adaptive_Policy_Execution_for_Precise_Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 现代模仿学习方法（包括视觉运动策略和视觉-语言-动作（VLA）策略）通常输出由底层控制器执行的高层动作参考。然而，由于缺乏高阶参考信号，且策略在训练过程中对底层控制动态缺乏感知，不可避免地导致了执行偏差。由此产生的实际动作会系统性地偏离策略指令，对精度敏感的操作产生关键影响。先前的研究要么修改策略架构，要么修改底层控制器，两者都需要对预训练策略或封装控制器进行侵入式改动。这自然引发了一个问题：当策略和控制器都被视为不可访问的黑箱时，我们能否弥合执行偏差？我们提出自适应策略执行（APEX），这是一个即插即用的框架，插入在策略和控制器之间，从策略输出中重构动态可行的参考，并在测试时根据底层状态反馈进行自适应调整，且具有可证明的收敛保证。大量实证研究表明，APEX在演示回放中将控制器引起的跟踪误差降低了41.2%，并在四种视觉运动策略和VLA策略类别中将操作成功率提升了4.8至25.8个百分点。

---

### 20. Uncertainty Quality of VGGT: An Analysis on the DTU Benchmark Dataset

- **作者**: Markus Hillemann, Robert Langendörfer, Steven Landgraf, Markus Ulrich
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.16479v1)
- **发表日期**: 2026-06-15
- **匹配关键词**: 3D reconstruction, 3d reconstruction
- **arXiv**: [2606.16479v1](http://arxiv.org/abs/2606.16479v1)
- **📥 PDF**: 已下载至本地 (`2606.16479v1_Uncertainty_Quality_of_VGGT_An_Analysis_on_the_DTU_Benchmark_Dataset.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 视觉几何基础Transformer（VGGT）在短时间内便引起了广泛关注，尤其因其荣获CVPR-2025最佳论文奖。与DUSt3R和MASt3R类似，VGGT旨在推动范式变革，用简单统一的单次前馈神经网络取代光束法平差和特征匹配等传统方法，该网络可在数秒内直接从场景的多张图像预测相机位姿、深度图和稠密三维结构。其关键特性在于能够通过单次前向传播一致性地处理任意数量的视图，无需任何后处理或迭代优化。对于摄影测量领域而言，这为实时、可扩展且易获取的三维重建开辟了新可能。在此背景下，不仅高重建精度至关重要，高质量的置信度估计同样不可或缺——它能增强可信度并实现稳健的质量保障。因此，本文系统研究了VGGT不确定性预测的质量。通过分析，我们确定了用于过滤VGGT原始输出的有效置信度阈值，并证明提升不确定性质量对改善其三维重建精度具有巨大潜力。

---

