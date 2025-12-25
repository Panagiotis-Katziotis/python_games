#impoort (random)
import random

repeat = "y"
while repeat == "y":
    print(random.randint(1, 6), random.randint(1, 6))
    repeat = input("Roll again? (y/n)")