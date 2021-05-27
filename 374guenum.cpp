/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is lower than the guess number
 *			      1 if num is higher than the guess number
 *               otherwise return 0
 * int guess(int num);
 */

class Solution {
public:
    int guessNumber(int n) {
        int right = n;
        int left = 0;
        while (true) {
            int pivot = left + ((right - left) / 2);
            int res = guess(pivot);
            if (res == 0) {
                return pivot;
            } else if (res == 1) {
                left = pivot + 1;
            } else {
                right = pivot - 1;
            }
        }
    }
};
