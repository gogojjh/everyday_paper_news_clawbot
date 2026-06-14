# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-06-14 08:01

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 5/20 篇提供

**🌟 Highlight**: 15 篇 | **📌 Poster**: 5 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. Mana: Dexterous Manipulation of Articulated Tools

- **作者**: Zhao-Heng Yin, Guanya Shi, Pieter Abbeel, C. Karen Liu ⭐
  - **高亮作者**: Guanya Shi
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.13677v1)
- **发表日期**: 2026-06-11
- **匹配关键词**: motion planning, tool use, affordance
- **arXiv**: [2606.13677v1](http://arxiv.org/abs/2606.13677v1)
- **📥 PDF**: 已下载至本地 (`2606.13677v1_Mana_Dexterous_Manipulation_of_Articulated_Tools.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 铰接式工具操作仍是灵巧机器人领域的一项重大挑战，因其需要协调内部自由度与密集接触的交互过程。尽管先前研究主要聚焦于刚性物体，但铰接式工具的使用因物理复杂性高、功能性抓取与操作策略学习困难而尚未得到充分探索。我们提出Mana（操控动画师）——一个通用的仿真到现实框架，将灵巧操作重新诠释为动画问题。受计算机动画启发，Mana采用由粗到精的流水线，通过运动规划与强化学习将程序化生成的抓取关键帧转化为操作轨迹。数据生成过程基本实现自动化，仅需数次鼠标点击即可指定功能可供性（每个工具耗时<1分钟）。在涵盖不同尺度与关节类型的四种铰接式工具上，Mana实现了抓取与手内操作的零样本仿真到现实迁移，为灵巧铰接式工具使用提供了可扩展的解决方案。

---

### 2. LabVLA: Grounding Vision-Language-Action Models in Scientific Laboratories

- **作者**: Baochang Ren, Xinjie Liu, Xi Chen, Yanshuo Liu, Chenxi Li, Daqi Gao, Zeqin Su, Jintao Xing, Zirui Xue, Rui Li, Xiangyu Zhao, Shuofei Qiao, Minting Pan, Wangmeng Zuo, Lei Bai, Dongzhan Zhou, Ningyu Zhang, Huajun Chen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.13578v1)
- **发表日期**: 2026-06-11
- **匹配关键词**: vision-language-action, VLA, vision-language-action model
- **arXiv**: [2606.13578v1](http://arxiv.org/abs/2606.13578v1)
- **📥 PDF**: 已下载至本地 (`2606.13578v1_LabVLA_Grounding_Vision-Language-Action_Models_in_Scientific_Laboratories.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 科学实验室日益依赖AI系统进行实验推理，但实际的物理操作仍远未实现自动化。AI能够辅助文献阅读、假设生成和方案设计，然而实验台前的具体操作仍需人类完成。视觉-语言-动作（VLA）模型为书面方案与机器人执行之间提供了可能的接口，但现有策略主要基于家庭和桌面场景的训练数据，极少涉及科学实验室中的仪器设备、透明液体或固定实验流程。弥补这一差距既需要实验室专属的监督数据，也需要能够适配执行实验方案的不同机器人形态的统一学习框架。因此，我们确定数据和机器人形态与模型设计同为关键瓶颈。为解决数据问题，我们构建了RoboGenesis——一个基于仿真的工作流与数据引擎，能够从原子技能组合配置实验室工作流，验证并过滤执行结果，最终为支持的机器人配置导出结构化演示数据。在策略层面，我们提出LabVLA模型，采用两阶段训练策略：首先通过FAST动作令牌预训练使Qwen3-VL-4B-Instruct骨干网络在连续控制学习前具备动作感知能力，随后在知识隔离条件下通过流匹配后训练附加DiT动作专家模块。在LabUtopia基准测试中，LabVLA在分布内和分布外场景下均取得了所有评估基线中最高的平均成功率。

---

### 3. NavWAM: A Navigation World Action Model for Goal-Conditioned Visual Navigation

- **作者**: Daichi Azuma, Taiki Miyanishi, Koya Sakamoto, Shuhei Kurita, Yaonan Zhu, Petr Khrapchenkov, Motoaki Kawanabe, Yusuke Iwasawa, Yutaka Matsuo
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.13494v1)
- **发表日期**: 2026-06-11
- **匹配关键词**: navigation, visual navigation, image-goal navigation
- **arXiv**: [2606.13494v1](http://arxiv.org/abs/2606.13494v1)
- **📥 PDF**: 已下载至本地 (`2606.13494v1_NavWAM_A_Navigation_World_Action_Model_for_Goal-Conditioned_Visual_Navigation.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://dachii-azm.github.io/navwam/
- **中文摘要**: 目标条件视觉导航要求机器人在部分可观测条件下，通过预测自身运动如何改变未来的自我中心视角，以及这种变化是否使其更接近目标来采取行动。导航世界模型提供了此类视觉前瞻能力，但这类模型仍属于预测模块，需要外部规划器将预测的未来状态转化为闭环控制。我们提出导航世界动作模型（NavWAM），这是一种扩散-变换器策略，通过将未来观测、目标进度值和动作片段编码到共享潜在序列中，将导航世界模型的预测转化为可执行动作。通过联合学习未来预测与决定闭环行为的动作及价值目标，NavWAM使视觉前瞻能力可直接用于机器人控制。我们通过仿真预训练和真实机器人适配构建NavWAM，并在图像目标导航任务中，将其与基于规划的世界模型及代表性直接导航策略进行对比评估。在离线基准测试和真实机器人闭环部署中，NavWAM在采用默认策略模式（无需CEM式动作搜索）的情况下，相较于基于规划的世界模型基线取得了性能提升。项目页面：https://dachii-azm.github.io/navwam/

---

### 4. GIVE: Grounding Human Gestures in Vision-Language-Action Models

- **作者**: Pengfei Liu, Gen Li, Junqiao Fan, Boyu Ma, Jindou Jia, Yang Xiao, Jianfei Yang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.13435v1)
- **发表日期**: 2026-06-11
- **匹配关键词**: vision-language-action model, HRI, vision-language-action, human-robot interaction, VLA
- **arXiv**: [2606.13435v1](http://arxiv.org/abs/2606.13435v1)
- **📥 PDF**: 已下载至本地 (`2606.13435v1_GIVE_Grounding_Human_Gestures_in_Vision-Language-Action_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 人类交流本质上是多模态的，语言常伴随手势等非语言线索来传达意图。然而，当前的视觉-语言-动作（VLA）模型将机器人操作视为纯文本驱动的任务，忽视了手势在人机交互（HRI）中的重要作用。当语言指令模糊或信息不足时，这往往会导致意图定位不准确和操作不可靠。为解决这一挑战，我们提出GIVE（通过视觉语义增强的手势意图）方法，这是一种在不修改架构的前提下，通过增强预训练VLA模型的人类手势理解能力的有效方案。具体而言，GIVE通过两条互补路径整合手势信息：视觉路径将手部骨架和指尖射线叠加到机器人观测中实现显式物体定位，语义路径则生成人类手势与任务指令的高层描述以实现鲁棒的意图定位。通过联合利用视觉与语义引导，GIVE使VLA策略能更好地将手势与操作行为关联，并适应动态交互意图。在真实世界的人机交互实验中，GIVE显著优于基线方法，目标物体识别准确率提升40%，整体任务成功率提升80%，同时展现出对未见空间布局和不同参与者的强大鲁棒性与泛化能力。

---

### 5. See Selectively, Act Adaptively: Dual-Level Structural Decomposition for Bimanual Robot Manipulation

- **作者**: Yoon-Ji Choi, Young-Chae Son, Soo-Chul Lim
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.13279v1)
- **发表日期**: 2026-06-11
- **匹配关键词**: vision-language-action, VLA, bimanual manipulation
- **arXiv**: [2606.13279v1](http://arxiv.org/abs/2606.13279v1)
- **📥 PDF**: 已下载至本地 (`2606.13279v1_See_Selectively,_Act_Adaptively_Dual-Level_Structural_Decomposition_for_Bimanual_Robot_Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 在双臂机器人操作中，任务相关的视觉信息会随任务阶段和情境动态变化，而双臂的交互模式则在独立与协同状态间切换，这使得策略学习极具挑战性。然而，现有的整体式视觉-语言-动作（VLA）策略通过单一共享表征和动作生成路径处理多样化的视觉输入与交互模式，往往无法分别考虑视觉相关性和双臂交互结构。为解决这一问题，我们提出了一种基于双层结构分解的双臂操作VLA框架。其中，视角选择视觉路由器动态调整腕部视角的贡献权重以突出相关视觉线索，而交互感知动作混合专家（MoE）则将动作生成分解为协同与单臂两条路径，以适应不同的双臂交互模式。我们在RoboTwin 2.0的六项模拟双臂操作任务和三项长时域真实世界任务中评估了该方法。与整体式基线相比，我们的模型在模拟环境中将整体平均成功率提升了27.7%，在真实世界评估中提升了43.3%，并且在两种场景下均持续优于单模块变体。这些结果表明，联合考虑选择性视觉处理与双臂交互结构的显式分解，为鲁棒的双臂操作提供了有效的归纳偏置。

---

### 6. WT-UMI: Tactile-based Whole-Body Manipulation via Force-Supervised Contact-Aware Planning

- **作者**: Jaehwi Jang, Zhaoyuan Gu, Alfred Cueva, Zimeng Chai, Junjie Sheng, Thong Nguyen, Himank Galundia, Yifan Wu, Huishu Xue, Isaac Legene, Ojas Mediratta, Davin Doan, Andrew Collins, Sarah Sadegh, KyoungMok Kim, Rishita Dhalbisoi, Zun Chen, Ye Zhao
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.13232v1)
- **发表日期**: 2026-06-11
- **匹配关键词**: whole-body manipulation
- **arXiv**: [2606.13232v1](http://arxiv.org/abs/2606.13232v1)
- **📥 PDF**: 已下载至本地 (`2606.13232v1_WT-UMI_Tactile-based_Whole-Body_Manipulation_via_Force-Supervised_Contact-Aware_Planning.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://wt-umi.github.io/WTUMI/.
- **中文摘要**: 全身型人形机器人对笨重、可变形及共享负载物体的操作需要分布式接触感知和显式力调节，然而大多数模仿策略仅隐式处理接触力。另一方面，不同演示源提供了具有固有权衡的互补模态：人类演示捕捉自然接触力但无法生成机器人可执行动作，而遥操作直接记录机器人动作却缺乏自然的力调节能力。本文提出\textbf{WT-UMI}——一种可穿戴全身触觉接口，可由人类操作员佩戴或安装于人形机器人上，在人类演示和人形机器人遥操作两种模式下提供触觉图像、接触力及末端执行器位姿的精确观测。我们引入力条件化目标位姿修正模块，通过从遥操作数据中学习修正量，将测量到的人类位姿转换为接触感知的机器人目标。为利用人类数据中的自然力交互，我们提出力监督规划器，可预测末端执行器位姿片段和接触力轨迹。预测的接触力作为基于触觉的导纳控制器的参考值。在涵盖可变形物体、笨重刚体及人机协作的五项接触密集型任务中，WT-UMI相较于四种策略基线提升了成功率并降低了接触位置跟踪误差。项目页面详见https://wt-umi.github.io/WTUMI/。

---

### 7. Proprioceptive-visual correspondence enables self-other distinction in humanoid robots

- **作者**: Yurun Chen, Tianyuan Gao, Yizhong Ge, Shikun Ban, Yizhou Wang, Hongkai Xiong, Wenjun Zeng, Wentao Zhu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.13222v1)
- **发表日期**: 2026-06-11
- **匹配关键词**: motion planning
- **arXiv**: [2606.13222v1](http://arxiv.org/abs/2606.13222v1)
- **📥 PDF**: 已下载至本地 (`2606.13222v1_Proprioceptive-visual_correspondence_enables_self-other_distinction_in_humanoid_robots.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://euron-zc.github.io/humanoid-self-model/.
- **中文摘要**: 区分自我与他人是社会智能的前提，然而与人类共享工作空间的人形机器人仍缺乏这种能力。本研究展示了一种方法：人形机器人可通过本体感觉-视觉对应关系学习自我-他人区分，无需任何身份标签或运动学模型。一旦建立这种区分能力，即可引导出预测性自我模型——该模型将关节构型映射至三维身体占用空间，捕捉机器人身体随动作变化的方式。在涉及人类或形态相同机器人的多智能体场景中，该系统能可靠识别自身，学习三维自我模型，并支持目标抓取、碰撞感知运动规划及人机运动重定向等下游任务。这些成果共同勾勒出一条路径：使机器人在共享物理空间中与同伴协作时，能够建立身体自我表征。项目页面：https://euron-zc.github.io/humanoid-self-model/

---

### 8. Y-BotFrame: An Extensible Embodied Agent Framework for Quadruped Robot Assistants

- **作者**: Luyao Zhang, Ke Li, Yuan Ding, Xulong Zhao, Guo Yu, Chengwei Yan, Fuyu Dong, Jiawei Hu, Di Wang, Nan Luo, Gang Liu, Quan Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.13049v1)
- **发表日期**: 2026-06-11
- **匹配关键词**: navigation, human-robot collaboration, visual feedback
- **arXiv**: [2606.13049v1](http://arxiv.org/abs/2606.13049v1)
- **📥 PDF**: 已下载至本地 (`2606.13049v1_Y-BotFrame_An_Extensible_Embodied_Agent_Framework_for_Quadruped_Robot_Assistants.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 四足机器人具备高度灵活性，能够穿越多种复杂地形。作为高机动性的地面智能平台，它们可搭载导航控制、环境感知及智能交互模块，成为各类算法的实体移动部署载体。本文提出Y-BotFrame可扩展具身平台，将机器人转化为智能地面助手。该系统融合语音、视觉与激光雷达等多模态感知能力，采用大语言模型作为认知核心，实现环境理解、上下文推理与任务规划。系统将用户自然语言指令映射为机器人可执行的具身任务单元。Y-BotFrame支持通过语音指令与视觉反馈的自然交互方式，无需遥控器即可实现高效人机协作。凭借高度可扩展的框架，该系统支持新功能模块的即插即用集成，以及模块化升级与迭代开发，为通用型指令驱动具身智能体的实体部署提供了参考实现。补充视频见https://xdei-group.github.io/Y-BotFrame/。

---

### 9. Trajectory-Level Redirection Attacks on Vision-Language-Action Models

- **作者**: Gokul Puthumanaillam, Vardhan Dongre, Pranay Thangeda, Hooshang Nayyeri, Dilek Hakkani-Tür, Melkior Ornik
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.12978v1)
- **发表日期**: 2026-06-11
- **匹配关键词**: vision-language-action, VLA, vision-language-action model
- **arXiv**: [2606.12978v1](http://arxiv.org/abs/2606.12978v1)
- **📥 PDF**: 已下载至本地 (`2606.12978v1_Trajectory-Level_Redirection_Attacks_on_Vision-Language-Action_Models.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://vla-redirection-attack.github.io/
- **中文摘要**: 视觉-语言-动作（VLA）策略将自然语言引入闭环机器人控制，使机器人能够直接根据文本指令执行操作任务。由于提示在每次重新规划步骤中都会被重复使用，且每个提示条件化的动作都会改变策略所作用的未来观测结果，因此同一接口赋予了文本在控制中的循环作用。现有VLA攻击研究的是能够引发目标低级动作或使此类动作在变化的图像中持续存在的对抗性提示。我们识别出一种更强的轨迹级故障模式：一个看似仍指定了预期任务，但最终改变了物理结果的提示。我们在数学上将该场景形式化为“命令保持的轨迹重定向”，这是一种仅针对提示的威胁模型，其中攻击者在回合开始前选择一个提示，所有策略和环境组件保持固定，且提示必须接近良性指令，同时省略目标词和纠正性语言。为找到此类提示，我们引入了一种基于策略的提示搜索方法，该方法利用轨迹展开来发现满足命令保持约束的同时，其闭环行为追踪目标任务的扰动。仿真和硬件实验表明，接近良性的提示扰动可以将VLA轨迹展开重定向到攻击者指定的目标。这些结果揭示了VLA指令理解中的轨迹级漏洞：看似保留了预期命令的文本仍可能使攻击者控制机器人的最终物理结果。项目网站：https://vla-redirection-attack.github.io/

---

### 10. SERF: Spatiotemporal Environment and Robot Feature Map for Long-Horizon Mobile Manipulation

- **作者**: Sunghwan Kim, Byeonghyun Pak, Kehan Long, Yulun Tian, Nikolay Atanasov
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.12956v1)
- **发表日期**: 2026-06-11
- **匹配关键词**: vision-language-action, mobile manipulation, VLA
- **arXiv**: [2606.12956v1](http://arxiv.org/abs/2606.12956v1)
- **📥 PDF**: 已下载至本地 (`2606.12956v1_SERF_Spatiotemporal_Environment_and_Robot_Feature_Map_for_Long-Horizon_Mobile_Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 长时域机器人移动操作需要持续推理定位、环境变化和任务进度，这些信息仅凭图像观测难以推断。本文证明，将移动操作策略与时空特征图相结合，可提升长时域推理能力。该特征图在共享潜在空间中将环境与铰接机器人本体表示为神经点，并通过自我中心观测和本体感知状态进行在线更新。我们利用物体级刚性追踪更新环境神经点，通过正向运动学更新机器人神经点。通过从多参考帧和多空间尺度提取特征图标记，将所提出的时空环境与机器人特征（SERF）图作为状态输入至视觉-语言-动作（VLA）模型，为策略提供局部与全局上下文信息。我们在家庭环境长时域移动操作基准BEHAVIOR-1K上验证了SERF。实验表明，SERF VLA策略优于纯图像基线，通过更直接的轨迹更快达成子目标，增强了对场景配置变化的鲁棒性，并能从物体掉落故障中恢复。

---

### 11. An Embodied Simulation Platform, Benchmark, and Data-Efficient Augmentation Framework for Wet-Lab Robotics

- **作者**: Zhe Liu, Huanbo Jin, Zhaohui Du, Zhe Wang, He Xu, Peijia Li, Jiaming Gu, Quan Lu, Qi Wang, Bin Ji, Ting Xiao
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.12936v1)
- **发表日期**: 2026-06-11
- **匹配关键词**: VLA
- **arXiv**: [2606.12936v1](http://arxiv.org/abs/2606.12936v1)
- **📥 PDF**: 已下载至本地 (`2606.12936v1_An_Embodied_Simulation_Platform,_Benchmark,_and_Data-Efficient_Augmentation_Framework_for_Wet-Lab_Ro.pdf`)
- **🔓 开源**: CODE
- **中文摘要**: 湿实验室机器人能够提升生物医学实验的可重复性、通量和安全性，但其规模化学习需要可定制的模拟器以生成安全且可重复的任务、开放可编辑的实验室资产，以及将有限示范转化为可用训练数据的高效流程。我们提出Pipette——一个面向湿实验室机器人学习的具身仿真平台、基准测试及数据高效增强框架。Pipette发布了超过43个开源且可重新编辑的湿实验室资产，并配套可扩展的资产构建流程。其核心组件是基于仿真的数据增强流程：在仿真环境中重放人类示范，施加光照、相机视角、速度及动作扰动，并通过自动任务成功检测过滤生成的片段，从而从有限人工示范中快速扩展可用训练数据。我们进一步引入包含11项任务的湿实验室具身基准测试，涵盖样本处理、培养器具操作、设备操作及精密放置。在每项任务仅30次示范的条件下，ACT方法达到65.5%的平均成功率，而仿真增强将SmolVLA从44.1%提升至74.7%，π0从40.4%提升至46.5%，验证了Pipette在数据高效的视觉-语言-动作（VLA）训练与评估中的有效性。此外，Pipette支持自然语言驱动的场景构建与任务注册，降低了非专业用户定义新型湿实验室机器人任务的门槛。

---

### 12. AIR-VLA+: Decoupling Movement and Manipulation via Cascaded Dual-Action Decoders with Asymmetric MoE for Aerial Robots

- **作者**: Jianli Sun, Bin Tian, Qiyao Zhang, Zijian Liu, Yutong Wang, Zhiyong Cui, Bai Li, Yisheng Lv, Yonglin Tian
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.12859v1)
- **发表日期**: 2026-06-11
- **匹配关键词**: VLA
- **arXiv**: [2606.12859v1](http://arxiv.org/abs/2606.12859v1)
- **📥 PDF**: 已下载至本地 (`2606.12859v1_AIR-VLA+_Decoupling_Movement_and_Manipulation_via_Cascaded_Dual-Action_Decoders_with_Asymmetric_MoE_.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 空中操控系统长期以来一直受到端到端控制中表征耦合问题的困扰，因为平台级无人机（UAV）运动与末端执行器级机械臂操作在动作尺度、动力学特性和控制目标上存在显著差异。本文提出AIR-VLA+——一种专为空中操控设计的流匹配动作生成架构，其核心包含级联双动作解码器与非对称特征级混合专家（MoE）模块。我们构建了级联的操控与运动解码器，使无人机在运动过程中能够单向观测机械臂的意图以实现工作流协同，同时隔离无人机运动信息反向传播对机械臂操作稳定性的影响。针对无人机运动高度依赖高层语义且负责空中操控任务状态转换的特性，我们为无人机运动解码器设计了输入特征增强模块。该模块引入隐式视觉抓取投影器以感知夹爪与物体的交互状态，并注入压缩后的全局语义特征。在无人机运动解码器内部，我们部署了隐式MoE架构，使不同运动专家在训练过程中自发展现出对不同任务阶段的能力倾向。通过在特征流形上进行密集软混合计算，无人机运动获得了更强的任务阶段适应性。在标准化AIR-VLA基准上的实验表明，本方法以48.0的总体平均分全面超越所有基线，整体任务完成分数较单头π₀.₅策略提升80.2%，有效缓解了复合机器人的异构协调控制冲突。

---

### 13. Stubborn: A Streamlined and Unified Reinforcement Learning Framework for Robust Motion Tracking and Fall Recovery for Humanoids

- **作者**: Xiao Ren, Yuhui Yang, Zongbiao Weng, Zhijie Liu, He Kong
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.12814v1)
- **发表日期**: 2026-06-11
- **匹配关键词**: exploration
- **arXiv**: [2606.12814v1](http://arxiv.org/abs/2606.12814v1)
- **📥 PDF**: 已下载至本地 (`2606.12814v1_Stubborn_A_Streamlined_and_Unified_Reinforcement_Learning_Framework_for_Robust_Motion_Tracking_and_F.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 近期，基于强化学习的方法在提升人形机器人运动跟踪性能及实现扰动下的跌倒恢复方面展现出巨大潜力。然而，现有研究大多将运动跟踪与跌倒恢复视为不同任务，需要多阶段训练并配备专门的恢复奖励机制和/或独立的恢复策略。此外，现有强化学习方法常在严重跟踪失败后立即终止训练回合，限制了在失稳或跌倒状态下的恢复导向探索。针对上述问题，我们提出Stubborn——一种精简统一的强化学习框架，用于实现鲁棒的人形机器人运动跟踪与跌倒恢复。具体而言，Stubborn采用非对称Actor-Critic架构，包含三大核心组件：首先，采用偏航对齐的跟踪表征方法，在保留重力相关平衡信息的同时降低对全局漂移和航向扰动的敏感度；其次，引入基于伯努利分布的概率终止机制，使策略能够鼓励在不同失败模式下探索跌倒恢复行为；最后，提出概率终止与跟踪误差驱动的动态采样策略，根据跟踪性能重塑采样分布，提升困难运动片段和失稳状态的训练效率。与现有最优方法的全面对比及消融实验表明，Stubborn取得了具有竞争力的性能，所提出的概率终止机制与自适应采样策略对性能提升和鲁棒性增强具有显著贡献。真实世界演示请参见：https://aislab-sustech.github.io/Stubborn/。

---

### 14. Flex4DHuman: Flexible Multi-view Video Diffusion for 4D Human Reconstruction

- **作者**: Jen-Hao Cheng, Yipeng Wang, Hao Zhang, Gengshan Yang, Jenq-Neng Hwang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.13655v1)
- **发表日期**: 2026-06-11
- **匹配关键词**: gaussian splatting
- **arXiv**: [2606.13655v1](http://arxiv.org/abs/2606.13655v1)
- **📥 PDF**: 已下载至本地 (`2606.13655v1_Flex4DHuman_Flexible_Multi-view_Video_Diffusion_for_4D_Human_Reconstruction.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出Flex4DHuman，一种多视角视频扩散模型，能够将动态主体的单目或稀疏多视角视频，仅通过相对相机位姿条件约束，转化为同步的密集多视角视频。与以往依赖骨架、深度图、法线或渲染目标视角几何的人体中心方法不同，Flex4DHuman无需显式几何先验，而是通过相对相机位姿位置编码来引导生成过程。生成的视频可直接输入下游重建流程，创建动态4D高斯泼溅。基于Wan 2.1 1.3B文本生成视频模型，Flex4DHuman保留了骨干架构，并通过五轴位置编码编码相机与视角信息——该编码在时空RoPE基础上扩展了视角索引和连续SE(3)相对相机几何。三阶段课程学习逐步训练模型实现位姿跟随、灵活参考到目标视角生成以及时间展开。为支持时间展开，我们使用干净的历史目标视角令牌进行训练。同时加入多视角描述以实现测试时文本控制。结合现成的4D高斯泼溅阶段，我们的框架可将单目静态相机视频提升为动态4D高斯泼溅。在DNA-Rendering和ActorsHQ上的实验表明，Flex4DHuman超越了先前最先进方法，且同一公式在混合人体-动物训练后可泛化至动物类别。这些能力使Flex4DHuman成为从随意单目视频实现可扩展4D内容创作（适用于仿真、游戏、AR/VR及视频重拍）的实用一步。

---

### 15. Real-Time Execution with Autoregressive Policies

- **作者**: Sangkyu Lee, Seohyeon Park, Tackgeun You, Avi Caciularu, Idan Szpektor, Hwasup Lim, Youngjae Yu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.13355v1)
- **发表日期**: 2026-06-11
- **匹配关键词**: vision-language-action, vision-language-action model
- **arXiv**: [2606.13355v1](http://arxiv.org/abs/2606.13355v1)
- **📥 PDF**: 已下载至本地 (`2606.13355v1_Real-Time_Execution_with_Autoregressive_Policies.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 实时执行对于大规模视觉-语言-动作模型的实际部署至关重要，它通过异步推理确保动作轨迹的流畅性和快速响应能力。然而，近期关于实时执行的研究主要聚焦于扩散策略的变体，尽管自回归策略在同步推理中因生成速度较慢而更需要实时性优化。与此相反，我们证明自回归策略可通过调整分词粒度并应用约束解码实现实时执行，从而保证严格的延迟上限，支持多轨迹解码以最大化性能。在仿真和真实环境实验中，我们发现自回归策略在显著提升同步推理任务完成速度的同时，始终优于同等水平的流匹配策略。结合自回归策略在指令跟随任务中收敛更快、泛化性更强的固有优势，这些结果证实自回归策略仍可作为一种具有竞争力的策略类型支持实时执行。

---

## 📌 Poster

*其他相关研究*

---

### 1. SPARC: Reliable Spatial Annotations from Robot Demonstrations at Scale

- **作者**: Nils Blank, Paul Mattes, Maximilian Xiling Li, Jakub Suliga, Thomas Roth, Moritz Reuss, Pankhuri Vanjani, Rudolf Lioutikov
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.13497v1)
- **发表日期**: 2026-06-11
- **匹配关键词**: motion planning
- **arXiv**: [2606.13497v1](http://arxiv.org/abs/2606.13497v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 本文提出了基于可靠性校准的机器人演示空间标注方法（SPARC），这是一种风险感知框架，能够自动为机器人演示添加结构化空间标注，并为每个标注分配可靠性评分。结构化空间标注（如边界框、物体轨迹和操作阶段标签）可广泛应用于多种机器人领域，包括训练具身机器人策略、构建具身基础模型、运动规划以及分层任务组合。现有自动化流水线虽能大规模生成此类标注，但缺乏可靠的质量信号：检测器置信度对标注正确性的校准效果不佳，迫使研究者只能在接受噪声标签或丢弃有用样本之间做出选择。与现有自动化流水线不同，SPARC利用机器人任务固有的时空结构生成可靠性信号，从而减少噪声标签并保留更多有用样本。我们进一步提出了交互感知基准（IA-Bench），该基准用于衡量模型在机器人演示中定位交互物体位置的准确性。在涵盖多种具身形态与场景的1700个人工标注演示中，SPARC在定位精度上显著优于纯检测基线，同时在高精度操作点保留了三倍以上的样本。实验表明，基于SPARC标注微调的模型在物体定位与指向基准测试中，在同等规模模型中达到最优性能，并在更广泛的空间推理任务中保持竞争力，且无需人工验证或标注训练数据。此外，在杂乱且视觉模糊的真实场景中，基于SPARC标注训练的策略表现优于基线方法。代码、数据与模型已开源至intuitive-robots.github.io/sparc-labeling。

---

### 2. Point-Wise Geometry-Aware Transformer for Partial-to-Full Point Cloud Registration in Computer-Assisted Surgery

- **作者**: Siyu Zhou, Zhongliang Jiang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.13488v1)
- **发表日期**: 2026-06-11
- **匹配关键词**: navigation
- **arXiv**: [2606.13488v1](http://arxiv.org/abs/2606.13488v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 部分到整体的点云配准因重叠率变化、点密度波动及噪声干扰而颇具挑战。尽管Transformer在点云处理领域展现出强大潜力，但现有方法通常将其局限于全局上下文聚合，忽视了精确对应关系所需的关键细粒度局部几何特征。本文提出**GAPR-Net**——一种基于学习的点云配准框架，采用粗到精的架构融合卷积与Transformer模块，通过交叉注意力机制实现局部与全局信息在部分点云与完整点云间的融合。为此，我们提出一种变换不变的点级几何特征表示方法，能够稳健地捕捉每个点相对于其邻域点的相对几何特征。为评估方法有效性，我们在胫骨、股骨、骨盆及胸肋软骨四种几何形态各异的骨骼上开展实验。整体配准召回率达94.2%，均方根误差低至1.992毫米，旋转与平移的$R^2$值分别为0.908和0.974。结果表明，该方法有效解决了部分到整体的点云配准问题。该技术利用局部观测实现高精度三维点云配准，为计算机辅助手术中的精准导航与机器人介入提供了关键基础。代码将在双盲评审流程结束后公开。

---

### 3. Humor Style Drives Laughter, Topic Shapes Acceptability: Evaluating Bilingual Personal and Political Robot-Delivered AI Jokes

- **作者**: Anna-Maria Velentza, Anne-Gwenn Bosser
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.13256v1)
- **发表日期**: 2026-06-11
- **匹配关键词**: HRI, human-robot interaction
- **arXiv**: [2606.13256v1](http://arxiv.org/abs/2606.13256v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 幽默在人类社交关系中扮演着核心角色，而计算幽默的最新进展为人机交互中融入幽默创造了新机遇。尽管大型语言模型能够生成多种形式的幽默，但幽默风格、笑话内容及语言偏好如何影响群体环境中机器人传递幽默的感知仍不明确。本探索性研究采用混合因子设计，让参与者在大学教室中评估由机器人传递的AI生成笑话。我们考察了幽默类型（亲和型、自我提升型、攻击型、自贬型）与笑话内容（人物相关 vs. 政治相关）对感知趣味性和适宜性的影响，以及语言偏好。结果表明：幽默类型显著影响趣味性，攻击型和亲和型幽默评分更高；而笑话内容主要影响适宜性，人物相关笑话优于政治笑话。语言偏好则同时受笑话内容及参与者自评语言流利度与幽默实践的影响。

---

### 4. Embedding ISO 10218 Safety Compliance in Robots via Control Barrier Functions for Human-Robot Collaboration

- **作者**: Federico Parma, Cesare Tonola, Nicola Pedrocchi, Manuel Beschi
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.13203v1)
- **发表日期**: 2026-06-11
- **匹配关键词**: human-robot collaboration
- **arXiv**: [2606.13203v1](http://arxiv.org/abs/2606.13203v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 人机协作（HRC）要求严格遵守ISO 10218等安全标准，以防止有害交互。标准速度与分离监测（SSM）滤波器基于保守假设（如人体匀速运动）计算安全机器人速度，这导致无法准确预测最小安全距离，并引发不必要的操作中断。本文提出一种控制障碍函数（CBF），该函数显式融合人体加速度数据，在机器人最坏情况制动轨迹中解析式前向预测最小人机分离距离。为在控制层面保障安全，该预测性CBF被作为不等式约束集成到序列二次规划（SQP）框架中。具体提出两种方法：方法一为CBF约束的PD安全滤波器；方法二为施加空间管状约束的任务缩放SQP控制器。在UR10e机器人上进行的仿真与真实实验将两种方法与标准工业SSM模块基线进行对比。结果表明，方法二能动态调节执行速度并限制空间偏差。相较于方法一，方法二将平均轨迹误差降低63%，并避免过度规避动作，在符合ISO 10218 SSM指南的同时确保高任务吞吐量。

---

### 5. Multi-Modal Multi-Agent Robotic Cognitive Alignment enabled by Non-Invasive Consumer Brain Computer Interfaces: A Proof of Concept Exploration

- **作者**: Nataliya Kosmyna, Liz Jenkins, Anoop K. Sinha
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.13190v1)
- **发表日期**: 2026-06-11
- **匹配关键词**: exploration, human-robot interaction
- **arXiv**: [2606.13190v1](http://arxiv.org/abs/2606.13190v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 非语言行为与表达性动作对于自然的人机交互至关重要，但现有方法往往忽略了一个关键要素：人类的内部认知状态。主动式多智能体系统常在不恰当的时机打断人类，导致认知超负荷和任务表现下降。本文提出了一种生成"认知对齐"多智能体交互的框架，增强了机器人系统在人类高心理负荷与高投入状态下，根据情境将通信延迟至智能体系统用户的能力。我们介绍了一种闭环架构的设计与实现，该架构探索了自主任务执行与实时神经生理学专注度之间的相互作用。通过使用消费级脑机接口（BCI），我们的方法在人类执行引发投入度的任务时，持续监测脑电图（EEG）频谱频带功率。我们提出了一种基于投入度的处理流程：当检测到高投入度时，基于HTTP的信令机制将主智能体的感官输入和音频输出置于保持状态，使次级智能体能够在后台无缝处理复杂的委托任务。一旦人类认知状态恢复至较低认知负荷基线，主智能体便会释放队列中的智能体消息。初步结果证明了利用实时信号处理、大语言模型（LLMs）和物理机器人实体构建认知感知、非侵入式多智能体系统的可行性。

---

