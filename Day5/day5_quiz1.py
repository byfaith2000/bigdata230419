import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.rc('font', family='malgun Gothic')

widata = pd.read_csv('winequality-both.csv')

ddata1 = pd.DataFrame(widata)
#print(ddata1)
print(ddata1.head(5))

print()

# b. 변수별 요약 통계를 표시한다.(최소, 최대, 사분위, 평균, 표준편차)
print(ddata1.describe())
print()

# c. 와인 품질(quality)의 유일 값(점수)을 찾아 출력한다.
#print(ddata1['quality'].unique())
print(ddata1.quality.unique())
print()

# d. 와인 품질(quality)의 빈도(점수 별 갯 수)를 계산하여 출력한다.
#print(ddata1['quality'].value_counts())
print(ddata1.quality.value_counts())
print()

# e. 와인 종류(type)에 따른 (alcohol)의 기술 통계(describe())를 출력한다.
# grouped1 = ddata1.groupby(['type'])
# print(grouped1.head(10))
# print()
# print(grouped1.describe())
print(ddata1.groupby('type')[['alcohol']].describe())
print()


# f.  와인 종류에 따른 품질(quality)의 분포를 확인하기 위해 레드와인과 화이트 와인의 품질 값(quality)을 막대 그래프로 출력한다.
#    (이때 범례도 같이 출력한다. )
by_quality = ddata1.groupby(['quality', 'type']).size().unstack()
print(by_quality)
by_quality.plot(kind='bar')
plt.show()

# g. 와인 종류에 따라 와인 품질 값(quality)의 표준편차(std)와 평균(mean)값을 출력한다.
print(ddata1.groupby(['type']))[['quality']].agg(['std', 'mean'])