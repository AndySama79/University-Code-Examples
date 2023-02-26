import gym
import numpy as np

#TODO: initializing frozen lake environment
env = gym.make('FrozenLake-v0')

#TODO: defining the Q-table
Q = np.zeros((16, 4))

#TODO: setting the hyper-parameters
epsilon = 0.1   #*  exploration rate
alpha = 0.1     #* learning rate
gamma = 0.99    #* discount factor

#TODO: running the Q-learning algorithm for a specified number of episodes
episodes = 1000
for i in range(episodes):
    #TODO: reset the env for each episode
    state = env.reset()
    converged = False
    
    while not converged:
        #TODO: choose an action using epsilon-greedy exploration
        if np.random.uniform() < epsilon:
            action = env.action_space.sample()
        else:
            action = np.argmax(Q[state, :])

        next_state, reward, converged, _ = env.step(action)

        #TODO: update the Q-table
        Q[state, action] = (1 - alpha) * Q[state, action] + alpha * (reward + gamma * np.max(Q[next_state, :]))
        state = next_state

#TODO: evaluating the policy by running multiple simulations
trials = 100
total_reward = 0
for i in range(trials):
    state = env.reset()
    converged = False
    
    while not converged:
        action = np.argmax(Q[state, :])
        next_state, reward, converged, _ = env.step(action)

        total_reward += reward
        state = next_state

average_reward = total_reward / trials