"""
stacking =combining arrays along a row or column-wise 
np.vstack() = Adds arrays one below another (row-wise)
np.hstack() = Adds arrays side by side (column-wise)
"""

import numpy as np 

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

print(np.vstack((arr1 , arr2)))
print(np.hstack(((arr1 , arr2))))