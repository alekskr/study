#  1 Глобальные переменные могут читаться из локальной области видимости:
def spam1():
    print(eggs1)


eggs1 = 42
spam1()
print(eggs1)


#
#  2 В локальных областях видимости не могут использоваться переменные из других локальных областей:
def spam2():
    eggs = 99
    bacon1()
    print(eggs)


def bacon1():
    ham = 101
    print(ham)
    eggs = 3
    print(eggs)


spam2()


# 3 Локальные и глобальные переменные с одинаковыми именами:
# Если закоменить в обеих функциях eggs2 = ' ', то из этих
# локальных областей будет читаться глобальная переменная eggs2 = 'global'
def spam3():
    eggs2 = 'spam local'
    print(eggs2)  # выводится строка 'spam local'


def bacon():
    eggs2 = 'bacon local'
    print(eggs2)  # выводится строка 'bacon local'
    spam3()
    print(eggs2)  # выводится строка 'bacon local'


eggs2 = 'global'
bacon()
spam3()
print(eggs2)  # выводится строка 'global'
