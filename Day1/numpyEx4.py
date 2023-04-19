import numpy as np

arr1 = np.array([[4,2,1,7],
                 [33,77,11,22]])
print(arr1)
print()

barr1 = np.array([[True,False,False,True],
                  [False,False,True,True]])
print(barr1)
print()

print(arr1[barr1])  # True만 뽑아내어 리스트 만듬
print()

barr2 = np.array([False, True])
print(barr2)
print()

print(arr1[barr2])
print()

barr3 = np.array([True,False,True,False])
print(barr3)
print()

print(arr1[:, barr3])
print()

print(arr1 > 5)
print()

print(arr1[arr1 > 5])
print()

np.random.seed(1234)
data = np.random.randn(7,3)
print(data)
print()

names = np.array(['bob','joe','will','bob','will','joe','joe'])
print(names)
print()

print(names == 'bob')
print()

print(data[names == 'bob'])  # data[]<--[]안에 인덱스 한개 있으면 행을 의미한다?
print()

print(data[names == 'bob', 1:])
print()

data[data < 0] = 0
print(data)