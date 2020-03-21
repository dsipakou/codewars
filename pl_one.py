class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index = 0
        store = 0
        while index < len(digits):
            current_index = -index - 1
            if digits[current_index] == 9:
                digits[current_index] = 0
                store = 1
            elif store == 1:
                digits[current_index] += 1
                store = 0
                break
            else:
                digits[current_index] += 1
                break
            index += 1
        if store == 1:
            return [1] + digits
        return digits
