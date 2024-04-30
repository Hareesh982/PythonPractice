count = int(input("enter the number : "))
count_1 = count - 1
number = 1
for i in range(1,count+1):
    print(" "*(count_1)+"*"*number)
    count_1 = count_1 - 1
    number = number + 2
number_2 = 1
for j in range(1,count+1):
    number = number-2
    print(" "*number_2+"*"*(number-2))
    number_2 = number_2+1
    
