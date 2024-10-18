def binary_search(array, target):
    left, right = 0, len(array) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if array[mid] == target:
            return mid  # Return the index where the target is found
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Return -1 if the target is not found

# Example usage
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
index = binary_search(array, target)

if index != -1:
    print("Element found at index:", index)
else:
    print("Element not found")
