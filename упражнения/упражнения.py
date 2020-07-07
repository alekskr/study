# import random
# import math
#
#
# # задача1 - написать функцию, которая принимает список
# # в качестве аргумента и возвращает строку, в которой все
# # элементы списка разделены запятой, а перед последним элементом
# # стоит слово and.
print('*** задача 1 ***')


def func(spam):
    for i in range(len(spam)):
        if i == len(spam) - 1:
            s = ' and ' + str(spam[i])
        elif i == len(spam) - 2:
            s = str(spam[i])
        else:
            s = str(spam[i]) + ', '
        print(s, end='')
    print()


words = ['back', 'hour', 'five', 'black', 'five', 'hour']
words2 = [1, 5, 1, 2, 3, 3, 4, 5]
func(words)
func(words2)
print('*** конец задачи 1 ***' + '\n')
#
# # задача 2 - вывести все элементы меньше 5
# # вариант 1
# print('*** задача 2 ***')
# a = [1, 10, 4, 15, -1, 2, 0, 45.3, 2.3]
# for h in range(len(a)):
#     if a[h] < 5:
#         print(a[h], end=' ')
# print()
#
# # вариант 2
#
#
# def func5(elem1):
#     return elem1 < 5
#
#
# print(list(filter(func5, a)))
#
# # вариант 3
# print([elem for elem in a if elem < 5])
# print('*** конец задачи 2 ***' + '\n')
#
#
# # задача 3
# print('*** задача 3 ***')
#
#
# def func(a1, a2, a3):
#     if a3 == '+':
#         return a1 + a2
#     if a3 == '-':
#         return a1 - a2
#     if a3 == '*':
#         return a1 * a2
#     if a3 == '/':
#         return a1 / a2
#     else:
#         print('Неизвестная операция', end=': ')


# b1 = random.randint(1, 10)
# b2 = random.randint(1, 10)
# print('b1 = ' + str(b1) + ', b2 = ' + str(b2))
# b3 = input('Введите +, -, * или /: ')
# print(func(b1, b2, b3))
# print('*** конец задачи 3 ***' + '\n')
#
# # задача 4 - вывести периметр, площадь и диагональ квадрата в кортеж
# print('*** задача 4 ***')
#
#
# def square(a4):
#     return tuple(['периметр = ' + str(a4 * 4),
#                   'площадь = ' + str(a4 ** 2),
#                   'диагональ = ' + str(a4 * math.sqrt(2))])
#
#
# b4 = random.randint(1, 10)
# print('сторона квадрата равна: ' + str(b4))
# print(square(b4))
# print('*** Конец задачи 4 ***' + '\n')
#
#
# # задача 5 времена года
# print('*** задача 5 ***')
#
#
# def seasons():
#     while True:
#         mm = int(input('Введите номер месяца: '))
#         if mm == 12 or mm in range(1, 3):
#             print('месяц №' + str(mm) + ' - ' + 'zima')
#         elif mm in range(3, 6):
#             print('месяц №' + str(mm) + ' - ' + 'vesna')
#         elif mm in range(6, 9):
#             print('месяц №' + str(mm) + ' - ' + 'leto')
#         elif mm in range(9, 12):
#             print('месяц №' + str(mm) + ' - ' + 'osen')
#         else:
#             print('неверное значение, попробуйте снова: ', end='')
#             continue
#         break
#
#
# seasons()
# print('*** Конец задачи 5 ***' + '\n')
#
#
# # # задача 6 банк
# print('*** задача 6 ***')
#
#
# def bank(summa1, years1):
#     for year in range(years1):
#         summa1 = summa1 * 1.1
#     print(summa1)
#
#
# print('Сумма вклада, руб: ', end='')
# summa = float(input())
# print('Срок вклада, лет: ', end='')
# years = int(input())
# bank(summa, years)
# print('*** Конец задачи 6 ***' + '\n')
#
# # задача 7 високосный год
# print('*** задача 7 ***')
#
#
# def is_year_leap(year):
#     if year % 4 == 0:
#         return True
#     else:
#         return False
#
#
# print(is_year_leap(2020))
# print(is_year_leap(1998))
# ddd = random.randint(0, 2020)
# print(str(ddd) + ' - ' + str(is_year_leap(ddd)))
# print('*** Конец задачи 7 ***' + '\n')
#
#
# # задача 8 простые числа
# print('*** задача 8 ***')
#
#
# def is_prime(num):
#     if num == 1:
#         return False
#     for t in range(2, num):
#         if num % t == 0:
#             return False
#     else:
#         return True
#
#
# print('Введите число - ', end='')
# num1 = int(input())
# # num1 = random.randint(0, 100)
# print(num1)
# print(is_prime(num1))
# # is_prime(num1)
# print('*** Конец задачи 8 ***' + '\n')
#
#
# # задача 9 правильная дата
# print('*** задача 9 ***')
#
#
# def date(d, m, y):
#     if 1 <= d <= 31 and 1 <= m <= 12 and 1990 <= y <= 2020:
#         return date1  # True
#     else:
#         return False
#
#
# print('введите число ', end='')
# d1 = int(input())
# print('введите месяц ', end='')
# m1 = int(input())
# print('введите год ', end='')
# y1 = int(input())
# date1 = [d1, m1, y1]
# print(date(d1, m1, y1))
# print('*** Конец задачи 9 ***' + '\n')
#
# # задача 10 - вывести значения больше 5
# print('*** задача 10 ***')
# a = [99, 1, 66, 2, 0, -1.3, 5, 3, 7, 4]
# for p in range(len(a)):
#     if a[p] < 5:
#         print(a[p], end=' ')
# print()
# print('*** Конец задачи 10 ***' + '\n')

# задача 11 - даны два списка. вывести в общий список одинаковые элементы
print('*** задача 11 ***')
a = [1, 2, 3, 4, 5, -1, 6, 7, 8, 9, 10]
b = [3, 99, 1, 0, 5, 2, 2, 15, 23, 4, -1]
c = []
for r in a:
    if r in b:  # здесь r идет в качестве самого элемента, а не индекса
        print(r)
        c.append(r)
print(c)
print('===========')
d = []
for f in range(len(a)):  # здесь f идет как индекс элемента
    if a[f] in b:
        print(f)
        d.append(a[f])
print(d)
print('*** Конец задачи 11 ***' + '\n')

# задача 12. написать функцию, которая принимает список списков строк и отображает его в виде таблицы
# с выравниванием текса по правому краю в каждом столбце.
print('*** задача 12 ***')
table_data = [['apples', 'oranges', 'bananas', 'kiwi'],
              ['elephants', 'dogs', 'cats', 'birds'],
              ['bmw', 'lada', 'kia', 'volkswagen']]


def print_table(table):
    list_table_data = []
    for q in range(len(table)):
        list_table_data = list_table_data + table[q]
    # print(list_table_data)
    offset = len(max(list_table_data, key=len))
    # print(offset)
    for i in range(len(table[0])):
        for j in range(len(table)):
            print(table[j][i].ljust(offset), end=' ')
        print()


print_table(table_data)
print('*** Конец задачи 12 ***' + '\n')

# задача 13. Функция closest_mod_5 принимает ровно один целочисленный аргумент x и
# возвращает наименьшее целое число y, такое что:
# у больше или равно х,
# у делится на 5.


def closest_mod_5(x):
    if x % 5 == 0:
        return x
    return x + (5 - x % 5)


print('*** задача 13 ***' + '\n')

# задача 14. write a function that selects from the given list people older than 30, interested in art, and living
# in Berlin. The function should return their names as a string, separated by a comma and a space, e.g. "Maria, Daniel"
# for the example.


def select_dates(pers_data):
    names = []
    for i in pers_data:
        if i['age'] > 30 and i['city'] == 'Berlin' and 'art' in i['hobbies']:
            names.append(i['name'])
    print(', '.join(names))


potential_dates = [{"name": "Julia", "gender": "female", "age": 29,
                    "hobbies": ["jogging", "music"], "city": "Hamburg"},
                   {"name": "Sasha", "gender": "male", "age": 18,
                    "hobbies": ["rock music", "art"], "city": "Berlin"},
                   {"name": "Maria", "gender": "female", "age": 35,
                    "hobbies": ["art"], "city": "Berlin"},
                   {"name": "Daniel", "gender": "non-conforming", "age": 50,
                    "hobbies": ["boxing", "reading", "art"], "city": "Berlin"},
                   {"name": "John", "gender": "male", "age": 41,
                    "hobbies": ["reading", "alpinism", "museums"], "city": "Munich"}]
select_dates(potential_dates)

print('*** задача 14 ***' + '\n')

