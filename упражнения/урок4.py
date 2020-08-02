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


import copy

a = [1, 2, 3, [100]]
b = copy.deepcopy(a)
b[3].append(200)
print(a)
print(b)
