import random

# table_data = [['apples', 'oranges', 'bananas', 'kiwi'],
#               ['elephants', 'dogs', 'cats', 'birds'],
#               ['bmw', 'lada', 'kia', 'volkswagen']]


# def print_table(table):
#     list_table_data = []
#     for number in range(len(table)):
#         list_table_data = list_table_data + table[number]
#     # print(list_table_data)
#     offset = len(max(list_table_data, key=len))
#     # print(offset)
#     print('fruits'.center(offset).upper(), 'animals'.center(offset).upper(),
#           'cars'.center(offset).upper())
#     for i in range(len(table[0])):
#         for j in range(len(table)):
#             print(table[j][i].center(offset), end=' ')
#         print()


# print_table(table_data)


# items = {'rifle': 1, 'bullits': 200, 'bow': 1, 'arrows': 100, 'dagger': 1}
# dragon_loot = ['coin', 'dagger', 'coin', 'ruby', 'coin']


# def display_inventory(inv):

#     # считаем отступ
#     keys_list = []
#     for key in inv.keys():
#         keys_list.append(key)
#     offset = len(max(keys_list, key=len))

#     # выводим наименование, количество и общее количество
#     item_total = 0
#     for k, v in inv.items():
#         item_total += v
#         print(k.ljust(offset + 1, '_'), v)
#     print('Item total: {}'.format(item_total))


# def add_to_inventory(inventory, loot):
#     for i in loot:
#         inventory.setdefault(i, 0)
#         inventory[i] = inventory[i] + 1
#     print(inventory)

# display_inventory(items)
# add_to_inventory(items, dragon_loot)

# fruits = ["яблоко", "банан", "киви", "арбуз"]
# offset = len(max(fruits, key=len))
# for i, item in enumerate(fruits, start=1):
#     # print(i, item.rjust(offset))
#     print('{}. {}'.format(i, item.rjust(offset)))


# h = [1,2,3,4,5]
# print(sum(h, start=0))


# def my_func(name, surname='Guest'):
#     print(name, surname)
#     # return name, surname


# n = 'Sasha'
# my_func(n)
# my_func(n, 'Kriyt')


# def func(*args):
#     # print(name)
#     print(list(args))

# func(n, 1,23, 'ghhjhg')


# def func(name, age, surname):
#     print(name, surname, age)
#
#
# func(surname='Kriyt', age=34, name=n)


# def func(name, **kwargs):
#     print(name, kwargs)
#
#
# func(n, surname='Kriyt', age=34, flat=150)


# names = ('Ivan', 'Oleg', 'Ben')
# ages = [30, 25, 40]
#
#
# for name, age in zip(names, ages):
#     print(name, age)
# print(list(zip(names, ages)))
# print(dict(zip(names, ages)))


# def my_pow(x):
#     return x ** 2
#
#
data = [-2, -10, 6, 19]


# result = []
#
# for num in data:
#     num_2 = my_pow(num)
#     result.append(num_2)
# print(result)
#
# result_1 = list(map(my_pow, data))
# print(result_1)


# def my_filter(x):
#     return x > 0
#
#
# print(list(filter(my_filter, data)))


# result = list(map(lambda x: x ** 2, data))
# print(result)
#
# result = list(filter(lambda x: x > 0, data))
# print(result)

# a = 'parselTongue'
# if a.islower():
#     print(a)
# else:
#     for i in a:
#         if i.isupper():
#             a = a.replace(i, "_" + i.lower())
#     print(a)


# income = int(input())
# if 0 < income <= 15527:
#     tax_percent = 0
# elif 15528 <= income <= 42707:
#     tax_percent = 15
# elif 42708 <= income <= 132406:
#     tax_percent = 25
# else:
#     tax_percent = 28
# tax = round(income * tax_percent / 100)
# print('The tax for {} is {}%. That is {} dollars!'.format(income, tax_percent, tax))
#
# jack_age = int(input())
# alex_age = int(input())
# lana_age = int(input())
# print(min(jack_age, alex_age, lana_age))

# word1 = input()
# word2 = input()
# How many letters does the longest word contain?
# len_max_word = len(max(word1, word2, key=len))

# def closest_mod_5(x):
#     if x % 5 == 0:
#         return x
#     return x + (5 - x % 5)

# name = "John"
#
#
# def change_name(new_name):
#     global name
#     name = new_name
#
#
# change_name("Mary")
# print(name)


# def subtract(a, b):
#     print(a - b)
#
#
# subtract(b=3, a=1)


# def heading(a, n):
#     if n <= 1:
#         return '#', a
#     elif n == 2:
#         return '#' * 2, a
#     elif n == 3:
#         return '#' * 3, a
#     elif n == 4:
#         return '#' * 4, a
#     elif n == 5:
#         return '#' * 5, a
#     else:
#         return '#' * 6, a
#
#
# list_from_string = input().split()
# some_string = list_from_string[0]
# while True:
#     try:
#         level = int(list_from_string[1])
#         break
#     except IndexError:
#         level = 1
#         break
# print(list_from_string)
# heading(some_string, level)

#
# a = 'fhfgh'
# b = tuple(a)
#
# oceans = ['Atlantic', 'Pacific', 'Indian', 'Southern', 'Arctic']
# oceans = tuple(oceans)
# print(oceans)
#
# numbers = list(int(n) for n in input().split())
# print(numbers)

# a = ([])
# print(a)
#
# weekend = 'Saturday', 'Sunday'
# print(weekend)        # ('Saturday', 'Sunday')
# print(type(weekend))  # <class 'tuple'>
#
#
# first_name = 'ss'
# last_name = 'aa'
# full_name = first_name, last_name
# print(full_name)

#
# def final_deposit_amount(*interest, amount=1000):
#     for i in interest:
#         amount = (amount * i / 100) + amount
#     print(amount)
#     return round(amount, 2)
#
#
# final_deposit_amount(5, 7, 4)

#
# def tracklist(**kwargs):
#     for band in kwargs:
#         print(band)
#         for album, song in kwargs[band].items():
#             print('ALBUM:', album, 'TRACK:', song)
#
#
# tracklist(Woodkid={"The Golden Age": "Run Boy Run",
#                    "On the Other Side": "Samara"},
#           Cure={"Disintegration": "Lovesong",
#                 "Wish": "Friday I'm in love",
#                 "Seventeen Seconds": "A Forest"})
#
#
# def tracklist1(**kwargs):
#     for band in kwargs:
#         print(band)
#         for k, v in kwargs[band].items():
#             if type(v) is list:
#                 v = ', '.join(v)
#                 print('{}: {}'.format(k, v))
#             else:
#                 print('{}: {}'.format(k, v))
#         print()
#
#
# tracklist1(METALLICA={"Genre": "metal", "Tracks": ['Unforgiven II', "It's doesn't else matter",
# 'Whiskey in the jar']},
#            LINKIN_PARK={"Genre": "alternative", "Tracks": ['Numb', 'In the end', 'Battlesweet symphony']})

# import re
# phone_number_regex = re.compile(r'\d\d\d-\d\d-\d\d')
# a = phone_number_regex.search('Доставка пиццы Санкт-Петербург. 8 800 333-00-60')
# print(a.group())


# def select_dates(pers_data):
#     names = []
#     for i in pers_data:
#         for v in i.values():
#             if type(v) is int and v > 30:
#                 if i['city'] == 'Berlin':
#                     for j in i['hobbies']:
#                         if j == 'art':
#                             names.append(i['name'])
#                 break
#     return ', '.join(names)


# def select_dates(pers_data):
#     names = []
#     for i in pers_data:
#         if i['age'] > 30 and i['city'] == 'Berlin' and 'art' in i['hobbies']:
#             names.append(i['name'])
#     print(', '.join(names))
#
#
# potential_dates = [{"name": "Julia", "gender": "female", "age": 29,
#                     "hobbies": ["jogging", "music"], "city": "Hamburg"},
#                    {"name": "Sasha", "gender": "male", "age": 18,
#                     "hobbies": ["rock music", "art"], "city": "Berlin"},
#                    {"name": "Maria", "gender": "female", "age": 35,
#                     "hobbies": ["art"], "city": "Berlin"},
#                    {"name": "Daniel", "gender": "non-conforming", "age": 50,
#                     "hobbies": ["boxing", "reading", "art"], "city": "Berlin"},
#                    {"name": "John", "gender": "male", "age": 41,
#                     "hobbies": ["reading", "alpinism", "museums"], "city": "Munich"}]
# select_dates(potential_dates)


# shopping_list = ["milk", "olive oil", "bananas", "brownie"]
#
# shopping_list.remove("milk")
# print(shopping_list)


# def heading(text, level=1):
#     if level <= 1:
#         level = 1
#     if level >= 6:
#         level = 6
#     return f'{"#" * level} {text}'


# def get_percentage(number, round_digits=None):
#     number = number * 100
#     if round_digits is None:
#         return str(int(number)) + '%'
#     return str(round(number, round_digits)) + '%'
#
#
# num = float(input())
# round_num = int(input())
# print(get_percentage(num, round_num))
# print(get_percentage(num))


# user_city = "Istanbul"
#
#
# def change_city(new_user_city):
#     return new_user_city
#
#
# print(change_city("Paris"))
# print(user_city)

# user_city = "Istanbul"
#
# def change_city(new_user_city):
#     global user_city
#     user_city = new_user_city
#
# change_city("Paris")
# print(user_city)


# def person(pers_data):
#     for i in pers_data:
#         print('{}, дата рождения {}, место рождения {}'.format(i['name'], i['birth date'], i['city']))
#
#
# humans = [{'name': 'Vasiliy', 'birth date': (10, 10, 1976), 'city': 'Moscow'},
#           {'name': 'Olga', 'birth date': 1993, 'city': 'Novgorod'}]
# person(humans)
# print()


# names = ['Sasha', 'Lena', 'Boris', 'Petr', 'Oleg', 'Igor']
# salary = [100000, 95000, 20000, 50000, 80000, 150000]
# TAX = 13
# MAX_SALARY = 140000
#
# salary_name = dict(zip(names, salary))
# print(salary_name)
# file = open('salary.txt', 'w', encoding='UTF-8')
# for k, v in salary_name.items():
#     if v < MAX_SALARY:
#         file.write('{} - {} \n'.format(k, v))
# file.close()
#
# file = open('salary.txt', 'r', encoding='UTF-8')
# for line in file:
#     name_salary = line.strip().split(' - ')
#     salary_with_tax = int(name_salary[1]) - (int(name_salary[1]) * TAX / 100)
#     print('{} получил зарплату {}, с вычетом налогов получил {}'.format(name_salary[0].upper(),
#                                                                         name_salary[1], salary_with_tax))

# A = int(input())
# B = int(input())
# H = int(input())
#
# if A <= H < B:
#     print('Normal')
# elif H < A:
#     print('Deficiency')
# else:
# # if H > B:
#     print('Excess')

# x = float(input())
# y = float(input())
# if x > 0 and y > 0:
#     print('I')
# elif x > 0 and y < 0:
#     print('IV')
# elif x < 0 and y > 0:
#     print('II')
# else:
#     print('III')

# text = 'Nobody. expects? the, Spanish inquisition!'
# print(text.replace('.', '').replace(',', '').replace('!', '').replace('?', ''))
# list_puntuanions = ['.', ',', '!', '?']
# for i in list_puntuanions:
#     text = text.replace(i, '')
# print(text.lower())
#
#
# punc_replace = [(",", ""), (".", ""), ("!", ""), ("?", "")]
# sentence = 'Nobody. expects? the, Spanish inquisition!'
# for x, y in punc_replace:
#     # print(x, y)
#     sentence = sentence.replace(x, y)
# print(sentence.lower())

# text = 'fvfv hyh eddffv'
# print(text.replace('', ' '))


# names = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
# digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# nam_dig = dict(zip(digits, names))
# print(nam_dig)
# nam_dig = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven',
#            '8': 'eight', '9': 'nine'}
# number = input()
# print(number)
#
# for i in number:
#     for k, v in nam_dig.items():
#         if i == k:
#             print(v)


def what_to_do(instructions):
    # if 'Simon says' in instructions:
    #     index = instructions.find('Simon says')
    index = instructions.find('Simon says')
    if instructions.startswith('Simon says'):
        print('I', instructions[index:])
    elif instructions.endswith('Simon says'):
        print('I', instructions[:index+1])
    else:
        return "I won't do it!"


instruction = input()
what_to_do(instruction)
