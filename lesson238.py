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

m3 = arr.reshape(3,4).copy()
print(m3)
print()
m3[0][0] = 0
print(m3)
print(arr)
print()

m3 = arr.copy().reshape(3,4)
print(m3)
print()
m3[0][0] = 0
print(m3)
print(arr)
print()
print('-'*80)

m = np.array(
    [
        [1,2,3],
        [4,5,6]
    ]
)
print(m.shape)
print(m)
arr2 = m.reshape((6,))
print(arr2)
arr2 = m.reshape(6)
print(arr2)
arr2[2] = 30
print(arr2)
print(m)
print('-'*80)




