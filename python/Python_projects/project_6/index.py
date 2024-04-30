# email slicer to find the username and domain name

def method_1(email):
    name,string,domain = email.strip().partition("@")
    print("User name : ",name)
    print("Domain : ",domain)


def method_2(email):
    slice = email.strip().partition("@") #partition stores the splitted values in tuple
    print(slice)
    print("User name : ", slice[0])
    print("Domain : ", slice[-1])


email = input("Enter your email : ")
method_1(email)
method_2(email)
