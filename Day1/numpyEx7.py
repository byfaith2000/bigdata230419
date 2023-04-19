import numpy as np

np.random.seed(1234)
arr1 = np.random.randn(5,4)
print(arr1)
print()

print(arr1.mean(), arr1.std(), arr1.sum())
print()

print(arr1.mean(axis=0))
print()

print(arr1.mean(axis=1))
print()

print(arr1.std(axis=1))
print()

arr2 = np.arange(8)
print(arr2)
print(arr2.cumsum())
print()

arr3 = np.array([[0,1,2],
                [3,4,5],
                [6,7,8,]])
print(arr3)
print()

print(arr3.cumsum(axis=0))
print()

print(arr3.cumprod(axis=1))