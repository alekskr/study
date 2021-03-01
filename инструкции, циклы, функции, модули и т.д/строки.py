import pyperclip

# метод pyperclip
spam = 'abcd'
pyperclip.copy(spam)
print(pyperclip.paste())

# срезы
name_of_person = 'Aleksandr'
print(name_of_person[-1])
print(name_of_person[0:-5])
print(name_of_person[:-5])
print(name_of_person[::-1])

# метод find()
email = 'welcome@mail.ru'
index = email.find('@')
print(index)
print(email[:index])

# методы lower() и upper()
name = 'ПеТрОв ИвАнов'
print(name.lower())
print(name.upper())
print()
print('How are you?')
# feeling = input()
feeling = 'GreAt'
if feeling.lower() == 'great':
    print('I feel great good')
else:
    print('something text')

# метод capitalize()
print(name.capitalize())

# метод title()
print(name.title())

# индекс символа
print(name.index('о'))

# длина строки
print(len(name))

# метод count() считает количество определенных символов
name = 'ПеТрОв ИвАнов'
print(name.count('в'))
print(name.lower().count('о'))

# метод split - разделяет
name = 'ПеТрОв ИвАнов Иванович'
print(name.split('Т'))
email = 'welcome@mail.ru'
print(email.split('@'))

# метод format()
name = 'Иван'
surname = 'Иванов'
print('Welcome, {} {}'.format(name, surname))
print('Welcome, {1} {0}'.format(name, surname))

# методы center() rjust() ljust() zfill()
print('начало'.center(3, '-'))
print('начало'.center(20, '-'))
print('глава 1'.ljust(10, '.'))
print('конец'.rjust(10, '.'))
print('помидор'.zfill(10))

# вывод данных
name = 'Sasha'
age = 30
money = 200.2
# обычный способ
print('Hello,', name, '. You\'re', age, '. You have only', money)
print('Hello, ' + name + '. You\'re ' + str(age) + '. You have only ' + str(money))
# старый способ, уже никто не пользуется
result = 'Hello %s, вам %i лет, у вас %f денег' % (name, age, money)
print(result)
name1 = 'Петр'
surname1 = 'Иванов'
res = 'Hello, Dear %s %s.' % (name1, surname1)
print(res)
print('Hello, Dear %s %s.' % (name1, surname1))
# новый способ
result = 'Hello, {}. Вам {} лет. У вас {} рублей'.format(name, age, money)
result1 = f'Hello, {name}. Вам {age} лет. У вас {money} рублей.'
print(result)
print(result1)
print()

# многострочные блоки
print('''С другой стороны реализация намеченного плана...

Задача организации... 

С другой стороны постоянный количественный рост...''')

# starswith() и endswith()
a = 'Hello world'
print(a.startswith('Hello'))
print(a.endswith('d'))

# .join()
a = ['cats', 'rats', 'bats']
print(', '.join(a))
b = ['My', 'name', 'is', 'sasha']
print(' '.join(b))

# Дан словарь продуктов. Вывести наименование продукта и количество
products = {'apples': 10, 'burgers': 20, 'cookies': 30, 'bananas': 5, 'nuts': 15}
products_list = list(products.keys())
print(products_list)
offset = len(max(products_list, key=len))
print(offset)


def print_items(items):
    print("-PRODUCT'S LIST-".center(offset))
    for k, v in items.items():
        print(k.ljust(offset, '.') + str(v).rjust(offset, '.'))
    all_products = 0
    for v in products.values():
        all_products = all_products + v
    print("PRODUCT'S AMOUNT :", all_products)


print_items(products)

word = "Mississippi"
# starting from the right side, all "i", "p", and "s" are removed:
print(word.rstrip("ips"))  # "M"

# the word starts with "M" rather than "i", "p", or "s", so no chars are removed from the left side:
print(word.lstrip("ips"))  # "Mississippi"

# "M", "i", "p", and "s" are removed from both sides, so nothing is left:
print(word.strip("Mips"))  # ""

string = "no clouds here to spy on pets"
print(len(string))

print('cat', 'dog', 'bat')
print('cat', 'dog', 'bat', sep=',')

dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']

a = 'rutinize is to examene closely and minutely'.split()
print(a)
b = []
for i in a:
    if i not in dictionary:
        b.append(i)
print(b)
if not b:
    print('OK')
else:
    for i in b:
        print(i)