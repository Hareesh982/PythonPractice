
def binary_search(arr,ele):
    low = 0
    high = len(arr)-1
    for i in range(len(arr)):
        mid = (low + high)//2
        if arr[mid] == ele:
            position = mid + 1
            return f"Element found at index {mid} , position {position}"
        elif ele > arr[mid]:
            low = mid + 1
        elif ele < arr[mid]:
            high = mid - 1
    return "Element not found"

if __name__ == '__main__':
    if __name__ == '__main__':
        n = int(input("Enter the size of array : "))
    arr = []
    for i in range(n):
        j = i + 1
        arr_ele = int(input(f"Enter the element : "))
        arr.append(arr_ele)
    element = int(input("Enter the element to be found : "))
    print(arr)
    res = binary_search(arr,element)
    print(res)