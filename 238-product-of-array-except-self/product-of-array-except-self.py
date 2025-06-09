class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n

        l_pr = 1
        for i in range(n):
            ans[i] = l_pr
            l_pr *= nums[i]
        r_pr = 1
        for i in range(n-1, -1, -1):
            ans[i] = ans[i] * r_pr
            r_pr *= nums[i]
        return ans