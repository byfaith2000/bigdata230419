import pandas as pd

frame1 = pd.DataFrame([[2,3,4],[6,7,8]])
print(frame1)
print()

frame1 = pd.DataFrame([[2,3,4],[6,7,8]],
                      index=['one','two'],
                      columns=['first','second','third'])
print(frame1)
print()

ldata1 = [('kim','seoul',180), ('lee', 'busan', 190), ('jeung', 'suwon', 170)]
frame2 = pd.DataFrame(ldata1,
                      columns=['name', 'city', 'height'])
print(frame2)
print()

# 1: N차 딕셔너리를 데이타 프레임으로
ddata = {'city':['ohio', 'ohio', 'nevada', 'nevada', 'nevada'],
         'year':[2010, 2021, 2014, 2016, 2018],
         'pop':[1.5,1.7,2.5,2.9,3.3]}
frame3 = pd.DataFrame(ddata)
print(frame3)
print()

frame4 = pd.DataFrame(ddata,
                      columns=['year','pop','city'],
                      index=['one','two','three','four','five'])
print('-----------------')
print(frame4)
print()

print(frame4['city'])
print()
print(frame4.city)
print()
print('-----------------')
print(frame4.loc['three'])  # 행방향 가져올 때 location사용, 행렬처럼 사용할 수 있다?, 행방향은 타입이 다양하기 때문
# loc안에 대괄호 하나 더 넣으면 동일한 형태가 된다.
print(frame4.loc[['three']])
print()
print('================================================')
print(frame4.loc['three','pop'], frame4['pop']['three'])
print()

#frame4['area'] = pd.Series([100,100,200,200,200]) # 인덱스가 안맞아서 NaN으로 나옴
#print(frame4) #NaN = Not a Number   # 판다스는 축정보와 항상 매칭이 된다 <<중요함

print('==================================================================')
#frame4['area'] = pd.Series([100,100,200,200,200], index=['one','two','three','five'])
frame4['area'] = pd.Series([100,100,200,200,200], index=frame4.index)
print(frame4)
print()

frame4.loc['six'] = pd.Series([2020, 4.1, 'texas', 700], index=frame4.columns)
print(frame4)

frame4.index.name = 'ID'
frame4.columns.name = 'ATTR'
print(frame4)


