
def fun(array,key,i=0):
    if key == array[i]:
        i = i + 1
        return f"element found at position {i}"
    else:
        i = i + 1
        return fun(array,key,i)

array = [3,4,2,5,7,6]
key = int(input("Enter the key : "))
x = fun(array,key)
print(x)