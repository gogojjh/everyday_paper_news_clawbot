# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-04-19 08:03

**今日新增**: 10 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 3/10 篇提供

**🌟 Highlight**: 2 篇 | **📌 Poster**: 8 篇

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. CAVERS: Multimodal SLAM Data from a Natural Karstic Cave with Ground Truth Motion Capture

- **作者**: Giacomo Franchini, David Rodríguez-Martínez, Alfonso Martínez-Petersen, C. J. Pérez-del-Pulgar, Marcello Chiaberge
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.15052v1)
- **发表日期**: 2026-04-16
- **匹配关键词**: navigation, 3d reconstruction, 3D reconstruction
- **arXiv**: [2604.15052v1](http://arxiv.org/abs/2604.15052v1)
- **📥 PDF**: 已下载至本地 (`2604.15052v1_CAVERS_Multimodal_SLAM_Data_from_a_Natural_Karstic_Cave_with_Ground_Truth_Motion_Capture.pdf`)
- **🔓 开源**: CODE, GITHUB
  - 链接：https://github.com/spaceuma/cavers.
- **中文摘要**: 在天然喀斯特洞穴中运行的自主机器人面临着与矿井或隧道环境截然不同的感知与导航挑战：不规则几何结构、反光的潮湿表面、近乎零的环境光照以及复杂的分支通道。然而，针对此类环境的公开数据集仍然稀缺，且现有数据集的传感模式和环境多样性有限。我们提出了CAVERS多模态数据集，该数据集采集自西班牙马拉加维多利亚洞穴中两个结构迥异的洞室，包含24组序列总计约335GB的记录数据。传感器套件整合了英特尔RealSense D435i RGB-D-I相机、Optris PI640i近红外热成像相机和Velodyne VLP-16激光雷达，分别在完全黑暗和人工照明条件下以手持方式及轮式移动平台搭载方式运行。针对大多数序列，我们通过直接安装在洞穴内的Optirack运动捕捉系统提供了毫米级精度的120Hz六自由度位姿真值与速度数据。我们测试了涵盖视觉、视觉-惯性、热成像-惯性及激光雷达七种前沿SLAM与里程计算法，并展示了三维重建流程，验证了该数据集的实用性。

---

### 2. GlobalSplat: Efficient Feed-Forward 3D Gaussian Splatting via Global Scene Tokens

- **作者**: Roni Itkin, Noam Issachar, Yehonatan Keypur, Yehonatan Keypur, Anpei Chen, Sagie Benaim
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.15284v1)
- **发表日期**: 2026-04-16
- **匹配关键词**: gaussian splatting, 3D gaussian splatting
- **arXiv**: [2604.15284v1](http://arxiv.org/abs/2604.15284v1)
- **📥 PDF**: 已下载至本地 (`2604.15284v1_GlobalSplat_Efficient_Feed-Forward_3D_Gaussian_Splatting_via_Global_Scene_Tokens.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://r-itk.github.io/globalsplat/
- **中文摘要**: 高效的空间基元分配是3D高斯泼溅技术的基础，它直接决定了表示紧凑性、重建速度与渲染保真度之间的协同关系。现有解决方案无论是基于迭代优化还是前馈推理，都难以在这些目标间取得平衡，主要因其依赖缺乏全局场景感知的局部启发式分配策略。具体而言，当前前馈方法大多采用像素对齐或体素对齐方式，通过将像素反投影为密集的视角对齐基元，导致三维资产中嵌入冗余信息。随着输入视角的增加，表示规模会持续膨胀，全局一致性也变得脆弱。为此，我们提出GlobalSplat框架，其核心设计理念是“先对齐，后解码”。该方法通过学习紧凑的全局潜在场景表示，在解码任何显式三维几何结构之前，先对多视角输入进行编码并解析跨视角对应关系。这种设计的关键优势在于，无需依赖预训练的像素预测主干网络或复用密集基线的潜在特征，即可实现紧凑且全局一致的重建效果。通过采用从粗到精的训练策略逐步提升解码能力，GlobalSplat从根本上避免了表示膨胀问题。在RealEstate10K和ACID数据集上的实验表明，我们的模型仅需1.6万个高斯单元即可实现具有竞争力的新视角合成效果，显著少于密集处理流程的需求量，最终获得仅4MB的轻量化存储占用。此外，GlobalSplat在单次前向传播中仅需78毫秒，推理速度显著超越基线方法。项目页面详见https://r-itk.github.io/globalsplat/

---

## 📌 Poster

*其他相关研究*

---

### 1. Vision-Based Safe Human-Robot Collaboration with Uncertainty Guarantees

- **作者**: Jakob Thumm, Marian Frei, Tianle Ni, Matthias Althoff, Marco Pavone
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.15221v1)
- **发表日期**: 2026-04-16
- **匹配关键词**: human-robot collaboration
- **arXiv**: [2604.15221v1](http://arxiv.org/abs/2604.15221v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 我们提出了一种基于视觉的人体姿态估计与运动预测框架，该框架通过符合性预测保证实现可认证安全的人机协作。本框架将偶然不确定性估计与分布外检测相结合，以获得高概率置信度。为将我们的流程集成至可认证安全框架中，我们提出了具有高有效置信度的人体运动预测符合性预测集。我们在记录的人体运动数据及真实人机协作场景中对本流程进行了评估。

---

### 2. NEAT-NC: NEAT guided Navigation Cells for Robot Path Planning

- **作者**: Hibatallah Meliani, Khadija Slimani, Samira Khoulji
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.15076v1)
- **发表日期**: 2026-04-16
- **匹配关键词**: path planning, navigation
- **arXiv**: [2604.15076v1](http://arxiv.org/abs/2604.15076v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 为在空间中导航，大脑利用位置细胞、网格细胞、头部方向细胞、边界细胞和速度细胞等多种细胞构建环境的内部表征。这些细胞与感觉输入共同作用，使生物体能够探索周围空间。受这些生物学原理启发，我们开发了NEATNC——一种基于增强拓扑神经进化的导航细胞系统。本文旨在利用空间认知细胞提升NEAT算法在动态环境路径规划中的性能。该方法以导航细胞作为输入，通过演化递归神经网络来模拟大脑海马体功能。我们在静态与动态场景中对所提算法进行了多维度评估。本研究彰显了NEAT算法对复杂多变环境的适应能力，印证了生物学理论的应用价值，表明该方法特别适用于机器人及游戏领域的实时动态路径规划。

---

### 3. DockAnywhere: Data-Efficient Visuomotor Policy Learning for Mobile Manipulation via Novel Demonstration Generation

- **作者**: Ziyu Shan, Yuheng Zhou, Gaoyuan Wu, Ziheng Ji, Zhenyu Wu, Ziwei Wang
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.15023v1)
- **发表日期**: 2026-04-16
- **匹配关键词**: contact-rich manipulation, mobile manipulation
- **arXiv**: [2604.15023v1](http://arxiv.org/abs/2604.15023v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 移动操作是使机器人能够在家庭和工厂等广阔环境中进行交互的基本能力。现有方法大多遵循两阶段范式：机器人首先导航至对接点，随后利用强大的视觉运动策略执行固定基座操作。然而，由于对接点偏移，现实世界中的移动操作常面临视角泛化问题。为解决这一难题，我们提出名为DockAnywhere的新型低成本演示生成框架，通过将单次演示提升至多样可行的对接配置，显著改善对接变化下的视角泛化能力。具体而言，DockAnywhere通过解耦依赖对接的基座运动与跨视角保持不变的密集接触操作技能，将轨迹拓展至任意可行对接点。在可行性约束下采样可行对接方案，并通过结构保持增强生成对应轨迹。通过将机器人与物体表示为点云并实施点级空间编辑，在三维空间中合成视觉观测，确保跨视角观测与行动的一致性。在ManiSkill仿真平台与真实场景中的大量实验表明，DockAnywhere能大幅提升策略成功率，并轻松泛化至训练中未见对接点的新视角，显著增强了移动操作策略在现实部署中的泛化能力。

---

### 4. HRDexDB: A Large-Scale Dataset of Dexterous Human and Robotic Hand Grasps

- **作者**: Jongbin Lim, Taeyun Ha, Mingi Choi, Jisoo Kim, Byungjun Kim, Subin Jeon, Hanbyul Joo
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.14944v1)
- **发表日期**: 2026-04-16
- **匹配关键词**: dexterous grasping
- **arXiv**: [2604.14944v1](http://arxiv.org/abs/2604.14944v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 我们推出HRDexDB——一个大规模、多模态的高精度灵巧抓取序列数据集，涵盖人类与多种机器人手部操作。与现有数据集不同，HRDexDB全面收录了人类手部及多种机器人手型对100种不同物体的抓取轨迹。通过融合前沿视觉技术与新型专用多相机系统，HRDexDB为操作主体与被操控物体提供了高精度时空三维真实运动数据。为促进物理交互研究，该数据集包含高分辨率触觉信号、同步多视角视频及第一人称视角视频流。数据集共收录1.4K次抓取实验（含成功与失败案例），每条数据均涵盖视觉、运动学与触觉多模态信息。通过在同一目标物体上以可比拟的抓取动作实现人类灵巧操作与机器人执行的高度对齐记录，HRDexDB为多模态策略学习与跨领域灵巧操控研究奠定了基准基础。

---

### 5. An Intelligent Robotic and Bio-Digestor Framework for Smart Waste Management

- **作者**: Radhika Khatri, Adit Tewari, Nikhil Sharma, M. B. Srinivas
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.14882v1)
- **发表日期**: 2026-04-16
- **匹配关键词**: path planning
- **arXiv**: [2604.14882v1](http://arxiv.org/abs/2604.14882v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 快速城市化与持续人口增长使城市固体废物管理面临日益严峻的挑战，凸显了对智能化、自动化废物处理方案的迫切需求。本文提出并评估了一种集成废物管理框架，该框架融合了机器人垃圾分类模块与优化型生物消化器两大互联系统。机器人垃圾分类系统采用MyCobot 280 Jetson Nano机械臂，结合YOLOv8目标检测技术与基于机器人操作系统（ROS）的路径规划算法，实现实时废物识别与分拣。该系统能以高精度将废物分为四类，显著减少人工干预需求。分类后的可生物降解废物被输送至配备多传感器的生物消化器系统，传感器持续监测温度、pH值、压力及电机转速等关键参数。通过粒子群优化（PSO）算法与回归模型相结合，系统参数得以动态调整，这种智能优化方法确保了运行稳定性，并在多变环境条件下实现消化效率最大化。动态环境下的系统测试表明，该框架实现了98%的分拣准确率与高效的生物转化效能。所提出的框架为现代废物管理提供了可扩展、智能化且实用的解决方案，适用于住宅与工业应用场景。

---

### 6. Generalization in LLM Problem Solving: The Case of the Shortest Path

- **作者**: Yao Tong, Jiayuan Ye, Anastasia Borovykh, Reza Shokri
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.15306v1)
- **发表日期**: 2026-04-16
- **匹配关键词**: path planning
- **arXiv**: [2604.15306v1](http://arxiv.org/abs/2604.15306v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 语言模型能否实现系统性泛化仍是一个备受争议的议题。然而，实证性能往往受到训练数据、训练范式及推理策略等多重因素的共同影响，导致模型失效的原因难以解析。为此，我们构建了一个基于最短路径规划的受控合成实验环境——这是一个典型的可组合序列优化问题。该实验框架能够清晰分离上述影响因素，并支持空间迁移（向未见地图的泛化）与长度扩展（处理更长时程问题）这两个正交的泛化维度。研究发现，模型在空间迁移方面表现优异，但在长度扩展场景下因递归不稳定性而持续失效。我们进一步分析了学习流程中不同阶段对系统性问题解决能力的影响：例如，数据覆盖范围决定了模型的能力上限；强化学习虽能提升训练稳定性却无法突破该上限；推理阶段的规模扩展虽可提升性能，却无法弥补长度扩展导致的失效问题。

---

### 7. Agentic Microphysics: A Manifesto for Generative AI Safety

- **作者**: Federico Pierucci, Matteo Prandi, Marcantonio Bracale Syrnikov, Marcello Galisai, Piercosma Bisconti
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.15236v1)
- **发表日期**: 2026-04-16
- **匹配关键词**: tool use
- **arXiv**: [2604.15236v1](http://arxiv.org/abs/2604.15236v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔒 开源**: 未提及
- **中文摘要**: 本文提出了一种针对智能体人工智能安全研究的方法论框架。随着系统逐步具备规划、记忆、工具使用、持久身份和持续交互能力，安全分析已不能局限于孤立模型层面。群体性风险源于智能体间的结构化交互——通过长期持续的沟通、观察与相互影响过程，这些交互将塑造集体行为模式。当分析对象发生转变时，方法论缺口随之显现：无论是聚焦单个智能体还是宏观结果的研究路径，都难以揭示产生集体风险的交互层机制及其可控设计变量。我们需要建立一种能够明确因果关联、将局部交互结构与群体动态相联结的框架，以实现现象解释与风险干预的双重目标。为此我们提出两个相互关联的核心概念：智能体微观机制界定了分析层级，即在特定协议条件下一个智能体的输出转化为另一个智能体输入的局部交互动态；生成式安全则确立了方法论路径，通过从微观条件中培育现象并激发风险，从而识别充分机制、探测临界阈值并设计有效干预措施。

---

### 8. RaTA-Tool: Retrieval-based Tool Selection with Multimodal Large Language Models

- **作者**: Gabriele Mattioli, Evelyn Turri, Sara Sarto, Lorenzo Baraldi, Marcella Cornia, Lorenzo Baraldi, Rita Cucchiara
- **单位**: 详见 [arXiv 页面](http://arxiv.org/abs/2604.14951v1)
- **发表日期**: 2026-04-16
- **匹配关键词**: tool use
- **arXiv**: [2604.14951v1](http://arxiv.org/abs/2604.14951v1)
- **📥 PDF**: 未下载（仅高亮论文自动下载）
- **🔓 开源**: HUGGINGFACE
- **中文摘要**: 基于基础模型的工具学习旨在赋予人工智能系统调用外部资源的能力——如API接口、计算工具及专用模型——以解决超越单一语言生成模型能力范围的复杂任务。尽管大语言模型和多模态大语言模型在推理与感知能力上取得显著进展，现有工具调用方法仍主要局限于纯文本输入和封闭环境设定。这导致其难以解析多模态用户指令，且无法泛化至训练阶段未接触过的工具。本研究提出RaTA-Tool这一面向开放世界的多模态工具选择创新框架。区别于传统从用户查询到固定工具标识的直接映射学习，我们的方法使多模态大语言模型能够将多模态查询转化为结构化任务描述，进而通过将该表征与语义丰富的机器可读工具描述进行匹配，检索出最适配的工具。这种基于检索的范式天然支持无需重新训练即可扩展至新工具的特性。为增强任务描述与工具选择之间的匹配精度，我们引入基于偏好的优化阶段，采用直接偏好优化技术。为推进该领域研究，我们还构建了首个开放世界多模态工具使用数据集，其标准化工具描述源自Hugging Face模型卡片。大量实验表明，我们的方法显著提升了工具选择性能，尤其在开放世界多模态场景中表现突出。

---

