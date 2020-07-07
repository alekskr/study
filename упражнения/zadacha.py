

def func(spam):
    for i in range(len(spam)):
        if i == len(spam) - 1:
            s = ' and ' + str(spam[i])
        elif i == len(spam) - 2:
            s = str(spam[i])
        else:
            s = str(spam[i]) + ', '
        print(s, end='')
    print()


words = ['back', 'hour', 'five', 'black', 'five', 'hour']
words3 = [1, 5, 2, 3, 1, 4, 5]
func(words)
func(words3)
######################


def dat(date1):
    for i in range(len(date1)):
        if i == len(date1) - 1:
            s = str(date1[i])
        else:
            s = str(date1[i]) + '.'
        print(s, end='')
    print()


month2020_30 = [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
month2020_31 = [1, 3, 5, 7, 8, 10, 12]
print('введите число ', end='')
d = int(input())
if d in range(1, 31):
    print('введите месяц ', end='')
    while True:
        m = int(input())
        date = [d, m, 2020]  # вызов функции
        if m in month2020_30:
            dat(date)  # можно вызвать функцию
            print(str(d) + '.' + str(m) + '.' + str(2020))  # а можно просто напечатать результат
            break
        elif m == 2 and d in range(1, 30):
            dat(date)
            break
        else:
            print('wrong number of month, try again: ', end='')
            continue
elif d == 31:
    print('введите месяц ', end='')
    while True:
        m = int(input())
        date = [d, m, 2020]
        if m in month2020_31:
            dat(date)
            break
        else:
            print('wrong number of month, try again: ', end='')
            continue

# print('введите год ', end='')
# y1 = int(input())
# date1 = [d1, m1, y1]


g = [['.', '.', '.', '.', '.', '.'],
     ['.', '0', '0', '.', '.', '.'],
     ['0', '0', '0', '0', '.', '.'],
     ['0', '0', '0', '0', '0', '.'],
     ['.', '0', '0', '0', '0', '0'],
     ['0', '0', '0', '0', '0', '.'],
     ['0', '0', '0', '0', '.', '.'],
     ['.', '0', '0', '.', '.', '.'],
     ['.', '.', '.', '.', '.', '.']]
