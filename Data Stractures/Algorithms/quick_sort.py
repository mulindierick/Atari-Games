# o(nlogn) - best case
# o(n^2) - worst case  - occurs when array is already sorted or all elements are the same

def get_index(arr, start, end):
    pivot = arr[start]
    index = start
    
    for i in range(start+1, len(arr)):
        if pivot > arr[i]:
            index += 1 
            arr[i], arr[index] = arr[index], arr[i]
    arr[start], arr[index] = arr[index], arr[start]
    return index
            
def quick_sort(arr, start, end):
    if start < end:
        index = get_index(arr, start, end)
        quick_sort(arr, start, index - 1)
        quick_sort(arr, index+1, end)
    return arr

print(quick_sort([2,0,3,45,53,2,1,2,1,34,5,664,3,22,3,2], 0, len([2,3,45,53,2,1,2,1,34,5,664,3,22,3,2]) - 1))