# Quantization, Mixed Precision, and Efficient Inference

Modern AI systems are optimized for cost and speed, not only accuracy.

## 1. Why quantization matters
Quantization reduces the precision of weights and activations, such as:
- FP32 -> FP16
- FP16 -> INT8
- INT8 -> INT4

This reduces memory and compute while keeping model behavior close to the original.

## 2. Mixed precision training
Use lower precision (FP16/BF16) for training with loss scaling to keep stability.

## 3. Use cases
- mobile inference
- edge AI
- LLM serving
- lower cloud cost
- faster response times

## 4. Quantization strategies
- post-training quantization
- quantization-aware training
- dynamic quantization
- static quantization

## 5. Practical tools
- bitsandbytes
- ONNX Runtime
- TensorRT
- vLLM
- TGI
- torch.quantization

## 6. Inference optimization
Important concepts:
- batching
- caching
- throughput vs latency
- token streaming
- KV-cache
- serving concurrency

## 7. Intuition
A smaller model or compressed weights can drastically reduce deployment cost while preserving most of the performance.

## 8. Exercise
Compare latency and output quality of a model before and after quantization on a small benchmark.
