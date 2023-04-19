import numpy as np
import pandas as pd

# 판다스는 numpy 단점을 보완한 것
# 데이터 pre-processing에 유리(대표적으로 누락처리)
# 축에 이름을 붙인다.
# Pandas는 양이 많아 많은 연습이 필요하다.
# 축에 대한 정보 : 시리즈, 데이타 프레임
# 시리즈는 인덱스 1개축(열)에 대응하는 Data값(열)이 있다. 
# 시리즈는 딕셔너리와 비슷, 그러나 딕셔너리 키는 유니크하고 시리즈 인덱스는 중복가능
sd1 = pd.Series([4,7,-5,3])
print(sd1)
print(type(sd1))

sd2 = pd.Series([4,7,-5,3], index=['a','b','a','c'])
print(sd2)
print()

# n디멘젼 따로 추출

print(sd2.index)
print()
print(sd2.values, type(sd2.values))

print(sd2['b'])
print()
print(sd2[['c', 'b']])
print()

sd2['b'] = 1000
print()
print(sd2)
print()

print(sd2 * 3)

print(sd2 > 3)
print()

print(sd2[sd2>3])
print()
print('----------------------------------')
print(sd2)
print(np.square((sd2)))
print()
print(np.sign(sd2))

ddata1 = {'seoul':1000, 'busan':2000, 'incheon':3000, 'daegu':4000}
print(ddata1)
print()

sd3 = pd.Series(ddata1)
print(sd3)