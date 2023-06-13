* The optimized solution has a time complexity of O(n^2), where n is the size of the input
*  grid (assuming the grid is a square matrix). This is because we iterate over each element
*  of the grid once to construct the set of rows and then iterate over each column to check for matching rows.
​
* The space complexity of the optimized solution is O(n^2) as well. This is due to the space
* required to store the set of rows, which can contain up to n elements in the case of a
* square matrix. The memory used for other variables and operations is negligible compared
* to the size of the grid.
*
* Overall, the optimized solution provides an improvement by eliminating the need to
* explicitly construct the columns array and using a set for efficient membership testing.
* However, the time and space complexity remain the same as the original solution.