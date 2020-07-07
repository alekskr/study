import random


def person(name):
    print('Hello ' + name)


person('Alice')
person('Bob')


#


def amount(number):
    print('сумма 1 + ' + str(number) + ' = ' + str(1 + number))


r = random.randint(1, 9)
e = random.randint(1, 9)
amount(r)
amount(e)
if r == e:
    print('Bingo!!!')

print('***')
secret = random.randint(1, 20)
print('Enter your number: ', end='')
for guess in range(1, 7):
    numb = int(input())
    if numb == secret:
        print('Yeahhh!! Amount of your attempts is ' + str(guess))
        break
    elif numb > secret and guess <= 5:
        print('Your number is bigger than secret, try again, you have ' + str(6 - guess) + ' attepmts: ', end='')
        # continue
    elif numb < secret and guess <= 5:
        print('Your number is smaller than secret, try again, you have ' + str(6 - guess) + ' attepmts: ', end='')
        # continue
    else:  # guess == 6:
        print('You\'re wrong!! Your attempts is over!!')
        break
print('Goodbye!')
