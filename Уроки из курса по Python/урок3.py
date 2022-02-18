# #1
# def func(a, b, c):
#     print(f'{a.title()}, {b} {years}, living in {c.title()}')
#
#
# while True:
#     name = input('Enter name: ')
#     if name.isalpha():
#         break
#     else:
#         print('Incorrect record, try again: ')
#
# while True:
#     age = input('Enter your age: ')
#     if age.isdigit():
#         break
#     else:
#         print('Incorrect record, try again: ')
#
# if 0 <= int(age) <= 20:
#     years = 'лет'
# else:
#     years = 'год(а)'
#
# place = input('Enter your location: ')
#
# func(name, age, place)
# print()

# 2
# name = ['Oleg', 'Olga', 'Petr', 'Masha', 'Bob', 'Ivan', 'Sergey']
# salary = [10000, 20000, 30000, 40000, 50000, 100000, 550000]
# MAX_SALARY = 500000
# TAX_PERCENT = 13
#
# name_sal = dict(zip(name, salary))
# print(name_sal)
#
# file = open('salary.txt', 'w+', encoding='UTF-8')
# for k, v in name_sal.items():
#     if v < MAX_SALARY:
#         file.write('{} - {}\n'.format(k, v))
# file.seek(0)
# for line in file:
#     name, salary = line.split(' - ')
#     tax = int(salary) * TAX_PERCENT / 100
#     after_tax = int(salary) - int(tax)
#     print('{}: зарплата {}, налог {}, получил {}'.format(name.upper(), salary.strip(), int(tax), after_tax))
# file.close()

# 3
# 3.1 создать функцию, принимающую на вход 3 аргумента и возвращ наибольш из них
# a, b, c = 10, 1000, 100
#
#
# def num_max(*args):
#     return max(*args)
#
#
# print(num_max(a, b, c))
# print()
#
# # 3.2 созадть функцию, принимающую на вход список и возвращ наибольший элемент списка
# d = [1, 50, -90, 100]
#
#
# def num_max2(d1):
#     return max(d1), min(d1)
#
#
# print(list(num_max2(d)))
# print()
#
# # 3.3 создать функцию, принимающую неограниченное количество строковых аргументов. Вернуть самую длинную строку.
# a = 'aaa'
# b = 'bbbba'
# c = 'c'
# d = 'abcd'
#
#
# def dig(*args):
#     return max(*args, key=len)
#
#
# print(dig(a, b, c, d))
# print()

# 4
import random
# hero = {'name': 'Hero', 'health': 100, 'damage': 50}
# enemy = {'name': 'Enemy', 'health': 100, 'damage': 50}
# def attack(person1, person2):
#     person1['health'] = person1['health'] - person2['damage']
#
#
# attack(hero, enemy)
# print(hero['health', enemy['health']])
hero = {'name': 'Hero', 'health': 100, 'damage': random.randint(10, 50), 'armor': 1.2}
enemy = {'name': 'Enemy', 'health': 100, 'damage': random.randint(10, 50), 'armor': 1.2}


def damage_recieve(person1, person2):
    person2['damage'] = person2['damage'] / person1['armor']
    return person2['damage']


def attack(person1, person2):
    person1['health'] = person1['health'] - person2['damage']
    print('Health of {} is {}. Damage of {} is {}'.format(person1['name'], person1['health'], person2['name'],
                                                          person2['damage']))
    if person1['health'] <= 0:
        print('{} WIN!!!'.format(person2['name']))


while True:
    if hero['health'] > 0 and enemy['health'] > 0:
        attack(hero, enemy)
    if hero['health'] > 0 and enemy['health'] > 0:
        attack(enemy, hero)
    else:
        break
