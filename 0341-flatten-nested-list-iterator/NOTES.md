# Thought process/ intuition
​
so the we need to check how we are solving the issue of deep nesting we can not
write a if loops .
​
recursion may be the solution  here
​
1. we can convert list to string and then remove [ and ] we get plain series of numbers =>
`self.denestList = list(map(int, str(nestedList).replace('[','').replace(']','').split(',')))`
this is not going to work beacause we assuemed we are getting input like this : [[1,1],2,[1,1]]
but we got like this :  [NestedInteger{_integer: None, _list: [NestedInteger{_integer: 1, _list: []}, NestedInteger{_integer: 1, _list: []}]}, NestedInteger{_integer: 2, _list: []}, NestedInteger{_integer: None, _list: [NestedInteger{_integer: 1, _list: []}, NestedInteger{_integer: 1, _list: []}]}]
`class NestedIterator:
def __init__(self, nestedList: [NestedInteger]):
print(nestedList)
self.next_count = -1
self.denestList = list(map(int, str(nestedList).replace('[','').replace(']','').split(',')))
def next(self) -> int:
if self.next_count > len(self.denestList):
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