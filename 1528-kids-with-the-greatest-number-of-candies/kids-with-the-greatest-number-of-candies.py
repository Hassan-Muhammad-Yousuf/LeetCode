class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = max(candies)
        output = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= n: 
                output.append(True)
            else:
                output.append(False)
        return output 