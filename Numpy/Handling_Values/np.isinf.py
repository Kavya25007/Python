#np.isinf()- checks infinite values and returns True or False
import numpy as np 

arr = np.array([1,2,np.inf , 4 , -np.inf, 6])

print(np.isinf(arr))
