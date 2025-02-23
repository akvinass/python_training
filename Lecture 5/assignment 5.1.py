import keyword
import string

user_input = input('Username: ')

if user_input in keyword.kwlist:
    print(False)

elif any (i.isupper() for i in user_input) or user_input[0].isdigit():
    print(False)

elif any (i == ' ' for i in user_input):
    print(False)

elif any (i in string.punctuation and i != '_' for i in user_input) or '__' in user_input:
    print(False)

else:
    print(True)
