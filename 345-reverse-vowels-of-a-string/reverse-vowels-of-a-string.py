class Solution:
    def reverseVowels(self, s: str) -> str:
        v = 'aeiouAEIOU'
        s = list(s)
        l, r = 0 ,len(s) - 1
        while l < r:
            if s[l] not in v:
                l += 1
                continue
            if s[r] not in v:
                r -= 1
                continue
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return "".join(s)