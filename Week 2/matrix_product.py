import numpy as np

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
