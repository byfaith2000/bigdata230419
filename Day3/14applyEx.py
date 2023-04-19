import pandas as pd
import numpy as np

tips = pd.read_csv('tips.csv')
tips['tip_pct'] = tips['tip'] / tips['total_bill']


def top_func(gdata, n=5, column='tip_pct') :  #gdata는 그룹 데이터 의미로 임의로 정한값, 여기에 흡연 그룹데이터와 비흡연 그룹데이터가 들어감
    return gdata.sort_values(by=column, ascending=False)[:n] # 상위 N개 (5개) 리턴

print(tips.groupby('smoker').apply(top_func))
print()

print(tips.groupby('smoker').apply(top_func, n=3, column='total_bill'))

# apply에서 사용하는 매개변수는 키워드 매개변수만 사용가능함