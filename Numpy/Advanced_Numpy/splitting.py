"""
np.split() -> split array in equal parts
np.hsplit() -> split array horitonzally
np.vsplit() -> split array vertically
"""
import numpy as np
arr = np.array([2,1,3,4,9,6])
print(np.split(arr, 2))

print(np.hsplit(arr , 2))
print(np.vsplit(arr , 2))