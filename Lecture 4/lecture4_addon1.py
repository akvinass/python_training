numbers = [1, 2, 4, 5, 6]
import random
random.shuffle(numbers)
numbers.sort()

n = max(numbers)
t = n * (n + 1) // 2
y = sum(numbers)
z = t - y
print(z, 'is the missing number')


#for x in range(len(numbers) - 1):
    #y = numbers[x] + 1
    #z = numbers[x + 1]
    #if y != z:
        #print(y, 'is the missing number')
        #break