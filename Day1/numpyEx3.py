# 색인과 슬라이싱 : numpy배열은 인덱싱[i]과 슬라이싱[i:j]과 불 인덱싱이 가능함
import numpy as np

arr = np.arange(10)
print(arr)
print(arr[5])
print(arr[5:8]) # 5 ~ 8-1
arr[5:8] = 12  # arr n차 어레이의 인덱싱 5에서 7을 12로 채워라
print(arr)

print('-------------------------------------')
arr1 = np.array([5,7,9,1,2,7,6,4,8])
print(arr1)

print(arr1[2])
print(arr1[2:7])
arr1[0] = 100
print(arr1)
print()
print('-------------------------------------')

arr2 = np.array([[4,2,1,6],
                 [8,9,2,4],
                 [1,3,5,7]])
print(arr2[1,2]) # 정답 2, 숫자는 인덱스
print(arr2[1][2]) # 정답 2, 숫자는 인덱스
print(arr2[1:, 2:]) # 정답 2, 숫자는 인덱스
print(arr2[1:][2:]) # 숫자는 인덱스
print()

print(arr2[1:, 2]) # 숫자는 인덱스, 리스트 형태
print()
print(arr2[1:, [2]]) # 숫자는 인덱스, 2차 배열형태
print()
print(arr2[1:, 2:3])