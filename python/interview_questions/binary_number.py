# To check a number is binary or not

if __name__ == "__main__":
    num = int(input("Enter the number : "))
    t = 0
    while num > 0:
        rem = num % 10
        num = num // 10
        if rem in [1,0]:
            continue
        else:
            t = 1
            break
            
    if t == 1:
        print("Not a binary number")
    else:
        print("Binary number")
    