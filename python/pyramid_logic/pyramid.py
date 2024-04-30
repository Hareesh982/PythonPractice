count = int(input("enter the number : "))
count_1 = count - 1
number = 1
for i in range(1, count+1):
    print(" "*(count_1)+"*"*number)
    count_1 = count_1 - 1
    number = number + 2
