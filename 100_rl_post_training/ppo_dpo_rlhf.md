# PPO, DPO, RLHF, and Alignment

This section covers modern training methods for improving LLM behavior after pretraining.

## 1. RLHF
Reinforcement Learning from Human Feedback uses human preference data to shape model behavior.

Typical flow:
1. collect prompts
2. generate multiple outputs
3. rank outputs by human preference
4. train a reward model
5. optimize policy using RL

## 2. DPO
Direct Preference Optimization avoids explicit reward modeling by optimizing directly on preference pairs.

## 3. PPO
Proximal Policy Optimization is a widely used RL algorithm for stable policy optimization.

## 4. GRPO
Group Relative Policy Optimization is used in newer reasoning-focused model training systems.

## 5. Alignment goals
- helpfulness
- harmlessness
- honesty
- reasoning quality
- user preference match

## 6. Important caution
Alignment and post-training can be distorted by:
- reward hacking
- poor preference data
- over-optimization
- overfitting to evaluation signals

## 7. Goal
Learn how post-training transforms a base model into a usable assistant or agent that behaves in aligned, useful ways.
