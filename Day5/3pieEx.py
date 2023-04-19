import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.rc('font', family='malgun Gothic')

# data = [5,25,50,20]
# plt.pie(data)
# plt.show()

data = pd.read_csv('covid_data.csv', index_col='국가')
chartdata = data.loc[['독일','프랑스','중국','영국'], '4월06일']
print(chartdata)

mylabel = chartdata.index
mycolors = ['blue','#6aff00', 'yellow','#fa003c']

plt.figure(figsize=(5,5))
plt.pie(chartdata,
        labels=mylabel,
        startangle=90,
        counterclock=False,
        colors=mycolors,
        autopct='%.2f%%',
        explode=(0,0.1,0,0),   # 두번째 파이를 돋보이게
        shadow=True)
plt.legend(loc='best')
plt.xlabel('국가명')
plt.title('주요 국가 코로나 발생 비율(4월6일)', fontsize=15)
plt.show()