# 유니버셜 함수 - ufunc라고 불리는 유니버셜 함수는 ndarray안에 있는 데이터 원소별로 연산을 수행하는 함수이다.
import numpy as np

arr1 = np.arange(10)
print(arr1)
print(np.exp(arr1))
print()

print(np.sqrt(arr1))
print()

print(np.cos(arr1))
print()

print(np.square(arr1))
print()

print(np.sin(arr1))
print()

arr2 = np.array([-4,3,1,-9,12])
print(np.sign(arr2))  # 부호?
print()

arr3 = np.arange(8)
print(arr3)
print()

arr4 = arr3.reshape(2,4)
print(arr4)
print()

print(arr4.T)