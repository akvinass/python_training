def common_elements():
    list_3 = {i for i in range(100) if i % 3 == 0}
    list_5 = {i for i in range(100) if i % 5 == 0}
    return list_3 & list_5

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}, 'Test1'
print('OK')