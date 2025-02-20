import random
my_list = []
while len(my_list) < 10:
    my_list.append(random.randint(1,10))
    if len(my_list) == 10:
        break
print(my_list)

for b in range(0, len(my_list) - 1):
    x = sum(my_list[b:b+2])
    if x == 7:
        print('Found a pair that sums to 7!')
        break

print('Try once again')