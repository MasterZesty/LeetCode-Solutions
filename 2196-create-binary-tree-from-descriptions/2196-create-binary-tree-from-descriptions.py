# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
          
            nodes = {}
            childs = {}
            
            for i, cp_record in enumerate(descriptions):
                
                parent_val, child_val, isleft = cp_record
                # print(f"cp_record: {cp_record}")
                
                # if parent node record already exist
                if nodes.get(parent_val, 0) != 0:
                    
                    # if child node record does not exist
                    if nodes.get(child_val, 0) == 0:
                        # then crate child node record
                        child_node = TreeNode(child_val)
                        nodes[child_val] = child_node
                        
                        # add to list of child nodes
                        childs[child_val] = 1
                    
                        # append to left
                        if isleft == 1:
                            nodes[parent_val].left = child_node

                        # append to right
                        if isleft == 0:
                            nodes[parent_val].right = child_node
                    
                    # if child node record already exist
                    elif nodes.get(child_val, 0) != 0:
                        
                        # add to list of child nodes
                        childs[child_val] = 1
                        
                        # append to left
                        if isleft == 1:
                            nodes[parent_val].left = nodes[child_val]
                        
                        # append to right
                        if isleft == 0:
                            nodes[parent_val].right = nodes[child_val]
                        
                
                # if parent node record does not exist
                if nodes.get(parent_val, 0) == 0:
                    # then create parent node record
                    parent_node = TreeNode(parent_val)
                    nodes[parent_val] = parent_node
                    
                    # check if child node record exist 
                    if nodes.get(child_val, 0) == 0:
                        # if not create child node record
                        child_node = TreeNode(child_val)
                        nodes[child_val] = child_node
                        
                        # add to list of child nodes
                        childs[child_val] = 1
                        
                        # append to left
                        if isleft == 1:
                            parent_node.left = child_node
                        
                        # append to right
                        if isleft == 0:
                            parent_node.right = child_node
                    
                    # if child node record exist
                    elif nodes.get(child_val, 0) != 0:
                        
                        # add to list of child nodes
                        childs[child_val] = 1
                        
                        # append to left
                        if isleft == 1:
                            parent_node.left = nodes[child_val]
                        
                        # append to right
                        if isleft == 0:
                            parent_node.right = nodes[child_val]
                            
                # print(f"childs: {childs}")
            
            # print(f"nodes: {nodes[38]}")
            # print(f"childs: {childs}")
            root = None
            
            for node in nodes:
                if childs.get(node, 0) == 0:
                    root = nodes[node]
                    break
                    
            # print(f"root: {root.val}")
            return root