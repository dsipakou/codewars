/**
 * @param {character[]} tasks
 * @param {number} n
 * @return {number}
 */
var leastInterval = function(tasks, n) {
    let counts = {};
    let curMax = 0;
    for (let i in tasks) {
        counts[tasks[i]] = counts[tasks[i]] ? counts[tasks[i]] + 1 : 1;
        curMax = Math.max(curMax, counts[tasks[i]])
    }
    return curMax + (curMax - 1) * n
};
