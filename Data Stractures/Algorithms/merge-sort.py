# o(nlogn) - best and worst case 
def merge(arr1, arr2):
    result = []
    left = 0
    right = 0
    
    while left < len(arr1) and right < len(arr2):
        if(arr1[left] < arr2[right]):
            result.append(arr1[left])
            left+=1
        else:
            result.append(arr2[right])
            right+=1
    while left < len(arr1):
        result.append(arr1[left])
        left+=1
    while right < len(arr2):
        result.append(arr2[right])
        right+=1
    return result
    
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2 
    arr3 = merge_sort(arr[:mid])
    arr4 = merge_sort(arr[mid:])
    return merge(arr3, arr4)

print(merge_sort([92,23940,2,12021,23404,6,5756,234,36764342,34543,5435,34,55,655,4332,43]))