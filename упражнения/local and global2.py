def spam():
    global eggs
    eggs = 'spam global'
    # print(eggs)


def bacon():

    eggs = 'bacon'
    print(eggs)


def ham():

    eggs = 'ham'
    print(eggs)


eggs = 42
spam()
bacon()
ham()
print(eggs)
