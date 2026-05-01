"""
concatenate = Used to join arrays together
np.concatenate((array1, array2), axis=0)

axis = 0 → ↓ (downward, rows)
axis = 1 → → (sideways, columns)

"""
import numpy as np

a = np.array([1, 2])
b = np.array([3, 4])

c = np.concatenate((a, b))
print(c)


a = np.array([[1, 2]])
b = np.array([[3, 4]])

c1 = np.concatenate((a, b), axis=1)
print(c1)