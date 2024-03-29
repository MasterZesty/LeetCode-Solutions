https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/discuss/4303947/CC%2B%2B-Frequency-Count-vs-Sortoror67-ms-Beats-100

https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/discuss/4304067/Python3-Solution

## Apporch 2

#### Intuition
Given an array, we aim to find the number of operations needed to make all elements equal. To do so, we need to strategically reduce larger elements to the smallest element in the array.

#### Approach
Count the frequencies of each number: Create a map or dictionary to store the frequencies of each element in the array.
Sort the elements: Sort the array in descending order to start with the largest elements.
Iterate through the sorted array: As we iterate through the sorted array, keep track of the number of operations required to reduce elements.
For each element in the sorted array, increment the count of operations needed to make it equal to the smallest element (which will be at the end after sorting).
Accumulate the count of operations.
Return the total count of operations: This count represents the minimum number of operations required to make all elements equal.

### Complexity Analysis

##### Time Complexity:
Counting the frequencies of elements takes O(n) time.
Sorting the array takes O(n log n) time.
Iterating through the sorted array to count operations takes O(n) time.
Therefore, the overall time complexity is O(n log n).

##### Space Complexity:
Space required to store the frequencies in a map or dictionary is O(n).
Sorting the array in place might take O(log n) extra space due to recursive calls in certain sorting algorithms like quicksort.
Therefore, the overall space complexity is O(n).

```python
class Solution(object):
    def reductionOperations(self, nums):
        max_val = max(nums)
        freq = [0] * (max_val + 1)

        for num in nums:
            freq[num] += 1

        operations = 0
        current = max_val

        while True:
            while current > 0 and freq[current] == 0:
                current -= 1
            
            if current == 0:
                break

            next_largest = current - 1
            while next_largest > 0 and freq[next_largest] == 0:
                next_largest -= 1

            if next_largest == 0:
                break
            
            operations += freq[current]
            freq[next_largest] += freq[current]
            freq[current] = 0

        return operations
```
