
def fibonacci(num):
    n1 = 0
    n2 = 1
    for i in range(num):
        n3 = n1 + n2
        n1,n2 = n2,n3
        print(n3,end = " ")
    print()
if __name__ == "__main__":
    for i in range(10):
        res = fibonacci(i)