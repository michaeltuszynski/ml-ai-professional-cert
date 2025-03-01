# Mini-Lesson 22.3: Reinforcement Learning and Its Application to Neural Networks

Reinforcement learning (RL) is a type of ML where an agent learns to make decisions by interacting with an environment to maximize cumulative reward. The basics of reinforcement learning are:

## Agent, Environment, and Actions

- **Agent**: The learner or decision-maker that interacts with the environment. It makes decisions based on observations from the environment and aims to maximize rewards.
- **Environment**: The external system with which the agent interacts. It provides feedback (rewards) and changes its state based on the agent's actions.
- **Actions**: Choices made by the agent that affect the environment. The set of all possible actions is called the action space.

## State

A representation of the current situation or context in the environment. States define what the agent observes and helps determine the appropriate action.

## Rewards

A scalar feedback signal received from the environment after the agent performs an action. Rewards can be positive (rewards) or negative (penalties) and are used to evaluate the action's effectiveness.

## Policy

A strategy used by the agent to decide which action to take in a given state. It can be deterministic (always chooses the same action for a state) or stochastic (chooses actions probabilistically).

## Value Function

A function that estimates the expected cumulative reward an agent can obtain starting from a state (state value) or state–action pair (action value). This helps the agent evaluate the long-term benefit of states or actions.

- **State Value Function (V(s))**: Estimates the expected reward for being in state s and following a particular policy.
- **Action Value Function (Q(s, a))**: Estimates the expected reward for taking action a in state s and following a particular policy thereafter.

## Return

The total accumulated reward the agent receives over time, often discounted to prioritize immediate rewards. It can be calculated as a sum of rewards over episodes or steps.

## Exploration vs. Exploitation

- **Exploration**: The agent tries new actions to discover their effects and learn more about the environment.
- **Exploitation**: The agent uses known information to select actions that maximize reward based on previous experience.

## Temporal Difference (TD) Learning

A method where the agent learns value functions based on the difference between successive predictions. TD learning updates estimates based on the difference between the predicted and observed rewards.

## Module-Free vs. Model-Based Methods

- **Model-Free Methods**: The agent learns to make decisions based solely on experience without using a model of the environment. Examples include Q-learning and SARSA.
- **Model-Based Methods**: The agent uses a model of the environment to simulate outcomes and plan actions. These methods can be more efficient but require a model of the environment dynamics.

## Algorithms

- **Value-Based Methods**: Focus on learning value functions. Examples include Q-learning and Deep Q-networks (DQN).
- **Policy-Based Methods**: Directly learn the policy that maximizes rewards. Examples include policy gradient methods.
- **Actor–Critic Methods**: Combine value- and policy-based approaches, where the actor updates the policy, and the critic evaluates the policy by learning the value function.

Reinforcement learning is widely used in various applications, such as robotics, game playing, autonomous vehicles, and finance, due to its ability to handle complex decision-making problems where traditional methods may fall short.

## Recurrent Neural Networks vs. Traditional Neural Networks

Recurrent neural networks (RNNs) are a specialized type of neural network designed to handle sequential data, which sets them apart from traditional neural networks.

**Differences in Temporal Dynamics:**
- **RNN:** Processes sequential data by maintaining an internal state that evolves over time, allowing the network to remember information from previous time steps and use it to influence future predictions.
- **NN:** Processes fixed-size input data and produces output without considering the order or sequence of the data. Lacks temporal dynamics.

**Differences in Memory:**
- **RNN:** Has a form of memory through hidden states that capture information about previous inputs in the sequence. This memory allows RNNs to make predictions based on the entire sequence of data.
- **NN:** Lacks explicit memory of past inputs.

**Differences in Training:**
- **RNN:** Training is more complex due to the need to handle the temporal dependencies and potential vanishing or exploding gradient problems.
- **NN:** Training involves updating weights based on the error between the predicted and actual outputs.