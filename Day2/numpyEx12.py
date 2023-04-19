import numpy as np

arr1 = np.arange(1,7).reshape(2,3)
arr2 = np.arange(7,13).reshape(2,3)
print(arr1)
print(arr2)
print()

print(np.concatenate([arr1, arr2], axis=0))
print()
print(np.concatenate([arr1, arr2], axis=1))
print()

print(np.vstack([arr1, arr2]))  # 밑으로 붙이기
print(np.hstack([arr1, arr2]))  # 옆으로 붙이기
print()

arr3 = np.arange(6)
arr4 = np.arange(6).reshape(3,2)
arr5 = np.random.randn(3,2)
print(arr3)
print()
print(arr4)
print()
print(arr5)
print()

print(np.r_[arr4, arr5])  # 밑으로 붙이기
print()

print(np.c_[arr4, arr5])  # 옆으로 붙이기
print()

print(np.c_[np.r_[arr4, arr5], arr3])