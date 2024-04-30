count = int(input("enter the number : "))
for i in range(count):
    for j in reversed(range(1,count + 1)):
        print(j,end=" ")
    print()
    count = count - 1

# 10 9 8 7 6 5 4 3 2 1
# 9 8 7 6 5 4 3 2 1
# 8 7 6 5 4 3 2 1
# 7 6 5 4 3 2 1
# 6 5 4 3 2 1
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1
