import numpy as np
import gym

#TODO: initialize the frozen lake env
env = gym.make('Frozenlake-v0')
states = env.observation_space.n
actions = env.action_space.n

#TODO: Symmetric random walk
def symmetric_walk(steps, opt_path):
    opt = 0
    for i in range(steps):
        state = env.reset()
        converged = False
        while not converged:
            action = opt_path[state]
            next_state, reward, done, _ = env.step(action)
            state = next_state
            if converged and reward == 1:
                opt += 1
    return opt

#TODO: analytical expression
def prob_walk(x, y, steps):
    prob = 0
    for i in range(steps):
        for j in range(steps):
            prob += np.math.comb(i+j, i) * np.math.comb(steps-i-1+j, j)
    prob *= (1/4)**steps
    return prob

#TODO: q-learning
def q_learning(env, epsilon=0.1, alpha=0.1, gamma=0.99):
    pass