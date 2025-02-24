import string

user_input = input('Input: ').replace(' ', '').lower()
letters = string.ascii_lowercase
pangram = True

for i in letters:
    if i not in user_input:
        pangram = False
        break

if pangram:
    print('Pangram detected!')
else:
    print("It's not a pangram")