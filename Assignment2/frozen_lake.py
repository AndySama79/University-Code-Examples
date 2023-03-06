import numpy as np
import sys
import gym

#TODO: initialize the frozen lake env
env = gym.make('FrozenLake-v1')
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
def q_learning(env, epsilon=0.1, alpha=0.5, gamma=0.9, episodes=1000):
    #TODO: Q-table
    Q = np.zeros((states, actions))
    optimal = np.argmax(Q, axis=1)
    steps = 0

    for i in range(episodes):
        state = env.reset()
        converged = False
        while not converged:
            if np.random.random() < epsilon:
                action = env.action_space.sample()
            else:
                action = optimal[state]
            next_state, reward, converged, _ = env.step(action)
            Q[state, action] += alpha * (reward + gamma * np.max(Q[next_state]) - Q[state, action])
            optimal[state] = np.argmax(Q[state])
            state = next_state
            if converged and reward == 1:
                steps += 1
    return Q, steps

def main():
    if len(sys.argv) < 3:
        print(f'usage: {sys.argv[0]} <steps> <episodes>')
        sys.exit()
    
    path = np.array([1, 2, 1, 0, 2, 1, 1, 2, 2, 1, 0, 2, 0, 2, 3, 0])
    
    steps = int(sys.argv[1])
    episodes = int(sys.argv[2])
    steps_random_walk = symmetric_walk(steps, path)
    prob_prob_walk = prob_walk(3, 3, steps)
    Q, steps_Q = q_learning(env, episodes)

    print('Symmetric Random Walk: ', steps_random_walk)
    print('Analytical Expression:', int(prob_prob_walk * steps))
    print('Q-learning:', steps_Q)

if __name__ == '__main__':
    main()