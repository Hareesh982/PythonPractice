
def prime(num):
    if num in [2,3,5,7]:
        return f"{num} is Prime number"
    else:
        if num%2 == 0 or num %3 == 0 or num%5 == 0 or num%7 == 0:
            return f"{num} is Not a prime number"
        else:
            return f"{num} is Prime number"

if __name__ == "__main__":
    for i in range(100):
        res = prime(i)
        print(res)
    