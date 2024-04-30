# Sum of digits of a number

def sum_of_digits(num,sum):
    if num > 0:
        rem = num % 10
        num = num // 10
        sum = sum + rem
        return sum_of_digits(num,sum)
    else:
        return sum
if __name__ == "__main__":
    for i in [1,12,123,1234,12345,123456,1234567,12345678]:
        sum = 0
        res = sum_of_digits(i,sum)
        print(i," --> ",res)
    