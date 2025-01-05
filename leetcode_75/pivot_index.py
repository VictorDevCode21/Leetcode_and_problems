from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pivot_index = -1
        n= len(nums)
        left_sum = 0
        right_sum = 0
        total_sum = sum(nums)
        
        
        p = [0] * n
        p[0] = nums[0]
        
        for i in range(0, n):
            p[i] = p[i - 1] + nums[i]
            
            if i > 0:
                left_sum = p[i - 1]
            else: 
                left_sum = 0
            
            right_sum = total_sum - left_sum - nums[i]
            
            if right_sum == left_sum:
                pivot_index = i 
                break
                
        return pivot_index
        
        
        
        
Solution().pivotIndex(nums = [4])