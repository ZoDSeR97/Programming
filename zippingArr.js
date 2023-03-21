/**
   * Converts the given arrays of keys and values into an object.
   * - Time: O(n).
   * - Space: O(n).
   * @param {Array<string>} keys
   * @param {Array<any>} values
   * @returns {Object} The object with the given keys and values.
   */
function zipArraysIntoMap(keys, values) {
    res = {};
    for (var i = 0; i < keys.length; i++)
        res[keys[i]] = values[i];
    return res;
}