/**
 * Encodes the given string such that duplicate characters appear once followed
 * by a number representing how many times the char occurs. Only encode strings
 * when the result yields a shorter length.
 * - Time: O(n).
 * - Space: O(n).
 * @param {string} str The string to encode.
 * @returns {string} The given string encoded.
 */
function encodeStr(str){
    var shortStr = str[0]
    count = 1
    for(var i = 1; i < str.length; i++){
        if (shortStr[shortStr.length-1] != str[i]){
            shortStr+=count+str[i];
            count = 0;
        }
        count++;
    }
    shortStr+=count;
    if (shortStr.length < str.length)
        return shortStr;
    return str;
}