#Hangman game

import random
from words import words

computer = random.choice(words)
length = len(computer)
output = []
position = 0
word = "no"
count = 0

for i in range(length):
    output.append("_")

user_input = input("do you want to play the game? type yes/no : ").lower()
if(user_input=="no"):
    quit()
elif(user_input=="yes"):
    while(word=="no"):
        user = input("enter the letter : ")
        if user in computer:
            position = computer.index(user)
            output[position]=user
        else:
            print(f"{user} letter is not in the word")
            continue
        value = "".join(output)
        print(value)
        count = count + 1
        if(count == length//2+1 ):
            break
        word = input("Do you know the word? type yes/no : ").lower()
        if(word == "no"):
            continue
        elif(word=="yes"):
            break

if(word == "yes"):
    ans = input("enter the word : ")
    if(ans == computer):
        print(f"you have guessed the correct word i.e {computer}")
    else:
        print("your guess is wrong")
        print(f"The word is {computer}")
else:
    ans = input("enter the word : ")
    if(ans == computer):
        print(f"you have guessed the correct word i.e {computer}")
    else:
        print("your guess is wrong")



