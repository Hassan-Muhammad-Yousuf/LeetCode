class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rc = defaultdict(int)
        c = 0

        for row in grid:
            rc[tuple(row)] += 1

        for col in zip(*grid):
            c += rc[col]

        return c
        
       