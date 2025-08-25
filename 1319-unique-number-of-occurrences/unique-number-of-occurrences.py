class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}

        for i in arr:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1

        seen = set()
        for j in freq.values():
            if j in seen:
                return False
            else:
                seen.add(j)
        
        return True