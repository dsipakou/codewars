class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        l1 = 0
        l2 = 0
        while l1 < len(nums1) and l2 < len(nums2):
            if nums1[l1] >= nums2[l2]:
                for i in range(len(nums1) - 1, l1, -1):
                    nums1[i] = nums1[i - 1]
                nums1[l1] = nums2[l2]
                l2 += 1
            elif nums1[l1] == 0:
                nums1[l1] = nums2[l2]
                l2 += 1
            else:
                l1 += 1
        return nums1
