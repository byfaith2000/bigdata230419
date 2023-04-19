import numpy as np
import pandas as pd

sd1 = pd.Series([1, np.nan, 3.5, np.nan, 7])
print(sd1)
print()

print(sd1.notnull())
print()
print(sd1[sd1.notnull()])
print()

print(sd1.dropna())
print()

np.random.seed(1234)
frame1 = pd.DataFrame(np.random.randn(7,3),
                      columns=['one', 'two', 'three'])
frame1.iloc[:4, 1] = np.nan
frame1.iloc[:2, 2] = np.nan
print(frame1)
print()

print(frame1.fillna(0))
print()

print(frame1.fillna({'two':0.5, 'three':-1}))
print()

print(frame1.fillna(method='bfill'))

# 나머지 값들의 평균값을 넣고 싶을 때
print(frame1.mean(axis=0))
print()

print(frame1.fillna(frame1.mean(axis=0)))