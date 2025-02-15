my_list = [12, 3, 4, 10]

if len(my_list) == 0:
    print(my_list)
else:
    my_list = [my_list[-1]] + my_list[:-1]
    print(my_list)