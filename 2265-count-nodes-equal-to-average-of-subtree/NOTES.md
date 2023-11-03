for ref :
1. https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/discuss/4237092/Beats-90.78-oror-DFS-oror-Easiest-Explanation
2. https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/discuss/4237404/VideoGive-me-8-minutes-How-we-think-about-a-solution-Why-we-use-postorder-traversal
​
Total Sum = sum of left subtree + sum of right subtree + current value
Number of nodes = number of nodes from left + number of nodes from right + 1
​
```
class TreeNode:
def __init__(self, val=0, left=None, right=None):
self.val = val
self.left = left
self.right = right
​
def inorder(root):
if not root:
return []
result = []
result += inorder(root.left)
result.append(root.val)
result += inorder(root.right)
return result
​
def preorder(root):
if not root:
return []
result = []
result.append(root.val)
result += preorder(root.left)
result += preorder(root.right)
return result
​
def postorder(root):
if not root:
return []
result = []
result += postorder(root.left)
result += postorder(root.right)
result.append(root.val)
return result
```