import copy


print('две переменные ссылаются на один список:')
spam = ['cat', 'bat', 'rat', 'elephant']
pam = spam
pam[1] = 'dog'
print(spam)
print(pam)
spam.append('cow')
print(spam)
print(pam)
print('создаем дубликат списка spam:')
pam = copy.copy(spam)
pam[1] = 42
print(spam)
print(pam)
