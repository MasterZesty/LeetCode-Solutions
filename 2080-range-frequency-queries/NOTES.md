mid = l + (r - l)//2
# print(f"l: {l} r: {r} mid: {mid} arr value: {sub_arr[mid]} | search arr {sub_arr[l:r+1]}")
if sub_arr[mid] == value:
count += 1
# Expand the search space
# to left
i = mid - 1
while i >= 0 and sub_arr[i] == value:
count += 1
i -= 1
# to right
i = mid + 1
while i <= n and sub_arr[i] == value:
count += 1
i += 1
# break this because we found all occrnaces of values
# we can not expand this window further
break
​
if sub_arr[mid] > value:
r = mid - 1
if sub_arr[mid] < value:
l = mid + 1
​
# print(f"l: {l} r: {r} mid: {mid} arr value: {sub_arr[mid]} | search arr {sub_arr[l:r+1]}")
# print(f"count {value} is {count}")
return count
​
​
# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
```