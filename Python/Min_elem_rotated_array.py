def find_min_in_rotated_array(arr):
    low = 0
    high = len(arr) - 1

    # If the array is not rotated (or empty)
    if not arr or arr[low] <= arr[high]:
        return arr[low] if arr else None  # Return None for empty array

    while low <= high:
        mid = (low + high) // 2

        # Check if mid is the minimum element
        if mid > 0 and arr[mid] < arr[mid - 1]:
            return arr[mid]

        # Check if the next element is the minimum
        if mid < len(arr) - 1 and arr[mid] > arr[mid + 1]:
            return arr[mid + 1]

        # Decide which half to continue searching
        if arr[mid] >= arr[low]:
            low = mid + 1  # Move to the right half
        else:
            high = mid - 1  # Move to the left half

    return None  # Should not reach here if the input is valid

# Example usage
rotated_array = [4, 5, 6, 7, 0, 1, 2]
min_element = find_min_in_rotated_array(rotated_array)
print("The minimum element is:", min_element)
