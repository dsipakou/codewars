/**
 * @param {number} numBottles
 * @param {number} numExchange
 * @return {number}
 */
var numWaterBottles = function(numBottles, numExchange) {
    let output = numBottles
    while (numBottles >= numExchange) {
        output += (numBottles - numBottles % numExchange) / numExchange
        numBottles = (numBottles - numBottles % numExchange) / numExchange + numBottles % numExchange
        console.log(numBottles)
    }
    return output
};
