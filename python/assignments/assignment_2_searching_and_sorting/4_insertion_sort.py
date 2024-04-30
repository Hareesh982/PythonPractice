
def insertion_sort(array,n):
    for i in range(1,n):
        key = array[i]
        j = i - 1
        while j>=0 and array[j] > key:
            array[j+1] = array[j]
            j = j - 1
        array[j+1] = key
    return array

if __name__ == "__main__":
    array = [2,4,6,8,1,3,5,7]
    n = len(array)

    print("Initial array : ",array)
    insertion = insertion_sort(array,n)
    print("Sorted array : ",insertion)