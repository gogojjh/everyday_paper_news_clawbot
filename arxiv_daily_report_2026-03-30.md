# 📚 arXiv Robotics 论文日报

**生成时间**: 2026-03-30 13:49

**今日新增**: 20 篇

**搜索关键词**: `humanoid robot OR humanoid OR legged robot OR quadruped robot OR bipedal robot OR hexapod robot | visual navigation OR vision-based navigation OR semantic navigation OR VLN OR visual mapping OR vision-based mapping OR 3D reconstruction OR neural mapping | lifelong SLAM OR long-term SLAM OR continuous SLAM OR persistent SLAM OR lifelong mapping OR long-term localization OR lifelong navigation | vision-language-action OR VLA OR diffusion policy OR diffusion policy for manipulation OR diffusion-based policy | nerf OR neural radiance field OR gaussian splatting OR 3D gaussian splatting OR neural rendering | image-goal navigation OR point-goal navigation OR object-goal navigation OR goal-oriented navigation | robot navigation OR path planning OR motion planning OR autonomous navigation OR obstacle avoidance OR exploration OR multi-robot navigation | articulated object OR cabinet opening OR door opening OR handle manipulation OR affordance OR interactive perception OR grasp detection OR dexterous grasping OR 6-DoF grasping OR bimanual manipulation | human-robot interaction OR collaborative robot OR social navigation OR human-aware planning OR visual servoing OR eye-in-hand OR visual tracking`

---

**🔓 开源代码/模型**: 3/20 篇提供

**🏅 Oral**: 5 篇 | **🌟 Highlight**: 15 篇 | **📌 Poster**: 0 篇

---

## 🏅 Oral (Top recommendations)

*基于用户近期关注方向（world model/action generation；lifelong spatial memory/SLAM2.0；interaction/articulated/tactile）*

---

### 1. DiffusionAnything: End-to-End In-context Diffusion Learning for Unified Navigation and Pre-Grasp Motion

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2603.26322)
- **发表日期**: 
- **匹配关键词**: diffusion policy, navigation, vision-language-action, VLA
- **arXiv**: [2603.26322](https://arxiv.org/abs/2603.26322)
- **📥 PDF**: 已下载至本地 (`2603.26322_DiffusionAnything_End-to-End_In-context_Diffusion_Learning_for_Unified_Navigation_and_Pre-Grasp_Moti.pdf`) | recent-focus score=11.50
- **🔒 开源**: 未提及
- **摘要**: arXiv:2603.26322v1 Announce Type: new 
Abstract: Efficiently predicting motion plans directly from vision remains a fundamental challenge in robotics, where planning typically requires explicit goal specification and task-specific design. Recent vision-language-action (VLA) models infer actions directly from visual input but demand massive computational resources, extensive training data, and fail zero-shot in novel scenes. We present a unified image-space diffusion policy handling both meter-sc...

---

### 2. DFM-VLA: Iterative Action Refinement for Robot Manipulation via Discrete Flow Matching

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2603.26320)
- **发表日期**: 
- **匹配关键词**: HRI, VLA
- **arXiv**: [2603.26320](https://arxiv.org/abs/2603.26320)
- **📥 PDF**: 已下载至本地 (`2603.26320_DFM-VLA_Iterative_Action_Refinement_for_Robot_Manipulation_via_Discrete_Flow_Matching.pdf`) | recent-focus score=7.50
- **🔒 开源**: 未提及
- **摘要**: arXiv:2603.26320v1 Announce Type: new 
Abstract: Vision--Language--Action (VLA) models that encode actions using a discrete tokenization scheme are increasingly adopted for robotic manipulation, but existing decoding paradigms remain fundamentally limited. Whether actions are decoded sequentially by autoregressive VLAs or in parallel by discrete diffusion VLAs, once a token is generated, it is typically fixed and cannot be revised in subsequent iterations, so early token errors cannot be effecti...

---

### 3. VLA-OPD: Bridging Offline SFT and Online RL for Vision-Language-Action Models via On-Policy Distillation

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2603.26666)
- **发表日期**: 
- **匹配关键词**: vision-language-action, vision-language-action model, VLA
- **arXiv**: [2603.26666](https://arxiv.org/abs/2603.26666)
- **📥 PDF**: 已下载至本地 (`2603.26666_VLA-OPD_Bridging_Offline_SFT_and_Online_RL_for_Vision-Language-Action_Models_via_On-Policy_Distillat.pdf`) | recent-focus score=7.50
- **🔒 开源**: 未提及
- **摘要**: arXiv:2603.26666v1 Announce Type: new 
Abstract: Although pre-trained Vision-Language-Action (VLA) models exhibit impressive generalization in robotic manipulation, post-training remains crucial to ensure reliable performance during deployment. However, standard offline Supervised Fine-Tuning (SFT) suffers from distribution shifts and catastrophic forgetting of pre-trained capabilities, while online Reinforcement Learning (RL) struggles with sparse rewards and poor sample efficiency. In this pap...

---

### 4. Policy-Guided World Model Planning for Language-Conditioned Visual Navigation

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2603.25981)
- **发表日期**: 
- **匹配关键词**: visual navigation, navigation, learned navigation
- **arXiv**: [2603.25981](https://arxiv.org/abs/2603.25981)
- **📥 PDF**: 已下载至本地 (`2603.25981_Policy-Guided_World_Model_Planning_for_Language-Conditioned_Visual_Navigation.pdf`) | recent-focus score=6.50
- **🔒 开源**: 未提及
- **摘要**: arXiv:2603.25981v1 Announce Type: new 
Abstract: Navigating to a visually specified goal given natural language instructions remains a fundamental challenge in embodied AI. Existing approaches either rely on reactive policies that struggle with long-horizon planning, or employ world models that suffer from poor action initialization in high-dimensional spaces. We present PiJEPA, a two-stage framework that combines the strengths of learned navigation policies with latent world model planning for ...

---

### 5. ETA-VLA: Efficient Token Adaptation via Temporal Fusion and Intra-LLM Sparsification for Vision-Language-Action Models

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2603.25766)
- **发表日期**: 
- **匹配关键词**: vision-language-action, vision-language-action model, VLA
- **arXiv**: [2603.25766](https://arxiv.org/abs/2603.25766)
- **📥 PDF**: 已下载至本地 (`2603.25766_ETA-VLA_Efficient_Token_Adaptation_via_Temporal_Fusion_and_Intra-LLM_Sparsification_for_Vision-Langu.pdf`) | recent-focus score=6.50
- **🔒 开源**: 未提及
- **摘要**: arXiv:2603.25766v1 Announce Type: new 
Abstract: The integration of Vision-Language-Action (VLA) models into autonomous driving systems offers a unified framework for interpreting complex scenes and executing control commands. However, the necessity to incorporate historical multi-view frames for accurate temporal reasoning imposes a severe computational burden, primarily driven by the quadratic complexity of self-attention mechanisms in Large Language Models (LLMs). To alleviate this bottleneck...

---

## 🌟 Highlight

*人形机器人 | 足式机器人 | 视觉导航 | 终身导航 | 视觉建图 | 知名作者*

---

### 1. Chasing Autonomy: Dynamic Retargeting and Control Guided RL for Performant and Controllable Humanoid Running

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2603.25902)
- **发表日期**: 
- **匹配关键词**: obstacle avoidance
- **arXiv**: [2603.25902](https://arxiv.org/abs/2603.25902)
- **📥 PDF**: 已下载至本地 (`2603.25902_Chasing_Autonomy_Dynamic_Retargeting_and_Control_Guided_RL_for_Performant_and_Controllable_Humanoid_.pdf`)
- **🔒 开源**: 未提及
- **摘要**: arXiv:2603.25902v1 Announce Type: new 
Abstract: Humanoid robots have the promise of locomoting like humans, including fast and dynamic running. Recently, reinforcement learning (RL) controllers that can mimic human motions have become popular as they can generate very dynamic behaviors, but they are often restricted to single motion play-back which hinders their deployment in long duration and autonomous locomotion. In this paper, we present a pipeline to dynamically retarget human motions thro...

---

### 2. Partial Motion Imitation for Learning Cart Pushing with Legged Manipulators

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2603.26659)
- **发表日期**: 
- **匹配关键词**: mobile manipulation
- **arXiv**: [2603.26659](https://arxiv.org/abs/2603.26659)
- **📥 PDF**: 已下载至本地 (`2603.26659_Partial_Motion_Imitation_for_Learning_Cart_Pushing_with_Legged_Manipulators.pdf`)
- **🔒 开源**: 未提及
- **摘要**: arXiv:2603.26659v1 Announce Type: new 
Abstract: Loco-manipulation is a key capability for legged robots to perform practical mobile manipulation tasks, such as transporting and pushing objects, in real-world environments. However, learning robust loco-manipulation skills remains challenging due to the difficulty of maintaining stable locomotion while simultaneously performing precise manipulation behaviors. This work proposes a partial imitation learning approach that transfers the locomotion s...

---

### 3. Can a Robot Walk the Robotic Dog: Triple-Zero Collaborative Navigation for Heterogeneous Multi-Agent Systems

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2603.21723)
- **发表日期**: 
- **匹配关键词**: path planning, navigation
- **arXiv**: [2603.21723](https://arxiv.org/abs/2603.21723)
- **📥 PDF**: 已下载至本地 (`2603.21723_Can_a_Robot_Walk_the_Robotic_Dog_Triple-Zero_Collaborative_Navigation_for_Heterogeneous_Multi-Agent_.pdf`)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/triple-zeropp/Triple-zero-robot-agent
- **摘要**: arXiv:2603.21723v2 Announce Type: replace 
Abstract: We present Triple Zero Path Planning (TZPP), a collaborative framework for heterogeneous multi-robot systems that requires zero training, zero prior knowledge, and zero simulation. TZPP employs a coordinator--explorer architecture: a humanoid robot handles task coordination, while a quadruped robot explores and identifies feasible paths using guidance from a multimodal large language model. We implement TZPP on Unitree G1 and Go2 robots and ev...

---

### 4. Can Vision Foundation Models Navigate? Zero-Shot Real-World Evaluation and Lessons Learned

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2603.25937)
- **发表日期**: 
- **匹配关键词**: visual navigation, navigation, robot navigation
- **arXiv**: [2603.25937](https://arxiv.org/abs/2603.25937)
- **📥 PDF**: 已下载至本地 (`2603.25937_Can_Vision_Foundation_Models_Navigate?_Zero-Shot_Real-World_Evaluation_and_Lessons_Learned.pdf`)
- **🔒 开源**: 未提及
- **摘要**: arXiv:2603.25937v1 Announce Type: new 
Abstract: Visual Navigation Models (VNMs) promise generalizable, robot navigation by learning from large-scale visual demonstrations. Despite growing real-world deployment, existing evaluations rely almost exclusively on success rate, whether the robot reaches its goal, which conceals trajectory quality, collision behavior, and robustness to environmental change. We present a real-world evaluation of five state-of-the-art VNMs (GNM, ViNT, NoMaD, NaviBridger...

---

### 5. 120 Minutes and a Laptop: Minimalist Image-goal Navigation via Unsupervised Exploration and Offline RL

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2603.26441)
- **发表日期**: 
- **匹配关键词**: image-goal navigation, visual navigation, navigation, exploration
- **arXiv**: [2603.26441](https://arxiv.org/abs/2603.26441)
- **📥 PDF**: 已下载至本地 (`2603.26441_120_Minutes_and_a_Laptop_Minimalist_Image-goal_Navigation_via_Unsupervised_Exploration_and_Offline_R.pdf`)
- **🔒 开源**: 未提及
- **摘要**: arXiv:2603.26441v1 Announce Type: new 
Abstract: The prevailing paradigm for image-goal visual navigation often assumes access to large-scale datasets, substantial pretraining, and significant computational resources. In this work, we challenge this assumption. We show that we can collect a dataset, train an in-domain policy, and deploy it to the real world (1) in less than 120 minutes, (2) on a consumer laptop, (3) without any human intervention. Our method, MINav, formulates image-goal navigat...

---

### 6. Drive-Through 3D Vehicle Exterior Reconstruction via Dynamic-Scene SfM and Distortion-Aware Gaussian Splatting

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2603.26638)
- **发表日期**: 
- **匹配关键词**: gaussian splatting, 3D reconstruction, 3D gaussian splatting, 3d reconstruction
- **arXiv**: [2603.26638](https://arxiv.org/abs/2603.26638)
- **📥 PDF**: 已下载至本地 (`2603.26638_Drive-Through_3D_Vehicle_Exterior_Reconstruction_via_Dynamic-Scene_SfM_and_Distortion-Aware_Gaussian.pdf`)
- **🔒 开源**: 未提及
- **摘要**: arXiv:2603.26638v1 Announce Type: cross 
Abstract: High-fidelity 3D reconstruction of vehicle exteriors improves buyer confidence in online automotive marketplaces, but generating these models in cluttered dealership drive-throughs presents severe technical challenges. Unlike static-scene photogrammetry, this setting features a dynamic vehicle moving against heavily cluttered, static backgrounds. This problem is further compounded by wide-angle lens distortion, specular automotive paint, and non...

---

### 7. Wanderland: Geometrically Grounded Simulation for Open-World Embodied AI

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2511.20620)
- **发表日期**: 
- **匹配关键词**: 3D reconstruction, visual navigation, navigation, 3d reconstruction
- **arXiv**: [2511.20620](https://arxiv.org/abs/2511.20620)
- **📥 PDF**: 已下载至本地 (`2511.20620_Wanderland_Geometrically_Grounded_Simulation_for_Open-World_Embodied_AI.pdf`)
- **🔓 开源**: PROJECT_PAGE
  - 链接：https://ai4ce.github.io/wanderland/.
- **摘要**: arXiv:2511.20620v2 Announce Type: replace-cross 
Abstract: Reproducible closed-loop evaluation remains a major bottleneck in Embodied AI such as visual navigation. A promising path forward is high-fidelity simulation that combines photorealistic sensor rendering with geometrically grounded interaction in complex, open-world urban environments. Although recent video-3DGS methods ease open-world scene capturing, they are still unsuitable for benchmarking due to large visual and geometric sim-to-re...

---

### 8. Few TensoRF: Enhance the Few-shot on Tensorial Radiance Fields

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2603.25008)
- **发表日期**: 
- **匹配关键词**: 3D reconstruction, nerf, 3d reconstruction
- **arXiv**: [2603.25008](https://arxiv.org/abs/2603.25008)
- **📥 PDF**: 已下载至本地 (`2603.25008_Few_TensoRF_Enhance_the_Few-shot_on_Tensorial_Radiance_Fields.pdf`)
- **🔒 开源**: 未提及
- **摘要**: arXiv:2603.25008v2 Announce Type: replace-cross 
Abstract: This paper presents Few TensoRF, a 3D reconstruction framework that combines TensorRF's efficient tensor based representation with FreeNeRF's frequency driven few shot regularization. Using TensorRF to significantly accelerate rendering speed and introducing frequency and occlusion masks, the method improves stability and reconstruction quality under sparse input views. Experiments on the Synthesis NeRF benchmark show that Few TensoRF me...

---

### 9. Geo$^\textbf{2}$: Geometry-Guided Cross-view Geo-Localization and Image Synthesis

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2603.25819)
- **发表日期**: 
- **匹配关键词**: 3D reconstruction, 3d reconstruction
- **arXiv**: [2603.25819](https://arxiv.org/abs/2603.25819)
- **📥 PDF**: 已下载至本地 (`2603.25819_Geo$^textbf{2}$_Geometry-Guided_Cross-view_Geo-Localization_and_Image_Synthesis.pdf`)
- **🔒 开源**: 未提及
- **摘要**: arXiv:2603.25819v1 Announce Type: new 
Abstract: Cross-view geo-spatial learning consists of two important tasks: Cross-View Geo-Localization (CVGL) and Cross-View Image Synthesis (CVIS), both of which rely on establishing geometric correspondences between ground and aerial views. Recent Geometric Foundation Models (GFMs) have demonstrated strong capabilities in extracting generalizable 3D geometric features from images, but their potential in cross-view geo-spatial tasks remains underexplored. ...

---

### 10. FAST3DIS: Feed-forward Anchored Scene Transformer for 3D Instance Segmentation

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2603.25993)
- **发表日期**: 
- **匹配关键词**: 3D reconstruction, 3d reconstruction
- **arXiv**: [2603.25993](https://arxiv.org/abs/2603.25993)
- **📥 PDF**: 已下载至本地 (`2603.25993_FAST3DIS_Feed-forward_Anchored_Scene_Transformer_for_3D_Instance_Segmentation.pdf`)
- **🔒 开源**: 未提及
- **摘要**: arXiv:2603.25993v1 Announce Type: new 
Abstract: While recent feed-forward 3D reconstruction models provide a strong geometric foundation for scene understanding, extending them to 3D instance segmentation typically relies on a disjointed "lift-and-cluster" paradigm. Grouping dense pixel-wise embeddings via non-differentiable clustering scales poorly with the number of views and disconnects representation learning from the final segmentation objective. In this paper, we present a Feed-forward An...

---

### 11. Conditional Diffusion for 3D CT Volume Reconstruction from 2D X-rays

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2603.26509)
- **发表日期**: 
- **匹配关键词**: 3D reconstruction, 3d reconstruction
- **arXiv**: [2603.26509](https://arxiv.org/abs/2603.26509)
- **📥 PDF**: 已下载至本地 (`2603.26509_Conditional_Diffusion_for_3D_CT_Volume_Reconstruction_from_2D_X-rays.pdf`)
- **🔓 开源**: GITHUB
  - 链接：https://github.com/ai-med/AXON.
- **摘要**: arXiv:2603.26509v1 Announce Type: new 
Abstract: Computed tomography (CT) provides rich 3D anatomical details but is often constrained by high radiation exposure, substantial costs, and limited availability. While standard chest X-rays are cost-effective and widely accessible, they only provide 2D projections with limited pathological information. Reconstructing 3D CT volumes from 2D X-rays offers a transformative solution to increase diagnostic accessibility, yet existing methods predominantly ...

---

### 12. Scene Grounding In the Wild

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2603.26584)
- **发表日期**: 
- **匹配关键词**: gaussian splatting, 3D reconstruction, 3D gaussian splatting, 3d reconstruction
- **arXiv**: [2603.26584](https://arxiv.org/abs/2603.26584)
- **📥 PDF**: 已下载至本地 (`2603.26584_Scene_Grounding_In_the_Wild.pdf`)
- **🔒 开源**: 未提及
- **摘要**: arXiv:2603.26584v1 Announce Type: new 
Abstract: Reconstructing accurate 3D models of large-scale real-world scenes from unstructured, in-the-wild imagery remains a core challenge in computer vision, especially when the input views have little or no overlap. In such cases, existing reconstruction pipelines often produce multiple disconnected partial reconstructions or erroneously merge non-overlapping regions into overlapping geometry. In this work, we propose a framework that grounds each parti...

---

### 13. Wid3R: Wide Field-of-View 3D Reconstruction via Camera Model Conditioning

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2602.05321)
- **发表日期**: 
- **匹配关键词**: 3D reconstruction, nerf, 3d reconstruction
- **arXiv**: [2602.05321](https://arxiv.org/abs/2602.05321)
- **📥 PDF**: 已下载至本地 (`2602.05321_Wid3R_Wide_Field-of-View_3D_Reconstruction_via_Camera_Model_Conditioning.pdf`)
- **🔒 开源**: 未提及
- **摘要**: arXiv:2602.05321v2 Announce Type: replace 
Abstract: We present Wid3R, a feed-forward neural network for multi-view visual geometry reconstruction that supports wide field-of-view camera models. Unlike existing methods that assume rectified or pinhole inputs, Wid3R directly models wide-angle imagery without explicit calibration or undistortion. Our approach leverages a ray-based representation with spherical harmonics and introduces a novel camera model token to enable distortion-aware reconstru...

---

### 14. Emergent Neural Automaton Policies: Learning Symbolic Structure from Visuomotor Trajectories

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2603.25903)
- **发表日期**: 
- **匹配关键词**: VLA
- **arXiv**: [2603.25903](https://arxiv.org/abs/2603.25903)
- **📥 PDF**: 已下载至本地 (`2603.25903_Emergent_Neural_Automaton_Policies_Learning_Symbolic_Structure_from_Visuomotor_Trajectories.pdf`)
- **🔒 开源**: 未提及
- **摘要**: arXiv:2603.25903v1 Announce Type: new 
Abstract: Scaling robot learning to long-horizon tasks remains a formidable challenge. While end-to-end policies often lack the structural priors needed for effective long-term reasoning, traditional neuro-symbolic methods rely heavily on hand-crafted symbolic priors. To address the issue, we introduce ENAP (Emergent Neural Automaton Policy), a framework that allows a bi-level neuro-symbolic policy adaptively emerge from visuomotor demonstrations. Specifica...

---

### 15. Realtime-VLA V2: Learning to Run VLAs Fast, Smooth, and Accurate

- **作者**: 
- **单位**: 详见 [arXiv 页面](https://arxiv.org/abs/2603.26360)
- **发表日期**: 
- **匹配关键词**: VLA
- **arXiv**: [2603.26360](https://arxiv.org/abs/2603.26360)
- **📥 PDF**: 已下载至本地 (`2603.26360_Realtime-VLA_V2_Learning_to_Run_VLAs_Fast,_Smooth,_and_Accurate.pdf`)
- **🔒 开源**: 未提及
- **摘要**: arXiv:2603.26360v1 Announce Type: new 
Abstract: In deployment of the VLA models to real-world robotic tasks, execution speed matters. In previous work arXiv:2510.26742 we analyze how to make neural computation of VLAs on GPU fast. However, we leave the question of how to actually deploy the VLA system on the real robots open. In this report we describe a set of practical techniques to achieve the end-to-end result of running a VLA-driven robot at an impressive speed in real world tasks that req...

---

