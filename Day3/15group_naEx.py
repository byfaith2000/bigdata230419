import pandas as pd
import numpy as np

states = ['ohio','new_york','vermont','florida',
          'oregon','nevada','califonia','idaho']

data = pd.Series(np.random.randn(8), index=states)
data[['vermont','nevada','idaho']] = np.nan
print(data)
print()

labeling_key = ['east'] * 4 + ['west'] * 4
print(labeling_key)
print()

print(data.groupby(labeling_key).mean())
print()

fill_mean = lambda g : g.fillna(g.mean())
print(data.groupby(labeling_key, group_keys=False).apply(fill_mean))  #group_keys=False 안넣으면 에러창 뜸(버전에 따른..)
print()

fill_values = {'east':0.5, 'west':-1}
fill_func = lambda g : g.fillna(fill_values[g.name])
print(data.groupby(labeling_key, group_keys=False).apply(fill_func))