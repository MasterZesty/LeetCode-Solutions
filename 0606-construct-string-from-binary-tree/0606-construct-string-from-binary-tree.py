# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        res = []
        
        def preorder(node,res):
            
            if node is None:
                return
            
            print(f"node val is {node.val}")
            res.append(str(node.val))
            
            if node.left is None and node.right is None:
                return
            
            res.append("(")
            preorder(node.left,res)
            res.append(")")
            
            # study example 2 for if logic
            if node.right is not None:
                res.append("(")
                preorder(node.right,res)
                res.append(")")
            
        preorder(root, res)
        
        print(res)
        
        ans = ''.join(res)
        
        
        return ans
            
    
    
    
    