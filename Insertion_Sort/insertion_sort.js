
function insertionSort(arr) {
    for (var i = 1; i < arr.length; i++) {
        var key = arr[i];
        for (var j = i - 1; j > 0; j--) {
            if (arr[j] > key) {
                arr[j+1] = arr[j];
            } else {
                break;
            }
        }
        arr[j+1] = key;
    }
    
    console.log(arr);
}

insertionSort([1,5,68,7,2])
