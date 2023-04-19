import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.rc('font', family='malgun Gothic')

mpg = pd.read_csv('mpg.csv')

fig = plt.figure(figsize=(16,10))
grid = plt.GridSpec(4,4, hspace=0.6, wspace=0.3)

ax_main = fig.add_subplot(grid[:-1, :-1])
ax_right = fig.add_subplot(grid[:-1, -1], xticklabels=[], yticklabels=[])
ax_bottom = fig.add_subplot(grid[-1, :-1], xticklabels=[], yticklabels=[])

ax_main.scatter(data=mpg, x='displ', y='hwy', alpha=0.8, edgecolor='k')
ax_right.hist(mpg.hwy, bins=40, color='darkblue', orientation='horizontal')
ax_bottom.hist(mpg.displ, bins=40, color='orange')
ax_bottom.invert_yaxis()

ax_main.set_xlabel('엔진의 크기')
ax_main.set_ylabel('마일수', rotation=270)
ax_main.set_title('gridspec graph', fontsize=15)

ax_main.yaxis.tick_right()
ax_main.yaxis.set_label_position('right')

plt.show()