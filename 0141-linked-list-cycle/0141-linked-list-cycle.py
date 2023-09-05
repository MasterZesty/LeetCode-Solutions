# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Approch 1 : Floyd’s Cycle Finding Algorithm - Floyd’s cycle finding algorithm 
        # or Hare-Tortoise algorithm is a pointer algorithm that uses only two pointers, 
        # moving through the sequence at different speeds. This algorithm is used to find 
        # a loop in a linked list. It uses two pointers one moving twice as fast as the 
        # other one. The faster one is called the fast pointer and the other one is called 
        #the slow pointer.
        # ref : https://www.geeksforgeeks.org/floyds-cycle-finding-algorithm/
        
        slowptr = head
        fastptr = head
        
        while (slowptr != None and fastptr != None and fastptr.next != None):
            slowptr = slowptr.next
            fastptr = fastptr.next.next
            
            if slowptr == fastptr:
                return True
            
        return False
    
    
        # Approch 2 : store node/node address in hashset and if it come again 
        # then loop in the ll
            