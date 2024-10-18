#include <stdio.h>
#include <stdlib.h> // Include stdlib for malloc and free

void reverseArrayExtraArray(int arr[], int size) {
    // Allocate memory for the reversed array
    int* reversedArr = (int*)malloc(size * sizeof(int)); // Dynamically allocate memory
    if (reversedArr == NULL) {
        printf("Memory allocation failed!\n");
        return;
    }

    for (int i = 0; i < size; i++) {
        reversedArr[i] = arr[size - i - 1]; // Reverse the elements
    }

    // Print reversed array
    printf("Reversed Array: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", reversedArr[i]); // Print each element
    }
    printf("\n"); // New line for better output formatting

    free(reversedArr); // Free the allocated memory
}

int main() {
    int originalArr[] = { 1, 2, 3, 4, 5 };
    int size = sizeof(originalArr) / sizeof(originalArr[0]);

    reverseArrayExtraArray(originalArr, size); // Call the function

    return 0; // Indicate successful completion
}
