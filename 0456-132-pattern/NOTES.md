Minimum from the Left (MinLeft) Approach:
By keeping track of the minimum value from the left for each element, we can employ another efficient method to detect the pattern.
​
Binary Search Approach:
While not the most optimal, this approach offers a unique perspective on the problem. Leveraging binary search, we maintain a sorted list of numbers encountered so far. This method systematically detects the 132 pattern and showcases the versatility of binary search in algorithmic challenges beyond traditional searching.
​
​
​
​
Code Stack
class Solution:
def find132pattern(self, nums: List[int]) -> bool:
stack, third = [], float('-inf')
for num in reversed(nums):
if num < third:
return True
while stack and stack[-1] < num:
third = stack.pop()
stack.append(num)
return False
Code MinLeft
class Solution:
def find132pattern(self, nums: List[int]) -> bool:
n = len(nums)
minFromLeft = [nums[0]]
for i in range(1, n):
minFromLeft.append(min(minFromLeft[i-1], nums[i]))
stack = []
for j in range(n-1, -1, -1):
if nums[j] > minFromLeft[j]:
while stack and stack[-1] <= minFromLeft[j]:
stack.pop()
if stack and stack[-1] < nums[j]:
return True
stack.append(nums[j])