import math
import random

print('Задача 1'.center(len(max('Задача 1')) + 15, '-'))
# написать программу, выводящую фрукты в виде пронумерованного списка, выровненного по правой стороне

fruits = ['banana', 'apple', 'apricot']

right_offset = len(max(fruits, key=len))
print(max(fruits, key=len))
print(len(max(fruits, key=len)))

for i in range(len(fruits)):
    print(f'{i + 1}. {fruits[i].rjust(right_offset)}')

print()

for i, fruit in enumerate(fruits, start=1):
    # print(f'{i}. {fruit.rjust(right_offset)}')
    print('{}. {}'.format(i, fruit.rjust(right_offset).title()))

print('\n', 'Задача 2'.center(len(max('Задача 1')) + 15, '-'))
#  Даны два списка. Надо удалить из первого списка элементы, присутствующие во втором
list_a = [1, 2, 3, 4, 4, 5, 1, 6]
list_b = [3, 4, 5, 6, 3, 7]

for i in list_b:
    while i in list_a:
        list_a.remove(i)
print(list_a)

print('\n', 'Задача 3'.center(len(max('Задача 1')) + 15, '-'))
a = [1, 2, 3, 4, 4, 5, 1, 6]
c = []
for i in a:
    if i % 2 == 0:
        j = i / 4
        c.append(j)
    else:
        k = i * 2
        c.append(k)
print(c)

print('\n', 'Задача 4'.center(len(max('Задача 1')) + 15, '-'))
a = [4, 2, 16, 0, 99, 15, 67, -50]
b = []

for i in a:
    if i >= 0:
        c = math.sqrt(i)
        if c == int(math.sqrt(i)):
            b.append(int(c))
print(b)

print('\n', 'Задача 5'.center(len(max('Задача 1')) + 15, '-'))
days = ('', 'первое', 'второе', 'третье', 'четвертое', 'пятое',
        'шестое', 'седьмое', 'восьмое', 'девятое', 'десятое',
        'одиннадцатое', 'двенадцатое', 'тринадцатое',
        'четырнадцатое', 'пятцадцатое', 'шестнадцатое',
        'семьнадцатое', 'восемьнадцатое')
months = ('', 'января', 'февраля', 'марта', 'апреля',
          'мая', 'июня', 'июля', 'августа', 'сентября',
          'октября', 'ноября', 'декабря')
date = '01.01.2010'
# date = input('enter date in dd.mm.yyyy: ')
day, month, year = date.split('.')
day = int(day)
month = int(month)
year = int(year)
print(f'{days[day]} {months[month]} {year} года')

print('\n', 'Задача 6'.center(len(max('Задача 1')) + 15, '-'))
# написать алгоритм, заполняющий список произвольн целыми
# числами в диапазоне от -100 до 100
# вариант 1
a = []
k = 10
while len(a) != k:
    b = random.randint(-100, 100)
    a.append(b)
print(a)
# вариант 2
a = []
i = 10
for i in range(0, i):
    b = random.randint(-100, 100)
    a.append(b)
print(a)

print('\n', 'Задача 7'.center(len(max('Задача 1')) + 15, '-'))
a = [1, 2, 2, 3, 5, 6, 1, 3, 9, 9]
# вывести список с неповторяющимися элементами исходного списка
# вариант 1
b = []
for i in range(len(a)):
    if a[i] not in b:
        b.append(a[i])
print(b)
# вариант 2
b = []
for i in a:
    if i not in b:
        b.append(i)
print(b)
# вариант 3
b = list(set(a))
print(b)
# вывести список с элементами исходного списка, которые не имеют повторений
b = []
for i in a:
    if a.count(i) == 1:
        b.append(i)
print(b)

# print('\n', 'Задача 8'.center(len(max('Задача 1')) + 15, '-'))
# # Проверка правильности даты
#
#
# def date_right(d, m, y):
#     if d in days30 and m in months30 and d != days30[27] and m != months30[0]:
#         print(f'{d}.{m}.{y}')
#     elif d in days31 and m in months31:
#         print(f'{d}.{m}.{y}')
#     elif d in days30[0:28] and months30[0]:
#         print(f'{d}.{m}.{y}')
#     else:
#         print('Дата задана неверно')
#
#
# days30 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
#           11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
#           21, 22, 23, 24, 25, 26, 27, 28, 29, 30)
# days31 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
#           11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
#           21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31)
#
# months30 = (2, 4, 6, 9, 11)
# months31 = (1, 3, 5, 7, 8, 10, 12)
# date = input('Введите дату в формате dd.mm.yyyy: ')
# d1, m1, y1 = date.split('.')
# d1 = int(d1)
# m1 = int(m1)
# y1 = int(y1)
#
# date_right(d1, m1, y1)

print('\n', 'Задача 9'.center(len(max('Задача 1')) + 15, '-'))
# Уравнение задано в виде строки: y = kx + (или - * /) b. Определить y с заданным x.
equation = 'y = -12x sign 10.74'
x = float(input('Enter x: '))
split_result = equation.split()
print(split_result)
split_result[3] = input('Enter +, -, * or /: ')
number_with_x = float(split_result[2].replace('x', '')) * x
print(number_with_x)
if split_result[3] == '+':
    y = number_with_x + float(split_result[4])
    print(y)
if split_result[3] == '-':
    y = number_with_x - float(split_result[4])
    print(y)
if split_result[3] == '*':
    y = number_with_x * float(split_result[4])
    print(y)
if split_result[3] == '/':
    y = number_with_x / float(split_result[4])
    print(y)

