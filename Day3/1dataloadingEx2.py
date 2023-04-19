import pandas as pd
import numpy as np

# 데이타가 너무커서 쪼개서 사용할 때
chunker = pd.read_csv('ex6.csv', chunksize=1000)
print(chunker)

# 누적시킬 시리즈를 하나 만든다.
tot = pd.Series([], dtype=np.float64)

for piece in chunker :
    # print(piece, end='\n\n')
    tot = tot.add(piece['key'].value_counts(), fill_value=0)  # 지정된 열의 각 값(value)에 대한 모든 발생 횟수를 반환

tot = tot.sort_values(ascending=False)
print(tot[:10])

print(tot)

print()
sdata1 = pd.Series(['a','b','c','a','a','c'])
print(sdata1)
print()
print(sdata1.value_counts())
