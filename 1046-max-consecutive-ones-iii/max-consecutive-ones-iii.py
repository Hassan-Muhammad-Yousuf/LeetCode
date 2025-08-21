class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
      n_w = 0
      n_z = 0
      l = len(nums)
      n = 0

      for i in range(l):
        if nums[i] == 0:
            n_z += 1
        while n_z > k:
            if nums[n_w] == 0:
                n_z -= 1
            n_w +=1
        n = max(n, i - n_w + 1)
      return n

