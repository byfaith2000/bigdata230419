import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.rc('font', family='malgun Gothic')

drinks = pd.read_csv('drinks.csv')
drinks.info()

#ㄴ
cols = ['beer_servings', 'spirit_servings', 'wine_servings', 'total_litres_of_pure_alcohol']
corrdata = drinks[cols].corr()
print(corrdata)
print()

import seaborn as sns

# cols_label = ['beer', 'spirit', 'wine', 'alchohol']
# sns.heatmap(corrdata.values,
#             annot=True,
#             xticklabels=cols_label,
#             yticklabels=cols_label)
# plt.show()

# sns.pairplot(drinks[['beer_servings', 'spirit_servings', 'wine_servings', 'total_litres_of_pure_alcohol']])
# plt.show()

drinks['continent'] = drinks['continent'].fillna('OT')
drinks.info()
print()

labels = drinks['continent'].value_counts().index().tolist()
fracs1 = drinks['continent'].value_counts().values.tolist()

plt.pie(fracs1, labels=labels, autopct='%.0f%%', shadow=True, explode=(0,0,0,0.25,0,0))
plt.show()