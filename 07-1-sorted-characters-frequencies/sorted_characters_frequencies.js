// function with ASCII code using array
function ASCIIMethod(text){
    console.log("ASCIIMethod");
    
    // create new array and fill it with zeros
    let freq = new Array(128).fill(0);

    // loop over the 'text' and convert each letter into ascii 
    for(i = 0; i < text.length; i++){
        let current_code = text.charCodeAt(i);
        freq[current_code]++;
    }
    
    // printing the result
    for(i = 0; i < freq.length; i++){
        if (freq[i] > 0){
            // converting from ascii into letter
            let char = String.fromCharCode(i);
            console.log(char + ' -> ' + freq[i]);
        }
    }
}

// function with UTF-8 using object
function anyCodeMethod(text){
    console.log("anyCodeMethod");
    
    let freq = {};
    
    for(i = 0; i <text.length; i++){
        // if the char isn't exist, create it.
        if(freq[text[i]] == null){
           freq[text[i]] = 1; 
        } else {
            freq[text[i]] += 1; 
        }
    }
    
    let freqArr = Object.entries(freq);
    
    sort(freqArr, 0, freqArr.length - 1)
    
    for (let [key, val] of freqArr) {
        console.log(key + ' -> ' + val);
    }
}

// merge sort function to sort the result
function sort(arr, start, end){
    if (end <= start) return;
    let mid = Math.floor((end + start) / 2);
    sort(arr, start, mid);
    sort(arr, mid + 1, end);
    merge(arr, start, mid, end);
}

function merge(arr, start, mid, end){
    let left_length = mid - start + 1;
    let right_length = end - mid;
    
    let left_array = []
    let right_array = []
    
    // fill
    for (let i=0; i < left_length; i++){
        left_array[i] = arr[start + i]
    }
    
    for (let j=0; j < right_length; j++){
        right_array[j] = arr[mid + 1 + j]
    }
    
    let i=0;
    let j=0;
    let k = start;
    
    while (i < left_length && j < right_length){
        if (left_array[i][1] <= right_array[j][1]){
            arr[k] = left_array[i]
            i++;
        } else {
            arr[k] = right_array[j]
            j++;
        }
        k++;
    }
    
    while(i < left_length) {
        arr[k] = left_array[i]
        i++;
        k++;
    }
    while(j < right_length) {
        arr[k] = right_array[j]
        j++;
        k++;
    }
}
// Tests 
ASCIIMethod('mohammed abdelmoneim')
console.log("________________________")
anyCodeMethod('mohammed abdelmoneim')
