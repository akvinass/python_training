import random
x = random.randint (1, 100)
#print(x)
user_input = int(input('Input a positive number from 1 to 100: '))

while user_input != x:
    if user_input not in range(1, 100):
        print('The number is out of range!')
    elif user_input < x:
        print('Warmer!')
    elif user_input > x:
        print('Colder!')
    user_input = int(input('Input a positive number from 1 to 100: '))
print('That is correct!')