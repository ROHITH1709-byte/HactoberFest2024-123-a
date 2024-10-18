#include <stdio.h>

void reverseArrayExtraArray(int arr[], int size) {
    // Create an array to hold the reversed elements
    int reversedArr[size];
    
    // Reverse the elements
    for (int i = 0; i < size; i++) {
        reversedArr[i] = arr[size - i - 1];
    }

    // Print reversed array
    printf("Reversed Array: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", reversedArr[i]);
    }
    printf("\n"); // New line for better output formatting
}

int main() {
    int originalArr[] = { 1, 2, 3, 4, 5 };
    int size = sizeof(originalArr) / sizeof(originalArr[0]);

    reverseArrayExtraArray(originalArr, size); // Call the function

    return 0; // Indicate successful completion
}
