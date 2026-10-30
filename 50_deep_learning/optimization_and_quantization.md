# Optimization and Quantization

This section covers how models are made efficient and usable in the real world.

## 1. Optimization fundamentals
The goal of optimization is to minimize loss efficiently.

Core methods:
- SGD
- Momentum
- RMSProp
- Adam
- AdamW

## 2. Learning rate
Learning rate controls step size in optimization.

Too high:
- instability
- divergence

Too low:
- very slow learning

## 3. Regularization
Methods include:
- L2 regularization
- dropout
- weight decay
- early stopping

These help prevent overfitting.

## 4. Mixed precision training
Mixed precision uses lower-precision representations such as FP16 or BF16.

Benefits:
- faster training
- lower memory use
- better throughput on GPUs

## 5. Quantization
Quantization reduces precision to save memory and speed up inference.

Examples:
- FP32 -> FP16
- FP16 -> INT8
- INT8 -> INT4

## 6. Why quantization matters
It is essential for:
- LLM serving
- edge deployment
- latency-sensitive applications
- reducing cloud costs

## 7. Parameter-efficient fine-tuning
Examples:
- LoRA
- QLoRA
- adapters
- prompt tuning

These let models adapt to tasks with far less training cost.

## 8. Practical exercise
Train a small model with AdamW and compare training behavior to SGD. Then study quantized inference on a small model or benchmark.

## 9. Summary
Optimization and quantization are the practical core of making AI models train well, fit memory constraints, and run efficiently in production.
