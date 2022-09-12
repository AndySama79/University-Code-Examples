# Imports
import numpy as np
import matplotlib.pyplot as plt
import time

# my function for matrix mulitplication
def matrix_product(M, N):
    rows = N.shape[0]
    cols = M.shape[1]
    A = np.zeros((M.shape[0], N.shape[1]))

    if rows != cols:
        return -1
    else:
        for i in range(0, M.shape[0]):
            for j in range(0, N.shape[1]):
                A[i][j] = (sum(M[i, :] * N[:, j]))
    
    return A

# main 
np_avg = []
my_avg = []

while i < 129:
    M = np.random.rand(i, i)
    np_time = []
    my_time = []

    st = time.time()
    A = np.matmul(M, M)
    time.sleep(2)
    et = time.time()
    np_time.append(et-st-2)

    st = time.time()
    A = matrix_product(M, M)
    time.sleep(2)
    et = time.time()
    my_time.append(et-st-2)

    i = i * 2

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
plt.title("Numpy vectorization v/s Naive Algorithm")

plt.show()