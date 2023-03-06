import numpy as np

#TODO:  initialize Q-values
Q = np.zeros(2)

#TODO:  set-up hyper-parameters
T = 1 #   temperature
alpha = 0.9 #   learning rate
episodes = 1000

#TODO:  defining reward for each action (unknown)
def get_reward(action):
    if action == 0:
        return np.random.normal(1, 1)
    else:
        return np.random.normal(2, 1)
    
#TODO:  simulate for given number of episodes
for i in range(episodes):
    #TODO:  calculate Boltzmann probabilities
    p_A1 = np.exp(Q[0] / T) / (np.exp(Q[0] / T) + np.exp(Q[1] / T))
    p_A2 = 1 - p_A1

    #TODO:  choose action based on probability
    if np.random.uniform() < p_A1:
        action = 0
    else:
        action = 1
    
    reward = get_reward(action)

    #TODO:  update Q-values
    Q[action] = Q[action] + alpha * (reward - Q[action])

#TODO:  get the final Q-values and best action
print("Final Q-values", Q)
if Q[0] > Q[1]:
    print("Best Action: A_1")
else:
    print("Best Action: A_2")