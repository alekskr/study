#! python3;
# pw.py - Программа для хранения;

import sys
import pyperclip

PASSWORDS = {'email': 'dfdomkmm', 'vk': 'fvofovof', 'skype': 'btbtbt'}

if len(sys.argv) < 2:
    print('Использование: python pw.py [имя учетной записи] - копирование пароля')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print(f'Пароль для {account} скопирован в буфер')
else:
    print(f'Аккаунт {account} отсутствует в списке')
