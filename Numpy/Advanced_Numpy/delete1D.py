""" 
np.delete = Deletes elements from an array based on index/position
np.delete(array, index, axis=None)
"""
import numpy as np
arr = np.array([1,2,3,4])
new_array = np.delete(arr , 3)
print(new_array)

