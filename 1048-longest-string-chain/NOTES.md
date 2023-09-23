b. For each index i in the range of the length of the current word:
​
i. Generate the predecessor of the current word by removing the character at index i using slicing (word[:i] + word[i+1:]), and assign it to pred.
​
ii. Check if the predecessor pred is already in the chains dictionary:
​
If it is, update the chain length for the current word (chains[word]) to the maximum of its current chain length and the chain length of the predecessor incremented by 1 (chains[pred] + 1).
​
If it's not, continue to the next iteration.
​
Return the maximum chain length found by taking the maximum value from the values in the chains dictionary using the max function. This represents the longest string chain.
​
The function returns the maximum chain length.
​
Complexity
Time complexity: O(n log n + len(word) * 16) → O(n log n)
​
the first part of O(n log n) comes from sorting, where n is the number of words (which can be at most 1000)
​
len(word) * 16 comes from for loop. len(word) is n and 16 comes from one of constraints and can be removed, so part of len(word) * 16 should be n.
​
Since O(n log n) dominates time, overall time complexity is O(n log n)
​
Space complexity: O(n)
n is the number of words
​
class Solution:
def longestStrChain(self, words: List[str]) -> int:
chains = {}  # Stores the max chain length for each word
sorted_words = sorted(words, key=len) # Sort words by length
​
for word in sorted_words:
chains[word] = 1  # Initialize the chain length for the current word
for i in range(len(word)):
pred = word[:i] + word[i+1:]  # Generate predecessor by removing one character
if pred in chains:
chains[word] = max(chains[word], chains[pred] + 1)
​
return max(chains.values())