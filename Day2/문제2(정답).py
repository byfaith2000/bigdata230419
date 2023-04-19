import numpy as np
import pandas as pd

data = {
    '번호': [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
    '반': ['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B'],
    '영어': [100, 90, 100, 80, 70, 90, 100, 70, 80, 90],
    '국어': [90, 80, 90, 70, 100, 80, 90, 100, 70, 80],
    '수학': [80, 100, 80, 90, 80, 100, 70, 80, 90, 100]}

df_score = pd.DataFrame(data, columns=['반','번호','국어','영어','수학'])
print(df_score)
print()

df_score.drop(['반','번호'], axis=1, inplace=True)
print(df_score)
print()

df_score['평균'] = df_score.mean(axis=1)
print(df_score)
print()

df_score.loc['평균'] = df_score.mean(axis=0)
print(df_score)