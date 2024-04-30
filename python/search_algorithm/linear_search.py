
def linear_search(arr,element):
    for i in range(0,len(arr)):
        if arr[i] == element:
            return f"element {arr[i]} found at position {i}"
    return "element not found"


if __name__ == '__main__':
    n = int(input("Enter the size of array : "))
    arr = []
    for i in range(n):
        j = i + 1
        arr_ele = int(input(f"Enter the element {j} : "))
        arr.append(arr_ele)
    element = int(input("Enter the element to be found : "))
    res = linear_search(arr,element)
    print(res)
