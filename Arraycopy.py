import numpy as np
arr = np.arange(10)

out = arr.copy()

out[out%2 == 1] = -1

print('Modified Array')
print(out)

print('\nOriginal Array')
print(arr)

array1 = np.array([[23,49,56,67],[28,47,78,30]])
#Sort ascending order
array2 = np.sort(array1)
print(array2)
#Sort descending order- row wise
print(np.sort(array1)[:,::-1])
#Sort descending order- column wise
print(np.sort(array1)[::-1])
#Sort ascending order - column wise
print(np.sort(array1, axis = 0))