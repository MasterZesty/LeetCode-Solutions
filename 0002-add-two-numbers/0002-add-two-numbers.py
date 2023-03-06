# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr_l1 = l1
        num1 = ''
        while curr_l1 != None:
            print(curr_l1.val)
            num1 = str(curr_l1.val) + num1
            curr_l1 = curr_l1.next
            
        #print('num1:',num1)
        
        curr_l2 = l2
        num2 = ''
        while curr_l2 != None:
            print(curr_l2.val)
            num2 = str(curr_l2.val) + num2
            curr_l2 = curr_l2.next
            
        #print('num2', num2)
        
        sum = str(int(num1) + int(num2))[::-1]
        #print('sum rev',sum)
        
        ll = ListNode(int(sum[0]))
        curr = ll
        
        for i,val in enumerate(sum):
            if i != 0:
                node = ListNode(int(val))
                curr.next = node
                curr = node
                
            
        return ll
        
        
        
        