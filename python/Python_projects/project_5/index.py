import random

def play_game():
    user = 0
    list_1 = [1,2,3,4,5,6,7,8,9]
    one, two, three, four, five, six, seven, eight, nine = " ", " ", " ", " ", " ", " ", " ", " ", " "
    
    print(f"| {one} | {two} | {three} |")
    print("|---|---|---|")
    print(f"| {four} | {five} | {six} | ")
    print("|---|---|---|")
    print(f"| {seven} | {eight} | {nine} |")
    
    for i in range(5):
        com = random.choice(list_1)
        print(f"computer position is {com}")
        list_1.remove(com)

        if(com == 1):one = 1 
        elif(com == 2):two = 1
        elif(com == 3):three = 1
        elif(com == 4):four = 1
        elif(com == 5):five = 1
        elif(com == 6):six = 1
        elif(com == 7):seven = 1
        elif(com == 8):eight = 1
        elif(com == 9):nine = 1

        print(f"| {one} | {two} | {three} |")
        print("|---|---|---|")
        print(f"| {four} | {five} | {six} | ")
        print("|---|---|---|")
        print(f"| {seven} | {eight} | {nine} |")

        if(i<4):
            user = int(input("Enter the position : "))
            if(user == 1):one = 0
            elif(user == 2):two = 0
            elif(user == 3):three = 0
            elif(user == 4):four = 0
            elif(user == 5):five = 0
            elif(user == 6):six = 0
            elif(user == 7):seven = 0
            elif(user == 8):eight = 0
            elif(user == 9):nine = 0

            print(f"| {one} | {two} | {three} |")
            print("|---|---|---|")
            print(f"| {four} | {five} | {six} | ")
            print("|---|---|---|")
            print(f"| {seven} | {eight} | {nine} |")
            list_1.remove(user)
        else:
            break
        if((one==1 and two==1 and three==1) or (four==1 and five==1 and six==1) or (seven==1 and eight==1 and nine==1) or (one==1 and four==1 and seven==1) or (two==1 and five==1 and eight==1) or (three==1 and six==1 and nine==1) or (one==1 and five==1 and nine==1) or(three==1 and five==1 and seven==1)):
            print("computer won")
            break
        elif((one==0 and two==0 and three==0) or (four==0 and five==0 and six==0) or (seven==0 and eight==0 and nine==0) or (one==0 and four==0 and seven==0) or (two==0 and five==0 and eight==0) or (three == 0 and six == 0 and nine == 0) or (one == 0 and five == 0 and nine == 0) or (three == 0 and five == 0 and seven == 0)):
            print("user won")
            break
        else:
            continue
def game():
    print("TIC-TAC-TOE")
    user_input = input("Do you want to play the game? yes/no : ").lower()
    if(user_input == "yes"):
        play_game()
    elif(user_input == "no"):
        quit()
    else:
        print("please type yes or no")
        game()
game()
