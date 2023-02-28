# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    

#     global dict_subtree_freq
#     dict_subtree_freq = {}
    
#     global ans
#     ans = []
    
#     def dfs(self,root):
          # for this soln ref https://youtu.be/Ya8LifGLUHc
        
#         if node is None:
#             return '#'
        
#         s1 = ''
#         s2 = ''
#         curr = str(root.val)
        
#         if root.left is not None:
#             s1 = self.dfs(root.left)
        
#         if root.right is not None:
#             s2 = self.dfs(root.right)
            
#         t = curr + 'l' + s1 + 'r' + s2
#         print(t)
        
#         if t not in dict_subtree_freq:
#             dict_subtree_freq[t] = 1
#         else:
#             dict_subtree_freq[t] += 1
        
#         if dict_subtree_freq[t] == 2:
#             ans.append(root)
            
#         return t
    
    def findDuplicates(self, node, frequency, result):
        if node is None:
            return "#"
        
        leftIdentifier = self.findDuplicates(node.left, frequency, result)
        rightIdentifier = self.findDuplicates(node.right, frequency, result)
        
        identifier = str(node.val) + "," + leftIdentifier + "," + rightIdentifier
        frequency[identifier] = frequency.get(identifier, 0) + 1
        
        if frequency[identifier] == 2:
            result.append(node)
        
        return identifier
        
        
    
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        # dfs(root)
        # return ans
    
        frequency = {}
        result = []
        self.findDuplicates(root, frequency, result)
        return result
        
#         global og_tree_root
#         og_tree_root = root
        
#         global subtree_list
#         subtree_list = []
        
#         def constrct_subtree(subtree_root):
            
#             if subtree_root is None:
#                 return
            
            
#             # in og tree find nodes having val = val of root of a subtree
#             # using iterative approch for tree traversal using stack preorder traversal
#             og_tree_node_list = []
            
#             nodestack = []
#             nodestack.append(og_tree_root)
#             while len(nodestack)>0 :
                
#                 t_node = nodestack.pop()
#                 if t_node.val == subtree_root.val and t_node != subtree_root:
#                     #print("possible subtree found")
#                     og_tree_node_list.append(t_node)
                    
#                     # this line may conatian bug
#                     # if t_node not in subtree_list and t_node!=og_tree_root:
#                     #     subtree_list.append(t_node)
                    
#                 #print(t_node.val)
                
#                 if t_node.right is not None:
#                     nodestack.append(t_node.right)
                    
#                 if t_node.left is not None:
#                     nodestack.append(t_node.left)
                    
#             # print('possible subtrees when subtree_root',og_tree_node_list)
#             # print()
            
#             for m in og_tree_node_list:
#                 if str(m) == str(subtree_root):
#                     # print('duplicates found',str(m))
#                     if m not in subtree_list:
#                         subtree_list.append(m)
#             # print()
                    
            
        
#         def tree_traversal(root):
            
#             if root:
                
#                 # print root
#                 #print('Traverse throght tree with root as :',root.val)
#                 # constrct a subtree for this specific root to 
#                 # check that subtrees duplictaes exist or not
#                 # for this root construct subtree
#                 constrct_subtree(root)
                
                
#                 tree_traversal(root.left)
                
#                 tree_traversal(root.right)
                
#         tree_traversal(root)
#         print('subtree_list ', subtree_list)
#         # print()
        
#         ans = []
#         idx = []
        
        
#         edge_case_flag = False
        
#         i = 0
#         for node_i in subtree_list:
#             temp = []
#             temp.append(i)
#             j = 0
            
#             for node_j in subtree_list:
#                 if node_i != node_j:
#                     # print(node_i.val,node_j.val)
#                     if str(node_i) == str(node_j):
#                         #handle egde case
#                         if node_i.val == 0 and node_j.val == 0:
#                             edge_case_flag = True
#                         else:
#                             edge_case_flag = False
#                         #print(str(node_i),'|', str(node_j))
#                         temp.append(j)
#                     else:
#                         #print(str(node_i),'|', str(node_j))
#                         pass
#                 j += 1
#             #print('temp',temp)
#             temp.sort()
#             if temp not in idx:
#                 idx.append(temp)
#                 ans.append(subtree_list[temp[0]])
#             i+= 1
            
            
        
#         return ans  

#         above code cause TLE

                        
                    
                
                    
        
            
                