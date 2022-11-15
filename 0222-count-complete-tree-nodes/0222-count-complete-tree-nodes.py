# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        # print(root.right,root.left,root.val,sep='\n')
        
        global count
        
        count = 0
        
        if root == None:
            return 0
        
        # helper function
        def ret_no_nodes(node):
            
            global count
            
            if node == None:
                # print("Error Node ",node)
                return 0
            
            # base case
            if node.left == None and node.right== None:
                print(node.val,end=' ')
                count += 1
                # print("count",count)
                return 1
            
            #i am not aware but it is left root right - inorder traversal maybe
            
            # call on left nodes
            # print("left nodes")
            ret_no_nodes(node.left)
            
            # print(node.val,end=' ')
            count += 1
            
            # call on right nodes
            # print("right nodes")
            ret_no_nodes(node.right)
            
        ret_no_nodes(root)
        return count