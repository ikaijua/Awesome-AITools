# Genesis Introduction

## What is Genesis?

**Genesis** (by [Genesis-Embodied-AI](https://github.com/Genesis-Embodied-AI/genesis-world)) is a high-performance simulation platform designed specifically for general-purpose robotics and **Embodied AI** learning. It provides an end-to-end simulation stack that integrates a multi-physics engine, a photo-realistic renderer, and a cross-platform compiler.

## Core Features

### 1. Unified Multi-Physics Engine
Unlike traditional simulators, Genesis supports Rigid bodies, FEM (deformables), MPM (sand/snow), SPH (liquids), and PBD (cloth/fluids) all in one unified state, allowing for complex interactions between different types of matter.

### 2. Nyx Renderer
A custom-built, photo-realistic renderer designed for robotics. It supports Physically Based Rendering (PBR) and advanced techniques like 3D Gaussian Splatting to provide high-fidelity visual input for AI agents.

### 3. Quadrants Compiler
A specialized compiler that translates Python code into high-performance kernels for CUDA (NVIDIA), ROCm (AMD), Metal (Apple), and Vulkan, enabling simulation to run on everything from laptops to GPU clusters.

### 4. Differentiable Simulation
Includes native autodiff capabilities, allowing for gradient-based optimization of robot designs and control policies, which is a key requirement for modern AI research.

### 5. Broad Asset Support
Seamlessly imports industry-standard formats including URDF, MJCF, OBJ, GLB, and USD.

## Who is it for?

- **Robotics Researchers:** For developing and testing complex control algorithms in safe, reproducible environments.
- **AI/ML Engineers:** For training embodied AI agents that need to interact with a complex physical world.
- **Data Scientists:** For generating high-fidelity synthetic datasets for computer vision and sensor fusion.

## Quick Start

### Installation

```bash
pip install genesis-world
```

### Basic Usage (Python)

```python
import genesis as gs

# Initialize Genesis
gs.init(backend=gs.cuda)

# Create a scene
scene = gs.Scene()

# Add a robot (e.g., a Franka arm)
robot = scene.add_entity(
    gs.morphs.URDF(file='urdf/franka_emika/panda.urdf')
)

# Build and run
scene.build()
for i in range(1000):
    scene.step()
```

## Related Resources

- [GitHub Repository](https://github.com/Genesis-Embodied-AI/genesis-world)
- [Official Website](https://genesis-world.ai/)
- [Documentation](https://docs.genesis-world.ai/)

## License

Genesis is an open-source project. Please refer to its repository for licensing details.
