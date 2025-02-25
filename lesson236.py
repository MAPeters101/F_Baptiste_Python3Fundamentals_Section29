import numpy as np

a = np.zeros(5)
print(a)
print(a.dtype)

a = np.zeros(5, dtype=int)
print(a)
print(a.dtype)

a = np.zeros(5, dtype=float)
print(a)
print(a.dtype)
print()

a = np.zeros((4, 3), dtype=np.uint8)
print(a)
print(a.dtype)
print('-'*80)

m = np.ones((10,2), dtype=float)
print(m)
print(m.dtype)
print()

m = np.full((2,5), 3.14, dtype=np.float32)
print(m)
print(m.dtype)
print()

m = np.eye(5)
print(m)
print(m.dtype)
print()

m = np.eye(5, dtype=int)
print(m)
print(m.dtype)
print()

m = np.eye(5, 3, dtype=np.uint16)
print(m)
print(m.dtype)
print()



