```
class Solution:
def maxCoins(self, piles: List[int]) -> int:
# Sort the piles in ascending order
piles.sort()
# Total number of piles
n = len(piles)
# The number of rounds where you can pick 2nd maximum in each triplet
r = n // 3
# Variable to store the maximum coins obtained
max_coin = 0
# Pointers for the three positions in each triplet
low = 0
mid = n - 2
high = n - 1
# Iterate until you've completed the required rounds
while r > 0:
# Add the middle element (2nd maximum in the current triplet) to the maximum coins
max_coin += piles[mid]
# Move pointers to the next triplet
low += 1
mid -= 2
high -= 2
# Decrement the number of remaining rounds
r -= 1
return max_coin
​
```