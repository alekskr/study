# import pprint
# fruit = {'name': 'carrot', 'quantity': 12}
# fruit.setdefault('color', 'orange')
# print(fruit)
# fruit.setdefault('color', 'red')
# print(fruit)
#
# message = 'Очередность выполнения операторов'
# count = {}
# for i in message:
#     count.setdefault(i, 0)
#     count[i] = count[i] + 1
# print(count)
# pprint.pprint(count)
#
# mess = 'abc'
# a = []
# for i in mess:
#     a = a + list(i)
# print(a)
#
# mess1 = ['a', 'b', 'c']
# for i in mess1:
#     print(i)
#
# bdays = {'Ben': '1 mar', 'Dan': '2 dec', 'Fil': '4 apr'}
# while True:
#     name = input('Enter name: ')
#     if name == '':
#         break
#     if name in bdays:
#         print(f'{bdays[name]} is bday of {name}')
#         break
#     else:
#         print(f'This name isn\'t in this list')
# print('End!')
#
#
# mess = 'abca nd'
# a = {}
# for i in mess:
#     a.setdefault(i, 0)
#     a[i] = a[i] + 1
# print(a)

# human = {'name': 'Илья', 'age': 43, 'money': 39.1}
# human['data'] = [1, 2]
# print(human['name'])
# human['input'] = input('enter value: ')
# print(human)
#
# #  метод get()
# print(human.get('qwe'))
# print(human.get('name'))

#  метод pop()
# print(human.pop('age'))
# print(human)
# print(human.popitem())
# print(human)

# Вложенные словари и списки
# all_guests = {'Alice': {'apples': 5, 'oranges': 3}, 'Bob': {'burgers': 8, 'apples': 4},
#               'John': {'beers': 3, 'orange': 1}}
#
#
# def total_things(guests, thing):
#     num_brought = 0
#     for k, v in guests.items():
#         num_brought = num_brought + v.get(thing, 0)
#     return num_brought
#
#
# print('Принесенные предметы:')
# print('Apples:', total_things(all_guests, 'apples'))
# print('Oranges:', total_things(all_guests, 'oranges'))
# print('Burgers:', total_things(all_guests, 'burgers'))
# print('Beers:', total_things(all_guests, 'beers'))
# print('Cups:', total_things(all_guests, 'cups'))
# print('Bananas:', total_things(all_guests, 'bananas'))
#
# spam = {'name': 'Pooka', 'age': 5}
# spam.setdefault('color', 'black')
# print(spam)

###
first_family = {"wife": "Janet", "wife's mother": "Katie", "wife's father": "George"}
second_family = {"husband": "Leon", "husband's mother": "Eva", "husband's father": "Gaspard",
                 "husband's sister": "Isabelle"}
big_family = {}
big_family.update(first_family)
big_family.update(second_family)
print(len(first_family))

import json
# with open('qweqwrqrq.json', 'r') as json_file:
#     ddddd = json.load(json_file)
#
# print(ddddd)

with open('qweqwrqrq.json', 'r') as json_file:
    users_dict = json.load(json_file)

print(len(users_dict['users']))
for v in users_dict.values():
    print(len(v))
print(len(users_dict))


# squares = {1: 1, 3: 9, 5: 25, 6: 36, 8: 64, 10: 100, 11: 121, 15: 225}
# x = int(input())
# for k, v in squares.items():
#     if x == k:
#         squares.pop(k)
#         print(v)
#         break
# else:
#     print('There is no such key')
# print(squares)