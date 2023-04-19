# 정렬
import numpy as np

np.random.seed(12345)
arr1 = np.random.randn(5,3)
print(arr1)
print()

arr1.sort(axis=0)
print(arr1)
print()

arr1.sort(axis=1)
print(arr1)
print()

arr2 = np.array([5,0,1,3,2])
arr3 = arr2.argsort()  # argsort() : 정렬된 행렬의 인덱스를 반환
# arr2를 오름차순으로 소팅하되 인덱스값을 반환해라
print(arr3)

print(arr2[arr3])  #  인덱스에 있는 값 반환

print()
print('----------------------------------------------------')
np.random.seed(12345)

arr = np.random.randn(3,5)
arr[0] = values
print(arr)
print()

print(arr[:, arr[0].argsort()])
# 정확히 이해는 안됨
# a.argsort()는 a라는 ndarray를 오름차순 정렬하기 위한 index의 순서를 배열로 반환한다.