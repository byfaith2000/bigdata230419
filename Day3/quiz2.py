import pandas as pd
import numpy as np

df1 = pd.DataFrame({
    '매출': [10000000, 12000000, 9000000, 6000000, 8000000, 1100000],
    '비용': [15000000, 1300000, 1200000, 9000000, 9900000, 9500000]},
    index=['1월', '2월', '3월', '4월', '5월', '6월'])

df2 = pd.DataFrame({
    '매출': [13000000, 14000000, 17000000, 15400000, 16500000, 16600000],
    '비용': [11000000, 10400000, 11000000, 12100000, 9000000, 9500000]},
    index=['7월', '8월', '9월', '10월', '11월', '12월'])

print(df1)
print()

print(df2)
print()

df3 = pd.concat((df1, df2), axis=0)  #디폴트가0이므로 axis지정안해도 됨
print(df3)


df3['이익'] = df3['매출'] - df3['비용']
print(df3)
print()

df3.loc['실적']=df3.sum(axis=0)
print(df3)





#difff = result.[1]-result.[2]

#result['이익'] = result.('매출'-'비용')(axis=0)
#print(result)