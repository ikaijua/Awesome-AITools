# Genesis 简介

## 什么是 Genesis？

**Genesis**（由 [Genesis-Embodied-AI](https://github.com/Genesis-Embodied-AI/genesis-world) 开发）是一个专为通用机器人和 **具身智能 (Embodied AI)** 学习设计的高性能仿真平台。它提供了一个端到端的仿真栈，集成了统一物理引擎、照片级渲染器和跨平台编译器。

## 核心特性

### 1. 统一多物理引擎
与传统仿真器不同，Genesis 在统一状态下支持刚体、有限元 (FEM，可变形体)、物质点法 (MPM，沙/雪)、平滑粒子流体动力学 (SPH，液体) 和基于位置的动力学 (PBD，布料/流体)，允许不同类型的物质之间进行复杂的交互。

### 2. Nyx 渲染器
专门为机器人需求设计的自定义照片级渲染器。它支持基于物理的渲染 (PBR) 和 3D 高斯泼溅 (3D Gaussian Splatting) 等先进技术，为 AI 代理提供高保真的视觉输入。

### 3. Quadrants 编译器
一个专门的编译器，可将 Python 代码转换为适用于 CUDA (NVIDIA)、ROCm (AMD)、Metal (Apple) 和 Vulkan 的高性能内核，使仿真能够从笔记本电脑扩展到 GPU 集群运行。

### 4. 可微仿真
内置原生自动微分 (Autodiff) 能力，允许对机器人设计和控制策略进行基于梯度的优化，这是现代 AI 研究的核心需求。

### 5. 广泛的资产支持
无缝导入行业标准格式，包括 URDF、MJCF、OBJ、GLB 和 USD。

## 适用人群

- **机器人研究员**：在安全、可重复的环境中开发和测试复杂的控制算法。
- **AI/ML 工程师**：训练需要与复杂物理世界交互的具身智能代理。
- **数据科学家**：为计算机视觉和传感器融合生成高保真的合成数据集。

## 快速上手

### 安装

```bash
pip install genesis-world
```

### 基础用法 (Python)

```python
import genesis as gs

# 初始化 Genesis
gs.init(backend=gs.cuda)

# 创建场景
scene = gs.Scene()

# 添加机器人 (例如 Franka 机械臂)
robot = scene.add_entity(
    gs.morphs.URDF(file='urdf/franka_emika/panda.urdf')
)

# 构建并运行
scene.build()
for i in range(1000):
    scene.step()
```

## 相关资源

- [GitHub 仓库](https://github.com/Genesis-Embodied-AI/genesis-world)
- [官方网站](https://genesis-world.ai/)
- [文档](https://docs.genesis-world.ai/)

## 许可证

Genesis 是一个开源项目。许可详情请参考其 GitHub 仓库。
