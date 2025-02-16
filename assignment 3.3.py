my_list = [1, 2, 3, 4, 5, 6]

x = len(my_list)/2
y = len(my_list)//2
z = x - y

if  z == 0:
    print([my_list[:len(my_list)//2], my_list[len(my_list)//2:]])

if  z != 0:
    print([my_list[:len(my_list)//2 + 1], my_list[len(my_list)//2 + 1:]])