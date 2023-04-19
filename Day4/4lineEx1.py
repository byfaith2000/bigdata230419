import matplotlib.pyplot as plt
import pandas as pd
plt.rc('font', family='malgun Gothic')

data = pd.read_csv('covid_data.csv', index_col='국가')
print(data)
# 데이타 프레임을 이용해서 plot을 그릴 수 있다.

chartdata = data.loc[['스페인', '프랑스', '독일', '중국', '영국', '이란'], ['4월06일', '4월07일', '4월08일', '4월09일', '4월10일']]
print(chartdata)

plt.rc('font', family='malgun Gothic')  #
chartdata.T.plot(title='국가별 코로나 발생 건수', figsize=(10, 6), legend=True, marker='o')  # T는 Trans
plt.grid(True)
plt.xlabel('일자')
plt.ylabel('발생 건수')
plt.show()