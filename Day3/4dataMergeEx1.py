import pandas as pd
import numpy as np

frame1 = pd.DataFrame({'key':['b','b', 'a', 'c', 'a', 'a', 'b'],
                       'data1':range(7)})
frame2 = pd.DataFrame({'key':['a','b','d'],
                       'data2':range(3)})
print(frame1)
print()
print(frame2)

# 키가 없는 것은 제외하고 연결하는 것을 내부조인이라고 함 how = 'inner', 전부표시하려면 how = 'outer'
# SQL의 join연산과 유사하다.
print(pd.merge(frame1, frame2, on='key'))
print()

print(pd.merge(frame1, frame2, on='key', how='outer'))
print()

print(pd.merge(frame1, frame2, on='key', how='left'))
print()

print(pd.merge(frame1, frame2, on='key', how='right'))
print()
print('-------------------------------------------------------------------------')
# 키내용은 같고 이름이 다를 때 : lkey, rkey -> merge후 한개의 키만 사용하기 위해 나머지 키는 날림
frame3 = pd.DataFrame({'lkey':['b','b', 'a', 'c', 'a', 'a', 'b'],
                       'data1':range(7)})
frame4 = pd.DataFrame({'rkey':['a','b','d'],
                       'data2':range(3)})

print(pd.merge(frame3, frame4, left_on='lkey', right_on='rkey').drop('rkey',axis=1))