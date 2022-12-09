def find_max(arr):
    # Base case: if the array has only one element, return that element.
    if len(arr) == 1:
        return arr[0]

    # Divide the array into two smaller arrays.
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Find the maximum element in each of the two arrays.
    max_left = find_max(left)
    max_right = find_max(right)

    # Return the maximum of the two maximum elements.
    return max(max_left, max_right)

# Test the divide and conquer approach on a sample array.
arr = [3, 7, 4, 8, 9, 1, 2, 5]
print(find_max(arr))  # should print 9
