"""
np.append( )= Used to add elements at the end of an array
✔ Returns a new array (original unchanged)
✔ Default → flattens array if axis not given
✔ axis=0 → add row
✔ axis=1 → add column
"""

import numpy as np 
arr = np.array([1,2,3,4,5,6])
New_Array = np.append(arr , [ 40,50,60])

print(New_Array)