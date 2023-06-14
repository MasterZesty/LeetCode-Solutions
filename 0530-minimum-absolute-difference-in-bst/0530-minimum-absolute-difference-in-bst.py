# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # Inorder Tree Traversal - it will give node in non
        # decrsing order
        nodes = []
        ans = 1e9
        
        def inorder_dfs(node):

            if node:
                
                inorder_dfs(node.left)

                #print(f'value : {node.val}')
                nodes.append(node.val)

                inorder_dfs(node.right)
                
        inorder_dfs(root)
        
        
        for i in range(1,len(nodes)):
            ans = min(ans,nodes[i]-nodes[i-1])
            
        
        return ans