import pandas as pd

data = pd.DataFrame({'food':['bacon', 'pulled pork', 'bacon', 'pastrami', 'corned beef',
                             'bacon', 'pastrami', 'honey ham', 'nova lox'],
                     'ounces':[4,3,12,6,7.5,8,3,5,6]})
print(data)

meat_to_animal = {
    'bacon' : 'pig',
    'pulled pork' : 'pig',
    'pastrami' : 'cow',
    'corned beef' : 'cow',
    'honey ham' : 'pig',
    'nova lox': 'salmon'
}
print(meat_to_animal)
print()

# 맵안에는 함수뿐 아니라 딕셔너리도 넣을 수 있다. 해당 데이타 보완

data['animal'] = data['food'].map(lambda x : meat_to_animal[x])
print(data)
print()

data['animal2'] = data['food'].map(meat_to_animal)
print(data)