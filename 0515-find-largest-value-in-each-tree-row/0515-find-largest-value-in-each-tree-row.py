# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        
        if root == None:
            return []
        
        node_queue = []
        node_queue.append(root)
        node_visited = []
        
        while(len(node_queue) > 0):
            # do stuff
            
            curr_len = len(node_queue)
            curr_max = float('-inf')
            
            for _ in range(curr_len):
                # pop node from queue
                curr_node = node_queue.pop(0)
                #print(f'node value : {curr_node.val}')
                curr_max = max(curr_max, curr_node.val)

                # mark as visited
                node_visited.append(curr_node)

                # explore node
                if curr_node.left != None:
                    node_queue.append(curr_node.left)

                if curr_node.right != None:
                    node_queue.append(curr_node.right)
                    
            ans.append(curr_max)
                
        return ans
            