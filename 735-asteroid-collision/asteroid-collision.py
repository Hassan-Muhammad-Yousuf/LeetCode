class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # stack to store the results

        results = []
        # iterate the list
        for i in asteroids:
        # find the positions of the asteroids
            while results and results[-1] > 0 and i < 0:
                if results[-1] + i < 0:
                    results.pop()
                elif results[-1] + i > 0:
                    break
                else:
                    results.pop()
                    break
            else:
                results.append(i)

        return results
        
        # return remaning asteroids 
        return results