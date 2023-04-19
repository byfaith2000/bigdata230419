import numpy as np

# array : 입력 데이터(리스트, 튜플, 배열 또는 순차형데이터)를 ndarray로 변환.
# dtype이 명시되지 않으면 자료형을 추정하고 입력데이트는 복사해서 생성
# array는 콤마가 없고 리스트는 콤마가 있다.
data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)
print(arr1)
print(type(arr1)) #<class 'numpy.ndarray'>
print(arr1.dtype) # float64
print()
print('--------------------------------')
arr2 = np.array(data1, dtype=np.int32) # 정수 데이타로 변경됨
print(arr2)
print()

data2 = [[1,2,3,4], [5,6,7,8]]
print(data2)
print(type(data2)) # 이건 리스트가 되고
arr2 = np.array(data2)
print(arr2, '\n')
print(type(arr2)) # 이건 n차 array가 된다.

print('--------------------------------')
print(arr2.ndim) # 2차다.
print(arr2.shape) # 2행 4열이다.
print(arr2.dtype,'\n') # 정수형이다.
print('--------------------------------')
arr3 = arr2.astype(np.float32) # 실수형으로 변경
print(arr3)
print()

# range함수
# range(A) : 0부터 A-1까지의 정수 반환
# range(A, B) : A부터 B-1까지 정수 반환
# range(A,B,C) : A부터 B-1까지 C간격으로 정수 반환
# 파이썬에서 기본적으로 제공하는 메소드인 range와 차이점은,
# range 함수에는 정수단위만 지원하나, np.arange는 실수 단위도 표현 가능
# 또한 range 매소드는 range iterator 자료형을 반환, np.arange 매소드는 numpy array 자료형 반환

# for 숫자변수 in 범위 :
#       코드
for i in range(7) :
  print(i)

# arange : 내장 range함수와 유사하나 리스트 대신 ndarray반환, 일정한 간격으로 배열된 배열을 만드는 함수 array range??
arr5 = np.arange(1, 10, 2)
print(arr5)

print(np.arange(10))
print(type(arr5)) #<class 'numpy.ndarray'>
print()

#linespace : 주어진 데이터범위를 일정한 간격으로 분할해서 배열을 만든 후 튜플로 반환
arr6 = np.linspace(-3, 3, 5)
print(arr6, type(arr6))
print()

# ones : 주어진 dtype으로 배열을 생성하고 내용을 모두 1로 초기화
arr7 = np.ones([3,4])
print(arr7)
print()

# zeros : ones와 같지만 내용을 0으로 채움
arr8 = np.zeros([3,4])
print(arr8)
print()

# empty : 메모리를 할당하여 새로운 배열을 생성하지만 값을 초기화하지 않음
arr9 = np.empty([3,4])
print(arr9)
print()

arr10 = np.full([3,4], 100)
print(arr10)
print()

print(np.zeros_like(arr10)) # arr10 n차 array와 같은 shape의 zeros array 구할 때



