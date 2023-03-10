# param_1 = obj.getRandom()
```
​
* but this will fail when N is very very large or unknown
​
* so there is another algo called Reservoir Algo
* Space O(1) Time O(N)
​
ref video : https://youtu.be/32hcF0WJdTU
​
NOT IMPLEMENTED YET WILL BE REVISITING
​
```
class Solution(object):
​
def __init__(self, head):
"""
:type head: Optional[ListNode]
"""
self.head = head
​
def getRandom(self):
"""
:rtype: int
"""
count = 0
result = None
curr = self.head
​
while curr:
count += 1
# generate a random number between 1 and the count
# if the random number is 1, update the result with the current node's value
if random.randint(1, count) == 1:
result = curr.val
curr = curr.next
​
return result
​
```