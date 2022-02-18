# передача аргумента по ссылке и по значению
# x = [1, 2, 3]
#
#
# def test(some_list):
#     some_list.append(100)
#
#
# test(x)
# print(x)


# a = [1, 2, 3, 4, 5, 6]
# for number in a.copy():
#     print(number)
#     a.remove(number)
# print(a)


# a = [1, 2, 3, 4, 5, 6]
# b = a.copy()
# b.append(1000)
# print(a)
# print(b)


# import copy
#
# a = [1, 2, 3, [100]]
# b = copy.deepcopy(a)
# b[3].append(200)
# print(a)
# print(b)


# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
# # Красиво вывести на экран:
# # print("matrix = ", matrix)
#
# print("matrix = ")
# for line in matrix:
#     print(line)
#
# i = 0
# while len(matrix) > i:
#     line = matrix[i]
#     j = 0
#     while len(line) > j:
#         print("matrix[{}][{}] = {}".format(i, j, matrix[i][j]))
#         j += 1
#     i += 1
#
# print("*************FOR IN ***************")
# # Вывести на экран пронумерованно номер строки и элемента
# for i, line in enumerate(matrix):
#     for j, el in enumerate(line):
#         print("matrix[{}][{}] = {}".format(i, j, matrix[i][j]))
#
# # # Пример транспонирования (поворота) матрицы
# print("rotate_matrix = ", list(map(list, zip(*matrix))))


# print(0 or 5)
# print(0 and 5)
# print(5 and 0)


# name = input('Name: ')
# print(name or 'noname')


# age = int(input('Age: '))
# print('Welcome' if age >= 18 else 'No Access')


# def admin():
#     print("I'm admin")
#
#
# login = input('Your login: ')
# admin() if login == 'admin' else print("Hello, user")


# x = [1, 2, 3]
# y = x
# print(x is y)

# a = 10
# b = 10
# print(a is b)
# a += 1
# print(a is b)
# b += 1
# print(a is b)

# a = 300
# b = 300
# print(a is b)


# values = (1, 2, 3, 4, 5, 6)
# keys = 'qwerty'
# my_dict = {key: value * 2 for key, value in zip(keys, values)}
# print(my_dict)
#
# if len(values) == len(keys):
#     my_dict = {key: value * 2 for key, value in zip(keys, values)}
#     print(my_dict)


# a = [1, 2]
# try:
#     b = a[5]
# except IndexError:
#     print('Неверный индекс')
#
# a = [1, 2]
# try:
#    b = a[5]
# except Exception as e:
#    print(e.__class__)
#
#
# try:
#     age = int(input('Введите возраст: '))
# except ValueError:
#     print('Вы должны были ввести число')
# except ZeroDivisionError:
#     print('Деление на ноль')


# import re
# pattern = '[a-zA-Z0-9-_]+@[a-z]+\.(ru|com)'
# email = 'alex@mail.ru'
# print(re.match(pattern, email))
#
# pattern = '([a-zA-Z0-9-_]+@[a-z]+\.(ru|com))'
# email = 'send email to alex@mail.ru'
# print(re.search(pattern, email))
# print(re.search(pattern, email).group(1))
# print(re.match(pattern, email))

# pattern = '([a-zA-Z0-9-_]+@[a-z]+\.(ru|com))'
# text = 'dfg 123@gmail.com dfvlk fi59 9430@ !3kf alex@mail.ru'
# print(re.findall(pattern, text))

# list1 = [1, 2, 4, 0]
# result = [i ** 2 for i in list1.copy()]
# print(result)
#
#
# fruit1 = ['apple', 'orange', 'lemon', 'banana', 'apricot']
# fruit2 = ['ananas', 'lemon', 'peach', 'apple']
# fruit3 = []
# result = [i for i in fruit1 if i in fruit2]
# print(result)


# import re
# name = input()
# surname = input()
# email = input()
# pattern = '[a-z0-9_]+@[a-z0-9]+\.(ru|org|com)'
# if not name.istitle() or not surname.istitle():
#     print('неверно задано name/surname')
# if re.match(pattern, email) is None or pattern != email[:]:
#     print('неверная почта')
#
# some_str = '''fio mlfg... 543mg...fergew ...
# wer,ewr .. wf. frf...'''
# pattern = '\.{2,}'
# if re.search(pattern,some_str) is None:
#     print('В строке нет ...')
# else:
#     print('В строке есть ...')


def card():
    while True:
        card_number = input('card number: ')
        if not card_number.isdecimal() or len(card_number) != 5:
            print('Неверный номер карты, введите еще раз.')
            continue
        else:
            pin()
        break


def pin():
    while True:
        pin_number = input('Введите pin: ')
        if not pin_number.isdecimal() or len(pin_number) != 4:
            print('Неверный pin, введите еще раз.')
            continue
        else:
            print()
            menu()
        break


def menu():
    print('Меню '.center(20, '-'))
    print(
        '''1. Снять наличные
2. Внести наличные
3. Перевод на другую карту
4. Баланс
5. Забрать карту''')
    step = int(input('Выберите действие: '))
    if step == 4:
        balance()
    if step == 5:
        print('Goodbye')


def balance():
    print('\nВаш баланс составляет ...\n')
    menu()


print('Вставьте карту')
card()
