import pandas as pd

df = pd.DataFrame({'country': ['France', 'USA', 'Ukrane', 'Russia'],
                   'capital': ['Paris', 'Washington', 'Kiev', 'Moscow'],
                   'population': [66.99, 328.2, 41.98, 145.97]}, index=['fr', 'us', 'ua', 'ru'])

print(df)
print('\n*****\n')

print(df['country']['fr'])
print(df['country'][0])
print(df.at['fr', 'country'])
print(df.loc['fr', 'country'])

print('\n*****\n')

print(df.index)
print(df.columns)

print('\n*****\n')

# если в файле разделитель значений не запятая, а другой знак, то надо использовать аргумент sep.
# с помощью names можно определить или переопределить заголовки столбцов
txt_df = pd.read_csv('D:\\Python projects\\обучение\\pandas\\test.txt', names=['index', 'value'], encoding='utf-8',
                     sep=';', header=0)
# print(txt_df)
txt_df.index = ['a1', 'b1', 'c1']
print(txt_df)

print('\n*****\n')

# функция read_html позволяет читать данные из сети. При этом pandas будет автоматически искать таблицы и возвращать
# список найденных таблиц. Нужную таблицу можно взять по ее индексу.
wiki_df = pd.read_html('https://ru.wikipedia.org/wiki/%D0%A2%D0%B0%D0%B1%D0%BB%D0%B8%D1%86%D0%B0')
print(wiki_df)
print('\n*****\n')
print(wiki_df[0])
print('\n*****\n')
print(wiki_df[0].at[1, 'Имя'])

# Если необходимо переименовать столбцы полученной таблицы, то надо использовать `.columns`:
names_df = wiki_df[0]
names_df.columns = ['surname', 'name', 'patronymic']
print(names_df)

print('\n*****\n')

df_json = pd.read_json('qwerty.json')
print(df_json)

print('\n*****\n')

df = pd.read_csv('city.csv')
print(df)
print('\n*****\n')

print(f'Первые строки:\n{df.head(3)}\nПоследние строки:\n{df.tail(3)}')
print('\n*****\n')

print(df.info())
print('\n*****\n')

print(f'список столбцов:\n{df.columns}')
print('\n*****\n')

print(df[df['area'].isnull()])
print('\n*****\n')

print(f'Список сколько всего регионов:\n{df.region.unique()}')
print(f'Количество регионов: {len(df.region.unique())}')
# или:
print(f'Количество регионов: {df.region.unique().size}')

print('\n*****\n')

print(df.region.value_counts())
print(df.area.value_counts(normalize=True))

print('\n*****\n')

print(df.federal_district.unique())
print(df.address.unique())

print('\n*****\n')

print(pd.get_option('display.max_rows'))
pd.set_option('max_rows', 1000)
print(df.head(61))

print('\n*****\n')

pd.reset_option('all')
print(pd.get_option('max_rows'))

print('\n*****\n')

# создание тестового dataframe
# вариант 1
my_dict = {}
for i in range(11):
    my_dict[f'column_{i}'] = [f'value_{n}' for n in range(3)]
test_df = pd.DataFrame(my_dict)
print(test_df)
print('\n*****\n')

# варивнт 2 - с помощью встроенной функции
test_df2 = pd.get_dummies(list(range(3)), prefix='column', prefix_sep='==')
print(test_df2)

print('\n*****\n')

df = pd.read_csv('price1.txt', sep=';')
print(df)

print(f'\nВыбрать одну серию title:\n{df["title"]}')

print(f'\nВыбрать сразу несколько серий:\n{df[["id", "price"]]}')

print('\n*****\n')

# Получение одиночного значения:
print(df.iat[0, 1])
print(df.at[0, 'title'])

print('\n*****\n')

# Выбрать всю строку целиком:
print(df.loc[[4]])

print('\n*****\n')

# Выбрать несколько строк:
print(df.loc[[4, 5]])

print('\n*****\n')

# Выбор строк, идущих подряд:
print(df.loc[1:4, :])

print('\n*****\n')

# Выбор нескольких строк с конкретным столбцом:
print(df.loc[[0, 2, 4], ['id', 'price']])
print('\n')
print(df.loc[[2], ['id', 'price']])
print('\n')
print(df.loc[2][['id', 'price']])

print('\n*****\n')

# Выбрать конкретные строки и срез между колонок:
print(df.loc[[0, 4], 'id':'price'])


rrr = {}
for i in range(1, 3):
    rrr[f'column_{i}'] = [f'value_{str(n)}' for n in range(1, 5)]
print(rrr)

df = pd.DataFrame(rrr)
print(df)
df = pd.get_dummies(list(range(1, 4)))
print(df)

