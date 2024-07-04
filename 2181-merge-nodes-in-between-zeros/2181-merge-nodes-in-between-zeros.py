# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        currnode = head
        
        while currnode:
            
            # print(f"nodeval:{currnode.val}")
            
            currmerge = 0
            tnode = currnode
            
            if currnode.val == 0:
                currnode = currnode.next
            
            while currnode.val != 0 and currnode:
                currmerge += currnode.val
                currnode = currnode.next
            
            # print(f"currmerge: {currmerge}")
            
            tnode.val = currmerge
            tnode.next = currnode.next
            
            currnode = currnode.next

        # print(f"head: {head}")
        return head
        