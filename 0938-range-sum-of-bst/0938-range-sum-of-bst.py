# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        global sum_bst
        sum_bst = 0
        
        def bst_traversal(node, low, high):
            global sum_bst
            
            if node is None:
                return
            
            if node.val >= low and node.val <= high:
                # print(f"node val : {node.val} | {sum_bst}")
                sum_bst += node.val
            
            if node.left is not None:
                bst_traversal(node.left, low, high)
                
            if node.right is not None:
                bst_traversal(node.right, low, high)
        
        
        bst_traversal(root, low, high)
        
        return sum_bst