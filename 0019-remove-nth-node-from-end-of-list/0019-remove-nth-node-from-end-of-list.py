# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Calculate the length of the linked list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        # Calculate the position of the node to be removed
        target_position = length - n

        # If the target position is the first node, remove the head
        if target_position == 0:
            return head.next

        # Traverse the list to the node before the target node
        current = head
        for _ in range(target_position - 1):
            current = current.next

        # Remove the target node
        current.next = current.next.next

        return head
            