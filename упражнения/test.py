"""test"""
# a = 5
# b = 10
#
# print('введите число: ', end='')
# c = int(input())
# while c <= 0 or c >= 10:
#     print('число должно быть больше 0 и меньше 10, введите еще раз: ', end='')
#     c = int(input())
# else:
#     print('число подходит, ' + str(c) + ' ** 2 = ' + str(c ** 2))
# s = 0  # отсюда считаем сумму от с до 10
# for i in range(c, 11):
#     s = c + i
# print('сумма чисел от c до 10: ' + str(s))
# # далее меняем переменные местами
# print(a, b, c, s)
# a, b, c, s = a, s, c, b
# print(a, b, c, s)
# #
# if c > a:
#     print('вар1 (s + a) / 2 = ' + str(float((s + a) / 2)))
# elif c < a:
#     print('вар2 b * c + a ** s = ' + str(float(b * c + a ** s)))
# else:
#     print('вот так!')
# print('The end!')

# print('Введите число: ', end='')
# a = int(input())
# while a < 1 or a > 9:
#     print('неверное число, введите новое больше 0 и меньше 10: ', end='')
#     a = int(input())
# else:
#     print('число подходит, ' + str(a) + ' ** 2 = ' + str(a ** 2))
# #
# print('сумма чисел от a до 10')
# for i in range(10):
#     a = a + i
# print(a)
# print('end')
# #
# print('сумма чисел от 1000 до 2000')
# s = 1000
# for i in range(s, 2001):
#     s = s + i
# print('s = ' + str(s))


# words = ['hi', 'hey', 'yes', 'no']
# a = 0
# b = len(words) - 1
# while a <= b:
#     word = words[a]
#     print(word + '!')
#     a = a + 1
# print('*' * 30)
#
# words = ['hi', 'hey', 'yes', 'no']
# for i in words[0:2]:
#     print(i)


# def fahrenheit_to_celsius(temps_f):
#     temps_c = (temps_f - 32) * 5 / 9
#     print('{} C'.format(round(temps_c, 2)))
#
#
# def celsius_to_fahrenheit(temps_c):
#     temps_f = temps_c * 9 / 5 + 32
#     print('{} {}'.format(round(temps_f, 2), 'F'))
#
#
# def main():
#     """Entry point of the program."""
#     temperature, unit = input().split()  # read the input
#     if unit.lower() == 'f':
#         return fahrenheit_to_celsius(int(temperature))
#     if unit.lower() == 'c':
#         return celsius_to_fahrenheit(int(temperature))
#
#
# # main()
# print(main())


# iris = {}
#
#
# def add_iris(id_n, species, petal_length, petal_width, **kwargs):
#     global iris
#     parameters = {'species': species, 'petal_length': petal_length, 'petal_width': petal_width}
#     parameters.update(kwargs)
#     new_iris = {id_n: parameters}
#     iris.update(new_iris)
#     print(iris)
#
#
# add_iris(0, 'Iris versicolor', 4.0, 1.3, petal_hue='pale lilac')


# def add_iris(id_n, species, petal_length, petal_width, **kwargs):
#     global iris
#     parameters = {'species': species, 'petal_length': petal_length, 'petal_width': petal_width}
#     parameters.update(kwargs)
#     iris[id_n] = parameters
#     print(iris)
#
#
# add_iris(0, 'Iris versicolor', 4.0, 1.3, petal_hue='pale lilac')


# people = {'Jackie': 176, 'Wilson': 185, 'Saersha': 165, 'Roman': 185, 'Abram': 169}
#
#
# def tallest_people(**kwargs):
#     names = []
#     max_value = max(kwargs.values())
#     print(max_value)
#     for k, v in kwargs.items():
#         if v == max_value:
#             names.append(k)
#             names.sort()
#     for name in names:
#         print('{} : {}'.format(name, max_value))


# print(tallest_people(Jackie=176, Wilson=185, Saersha=165, Roman=185, Abram=169))
# tallest_people(Jackie=176, Wilson=185, Saersha=165, Roman=185, Abram=169)


# import sys
# # while True:
# print('Type exit to exit')
# response = input()
# if response == 'exit':
#     sys.exit()
# print('You typed ' + response + '.')

# import math
# print(math.sqrt(4))
#
# from collections import Counter
# parking = ['Audi', 'BMW', 'VW', 'Audi', 'Lada', 'VW']
# brand = Counter(parking)
#
# print('\nКоличество элементов:', brand)
#
# print('\nКаждый элемент словаря на новой строке:')
# for i in brand:
#     print(i, brand[i])
#
# print('\nКоличество букв в определенном элементе:')
# letters = Counter(parking[4])
# print(letters)


# a = -1
# print(abs(a))

# import math

# h = 5
# r = 3
# volume = math.pi * math.pow(r, 2) * h  # 141.3716...
# print(round(volume, 1))  # 141.4
#
# a = abs(int(input()))
# S = 2 * math.sqrt(3) * math.pow(a, 2)
# V = 1 / 3 * math.sqrt(2) * math.pow(a, 3)
# print(round(S, 2), round(V, 2))
#
# a = abs(int(input()))
# b = int(input())
# if b < 1:
#     z = math.log(a)
# else:
#     z = math.log(a, b)
# print(round(z, 2))
#
# r = 3.5
# s = math.pi * math.pow(r, 2)
# print(round(s, 2))
# print(math.pi)

# a = math.radians(float(input()))
# a = float(input())
# sin = math.sin(a)
# cos = math.cos(a)
# print(sin - cos)


# def object_with_beautiful_identity():
#     for i in range(10_000):
#         # Change the next line
#         if str(id(i))[-3:] == '888':
#             print(i)
#             return i
#     return None
#
#
# object_with_beautiful_identity()


# one_ancestor = input()
# other_ancestor = input()
#
# # Calculate the identity of a new alien here
# new_alien = int((id(one_ancestor) + id(other_ancestor)) / 2)
# print(new_alien)

# a = 100
# b = 100
# c = 10000
# d = 10000
# a = [1, 2, 3]
# b = [1, 2, 3]
# print(a is b)
# a = [2, 3, 9]
# b = a
# b[2] = 10
# c = b
#
# print(a)
# print(b)
# print(c)
# print(a is c)


# def print_book_info(title, author=None, year=None):
#     if author is None and year is not None:
#         print('"{}" was written in {}'.format(title, year))
#     elif year is None and author is not None:
#         print('"{}" was written by {}'.format(title, author))
#     elif author is None and year is None:
#         print('"{}"'.format(title))
#     else:
#         print('"{}" was written by {} in {}'.format(title, author, year))

# n = 1
# for i in range(1, 365):
#     n = n + i
# print(n)

# ghostbusters = {'Peter', 'Raymond', 'Egon'}
# soldiers = {'Winston'}
# secretaries = {'Janine'}
#
# ghostbusters |= soldiers
# print(ghostbusters)
# ghostbusters.update(secretaries)
# print(ghostbusters)

# numbers1 = {1, 2, 3, 4}
# numbers2 = {0, 2, 3}
# numbers1.intersection_update(numbers2)
# print(numbers1)

# a = set("my code is brOKen")
# b = "i'm not OK with that"
# c = a.union(b)
# print(c)


# n = abs(int(input()))
i = []

# my_list = [[1, 2] for i in range(n)]
# print(my_list)

# nums = [x * 2 for x in range(11) if x % 2 == 1]
# print(nums)

# a = ['123']
# b = []
# for i in a:
#     for j in i:
#         j = int(j)
#         b.append(j)
# print(sum(b)/len(b))
#
# a = '123'
# # for i in a:
# #     print(i)
# a = input()
# s = [float(i) for i in a]
# print(sum(s) / len(s))

# a = '15325'
# # a = input()
# b = [int(i) for i in a]
# c = []
# for i, _ in enumerate(b):
#     c.append(b[i] + sum(b[0:i]))
# print(c)


# students = [["Will", "B"], ["Kate", "B"], ["Max", "A"], ["Elsa", "C"], ["Alex", "B"], ["Chris", "A"]]
# c = []
# for i in students:
#     if i[1] == 'A':
#         c.append(i[0])
# print(c)
#
# c = [i[0] for i in students if i[1] == 'A']
# print(c)


# text = [["Glitch", "is", "a", "minor", "problem", "that", "causes", "a", "temporary", "setback"],
#         ["Ephemeral", "lasts", "one", "day", "only"],
#         ["Accolade", "is", "an", "expression", "of", "praise"]]
# text1 = []
# for i in text:
#     for j in i:
#         text1.append(j)
# print(text1)
#
# a = int(input())
# b = []
# for i in text1:
#     if len(i) <= a:
#         b.append(i)
# print(b)
#
# t1 = [j for i in text for j in i]
# t2 = [i for i in t1 if len(i) <= a]
# print(t2)

# symbol = input()
# list1 = list(symbol[:3])
# list2 = list(symbol[3:6])
# list3 = list(symbol[6:])
# field = [list1, list2, list3]
# print(field)
# # field = [['X', 'O', 'X'], ['O', 'X', 'O'], ['X', 'O', 'O']]
# print('---------')
# for line in field:
#     print('|', line[0], line[1], line[2], '|')
# print('---------')

# import mymodule
#
# mymodule.hello()
# print(mymodule.fib(10))

# n = int(input())
# summa = 0
# for _ in range(n):
#     a = int(input())
#     summa += a
# print(summa / n)


# n = int(input())
# if n == 1:
#     print('This number is not prime')
# else:
#     for i in range(2, n):
#         if n % i == 0:
#             print('This number is not prime')
#             break
#     else:
#         print('This number is prime')


# for i in range(10):
#     line = "*"
#     for j in range(10):
#         if i == j:
#             break
#         line = line + "{}".format(j)
#     print(line)

# import datetime
#
# some_date = datetime.datetime(3486, 5, 15, 23, 59)
# print(some_date.time())
# print((some_date.date()))

###
# import random
# import string
#
#
# def password_generator(length):
#     chars = string.ascii_letters + string.digits
#     exep = ('O', '0', 'l', '1')
#     password = ''
#     while len(password) != length:
#         char = random.choice(chars)
#         if char not in exep:
#             password = password + char
#     return password
#
#
# print(password_generator(10))

# pasta = "tomato, basil, garlic, salt, pasta, olive oil"
# apple_pie = "apple, sugar, salt, cinnamon, flour, egg, butter"
# ratatouille = "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt"
# chocolate_cake = "chocolate, sugar, salt, flour, coffee, butter"
# omelette = "egg, milk, bacon, tomato, salt, pepper"
#
# ingr = input()
# dishes = {pasta: 'pasta', apple_pie: 'apple pie', ratatouille: 'ratatouille', chocolate_cake: 'chocolate cake',
#           omelette: 'omelette'}
# for k, v in dishes.items():
#     if ingr in k:
#         print(f'{v} time!')


# def fahrenheit_to_celsius(temps_f):
#     temps_c = (temps_f - 32) * 5 / 9
#     return round(temps_c, 2)
#
#
# def celsius_to_fahrenheit(temps_c):
#     temps_f = temps_c * 9 / 5 + 32
#     return round(temps_f, 2)
#
#
# def main():
#     """Entry point of the program."""
#     temperature, unit = input().split()
#     if unit in ('c', 'C'):
#         print(celsius_to_fahrenheit(float(temperature)), 'F')
#     else:
#         print(fahrenheit_to_celsius(float(temperature)), 'C')
#
#
# main()


# def sq_sum(*args):
#     a = []
#     for i in args:
#         sq = i * i
#         a.append(sq)
#     return sum(a)
#
#
# print(sq_sum(1, 2, 2, 4))


# a = int(input())
# b = int(input())
# c = [i for i in range(a, b + 1) if i % 3 == 0]
# print(sum(c) / len(c))


# def check_list(lst):
#     return lst and lst[0]
#
#
# lists = [[5, 9], [0, 0], []]
# result = []
# for lst in lists:
#     result.append(check_list(lst))
#
# print(result)
# print(5 or 0)
# print(0 or 5)


# def compare(numerator, denominator):
#     return bool(denominator) and numerator / denominator == 0.5
#
#
# a = int(input())
# b = int(input())
#
# print(compare(a, b))


# import math
#
# def sigma_func(x):
#     return math.exp(x) / (math.exp(x) + 1)
#
#
# a = int(input())
# print(round(sigma_func(a), 2))

# a = ['ONE', 'TWO', 'THREE']
# b = ['one', 'two', 'three']
# c = dict(zip(a, b))
# print(c)
# with open('D:\\Python projects\\обучение\\1.csv', 'w') as f:
#     for k, v in c.items():
#         f.write('{}{}'.format(k, v))

import subprocess


import subprocess
book = 'C:\\Users\\alexk\\Desktop\\1.txt'
program = 'notepad.exe'
subprocess.Popen([program, book]).wait()

print('ok')