import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#plt.rc('font', family='malgun Gothic')

# ddata = np.random.randn(10000)
# plt.boxplot(ddata)
# plt.show()
#
# np.random.seed(777)
# normal = np.random.normal(loc=0, scale=1, size=500)
# lognormal = np.random.lognormal(mean=0, sigma=1, size=500)
# index_value = np.random.randint(low=0, high=499, size=500)
# normal_sample = normal[index_value]
# lognormal_sample = lognormal[index_value]
#
# box_plot_data = [normal, normal_sample, lognormal, lognormal_sample]
#
# box_labels = ['normal', 'normal_sample', 'lognormal', 'lognormal_sample']
# plt.boxplot(box_plot_data, labels=box_labels, showmeans=True)  # x축 항목이 labels임, 평균값은 그래프에서 녹색 삼각형
# plt.show()

# myframe = pd.read_csv('tips.csv', index_col=0)
# print(myframe.head())
# frame1 = myframe.loc[myframe['time'] == 'Dinner', 'total_bill']  #myframe에 있는 time이 Dinner인 행과 그때의 total_bill의 값
# frame1.index.name = 'Dinner'
# print(frame1.head())
#
# frame2 = myframe.loc[myframe['time'] == 'Lunch', 'total_bill']
# frame2.index.name = 'Lunch'
#
# charData = [np.array(frame1), np.array(frame2)]
# xtick_label = ['Dinner', 'Lunch']
#
# fig, (ax1, ax2) = plt.subplots(1,2,figsize=(9,4))  # subplots는 가로로 2개 있는 그래프에서 각 축정보를 이용해 각각의 그래프를 불러올 수 있다?
# ax1.boxplot(charData, vert=True, labels = xtick_label)
# ax1.set_title('vertical boxplot')
#
# ax2.boxplot(charData, vert=False, labels = xtick_label)
# ax2.set_title('horizonal boxplot')
#
# plt.show()

np.random.seed(111)

frame = pd.DataFrame(np.random.rand(5,3),
                     index=['customer1', 'customer2', 'customer3', 'customer4', 'customer5'],
                     columns=['metric1', 'metric2', 'metric3'])
print(frame)

fig, (ax1, ax2) = plt.subplots(1,2,figsize=(9,4))

frame.plot(kind='bar', ax=ax1, alpha=0.75, title='bar plot')
ax1.set_xlabel('customer')
ax1.set_ylabel('value')
plt.setp(ax1.get_xticklabels(), rotation=25)  #setp : set property

frame.plot(kind='box', ax=ax2, title='box plot')
ax2.set_xlabel('metrics')
ax2.set_ylabel('value')
plt.tight_layout()

plt.show()




