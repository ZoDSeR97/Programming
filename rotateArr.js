/**
   * Takes in an array and a number of steps to shift the values to the **right** by. 
   * Then wrap-around any values to that shift off array's end to the other side so no data is lost.
   * Example Function Call: rotateArray(arr, 2)
   * Expected Output: [3, 4, 1, 2]
   * - Time: O(n).
   * - Space: O(1).
   * @param {Array} arr, @param {Int} shiftBy
   * @returns {Array} shifted by specific steps.
   */

function rotateArray(arr, shiftBy) {
    // Code Here ＼(ﾟｰﾟ＼)
    left = false;
    if(shiftBy < 0){
        shiftBy *= -1 // shiftby = shiftby *-1
        left = true;
    }
    for (var i = 0; i<shiftBy;i++)
        if (!left)
            arr.unshift(arr.pop());
        else
            arr.push(arr.shift());

    return arr;
}