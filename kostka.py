import random

min = 1
max = 6

dice = random.randint(min, max)    
dices = []


for i in range(5):
    dices.append(random.randint(min, max))


dices.sort()

print(dices)

'''
if dice == 1:
    print('o')
elif dice == 2:
    print('o')
    print('o')
elif dice == 3:
    print('o')
    print('o')
    print('o')
elif dice == 4:
    print('o')
    print('o')
    print('o')
    print('o')
elif dice == 5:
    print('o')
    print('o')
    print('o')
    print('o')
    print('o')
else:
    print('o')
    print('o')
    print('o')
    print('o')
    print('o')
    print('o')
'''    
