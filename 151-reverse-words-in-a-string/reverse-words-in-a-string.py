class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()

        stack = []
        for i in s:
            stack.append(i)
        r_word = ""
        while stack:
            r_word += stack.pop() + " "
        return r_word.strip()