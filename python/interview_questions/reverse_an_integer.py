def reverse(num):
    if num in [0,1,2,3,4,5,6,7,8,9]:
        print("Reverse of an integer is : ",num)
    else:
        while num > 0:
            rem = num % 10
            num = num // 10
            print(rem, end = "")

if __name__ == "__main__":
    num = int(input("Enter the integer : "))
    reverse(num)