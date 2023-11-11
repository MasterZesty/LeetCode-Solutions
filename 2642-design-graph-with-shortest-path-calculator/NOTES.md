## Intuition/Approch
​
1. think of a data structure how we can represent graph
​
```
Adjacency matrix representation
To store weighted graph using adjacency matrix form, we call the matrix as cost matrix. Here each cell at position M[i, j] is holding the weight from edge i to j. If the edge is not present, then it will be infinity. For same node, it will be 0.
```
​
### How to find Shortest Paths from Source to all Vertices using Dijkstra’s Algorithm
​
ref : https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/
​
```
Dijkstra's Algorithm is an algorithm to find the shortest path between two nodes in a graph or two cells in a matrix or any problem that can be represented as a graph.📈
​
It's part of a family of algorithms designed to uncover the shortest path between nodes or cells like BFS, Bellman-Ford Algorithm, Floyd-Warsahll Algorithm. Each algorithm has its unique applications.
​
Let's focus on Dijkstra's Algorithm:
Nature: It's a single-source, multiple-destination algorithm. In simpler terms, it pinpoints the shortest path from a starting node to any other node in our graph.
Constraints: Dijkstra's Algorithm is suitable for graphs or problems featuring positive weights. If we encounter negative weights, we'd choose alternative algorithms such as Bellman-Ford.
And there you have it! Dijkstra's Algorithm is the key 🗝to our problem, well-known for tackling precisely these types of challenges.
​
We will construct our graph simply like any other graph problem and when we are required to calculate shortest path between two nodes we will call our svaior Dijkstra's Algorithm.
​
And this is the solution for our today'S problem I hope that you understood it🚀🚀
```
​
ref : https://leetcode.com/problems/design-graph-with-shortest-path-calculator/discuss/4274432/Dijkstra's-Algorithm-oror-Explained-Intuition
​
​