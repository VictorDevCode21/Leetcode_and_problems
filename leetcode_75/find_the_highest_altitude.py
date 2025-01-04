from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        max_alt = 0
        gain.insert(0,0)
        p = [0] * (n + 1) 
        p[0] = gain[0]
        
        for i in range(1, n + 1):
            p[i] = p[i - 1] + gain[i]
            if p[i] > max_alt:
                max_alt = p[i]
        
        return max_alt
        
Solution().largestAltitude(gain = [44,32,-9,52,23,-50,50,33,-84,47,-14,84,36,-62,37,81,-36,-85,-39,67,-63,64,-47,95,91,-40,65,67,92,-28,97,100,81])