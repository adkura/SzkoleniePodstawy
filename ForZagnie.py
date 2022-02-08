##i = 10
##
### 10! = 1*2*3*4*5*6*7*8*9*10
##
##silnia = 1
##
##for x in range(1, i+1):
##    silnia = silnia * x
##else:
##    print(silnia)
##

print('-----------------------------------')

y = 1
for x in range(1,11):
    silnia = 1
    for y in range(1,x+1):
        silnia *= y
    print(x, silnia)

print('-----------------------------------')

list_noun = ['dog', 'potato', 'meal', 'icecream', 'car']
list_adj = ['dirty', 'big', 'hot', 'colorful', 'fast']

for noun in list_noun:
    for adj in list_adj:
        print(adj, noun)
