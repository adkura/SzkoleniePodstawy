minLikes = 500
minShares = 100

numLikes = 600
numShares = 50

if numLikes >= minLikes and numShares >= minShares:
    print("Obniżamy ceny!")
else:
    print("Nic z tego! nie ma obniżki")

#------------------------------------

isPizzaOrdered = True
isBigDrinkOrdered = True
isWeekend = False

if (isPizzaOrdered or isBigDrinkOrdered) and not isWeekend:
    print("Burger dla Ciebie!")
else:
    print("Dziś promocji nie dostajesz!")

#------------------------------------------------

diskSize = 140
diskSizeUsed = 133
fileSize = 10

if diskSize-diskSizeUsed >= fileSize:
    print("File can be downloaded")
else:
    print("Is small size to disk!")
    
