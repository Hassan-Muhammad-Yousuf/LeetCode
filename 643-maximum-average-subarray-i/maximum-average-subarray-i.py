class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cursum = sum(nums[:k])
        maxsum = cursum
        for i in range(k, len(nums)):
            cursum = cursum + nums[i] - nums[i-k]
            maxsum = max(maxsum, cursum)
        return maxsum/k
