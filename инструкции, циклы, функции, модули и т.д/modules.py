import math
import string
import random

print(math.factorial(5))  # prints the value of 5!

print(math.log(10))  # prints the natural logarithm of 10

print(math.pi)  # math also contains several constants
print(math.e)

# from string import digits
print(string.digits)
# print(digits)

# input_string = input('Enter: ')
# print(string.capwords(input_string))

# x = int(input())
# e = math.e
x = -57
print(math.expm1(x))

# x = 36
# random.seed(x)
print(random.randint(-100, 100))

print(string.ascii_uppercase)
print(string.ascii_letters)

x = -54.56
y = 11.22
print(math.copysign(x, y))

random.seed(3)
print(random.random())


print(random.sample(range(100), 10))
print(random.choice('Voldemort'))

random.seed(-65)
print(random.betavariate(alpha=0.9, beta=0.1))
print(random.choice('Voldemort'))
print(random.uniform(0, 1))

# sentence = input().split()
# random.seed(3)
# random.shuffle(sentence)
# print(' '.join(sentence))

name = 'ПеТрОв ИвАнОв'
print(name.swapcase())
