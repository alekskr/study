i = int(input('введите число: '))
while i < 0 or i > 10:
    print('введите другое число от 0 до 10:')
    i = int(input())
else:
    print('число подходит. ' + str(int(i)) + ' ** 2 = ' + str(int(i**2)))
print('end')
# 
print('введите число:')
while True:
    i = int(input())
    if 0 <= i <= 10:
        print('число подходит. ' + str(int(i)) + ' ** 2 = ' + str(int(i**2)))
    else:
        print('введите другое число от 0 до 10:')
        continue
print('end2')
# 
print('Enter name:')
name = input()
#while name != 'sasha' and name != 'Sasha':
while not name == 'sasha' and not name == 'Sasha':
    print('Try again:')
    name = input()
else:
    print('\n' + 'Hi, Sasha!')
print('*' * 50)
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
