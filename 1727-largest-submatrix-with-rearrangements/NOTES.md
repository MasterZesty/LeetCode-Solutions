https://leetcode.com/problems/largest-submatrix-with-rearrangements/discuss/4331401/C%2B%2B-94.89-fasteroror-Histogram-Max-Area-Finding-Problem-oror-Count-ones-and-sort
​
### Approach:
​
**Imagine each column in the matrix as a vertical bar, where its height represents the count of consecutive ones above it, including itself.**
​
**It is basically a Histogram Area Finding Problem: Calculating the maximum area of a histogram for each row: This helps in determining the maximum rectangle that can be formed considering the consecutive 1s in each column.**
​
**For example, the given matrix:**
​
```
[[0,0,1],
[1,1,1],
[1,0,1]]
```
​
**Transforming it into a 'height' array gives us [2, 0, 3]. Sorting this array becomes [3, 2, 0].**
​
**Now, after sorting 'height' array, let's find the largest submatrix:**
​
**At column 0 with a height of 3, there's only one column, so the area is 3.
Moving to column 1 with a height of 2, we have two columns that can form a base of height 2, resulting in an area of 4.
Finally, at column 2 with a base height of 0, there's only one column that fulfills this, resulting in an area of 0.
Therefore, the maximum area achievable with rearranged columns to create a submatrix of consecutive 1s is 4."**
​
​
https://leetcode.com/problems/largest-submatrix-with-rearrangements/discuss/4332463/fully-explained-solution-with-example-and-dry-run/