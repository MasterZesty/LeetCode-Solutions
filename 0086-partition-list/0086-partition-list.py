# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
#         ll_1 = None
        
#         ll_2 = None
        
#         ptr = head
#         while ptr != None:
#             # print(ptr.val, ' -> ',end='')
            
#             if ptr.val < x:
#                 # print('val is < x')
#                 node = ListNode(ptr.val,None)
#                 if ll_1 is None:
#                     # print("ll_1 got first node with val ",node.val,ll_1)
#                     ll_1 = node
#                 else:
#                     # print("ll_1 got subsequent another node with val ",node.val,ll_1)

#                     last = ll_1
#                     while last.next is not None:
#                         last = last.next
                    
#                     last.next = node
                
#             if ptr.val >= x:
#                 # print('val is > x')
#                 node = ListNode(ptr.val,None)
#                 if ll_2 is None:
#                     # print("ll_1 got first node with val ",node.val,ll_1)
#                     ll_2 = node
#                 else:
#                     # print("ll_1 got subsequent another node with val ",node.val,ll_1)

#                     last = ll_2
#                     while last.next is not None:
#                         last = last.next
                    
#                     last.next = node
                
#             # print(ll_1)
#             # print(ll_2)

#             ptr = ptr.next

        
#         #print("print ll_1 : ",ll_1)
#         #print("print ll_2 : ",ll_2)

# #         ptr = ll_1
# #         while ptr != None:
# #             print(ptr.val, ' -> ',end='')
# #             ptr = ptr.next
            
# #         print()
        
# #         ptr = ll_2
# #         while ptr != None:
# #             print(ptr.val, ' -> ',end='')
# #             ptr = ptr.next

#         # if list is empty and l1 and l2 are empty
#         if ll_1 == None:
#             if ll_2== None:
#                 return ListNode(0)
            
#         if ll_2 == None:
#             if ll_1== None:
#                 return ListNode(0)

#         # if ll contain all elements > x such that only ll_2 is filled
#         if ll_1 == None:
#             if ll_2 != None:
#                 return ll_2
            
#         # if ll contain all elements < x such that only ll_1 is filled        
#         if ll_2 == None:
#             if ll_2 != None:
#                 return ll_1
        
    
#         # otherwise joins two list
#         ptr = ll_1
#         while ptr.next != None:
#             ptr = ptr.next

#         ptr.next = ll_2
            
#         # print final LL
#         # ptr = ll_1
#         # while ptr != None:
#         #     print(ptr.val, ' -> ',end='')
#         #     ptr = ptr.next
            
        
        
#         return ll_1
        
        d1=c1=ListNode(0)
        d2=c2=ListNode(0)
        while head:
            if head.val<x:
                d1.next=head
                d1=d1.next

            else:
                d2.next=head
                d2=d2.next    

            head=head.next

        d2.next=None
        d1.next=c2.next
        return c1.next    