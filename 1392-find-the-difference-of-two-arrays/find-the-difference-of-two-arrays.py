class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        arr1 = set(nums1)
        arr2 = set(nums2)

        r1 = arr1 - arr2
        r2 = arr2 - arr1

        return [list(r1), list(r2)]