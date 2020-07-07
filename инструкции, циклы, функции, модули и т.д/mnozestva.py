# a = 1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 5, 6
# print(a)
# print(list(a))
# print(set(a))
# print(len(set(a)))
#
#
# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a | b)
# print(a == b)
# print(a & b)
# print(a ^ b)


a = [1, 2, 3, 4, 4, 5, 1, 6]
b = [3, 4, 5, 6, 3, 7]

# for i in b:
#     while i in a:
#         a.remove(i)
# print(a)

c = []
for i in a:
    if i % 2 == 0:
        j = i / 4
        c.append(j)
    else:
        k = i * 2
        c.append(k)
print(c)
