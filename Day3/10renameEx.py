import numpy as np
import pandas as pd

frame = pd.DataFrame(np.arange(12).reshape(3,4),
                    index=['ohio', 'colorado', 'new york'],
                    columns=['one', 'two', 'three', 'four'])
print(frame)
print()

print(frame.index.map(str.upper))
frame.index = frame.index.map(str.upper)
print()
print(frame)
print()

print(frame.rename(index=str.title, columns=str.upper))
print()

# 콕 찝어서
print(frame.rename(index={'OHIO':'INDIANA'},
                   columns={'three':'third'}))