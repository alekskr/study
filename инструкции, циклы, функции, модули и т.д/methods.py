#  index()
print('index()')
cars = ['kia', 'lada', 'bmw']
print(cars)
print(cars.index('lada'), cars.index('bmw'))
print('*' * 30)

#  append() insert()
print('append() insert()')
cars.append(['vw', 'mazda'])
cars.append('kia')
cars.insert(1, 'honda')
print(cars)
print('*' * 30)

#  remove() del()
print('remove() del()')
cars.remove('kia')
print(cars)
del cars[-2][0]
print(cars)
print('*' * 30)

#  sort()
print('sort()')
let = ['m', 'c', 'Z', 'o', 'r', 'C', 'c', 'a']
let1 = ['m', 'c', 'Z', 'o', 'r', 'C', 'c', 'a']
num = [100, 55, 66.7, 52.2, 34, 99, 1, 0]
num.sort()
print(num)
num.sort(reverse=True)
print(num)
let.sort()
print(let)
let1.sort(key=str.lower)
print(let1)
