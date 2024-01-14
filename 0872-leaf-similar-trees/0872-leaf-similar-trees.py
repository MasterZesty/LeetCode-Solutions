# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def dfs(node, s):
            
            if node is None:
                return s
            
            # print(f" {node.val} ")
            if not node.left and not node.right:
                s = s + "_" + str(node.val)
                # print(f"leaf node: {node.val}")
            
            if node.left is not None:
                s = dfs(node.left, s)
                
            if node.right is not None:
                s = dfs(node.right, s)
            
            return s
        
        s1 = dfs(root1, "")
        s2 = dfs(root2, "")
        print(s1, s2)
        
        return (s1 == s2 )