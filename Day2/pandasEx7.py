import numpy as np
import pandas as pd

frame1 = pd.DataFrame(np.arange(12).reshape(3,4), columns=list('abcd'))
frame2 = pd.DataFrame(np.arange(20).reshape(4,5), columns=list('abcde'))
print(frame1)
print()
print(frame2)
print()

print(frame1 + frame2)  # NaN + 숫자는 NaN
print()

print(frame1.add(frame2, fill_value=0))  # NaN을 0으로 한다음 계산