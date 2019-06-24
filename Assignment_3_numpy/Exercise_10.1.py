import numpy as np

arr = np.arange(9).reshape(3,3)

print(arr)
arr[[0,1],:] = arr[[1,0],:]
print(arr)