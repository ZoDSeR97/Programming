/**
   * Reverse a given array
   * - Time: O(n).
   * - Space: O(1).
   * @param {Array} arr
   * @returns {Array} in reverse order.
   */
function isPalindrome(arr) {
    for (var i = 0; i < str.length / 2; i++)
        temp = arr[i];
        arr[i] = arr[arr.length-1-i];
        arr[arr.length-1-i] = temp;
    return arr;
}