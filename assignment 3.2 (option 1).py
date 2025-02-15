my_list = [12, 3, 4, 10]

if len(my_list) == 0:
    print(my_list)
if len(my_list) != 0:
    my_list.insert(0, my_list.pop(-1))
    print(my_list)