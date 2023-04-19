import pandas as pd
import numpy as np

tips = pd.read_csv('tips.csv')
tips['tip_pct'] = tips['tip'] / tips['total_bill']

#print(tips.pivot_table(index=['sex','smoker']))
print(tips.pivot_table(index=['sex','smoker'], aggfunc='mean'))

print()

print(tips.pivot_table(['tip','size'],
                       index=['sex'],
                       aggfunc=['mean']))
print()

print(tips.pivot_table(['tip','size'],
                       index=['sex'],
                       aggfunc=['mean','std']))
print()