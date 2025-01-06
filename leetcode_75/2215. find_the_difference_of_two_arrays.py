from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        frst_set, sec_set = set(nums1), set(nums2)
        
        return [list(frst_set - sec_set), list(sec_set - frst_set)]
        
        
        
        
Solution().findDifference(nums1 = [1,2,3], nums2 = [2,4,6])