#quiz game

play = input("Do you want to play the quiz? ").lower()
if play == "no":
    quit()
elif play == "yes":
    question = ["1. what does CPU stands for?", "2. what does RAM stands for?",
                "3. what does ROM stands for?", "4. what does PROM stands for?"]

    answer = ["central processing unit", "random access memory",
                "read only memory", "programmable read only memory"]

    def quiz(x, y):
        ans = input(x).lower()
        if(ans == y):
            print("correct")
        else:
            print("incorrect")

    for i in question:
        quiz(i, answer)