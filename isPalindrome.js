/**
   * Determines if the given str is a palindrome (same forwards and backwards).
   * - Time: O(n).
   * - Space: O(1).
   * @param {string} str
   * @returns {boolean} Whether the given str is a palindrome or not.
   */
function isPalindrome(str) {
    for (var i = 0; i < str.length / 2; i++)
        if (str[i] != str[str.length - 1 - i])
            return false
    return true
}