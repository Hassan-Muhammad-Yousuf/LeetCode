class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        nums = ""

        for i in s:
            if i.isdigit():
                nums += i

            elif i == '[':
                stack.append(int(nums))
                stack.append('[')
                nums = ""
            elif i == ']':
                substr = ""
                while stack and stack[-1] != '[':
                    substr = stack.pop() + substr
                stack.pop()

                mul = stack.pop()
                expanded = substr * mul
                stack.append(expanded)

            else:
                stack.append(i)
        return "".join(stack)
                