from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
#     def __str__(self):
#         result = []
#         current = self 
#         while current:
#             result.append(str(current.val))
#             current = current.next 
            
#         return " -> ".join(result)
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        prev, current = None, head 
        
        while current:
            temp = current.next 
            current.next = prev 
            prev = current
            current = temp
        
        return prev
        

Solution().reverseList(head = [1,2,3,4,5])