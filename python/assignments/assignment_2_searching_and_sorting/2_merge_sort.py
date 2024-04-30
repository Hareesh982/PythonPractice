
def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array)//2
    left_array = array[:mid]
    right_array = array[mid:]
    
    merge_sort(left_array)
    merge_sort(right_array)
    
    return merge_two_sorted_list(left_array,right_array,array)

def merge_two_sorted_list(array_1,array_2,array):
    n1 = len(array_1)
    n2 = len(array_2)
    i = 0
    j = 0
    k = 0
    while i < n1 and j < n2:
        if array_1[i] < array_2[j]:
            array[k] = array_1[i]
            i = i + 1
        elif array_2[j] < array_1[i]:
            array[k] = array_2[j]
            j = j + 1
        k = k + 1
    while i < n1:
        array[k] = array_1[i]
        i = i + 1
        k = k + 1
    while j < n2:
        array[k] = array_2[j]
        j = j + 1
        k = k + 1
    return array

if __name__ == "__main__":
    test_cases = [  
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9,8,7,2],
        [1,2,3,4,5]
    ]
    for i in test_cases:
        print("Initial Array : ",i)
        x = merge_sort(i)
        print(" Sorted Array : ",x)
        print()
    