user_input = int(input('Type in a 5-digit number: '))

digit1 = (user_input // 10000)
digit2 = (user_input // 1000) % 10
digit3 = (user_input // 100) % 10
digit4 = (user_input // 10) % 10
digit5 = (user_input % 10)

print (digit5, digit4, digit3, digit2, digit1)