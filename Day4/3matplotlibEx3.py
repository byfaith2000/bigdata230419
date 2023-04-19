import matplotlib.pyplot as plt
import numpy as np

# x = np.linspace(-4, 4, 1024)
# y = 0.25 * (x * 4) * (x + 1) * (x - 2)
# plt.plot(x, y, c='r')
#
# box = {'facecolor':'g',
#        'alpha':0.5,
#        'edgecolor':'k',
#        'boxstyle':'round'}
# plt.text(-0.5, 2, 'black text', fontsize=12, bbox=box, rotation=-7)
# plt.show()


# 여기서 쪼금 이해 안되었음
# align_list = ['center', 'left', 'right']
# for i, align in enumerate(align_list) :
#     plt.text(0, i, f'align{align}', ha=align, fontsize=14)
#
# plt.plot([0, 0], [-1, len(align_list)], c='#808080', ls='--')
# plt.scatter([0] * len(align_list), range(len(align_list)))
# plt.show()
##matplotlib.pyplot.text(x, y, s, fontdict=None, **kwargs), x, y는 문자위치, s는 내가 넣을 문구

# x = np.linspace(-4, 4, 1024)
# y = 0.25 * (x * 4) * (x + 1) * (x - 2)
# plt.annotate('annotate string',
#              ha='right',   # 호리즌틀 얼라인먼트
#              xytext=(-1.5, 20),
#              xy=(1.7, -2.8),
#              arrowprops={'facecolor':'r', 'shrink':0.1})
# plt.plot(x, y, c='k')
# plt.show()

# X축 1개, Y축 2개 있는 그래프 만들 때
# Figure 객체는 기본적으로 Axes 객체가 있음. 현재 사용하는 Axes를 가져옴,  gca() =>Axes객체
# get current axes : gca

ax1 = plt.gca()
ax2 = ax1.twinx()

ins1 = ax1.plot([10, 5, 2, 8, 7], 'r--', label='y1')
ax1.set_ylabel('y1')

ins2 = ax2.plot([100,200,220,190,150], 'b:', label='y2')
ax2.set_ylabel('y2')

ins = ins1 + ins2
llabels = [l.get_label() for l in ins]

plt.legend(ins, llabels, loc='best')

plt.show()













