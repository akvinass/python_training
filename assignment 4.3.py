import random
rnd_range = range(3, 11)
rnd_k = random.randint(3,8)
rnd_list = random.sample(rnd_range, rnd_k)

print(rnd_list)
print([rnd_list[0], rnd_list[2], rnd_list[-2]])

#modif_list = []
#for element in (0, 2, -2):
    #modif_list.append(rnd_list[element])
#print(rnd_list)
#print(modif_list)

#print(rnd_list)
#print([rnd_list[element] for element in (0, 2, -2)])

