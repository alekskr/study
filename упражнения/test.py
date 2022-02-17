from functools import reduce


def persistence(n):
    if len(str(n)) == 1:
        return 0
    else:
        a = list(map(int, str(n)))
        print(a)
        while len(a) > 1:
            b = a[0] * a[1]
            a.pop(0)
            a[0] = b
        return a[0]


print(persistence(999))
#
#
# l = [1, 2, 3]
# print(reduce(lambda x, y: x*y, l))
#
# print('999'.split())
#
# ff = list(map(int, '999'))
# print(ff)

