class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')

        for j in nums:
       
            if j <= first:
                first = j
            elif j <= second:
                second = j
            else:
                return True
        return False
        