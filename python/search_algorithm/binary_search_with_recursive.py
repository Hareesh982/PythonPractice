
def fun(low,high,key,array):
    mid = (low+high)//2
    if key == array[mid]:
        position = mid + 1
        return f"key found at position {position}"   
    elif key < array[mid]:
        high = mid - 1
        return fun(low,high,key,array)
    elif key > array[mid]:
        low = mid + 1
        return fun(low,high,key,array)


array = [1,2,3,4,5,6,7,8]
key = int(input("Enter the key : "))

low = 0
high = len(array)-1

x = fun(low,high,key,array)
print(x)
