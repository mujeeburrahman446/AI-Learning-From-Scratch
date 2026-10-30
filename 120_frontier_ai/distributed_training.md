# Distributed Training and Frontier AI Scaling

This section explains how large models are trained across many GPUs and machines.

## 1. Parallelism types
- data parallelism
- tensor parallelism
- pipeline parallelism
- sequence parallelism
- expert parallelism

## 2. Why distributed training is needed
Large model training requires:
- more memory than one GPU has
- more compute than one GPU can handle
- more throughput for large-scale learning

## 3. Challenges
- communication overhead
- synchronization cost
- memory fragmentation
- load balancing
- checkpointing

## 4. Hardware and infra
- GPUs
- interconnects
- host memory
- distributed storage
- cluster schedulers

## 5. Frontier model ideas
- scaling laws
- compute vs model size tradeoff
- long-context optimization
- MoE routing efficiency
- inference-time optimization

## 6. Goal
Learn how real frontier AI systems are trained, served, and optimized at scale.
