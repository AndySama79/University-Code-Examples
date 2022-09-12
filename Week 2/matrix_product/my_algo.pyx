import numpy as np

def matrix_product(double[:, :] M, double[:, :] N):
    
    cdef Py_ssize_t rows = N.shape[0]
    cdef Py_ssize_t cols = M.shape[1]
    # A = np.zeros((M.shape[0], N.shape[1]))

    A = np.empty((M.shape[0], N.shape[1]), dtype=float)
    cdef double[:, :] res = A

    cdef i, j, k

    if rows != cols:
        return -1
    else:
        for i in range(0, M.shape[0]):
            for j in range(0, N.shape[1]):
                for k in range (0, cols):
                    A[i, j] += (M[i, k] * N[k, j])

    return A

