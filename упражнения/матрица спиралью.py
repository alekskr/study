n = 5  # размер матрицы
m = []  # будущая матрица

# создание пустой матрицы
for i in range(n):
    m.append(['-'] * n)
print(m)

count = 0  # счетчик чисел от 0 до n

# заполнение верхнего ряда матрицы
for j in range(n):
    m[0][j] = count
    count += 1
print(m)

i = 0  # индекс последней заполненной строки
j = n - 1  # индекс последнего заполненного элемента

while n * n != count:
    # цикл движения вниз:
    # n - 1 т.к. первая строка матрицы уже заполнена
    for index in range(n - 1):
        i += 1
        m[i][j] = count
        count += 1
        # print(m)

    # цикл движения влево:
    for index in range(n - 1):
        j -= 1
        m[i][j] = count
        count += 1
        # print(m)

    # цикл движения вверх:
    # n - 2 т.к. первая и последняя строки матрицы уже заполнены
    for index in range(n - 2):
        i -= 1
        m[i][j] = count
        count += 1
        # print(m)

    # цикл движения вправо:
    for index in range(n - 2):
        j += 1
        m[i][j] = count
        count += 1
        # print(m)

    n -= 2

print(m)

# вычисление отступа:
max_values = []
for i in m:
    max_values.append(max(i))
offset = len(str(max(max_values)))

print('*' * 25)

for i in m:
    s = [str(x).center(offset) for x in i]
    print(' '.join(s))

print('*' * 25)
