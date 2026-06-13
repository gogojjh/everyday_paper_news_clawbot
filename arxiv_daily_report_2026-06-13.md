# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-06-13 08:02

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 7/20 篇提供

**🌟 Highlight**: 20 篇 | **📌 Poster**: 0 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. Mana: Dexterous Manipulation of Articulated Tools

- **作者**: Zhao-Heng Yin, Guanya Shi, Pieter Abbeel, C. Karen Liu ⭐
  - **高亮作者**: Guanya Shi
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.13677v1)
- **发表日期**: 2026-06-11
- **匹配关键词**: affordance, tool use, motion planning
- **arXiv**: [2606.13677v1](http://arxiv.org/abs/2606.13677v1)
- **📥 PDF**: 已下载至本地 (`2606.13677v1_Mana_Dexterous_Manipulation_of_Articulated_Tools.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 铰接式工具操作仍是灵巧机器人领域的一项重大挑战，原因在于需要协调内部自由度与密集接触的交互过程。尽管先前的研究主要聚焦于刚性物体，但铰接式工具的使用因其物理复杂性以及功能性抓取与操作策略的学习难度而尚未得到充分探索。我们提出Mana（操控动画师）——一种通用的仿真到现实框架，将灵巧操作重新诠释为动画问题。受计算机动画启发，Mana采用从粗到细的流水线，通过运动规划与强化学习将程序化生成的抓取关键帧转化为操作轨迹。数据生成过程基本实现自动化，仅需数次鼠标点击即可指定功能可供性（每个工具耗时不足1分钟）。在涵盖不同尺度与关节类型的四种铰接式工具上，Mana实现了抓取与手内操作的零样本仿真到现实迁移，为灵巧铰接式工具使用提供了一种可扩展的方法。

---

### 2. LabVLA: Grounding Vision-Language-Action Models in Scientific Laboratories

- **作者**: Baochang Ren, Xinjie Liu, Xi Chen, Yanshuo Liu, Chenxi Li, Daqi Gao, Zeqin Su, Jintao Xing, Zirui Xue, Rui Li, Xiangyu Zhao, Shuofei Qiao, Minting Pan, Wangmeng Zuo, Lei Bai, Dongzhan Zhou, Ningyu Zhang, Huajun Chen
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.13578v1)
- **发表日期**: 2026-06-11
- **匹配关键词**: VLA, vision-language-action model, vision-language-action
- **arXiv**: [2606.13578v1](http://arxiv.org/abs/2606.13578v1)
- **📥 PDF**: 已下载至本地 (`2606.13578v1_LabVLA_Grounding_Vision-Language-Action_Models_in_Scientific_Laboratories.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 科学实验室日益依赖AI系统来推理实验过程，但实验的物理操作仍大多超出其能力范围。AI可辅助文献阅读、假设生成与方案规划，然而在实验台上执行这些方案仍需人类操作员。视觉-语言-动作（VLA）模型为书面方案与机器人执行之间提供了潜在接口，但现有策略主要基于家庭和桌面场景的演示训练，极少涉及科学实验室中的仪器、透明液体或固定实验流程。弥合这一差距既需要实验室专属的监督数据，也需要能适配执行实验方案所需多种机器人形态的统一学习框架。因此，我们确定数据和机器人形态与模型设计并列为关键瓶颈。为解决数据问题，我们构建了RoboGenesis——一个基于仿真的工作流与数据引擎，可将配置好的实验室工作流分解为原子技能，验证并筛选执行结果，最终为支持的机器人配置导出结构化演示。在策略层面，我们提出LabVLA模型，采用两阶段训练方案：首先通过FAST动作标记预训练，使Qwen3-VL-4B-Instruct骨干网络在学习连续控制前具备动作感知能力；随后在知识隔离条件下，通过流匹配后训练附加DiT动作专家模块。在LabUtopia基准测试中，LabVLA在分布内与分布外场景下均取得了所有评估基线中最高的平均成功率。

---

### 3. NavWAM: A Navigation World Action Model for Goal-Conditioned Visual Navigation

- **作者**: Daichi Azuma, Taiki Miyanishi, Koya Sakamoto, Shuhei Kurita, Yaonan Zhu, Petr Khrapchenkov, Motoaki Kawanabe, Yusuke Iwasawa, Yutaka Matsuo
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.13494v1)
- **发表日期**: 2026-06-11
- **匹配关键词**: image-goal navigation, visual navigation, navigation
- **arXiv**: [2606.13494v1](http://arxiv.org/abs/2606.13494v1)
- **📥 PDF**: 已下载至本地 (`2606.13494v1_NavWAM_A_Navigation_World_Action_Model_for_Goal-Conditioned_Visual_Navigation.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://dachii-azm.github.io/navwam/
- **中文摘要**: 目标条件视觉导航要求机器人在部分可观测条件下行动，通过预测自身运动如何改变未来的自我中心视角，以及这种改变是否使其更接近目标。导航世界模型提供了此类视觉前瞻能力，但它们仍是预测模块，需要外部规划器将预测的未来转化为闭环控制。我们提出导航世界动作模型（NavWAM），这是一种扩散变换器策略，通过将未来观测、目标进度值和动作片段编码到共享潜在序列中，将导航世界模型的预测转化为可执行动作。通过联合学习未来预测与决定闭环行为的动作及价值目标，NavWAM使视觉前瞻可直接用于机器人控制。我们通过仿真预训练和真实机器人自适应构建NavWAM，并在图像目标导航任务中，将其与基于规划的世界模型及代表性直接导航策略进行对比评估。在离线基准测试和真实机器人闭环部署中，NavWAM在默认策略模式（无需CEM式动作搜索）下，相较于基于规划的世界模型基线取得了更优表现。项目页面：https://dachii-azm.github.io/navwam/

---

### 4. GIVE: Grounding Human Gestures in Vision-Language-Action Models

- **作者**: Pengfei Liu, Gen Li, Junqiao Fan, Boyu Ma, Jindou Jia, Yang Xiao, Jianfei Yang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.13435v1)
- **发表日期**: 2026-06-11
- **匹配关键词**: human-robot interaction, vision-language-action model, vision-language-action, HRI, VLA
- **arXiv**: [2606.13435v1](http://arxiv.org/abs/2606.13435v1)
- **📥 PDF**: 已下载至本地 (`2606.13435v1_GIVE_Grounding_Human_Gestures_in_Vision-Language-Action_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 人类交流本质上具有多模态特性，语言常伴随手势等非语言线索来传递意图。然而，当前的视觉-语言-动作（VLA）模型将机器人操作视为纯文本驱动的任务，忽视了手势在人机交互（HRI）中的重要作用。当语言指令模糊或信息不足时，这常导致意图定位不准确和操作不可靠。为解决这一挑战，我们提出GIVE（通过视觉-语义增强的手势意图）方法，这是一种无需修改架构即可增强预训练VLA模型人类手势理解能力的有效方案。具体而言，GIVE通过两条互补路径整合手势信息：视觉路径将手部骨架和指尖射线叠加到机器人观测数据上实现显式目标定位，语义路径则生成人类手势与任务指令的高层描述以实现鲁棒的意图定位。通过联合利用视觉与语义引导，GIVE使VLA策略能更好地将手势与操作行为关联，并适应动态交互意图。在真实人机交互实验中，GIVE显著超越基线模型，目标物体识别准确率提升40%，整体任务成功率提升80%，同时展现出对未见空间布局和不同参与者的强大鲁棒性与泛化能力。

---

### 5. See Selectively, Act Adaptively: Dual-Level Structural Decomposition for Bimanual Robot Manipulation

- **作者**: Yoon-Ji Choi, Young-Chae Son, Soo-Chul Lim
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.13279v1)
- **发表日期**: 2026-06-11
- **匹配关键词**: bimanual manipulation, vision-language-action, VLA
- **arXiv**: [2606.13279v1](http://arxiv.org/abs/2606.13279v1)
- **📥 PDF**: 已下载至本地 (`2606.13279v1_See_Selectively,_Act_Adaptively_Dual-Level_Structural_Decomposition_for_Bimanual_Robot_Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 在双臂机器人操作中，任务相关的视觉信息会随任务阶段和情境动态变化，而双臂的交互模式则在独立与协同状态之间切换，这使得策略学习极具挑战性。然而，现有的一体化视觉-语言-动作（VLA）策略通过单一共享表征和动作生成通路处理多样化的视觉输入与交互模式，往往无法分别考虑视觉相关性和双臂交互结构。为解决这一问题，我们提出了一种基于双层结构分解的双臂操作VLA框架。其中，视图选择性视觉路由器通过动态调整腕部视角的贡献度来突出相关视觉线索，而交互感知动作混合专家（MoE）则将动作生成分解为协同通路与单臂通路，以适应不同的双臂交互模式。我们在RoboTwin 2.0的六项模拟双臂操作任务和三项长时域真实世界任务上评估了该方法。与一体化基线相比，我们的模型在模拟环境中将整体平均成功率提升了27.7%，在真实世界评估中提升了43.3%，并且在两种场景下均持续优于单模块变体。这些结果表明，联合考虑选择性视觉处理与双臂交互结构的显式分解，为鲁棒的双臂操作提供了有效的归纳偏置。

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
- **中文摘要**: 全身型人形机器人操控笨重、可变形及共享负载物体时，需要分布式接触感知与显式力调节能力，但现有模仿策略大多仅隐式处理接触力。另一方面，不同示教源提供的互补模态存在固有权衡：人类示教能捕捉自然接触力却无法生成机器人可执行动作，而遥操作虽可直接记录机器人动作，但力调节的自然性较弱。本文提出\textbf{WT-UMI}——一种可穿戴全身触觉接口，可由人类操作者佩戴或安装于人形机器人上，在人类示教与人形机器人遥操作两种模式下，提供触觉图像、接触力及末端执行器位姿的精确观测。我们引入力条件目标位姿修正模块，通过从遥操作数据中学习修正量，将测量到的人类位姿转换为接触感知的机器人目标。为利用人类数据中的自然力交互特性，我们提出力监督规划器，可预测末端执行器位姿片段与接触力轨迹。预测的接触力作为基于触觉的导纳控制器的参考输入。在涵盖可变形物体、笨重刚体及人-人形机器人协作的五类接触密集型任务中，WT-UMI相较于四种策略基线，在提升成功率的同时降低了接触位置跟踪误差。项目页面详见https://wt-umi.github.io/WTUMI/。

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
- **中文摘要**: 区分自我与他人是社会智能的前提，然而与人类共享工作空间的人形机器人仍缺乏这种能力。本研究展示了一种方法：人形机器人可通过本体感觉-视觉对应关系学习自我与他人的区分，无需任何身份标签或运动学模型。一旦建立这种区分能力，即可引导出预测性自我模型——该模型将关节构型映射至三维身体占用空间，捕捉机器人身体随动作变化的规律。在涉及人类或形态相同机器人的多智能体场景中，该系统能可靠识别自身、学习三维自我模型，并支持目标抓取、碰撞感知运动规划、人体到机器人运动重定向等下游任务。这些成果共同勾勒出一条路径，使机器人在共享物理空间中与同伴协同行动时，能够建立身体自我表征。项目页面：https://euron-zc.github.io/humanoid-self-model/

---

### 8. Y-BotFrame: An Extensible Embodied Agent Framework for Quadruped Robot Assistants

- **作者**: Luyao Zhang, Ke Li, Yuan Ding, Xulong Zhao, Guo Yu, Chengwei Yan, Fuyu Dong, Jiawei Hu, Di Wang, Nan Luo, Gang Liu, Quan Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.13049v1)
- **发表日期**: 2026-06-11
- **匹配关键词**: visual feedback, human-robot collaboration, navigation
- **arXiv**: [2606.13049v1](http://arxiv.org/abs/2606.13049v1)
- **📥 PDF**: 已下载至本地 (`2606.13049v1_Y-BotFrame_An_Extensible_Embodied_Agent_Framework_for_Quadruped_Robot_Assistants.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 四足机器人具备在多种复杂地形中灵活运动的能力。作为高机动性的地面智能平台，它们可搭载导航控制、环境感知与智能交互模块，成为各类算法的实体移动部署载体。本文提出Y-BotFrame可扩展具身平台，将机器人转化为智能地面助手。该平台集成语音、视觉与激光雷达等多模态感知能力，以大型语言模型作为认知核心，实现环境理解、上下文推理与任务规划。系统将用户自然语言指令映射为机器人可执行的具身任务单元。Y-BotFrame支持通过语音指令与视觉反馈进行自然交互，无需遥控器即可实现高效人机协作。凭借高度可扩展的框架，该平台支持新功能模块的即插即用集成，以及模块化升级与迭代开发，为通用型指令驱动具身智能体的实际部署提供了参考实现。补充视频见https://xdei-group.github.io/Y-BotFrame/。

---

### 9. Trajectory-Level Redirection Attacks on Vision-Language-Action Models

- **作者**: Gokul Puthumanaillam, Vardhan Dongre, Pranay Thangeda, Hooshang Nayyeri, Dilek Hakkani-Tür, Melkior Ornik
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.12978v1)
- **发表日期**: 2026-06-11
- **匹配关键词**: VLA, vision-language-action model, vision-language-action
- **arXiv**: [2606.12978v1](http://arxiv.org/abs/2606.12978v1)
- **📥 PDF**: 已下载至本地 (`2606.12978v1_Trajectory-Level_Redirection_Attacks_on_Vision-Language-Action_Models.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://vla-redirection-attack.github.io/
- **中文摘要**: 视觉-语言-动作（VLA）策略将自然语言引入闭环机器人控制，使机器人能够直接根据文本指令执行操作任务。由于提示在每个重新规划步骤中都会被重复使用，且每个提示条件化的动作都会改变策略所作用的未来观测结果，因此这一接口赋予了文本在控制中的持续性作用。现有VLA攻击研究主要关注能够引发目标低级动作或使此类动作在变化图像中持续存在的对抗性提示。我们识别出一种更强的轨迹级故障模式：即提示表面上仍指定了预期任务，但实际却改变了最终物理结果。我们通过数学形式化将该场景定义为**命令保持型轨迹重定向**，这是一种仅涉及提示的威胁模型，其中攻击者在回合开始前选择一个提示，所有策略与环境组件保持固定，且提示必须接近良性指令，同时省略目标词汇与纠正性语言。为寻找此类提示，我们提出了一种基于策略的提示搜索方法，该方法利用轨迹展开发现满足命令保持约束、且闭环行为追踪目标任务的扰动。仿真与硬件实验表明，接近良性的提示扰动能够将VLA轨迹展开重定向至攻击者指定的目标。这些结果揭示了VLA指令理解中的轨迹级漏洞：表面上保留预期命令的文本仍可能使攻击者控制机器人的最终物理结果。项目网站：https://vla-redirection-attack.github.io/

---

### 10. SERF: Spatiotemporal Environment and Robot Feature Map for Long-Horizon Mobile Manipulation

- **作者**: Sunghwan Kim, Byeonghyun Pak, Kehan Long, Yulun Tian, Nikolay Atanasov
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.12956v1)
- **发表日期**: 2026-06-11
- **匹配关键词**: VLA, mobile manipulation, vision-language-action
- **arXiv**: [2606.12956v1](http://arxiv.org/abs/2606.12956v1)
- **📥 PDF**: 已下载至本地 (`2606.12956v1_SERF_Spatiotemporal_Environment_and_Robot_Feature_Map_for_Long-Horizon_Mobile_Manipulation.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 长时域机器人移动操作需要对定位、环境变化及任务进展进行持续推理，而这些信息仅从图像观测中推断极具挑战性。本文证明，将移动操作策略与时空特征图相结合能够提升长时域推理能力。该特征图将环境与可动机械臂本体表示为共享潜在空间中的神经点，并通过自我中心观测与本体感知状态进行在线更新。我们利用物体级刚性追踪更新环境神经点，通过正向运动学更新机器人神经点。通过从多参考帧与多空间尺度提取特征图标记，我们将所提出的时空环境与机器人特征（SERF）图作为状态输入至视觉-语言-动作（VLA）模型，为策略提供局部与全局上下文信息。我们在家庭环境长时域移动操作基准BEHAVIOR-1K上验证了SERF方法。实验表明，SERF VLA策略优于纯图像基线，能通过更直接的轨迹更快达成子目标，提升对场景配置变化的鲁棒性，并能从物体掉落故障中恢复。

---

### 11. An Embodied Simulation Platform, Benchmark, and Data-Efficient Augmentation Framework for Wet-Lab Robotics

- **作者**: Zhe Liu, Huanbo Jin, Zhaohui Du, Zhe Wang, He Xu, Peijia Li, Jiaming Gu, Quan Lu, Qi Wang, Bin Ji, Ting Xiao
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.12936v1)
- **发表日期**: 2026-06-11
- **匹配关键词**: VLA
- **arXiv**: [2606.12936v1](http://arxiv.org/abs/2606.12936v1)
- **📥 PDF**: 已下载至本地 (`2606.12936v1_An_Embodied_Simulation_Platform,_Benchmark,_and_Data-Efficient_Augmentation_Framework_for_Wet-Lab_Ro.pdf`)
- **🔓 开源**: CODE
- **中文摘要**: 湿实验室机器人能够提升生物医学实验的可重复性、通量及安全性，但扩展其学习能力需要可定制的模拟器以生成安全且可重复的任务、开放可编辑的实验室资产，以及能将有限示范转化为可用训练数据的高效流水线。我们提出Pipette——一个面向湿实验室机器人学习的具身模拟平台、基准测试及数据高效增强框架。Pipette发布了超过43个开源且可重新编辑的湿实验室资产，并配套可扩展的资产构建流水线。其核心组件是基于模拟的数据增强流水线：在模拟环境中回放人类示范，施加光照、相机视角、速度及动作扰动，并通过自动任务成功检测过滤生成的片段，从而从有限的人工示范中快速扩展可用训练数据。我们进一步引入包含11项任务的湿实验室具身基准测试，涵盖样品处理、培养器具操作、设备操作及精准放置。在每项任务仅30次示范的条件下，ACT方法达到65.5%的平均成功率，而模拟增强将SmolVLA从44.1%提升至74.7%，π0从40.4%提升至46.5%，验证了Pipette在数据高效VLA训练与评估中的有效性。此外，Pipette支持自然语言驱动的场景构建与任务注册，降低了非专家用户定义新型湿实验室机器人任务的门槛。

---

### 12. AIR-VLA+: Decoupling Movement and Manipulation via Cascaded Dual-Action Decoders with Asymmetric MoE for Aerial Robots

- **作者**: Jianli Sun, Bin Tian, Qiyao Zhang, Zijian Liu, Yutong Wang, Zhiyong Cui, Bai Li, Yisheng Lv, Yonglin Tian
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.12859v1)
- **发表日期**: 2026-06-11
- **匹配关键词**: VLA
- **arXiv**: [2606.12859v1](http://arxiv.org/abs/2606.12859v1)
- **📥 PDF**: 已下载至本地 (`2606.12859v1_AIR-VLA+_Decoupling_Movement_and_Manipulation_via_Cascaded_Dual-Action_Decoders_with_Asymmetric_MoE_.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 空中操控系统长期以来一直受限于端到端控制中的表征耦合问题，因为平台级无人机（UAV）运动与末端执行器级机械臂操作在动作尺度、动力学特性和控制目标上存在显著差异。本文提出AIR-VLA+——一种专为空中操控设计的流匹配动作生成架构，其核心创新包括级联双动作解码器与非对称特征级混合专家（MoE）模块。我们构建了级联的操控与运动解码器，使无人机在运动过程中能够单向观测机械臂的意图以实现工作流协调，同时隔离无人机运动信息反向传播对机械臂操控稳定性的影响。针对无人机运动高度依赖高层语义且负责空中操控任务状态转换的特性，我们为无人机运动解码器设计了输入特征增强模块：通过引入隐式视觉抓取投影器感知夹爪与物体的交互状态，并注入压缩后的全局语义特征。在无人机运动解码器内部，我们部署了隐式MoE架构，使不同运动专家在训练过程中自发形成对不同任务阶段的能力倾向。通过在特征流形上进行密集软混合计算，无人机运动获得了更强的任务阶段适应性。在标准化AIR-VLA基准测试上的实验表明，本方法以48.0的总体平均分全面超越所有基线方法，整体任务完成分数较单头$π_{0.5}$策略提升80.2%，有效缓解了复合机器人的异构协调控制冲突。

---

### 13. Stubborn: A Streamlined and Unified Reinforcement Learning Framework for Robust Motion Tracking and Fall Recovery for Humanoids

- **作者**: Xiao Ren, Yuhui Yang, Zongbiao Weng, Zhijie Liu, He Kong
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.12814v1)
- **发表日期**: 2026-06-11
- **匹配关键词**: exploration
- **arXiv**: [2606.12814v1](http://arxiv.org/abs/2606.12814v1)
- **📥 PDF**: 已下载至本地 (`2606.12814v1_Stubborn_A_Streamlined_and_Unified_Reinforcement_Learning_Framework_for_Robust_Motion_Tracking_and_F.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 近期强化学习方法在提升人形机器人运动跟踪性能及实现扰动下的跌倒恢复方面展现出巨大潜力。然而，现有研究大多将运动跟踪与跌倒恢复视为不同任务，需要多阶段训练并配备专门的恢复奖励函数和/或独立恢复策略。此外，现有基于强化学习的方法常在严重跟踪失败后立即终止训练回合，限制了在失稳或跌倒状态下的恢复导向探索。针对上述问题，我们提出Stubborn——一个精简统一的强化学习框架，用于实现鲁棒的人形机器人运动跟踪与跌倒恢复。具体而言，Stubborn采用非对称Actor-Critic架构，包含三个核心组件：首先，采用偏航对齐的跟踪表征，在保留重力相关平衡信息的同时降低对全局漂移和航向扰动的敏感性；其次，引入基于伯努利分布的概率终止机制，使策略能够鼓励在不同失效模式下探索跌倒恢复行为；最后，提出概率终止与跟踪误差驱动的策略，根据跟踪性能动态重塑采样分布，提升困难运动片段与失稳状态的训练效率。与当前最优方法的全面对比及消融实验表明，Stubborn取得了具有竞争力的性能，所提出的概率终止机制与自适应采样策略对性能提升和鲁棒性增强均有贡献。真实世界演示请参见https://aislab-sustech.github.io/Stubborn/。

---

### 14. M*: A Modular, Extensible, Serving System for Multimodal Models

- **作者**: Atindra Jha, Naomi Sagan, Keisuke Kamahori, Irmak Sivgin, Rohan Sanda, Steven Gao, Mark Horowitz, Luke Zettlemoyer, Olivia Hsu, Jure Leskovec, Baris Kasikci, Stephanie Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.12688v1)
- **发表日期**: 2026-06-10
- **匹配关键词**: vision-language-action
- **arXiv**: [2606.12688v1](http://arxiv.org/abs/2606.12688v1)
- **📥 PDF**: 已下载至本地 (`2606.12688v1_M_A_Modular,_Extensible,_Serving_System_for_Multimodal_Models.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 我们正步入复合模型架构的新时代，这类架构整合了视觉编码器、语言主干网络、扩散与流式处理头、音频编解码器、动作生成器以及世界模型预测器等多样化组件。此类架构支撑着广泛的多模态模型，包括统一多模态模型、全能模型、语音-语言模型、视觉-语言-动作策略及世界模型。然而，现有模型服务框架基于对模型结构的狭隘假设构建，难以适应这种新型架构的多样性。本文提出M*——一个面向复合AI模型高效服务的通用服务系统。M*将模型表示为数据流图，通过遍历这些图来处理跨模态与跨任务的请求。其核心创新在于模块化抽象：支持模型组件的任意组合、物理集群的灵活部署，以及分布式运行时中与模型无关的优化。我们将此抽象称为"行走图"，并展示其如何简洁地捕获来自广泛模型家族的复合模型。我们在代表性模型上实现M*，发现其在BAGEL模型上处理文本到图像任务时，端到端延迟平均比vLLM-Omni降低20%；在Qwen3-Omni模型上处理文本到语音任务时，实时因子降低达2.9倍，吞吐量提升达2.7倍。在机器人规划任务中，M*相比V-JEPA 2-AC rollout基线性能提升达12.5倍。因此，本研究为以最小开发成本高效服务复杂模型铺平了道路。

---

### 15. World Pilot: Steering Vision-Language-Action Models with World-Action Priors

- **作者**: Zefu Lin, Rongxu Cui, Junjia Xu, Xiaojuan Jin, Wenling Li, Lue Fan, Zhaoxiang Zhang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.12403v1)
- **发表日期**: 2026-06-10
- **匹配关键词**: VLA, vision-language-action model, vision-language-action
- **arXiv**: [2606.12403v1](http://arxiv.org/abs/2606.12403v1)
- **📥 PDF**: 已下载至本地 (`2606.12403v1_World_Pilot_Steering_Vision-Language-Action_Models_with_World-Action_Priors.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://world-pilot.github.io/
- **中文摘要**: 视觉-语言-动作（VLA）模型继承自大规模预训练的语义基础，并在分布内操作任务中表现出色。然而，这种语义基础建立在静态图像-文本对之上，而操作是一个连续的、高接触过程，其动态特性无法通过此类预训练捕捉。我们提出World Pilot，一种VLA框架，通过世界-动作模型（WAM）的先验知识增强策略，并通过两条互补路径将其引入决策链。潜在引导通过场景演化潜在变量调节感知层，动作引导则提供预期轨迹作为动作生成器的运动先验。这两类先验共同赋予VLA对场景的预期视角、轨迹级运动提示及其语义条件，且即使由未经动作后训练的视频预训练世界模型提供，场景演化先验依然有效。World Pilot在LIBERO-Plus零样本OOD基准测试中达到84.7%的最优总成功率，并在四项操作任务的所有真实机器人设置中取得最高成功率，在视角、几何、可变形状态和姿态变化场景下优势最为显著。项目网站：https://world-pilot.github.io/

---

### 16. DIRECT: When and Where Should You Allocate Test-Time Compute in Embodied Planners?

- **作者**: Jadelynn Dao, Milan Ganai, Yasmina Abukhadra, Ajay Sridhar, Mozhgan Nasr Azadani, Katie Luo, Clark Barrett, Jiajun Wu, Chelsea Finn, Marco Pavone ⭐
  - **高亮作者**: Chelsea Finn
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.12402v1)
- **发表日期**: 2026-06-10
- **匹配关键词**: VLA
- **arXiv**: [2606.12402v1](http://arxiv.org/abs/2606.12402v1)
- **📥 PDF**: 已下载至本地 (`2606.12402v1_DIRECT_When_and_Where_Should_You_Allocate_Test-Time_Compute_in_Embodied_Planners?.pdf`)
- **🔓 开源**: PROJECT_PAGE
- **中文摘要**: 视觉-语言模型（VLMs）正越来越多地被部署为具身智能体的高层规划器，其中一种新兴策略是通过扩展测试时计算量来提升模型能力。然而，我们观察到这种做法会增加延迟、令牌消耗和浮点运算次数，同时在下游任务成功率上产生不均衡且往往递减的收益，从而限制了具身智能体的部署场景。我们认为，选择何时何地投入测试时计算资源，是将前沿性能带入现实世界的关键。为此，我们提出DIRECT框架——一种利用多模态场景上下文为每个提示词分配计算资源的路由框架，相较于固定模型选择策略，该框架能优化成功率-成本帕累托前沿。在链式思维深度、模型规模和记忆历史这三个主要扩展维度上，我们在VLABench和RoboMME上的实验表明：测试时计算并非均匀的杠杆——不同维度会产生性质迥异的能力增益。我们在DROID设置中的物理Franka机械臂上验证了这些发现，涵盖零样本操作和长时序链式任务，其中我们的路由系统在平均延迟降低高达65%的情况下，仍能匹配甚至超越更强模型的成功率。最终结果表明，简单粗暴地扩展测试时计算是低效的，而DIRECT能以极低的成本在机器人系统中实现前沿水平的具身规划能力。项目页面详见 jadee-dao.github.io/direct/。

---

### 17. Flex4DHuman: Flexible Multi-view Video Diffusion for 4D Human Reconstruction

- **作者**: Jen-Hao Cheng, Yipeng Wang, Hao Zhang, Gengshan Yang, Jenq-Neng Hwang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.13655v1)
- **发表日期**: 2026-06-11
- **匹配关键词**: gaussian splatting
- **arXiv**: [2606.13655v1](http://arxiv.org/abs/2606.13655v1)
- **📥 PDF**: 已下载至本地 (`2606.13655v1_Flex4DHuman_Flexible_Multi-view_Video_Diffusion_for_4D_Human_Reconstruction.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出Flex4DHuman——一种多视角视频扩散模型，能够将动态主体的单目或稀疏多视角视频，仅通过相对相机姿态条件，转化为同步的密集多视角视频。与以往依赖骨架、深度图、法线或渲染目标视角几何的人体中心方法不同，Flex4DHuman无需显式几何先验，而是通过相对相机姿态位置编码来引导生成。生成的视频可直接输入下游重建流程，用于创建动态4D高斯溅射模型。该模型基于Wan 2.1 1.3B文本生成视频模型构建，保留了骨干网络架构，并通过五轴位置编码（在时空RoPE基础上扩展视角索引和连续SE(3)相对相机几何）对相机和视角信息进行编码。采用三阶段课程学习策略，逐步训练模型实现姿态跟随、灵活参考到目标视角生成以及时间展开。为支持时间展开，我们使用干净的历史目标视角令牌进行训练，并添加多视角字幕以实现测试时的文本控制。结合现成的4D高斯溅射阶段，我们的框架可将单目静态相机视频提升为动态4D高斯溅射。在DNA-Rendering和ActorsHQ上的实验表明，Flex4DHuman超越了先前最先进的方法，而相同的公式在混合人体-动物训练后可泛化至动物类别。这些能力使Flex4DHuman成为从随意拍摄的单目视频实现可扩展4D内容创作（用于仿真、游戏、AR/VR及视频重拍）的实用一步。

---

### 18. Real-Time Execution with Autoregressive Policies

- **作者**: Sangkyu Lee, Seohyeon Park, Tackgeun You, Avi Caciularu, Idan Szpektor, Hwasup Lim, Youngjae Yu
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.13355v1)
- **发表日期**: 2026-06-11
- **匹配关键词**: vision-language-action model, vision-language-action
- **arXiv**: [2606.13355v1](http://arxiv.org/abs/2606.13355v1)
- **📥 PDF**: 已下载至本地 (`2606.13355v1_Real-Time_Execution_with_Autoregressive_Policies.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 通过异步推理实现的实时执行，既能确保平滑的动作轨迹，又能保证快速响应能力，这对于大规模视觉-语言-动作模型的实际部署至关重要。然而，近期关于实时执行的研究主要聚焦于扩散策略的变体，尽管自回归策略在同步推理中因推出速度较慢而更需要实时性支持。相比之下，我们证明自回归策略可通过调整分词范围并应用约束解码来实现实时执行，从而保证严格的延迟上限，进而支持多轨迹解码以最大化性能。在模拟和真实环境实验中，我们发现自回归策略始终优于同等水平的流匹配策略，同时通过同步推理显著提升了任务完成速度。结合自回归策略在指令跟随方面收敛更快、泛化性更佳等固有优势，这些结果证实自回归策略仍可成为支持实时执行的竞争性策略类型。

---

### 19. Embodied-BenchClaw: An Autonomous Multi-Agent System for Embodied Spatial Intelligence Benchmark Construction

- **作者**: Baoyang Jiang, Fengchun Zhang, Leyuan Wang, Haotian Li, Yida Wang, Zhe Ji, Jinshan Lai, Xi Ren, Jianwei Hu, Qiang Ma
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.11909v1)
- **发表日期**: 2026-06-10
- **匹配关键词**: robot navigation, navigation
- **arXiv**: [2606.11909v1](http://arxiv.org/abs/2606.11909v1)
- **📥 PDF**: 已下载至本地 (`2606.11909v1_Embodied-BenchClaw_An_Autonomous_Multi-Agent_System_for_Embodied_Spatial_Intelligence_Benchmark_Cons.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 基准测试对于评估具身空间智能至关重要，但其构建过程劳动密集、难以复用且维护困难。现有具身基准测试通常具有静态性，随着模型性能提升可能迅速饱和，从而限制其区分新能力的作用。我们提出Embodied-BenchClaw——一个用于构建具身空间智能基准测试的自主智能体系统。给定用户指定的评估意图，Embodied-BenchClaw通过五个阶段流水线自动生成完整且可持续更新的基准测试包：意图蓝图设计、数据采集、结构化与清洗、基准合成以及评估报告。该流水线由三个智能体协同完成规划、构建和评估任务。为提升可复用性与可靠性，Embodied-BenchClaw引入了可扩展的技能库与流程质量控制机制，使基准测试构建具备可组合、可验证和可修复特性。我们实例化了多个基准测试，涵盖室内空间推理、室外空间推理、机器人操作、四足机器人导航、无人机/航拍视角理解以及静态基准增强。这些基准测试跨越了多样化的具身载体、数据源和空间能力。通过人工评估、裁判模型评估、一致性检验、成本分析和消融实验，结果表明Embodied-BenchClaw能够以更少人工投入构建可验证、可执行、可维护且具有诊断价值的具身空间基准测试。

---

### 20. SAFER-Nav: Enhancing Safety for Visual Robot Navigation via Segmentation-Aware Fine-Tuning

- **作者**: Geonyeong Ko, Giung Lee, Changjoo Nam
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2606.11636v1)
- **发表日期**: 2026-06-10
- **匹配关键词**: robot navigation, navigation
- **arXiv**: [2606.11636v1](http://arxiv.org/abs/2606.11636v1)
- **📥 PDF**: 已下载至本地 (`2606.11636v1_SAFER-Nav_Enhancing_Safety_for_Visual_Robot_Navigation_via_Segmentation-Aware_Fine-Tuning.pdf`)
- **🔒 开源**: 未提及
- **中文摘要**: 基于视觉的导航模型，特别是基础模型，能够仅从RGB观测中生成可行的轨迹。然而，即使是最先进的基于Transformer和扩散模型的策略，在包含未知障碍物或条件变化的陌生部署环境中仍难以泛化。由此产生的轨迹往往仍能指向目标，但不够安全。现有研究通过外部轨迹校正或内部几何先验来提升安全性，但所得到的策略并未被训练以显式表示障碍物边界或可通行自由空间结构。为解决这一问题，我们提出了一种导航模型，该模型通过微调将这些结构直接融入策略中，并设计为兼容多种基于RGB的骨干网络。在多种机器人平台、室内环境以及静态与动态障碍物场景中，与ViNT、NoMaD及其CARE增强变体相比，我们的方法在保持目标到达性能的同时，降低了碰撞频率。

---

