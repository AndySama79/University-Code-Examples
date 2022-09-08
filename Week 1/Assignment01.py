# Imports
import numpy as np
import matplotlib.pyplot as plt
import time

# my function for matrix mulitplication
def my_mul(M, N):
    rows = M.shape[0]
    cols = N.shape[1]
    A = np.zeros((rows, cols))

    if rows != cols:
        print("Not Compatible")
        return
    else: 
        for i in range(0, rows):
            for j in range(0, cols):
                A[i][j] = sum(M[i, :] * N[:, j])
    
    return A

# main 
np_time = []
my_time = []

for i in range(10, 101, 10):
    M = np.random.rand(i, i)

    st = time.time()
    A = np.matmul(M, M)
    time.sleep(2)
    et = time.time()
    np_time.append(et-st-2)

    st = time.time()
    A = my_mul(M, M)
    time.sleep(2)
    et = time.time()
    my_time.append(et-st-2)

# plotting differences
X = np.arange(10)
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.bar(X + 0.00, np_time, color='#FF9F29', width=0.25)
ax.bar(X + 0.25, my_time, color='#1A4D2E', width=0.25)
ax.plot(X, np_time, color='#FF9F29')
ax.plot(X, my_time, color='#1A4D2E')

plt.xlabel("Dimensions")
plt.ylabel("Time")
plt.title("Numpy vectorization v/s My Algorithm")

plt.show()