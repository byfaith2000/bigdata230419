import pandas as pd
import numpy as np

sd1 = pd.Series([4,7,-5,3], index=list('dabc'))
print(sd1)
print()

sd2 = sd1.reindex(['a','b','c','d','e']) #e는 없으므로 NaN, NaN은 실수값으로 취급한다.
print(sd2)
print()

sd3 = pd.Series(['red','green','blue'], index=[0,2,4])
print(sd3)
print()

print(sd3.reindex(np.arange(6), method='ffill')) # frontfill, 앞에 있는 값으로 채워라, bfill, near~~

frame1 = pd.DataFrame(np.arange(9).reshape(3,3),
                      index=list('acd'),
                      columns=['one','two','three'])
print(frame1)
print()

print(frame1.reindex(['d','a','b']))
print()

print(frame1.reindex(columns=['one','three','four']))