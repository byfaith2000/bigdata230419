=====================================
Q1
1. 아래 코드를 이용하여 데이터 프레임을 구성한다.
myindex = ['김구', '이봉창', '안중근', '윤봉길']
mycolumns = ['강남구', '은평구', '마포구', '용산구']
mylist = list(10 * onedata for onedata in range(1, 17))

 ㄱ.1번째 행 데이터를 조회
 ㄴ.1번째와 3번째 행 데이터를 조회
 ㄷ.'윤봉길'행만 조회
 ㄹ.'이봉창'과 '윤봉길' 행을 조회
 ㅁ.'윤봉길'행의 '은평구' 데이터만 조회
 ㅂ.'김구'와 '이봉창'의 '용산구'와 '은평구' 데이터 조회
 ㅅ.'은평구'의 값이 100이하인 행들을 조회
 ㅇ.'은평구'의 값인 100인 행들을 조회
 ㅈ.'김구'부터 '안중근' 까지 '용산구' 데이터를 80으로 변경
=====================================
import pandas as pd
import numpy as np

myindex = ['김구','이봉창','안중근','윤봉길']
mycolumns = ['강남구','은평구','마포구','용산구']
mylist = list(10 * onedata for onedata in range(1, 17))
print(mylist)
print()

myframe = pd.DataFrame(np.reshape(mylist, (4,4)),
                       index=myindex,
                       columns=mycolumns)
print(myframe)
print()

print(myframe.iloc[1])
print()

print(myframe.iloc[[1,3]])
print()

print(myframe.loc['윤봉길'])
print()

print(myframe.loc[['이봉창', '윤봉길']])
print()

print(myframe.loc[['윤봉길'], ['은평구']])
print()

print(myframe.loc[['김구', '윤봉길'], ['용산구', '은평구']])
print()

result = myframe[myframe['은평구'] <= 100]
print(result)
print()

result = myframe[myframe['은평구'] == 100]
print(result)
print()

myframe.loc['김구':'안중근', '용산구'] = 80
print(myframe)