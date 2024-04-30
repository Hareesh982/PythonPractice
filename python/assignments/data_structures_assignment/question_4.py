# Question-4
# Write a program to print the first non-repeated character from a string?



def non_repeated(x):
    for i in x.strip():
        if x.count(i) == 1:
            return i

s = input("Enter a string : ")

character = non_repeated(s)

print(f"First non repeated character in a string is : {character}")



#**********************OUTPUT************************

# Enter a string: hareesh
# First non repeated character in a string is: a
