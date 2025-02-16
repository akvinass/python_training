my_list = [1, 2, 3, 4, 5]

x = len(my_list)/2
y = len(my_list)//2
z = x - y

if  z == 0:
    print([my_list[:y], my_list[y:]])
else:
    print([my_list[:y + 1], my_list[y + 1:]])