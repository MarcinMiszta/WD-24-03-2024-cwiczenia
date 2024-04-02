import numpy as np

def funkcja(n):
    mat = np.arange(1, n*n + 1)
    mat = mat.reshape((n, n))
    return mat
print(funkcja(6))