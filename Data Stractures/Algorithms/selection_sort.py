# find smallest element and bring it to the front.
# repeat until array is sorted 
# O(n^2) - best & worst case

def selection_sort(array):
    for i in range(len(array)):
        mn = float("inf")
        mn_index = 0
        for j in range(i, len(array)):
            if array[j] < mn:
                mn = min(mn, array[j])
                mn_index = j
                array[i], array[mn_index] = array[mn_index], array[i]
    return array

print(selection_sort([3,4,56,32,33,55,2,22,33456,77,81,3]))


def sel_sort_recursive(arr, start):
    if start >= len(arr) - 1:
        return arr
    mn = float("inf")
    mn_index = 0
    
    for i in range(start, len(arr)):
        if arr[i] < mn:
            mn = min(mn, arr[i])
            mn_index = i
    arr[start], arr[mn_index] = arr[mn_index], arr[start]
    return sel_sort_recursive(arr, start + 1)
    

print(sel_sort_recursive([4,34,5,2,42,456,4323,1], 0))