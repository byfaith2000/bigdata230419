# aggregation 묶다 의미

import pandas as pd
import numpy as np

tips = pd.read_csv('tips.csv')
tips.info()
print()

print(tips.head())

# tip_pct add
tips['tip_pct'] = tips['tip'] / tips['total_bill']
print(tips.head())

print('-------------------------------------------------------')
grouped = tips.groupby(['sex', 'smoker'])
grouped_pct = grouped['tip_pct']
print()

print(grouped_pct.mean())

print(grouped_pct.agg('mean'))  # 위 코드와 결과 동일함, 하지만 agg사용하면 함수 사용가능?
print()
print(grouped_pct.agg(['mean', 'std'])) # 그룹된 데이터에 함수 2개를 적용한 것, agg는 2개의 함수를 사용 가능
print()

# mean을 gmean으로, std를 g_std로 변경
print(grouped_pct.agg([('gmean', 'mean'),('g_std','std')]))
print()

# 전체 데이타 이용
print(grouped.agg({'tip':'max', 'size':'sum'})) # tip은 최대값, size는 합을 반환
print()
print(grouped.agg({'tip_pct':['min', 'max'],
                   'size':['sum','mean','std']}))

