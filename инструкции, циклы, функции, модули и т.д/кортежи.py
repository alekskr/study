humans = ('Ivan', 'Jo', 'Petr', 'Serg', 'Alex')

x = 0
while x < len(humans):
    print(humans[x])
    x = x + 1
print('-' * 20)
for i in humans:
    print(i)

print(humans[0:2])

days30 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
          11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
          21, 22, 23, 24, 25, 26, 27, 28, 29, 30)
print(days30[0:28])
