def binary_search(arr, element):
    # Initialize left and right pointers
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == element:
            # Found the element
            return mid
        elif arr[mid] < element:
            # Look in the right half of the array
            left = mid + 1
        else:
            # Look in the left half of the array
            right = mid - 1

    # Element not found
    return -1
