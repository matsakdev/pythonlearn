def contains_all_numbers(arr):
    # get length of an array
    n = len(arr)
    # from 1 to n (included)
    for i in range(1, n+1):
        # if don't have this element, result is false
        if i not in arr:
            return False
    return True