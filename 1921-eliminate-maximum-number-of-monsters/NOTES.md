Comparison of Approaches
The initial sort approach sorts the monsters by their calculated arrival times, allowing us to easily iterate through and eliminate them in order. This method's time complexity is $ O(n \log n) $ due to the sort operation, and it's simple to understand and implement. However, it may not be the most efficient if the input range is limited and well-defined, as it doesn't take advantage of possible patterns in the input distribution.
​
The counting sort approach counts the number of monsters arriving at each possible time, which can be done in $ O(n) $ time, making it faster for certain distributions of input data. The space complexity remains $ O(n) $, but the constants involved may be larger due to the need for a counting array. This method shines when the maximum arrival time is not significantly larger than the number of monsters because it can sort the arrival times without direct comparisons. However, if the range of arrival times is very large, it may not offer any advantage and could even consume more memory.
​
Approach Initial Sort
The approach to solving this problem involves several steps:
​
Calculate Arrival Times:
We compute the time it will take for each monster to reach the city. This is done by dividing the distance of each monster by its speed, yielding the time of arrival.
​
Sort Arrival Times:
Once we have the times, we sort them in ascending order. This allows us to process the monsters in the order they would reach the city.
​
Eliminate Monsters:
We simulate the process of eliminating monsters one by one. Starting with the monster that arrives first, we eliminate one monster per minute. During each minute, we check if the current monster has already reached the city (i.e., its arrival time is less than or equal to the time spent on previous eliminations). If so, we stop and return the number of monsters eliminated up to that point.
​
Return Result:
If we manage to go through all the monsters without any reaching the city, we return the total number of monsters.
​
Complexity
Time complexity:
The time complexity is $O(n \log n)$. The most time-consuming operation in the algorithm is the sorting of the arrival times. Calculating the arrival times is $O(n)$, and iterating through the sorted list is also $O(n)$. However, the sorting operation dominates, leading to the $O(n \log n)$ complexity.
​
Space complexity:
The space complexity is $O(n)$. We need additional space to store the arrival times of all monsters before sorting. The rest of the operations use constant space, except for the sorting which can take $O(n)$ space depending on the implementation of the sort function in the language used.
​
https://leetcode.com/problems/eliminate-maximum-number-of-monsters/discuss/4258414/98.19-Greedy-Initial-and-Counting-Sort