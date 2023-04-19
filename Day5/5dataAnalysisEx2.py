import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.rc('font', family='malgun Gothic')

welfare = pd.read_csv('welfare_python.csv', encoding='utf-8')
welfare.info()
print()

print(welfare.head())
print()

welfare.loc[welfare['gender'] == 1, ['gender']] == '남성'
welfare.loc[welfare['gender'] == 2, ['gender']] == '여성'
print(welfare)
print()

thisyear = 2023
welfare['age'] = thisyear - welfare['birth'] + 1
print(welfare.head())
print()

# 1 : 결혼, 3: 이혼,
def setMarriage(x) :
    if x == 1 :
        return '결혼'
    elif x == 3 :
        return  '이혼'
    else :
        return '무응답'

welfare['marriage'] = welfare['marriage'].apply(setMarriage)
print(welfare.head())
print()

# income 비어 있는 곳을 평균값으로 채우기
welfare.loc[welfare['income'].isnull(), 'income'] = welfare['income'].mean()
print(welfare.head())
print()

# code job 숫자를..
jobFrame = pd.read_csv('welfare_job.csv', encoding='cp949')
print(jobFrame.head())
print()

welfare = pd.merge(welfare, jobFrame, on='code_job')
print(welfare)
print()

def setReligion(x) :
    if int(x) == 1:
        return '있음'
    else:
        return '없음'

welfare['religion'] = welfare['religion'].apply(setReligion)
print(welfare.head())
print()

def newAge(x):
    if x < 30:
        return '청년'
    elif x >= 30 and x < 60:
        return '중년'
    else:
        return '노년'

welfare['age'] = welfare['age'].apply(newAge)
print('====-----------==================')
print(welfare.head())
print()

# 영어를 한글로
col_mapping = {'gender':'성별', 'birth':'생일', 'marriage':'결혼 유무', 'religion':'종교 유무',
               'code_job':'직업 코드', 'income':'소득', 'code_religion':'지역구',
               'age':'나이', 'job':'직업', 'ageg':'연령대'}
welfare = welfare.rename(columns=col_mapping)
welfare.info()
print()


# col_mapping = {'gender':'성별', 'birth':'생일', 'marriage':'결혼 유무', 'religion':'종교 유무',
#                'code_job':'직업 코드', 'income':'소득', 'code_religion':'지역구',
#                'age':'나이', 'job':'직업','ageg':'연령대'}
# print('============================================')
# welfare = welfare.rename(columns=col_mapping)
# welfare.info()
# print()

import seaborn as sns

# sns.countplot(data=welfare, x='결혼 유무', order=['결혼', '이혼', '무응답'], hue='종교 유무')
# plt.show()
#
# sns.countplot(data=welfare, y='결혼 유무', order=['결혼', '이혼', '무응답'], hue='종교 유무')
# plt.show()
print('---------------------------------')
pdata = welfare.pivot_table(index='성별', columns='결혼 유무', values='나이', aggfunc='mean')
print(pdata)
print()


# #내코드
# pdata = welfare.pivot_table(index='성별', columns='결혼 유무', values='나이', aggfunc='mean')
# print(pdata)
# print()

sns.heatmap(data=pdata, annot=True)
plt.show()
# #내코드
# sns.heatmap(data=pdata, annot=True)
# plt.show()




# nwelfare = welfare.loc[:, ['직업 코드', '소득', '나이']]
# sns.pairplot(data=nwelfare)
# plt.show()




# nwelfare = welfare.loc[:, ['직업코드', '소득', '나이', '결혼유무']]
# sns.pair




# sns.violinplot(data=welfare, x='성별', y='나이', hue='종교유무')
# plt.show()