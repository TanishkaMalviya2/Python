import numpy as np
arr=np.linspace(0,1,10)
print(arr.dtype , arr.shape)


'''np.array(data)          → converts existing list/tuple into an array
np.zeros(shape)         → array of given shape filled with 0s (pre-allocate)
np.ones(shape)          → array of given shape filled with 1s
np.arange(start,stop,step) → like range(), but returns array; you fix STEP SIZE
np.linspace(start,stop,num) → evenly spaced points; you fix COUNT, NumPy picks step
.dtype                  → tells you the data type of elements (int64, float64, etc.)
.shape                  → tuple showing size per dimension, e.g. (10,) = 1D, 10 elements'''