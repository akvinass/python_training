import string

user_input = input('Input: ')
letters = ' '.join(string.ascii_letters).split()
output = []

for i in user_input:
    if i in letters:
        x =  letters.index(i) + 3
        output.append(letters[x])
    else:
        output.append(i)

print('Encoded value:', ''.join(output))