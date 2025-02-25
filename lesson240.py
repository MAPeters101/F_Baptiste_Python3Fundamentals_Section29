import numpy as np
a1 = np.arange(1,6)
print(a1)
a2 = np.arange(1,11).reshape(2,5)
print(a2)
print()
s1 = np.vstack((a1, a2))
print(s1)
print('-'*80)

try:
    np.vstack((np.arange(3), a2))
except ValueError as ex:
    print(ex)
print('-'*80)

a1 = np.array([1,2,3,4])
a2 = np.array([0.1,0.2,0.3,0.4])
result = np.vstack((a1, a2))
print(a1)
print(a2)
print()
print(result)
print(result.dtype)
print('-'*80)

a1 = np.array([1,2,3,4], dtype=np.uint8)
a2 = np.array([1000,2000,3000,4000], dtype=np.uint16)
result = np.vstack((a1, a2))
print(a1)
print(a2)
print()
print(result)
print(result.dtype)
print('-'*80)


print(np.vstack(
    (
        np.arange(5),
        np.linspace(0,1,5),
        np.eye(5)
    )
))

print('-'*80)

a1 = np.array([1,2], dtype=np.uint8)
a2 = np.array([2,3], dtype=np.uint64)
a3 = np.array([4,5], dtype=np.int32)
result = np.vstack([a1, a2, a3])
print(result)
print(result.dtype)
print('-'*80)





