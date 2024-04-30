# Question-1
# Write a program to find all pairs of an integer array whose sum is equal to a given number?



def pair(array,num):
    for i in range(len(array)-1):
        for j in range(len(array)-1):
            if(array[i] + array[j+1] == num):
                print(f"{array[i]},{array[j+1]}")
    return ""

array = [1,2,3,4,5,6,7,8,9]
num = int(input("Enter the number : "))

fun = pair(array,num)
print(fun)




# ********************OUTPUT***********************

# Enter the number: 6
# 1, 5
# 2, 4
# 3, 3
# 4, 2
