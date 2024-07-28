function mergeSort(arr, start, end) {
    // exit if end >= start
    if (end <= start) return;
    // caluclate midpoint
    var midpoint = Math.floor((start + end) / 2);
    // mergeSort(arr, midpoint)
    mergeSort(arr, start, midpoint);
    // mergeSort(midpoint + 1, end)
    mergeSort(arr, midpoint + 1, end);
    // merge(arr, start, midpoint, end)
    merge(arr, start, midpoint, end);
}

function merge(arr, start, midpoint, end) {
    let i,j;
    let k;
    let left_length = midpoint - start + 1;
    let right_length = end - midpoint;
    
    // create two arrays
    let left_array = [];
    let right_array = [];
    
    // fill the two arrays with values
    for (i = 0; i < left_length; i++){
        left_array[i] = arr[start + i];
    }
    
    for (j = 0; j < right_length; j++) {
        right_array[j] = arr[midpoint + 1 + j];
    }
    
    // compare and sort
     i = 0;
     j = 0;
     k = start;
    while(i < left_length && j < right_length) {
        if (left_array[i] <= right_array[j]){
            arr[k] = left_array[i]
            i++;
        } else {
            arr[k] = right_array[j]
            j++;
        }
        k++;
    }
    
    // move remain items
    while (i < left_length) {
        arr[k] = left_array[i]
        i++;
        k++;
    }
    
    while (j < right_length) {
        arr[k] = right_array[j]
        j++;
        k++;
    }
}

let arr = [8,6,5,61,45,48];
console.log(arr);
mergeSort(arr, 0, arr.length - 1);
console.log(arr);


