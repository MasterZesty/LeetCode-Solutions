## Approch/Intuition
​
start ---------------------------> end
​
1. what is minimum time required to go from start to end
2. if t >= min_time return True else False
​
## so now we need to find a way to find a min time
​
## here we go
​
## Apporch 2
ref : https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/discuss/4262425/C%2B%2B-Chebyshev-distanceoror0ms-Beats-100
​
Since one grid has 8 adjacent grides, it uses
the Chebyshev distance
$$
L^{\infty}((x_0, y_0), (x_1, y_1))=\max(|x_0-x_1|, |y_0-y_1|)
$$
For the similar question for which one grid has 4 adjacent grides, it needs the Manhatten distance
$$
L^{1}((x_0, y_0), (x_1, y_1))=|x_0-x_1|+|y_0-y_1|
$$
​
#### Approach
If d>0 check whether t>=d
otherwise check whether t!=1
​
#### Complexity
Time complexity:
$$O(1)$$
​
Space complexity:
$$O(1)$$