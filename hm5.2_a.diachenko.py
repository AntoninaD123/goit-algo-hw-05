def binary_search_upper_bound(arr, target):
    """
    Binary search for a sorted array of floats.
    
    Returns:
    (iterations, upper_bound)
    - iterations: number of steps in the search
    - upper_bound: smallest element >= target (None if target is greater than all elements)
    """
    left = 0
    right = len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            # arr[mid] >= target
            upper_bound = arr[mid]
            right = mid - 1

    return (iterations, upper_bound)


# -------------------------------
# Example usage
# -------------------------------
arr = [0.1, 1.5, 2.3, 3.7, 4.4, 5.9, 6.6]  # sorted array of floats
target = 4.0

iterations, upper_bound = binary_search_upper_bound(arr, target)
print("Iterations:", iterations)
print("Upper bound:", upper_bound)

# Test case where target is higher than all elements
target2 = 10.0
iterations2, upper_bound2 = binary_search_upper_bound(arr, target2)
print("Iterations:", iterations2)
print("Upper bound:", upper_bound2)  # Should print None
