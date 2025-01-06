from typing import List 

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = {}
        values = set()
        answer = True
        
        for i in arr:
            count[i] = count.get(i, 0) + 1
            
        for j in count.values():
            if j in values:
                answer = False
                break
            else:
                values.add(j)
            
        return answer
            
            
        
Solution().uniqueOccurrences(arr = [-3,0,1,-3,1,1,1,-3,10,0])