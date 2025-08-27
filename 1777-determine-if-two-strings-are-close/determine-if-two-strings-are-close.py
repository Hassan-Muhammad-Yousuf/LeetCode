class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        count1  = {}
        count2  = {}

        for i in word1:
            if i in count1:
                count1[i] += 1
            else:
                count1[i] = 1
        
        for j in word2:
            if j in count2:
                count2[j] += 1
            else:
                count2[j] = 1
        
        if set(count1.keys()) != set(count2.keys()):
            return False
        if sorted(count1.values()) != sorted(count2.values()):
            return False
        return True

                
