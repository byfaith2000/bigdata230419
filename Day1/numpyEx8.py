import numpy as np

arr1 = np.array([True,False,True,True])
print(arr1.sum())
print()

bools = np.array([[False, False, True, False],
                  [False, False, True, True]])
print(bools)
print()

print(bools.all(axis=0))  # 열방향으로 모두 True인 경우 True
print()

print(bools.any(axis=0))  # 열방향으로 하나라도 True인 경우 True
print()

# np.random.seed : seed를 통한 난수 생성
# np.random.randint : 균일 분포의 정수 난수 1개 생성
# np.random.rand : 0부터 1사이의 균일 분포에서 난수 matrix array 생성
# np.random.randn : 가우시안 표준 정규 분포에서 난수 matrix array 생성
np.random.seed(12345)
data = np.random.randn(10,3) * 3
print(data)
print()

print('--------------------------------------')
print((data > 3))
print()

print(data[(data > 3).any(axis=1)]) # 데이타가 3보다 큰 것 중에 행방향으로 하나라도 True이면 값을 표시
print()

# print(data[:, (data > 5)])
print(data[:, (data > 5).any(axis=0)])  # 열방향으로 5이상이 하나라도 있는 열값