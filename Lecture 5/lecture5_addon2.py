input1 = input('Input: ').replace(' ', '').lower()
input2 = input('Input: ').replace(' ', '').lower()
#print(input1, input2)
print('Anagram detected!' if all (i in input1 for i in input2) else 'Those are different words')