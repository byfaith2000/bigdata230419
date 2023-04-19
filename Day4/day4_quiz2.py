import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
plt.rc('font', family='malgun Gothic')

data = pd.read_csv('tips.csv')
data.info()

print(data.head(5))

chartdata = data.loc[ : , ['total_bill', 'tip']]
print(chartdata)

#chartdata = data.loc[['스페인', '프랑스', '독일', '중국', '영국', '이란'], ['4월06일', '4월07일', '4월08일', '4월09일', '4월10일']]
#print(chartdata)

# plt.rc('font', family='malgun Gothic')  #
# chartdata.T.plot(title='국가별 코로나 발생 건수', figsize=(10, 6), legend=True, marker='o')  # T는 Trans
# plt.grid(True)
# plt.xlabel('일자')
# plt.ylabel('발생 건수')
# plt.show()

ax1 = plt.gca()
ax2 = ax1.twinx()

ins1 = ax1.plot([chartdata['total_bill']], 'r--', label='결제 금액')
ax1.set_ylabel('결제 금액')

ins2 = ax2.plot([chartdata['tip']], 'b:', label='tip')
ax2.set_ylabel('tip')

ins = ins1 + ins2
llabels = [l.get_label() for l in ins]

plt.legend(ins, llabels, loc='best')

plt.show()

# # X축 1개, Y축 2개 있는 그래프 만들 때
# # Figure 객체는 기본적으로 Axes 객체가 있음. 현재 사용하는 Axes를 가져옴,  gca() =>Axes객체
# # get current axes : gca
#
# ax1 = plt.gca()
# ax2 = ax1.twinx()
#
# ins1 = ax1.plot([10, 5, 2, 8, 7], 'r--', label='y1')
# ax1.set_ylabel('y1')
#
# ins2 = ax2.plot([100,200,220,190,150], 'b:', label='y2')
# ax2.set_ylabel('y2')
#
# ins = ins1 + ins2
# llabels = [l.get_label() for l in ins]
#
# plt.legend(ins, llabels, loc='best')
#
# plt.show()