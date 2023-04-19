import pandas as pd
import numpy as np

sd1 = pd.Series(np.arange(5), index=list('abcde'))
print(sd1)
print()

print(sd1.drop(['c','d'])) # 원본 안바뀜
print()

sd1.drop(['c','e'], inplace=True)  # 원본 바뀜
print()
print(sd1)

frame1 = pd.DataFrame(np.arange(16).reshape(4,4),
                      index=list('abcd'),
                      columns=['one','two','three','four'])
print(frame1)
print()
print(frame1.drop('a'))
print()

#print(frame1.drop('one', axis=1)) 
print(frame1.drop('one', axis='columns')) # 위와 결과값 동일, 열을 삭제할 때에는 축정보를 줘야 한다?

