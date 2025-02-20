user_input = int (input("Provide a 4-digit code: "))

digit_1 = (user_input // 1000)
digit_2 = (user_input // 100) % 10
digit_3 = (user_input // 10) % 10
digit_4 = (user_input % 10)

print(digit_1)
print(digit_2)
print(digit_3)
print(digit_4)