user_input = input('Input: ')
x = ['a', 'e', 'i', 'o', 'u']
count = []

for i in user_input:
    if i in x:
        count.append(i)
print(len(count))