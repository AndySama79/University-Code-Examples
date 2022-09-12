import numpy as np
import time
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

# A = np.random.rand(100, 100)
# B = np.random.rand(100, 100)

# st = time.time()
# matrix_product(A, B)
# time.sleep(1)
# et = time.time()
# print("My algo: ", et-st-1)

# st = time.time()
# np.matmul(A, B)
# time.sleep(1)
# et = time.time()
# print("Numpy: ", et-st-1)