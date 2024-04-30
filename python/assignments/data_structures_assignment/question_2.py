# Question-2
# Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.



def rev_array(x):
    j = -1
    for i in range(len(x)//2):
        x[i],x[j] = x[j],x[i]
        j = j - 1
    return x

array = [1,2,3,4,5]
print("Initial array : ",array)

rev = rev_array(array)
print("Reversed array : ",rev)



#*******************OUTPUT*********************

# Initial array:  [1, 2, 3, 4, 5]
# Reversed array:  [5, 4, 3, 2, 1]
