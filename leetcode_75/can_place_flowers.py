from typing import List






class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        
        for i in range(0, len(flowerbed), 1 ):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0 )  and ((i == len(flowerbed) -1)  or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                count+=1
                
        return count >= n
        
            
            

Solution().canPlaceFlowers(flowerbed = [0,0,1,0,1], n = 1 )