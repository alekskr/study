a = 30
b = 33
if b > a:
    print('b bolshe a')
elif a == b:
    print('a ravno b')


print("This is line 1." + '[END]')
print("This is line 2.", end='[END]\n')
print("This is line 3.", end='[END]\n')
print('a' + 'b')
print('a' * 5)

print('введите a ', end='')
a = int(input())
print('введите b ', end='')
b = int(input())
if a >= b:
    print(a + b)
else:
    print(a*a)
while True:
    print(b**a)
    break
if a <= b:
    print(str(a + b) + str(', ') + str(a * b))
print('конец')

print('enter age')
age = int(input())
if age >= 18:
    print('ok')
else:
    print('no')
