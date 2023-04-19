import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# dataA = np.random.randn(100, 2)
# dataA += np.array((-1, -1))
#
# dataB = np.random.randn(100, 2)
# dataB += np.array(((1, 1)))
#
# plt.scatter(dataA[:, 0], dataA[:, 1], color='0.25')
# plt.scatter(dataB[:, 0], dataA[:, 1], color='0.75', edgecolors='k')
# plt.show()

plt.rc('font', family='malgun Gothic')

mpg = pd.read_csv('mpg.csv', encoding='utf-8')
mpg.info()
# print(mpg.head())
#
# xdata = mpg.loc[:, ['displ']]  # 엔진크기
# ydata = mpg.loc[:, ['hwy']]  # 고속도로 연비
#
# plt.plot(xdata, ydata, marker='o', linestyle='None')
# plt.xlabel('엔진크기')
# plt.ylabel('고속도로 주행 마일 수')
# plt.title('산점도 그래프')
# plt.show()

# #구동방식, 산점도 여러개 표현
# print(mpg['drv'].unique()) # 구동방식
#
# mycolor = ['r','g','b']
# label_dic = {'f':'전륜구동', '4':'4륜구동', 'r':'후륜구동'}
#
# idx = 0
# for finditem in mpg['drv'].unique():
#     xdata = mpg.loc[mpg['drv']==finditem, 'displ']
#     ydata = mpg.loc[mpg['drv'] == finditem, 'hwy']
#     plt.plot(xdata, ydata, color=mycolor[idx], marker='o', linestyle='None', label = label_dic[finditem])
#     idx+=1
#
# plt.xlabel('엔진크기')
# plt.ylabel('고속도로 주행 마일 수')
# plt.title('산점도 그래프')
# plt.legend(loc='best')
# plt.show()

x = np.arange(1,15,1)
y_linear = x + 5 * np.random.randn(14)
y_quadratic = x ** 2 + 10 * np.random.randn(14)

#Linear w b(1차원)
fn_linear = np.poly1d(np.polyfit(x, y_linear, deg=1)) # polyfit은 W,D 찾는 것, poly1d는 식을 만드는 것
#Linear wb(2차원)
fn_quardratic = np.poly1d(np.polyfit(x, y_quadratic, deg=2))
print(fn_quardratic)

plt.figure(figsize=(10,8))

plt.plot(x, fn_linear(x), 'b-', x, fn_quardratic(x), 'g-', linewidth=2)

plt.scatter(x=x, y=y_linear, c='b', marker='s')
plt.scatter(x=x, y=y_quadratic, c='g', marker='o')
plt.xlabel('x axis')
plt.ylabel('f(x')
plt.show()