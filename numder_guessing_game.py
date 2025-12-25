
import random

number = random.randint(1, 99)
guesses = 0
while guesses < 6:
    usernum = int(input("Enter a number 1 and 99:"))
    guesses += 1
    print("This is your %d turn!" % guesses)
    if usernum < number:
         print("Your guess is low!")
    elif usernum > number:
         print("Your guess is high!")
    else:
        break
if usernum == number:
    print("You win!")
else:
    print("Game over! The number was:", number)