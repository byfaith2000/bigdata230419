# 22년 매출 품목 리스트에서 품목을 그룹으로 묶고 각 그룹별 판매량(합산)등을 요약할 때 유용

import pandas as pd
import numpy as np

frame = pd.DataFrame({'key1':['a','a','b','b','a'],
                      'key2':['one','two','one','two','one'],
                      'data1':np.random.randn(5),
                      'data2':np.random.randn(5)})
print(frame)
print()

grouped1 = frame.groupby('key1')
print(grouped1.mean())
print()

grouped2 = grouped1['data1']
print(grouped2.mean())
print()

# 대분류, 중분류 나눌때 개념
grouped3 = frame.groupby(['key1', 'key2'])
print(grouped3.sum())
print()

print(grouped1)
print()

for data in grouped1 :
    print(data, end='\n\n')
# 튜플 형태임, 결과값에서 'a'는 그룹 이름, 나머지가 결과값

for n, d in grouped1 :
    print(n)
    print(d, end='\n\n')

print(list(grouped1))
# a는 그룹 이름, b도 그룹 이름
print()

# 딕셔너리 형태로
print(dict(list(grouped1)))
print()

# b그룹 데이터만 뽑아 올 때
ddata = dict(list(grouped1))
print(ddata['b'])

np.random.seed(12345)
frame2 = pd.DataFrame(np.random.randn(5,5),
                      index=['joe', 'steve', 'wes', 'jim', 'travis'],
                      columns=list('abcde'))
print(frame2)
print()
print('================================================================')
#구룹바이의 기본 축은 열방향이다.(axis=0)
# a,b,c가 인치가 다른 TV라고 볼때
# => 1. mapping, 2. labeling
#frame2.groupby()
#print()

mapping = {'a':'red', 'b':'red', 'c':'blue', 'd':'blue', 'e':'red'}
grouped4 = frame2.groupby(mapping, axis=1)
print(grouped4.sum())
print()

labeling = ['one','one','one','two','two']
group5 = frame2.groupby(labeling)
print(group5.mean())
print()

# 매핑은 가로방향에 주로 사용(가독성), 인덱싱 방향은 라벨링 이용하면 좋음(꼭 그런 것은 아님)

# 함수를 통해서도 그룹을 지정할 수 있음
print(frame2.groupby(len).sum())
print()
#이름의 제일 마지막 글자로 그룹핑
print(frame2.groupby(lambda x: x[-1]).sum())