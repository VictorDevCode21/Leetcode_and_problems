from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        l = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[l] = nums[l], nums[i]
                l +=1
        
        return nums
        
Solution().moveZeroes(nums = [0,1,0,3,12])