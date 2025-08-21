class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vol = set("aeiou")
        count = 0
        max_vol = 0

        for ch in range(k):
            if s[ch] in vol:
                count += 1

        max_vol = count

        for i in range(k, len(s)):
            if s[i] in vol:
                count += 1
            if s[i-k] in vol:
                count -= 1
                
            max_vol = max(max_vol, count)
        return max_vol
