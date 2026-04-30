import numpy as np
arr = np.array([[1,2,5], [5,6,9]])

#insert new row at index 1
new_array = np.insert(arr , 1, [23,7,2], axis = 0)
print(new_array)

new_array2D = np.insert(arr , 3 , [5,6,7], axis = None)
print(new_array2D)