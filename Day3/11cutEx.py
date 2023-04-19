import pandas as pd

ages = [20, 22, 25, 27, 33, 37, 61, 45, 41, 32, 70, 40]
bins = [16, 25, 35, 60, 100]
ldata1 = pd.cut(ages,bins)
print(ldata1)
print()
print(pd.value_counts(ldata1))

# )는 미만? ]는 포함

ldata2 = pd.cut(ages, bins, right=False, labels=['Youth', 'yougAdult', 'MiddleAged', 'senior'])
print(ldata2)