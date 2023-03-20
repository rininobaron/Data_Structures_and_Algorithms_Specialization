var swap = function(array, firstIndex, secondIndex) {
    var temp = array[firstIndex];
    array[firstIndex] = array[secondIndex];
    array[secondIndex] = temp;
};

var indexOfMinimum = function(array, startIndex) {

    var minValue = array[startIndex];
    var minIndex = startIndex;

    for(var i = minIndex + 1; i < array.length; i++) {
        if(array[i] < minValue) {
            minIndex = i;
            minValue = array[i];
        }
    } 
    return minIndex;
};

var selectionSort = function(array) {
    var indexMin;
    for(var i = 0; i < array.length; i++) {
        indexMin = indexOfMinimum(array, i);
        swap(array, i, indexMin);
    }
    return array;
};

var array = [22, 11, 99, 88, 9, 7, 42];
selectionSort(array);
console.log("Array after sorting:  " + array);

//Program.assertEqual(array, [7, 9, 11, 22, 42, 88, 99]);

//var array = [14, 52, 5, 62, 12, 2, 45, 3, 96];
//selectionSort(array);
//Program.assertEqual(array, [2, 3, 5, 12, 14, 45, 52, 62, 96]);