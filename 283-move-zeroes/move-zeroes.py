class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[n] = nums[i]
                n += 1
        for j in range(n, len(nums)):
            nums[j] = 0