/**
 * Rotates a given string's characters to the right by the given amount,
 * wrapping characters to the beginning.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @param {number} amnt The amount of characters in the given str to rotate to the
 *    right.
 * @returns {string} The string rotated by the given amount.
 */
function LrotateStr(str, amnt) {
    newStr = ""
    amnt = amnt % str.length;
    if (amnt == 0)
        return str;
    for (var i = 0; i < str.length; i++)
        newStr += str[(i + amnt) % str.length];
    return newStr;
}
function RrotateStr(str, amnt) {
    newStr = ""
    amnt = amnt % str.length;
    if (amnt == 0)
        return str;
    for (var i = 0; i < str.length; i++)
        newStr += str[(i+(str.length-amnt))%str.length];
    return newStr;
}

str = "Hello World"
num = 1

console.log(LrotateStr(str, num))
console.log(RrotateStr(str, num))