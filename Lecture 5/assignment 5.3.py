import string

user_input = input("Let's create a hashtag: ").title()
punct = str.maketrans('', '', string.punctuation)
spaces = str.maketrans('', '', ' ')
x = '#' + user_input.translate(punct).translate(spaces)[:140]

print(x)
