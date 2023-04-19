import numpy as np

# numpy 배열은 for반복문을 작성하지 않고 데이터를 일괄 처리할 수 있는 벡터화를 지원한다.

arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([[4,8,2],[1,9,7]])
print(arr1)
print()
print(arr2)
print()

print(arr1 + arr2)
print()

print(arr1 * 4)
print()

print(1 / arr1)
print()

print(arr1 > arr2)
print()

print(arr2 > 4)

print(arr1 ** 0.5) # 루터

