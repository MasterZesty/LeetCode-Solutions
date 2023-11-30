```
class Solution:
def minimumOneBitOperations(self, n: int) -> int:
ans, f = 0, 0
for i in range(31, -1, -1):
if ((n >> i) & 1) == 1:
if f == 0:
ans = ans + ((1 << (i + 1))) - 1
f = 1
else:
ans = ans - ((1 << (i + 1)) - 1)
f = 0
print(ans)
return ans
```
​
https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/discuss/4345259/Easy-Video-Explanation-with-logic-building-and-Proofs-oror-Bit-Manipulation
​
https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/discuss/4344637/C%2B%2B-or-PYTHON-or-JAVA-oror-EXPLAINED-oror
​
https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/discuss/4344660/Beats-100-Explained-with-Video-Fastest-Recursive-Solution-Visualized-Too
​
​