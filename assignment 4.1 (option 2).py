my_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
def zero_func(x):
    return x == 0
my_list.sort(key=zero_func)
print(my_list)