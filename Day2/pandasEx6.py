import numpy as np
import pandas as pd

np.random.seed(12345)
frame1 = pd.DataFrame(np.random.randn(4,3),
                      index=['seoul', 'busan', 'incheon', 'daegu'],
                      columns=['att1', 'att2', 'att3'])
print(frame1)
print()
print('--------------------------------------')
# apply, map 많이 사용함
# 데이터프레임에서 특정 행(또는 열) 또는 전체값들을 내가 정의해 놓은 함수의 리턴값으로 바꿀 때 사용
# 형식 : df['A열이름'] = df['A'].apply(함수이름)
# 람다는 함수를 축약, x는 매개변수, : 오른쪽이 리턴값
# Dataframe일때 apply (함수, 축정보) , 해당축, 시리즈가 함수로 들어감
f1 = lambda x : x.max() - x.min()
print(frame1.apply(f1, axis=0))
print()
print(frame1.apply(f1, axis=1))
print('=======================================')
def f2(x) :
    return pd.Series([x.min(), x.max()], index=['min', 'max'])

print(frame1.apply(f2, axis=0))
print()

# Dataframe일때 apply map (함수) 하면 Dataframe 각 요소가 함수로 들어감

# 원본이 바뀌진 않음
f3 = lambda x : round(x, 2)
print(frame1.applymap(f3))
print()

# 시리즈일 때 map (함수) 사용하면 시리즈의 각값을 함수에서 사용
print(frame1['att2'].map(f3))

