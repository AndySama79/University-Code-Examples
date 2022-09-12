import my_algo_c
import matrix_product
import numpy as np
import time
import matplotlib.pyplot as plt

np_avg = []
my_avg = []
i = 2
while i <= 256:
    M = np.random.rand(i, i)

    np_time = []
    my_time = []

    for j in range(30):
        st = time.time()
        A = np.matmul(M, M)
        et = time.time()
        np_time.append(et-st)
    
    np_avg.append(np.average(np_time))

    for j in range(30):
        st = time.time()
        A = my_algo_c.matrix_product(M, M)
        et = time.time()
        my_time.append(et-st)

    my_avg.append(np.average(my_time))

    i = i * 2

# plotting differences
X = np.arange(len(np_avg))
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.bar(X + 0.00, np_avg, color='#FF9F29', width=0.25)
ax.bar(X + 0.25, my_avg, color='#1A4D2E', width=0.25)
ax.plot(X, np_avg, color='#FF9F29', label="numpy average")
ax.plot(X, my_avg, color='#1A4D2E', label="naive average")
leg = ax.legend(loc="upper left", frameon=False)

plt.xlabel("Dimensions in $2^{x}$")
plt.ylabel("Execution time")
plt.title("Numpy vectorization v/s Naive Algorithm")

plt.show()

    





