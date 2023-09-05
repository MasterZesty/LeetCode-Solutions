"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
#         # print(f'{head.val} - >')
        
#         # create new deep copy link list without that random attrb
#         travptr = head.next
#         newllhead = Node(head.val)
#         newlltail = newllhead
#         while travptr != None:
#             # print(f'{travptr.val} - >')
#             new_node = Node(travptr.val)
#             newlltail.next = new_node
#             newlltail = newlltail.next
#             travptr = travptr.next
            
#         # print new linked list without random attrb
#         t = newllhead
#         while t != None:
#             print(f'{t.val} - >')
#             t = t.next
            
#         # add that random to new list
        
            
#         return newllhead
    
        if not head:
            return None

        # Step 1: Create a new node for each node in the old linked list and store them in a hashmap.
        old_to_new = {}
        current = head
        while current:
            new_node = Node(current.val)
            old_to_new[current] = new_node
            current = current.next

        # Step 2: Iterate through the old linked list again and update the next and random pointers of the new nodes.
        current = head
        while current:
            if current.next:
                old_to_new[current].next = old_to_new[current.next]
            if current.random:
                old_to_new[current].random = old_to_new[current.random]
            current = current.next

        # The new head is the node corresponding to the old head.
        new_head = old_to_new[head]

        return new_head