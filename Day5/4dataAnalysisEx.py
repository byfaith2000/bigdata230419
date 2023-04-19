import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

fec = pd.read_csv('P00000001-ALL.csv')
fec.info()
print()

print(fec.loc[123456])

unique_cands = fec.cand_nm.unique()
print(unique_cands)
print()

parties = {'Bachmann, Michelle':'Republican',
           'Cain, Herman':'Republican',
           'Gingrich, Newt':'Republican',
           'Huntsman, Jon':'Republican',
           'Johnson, Gary Earl':'Republican',
           'McCotter, Thaddeus G':'Republican',
           'Obama, Barack':'Democrat',
           'Paul, Ron':'Republican',
           'Pawlenty, Timothy':'Republican',
           'Perry, Rick':'Republican',
           "Roemer, Charles E. 'Buddy' III":'Republican',
           'Romney, Mitt':'Republican',
           'Santorum, Rick':'Republican'}

fec['party'] = fec.cand_nm.map(parties)
print(fec.head())
print()

print(fec['party'].value_counts())
print()

fec = fec[fec.contb_receipt_amt > 0]
print()

print(fec.contbr_occupation.value_counts()[:10])
print()

occ_mapping = {
    'INFORMATION REQUESTED PER BEST EFFORTS':'NOT PROVIDED',
    'INFORMATION REQUESTED':'NOT PROVIDED',
    'INFORMATION REQUESTED (BEST EFFORTS)':'NOT PROVIDED',
    'C.E.O':'CEO',
    'C.E.O.':'CEO'
}

f = lambda x : occu_mapping.get(x, x)  # Information requested를 x로 넣으면 Not Proveded가 되고 입력 x가 없는 것은 입력 x가 그대로 입력되도록 하는 함수
fec.contbr_occupation = fec.contbr_occupation.map(f)
print(fec.contbr_occupation.value_counts()[:10])
print()

by_occupation = fec.pivot_table('contb_receipt_amt',
                                index='contbr_occupation',
                                columns='party',
                                aggfunc='sum')

print(by_occupation)
print()

over_2mm = by_occupation[by_occupation.sum(axis=1) > 2000000]
print(over_2mm)
print()

# bar 그래프
# over_2mm.plot(kind='barh')
# plt.show()

fec_mrbo = fec[fec.cand_nm.isin(['Obama, Barack', 'Romney, Mitt'])]
# print(fec_mrbo)

def get_top_amounts(group, key, n=5):
    totals = group.groupby(key)['contb_receipt_amt'].sum()
    return totals.sort_values(ascending=False)[:n]

grouped = fec_mrbo.groupby('cand_nm')
grouped.apply(get_top_amounts, 'contbr_occupation', n=7)
print()

# 구간을 나눔
bins = np.array([0, 1, 10, 100, 1000, 10000, 100000, 1000000, 10000000])
labels = pd.cut(fec_mrbo.contb_receipt_amt, bins)
print(labels)
print()

grouped = fec_mrbo.groupby(['cand_nm', labels])
print(grouped.size())
print()
# 행을 열로 가게
print(grouped.size().unstack(0))
print()

# 후보자별 금액합계
bucket_sums = grouped.contb_receipt_amt.sum().unstack(0)
print(bucket_sums)
print()

# 후보자별 퍼센티지
normed_sums = bucket_sums.div(bucket_sums.sum(axis=1), axis=0)
print(normed_sums)


# 그래프 그리기
normed_sums[:-2].plot(kind='barh', stacked=True)
plt.show()








