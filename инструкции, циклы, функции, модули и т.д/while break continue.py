print()
i = 0
while 1==1:
    print(i)
    i = i + 1
    if i >=5:
        print('Breaking')
        break
print('Finished')
print()
i = 5
while True:
    print(i)
    i = i - 1
    if i <=2:
        break
print('=' * 20)

# print('=' * 20)
# print('Введите возраст:', end=' ')
# age = int(input())
# if age >= int(18):
#     print('\n' + 'Введите имя:')
#     while True:
#         name = input()
#         if name == 'Sasha' or name == 'sasha':
#             print('\n' + 'Введите пароль:')
#             password = input()
#             while password != '123' and password != '123456':
#                 print('\n' + 'Неверный пароль! Попробуй еще раз:')
#                 password = input()
#             else:
#                 print('\n' + 'Hello, Sasha!')
#                 break
#         else:
#             print('\n' + 'Имя не найдено! Попробуй снова:')
#             continue
# else:
#     print('\n' + 'Ты слишком мал!')
# print('=' * 20)

# var 2
print('=' * 20)
while True:
    age = input('Введите возраст: ')
    if age.isdecimal():
        break
    else:
        print('Введите возраст правильно')
if int(age) >= 18:
    while True:
        name = input('Введите имя: ')
        if name.lower() == 'sasha':  # or name == 'sasha':
            while True:
                password = input('Введите пароль: ')
                if password == '123' or password == '123456':
                    print('Hello, Sasha!')
                    break
                else:
                    print('Неверный пароль! Попробуй еще раз:')
                    continue
            break
        else:
            print('\n' + 'Имя не найдено! Попробуй снова:')
            continue
else:
    print('\n' + 'Ты слишком мал!')
print('=' * 20)
