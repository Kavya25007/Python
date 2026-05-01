""" 
np.delete = Deletes elements from an array based on index/position
np.delete(array, index, axis=None)
index = 0 -> means delete first row
index = 1 -> means delete second row

"""

import numpy as np
arr_2d = np.array([[1,2,3], [4,5,6]])
new_array = np.delete(arr_2d, 1 , axis = 0)
print(new_array)