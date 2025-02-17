q_1 = input('Do you often take charge in group situations? y/n: ')
q_2 = input('Would you rather outsmart someone than outfight them? y/n: ')
q_3 = input('Do you believe that personal success is important? y/n: ')
q_4 = input('Would you be willing to bend the rules to get ahead? y/n: ')
q_5 = input('Do you enjoy learning for the sake of knowledge? y/n: ')

q_list = []

if q_1 == 'y':
    q_list.append(1)
else:
    q_list.append(1)
    del q_list[1]

if q_2 == 'y':
    q_list.append(1)
else:
    q_list.append(1)
    del q_list[1]

if q_3 == 'y':
    q_list.append(1)
else:
    q_list.append(1)
    del q_list[1]

if q_4 == 'y':
    q_list.append(1)
else:
    q_list.append(1)
    del q_list[1]

if q_5 == 'y':
    q_list.append(1)
else:
    q_list.append(1)
    del q_list[1]

if len(q_list) == 1:
    print('Congratulations. Your house is Hufflepuff!')
elif len(q_list) == 2:
    print('Congratulations. Your house is Hufflepuff!')
elif len(q_list) == 3:
    print('Congratulations. Your house is Ravenclaw!')
elif len(q_list) == 4:
    print('Congratulations. Your house is Gryffindor!')
elif len(q_list) == 5:
    print('Congratulations. Your house is Slytherin!')
