class Solution:
    def removeStars(self, s: str) -> str:
        #record the str 
        results = []
        for i in s:
        #finding stars in the str
            if i == '*':
                results.pop()
            else:
                results.append(i)

        #remove the stars alongwith left char of the str

        return "".join(results)