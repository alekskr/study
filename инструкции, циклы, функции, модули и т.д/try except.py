import random


# 1
def spam(devide):
    try:
        return 42 / devide
    except ZeroDivisionError:
        print('Error, ', end='')


print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

# 2
print('Ваше число: ', end='')
r = input()
while True:
    try:
        print(int(r))
        break
    except ValueError:
        print(float(r))
        break


# 3
def col(num):
    num = int(num)
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1
        print(num)


print('Введите целое число: ', end='')

while True:
    r = input()
    try:
        print(int(r))
        break
    except ValueError:
        print('Ошибка, введите целое число: ', end='')  # print(float(r))
        continue

col(r)

print('*' * 30)

m = random.randint(2, 15)
print('Масса m = ' + str(m) + ' кг')
col(m)

print('*' * 30)

# print('Введите массу, кг')
# m = input()
print('F = ' + str(float(m) * 9.8) + ' H')
