#guessing the random number

import random
count = 0
x = random.randint(1,11)

while(True):
    user = int(input("Guess the random number : "))
    if(user==x):
        break
    else:
        if(user<x):
            print(f"number is greater than {user}")
        elif(user>x):
            print("you were below the number")
        count = count + 1

print(f"you have guessed the number after {count} attempts")

