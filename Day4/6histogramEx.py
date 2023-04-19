import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
plt.rc('font', family='malgun Gothic')

# mu1, mu2, sigma = 100, 130, 15
# x1 = mu1 + sigma * np.random.randn(10000)
# x2 = mu2 + sigma * np.random.randn(10000)
# plt.hist(x1, bins=50, color='darkgreen')
# plt.hist(x2, bins=50, color='orange', alpha=0.5)
#
# plt.xlabel('bins')
# plt.ylabel('number of values in bin')
# plt.title('two frequency distributions')
# plt.show()

human = pd.read_csv('human_height.csv')
human.info()

man = human['man']
woman = human['woman']
plt.figure(figsize=(10,6))
plt.hist(man, bins=40, alpha=0.5, label='남자')
plt.hist(woman, bins=40, alpha=0.5, label='여자')
plt.xlabel('키')
plt.ylabel('남자 여자 키 분포')
plt.legend(loc='best')
plt.show()