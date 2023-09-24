# approch 2 : much more intuitive
ref : https://leetcode.com/problems/champagne-tower/discuss/4082519/98.90-oror-Matrix-oror-Simple-Solution-oror-Beginner
```
class Solution:
def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
# Create a 2D array to represent the champagne distribution in glasses,
# initialize all elements to 0.0.
result = [[0.0] * 101 for _ in range(101)]
# Pour the initial amount of champagne into the top glass (row 0, glass 0).
result[0][0] = poured
# Iterate through each row of glasses up to the 100th row.
for i in range(100):
# Iterate through the glasses in the current row (up to i).
for j in range(i + 1):
# If the current glass has champagne overflowing (more than or equal to 1 unit),
if result[i][j] >= 1:
# Calculate the overflow and distribute it equally to the glasses below.
result[i + 1][j] += (result[i][j] - 1) / 2.0
result[i + 1][j + 1] += (result[i][j] - 1) / 2.0
# Set the current glass to have exactly 1 unit of champagne.
result[i][j] = 1.0
# Return the amount of champagne in the specified glass (query_row, query_glass).
return result[query_row][query_glass]
```