import os
import sys
import numpy as np
import random
import matplotlib.pyplot as plt
import time

#TODO:  define the grid world and the cliffs
n_rows = 4
n_cols = 12
cliff = [(3, col) for col in range(1, 11)]

#TODO:  define start and end states
start = (3, 0)
end = (3, 11)

#TODO:  helper functions:
#*  1)  choose_action(state)    ->  defines the action selection method
#*  2)  take_action(state, action)  ->  defines the action execution method

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

#TODO:  SARSA algorithm
def sarsa(epsilon, alpha, gamma, episodes):
    #TODO: define Q-table of SARSA
    Q = np.zeros((n_rows, n_cols, 4))
    total_rewards = np.zeros(episodes)
    total_iterations = np.zeros(episodes)

    for i in range(episodes):
        state = start
        action = choose_action(state, Q, epsilon)
        total_reward = 0
        iteration = 0

        while state != end:
            next_state, reward = take_action(state, action)
            next_action = choose_action(next_state, Q, epsilon)
            Q[state[0], state[1], action] += alpha * (reward + gamma * Q[next_state[0], next_state[1], next_action] - Q[state[0], state[1], action])
            state = next_state
            action = next_action
            total_reward += reward
            iteration += 1

        total_rewards[i] = total_reward
        total_iterations[i] = iteration

    return total_rewards, total_iterations

#TODO:  Q-learning algorithm
def q_learning(epsilon, alpha, gamma, episodes):
    #TODO:  define the Q-table for Q-learning
    Q = np.zeros((n_rows, n_cols, 4))
    total_rewards = np.zeros(episodes)
    total_iterations = np.zeros(episodes)

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

        total_rewards[i] = total_reward
        total_iterations[i] = iteration

    return total_rewards, total_iterations

#TODO:  main function to drive the program
def main():
    if len(sys.argv) < 6:
        print(f'usage : {sys.argv[0]} <trials> <episodes> <epsilon> <alpha> <gamma>')
        sys.exit()
    trials = int(sys.argv[1])
    episodes = int(sys.argv[2])
    epsilon = float(sys.argv[3])
    alpha = float(sys.argv[4])
    gamma = float(sys.argv[5])

    print(f'alpha:{alpha}, gamma:{gamma}, epsilon:{epsilon}')

    total_rewards_sarsa, total_iterations_sarsa = np.zeros((trials, episodes)), np.zeros((trials, episodes))
    total_rewards_qlearning, total_iterations_qlearning = np.zeros((trials, episodes)), np.zeros((trials, episodes))

    print("Starting Trials...")

    start = time.time()

    for i in range(trials):
        total_rewards_sarsa[i], total_iterations_sarsa[i] = sarsa(epsilon, alpha, gamma, episodes)
        total_rewards_qlearning[i], total_iterations_qlearning[i] = sarsa(epsilon, alpha, gamma, episodes)
    
    end = time.time()

    print(f'Took {end - start} seconds to complete.')

    avg_rewards_sarsa = np.mean(total_rewards_sarsa, axis=0)
    avg_iterations_sarsa = np.mean(total_iterations_sarsa, axis=0)
    avg_rewards_qlearning = np.mean(total_rewards_qlearning, axis=0)
    avg_iterations_qlearning = np.mean(total_iterations_qlearning, axis=0)

    print(f'For SARSA')
    print(f'Max average reward SARSA: {np.max(avg_rewards_sarsa)}')
    print(f'Max average iterations SARSA: {np.max(avg_iterations_sarsa)}')
    print("\n")
    print(f'For Q-learning')
    print(f'Max average rewards Q-Learning: {np.max(avg_rewards_qlearning)}')
    print(f'Max average iterations Q-learning: {np.max(avg_iterations_qlearning)}')

    fig, ax = plt.subplots()
    ax.plot(avg_iterations_sarsa)
    ax.plot(avg_iterations_qlearning)
    ax.legend(["SARSA", "Q-Learning"])
    ax.set_xlabel("iteration -->")
    ax.set_ylabel("steps taken to converge -->")
    fig.suptitle(f"Convergence: SARSA v/s Q-learning\n epsilon:{epsilon}, alpha:{alpha}, gamma:{gamma}")
    plt.savefig("Convergence.png")
    plt.show()

if __name__ == "__main__":
    main()