import numpy as np

np.random.seed(12345)

data = np.random.normal(loc=10, scale=3, size=(4,3))
# loc는 분포의 평균, scale은 표준편차임
print(data)
print()

data2 = np.random.randint(low=0, high=10, size=10)
# 0에서 10사이에 10개의 난수 발생
print(data2)

arr1 = np.arange(10)
print(arr1)
print()
np.random.shuffle(arr1)
print(arr1)
print()

arr2 = np.arange(10)
print(arr2)
arr3 = np.random.permutation(arr2)
print(arr3)