class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        sort(stones.begin(), stones.end());
        int i, first, second;
        while (stones.size() > 1)
        {
            first = stones.back();
            stones.pop_back();
            second = stones.back();
            stones.pop_back();
            if (first > second) {
                stones.push_back(first - second);
                i = stones.size();
                while (i > 0) {
                    if (stones[i] < stones[i - 1]) {
                        int tmp = stones[i];
                        stones[i] = stones[i - 1];
                        stones[i - 1] = tmp;
                    } else {
                        break;
                    }
                }
            }
        }
        if (stones.size() == 0) {
            return 0;
        }
        return stones[0];
    }
};