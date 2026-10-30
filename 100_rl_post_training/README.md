# RL and Post-Training

This section covers how models learn from feedback and how they are aligned for human usefulness.

## Reinforcement Learning basics

### Core ideas
- agent
- environment
- state
- action
- reward
- policy
- value function

### Methods to learn
- bandits
- Markov Decision Processes (MDPs)
- dynamic programming
- Monte Carlo methods
- temporal difference learning
- Q-learning
- policy gradients
- REINFORCE
- actor-critic
- PPO
- DQN
- SAC

## Why RL matters
RL is used when the objective is not just predicting labels, but choosing actions to maximize long-term reward.

Examples:
- robotics
- game AI
- recommendation systems
- LLM decision-making
- autonomous tool use

## LLM post-training
Modern LLMs are usually improved after pretraining with post-training methods.

### Common stages
1. pretraining on large corpora
2. supervised fine-tuning (SFT)
3. preference modeling
4. RLHF or DPO-based optimization
5. safety alignment
6. tool-use and reasoning improvements

### Post-training methods
- supervised fine-tuning
- reward modeling
- RLHF
- DPO
- ORPO
- KTO
- GRPO
- best-of-N sampling
- constitutional AI
- preference optimization from synthetic data

## Alignment goals
- helpfulness
- harmlessness
- honesty
- reasoning quality
- task completion
- safety

## Frontier topics
- RL with tool access
- multi-step reasoning optimization
- reasoning models
- verifier-based training
- reward hacking detection
- long-horizon policy control
- multi-agent optimization

## Goal
This section connects model training to real-world AI behavior, alignment, and policy optimization.
