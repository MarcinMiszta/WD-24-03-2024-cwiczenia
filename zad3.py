import numpy as np

def funkcja(n):
    mat = np.arange(n*n)
    mat = mat.reshape((n, n))
    return mat
print(funkcja(6))