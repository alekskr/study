# 1 Есть список гостей и то, что они принесли. Вывести перечень всех предметов
all_guests = {'Alice': {'apples': 4, 'oranges': 3}, 'Bob': {'burgers': 4, 'beers': 5},
              'John': {'apples': 5, 'beers': 2, 'nuts': 25}}


def brougth(guests, items):
    all_brougth = 0
    for v in guests.values():
        all_brougth = all_brougth + v.get(items, 0)
    return all_brougth


print(all_guests)

# while True:  # добавляет нового гостя
#     next_guest = int(input('Enter 1 for add new guest or 0 for continue: '))
#     if next_guest == 1:
#         new_guest = {input('Enter name: '): {input('Enter item: '): int(input('Enter quantity: '))}}
#         all_guests.update(new_guest)
#     else:
#         break

all_items = []  # создается список всех предметов
for val in all_guests.values():
    for keys in val.keys():
        all_items.append(keys)
        # print(keys)

all_items_no_repeat = []  # создается список всех предметов без повторений
for i in all_items:
    if i not in all_items_no_repeat:
        all_items_no_repeat.append(i)

print(all_guests)
print(all_items_no_repeat)

for i in range(len(all_items_no_repeat)):
    print(f'{i + 1}. {all_items_no_repeat[i].title()} {brougth(all_guests, all_items_no_repeat[i])}')

print()

# 2 Задан перечень предметов и их количество в инвентаре (stuff). Вывести количество и наименование предметов.
# Есть лут с дракона. Добавить лут к инвентарю.
stuff = {'rifle': 1, 'bullet': 100, 'dagger': 2, 'torch': 1, 'arrow': 100, 'rope': 2}
stuff_list = list(stuff.keys())

dragon_loot = ['coin', 'dagger', 'arrow', 'arrow', 'bow', 'coin', 'map']


def display_inventory(inv):  # выводит данные инвентаря
    print('Перечень предметов:')
    all_inv = 0
    for k, v in inv.items():
        print(f'{v} {k}')
        all_inv = all_inv + v
    print(f'Всего предметов: {all_inv}')


def add_inventory(inv, add_item):  # добавляет лут дракона в инвентарь
    print('Инвентарь с учетом лута:')
    for loot in add_item:
        inv.setdefault(loot, 0)
        inv[loot] = inv[loot] + 1
    print(inv)


display_inventory(stuff)
print()
add_inventory(stuff, dragon_loot)

print()

# 3. написать функцию, которая принимает список списков строк и отображает его в виде таблицы
# с выравниванием текса по правому краю в каждом столбце.
table_data = [['apples', 'oranges', 'bananas', 'kiwi'],
              ['elephants', 'dogs', 'cats', 'birds'],
              ['bmw', 'lada', 'kia', 'volkswagen']]


def print_table(table):
    list_table_data = []
    for q in range(len(table)):
        list_table_data = list_table_data + table[q]
    # print(list_table_data)
    offset = len(max(list_table_data, key=len))
    # print(offset)
    for i in range(len(table[0])):
        for j in range(len(table)):
            print(table[j][i].ljust(offset), end=' ')
        print()


print_table(table_data)
