```
'''
Approch 1: recursion
'''
n = len(arr)
​
​
def solve(arr, k, i):
if i >= n:
return 0
maxval = 0
ans = 0
for j in range(i, min(n,i+k) ):
maxval = max(maxval, arr[j])
ans = max(ans, (j-i+1)*maxval + solve(arr, k, j+1))
return ans
​
return solve(arr, k, 0)
```