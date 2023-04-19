import numpy as np

np.random.seed(12345)
arr = np.random.randn(5,6)
print(arr)
print()

#1. 전체의 최대값
print(arr.max())
print()

#2. 각행의 합
print(arr.sum(axis=1))

#3. 각 열의 평균
print(arr.mean(axis=0))

print('---------------------------------')
#4. 첫 번째 열 값으로 모든 행으로 정렬
print(arr[np.argsort(arr[:,0])])
print()
#5. 두 번째 행 값으로 모든 열의 정렬
print(arr[:, np.argsort(arr[1])])