# 4 + 3  # + это метод __add__

class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.modules = []

    def __add__(self, other):
        self.modules.append(other)

    def add(self, module):
        self.modules.append(module)


car = Car('KIA CEED', 'BROWN')

module1 = 'кондей'
module2 = 'массаж кресел'
module3 = 'подогрев руля'
car + module1  # или - car.__add__(module)
car.__add__(module1)
car.__add__(module2)
car.add(module3)

print(f'The car is {car.name}, color {car.color}. This car has options: {", ".join(car.modules)}')
print('\n', '\n', '\n')


# задача LogReader - считать все файлы как будто это один файл (log1.txt, log2.txt)
import os


class LogReader:
    def __init__(self):
        self.files = []
        self.i = 0  # счетчик файлов
        # print(os.listdir('D:\\Python projects\\обучение\\упражнения'))

        for file in os.listdir('/\\'):  # получаем список всех файлов и папок
            file_name = 'D:\\Python projects\\обучение\\упражнения\\' + file
            if os.path.isdir(file_name):  # если сейчас итерируемое это папка, то continue
                continue
            if file_name.endswith('txt'):
                file_descriptor = open(file_name, encoding='UTF-8')  # открытый файл в оперативке
                self.files.append(file_descriptor)

# __del__ это деструктор.
    # метод  __del__ вызывается при закрытии объекта. он обратен методу __init__. Метод __del__ создаем, чтобы
    # освободить место в оперативке. Он будет вызываться сам при удалении объекта, а удаление происходит при удалении
    # из памяти, когда больше нет ссылок в рамках нашего кода
    def __del__(self):  # пробегаемся по каждому файлу и в каждом файле вызываем метод close()
        for file_descriptor in self.files:
            file_descriptor.close()
        print('Файлы закрыты')

# метод __iter__ вызывается на самом первом этапе, когда обрабатывается вход в цикл for. Метод спрашивает у объекта
    # итерируемый ли он. Если да, то запрашивается элемент с помощью метода __next__
    def __iter__(self):
        print('yes, iter')
        return self

    def __next__(self):
        while self.i < len(self.files):  # пока счетчик меньше длины списка files
            for line in self.files[self.i]:  # обращаемся к линиям файла с индексом i в списке files
                return line
            self.i += 1
        raise StopIteration  # выбрасываем исключение


log_reader = LogReader()

# for запрашивает объект итератор
# задача итератора вернуть объект, у которого есть метод __next__
for i in log_reader:
    print(i.strip())
    # print(i)


print('\n', '\n', '\n')


# ДЕКОРАТОРЫ
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self._age = age
        self.sex = sex

# допустим сперва нужно проверить возраст по каким-то параметрам. И в зависимости от этого вернуть какой-то другой
    # возраст. Для этого можно создать новый метод, например, get_age(). Но для этого придется в весь код вносить
    # правки. Но можно использовать декоратор. При этом в print() вызываем, атрибут human.age, но идет обращение к
    # методу def age() с декоратором.
    @property
    def age(self):
        # много кода
        return self._age

    @property
    def func(self):
        pass


# много какого-то кода
human = Human('Ivan', 3, 'M')
print(human.name, human.age, human.sex)


# еще пример:
class Person(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return " " .join([self.first_name, self.last_name])

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name


person = Person("Andrey", "Po")
print(person.full_name)  # "Andrey Po"
print(person.get_full_name())  # "Andrey Po"


print('\n', '\n', '\n')


# СТАТИЧЕКИЕ МЕТОДЫ
class DataBaseConnection:

    @staticmethod
    def connect():
        print('connecting')

    def select(self):
        print('selecting')

    def insert(self):
        print('inserting')


DataBaseConnection.connect()
db = DataBaseConnection()
db.insert()
db.connect()


print('\n', '\n', '\n')


# РАСШИРЕНИЕ ВСТРОЕННЫХ ТИПОВ
class MyDict(dict):
    def __setitem__(self, key, value):
        pass


my = MyDict()
my['qwert'] = 12345
print(my)


class MyDict1(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        print(f'Добавил в словарь ключ: {key}, значение: {value}')

    def __getitem__(self, k):
        print(f'Пытаюсь получить значение по ключу: {k}')
        return super().__getitem__(k)


my1 = MyDict1()
my1['zxc'] = 456
my1['asd'] = 789
print(my1)
print(my1['zxc'])

