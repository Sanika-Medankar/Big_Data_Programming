import numpy as np

arr = np.array([1, 2, 3])
newArr = np.append(np.repeat(arr, 3), np.tile(arr, 3))
print(newArr)
