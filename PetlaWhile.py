number = 1
previousNumber = 0

while number < 50:
    print(previousNumber, '+', number, '=', previousNumber + number)
    previousNumber = number
    number += 1


################################
import random
myNumber = random.randint(0,20)
guess = -1
trials = 0

print("Guess my number!")


while guess != myNumber:
    guess = int(input())
    trials += 1
    if guess > myNumber:
        print("Sorry- my number is smaller than your guess, Try again!")
    elif guess < myNumber:
        print("Sorry- my number is greater than your guess, Try again!")
else:
    print("Congratulaction! Odgładłeś po", trials, "próbach")





