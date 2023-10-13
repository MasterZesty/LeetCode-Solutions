The reason we calculate `min_cost[i - 1] + cost[i - 1]` in the dynamic programming approach is to find the minimum cost to reach step `i` while considering the two possible options:
​
1. The minimum cost to reach step `i - 1` (`min_cost[i - 1]`) plus the cost of step `i - 1` (`cost[i - 1]`).
2. The minimum cost to reach step `i - 2` (`min_cost[i - 2]`) plus the cost of step `i - 2` (`cost[i - 2]`).
​
We compare these two options and take the minimum of the two. This is because when we reach step `i`, we have the choice of coming from either step `i - 1` or step `i - 2`, and we want to choose the path with the minimum cost.
​
If we only used `cost[i - 1]`, we would not be considering the accumulated minimum cost up to step `i - 1`, which is the essence of dynamic programming. By considering the accumulated minimum cost, we ensure that the algorithm finds the optimal path with the lowest cost to reach the top of the staircase.
​
In summary, we calculate `min_cost[i - 1] + cost[i - 1]` to determine the minimum cost to reach step `i` while taking into account the costs of the previous steps and choosing the most cost-effective path.