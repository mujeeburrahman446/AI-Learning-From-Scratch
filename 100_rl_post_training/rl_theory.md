# RL Theory

Reinforcement learning is a framework where an agent learns by interacting with an environment and receiving rewards.

## 1. Core elements
- agent
- environment
- state
- action
- reward
- policy

## 2. Markov Decision Process
An MDP is formalized as:

```text
(S, A, P, R, gamma)
```

where:
- S = set of states
- A = set of actions
- P = transition probabilities
- R = reward function
- gamma = discount factor

## 3. Objective
The agent tries to maximize cumulative reward over time.

## 4. Bellman equation
```text
V(s) = max_a [R(s,a) + gamma * sum P(s'|s,a) * V(s')]
```

This expresses the value of a state in terms of future rewards.

## 5. Q-learning
Q-learning estimates the value of taking action a in state s.

```text
Q(s,a) = Q(s,a) + alpha * (reward + gamma * max_a' Q(s',a') - Q(s,a))
```

## 6. Policy gradients
Instead of estimating values directly, the agent learns a policy that chooses actions with probabilities.

## 7. PPO and other modern methods
Modern algorithms stabilize learning using surrogate objectives and clipped updates.

## 8. In LLM post-training
RL is used to align the model with human preferences and improve useful behavior.

## Summary
RL theory explains why agents can learn sequential decision-making in uncertain environments and how this extends to tool use, reasoning, and agentic systems.
