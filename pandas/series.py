import pandas as pd

a = [1, 2, 3, 4, 5]
ds1 = pd.Series(a)
print(f'ds1:\n{ds1}')
print('ds1.values:', ds1.values)
print('ds1.index:', ds1.index)
print('*****\n')

ds2 = pd.Series(a, index=('a', 'b', 'c', 'd', 'e'))
print(f'ds2:\n{ds2}')
print('ds2.values:', ds2.values)
print('ds2.index:', ds2.index)
print('*****\n')

ds3 = pd.Series({'a': 1, 'b': 2, 'c': 3})
print(f'ds3:\n{ds3}')

print('ds1[0], ds3[1]:', ds1[0], ds3[1])
print(f'ds3[[0, 2]]:\n{ds3[[0, 2]]}')

ds2['6'] = 500
ds2.at['6f'] = 100
print(f'ds2["6"]: {ds2.at["6"]}')
print('*****\n')

ds_test = pd.Series([10, 100])
ds_test[[0, 1]] = [110, 200]
ds_test.at[2] = 300
print(f'ds_test:\n{ds_test}')
print(ds_test.iat[0])
print(ds_test.at[0])
print('*****\n')

print(ds_test * 2)
print('*****\n')

cities = pd.Series({'Moscow': 12600000, 'Saint-P': 5300000, 'Novosibirsk': 1620000, 'Kazan': 1257000})
print(f'cities:\n{cities}')
print('\n')
cities2 = pd.Series({'Moscow': 12600000, 'Saint-P': 5300000, 'Novosibirsk': 1620000, 'Kazan': 1257000},
                    index=['Saint-P', 'Novosibirsk', 'Kazan', 'Milan', 'Moscow'])
print(f'cities2:\n{cities2}')
print('*****\n')

test1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
test2 = pd.Series([4, 5, 6, 7], index=['a', 'b', 'e', 'd'])
print(test1 + test2)
print('*****\n')
print(test1.add(test2, fill_value=0))
print(test2.add(test1, fill_value=0))
print('*****\n')

print(f'cities2.notnull:\n{cities2.notnull()}')
print(f'cities2.isnull:\n{cities2.isnull()}')
print('*****\n')
print(cities2[cities2.isnull()])
print('*****\n')
print(cities2[cities2.notnull()])
print('*****\n')

print(cities2[cities2 > 2000000])
print('*****\n')

print('cities2 > 1600000 and cities2 < 2000000:')
print(cities2[(cities2 > 1600000) & (cities2 < 2000000)])
print('*****\n')

print(cities2[~(cities2 > 5000000) & cities2.notnull()])
print('*****\n')

for index, value in cities2.items():
    print(f'index: {index}, value: {value}')

print(cities2.shape)
print(cities2.size)
print(cities2.count())
print('*****\n')

cities3 = cities2.copy()
cities3.at['Milan'] = 3200000
print(f'cities2:\n{cities2}')
print(f'cities3:\n{cities3}')

print(cities2.agg('max'))
print(cities2.max())
print(cities2.agg(['min', 'max', 'sum', 'mean']))
print('*****\n')

# метод apply()
s = pd.Series([10, 20, 30], index=['a1', 'b1', 'c1'])


def square(x):
    return x ** 2


print(s.apply(square))

# или тоже самое можно записать:
print(s.apply(lambda x: x ** 2))
print('*****\n')

ds = pd.Series([1, 2, 3, 4])


def func(x):
    if x % 2 == 0:
        return x
    else:
        return x + 1


print(ds.apply(func))

print(ds.apply(lambda x: x if x % 2 == 0 else x + 1))

print(s.at['a1'])
print(s.iat[0])


a = 'Hello'
b = list(a)
print(range(len(a)))
if 'H' in a:
    print('-'.join(a))
else:
    print(a)
print('*****\n')


fff = pd.Series(['Aa', 'Nn'])
print(fff.apply(lambda x: x if 'n' in x else x + '!!!!!!'))


def func(x):
    if 'n' in x:
        return '-'.join(x)
    else:
        return x


print(fff.apply(func))
