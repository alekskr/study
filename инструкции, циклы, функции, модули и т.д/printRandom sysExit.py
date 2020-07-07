import math
import random
import sys

print(math.sqrt(4))
print('*' * 20)
for i in range(5):
    print(random.randint(1, 10))
print('*' * 20)
while True:
    print('Type exit to exit')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')

