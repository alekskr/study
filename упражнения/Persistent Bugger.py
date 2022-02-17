# Написать функцию, которая принимает положительное число и возвращает одиночное число, равное тому,
# какое количество раз нужно перемножить друг на друга числа, чтобы получилось одно число
# Например:
# 39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
# 999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
# 4 --> 0 (because 4 is already a one-digit number)

import math


def persistence(n):
    # your code
    count = 0
    a = list(map(int, str(n)))
    while len(a) > 1:
        count += 1
        b = math.prod(a)
        a = list(map(int, str(b)))
    return count


print(persistence(999))
