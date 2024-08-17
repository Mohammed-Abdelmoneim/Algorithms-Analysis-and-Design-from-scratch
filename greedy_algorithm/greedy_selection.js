function greedy_selection(start, end) {
    // Initialize the result array with the first element (so greedy!)
    result = [0];
    i = 0; // Index for the start array
    j = 1; // Index for the end array
    
    // Iterate through the start array
    for (; i < start.length; i++) {
        // Check if the current start time is greater than or equal to the current end time
        // In case of session selection, check if the next session will start after the previous session ends
        if (start[i] >= end[j]){
            // Add the current index to the result array
            result.push(i);
            // Update the end pointer to the current index
            j = i;
        }
    }
    
    // Return the result array containing selected indices
    return result;
}

// Test our code, result should be [0, 2, 3, 5]
s = [9, 10, 11, 12, 13, 15];
e = [11, 11, 12, 14, 15, 16];
console.log(greedy_selection(s,e));
