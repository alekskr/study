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


people = {'Jackie': 176, 'Wilson': 185, 'Saersha': 165, 'Roman': 185, 'Abram': 169}


def tallest_people(**kwargs):
    names = []
    max_value = max(kwargs.values())
    print(max_value)
    for k, v in kwargs.items():
        if v == max_value:
            names.append(k)
            names.sort()
    for name in names:
        print('{} : {}'.format(name, max_value))


# print(tallest_people(Jackie=176, Wilson=185, Saersha=165, Roman=185, Abram=169))
tallest_people(Jackie=176, Wilson=185, Saersha=165, Roman=185, Abram=169)
