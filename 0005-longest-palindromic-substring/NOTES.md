Initialization:
​
Initialize variables:
strLength for the length of the modified string T.
palindromeLengths, an array to store the lengths of palindromes centered at each position in T.
center for the current center of the palindrome being processed.
rightEdge for the rightmost edge of the palindrome found so far.
Palindrome Detection:
​
Loop through the modified string T to find palindromes centered at each position.
Calculate the length of the palindrome at the current position i based on previously computed information and expand it if possible. This is done by comparing characters around the current position.
Update center and rightEdge if a longer palindrome is found.
Find the Longest Palindrome:
​
After processing the entire modified string T, identify the longest palindrome by searching the palindromeLengths array for the maximum value.
Determine the center of this longest palindrome.
Extract the Result:
​
Use the information about the longest palindrome (center and length) in the modified string T to extract the corresponding substring from the original input string s.
The code effectively implements this approach to find and return the longest palindromic substring in the input string s. Manacher's algorithm is more efficient than naive methods because it takes advantage of the properties of palindromes and avoids redundant comparisons, making it a good choice for solving this problem.
​
Complexity 🚁
🏹 Time complexity: O(N)
The time complexity of Manacher's algorithm is O(N), where N is the length of the input string s. This is because the algorithm processes each character of the modified string exactly once (with some constant factor overhead) in a linear pass. The key factor in achieving this efficiency is the "center expansion" technique used to find palindromes, which avoids unnecessary character comparisons.
​
🏹 Space complexity: O(N)
The space complexity of the code is O(N) as well. This is primarily due to the creation of the modified string T, which is constructed by adding extra characters, such as '^', '#', and '$', to the original string. The P array used to store the lengths of palindromes at each position also has a space complexity of O(N) because it is an array of the same length as the modified string. The other variables used in the algorithm (e.g., C, R, and loop counters) have constant space requirements and do not significantly contribute to the space complexity.
​
So, in terms of both time and space complexity, this code is very efficient for finding the longest palindromic substring in a string.