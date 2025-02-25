import numpy as np

a1 = np.array([1,2,3,4])
a2 = np.array((0.1,0.2,0.3,0.4))
print(a1)
print(type(a1))

print(a2)
print(type(a2))
print()
print(a1.dtype)
print(a2.dtype)
print('-'*80)

a = np.array([1,2,3,4], dtype=np.uint8)
print(a.dtype)
print()
#a = np.array([1,2,3,300], dtype=np.uint8)
a = np.array([1,2,3,255], dtype=np.uint8)
print(a)
#a = np.array([1,2,3,256], dtype=np.uint8)
#print(a)
#a = np.array([127], dtype=np.int8)
print(a)
#a = np.array([128], dtype=np.int8)
#print(a)
print('-'*80)

a = np.array([1,2,3.14])
print(a)
print(a.dtype)

a = np.array([1,2,9.9, 9.1], dtype=np.int64)
print(a)
print(a.dtype)

a = np.array([1, 3.14, 'x'])
print(a)
print(a.dtype)

#a = np.array([1, 3.14, 'x'], dtype=np.int64)
#print(a)
#print(a.dtype)
print('-'*80)

