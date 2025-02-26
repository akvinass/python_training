import string

user_input = input("Range of letters (e.g.: a-c): ").split('-')
value1, value2 = user_input
range_in = string.ascii_letters.index(value1)
range_out = string.ascii_letters.index(value2)

print(string.ascii_letters[range_in:range_out + 1])