ref : https://leetcode.com/problems/interleaving-string/discuss/3956393/99.78-2-Approaches-DP-and-Recursion
​
Interview Guide: "Interleaving String" Problem
Problem Understanding
In the "Interleaving String" problem, you are given three strings: s1, s2, and s3. Your task is to determine whether s3 can be formed by interleaving s1 and s2. For example, if s1 = "aabcc" and s2 = "dbbca", then s3 = "aadbbcbcac" should return true, but s3 = "aadbbbaccc" should return false.
​
Key Points to Consider
1. Understand the Constraints
Before diving into the solution, make sure you understand the problem's constraints. The lengths of the strings will not be more than 100 for s1 and s2, and not more than 200 for s3. This can help you gauge the time complexity you should aim for.
​
2. Multiple Approaches
There are multiple ways to solve this problem, including:
​
2D Dynamic Programming
1D Dynamic Programming
Recursion with Memoization
Each method has its own time and space complexity, so choose based on the problem's constraints.
​
3. Space Optimization
While 2D Dynamic Programming is the most intuitive approach, you can reduce the space complexity to (O(\min(m, n))) by employing 1D Dynamic Programming. In an interview setting, discussing this optimization can impress your interviewer.