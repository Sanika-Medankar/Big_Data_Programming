import numpy as np 


#   Exercise 1
print("\nExercise 1\n")
arr = np.array([0,1,2,3,4,5,6,7,8,9])
print(arr)

arr[arr % 2 != 0] = -1
print(arr)


#   Exercise 2
print("\nExercise 2\n")
arr = np.arange(10)
print(arr)
print(np.reshape(arr, (2,-1)))


#   Exercise 3
print("\nExercise 3\n")
arr = np.array([1, 2, 3])
newArr = np.append(np.repeat(arr, 3), np.tile(arr, 3))
print(newArr)


#   Exercise 4
print("\nExercise 4\n")
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])

outputArray = np.intersect1d(a,b)
print(outputArray)


#   Exercise 5
print("\nExercise 5\n")
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])

outputArray = np.in1d(a,b)
print(np.where(outputArray == True))


#   Exercise 6
print("\nExercise 6\n")
arr1 = np.random.uniform(5, 10, size = (5, 3))

print(arr1)


#   Exercise 7
print("\nExercise 7\n")
arr = np.arange(15)
np.set_printoptions(threshold=6)
print(arr)


#   Exercise 8
print("\nExercise 8\n")
np.random.seed(100)

rand_arr = np.random.random([3,3])/1e3

np.set_printoptions(precision=6, suppress=True)

print(rand_arr)


#   Exercise 9
print("\nExercise 9\n")
arr = np.arange(9).reshape(3,3)

print("Original Array\n{}".format(arr))
# print(np.transpose(arr))
# print(np.swapaxes(arr, 0, 1))
arr[:,[2,1]] = arr[:,[1,2]]
print("\nAfter transformation\n{}".format(arr))


#   Exercise 10
print("\nExercise 10\n")
arr = np.arange(9).reshape(3,3)
print("Original Array\n{}".format(arr))
arr[[0,1],:] = arr[[1,0],:]
print("\nAfter transformation\n{}".format(arr))