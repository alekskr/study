name = ['Oleg', 'Olga', 'Petr', 'Masha', 'Bob', 'Ivan', 'Sergey']
salary = [10000, 20000, 30000, 40000, 50000, 100000, 550000]
MAX_SALARY = 500000
TAX_PERCENT = 13

name_sal = dict(zip(name, salary))
print(name_sal)

file = open('D:\\Python projects\\обучение\\упражнения\\salary.txt', 'w+', encoding='UTF-8')
for k, v in name_sal.items():
    if v < MAX_SALARY:
        file.write('{} - {}\n'.format(k, v))
file.seek(0)
for line in file:
    name, salary = line.split(' - ')
    tax = int(salary) * TAX_PERCENT / 100
    after_tax = int(salary) - int(tax)
    print('{}: зарплата {}, налог {}, получил {}'.format(name.upper(), salary.strip(), int(tax), after_tax))
file.close()