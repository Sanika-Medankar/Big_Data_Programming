import numpy as np

arr = np.arange(9).reshape(3,3)

print(arr)
# print(np.transpose(arr))
# print(np.swapaxes(arr, 0, 1))
arr[:,[2,1]] = arr[:,[1,2]]
print(arr)