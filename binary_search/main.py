def binarySearch(arr, key):
    # Initialize the starting index (low) and ending index (high) for the search range
    low = 0
    high = len(arr) - 1

    # Continue searching while the search range is valid
    while low <= high:
        # Calculate the middle index of the current search range
        mid = (low + high) // 2
        # Check if the middle element is the key we are searching for
        if key == arr[mid]:
            return mid  # Return the index of the key if found
            
        else:
            # If the key is greater than the middle element, adjust the search range to the right half
            if key > arr[mid]:
                low = mid + 1
            # ... less than ..., adjust the search range to the left half
            else:
                high = mid - 1
    # If the key was not found in the array, return "Not Found!"      
    return "Not Found!"
