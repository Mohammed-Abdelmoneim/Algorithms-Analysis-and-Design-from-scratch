// Online C compiler to run C program online
#include <stdio.h>
#include <stdlib.h>

// merge function declaration
void merge(int array[], int start, int mid, int end);

void segregate(int array[], int start, int end) {
    // This will be recursion like MergeSort algo
    // The base case
    if (end <= start)
        return;
    int mid = (start + end) / 2;
    segregate(array, start, mid);
    segregate(array, mid + 1, end);
    merge(array, start, mid, end);
}
void merge(int array[], int start, int mid, int end){
    int i, j, k;
    // Lengths of the left and right subarrays
    int left_length = mid - start + 1;
    int right_length = end - mid;
    
    // Allocate memory for the left and right subarrays
    int *left_array = (int *)malloc(left_length * sizeof(int));
    int *right_array = (int *)malloc(right_length * sizeof(int));
    
    
    // fill the arrays
    // Copy data to the left subarray
    for (i = 0; i < left_length; i++){
        left_array[i] = array[start + i];
    }
    
    // Copy data to the right subarray
    for (j = 0; j < right_length; j++){
        right_array[j] = array[mid + 1 + j];
    }
    i = 0; // Index for left subarray
    j = 0; // Index for right subarray
    k = start; // Index for the original array
    
    // Merge elements from the left and right subarrays into the original array
    while(i < left_length && left_array[i] <= 0) {
        array[k] = left_array[i];
        i++;
        k++;
    }
    while(j < right_length && right_array[j] <= 0) {
        array[k] = right_array[j];
        j++;
        k++;
    }
    
    // Copy remaining elements from the left subarray, if any
    while(i < left_length){
        array[k] = left_array[i];
        i++;
        k++;
    }
    
    // Copy remaining elements from the right subarray, if any
    while(j < right_length){
        array[k] = right_array[j];
        j++;
        k++;
    }
    
    // Free the dynamically allocated memory
    free(left_array);
    free(right_array);
}
int main() {
    int array[] = {7,-6,-8,6,-19,5,-1,12};
    // Calculate the number of elements in the array
    int size = sizeof(array) / sizeof(array[0]);
    for (int i = 0; i < size; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");
    
    segregate(array, 0, size - 1);
    
    for (int i = 0; i < size; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");
    return 0;
}

// The best solution is not always the one with the best complexity class.
// The most convenient solution is not always the one with the best complexity class.
