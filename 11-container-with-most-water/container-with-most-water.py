class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_area = 0

        while l < r:
            w = r - l
            min_h = min(height[l],height[r])
            area = w * min_h

            if area > max_area:
                max_area = area

            if height[l] < height[r]:
                l = l + 1
            else:
                r = r - 1
        return max_area


   
            