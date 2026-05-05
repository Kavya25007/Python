#Converting List to Array

import numpy as np

#With default values
#np.zeros(coloums , rows)

zeros_array = np.zeros(6)
print(zeros_array)

#np.ones(coloums , rows)

ones_array = np.ones((6, 9))
print(ones_array)

#full function
#full(shape , value)

filled_array = np.full((2,2),7)
print(filled_array)