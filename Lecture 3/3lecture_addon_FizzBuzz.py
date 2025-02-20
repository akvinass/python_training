user_input = int(input('Type in a number: '))
x = 3
y = 5

if user_input == 0:
    print('Should not be a zero')

elif user_input % 3 == 0 and user_input % 5 == 0:
    print('FizzBuzz')
elif  user_input % 3 == 0:
    print('Fizz')
elif user_input % 5 == 0:
    print('Buzz')
elif user_input != x and str(x) in str(user_input):
    print('Almost Fizz')
elif user_input != y and str(y) in str(user_input):
    print('Almost Buzz')

