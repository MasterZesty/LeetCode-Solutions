# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        mid = 0
        
        next = head
        n = 1
        while next.next:
            n += 1
            next = next.next
            
        mid = n //2
        
        # print(f"n: {n} | mid: {mid}")
        
        next = head
        while next.next:
            if mid == 1:
                return next.next
            next = next.next
            mid -= 1
            
        return head