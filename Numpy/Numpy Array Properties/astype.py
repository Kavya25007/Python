#astype = convert one dataype into another datatype

import numpy as np
arr = np.array([1,2,3])
print(arr.dtype)
print(arr.astype(float))


arr1 = np.array([1.2 , 2.5, 6.7])
print(arr1.dtype)
print(arr1.astype(int))
