n = 10
row = [1]
# print([sum(x) for x in list(zip([0] + row, row + [0]))])
# for x in list(zip([0] + row, row + [0])):
#     print(sum(list(x)))
for i in range(n):
    print(row)
    row = [left + right for left, right in zip([0] + row, row + [0])]
    # row = [sum(x) for x in list(zip([0] + row, row + [0]))]


a = 'asasas'

if a == a[::-1]:
    print('y')
else:
    print('n')


def palindrom(x):
    return x == "".join(reversed(x))


print(palindrom('abba'))
print(''.join(a))
