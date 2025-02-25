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
