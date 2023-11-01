# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        hm = {}
        
        # tree traversal bfs
        node_queue = []
        node_queue.append(root)
        
        while len(node_queue) > 0 :
            # do stuff
            
            curr_node = node_queue.pop(0)
            hm[curr_node.val] = hm.get(curr_node.val,0) + 1
            
            if curr_node.left != None:
                node_queue.append(curr_node.left)
                
            if curr_node.right != None:
                node_queue.append(curr_node.right)
                
        
        max_value = max(hm.values())
        
                
        print(f'hm : {hm} max_value {max_value}')
        
        return [key for key, val in hm.items() if val == max_value]