# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        left = 1
        right = n
        while left < right:
            pivot = left + (right - left) // 2
            if isBadVersion(pivot) is True:
                right = pivot
            else:
                left = pivot + 1
        return right
