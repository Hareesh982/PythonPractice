import random
import json

with open('main.json','r') as file:
    data = json.load(file)

count_true = 0
count_false = 0
i = 1
j = 3
li = [1,2,3,4,5,6,7,8,9,10]

for i in range(1,6):
    r = random.choice(li)
    print(str(i)+"."+data[str(r)]["question"])
    for i in range(97,101):
        print(chr(i)+" "+data[str(r)][chr(i)])

    user = input("Enter the option : ").lower()
    if user == data[str(r)]["ans"]:
        print("correct answer\n")
        count_true = count_true + 1
    else:
        print("wrong answer\n")
        count_false = count_false + 1
    li.remove(r)

total_score = (count_true/5)*100
print("------------------------")
print(f"Correct answers : {count_true}")
print(f"Wrong answers : {count_false}")
print(f"Total score : {total_score}%")
print("------------------------")

    
    
        
    

    

