***To solve this problem, we need to come up with a custom sorting key for the integers in the array. The key should take into account both the number of 1's in the binary representation and the original integer value. We can achieve this by using a custom sorting function.***
​
***Approach
Our approach is straightforward:*
​
Convert each number into its binary representation using the bin() function.
Count the number of 1's using the count('1') method.
Sort the numbers first by the count of 1's and then by the number itself.
Python's sorted function will use the first element of the tuple for sorting and if there's a tie, it'll use the second element.
​
***Complexity***
Time complexity: The time complexity of the sorted function is $$O(n \log n)$$, where $n$ is the length of the array. Counting the 1's in the binary representation of each number can be done in $O(m)$ time, where $m$ is the maximum number of bits needed to represent any number in the list. Thus, the overall time complexity is $O(n \log n \times m)$.
​
Space complexity: The space complexity of the sorted function is $O(n)$, as it returns a new sorted list.