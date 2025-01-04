from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_average = 0
        cur_sum = 0
        n = len(nums)
        
        for i in range(k):
            cur_sum += nums[i]
            
        max_average = cur_sum / k
        
        for j in range(k, n):
            cur_sum += nums[j]
            cur_sum -= nums[j - k]
            
            avg = cur_sum / k
            max_average = max(max_average, avg)
        
        return max_average
        
Solution().findMaxAverage(nums =[1,12,-5,-6,50,3], k =4)