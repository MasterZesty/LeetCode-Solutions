n = len(nums)
# base edge case
if n == 1:
ans = '0' if nums[0] == '1' else '1'
return ans
ans = int(nums[0], 2)
for i in range(1,n):
#print(f'{nums[i]}')
ans = ans ^ int(nums[i], 2)
# print(f'ans: {ans} | bin {bin(ans)}')
#final processing
ans = bin(ans)
bit_size = len(nums[0])
zeros = bit_size - len(ans[2:])
append_zero = ''.join( ["0"]*zeros )
ans = append_zero + ans[2:]
# print(f'final ans : {ans}')
return ans
```
​
### Approch 2
​
https://leetcode.com/problems/find-unique-binary-string/discuss/4292653/Beats-100-Explained-With-Video-Simplest-Solution-(-2-3-Lines)-Visualized-Too
​
###### Intuition
The problem asks for a binary string that does not appear in the given array of binary strings. Since each binary string has a length of n and the strings are unique, we can construct a binary string by considering the characters at the diagonal positions in the given strings.
​
###### Approach
Initialize a StringBuilder to construct the result binary string.
Iterate through the array of binary strings.
At each iteration, append the character at the diagonal position (position i) in the current binary string to the result.
Return the result binary string.
​
###### Complexity
Time Complexity: O(n)
The algorithm iterates through the given array of binary strings once, and each iteration takes constant time.
Space Complexity: O(n)
The StringBuilder is used to construct the result binary string.