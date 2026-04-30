"""
np.insert(array , index , value , axis = None
array = original array
index = on which index have to insert value
value = the actual variable

For 1D- Array (axis(optional))
For 2D- Array 
axis = 0 means row-wise
axis = 1 means column wise
"""

import numpy as np 
arr = np.array([1,2,3,4,5,6])
New_Array = np.insert(arr,2,100)
print(arr) # original Array
print(New_Array)