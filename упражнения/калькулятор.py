print('Enter +, -, *, /')
print('Enter "quit" to end the program' + '\n')
while True:
    user_input = input('Your choice: ')
    if user_input == 'quit':
        break
    elif user_input == '+' \
            or user_input == '-' \
            or user_input == '*' \
            or user_input == '/':
        while True:
            num1 = input('Number 1: ')
            try:
                var = num1 == float(num1)
                while True:
                    num2 = input('Number 2: ')
                    try:
                        var = num2 == float(num2)
                        break
                    except ValueError:
                        print('Unknown input, try again: ')
                        continue
            except ValueError:
                print('Unknown input, try again: ')
                continue
            if user_input == '+':
                print('result = ' + str(float(num1) + float(num2)))
            if user_input == '-':
                print('result = ' + str(float(num1) - float(num2)))
            if user_input == '*':
                print('result = ' + str(float(num1) * float(num2)))
            if user_input == '/':
                print('result = ' + str(float(num1) / float(num2)))
            break
    else:
        print('Unknown input, try again: ')
        continue
    break
print('The end')
