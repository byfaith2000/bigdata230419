import numpy as np

xarr = np.array([1.1, 1.2, 1.3, 1.4])
yarr = np.array([2.1, 2.2, 2.3, 2.4])
cond = np.array([True, False, True, False])

result = [x if c else y for x, y, c in zip(xarr, yarr, cond)] #리스트

print(result)
print()

print(np.where(cond, xarr, yarr))  # n차 어레이, 조건이 맞으면 xarr, 아니면 yarr
print()


np.random.seed(12345)
arr = np.random.randn(4,4)
print(arr)
print()

print(np.where(arr > 0.2, 2, -2))
print()

print(np.where(arr > 0, 2, arr))