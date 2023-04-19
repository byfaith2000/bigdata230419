import pandas as pd
import numpy as np

sd1 = pd.Series(np.arange(4), index=list('dabc'))
print(sd1)
print()

# inplace가 True냐 False이냐에 따라 원본이 바뀌느냐 안바뀌느냐 결정됨
print(sd1.sort_index())

frame1 = pd.DataFrame(np.arange(8).reshape(2,4),
                      index=['three', 'one'],
                      columns=list('dabc'))
print(frame1)
print()

print(frame1.sort_index())
print()

print(frame1.sort_index(axis=1))  # 행축으로 오름차순 정렬
print()

print(frame1.sort_index(axis=1, ascending=False))
print()
print('---------------------------------------------')
sd2 = pd.Series([4,7,-3,2])
print(sd2)
print()

print(sd2.sort_values())
print()
print('---------------------------------------------')
ddata = {'a':[4,7,-3,2],
         'b':[0,1,0,1]}
frame2 = pd.DataFrame(ddata)
print(frame2)
print()

print(frame2.sort_values(by='a'))
print()
print(frame2.sort_values(by='b'))
print()
print(frame2.sort_values(by=['b','a']))  # 한번 소팅 후(b) 그 내에서 다시 소팅(a)
print()
print(frame2.sort_values(by=['b','a'], ascending=[False, True]))
