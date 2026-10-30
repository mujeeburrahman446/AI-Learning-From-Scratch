# CUDA and GPU Programming

CUDA is the bridge between AI theory and efficient hardware execution.

## What to learn

### 1. CPU vs GPU
- CPU is optimized for serial tasks
- GPU is optimized for parallel workloads
- AI training is highly parallel

### 2. Parallel execution model
- thread
- block
- grid
- warp
- streaming multiprocessor

### 3. CUDA memory hierarchy
- global memory
- shared memory
- registers
- local memory
- constant memory
- texture memory

### 4. CUDA kernels
Learn how kernel launches work and how to structure parallel code.

### 5. Core examples
- vector addition
- reduction
- matrix multiplication
- convolution basics
- element-wise ops

### 6. Libraries
- cuBLAS
- cuDNN
- NCCL

### 7. Performance concerns
- memory bandwidth
- occupancy
- synchronization
- coalesced memory access
- avoiding branch divergence
- workload balancing

### 8. Multi-GPU training
- data parallelism
- gradient synchronization
- distributed training concepts
- all-reduce and all-gather

## Why CUDA matters in AI
Without GPU acceleration:
- training large networks becomes impractical
- inference latency rises
- frontier models are impossible to serve efficiently

## Learning objective
Learn the fundamentals of parallel execution and understand how frameworks like PyTorch and TensorFlow use CUDA under the hood.

## Advanced topics
- profiling with Nsight
- memory optimization
- kernel tuning
- distributed GPU training
- inference optimization on GPU
