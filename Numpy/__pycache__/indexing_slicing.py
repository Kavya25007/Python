'''
array[index] # 1d Array
array[row , column] #2d Array
'''

import numpy as np
arr1 = np.array([2,4,6,1])
print(arr1[3])
print(arr1[-2])
print(arr1[-1])


'''
slicing

array[start:stop:step]
array[start:end] = start to end - 1
a'''

arr = np.array([3,5,2,6,7,24,66])
print(arr[1:5])
print(arr[:5])
print(arr[::2])