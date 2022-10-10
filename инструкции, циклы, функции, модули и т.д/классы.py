"""классы"""


# class Movie:
#     """movie"""
#
#     def __init__(self, title, director, year):
#         self.title = title
#         self.director = director
#         self.year = year
#
#
# titanic = Movie('Titanic', 'James Cameron', 1997)
# star_wars = Movie('Star Wars', 'George Lucas', 1977)
# fight_club = Movie('Fight Club', 'David Fincher', 1990)

###
# class RightTriangle:
#     """правильный треугольник"""
#
#     def __init__(self, hyp, leg_1, leg_2):
#         self.c = hyp
#         self.a = leg_1
#         self.b = leg_2
#         self.s = 1 / 2 * leg_1 * leg_2
#
#
# # triangle from the input
# input_c, input_a, input_b = [int(x) for x in input().split()]
# if input_c ** 2 == input_a ** 2 + input_b ** 2:
#     my_triangle = RightTriangle(input_c, input_a, input_b)
#     print(my_triangle.s)
# else:
#     print('Not right')

# John Smith (b. 1989) would look like JSmith1989
###
# class Student:
#
#     def __init__(self, name, last_name, birth_year):
#         self.name = name
#         self.last_name = last_name
#         self.birth_year = birth_year
#         self.id = name[0] + last_name + birth_year
#         # calculate the id here
#
#
# print(Student(input().capitalize(), input().capitalize(), input()).id)


###
# class Store:
#     def __init__(self, name, category):
#         self.name = name
#         self.category = category
#
# shop = Store("GAP", "clothes")
# print(shop.name, shop.category)


###
# class Point:
#     """1"""
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def dist(self, arg):
#         """2"""
#         return ((self.x - arg.x) ** 2 + (self.y - arg.y) ** 2) ** 0.5
#
#
# p1 = Point(1.5, 1)
# p2 = Point(1.5, 2)
# print(p1.dist(p2))


###
# import math
#
#
# class Hexagon:
#     """Hex"""
#     def __init__(self, side_length):
#         self.side_length = side_length
#
#     def get_area(self):
#         """
# area method
#         :return:
#         """
#         return round((3 * math.sqrt(3) * (self.side_length ** 2)) / 2, 3)
#
#
# a = Hexagon(5.4)
# print(a.get_area())
###

# class Chevrolet:
#     """Chevy"""
#     all_chevy = []
#
#     def __init__(self, name, year, info):
#         self.name = name
#         self.year = year
#         self.info = info
#         Chevrolet.all_chevy.append(self)
#
#
# belair = Chevrolet('Bel Air', '1950 - 1981',
#                    'Mid-level full-size car for the 1950–1975 in US market and 1950–1981 for Canadian market')
# elcamino = Chevrolet('El Camino', '1959-1987',
#                      'Coupé utility/pickup vehicle that was introduced in the 1959 model year '
#                      'in response to the success of the Ranchero pickup')
#
# for car in Chevrolet.all_chevy:
#     print('Model: {}, \nYears of production: {}, \nInfo: {}\n'.format(car.name, car.year, car.info))
#
#
# ###
# CINEMA_RATINGS = {
#     "The Dark Knight": 8.2,
#     "The Shawshank Redemption": 8.3,
#     "Pulp Fiction": 8.1,
# }
#
# for rating in CINEMA_RATINGS.values():
#     print(rating)


# class Sphere:
#     PI = 3.1415
#
#     def __init__(self, radius, volume):
#         self.radius = radius
#         self.volume = volume


# class Pet:
#     kind = "mammal"
#     n_pets = 0  # number of pets
#     pet_names = []  # list of names of all pets
#
#     def __init__(self, spec, name):
#         self.spec = spec
#         self.name = name
#         self.legs = 4
#
#
# tom = Pet('cat', 'Tom')
# tom.pet_names.append(tom.name)
# print(Pet.pet_names)


# class PiggyBank:
#     def __init__(self, dollars, cents):
#         self.dollars = dollars
#         self.cents = cents
#
#     def add_money(self, deposit_dollars, deposit_cents):
#         self.dollars += deposit_dollars
#         self.cents += deposit_cents
#         while self.cents > 99:
#             self.dollars += 1
#             self.cents = self.cents - 100
#         # print(self.dollars, self.cents)
#
#
# deposit = PiggyBank(1, 1)
# deposit.add_money(0, 50)
# deposit.add_money(0, 99)
# deposit.add_money(0, 88)
# deposit.add_money(500, 500)
# print(deposit.dollars, deposit.cents)

class Coffee:
    roast = "medium"
    kind = "beans"

    def __init__(self, sort, variety):
        self.sort = sort
        self.variety = variety
        self.caffeine = '0'
        self.cup = sort + variety + self.caffeine + Coffee.roast + Coffee.kind


newcup = Coffee(input(), input())
print(newcup.cup)