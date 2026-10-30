# CUDA Theory and GPU Architecture

CUDA is Nvidia's parallel computing platform and programming model.

## 1. CPU vs GPU
- CPU: optimized for sequential control tasks
- GPU: optimized for many parallel operations

AI workloads are highly parallel, so GPUs are ideal for model training and inference.

## 2. Thread model
- threads run in parallel
- threads are grouped into blocks
- blocks are grouped into a grid

## 3. Memory hierarchy
- registers
- shared memory
- local memory
- global memory
- constant memory

## 4. Parallel programming idea
A CUDA kernel launches many threads that process different portions of data simultaneously.

## 5. Why this matters for AI
All matrix operations and tensor computations can be parallelized. This is what makes deep learning training feasible at scale.

## 6. ML frameworks and CUDA
Frameworks like PyTorch and TensorFlow use CUDA kernels under the hood to accelerate matrix operations, convolutions, and attention computations.

## Summary
CUDA theory explains the hardware and software model that makes modern AI compute fast and scalable.
