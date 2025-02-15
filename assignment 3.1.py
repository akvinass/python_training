digit1 = float(input('Type in the first digit: '))
digit2 = float(input('Type in the second digit: '))
action = input('Chose an operation (+, -, *, /): ')


if action == '+':
    print(digit1 + digit2)
if action == '-':
    print(digit1 - digit2)
if action == '*':
    print(digit1 * digit2)
if action == '/' and digit2 != 0:
    print(digit1 / digit2)
if action == '/' and digit2 == 0:
    print('The divisor cannot be equal to zero')