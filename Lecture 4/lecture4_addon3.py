import random
x = random.randint (1, 100)
#print(x)
user_input = int(input('input a positive number: '))

while user_input != x:
    if user_input < x:
        print('Warmer!')
    else:
        print('Colder!')
    user_input = int(input('input a positive number: '))

print('That is correct!')