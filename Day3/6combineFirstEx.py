import numpy as np
import pandas as pd

s1 = pd.Series([np.nan, 2.5, np.nan, 3.5, 4.5, np.nan],
               index=list('fedcba'))

s2 = pd.Series(np.arange(len(s1), dtype=np.float32),  # s1의 갯수만큼 arange를 만든다.
               index=list('fedcba'))
print(s1)
print()
print(s2)
print()

# 머지, concat 에다 데이타를 보완해서 합치기
print(s1.combine_first(s2))  # s1 베이스에 s1에 있는 nan은 s2에 있는 값 반환

frame1 = pd.DataFrame({'a':[1, np.nan, 5, np.nan],
                       'b':[np.nan, 2, np.nan, 6]})
frame2 = pd.DataFrame({'a':[10,20,30,40],
                       'b':[np.nan, 2.2, 3.3, 4.4]})
print(frame1)
print()
print(frame2)
print()

print(frame1.combine_first(frame2))