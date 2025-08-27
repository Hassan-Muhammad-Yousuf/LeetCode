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
        freq1 = {}
        freq2 = {}

        for f1 in count1.values():
            if f1 in freq1:
                freq1[f1] += 1
            else:
                freq1[f1] = 1

        for f2 in count2.values():
            if f2 in freq2:
                freq2[f2] += 1
            else:
                freq2[f2] = 1

        if freq1 != freq2:
            return False

        return True

                
