def col(num):
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        # elif num % 2 == 1:
        else:
            num = 3 * num + 1
        print(num)


print('Введите целое число: ', end='')
r = int(float(input()))
col(r)


#  или другой вариант:
def col1(numb):
    numb = int(numb)
    while numb != 1:
        if numb % 2 == 0:
            numb = numb // 2
        else:
            numb = numb * 3 + 1
        print(numb)


print('Введите целое число: ', end='')
while True:
    i = input()
    try:
        print(int(i))
        break
    except ValueError:
        print('Ошибка, введите целое число: ', end="")
        continue
col1(i)

# a = int(float(input()))
# b = int(input())
# print(a + b)
