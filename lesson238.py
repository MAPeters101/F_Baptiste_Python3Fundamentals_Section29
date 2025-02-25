import numpy as np

arr = np.arange(12)
print(arr)
print(arr.shape)
m1 = arr.reshape(4,3)
print(m1)
m2 = arr.reshape(2,6)
print(m2)
m3 = m2.reshape(6,2)
print(m3)
print()
print(arr is m1)
print(m1 is m2)
print(m2 is m3)
print()

print(arr)
print(m1)
print(m2)
arr[0] = 100
print(arr)
print(m1)
print(m2)
print(m3)
print('-'*80)

m1[3][2] = 200
print(arr)
print(m1)
print(m2)
print(m3)
print('-'*80)





