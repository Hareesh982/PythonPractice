if __name__ == "__main__":
    li = []
    for i in range(3):
        x = int(input("Enter the number : "))
        li.append(x)
    if li[1] > li[0]:
        if li[1] > li[2]:
            print("greatest among three numbers is : ",li[1])
        else:
            print("greatest among three numbers is : ",li[2])
    else:
        if li[0] > li[2]:
            print("greatest among three numbers is : ",li[0])
        else:
            print("greatest among three numbers is : ",li[2])