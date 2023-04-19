import pandas as pd
import numpy as np

frame1 = pd.DataFrame(np.arange(1, 17).reshape(4,4),
                      index=['김구','이봉창','안중근','윤봉길'],
                      columns=['강남구','은평구','마포구','용산구'])
frame2 = frame1 * 10
print(frame2)
print()
print('11111111111111111111111111')
#ㄱ.첫번째 행데이터를 조회
print(frame2.loc['김구'])
print()
print('22222222222222222222222222')
#ㄴ.1번째와 3번째 행 데이터를 조회
print(frame2.loc['김구'], frame1.loc['안중근'])
print()
print('33333333333333333333333333')
#ㄴ.'윤봉길행만 조회'
print(frame2.loc['윤봉길'])
print()
print('444444444444444444444444444')
#ㄴ.'이봉창'과 '윤봉길' 행을 조회
print(frame2.loc['이봉창'], frame1.loc['윤봉길'])
print()
print('ㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁ')
#ㄴ.'윤봉길' 행의 '은평구' 데이터 조회
print(frame2.loc['윤봉길', '은평구'])
print()
print('ㅂㅂㅂㅂㅂㅂㅂㅂㅂㅂㅂㅂㅂㅂㅂㅂㅂㅂㅂ')
#ㅂ. '김구'와 '이봉창'의 '용산구'와 '은평구' 데이터 조회
#print(frame1.loc['윤봉길', '은평구'])
#print()

print('ㅅㅅㅅㅅㅅㅅㅅㅅㅅㅅㅅㅅㅅㅅㅅㅅㅅㅅㅅㅅ')
#ㄴ.'은평구'의 값이 100이하인 행들을 조회
print(frame2.('은평구'))
print()

print('ㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇ')
#ㅇ.'은평구'의 값이 100인 행들을 조회

print('ㅈㅈㅈㅈㅈㅈㅈㅈㅈㅈㅈㅈㅈㅈㅈㅈㅈㅈㅈㅈㅈㅈ')
#ㅈ.'김구'부터 '안중근'까지 '용산구'데이터를 80으로 변경