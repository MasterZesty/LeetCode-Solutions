# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    def check_mirror(self,left,right):
        
        if (not left and not right):
            return True
        
        if (not left or not right):
            return False
        
        c1 = self.check_mirror(left.left,right.right)
        c2 = self.check_mirror(left.right,right.left)
        
        return ( (left.val == right.val) and (c1 and c2) )
    
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        return self.check_mirror(root.left,root.right)
        
