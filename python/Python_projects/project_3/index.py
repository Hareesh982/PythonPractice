#rock,paper,scissors game

import random

user_count = 0
computer_count = 0
list_1 = ["rock","paper","scissors"]

while True:
    user = input("Pick Rock/Paper/Scissors or type Q to quit the game : ").lower()
    if user =="q":
        quit = 1
        break
    if user not in list_1:
        continue

    random_number = random.randint(0,2)
    computer = list_1[random_number]
    print("computer picked : ",computer)

    if(user==computer):
        print("draw")
    elif(user=="rock" and computer=="scissors"):
        print("you won")
        user_count+=1
    elif(user=="scissors" and computer=="paper"):
        print("you won")
        user_count+=1
    elif(user=="paper" and computer=="rock"):
        print("you won")
        user_count += 1
    else:
        print("computer won")
        computer_count+=1

if(user_count>0):
    print(f"you won {user_count} times")
    print(f"computer won {computer_count} times")


