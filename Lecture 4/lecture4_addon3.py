import random
x = random.randint (1, 100)
#print(x)
user_input = int(input('input a positive number from 1 to 100: '))
if user_input not in range(1, 100):
    print('The number should be within a range of 1-100!')
    user_input = int(input('input a positive number from 1 to 100: '))
while user_input != x:
    if user_input < x:
        print('Warmer!')
    else:
        print('Colder!')
    user_input = int(input('input a positive number: '))

print('That is correct!')