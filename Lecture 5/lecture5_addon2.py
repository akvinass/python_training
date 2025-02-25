input1 = input('Input: ').replace(' ', '').lower()
input2 = input('Input: ').replace(' ', '').lower()

if sorted(input1) == sorted(input2):
    print('Anagram detected!')
else:
    print('Those are different words')