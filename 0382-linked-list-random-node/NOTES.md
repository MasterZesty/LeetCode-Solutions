* Two Apporches first we can traverse each node and strore values in a list
* then will select random element from that list
* Time O(N) Space (N)

```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.values = []
        temp = head
        while temp:
            self.values.append(temp.val)
            temp = temp.next
            
        

    def getRandom(self) -> int:
        #print(self.values)
        return self.values[random.randint(0, len(self.values)-1)]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
```

* but this will fail when N is very very large or unknown

* so there is another algo called Reservoir Algo
* Space O(1) Time O(N)

ref video : https://youtu.be/32hcF0WJdTU

NOT IMPLEMENTED YET WILL BE REVISITING

```
class Solution(object):

    def __init__(self, head):
        """
        :type head: Optional[ListNode]
        """
        self.head = head

    def getRandom(self):
        """
        :rtype: int
        """
        count = 0
        result = None
        curr = self.head

        while curr:
            count += 1
            # generate a random number between 1 and the count
            # if the random number is 1, update the result with the current node's value
            if random.randint(1, count) == 1:
                result = curr.val
            curr = curr.next

        return result

```
