## Approach 1: Depth-First Search (DFS)
### Intuition
​
`In this problem, we are given information about numbers that are adjacent to each other in some array nums. We can think of these pairs in adjacentPairs as edges in a graph: if we have a pair (x, y), we can imagine that there is an undirected edge between node x and y.`
​
`This graph would form a doubly-linked list, since the edges, by definition, only describe adjacent elements. In fact, this doubly-linked list would represent nums, since the adjacent elements are adjacent elements in nums!`
​
​
## Approach 2: Iterative, Follow the Path
### Intuition
​
`As we discussed in the previous approach, the graph of this problem is essentially a linked list, so we don't need any algorithm like DFS or BFS (Breadth-First Search) to traverse it. We can just iteratively traverse it like we would a linked list.`
​
`Here, we implement graph and find root in the same manner as the previous approach.`
​
`Next, instead of a DFS, we use a variable curr that represents the current node. We also use a variable prev to indicate the previously visited node, to ensure we only move in a straight line. Note that the length of graph will be equal to the length of nums since each number in nums has at least one edge, and thus an entry in graph.`
​
`With this in mind, we will have a while loop that runs until ans.length = graph.length, indicating we have finished building ans. In this while loop, we iterate over each neighbor of graph[curr]. If neighbor != prev, it is the next node we should go to. We add neighbor to ans, update prev and curr accordingly, then break from the iteration to move on to the next node.`
​
`Once the while loop ends, we know that ans is complete, so we can simply return ans.`
​