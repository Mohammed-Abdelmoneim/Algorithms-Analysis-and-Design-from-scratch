def binarySearch(arr, key):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if key == arr[mid]:
            return mid
        else:
            if key > arr[mid]:
                low = mid + 1
            else:
                high = mid - 1
                
    return "Not Found!"
