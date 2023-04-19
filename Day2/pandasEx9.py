import numpy as np
import pandas as pd

frame = pd.DataFrame(np.random.randn(1000, 3),
                     columns=['first', 'second', 'thrid'])
print(frame)
print()

print(frame.sum())  # 디폴트가 열임
print()

print(frame.sum(axis=1))
print()

print(frame.mean())
print()

print(frame.std())
print()

print(frame.describe())
print()

frame.info()
print()

print(frame.head(10))
print()
print(frame.tail(15))

print('======================================================')
# 상관관계와 분산
frame2 = pd.DataFrame(np.random.randn(3,3),
                      columns=['ohio', 'utah', 'texas'])
print(frame2)
print()

print(frame2.ohio.corr(frame2.utah)) # 상관관계ㄱ
print(frame2.ohio.cov(frame2.utah)) # 공분산
print()

print(frame2.corr())
print()
print(frame2.cov())
