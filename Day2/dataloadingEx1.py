import pandas as pd

frame1 = pd.read_csv('ex1.csv')
print(frame1)
print()

frame2 = pd.read_csv('ex2.csv', header=None)
print(frame2)
print()

frame3 = pd.read_csv('ex2.csv', names=['one', 'two', 'three', 'four', 'msg'])
print(frame3)

# 제일 오른쪽 내용이 인덱스인 경우
frame3 = pd.read_csv('ex2.csv', names=['one', 'two', 'three', 'four', 'msg'], index_col='msg')
print(frame3)
print()

frame3 = pd.read_csv('ex2.csv', names=['one', 'two', 'three', 'four', 'msg'], index_col=4)
print(frame3)
print()

# 2개가 인덱스인 경우
frame4 = pd.read_csv('csv_mindex.csv', index_col=['key1', 'key2'])
print(frame4)
print()

# 데이터에 주석이 있는 경우, skip할 row의 인덱스 번호 이용
frame5 = pd.read_csv('ex4.csv', skiprows=[0,2,3])
print(frame5)
print()

import numpy as np
sframe = pd.DataFrame(np.random.randn(4,3),
                      columns=['seoul', 'busan', 'incheon'])
print(sframe)
sframe.to_csv('sfile.csv')
sframe.to_csv('sfile2.csv', index=False)  # 인덱스 미포함

print('aaaaa', end='\n\n')
print('bbb')