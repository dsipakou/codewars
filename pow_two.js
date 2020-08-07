/**
 * @param {number} num
 * @return {boolean}
 */
var isPowerOfFour = function(num) {
    let index = 1;
    if (num === 1) {
        return true
    }
    let currentNumber = 4;
    while (currentNumber < num) {
        currentNumber *= 4;
    }
    return currentNumber === num;
        
};
