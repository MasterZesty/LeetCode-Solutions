# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        no_of_paths = 0
        
        stack = [(root,0)]
        
        while stack:
            
            node, path = stack.pop()
            
            if node:
                
                # print(f"{node.val}")
                path ^= 1 << node.val # still confuesed how we come up with this
                
                if not node.left and not node.right:
                    # print(f"leaf node : {node.val}")
                    if path & (path - 1) == 0: # and this
                        no_of_paths += 1
                    
                else:
                    stack.append( (node.left, path) )
                    stack.append( (node.right, path) )
                    
                    
        return no_of_paths