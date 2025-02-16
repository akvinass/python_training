digit1 = float(input('Type in the first digit: '))
digit2 = float(input('Type in the second digit: '))
action = input('Chose an operation (+, -, *, /): ')

if action == '+':
    print(digit1 + digit2)
elif action == '-':
    print(digit1 - digit2)
elif action == '*':
    print(digit1 * digit2)
elif action == '/' and digit2 != 0:
    print(digit1 / digit2)
else:
    print('The divisor cannot be equal to zero')