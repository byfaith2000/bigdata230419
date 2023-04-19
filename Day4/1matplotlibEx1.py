import matplotlib.pyplot as plt
import numpy as np

#plt.title('plotEx1')
#plt.plot([1,3,8,19])
#plt.show()

#plt.title('plotEx2')
#plt.plot([1,3,8,19], 'rs--') #r이 red, s가 square,
#plt.show()

#plt.title('plotEx2')
#plt.plot([1,3,8,19], 'b^-.')
#plt.figure()

#plt.title('plotEx3')
#plt.plot([10,20,30,40], [1,3,8,19], 'b^-.')
#plt.show()

#plt.title('plotEx3')
#plt.plot([10,20,30,40], [1,3,8,19], color='green', lw=5, ls='--', marker='o', ms=12, mec='blue', mew=5, mfc='red')
## line space, marker size, marker edge color, marker edge width, marker face color
#plt.show()

#plt.title('plotEx4')
#plt.plot([10,20,30,40], [1,3,8,19], color='k', lw=5, ls=':', marker='o', ms=12, mec='orange', mew=5, mfc='green')
#plt.figure()

#plt.title('plotEx4')
#plt.plot([10,20,30,40], [1,3,8,19], color='k', lw=5, ls=':', marker='o', ms=12, mec='orange', mew=5, mfc='green')
#plt.xlim(0,50)
#plt.ylim(-5,35)
#plt.show()

# x = np.linspace(-np.pi, np.pi, 256)  # linear space..=>np.linspace(start, stop, num)->배열의 시작값, 끝값, 그 사이 num개의 일정한 간격
# y = np.cos(x)
# plt.plot(x,y)
# plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
#            ['-pi', 'pi/2', '0', 'pi/2', 'pi'])
# plt.yticks([-1,0,1],
#            ['low', '0', 'high'])
# plt.grid(True)
# plt.show()

# data = np.arange(0, 5, 0.2)
# plt.plot(data, data, 'b--', data, 0.1*data**2, 'go:', data, 0.1*data**3, 'rs-')
# #          x,   y,     setting
# plt.show()


# # 그래프 여러개 그릴 때 보통 이 방법으로 그려줌
# plt.plot([10,20,30,40], [1,3,8,19], color='green', lw=5, ls='--', marker='o', ms=12, mec='blue', mew=5, mfc='red')
# plt.plot([10,20,30,40], [22,7,15,2], color='green', lw=5, ls='--', marker='o', ms=12, mec='orange', mew=5, mfc='red')
# plt.xlabel('x axis')
# plt.ylabel
# plt.show()

# x = np.linspace(-np.pi, np.pi, 256)
# y1, y2 = np.cos(x), np.sin(x)
# plt.plot(x, y1, ls='--', label='cosine')
# plt.plot(x, y2, ls=':', label='sine')
# plt.xlabel('x axis')
# plt.ylabel('y axis')
# plt.legend(loc='best')
# plt.show()

x = np.linspace(-np.pi, np.pi, 256)
y1, y2 = np.cos(x), np.sin(x)
plt.plot(x, y1, ls='--')
plt.plot(x, y2, ls=':')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend(['cosine', 'sine'], loc='best', fontsize=14)  # 위와 비슷한 방법(범례)
plt.show()











