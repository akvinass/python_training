while True:
    d1 = float(input('Type in the first digit: '))
    d2 = float(input('Type in the second digit: '))
    action = input('Chose an operation (+, -, *, /): ')

    if action == '+':
        print(d1 + d2)
    elif action == '-':
        print(d1 - d2)
    elif action == '*':
        print(d1 * d2)
    elif action == '/':
        print(d1 / d2 if d2 !=0 else "The divisor cannot be equal to zero!")

    cont = input('Would you like to continue? y/n: ')
    if cont != 'y':
        break
print('End')