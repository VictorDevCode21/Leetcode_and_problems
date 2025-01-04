from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_number = 0
        output = []
        
        for i in candies:
            if i > max_number:
                max_number = i
            
        
        for i in candies:
            if i + extraCandies >= max_number:
                output.append(True)
            else:
                output.append(False)
        return output
        
        
Solution().kidsWithCandies(candies = [4,2,1,1,2], extraCandies= 1)