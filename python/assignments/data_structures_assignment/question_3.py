# Question-3
# Write a program to check if two strings are a rotation of each other?



def rotation(s1,s2):
    if len(s1)!=len(s2):
        return "strings are not rotation of each other"
    else:
        start = s1[0]
        x = s2.index(start)
        y = s2[x:]+s2[0:x]
        if s1 == y:
            return "strings are rotation of each other"
        else:
            return "strings are not rotation of each other"

string_1 = input("Enter string 1 : ").upper()
string_2 = input("Enter string 2 : ").upper()

fun = rotation(string_1,string_2)
print(fun)



#**********************OUTPUT*********************

# Enter string 1: ABBB
# Enter string 2: BBAB
# strings are rotation of each other

# Enter string 1: ABAC
# Enter string 2: ACAB
# strings are not rotation of each other
