def findMaxSubCubeSum(matrix, M, N, O):
    # Initialize the maximum sum to the smallest possible integer
    maxSum = -(1 << 60)

    # Iterate over the first dimension of the 3D array
    for i in range(M):
        # Initialize a 2D temporary array to store intermediate sums
        temp = [[0] * O for _ in range(N)]

        # Iterate over the first dimension again
        for j in range(i, M):
            # Update the temp array with the current 2D slice
            for k in range(N):
                for l in range(O):
                    temp[k][l] += matrix[j][k][l]

            # Now we will apply Kadane's algorithm on the 2D temp array
            for k in range(N):
                # This will hold the sum of columns
                kadane_array = [0] * O
                
                for l in range(k, N):
                    # Add the current row to the kadane_array
                    for m in range(O):
                        kadane_array[m] += temp[l][m]

                    # Apply 1D Kadane's algorithm on the kadane_array
                    current_sum = 0
                    for value in kadane_array:
                        current_sum += value
                        if current_sum > maxSum:
                            maxSum = current_sum
                        if current_sum < 0:
                            current_sum = 0

    # Return the maximum sum found
    return maxSum

# Example inputs
M = 3
N = 3
O = 3
matrix = [
    [[-1, -2, 3], [-4, -5, 6], [7, 8, 9]],
    [[-9, -8, 7], [-6, -5, 4], [3, 2, 1]],
    [[-1, -3, 5], [-7, -9, 2], [4, 6, 8]]
]

# Call the function to find the maximum sum of a sub-cube in the 3D array
result = findMaxSubCubeSum(matrix, M, N, O)

# Output the result
print("The maximum sum of a sub-cube in the 3D array is:", result)
