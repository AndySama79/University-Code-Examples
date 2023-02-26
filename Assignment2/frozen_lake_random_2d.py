import random

def frozen_lake(steps):
    x = 0
    y = 0

    for i in range(steps):
        dx = random.choice([-1, 0, 1])
        dy = random.choice([-1, 0, 1])

        x += dx
        y += dy

        #!   making sure that the particle stays within the bounds of the grid
        x = max(min(x, 3) -3)
        y = max(min(y, 3), -3)

        #!   checking for goal state
        if x == 3 and y == 3:
            return True
        
    return False