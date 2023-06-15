# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
#            # BFS - Level Order Traversal (Breadth First Search or BFS) of Binary Tree

#             q = []
#             q.append((root, 1 )) # Add the root node with its level (1)

#             current_level = 1  # Track the current level
            
#             ans = 0
#             t = 0
#             l = -1

#             while len(q) > 0:
#                 node, level = q.pop(0)
#                 print(f'current level : {current_level} | level : {level}')
                
#                 # Check if the level has changed
#                 if level != current_level:
#                     print(f'level sum {t}')
#                     print("----- Level End -----",level)
#                     current_level = level
#                     if t> ans:
#                         l = level
#                         ans = t
#                     t = node.val
#                 else:
#                     print(f't {t}')
#                     t += node.val
                    
#                 print(f'Node value: {node.val}')

#                 if node.left is not None:
#                     q.append((node.left, level + 1))

#                 if node.right is not None:
#                     q.append((node.right, level + 1))
                    
#                 if len(q) == 0:
#                     print(f'q==0 ==> t {t}')
#                     if t > ans:
#                         l = level
#                         ans = t

#             print("----- Level End -----",level)
#             print(f'ans {ans}')
#             print(l)

#             return l
            max_sum, ans, level = float('-inf'), 0, 0

            q = []
            q.append(root)

            while q:
                level += 1
                sum_at_current_level = 0
                # Iterate over all the nodes in the current level.
                for _ in range(len(q)):
                    node = q.pop(0)
                    sum_at_current_level += node.val

                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

                if max_sum < sum_at_current_level:
                    max_sum, ans = sum_at_current_level, level

            return ans

