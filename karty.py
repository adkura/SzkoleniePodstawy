import random

colors = ['Hearts','Diamonds','Clubs','Spades']
figures = ['Ace','King','Queen','Jack','10','9']

allCards = []

for color in colors:
    for figure in figures:
        allCards.append(color + ' ' + figure)

random.shuffle(allCards)

print(allCards)

#--------------------------------------
player1 = []
player2 = []
max = len(allCards)
i = 0

while i <= max-1:
    if i % 2:
        player1.append(allCards[i])
    else:
        player2.append(allCards[i])
    i += 1

print(player1)
print(player2)


#---------------------------------------
player1 = allCards[:12]
player2 = allCards[12:]

print(player1)
print(player2)

