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
print('-'*80)

print(list(range(2,11,2)))
print(np.arange(2,11,2))
print(np.arange(2,11,2, dtype=np.uint8))
print(np.linspace(2,10,num=5))
print(np.linspace(2,10,5))
print(np.linspace(2,10,10))
print('-'*80)

import math
x_coords = np.linspace(-2*math.pi, 2*math.pi, 50)
print(x_coords)
y_values = np.array([math.sin(x) for x in x_coords])
print(y_values)
print('-'*80)


print(np.random.random(5))
np.random.seed(0)
print(np.random.random(5))
np.random.seed(0)
print(np.random.random(5))
print()

print(np.random.random((5,3)))
print()

np.random.seed(0)
print(np.random.randint(1,10,50))
print('-'*80)

from numpy import random as npr
npr.seed(0)
print(npr.randint(1,6+1,10))
npr.seed(0)
print(npr.randint(1,7,(10,2)))
npr.seed(0)
print(npr.randint(1,7,(10,5)))


