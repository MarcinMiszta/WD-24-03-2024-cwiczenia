import numpy as np

def generuj(n):
    return np.linspace(1, 7, n)[::-1]


print(generuj(4))
print(np.diag(generuj(4)))


