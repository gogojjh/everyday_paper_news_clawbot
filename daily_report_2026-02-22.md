# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-02-22 12:57

**今日新增**: 5 篇

**搜索关键词**: `lifelong SLAM long-term SLAM continuous SLAM persistent SLAM lifelong mapping | robot navigation path planning motion planning autonomous navigation | articulated object manipulation cabinet door opening affordance`

---

**🔓 开源代码/模型**: 1/5 篇提供

---

## 🧭 Navigation

### 1. RA-Nav: A Risk-Aware Navigation System Based on Semantic Segmentation for Aerial Robots in Unpredictable Environments

- **作者**: Ziyi Zong, Xin Dong, Jinwu Xiang, Daochun Li, Zhan Tu
- **发表日期**: 2026-02-19
- **匹配关键词**: robot navigation, navigation
- **arXiv**: [2602.17515v1](http://arxiv.org/abs/2602.17515v1)
- **🔒 开源**: 未提及
- **中文摘要**: 现有空中机器人导航系统通常围绕静态与动态障碍物规划路径，但当静态障碍物突然移动时无法适应。通过融入环境语义感知能力，可对突然移动障碍物带来的潜在风险进行预估。本文提出RA-Nav——基于语义分割的风险感知导航框架。轻量化多尺度语义分割网络实时识别障碍物类别，进一步将其划分为静止型、暂时静态型与动态型三类。针对每类障碍物设计相应风险估计函数，实现实时风险预测，并以此构建完整的局部风险地图。基于该地图设计风险感知路径搜索算法，确保规划兼顾路径效率与安全性。随后进行轨迹优化，生成安全、平滑且动力学可行的轨迹。对比仿真表明，在障碍物状态突变场景中，RA-Nav相比基线方法获得更高成功率。通过真实数据仿真进一步验证了其有效性。

---

### 2. NRGS-SLAM: Monocular Non-Rigid SLAM for Endoscopy via Deformation-Aware 3D Gaussian Splatting

- **作者**: Jiwei Shan, Zeyu Cai, Yirui Li, Yongbo Chen, Lijun Han, Yun-hui Liu, Hesheng Wang, Shing Shin Cheng
- **发表日期**: 2026-02-19
- **匹配关键词**: navigation
- **arXiv**: [2602.17182v1](http://arxiv.org/abs/2602.17182v1)
- **🔓 开源**: CODE
- **中文摘要**: 视觉同步定位与建图（V-SLAM）是实现自主感知与导航的基础能力。然而，内窥镜场景因持续的软组织形变而违背了刚性假设，导致相机自身运动与内部形变之间存在强烈的耦合模糊性。尽管近期单目非刚性SLAM方法已取得显著进展，但这些方法往往缺乏有效的解耦机制，并依赖稀疏或低保真度的场景表示，从而导致跟踪漂移和重建质量受限。为突破这些局限，我们提出NRGS-SLAM——一种基于3D高斯泼溅的内窥镜单目非刚性SLAM系统。为解决耦合模糊性问题，我们引入了形变感知的3D高斯地图，通过为每个高斯基元添加可学习的形变概率进行增强，并采用无需外部非刚性标签的贝叶斯自监督策略进行优化。基于此表征，我们设计了可变形跟踪模块，通过优先处理低形变区域实现鲁棒的由粗到精姿态估计，继而执行高效的逐帧形变更新。精心设计的可变形建图模块能逐步扩展并优化地图，在表征能力与计算效率间取得平衡。此外，系统采用统一的鲁棒几何损失函数，融合外部几何先验以缓解单目非刚性SLAM固有的不适定性。在多个公开内窥镜数据集上的大量实验表明，相较于现有先进方法，NRGS-SLAM能实现更精确的相机姿态估计（均方根误差降低达50%）和更高质量的光照真实重建。全面的消融研究进一步验证了关键设计选择的有效性。源代码将在论文录用后公开。

---

### 3. Hybrid System Planning using a Mixed-Integer ADMM Heuristic and Hybrid Zonotopes

- **作者**: Joshua A. Robbins, Andrew F. Thompson, Jonah J. Glunt, Herschel C. Pangborn
- **发表日期**: 2026-02-19
- **匹配关键词**: motion planning
- **arXiv**: [2602.17574v1](http://arxiv.org/abs/2602.17574v1)
- **🔒 开源**: 未提及
- **中文摘要**: 基于嵌入式优化的混合系统规划因采用计算密集且常对特定数值公式敏感的混合整数规划而面临挑战。为应对这一挑战，本文提出一种混合系统运动规划框架，该框架将先进集合表示方法——混合Zonotope与新型交替方向乘子法（ADMM）混合整数规划启发式算法相结合。研究首先提出基于混合Zonotode的分段仿射系统可达性分析通用处理方法，并将其扩展至最优规划问题的构建。相较于既有技术生成的等效集合，采用所提方法生成的集合具有更低的内存复杂度与更紧密的凸松弛特性。所提出的ADMM启发式算法能高效利用混合Zonotope结构特性，针对混合Zonotope构建的规划问题，该算法相比现有先进混合整数规划启发式方法实现了收敛速度的提升。最终，所提出的嵌入式硬件混合系统规划方法在自动驾驶行为与运动联合规划场景中进行了实验验证。

---

### 4. Dodging the Moose: Experimental Insights in Real-Life Automated Collision Avoidance

- **作者**: Leila Gharavi, Simone Baldi, Yuki Hosomi, Tona Sato, Bart De Schutter, Binh-Minh Nguyen, Hiroshi Fujimoto
- **发表日期**: 2026-02-19
- **匹配关键词**: motion planning
- **arXiv**: [2602.17512v1](http://arxiv.org/abs/2602.17512v1)
- **🔒 开源**: 未提及
- **中文摘要**: 道路突发静态障碍物（即麋鹿测试）是自动驾驶避撞领域中一个广为人知的紧急场景。在现有技术中，模型预测控制（MPC）长期被用于自动驾驶车辆的规划与控制。然而，由于MPC在此类危险场景中执行规避动作时的高计算需求，麋鹿测试等紧急情况下的实时自动避撞问题仍未得到解决。本文通过实验实现MPC在突发意外静态障碍物出现后的运动规划，为实时避撞提供了新的见解。鉴于现有非线性MPC在实时提供可接受解决方案方面能力有限，我们提出了一种类人前馈规划器，用于在MPC优化问题因初始猜测质量差而不可行或无法找到合适解时提供辅助。我们引入最大转向操作概念来设计前馈规划器，模拟人类在检测到道路静态障碍物后的反应模式。利用FPEV2-Kanon电动汽车在不同速度和紧急程度下进行了实车实验，并通过与现有MPC运动规划器的对比验证了本规划策略的有效性。

---

### 5. Bluetooth Phased-array Aided Inertial Navigation Using Factor Graphs: Experimental Verification

- **作者**: Glen Hjelmerud Mørkbak Sørensen, Torleiv H. Bryne, Kristoffer Gryte, Tor Arne Johansen
- **发表日期**: 2026-02-19
- **匹配关键词**: navigation
- **arXiv**: [2602.17407v1](http://arxiv.org/abs/2602.17407v1)
- **🔒 开源**: 未提及
- **中文摘要**: 相控阵蓝牙系统已成为在仓库物流、无人机着陆和自主对接等全球导航卫星系统受限场景下实现辅助惯性导航的低成本替代方案。基于商用现成组件构建导航系统可降低相控阵无线电导航系统的应用门槛，但代价是测量噪声显著增加且有效作用距离相对较短。本文通过多旋翼无人机飞行实验数据，对比了基于因子图优化估计器的鲁棒估计策略。我们评估了在蓝牙角度测量辅助下，结合距离或气压测量时，系统在全球导航卫星信号丢失场景中的性能表现。

---

