class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        l = {}
        ans = 0

        for i in range(len(nums)):
            w = k - nums[i]
            if w in l and l[w] > 0:
                ans += 1
                l[w] -= 1
            else:
                l[nums[i]] = l.get(nums[i], 0) + 1
            
        return ans