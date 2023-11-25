ref :
1. https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/discuss/4326565/Simple-well-explained-C%2B%2B-solution-oror-TC%3AO(n)-SC%3AO(1)
2. https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/discuss/4327519/simplest-c-explained-solution-prefixsum-and-suffixsum-approach/
​
absDiff = ((number of elements before x1) * x1 - leftSum) +  (rightSum - (number of elements after x1 including x1) * x1);
​
### Intuition
Here we are first calculating the total sum of the array. Then, for each element, it calculates the sum of absolute differences with all other elements by separately considering the elements to its left and right. The results are stored in a vector and returned. This approach allows the problem to be solved in linear time complexity.
​
### Approach
The approach for this code is as follows:
​
Initialization: Initialize total_sum to 0, n to the size of the input vector nums, and curr_sum to 0. total_sum is used to store the sum of all elements in nums, and curr_sum is used to store the cumulative sum of elements as we iterate through nums.
​
Calculate Total Sum: Iterate through nums and add each element to total_sum.
​
Calculate Sum of Absolute Differences: For each element nums[i], calculate the sum of absolute differences as follows:
​
Update curr_sum by adding nums[i].
Calculate Rsum as the difference between total_sum and curr_sum. This represents the sum of the elements to the right of nums[i].
Calculate Lsum as the difference between curr_sum and nums[i]. This represents the sum of the elements to the left of nums[i].
Update Lsum and Rsum to represent the sum of absolute differences of nums[i] with all elements to its left and right respectively.
Add the sum of Lsum and Rsum to the answer vector ans.
Return Result: Return ans, which is a vector containing the sum of absolute differences for each element in nums.
​
###### The key idea here is to calculate the sum of absolute differences for each element in linear time by separately considering the elements to its left and right. This approach significantly improves the efficiency of the code.
​
### Complexity
Time complexity: O(n)
Space complexity: O(1)