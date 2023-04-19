import pandas as pd
import numpy as np

frame1 = pd.DataFrame([[-999, 2, -1000],
                       [2, -999, -999]],
                      columns=['first', 'second', 'thrird'])
print(frame1)
print()

print(frame1.replace([-999, -1000], np.nan))
print()

print(frame1.replace({-999:-1, -1000:0}))

