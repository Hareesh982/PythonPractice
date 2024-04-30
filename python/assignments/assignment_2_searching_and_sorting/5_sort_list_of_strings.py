
def string_sort(array,n):
    for i in range(n-1):
        for j in range(n-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
    return array

if __name__ == "__main__":
    array = ["apple", "banana", "aab","date","a","b" ,"elderberry","bat"]
    n = len(array)
    print("Initial array : ",array)
    final_array = string_sort(array,n)
    print("Sorted array : ",final_array)