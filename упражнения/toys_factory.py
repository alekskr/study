class Toys:
    def __init__(self, name, color):
        self.name = name
        self.color = color


class Mult(Toys):
    def __init__(self, name, color):
        super().__init__(name, color)
        self.toy_type = 'mult'
        print(f'Игрушка {self.name} готова. Тип {self.toy_type}. Цвет {self.color}')


class Animal(Toys):
    def __init__(self, name, color):
        super().__init__(name, color)
        self.toy_type = 'animal'
        print(f'Игрушка {self.name} готова. Тип {self.toy_type}. Цвет {self.color}')


class Toxic(Toys):
    def __init__(self, name, color):
        super().__init__(name, color)
        self.toy_type = 'toxic'
        print(f'Игрушка {self.name} готова. Тип {self.toy_type}. Цвет {self.color}')


class Factory:

    def create_toy(self, name, color, toy_type):
        self.buy_material(name)
        self.make_toy(name)
        self.paint(name, color)
        if toy_type == 'mult':
            return Mult(name, color)
        elif toy_type == 'animal':
            return Animal(name, color)
        elif toy_type == 'toxic':
            return Toxic(name, color)

    def buy_material(self, name):
        print(f'Закупка материала для игрушки - {name}.')

    def make_toy(self, name):
        print(f'Пошыв игрушки - {name}')

    def paint(self, name, color):
        print(f'Окрас игрушки {name} в цвет - {color}')


factory = Factory()
new_toy = factory.create_toy('Cheburashka', 'brown', 'mult')
new_toy2 = factory.create_toy('Reptile', 'green', 'animal')
new_toy3 = factory.create_toy('Ball', 'red', 'toxic')

print(isinstance(new_toy, Mult))
print(isinstance(new_toy2, Toys))
print(isinstance(new_toy3, Toxic))

if isinstance(new_toy3, Toxic):
    print('Опасно!')
else:
    print('Можно играть.')
