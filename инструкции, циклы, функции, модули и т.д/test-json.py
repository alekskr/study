import json
import pandas as pd


def intro():
    while True:
        print('''
   =База данных автомобилей=
1 - Список всех моделей
2 - Добавить новую модель
0 - Выход''')

        print('Введите:', end=' ')
        menu_item = int(input())
        if menu_item == 1:
            print_all_cars()
        elif menu_item == 2:
            create_new_car()
        elif menu_item == 0:
            exit()
        else:
            print('\nНеверный ввод.')


def create_new_car():
    """занести в базу новый автомобиль"""
    print('=Введите данные автомобиля=')
    auto = input('auto: ').capitalize()
    model = input('model: ')
    transmission = input('transmission: ').lower()
    engine = input('Бензин/Дизель/Электро: ')
    if engine == 'электро'.lower():
        engine_volume = '-'
    else:
        engine_volume = input('Объем двигателя: ')
    new_car = NewCar(auto, model, transmission, engine, engine_volume)
    print(new_car.model)


def print_all_cars():
    """вывести список марок"""
    with open('auto.json', 'r') as json_file:
        cars = json.load(json_file)
        print('=Список всех автомобилей=')
        # print(cars)

        for i in cars:
            try:
                print(i['auto'], i['model'], i['transmission'], i['engine_volume'], i['engine'])
            except KeyError:
                print(i['auto'], i['model'], i['transmission'], i['engine_volume'], '')


class NewCar:
    def __init__(self, brand, model, transmission, engine, engine_volume):
        self.brand = brand
        self.model = model
        self.transmission = transmission
        self.engine = engine
        self.engine_volume = engine_volume
        self.write_new_data_to_file()

    def write_new_data_to_file(self):
        new_data = {
            'auto': self.brand,
            'model': self.model,
            'transmission': self.transmission,
            'engine': self.engine,
            'engine_volume': self.engine_volume
        }
        with open('auto.json', 'r') as json_file:
            json_data = json.load(json_file)
            json_data.append(new_data)

        with open('auto.json', 'w') as json_file:
            json.dump(json_data, json_file, indent=4)


if __name__ == '__main__':
    intro()
