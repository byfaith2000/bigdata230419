# 집합 함수

import numpy as np

names = ['bob', 'joe', 'will', 'bob', 'will', 'joe', 'joe']
print(names)
print(np.unique(names))  # 중복 제거
print()

arr1 = np.array([1,2,3,4])
arr2 = np.array([3,4,5,6])

print(np.union1d(arr1, arr2))  # 두개의 배열의 합집합을 정렬하여 반환
print(np.intersect1d(arr1, arr2))  # 두개의 배열의 교집합을 정렬하여 반환
print(np.setdiff1d(arr1, arr2))  # 첫번째 배열에서 두번째 배열을 뺀 차집합
print(np.setxor1d(arr1, arr2))  # 두 배열 합집합에서 교집합을 뺀 대칭차집합을 반환