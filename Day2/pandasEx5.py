# df.loc["row", "column"]으로 인덱싱할 수 있다. 
# df.iloc[0, 0]으로 인덱싱할 수 있다.(인티저 location으로 인덱스로 위치를 찾는다.)

import pandas as pd
import numpy as np

sd1 = pd.Series([4,7,2,9,1], index=list('abcde'))
print(sd1)
print()

print(sd1['b'],sd1[1])
print()

print(sd1[1:4])
print()

print(sd1['b':'e']) # e도 포함됨, 숫자는 -1

frame1 = pd.DataFrame(np.arange(16).reshape(4,4),
                      index=['ohio','colorado','utah','new york'],
                      columns=['one','two','three','four'])
print(frame1)
print()

print(frame1.iloc[1,1])  # iloc =>인티저를 기준으로 행방향?, integer location
print()
print(frame1.iloc[1:,2:])

