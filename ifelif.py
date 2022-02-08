minLikes = 500
minShares = 100

numLikes = 400
numShares = 80

if numLikes >= minLikes and numShares >= minShares:
    print("Obniżamy ceny!")
else:
    if numLikes < minLikes:
        print("brakuje lajków")
    else:
        if numShares < minShares:
            print("brakuje udostępnień")

#####################################

if numLikes >= minLikes and numShares >= minShares:
    print("Obniżamy ceny!")
elif numLikes < minLikes:
        print("brakuje lajków")
elif numShares < minShares:
        print("brakuje udostępnień")



####################################
isPizzaOrdered = False
isBigDrinkOrdered = True
isWeekend = False

if (isPizzaOrdered or isBigDrinkOrdered) and not isWeekend:
    print("Burger dla Ciebie!")
else:
    if isWeekend:
        print("jest weekend")
    else:
        print("nie kupiłeś napoju lub pizzy")

#################################################################

if (isPizzaOrdered or isBigDrinkOrdered) and not isWeekend:
    print("Burger dla Ciebie!")
elif isWeekend:
    print("jest weekend")
else:
    print("nie kupiłeś napoju lub pizzy")
