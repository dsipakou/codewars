from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1
        left_max = 0
        right_max = 0
        while left < right:
            cur_left = height[left]
            cur_right = height[right]
            print(f"Left: {cur_left}, max_left: {left_max}, right: {cur_right}, max_right: {right_max}")
            if cur_left > left_max or cur_right > right_max:
                local_height = min(height[left], height[right])
                max_area = max(max_area, local_height * (right - left))
                print(f"max_area: {max_area}")
                left_max = max(left_max, height[left])
                right_max = max(right_max, height[right])
            if cur_left < cur_right:
                left += 1
            elif cur_left > cur_right:
                right -= 1
            else:
                if height[left + 1] > height[right - 1]:
                    left += 1
                else: right -= 1
        return max_area



s = Solution()
print(s.maxArea([14,13,12,11,10,9,8,7,6,5,4,3,2,1]))
