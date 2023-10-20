return -1
return self.denestList[self.next_count]
def hasNext(self) -> bool:
if self.next_count > len(self.denestList):
return False
self.next_count += 1
return True
`
​
2. as above approch failed we can use recursion with helper function
​
ref :
​
1. https://leetcode.com/problems/flatten-nested-list-iterator/discuss/4187840/95.83-Recursive-Flattening-and-Stack
2. https://youtu.be/Mh8-eLca4Ks
​
​
​
​
​
​