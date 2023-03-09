# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # first we have to check if there is a cycle in a linked list
        
        cycle = False
        
        slow = head
        fast = head
        
        if head == None:
            return None
        
        if head.next == None:
            return None
        
        while (slow != None and fast != None and fast.next!= None and slow.next!=None):
            print('while loop ',slow.val)
            
            if slow.next == None:
                return None
            
            slow = slow.next
            fast = fast.next.next
            #print(slow,fast)
            
            
            if slow == fast:
                print('cycle found fast = slow ')
                cycle = True
                while slow != head:
                    slow = slow.next
                    head = head.next
                print('cycle start at ',slow)
                break
        
        if cycle:
            print('return cycle at :',slow.val)
            return slow
        else:
            return None
                
                
            
        