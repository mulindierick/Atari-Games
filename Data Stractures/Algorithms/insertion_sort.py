# start at index 2, compare curr num to all nums before it until curr num is in its right spot.
# o(n^2) - worst, o(n) - best, happens when list is already sorted

def insertion_sort(arr):
    for i in range(1, len(arr)):
        curr = arr[i]
        back = i - 1
        
        while back >= 0 and arr[back] > curr:
            arr[back + 1], arr[back] = arr[back], arr[back + 1] # do the swaps
            back -= 1
        arr[back + 1] = curr #bring it back right behind curr
    return arr
    
print(insertion_sort([3,5,23,7,5,1]))


def insertion_sort_recursive(arr, i, arr_len):
    
    curr = arr[i]
    back = i - 1
    while back >= 0 and arr[back] > curr:
        arr[back + 1], arr[back] = arr[back], arr[back + 1]
        back -= 1 
    arr[back + 1] = curr
    
    if i + 1 <= arr_len:
        insertion_sort_recursive(arr, i + 1, arr_len)
    return arr
    

print(insertion_sort_recursive([3,5,23,7,5,1], 1, len([3,5,23,7,5,1]) - 1))