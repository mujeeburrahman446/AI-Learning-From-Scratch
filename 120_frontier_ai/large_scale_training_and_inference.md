# Large-Scale Training and Inference

This section covers what happens when models become large enough that single-GPU or single-machine training is no longer enough.

## 1. Why scale matters
Large models require:
- more compute
- more memory
- more data
- more parallelism
- better orchestration

## 2. Parallelism strategies
### Data parallelism
Each device loads a different mini-batch and synchronizes gradients.

### Tensor parallelism
Model weights are split across devices.

### Pipeline parallelism
Different layers are assigned to different devices.

### Expert parallelism
Used in MoE models, where tokens are routed to different expert submodels.

## 3. Distributed training challenges
- communication overhead
- synchronization cost
- failure recovery
- memory fragmentation
- load imbalance

## 4. Inference optimization
Inference must optimize:
- latency
- throughput
- memory use
- model serving concurrency
- cost per request

## 5. KV cache
Large language model inference uses caching to avoid recomputing earlier tokens.

This improves speed for long prompts and multi-turn conversations.

## 6. Quantized serving
Quantization is often used for deployment to reduce serving cost and increase throughput.

## 7. Popular tools
- DeepSpeed
- FSDP
- Megatron-LM
- vLLM
- TGI
- ONNX Runtime
- TensorRT
- Triton Inference Server

## 8. Practical exercise
Compare a small local inference setup to a batched or cached inference stack and summarize the tradeoffs.

## 9. Summary
The large-scale AI story is not just about bigger models. It is about efficiency, distributed execution, serving, and production constraints.
