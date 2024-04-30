
def bubble_sort(array,n):
    for i in range(n-1):
        for j in range(n-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array

if __name__ == "__main__":
    array = []
    s = int(input("Enter the size of the array : "))
    for i in range(s):
        ele = int(input("Enter the element : "))
        array.append(ele)
    n = len(array)

    print("Initial array : ",array)
    bubble = bubble_sort(array,n)
    print("Sorted array : ",bubble)
