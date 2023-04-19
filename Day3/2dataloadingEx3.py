import pandas as pd

frame = pd.read_excel('monthly_sales.xlsx', header=1, index_col=0)
print(frame)

# 쉬트 여러개 있을 때

frame2 = pd.read_excel('class_info.xlsx', header=0, sheet_name='2학년')
print(frame2)
print()

frame2 = pd.read_excel('class_info.xlsx', header=0, sheet_name=0)
print(frame2)
print()

# 모든 쉬트 읽어 올때 -> 딕셔너리 형태로 읽어 옴
data = pd.read_excel('class_info.xlsx', sheet_name=None)
print(data)
print()

# 2학년 데이타만 읽어올 때
print(data['2학년'])

# 지정된 쉬트만 가져올 때
data2 = pd.read_excel('class_info.xlsx', sheet_name=['1학년', '2학년'])
print(data2)

# 데이타 크면 csv, xlsx는 엄청 느리다.
