import random


def answer(number):
    if number == 1:
        return 'It\'s certain'
    elif number == 2:
        return 'It\'s decidely so'
    elif number == 3:
        return 'Yes'
    elif number == 4:
        return 'Reply hazy, try again'
    elif number == 5:
        return 'Ask again later'
    elif number == 6:
        return 'Concentrate and ask again'
    elif number == 7:
        return 'My reply is no'
    elif number == 8:
        return 'Outlook not so good'
    elif number == 9:
        return 'Very doubtful'


# print('Введите число: ', end='')
# r = int(input())  # ввод цифр вручную
# print(answer(random.randint(1, 9)))  # можно использовать такую строку
r = random.randint(1, 9)  # ввод цифр модулем случайных чисел
print('*' * 30)
print(f'{r} - {answer(r)}')
print('*' * 30)

messages = ['It\'s certain', 'It\'s decidely so', 'Yes',
            'Reply hazy, try again', 'Ask again later',
            'Concentrate and ask again', 'My reply is no',
            'Outlook not so good', 'Very doubtful']
r1 = random.randint(0, len(messages) - 1)
print(len(messages))
print(f'{r1 + 1} - {messages[r1]}')
