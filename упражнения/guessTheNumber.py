import random

secret = random.randint(1, 20)
print('Попробуйте угадать число от 1 до 20. У вас 6 попыток!')


# for i in range(1, 7):
#     guess = int(input('Ваш вариант: '))
#     if guess < secret and i < 6:
#         print('Предложенное число меньше задуманного. ', end='')
#     elif guess > secret and i < 6:
#         print('Предложенное число больше задуманного. ', end='')
#     else:
#         break
#
# if guess == secret:
#     print(f'Верно! Количество попыток: {i}')
# else:
#     print(f'Нет! Было задумало число: {secret}')

#  или другой вариант:

def answer():
    for i in range(1, 7):
        guess = int(input('Ваш вариант: '))
        if secret > guess and i < 6:
            print('Ваше число меньше задуманного. ', end='')
        elif secret < guess and i < 6:
            print('Ваше число больше задуманного. ', end='')
        elif secret == guess:
            print(f'Верно! Количество попыток: {i}')
            break
        else:
            print(f'Нет! задуманное число: {secret}')
            break


answer()
print('Goodbye')
