string_A = '+---+---+---+---+'
string_B = '|   |   |   |   |'

for i in range(10):
    print(string_A)

print("---------------------------------------------------------")


for i in range(9):
    print(string_A)
    if i < 8:
        print(string_B)

print("---------------------------------------------------------")

for i in range(9):
    print('x' * i)
    



print("---------------------------------------------------------")

for i in range(9):
    if i %2 == 0:
        print('o' * i)    
    else:
        print('x' * i)
    
