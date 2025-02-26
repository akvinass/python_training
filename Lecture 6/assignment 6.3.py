import math

user_input = int(input("Input a whole number: "))

while user_input > 9:
    user_input = math.prod(int(i) for i in str(user_input))
print(user_input)