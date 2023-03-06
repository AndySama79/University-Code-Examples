import os
import sys
import numpy as np
import random
import matplotlib.pyplot as plt
import time

#TODO:  define the grid world and the cliffs
n_rows = 4
n_cols = 4
cliff = [(1, col) for col in range(1, n_cols)]

#TODO:  define start and end states
start = (0, 0)
end = (3, 3)

def choose_action(state, Q, epsilon):
    if random.uniform(0, 1) < epsilon:
        return random.randint(0, 3)
    else:
        return np.argmax(Q[state[0], state[1]])
    
def take_action(state, action):
    if action == 0: #   move up
        next_state = (max(state[0]-1, 0), state[1])
    elif action == 1:   #   move down
        next_state = (min(state[0]+1, n_rows-1), state[1])
    elif action == 2:   #   move left
        next_state = (state[0], max(state[1]-1, 0))
    elif action == 3:   #   move right
        next_state = (state[0], min(state[1]+1, n_cols-1))
    if next_state in cliff:
        reward = -100
        next_state = start
    elif next_state == end:
        reward = 0
    else:
        reward = -1
    return next_state, reward

def q_learning(epsilon, alpha, gamma, episodes):
    Q = np.zeros((n_rows, n_cols, 4))

    for i in range(episodes):
        state = start
        action = choose_action(state, Q, epsilon)
        total_reward = 0
        iteration = 0

        while state != end:
            action = choose_action(state, Q, epsilon)
            next_state, reward = take_action(state, action)
            Q[state[0], state[1], action] += alpha * (reward + gamma * np.max(Q[next_state[0], next_state[1]]) - Q[state[0], state[1], action])
            state = next_state
            total_reward += reward
            iteration += 1

    return iteration

def prob_walk(n):
    x = 0
    y = 0
    converged = False
    steps = 0

    for i in range(n):
        dx = random.choice([-1, 0, 1])
        dy = random.choice([-1, 0, 1])

        x += dx
        y += dy

        #!   making sure that the particle stays within the bounds of the grid
        x = max(min(x, 3), 0)
        y = max(min(y, 3), 0)

        steps += 1

        #!   checking for goal state
        if x == 3 and y == 3:
            converged = True
            break
    if converged:
        return steps

def main():
    if len(sys.argv) < 3:
        print(f'usage: {sys.argv[0]} <steps> <episodes>')
        sys.exit()
    
    steps = int(sys.argv[1])
    episodes = int(sys.argv[2])
    steps_prob_walk = prob_walk(steps)
    steps_q_learning = q_learning(0.2, 0.5, 0.9, episodes)

    print('Symmetric 2D Walk: ', steps_prob_walk)
    print('Q-learning: ', steps_q_learning)

if __name__ == '__main__':
    main()

        