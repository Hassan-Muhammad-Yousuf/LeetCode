class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r = [i for i,j in enumerate(senate) if j == 'R']
        d = [i for i,j in enumerate(senate) if j == 'D']
        n = len(senate)

        while r and d:
            r_index = r.pop(0)
            d_index = d.pop(0)
            
            if r_index < d_index:
                r.append(r_index+n)
            else:
                d.append(d_index+n)

        if r:
            return "Radiant"
        else:
            return "Dire"


                
              
       
    

       
            