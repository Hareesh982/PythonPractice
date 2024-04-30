def selection_sort(array,n):
    for i in range(n):
        min_value = i
        for j in range(i+1,n):
            if array[min_value] > array[j]:
                min_value = j
        array[i], array[min_value] = array[min_value], array[i]
    return array

if __name__ == "__main__":
    array = []
    s = int(input("Enter the size of the array : "))
    for i in range(s):
        ele = int(input("Enter the element : "))
        array.append(ele)
    n = len(array)

    print("Initial array : ",array)
    selection = selection_sort(array,n)
    print("Sorted array : ",selection)
    