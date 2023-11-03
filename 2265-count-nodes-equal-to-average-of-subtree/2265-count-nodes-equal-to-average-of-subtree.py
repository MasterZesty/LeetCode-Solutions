# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        # find a trversal method which is like
        # DFS with left right root traversal => postorder treversal
        
        res_node_count = 0
        
        def postorder(node):
            #use nonlocal
            nonlocal res_node_count
            
            #empty subtree or a leaf node -> base cas returns sum,no of nodes
            if node is None:
                return 0,0
            
            #postorder left right root
            
            left_sum, left_subtree_node_count = postorder(node.left)
            
            right_sum, right_subtree_node_count = postorder(node.right)
            
            
            # Total Sum = sum of left subtree + sum of right subtree + current value
            total_sum = left_sum + right_sum + node.val
            
            # Number of nodes = number of nodes from left + number of nodes from right + 1
            total_nodes = left_subtree_node_count + right_subtree_node_count + 1
            
            #print(f'node : {node.val} | sum {total_sum} | node_count {total_nodes} | avg {total_sum // total_nodes}')
            
            if total_sum // total_nodes == node.val:
                res_node_count += 1
                
            return total_sum,total_nodes
        
        postorder(root)
        
        return res_node_count
            
            