def price_string(func):
    def wrapper(arg):
        return "£" + str(func(arg))
    return wrapper


@price_string
def new_price(price):
    return price * 90 / 100


price1 = 100
print(new_price(price1))


def print_info(func):
    def wrapper(arg1, arg2):
        print("The arguments of the function are:", arg1, arg2)
        return func(arg1, arg2)
    return wrapper


@print_info
def addition(arg1, arg2):
    return arg1 + arg2


a = 2
b = 4
print(addition(a, b))


def morning(func):
    def wrapper(name):
        func(name)
        print('Good morning,', name)
    return wrapper


@morning
def greetings(name1):
    print('Hello,', name1)


greetings('Susie')


def nighttime(func):
    def wrapper(name):
        print('It is nighttime')
        return func(name)
    return wrapper


@nighttime
def get_message(name):
    print('We can hear some night birds like', name)


get_message('owls')


def tagged(func):
    def wrapper(string):
        return '<title>' + func(string) + '</title>'
    return wrapper


@tagged
def from_input(inp):
    return inp.strip()


print(from_input(' hhhh h '))
