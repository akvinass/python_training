my_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

for element in my_list:
    if element == 0:
        my_list.remove(element)
        my_list.append(element)

print(my_list)