import matplotlib.pyplot as plt
import pandas as pd
plt.rc('font', family='malgun Gothic')

# customer = ['김길동','홍길동','최길동','이길동','오길동']
# customer_index = range(len(customer))
# y_data = [130, 90, 200, 110, 230]
#
# fig = plt.figure(figsize=(6,4))
# ax1 = fig.add_subplot(111)
# ax1.bar(customer_index, y_data, color='darkblue')
# plt.xlabel('고객 이름')
# plt.ylabel('수요')
# plt.xticks(customer_index, customer, rotation=45)
# plt.show()

data = pd.read_csv('covid_data.csv', index_col='국가')
chartdata = data['4월06일']
#print(chartdata)

plt.figure(figsize=(10,8))
colors = ['b','g','r','c','m','y','k'] # 막대색
plt.bar(chartdata.index, chartdata, color=colors, alpha=0.7)
plt.xlabel('국가명')
plt.ylabel('발생수')
plt.title('국가별 코로나 발생 건 수(4월 06일)', fontsize = 16)

# 발생 건수 백분율
ratio = 100 * chartdata / chartdata.sum()

# %값 계산
for idx in range(chartdata.size) :
    value = format(chartdata[idx], ',') + '건'
    plt.text(x=idx, y=chartdata[idx] + 2000, s=value, ha='center', fontsize=10)
    # 자리수 조정
    ratioval = '%1.1f%%'%(ratio[idx])
    plt.text(x=idx, y=chartdata[idx]/2, s=ratioval, ha='center', fontsize=10)
    
# 평균값 선 넣는 코드(맨 나중에)
meanval = chartdata.mean()
# 수평선(평균)
plt.axhline(y=meanval, color='r', linewidth=2, linestyle='--')

plt.show()