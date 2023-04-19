import numpy as np
import matplotlib.pyplot as plt

plot_data1 = np.random.randn(50).cumsum()
plot_data2 = np.random.randn(50).cumsum()
plot_data3 = np.random.randn(50).cumsum()
plot_data4 = np.random.randn(50).cumsum()

fig = plt.figure(figsize=(8,6))
ax1 = fig.add_subplot(111)
ax1.plot(plot_data1, marker='o', color='blue', linestyle='-', label='Blue Solid')
ax1.plot(plot_data2, marker='+', color='red', linestyle='--', label='Red Solid')
ax1.plot(plot_data3, marker='*', color='green', linestyle='-.', label='Green Solid')
ax1.plot(plot_data4, marker='s', color='orange', linestyle=':', label='Orange Solid')

ax1.set_title('Line Plots : Markers, Colors, and LineStyles')
plt.xlabel('Draw')
plt.ylabel('Random Number')
plt.legend(loc = 'best')

plt.savefig('linePlot.png', dpi=400)
plt.show()


# plt.figure(figsize=(10, 2))   # 10인치 바이 2인치
# plt.title('figsize : (10, 2)')
# plt.plot(np.random.randn(200))
# plt.show()

# # 그래프 여러개 그릴 때 보통 이 방법으로 그려줌
# plt.plot([10,20,30,40], [1,3,8,19], color='green', lw=5, ls='--', marker='o', ms=12, mec='blue', mew=5, mfc='red')
# plt.plot([10,20,30,40], [22,7,15,2], color='green', lw=5, ls='--', marker='o', ms=12, mec='orange', mew=5, mfc='red')
# plt.xlabel('x axis')
# plt.ylabel
# plt.show()