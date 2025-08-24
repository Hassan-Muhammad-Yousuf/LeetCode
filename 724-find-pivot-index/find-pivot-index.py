class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = 0
        piv = sum(nums)

        for i in range(len(nums)):
            right = piv - left - nums[i]
            
            if left == right:
                return i
            left = left + nums[i]
        return -1
                