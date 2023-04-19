import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
plt.rc('font', family='malgun Gothic')

# frame = pd.read_csv('tips.csv').head(100)
# xrange = range(len(frame))
#
# data_bill = frame.loc[ :, ['total_bill']]
# data_tip = frame.loc[:, ['tip']]
#
# fig, ax1 = plt.subplots()
# ax1.set_title('결제 금액과 Tip')
# color = 'tab:red'
# ax1.set_ylabel('결제 금액', color=color, rotation=0)
# ax1.plot(xrange, data_bill, color=color)
# ax1.tick_params(axis='y', labelcolor=color)
#
# ax2 = ax1.twinx()
# color = 'tab:blue'
# ax2.set_ylabel('팁', color=color, rotation=0)
# ax2.plot(xrange, data_tip, color=color)
# ax2.tick_params(axis='y', labelcolor=color, labelrotation=0)
#
# plt.show()

diamonds = pd.read_csv('diamonds.csv')
diamonds = diamonds.sample(frac=0.02)
cut_list = diamonds['cut'].unique()

my_color = ['r','g','b','y','m']
cut_dict = {cut_list[idx]: my_color[idx] for idx in range(len(cut_list))}
diamonds['newcut'] = diamonds['cut'].apply(lambda cut:cut_dict[cut])

newcut = diamonds['newcut']

plt.figure(figsize=(8,6))
x_data = diamonds['price']
y_data = diamonds['depth']
plt.scatter(x=x_data, y=y_data, c=newcut, alpha=0.7)
plt.xlabel('price')
plt.ylabel('depth')
plt.show()