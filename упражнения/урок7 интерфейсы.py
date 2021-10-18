# 4 + 3  # + это метод __add__

class Car:
    def __init__(self):
        self.modules = []

    def __add__(self, other):
        self.modules.append(other)

    def add(self, mod):
        self.modules.append(mod)


car = Car()

module1 = 'кондей'
module2 = 'массаж кресел'
module3 = 'подогрев руля'
car + module1  # или - car.__add__(module)
car.__add__(module1)
car.__add__(module2)
car.add(module3)
print(car.modules)


# задача LogReader - считать все файлы как будто это один файл (log1.txt, log2.txt)
import os


class LogReader:
    def __init__(self):
        self.files = []

        for file in os.listdir():  # получаем список всех файлов и папок
            if os.path.isdir(file):  # если сейчас итерируемое папка, то continue
                continue
            if file.startswith('log'):
                print(file)
                file_descriptor = open(file, encoding='UTF-8')  # открытый файл в оперативке
                self.files.append(file_descriptor)

        self.i = 0  # счетчик

# метод  __del__ вызывается при закрытии объекта. он обратен методу __init__. Метод __del__ создае, чтобы освободить
    # место в оперативке. Он будет вызываться сам при удалении объекта, а удаление происходит при удалении из памяти,
    # когда больше нет ссылок в рамках нашего кода
    def __del__(self):  # пробегаемся по каждому файлу и в каждом файле вызываем метод close()
        for file_descriptor in self.files:
            file_descriptor.close()
        print('Файлы закрыты')

    def __iter__(self):
        print('yes, iter')
        return self

    def __next__(self):
        while self.i < len(self.files):  # пока счетчик меньше длины списка files
            for line in self.files[self.i]:  # обращаемся к линиям файла с индексом i в списке files
                return line
                # print(line)
            self.i += 1
        raise StopIteration  # выбрасываем исключение


log_reader = LogReader()

for i in log_reader:
    print(i.strip())
