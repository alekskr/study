# round()
print(round(2.65, 1))
print(round(2.75, 1))
print(round(1.98754, 3))
print()


def say_hello(name):
    print('Hello', name)


say_hello('Ivan')
print()


def average(numbers):
    count = len(numbers)
    all_sum = sum(numbers)
    return all_sum / count


average_number = average([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(average_number)
print()


# необязательный аргумент
def my_func(name, surname='Guest'):
    print(name, surname)


my_func('Sasha')
print()


# большое количество аргументов
def func(name, *args):
    print(name, args)
    print(args)
    print(args[2])


func('Sasha', 10, 20, 30)
print()


def func2(name, age, surname):
    print(name, surname, age)


func2('Ivan', surname='Ivanov', age=50)
print()


# передача в функцию по ключу и значению
def func3(name, **kwargs):
    print(name, kwargs)


func3('Ivan', surname='Ivanov', age=20, flat=123)


def func4(**kwargs):
    print(kwargs)


func4(name='Ivan', surname='Ivanov', age=20, flat=123)
print()

# pow() возведение в степень
x = 10
print(pow(x, 2))
print()

# zip()
names = ['Ivan', 'Oleg', 'Sosed', 'Bob']
ages = (35, 45, 80)

print(list(zip(names, ages)))
print(dict(zip(names, ages)))

# создаются строки:
for name, age in zip(names, ages):
    print(name, age)

# создаются кортежи:
for n in zip(names, ages):
    print(n)
print()
import itertools

# Если требуется учесть все значения из самой длинной переменной,
# то следует использовать функцию zip_longest из модуля itertools:
for i in itertools.zip_longest(names, ages):
    print(i)
print()
# если элемента не хватает, то по-умолчанию подставляется объект None. Можно указать свой вариант заполнения:
for i in itertools.zip_longest(names, ages, fillvalue='GG'):
    print(i)


# возвести значения из списка data в степень 3
def my_pow(x):
    return x ** 3


data = [-2, -10, 6, 15]
result = []

for i in data:
    result.append(my_pow(i))
print(result)
# тоже самое можно сделать с помощью функции map():
result_1 = list(map(my_pow, data))
print(result_1)
print()

# есть список чисел в строковом типе данных, нужно превратить их в целое число:
old_list = ['1', '2', '3', '4', '5', '6', '7']
new_list = []
for item in old_list:
    new_list.append(int(item))
print(new_list)
# То же самое можно сделать, применив функцию map():
old_list = ['1', '2', '3', '4', '5', '6', '7']
new_list = list(map(int, old_list))
print(new_list)
print()

# filter()
data = [-2, -10, 6, 15]


def my_filter(x):
    return x > 0


result_2 = list(filter(my_filter, data))
print(result_2)
print()

# lambda
data = [-2, -10, 6, 15]

result = list(map(lambda x: x ** 2, data))
print(result)
result = list(filter(lambda x: x > 0, data))
print(result)
