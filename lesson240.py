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

print(a1)
print(a1.dtype)
c1 = a1.astype(np.float32)
print(a1)
print(a1.dtype)
print(c1)
print(c1.dtype)
print('-'*80)

result = np.vstack(
    (
        a1.astype(np.int64),
        a2.astype(int),
        a3.astype(np.int64)
    )
)
print(result)
print(result.dtype)
print('-'*80)

a1 = np.array([1,2,3,4])
a2 = np.array([10,20,30,40])
result = np.vstack((a1, a2))
print(a1)
print(a2)
print()
print(result)
print('='*80)
print()
a1[0] = 100
result[0][1] = 2000
print(a1)
print(a2)
print()
print(result)
print()
print('-'*80)

a1 = np.linspace(0, 5, 10).reshape(5,2)
print(a1)
np.random.seed(0)
a2 = np.random.randint(0,10,10).reshape(5, 2)
print(a2)
result = np.hstack((a1, a2))
print(result)
print()

a1 = np.linspace(0, 5, 10).reshape(5,2)
print(a1)
np.random.seed(0)
a2 = np.random.randint(0,10,20).reshape(5, 4)
print(a2)
result = np.hstack((a1, a2))
print(result)
print()

