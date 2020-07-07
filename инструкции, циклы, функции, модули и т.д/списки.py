# g = [['.', '.', '.', '.', '.', '.'],
#      ['.', '0', '0', '.', '.', '.'],
#      ['0', '0', '0', '0', '.', '.'],
#      ['0', '0', '0', '0', '0', '.'],
#      ['.', '0', '0', '0', '0', '0'],
#      ['0', '0', '0', '0', '0', '.'],
#      ['0', '0', '0', '0', '.', '.'],
#      ['.', '0', '0', '.', '.', '.'],
#      ['.', '.', '.', '.', '.', '.']]
# print(len(g[4]))
# print(len(g))
# for i in range(len(g[4])):
#     for j in range(len(g)):
#         print(g[j][i], end='')
#     print()

# spam = ['cat', 'bat', 'rat', 'elephant']
# spam[1] = 'dog'
# print(spam)
# print(spam[0])
# print(spam[1])
# print('Hello ' + spam[0])
#
# spam1 = [['cat', 'bat'], [10, 20, 30]]
# print(spam1[1][2])
# print(spam1[-1][0], spam1[-1][-3])
#
# print(spam[1:3])
# print(spam[0:-1])
#
# print(len(spam))
# print(len(str(spam)))
#
# spam[1] = 'ABC'
# print(spam)
# spam[2] = spam[1]
# print(spam)
# spam[-1] = 12345
# print(spam)
#
# print('*' * 30)
#
# print(spam)
# print(spam1)
# print(spam + spam1)
#
# del spam1[0]
# print(spam + spam1)
#
#
# names = []
# while True:
#     print('Введите имя номер ' + str(len(names) + 1) + ' (Или нажмите ентер для продолжения): ')
#     name = input()
#     if name == '':
#         break
#     names = names + [name]
# print('The names are: ')
# for name in names:
#     print(name)
# spam = ['A', 'B', 5]
# print(spam + names)
#
#
# print('cat' in ['cat', 'dog', 'rat'])
# print('bat' in ['cat', 'dog', 'rat'])
#
# print('=' * 30)
# mycars = ['kia', 'lada', 'bmw']
# print('Enter a car name: ', end='')
# while True:
#     name = input()
#     if name not in mycars:
#         print('I don\'t have a car named ' + name + ' Try again: ', end='')
#     else:
#         print('Yes! ' + name + ' is my car!')
#         break
#
# spam = ['cat', 'bat', 'rat', 'elephant']
# spam1 = tuple(spam)
# print(spam1)
# spam1 = list(spam)
# print(spam1)
# print(list('hello'))

# spam = [2, 4, 6, 8, 10]
# spam[2] = 'hello'
# print(spam)
#
# spam = ['a', 'b', 'c', 'd']
# print(spam[int(int('3' * 2) / 11)])
# print(spam[-1])
# print(spam[:2])
#
# bacon = [3.14, 'cat', 11, 'cat', True]
# print(bacon.index('cat'))
# bacon.append(99)
# print(bacon)
# bacon.remove('cat')
# print(bacon)
# del bacon[2]
# print(bacon)
# bacon.insert(2, 'dog')
# print(bacon)
# print(bacon[3])
# print(tuple(bacon))
# print(tuple(spam))
# print(list(spam))

# name = 'Alex'
# humans = ['Ivan', 'Jo', 'Petr', 'Serg', name]
# print(humans)
# humans[1] = 'Nat'
# print(humans)
# humans[2:4] = ['Goga', 'Shu', 'Den']
# print(humans)
# humans[3] = ['Lo', 'Kur']
# print(humans)
# humans.append(10)
# print(humans)
# humans.insert(1, 'PPP')
# print(humans)
# print(humans.index(name))
# humans.remove('PPP')
# print(humans)
# del humans[3:5]
# print(humans)
# deleted_element = humans.pop(1)
# print(humans)
# print(deleted_element)
# print('Alex' in humans)
# print('Sasha' in humans)

human = ['alex', 'olga', 'ivan']
x = 0
while x < len(human):
    print(human[x])
    x = x + 1

for i in human:
    print(i)

a = []
for i in range(1, 11):
    print(i)
    a.append(i)
print(a)

for i in range(len(human)):
    print('number', i, human[i])


strings = ["H", "e", "l", "l", "o"]
string = ''.join(strings)
print(string)


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
a_str = ' '.join(str(i) for i in a)
print(a_str)
print(' '.join(map(str, a)))


numbers = ["77", "145", "987", "2095", "6", "371", "4999", "81"]
numbers.sort()
print(numbers)