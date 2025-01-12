class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged = sorted(nums1 + nums2)
        pos = merged[len(merged) // 2]
        return pos if len(merged) % 2 != 0 else (pos + merged[len(merged) // 2 - 1]) / 2