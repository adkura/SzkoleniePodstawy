numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]

i=0
imax = len(numbers)-1


while i<imax:
    print(numbers[i])
    if numbers[i]*2 == numbers[i+1]:
        print('\tFound', numbers[i])
    i+=1


###################################
i=0
imax = len(numbers)-2


while i<imax:
    print(numbers[i])
    if numbers[i]**2 == numbers[i+1] and numbers[i+1]**2 == numbers[i+2]:
        print('\tFound', numbers[i])
    i+=1
    
#####################################
texts = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

i=1
imax=len(texts)-1

while i<imax:
    #print(i, texts[i])
    if len(texts[i]) == len(texts[i+1]):
        print('Found: ', texts[i], texts[i+1])
    i+=1
