def fibonacci(n1,n2):
    n3 = n1 + n2
    print(n3)
    fibonacci(n2,n3)
if __name__ == "__main__":
    for i in range(5):
        n1 = 0
        n2 = 1
        fibonacci(n1,n2)