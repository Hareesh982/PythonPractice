def armstrong(num):
    temp = num
    l = 0
    li = []
    while temp > 0:
        rem = temp % 10
        temp = temp//10
        l = l + 1
        li.append(rem)
    sum = 0
    for i in li:
        sum = sum + (i**l)

    if sum == num:
        return "Armstrong number"
    else:
        return "not a Armstrong number"

if __name__ == "__main__":
    num = int(input("Enter the number : "))
    res = armstrong(num)
    print(res)