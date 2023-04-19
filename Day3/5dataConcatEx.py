import numpy as np
import pandas as pd

s1 = pd.Series([0,1], index=list('ab'))
s2 = pd.Series([2,3,4], index=list('cde'))
s3 = pd.Series([5,6], index=list('fg'))
print(s1)
print()
print(s2)
print()
print(s3)
print()

print(pd.concat([s1,s2, s3], axis=0))
print()

print(pd.concat([s1,s2,s3], axis=1))
print()

s4 = pd.concat([s1 * 5, s3])
print(s4)
print()

print(pd.concat([s1, s4], axis=1))
print()

# NaN제외할 때 inner 사용
print(pd.concat([s1, s4], axis=1, join='inner'))
print()

frame1 = pd.DataFrame(np.arange(6).reshape(3,2),
                      index=list('abc'),
                      columns=['one', 'two'])
frame2 = pd.DataFrame(np.arange(4).reshape(2,2),
                      index=list('ac'),
                      columns=['three', 'four'])
print(frame1)
print()
print(frame2)
print()

print(pd.concat([frame1, frame2], axis=1))
print()

print(pd.concat([frame1, frame2], axis=1, keys=['f1', 'f2']))


