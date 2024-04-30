
cube = lambda x: x**3

def fibonacci(n):
    li_1 = [0,1]
    li_2 = []
    n1 = 0
    n2 = 1
    if n == 1:
        li_2.append(n1)
        return li_2
    elif n == 0:
        return li_2
    else:
        for i in range(n-2):
            n3 = n1 + n2
            li_1.append(n3)
            n1,n2 = n2,n3
        return li_1

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))


#****************SAMPLE_INPUT****************

# 5

#***************OUTPUT*****************

# [0, 1, 1, 8, 27]
