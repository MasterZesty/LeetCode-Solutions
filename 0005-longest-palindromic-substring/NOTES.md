***Attempt 1 :***

```
        n = len(s)
        max_len_p = 0
        ps = ''
        
        def helpe_is_palindrome(s):
            n = len(s)
            if n == 1:
                return True
            
            if n % 2 == 0:
                return s[: n//2] == s[n:n//2-1 : -1]
            
            if n % 2 != 0:
                return s[: n//2] == s[n:n//2: -1]
        
        for i in range(n,0,-1):
            # print(s[0:i])
            if helpe_is_palindrome(s[:i]):
                
                if len(s[:i]) > max_len_p:
                    max_len_p = len(s[:i])
                    ps = s[:i]
        
        for i in range(n):
            print(s[0:i])
#             if helpe_is_palindrome(s[:i]):
                
#                 if len(s[:i]) > max_len_p:
#                     max_len_p = len(s[:i])
#                     ps = s[:i]
                    
                    
        return ps
```

***Attempt 2 :***
ref: https://www.youtube.com/watch?v=lhAl44jZvIk
ref: https://leetcode.com/problems/longest-palindromic-substring/discuss/4212378/How-to-answer-in-interview-Intuition-to-Solution-Fastest-Easier-than-other-solutions

Intuition
The problem requires us to find the longest palindromic substring within a given string. A simple approach is to check every possible substring within the given string and determine if it's a palindrome. However, this brute-force approach results in a time complexity of O(n^3), which is highly inefficient.

A more efficient approach is to use dynamic programming, which allows us to optimize the solution to O(n^2). The key idea is to recognize that a palindrome reads the same backward as forward. Therefore, we can efficiently identify palindromes by expanding around a center. We start with a single character as a center and expand it in both directions, keeping track of the longest palindrome found.

Approach
Initialize two variables, maxLen and lo, to keep track of the maximum palindrome length and the starting index of the longest palindrome.
Iterate through the characters of the input string.
For each character, expand around the center, considering both odd and even-length palindromes.
While expanding, check if the substring is a palindrome.
If a longer palindrome is found, update maxLen and lo accordingly.
After iterating through all characters, return the longest palindrome substring using the lo and maxLen variables.
Complexity
Time Complexity: O(n^2) - We expand around each character once, leading to a quadratic time complexity.
Space Complexity: O(1) - We use a constant amount of extra space.
This optimized solution efficiently finds the longest palindromic substring in a given string.

 ***Attempt 3 :***

***Manacher's Algorithm***
ref: https://leetcode.com/problems/longest-palindromic-substring/discuss/4212241/98.55-Manacher's-algorithm

:- Manacher's Algorithm 🚩
Intuition 🚀:
The code implements Manacher's algorithm, which is designed to find the longest palindromic substring in a given string. The algorithm is an efficient way to tackle this problem and is based on the following key ideas:

Utilize symmetry: Palindromes have a property of symmetry, which means their left and right sides are mirror images of each other. Manacher's algorithm takes advantage of this property to optimize the process.

Avoid redundant computations: The algorithm uses previously computed information to avoid redundant checks, which makes it more efficient than brute force methods.

Approach 🚀:
Preprocessing:

The input string s is preprocessed to create a modified string T with special characters (^, #, and dollar ) inserted between each character to simplify palindrome detection.
Initialization:

Initialize variables:
strLength for the length of the modified string T.
palindromeLengths, an array to store the lengths of palindromes centered at each position in T.
center for the current center of the palindrome being processed.
rightEdge for the rightmost edge of the palindrome found so far.
Palindrome Detection:

Loop through the modified string T to find palindromes centered at each position.
Calculate the length of the palindrome at the current position i based on previously computed information and expand it if possible. This is done by comparing characters around the current position.
Update center and rightEdge if a longer palindrome is found.
Find the Longest Palindrome:

After processing the entire modified string T, identify the longest palindrome by searching the palindromeLengths array for the maximum value.
Determine the center of this longest palindrome.
Extract the Result:

Use the information about the longest palindrome (center and length) in the modified string T to extract the corresponding substring from the original input string s.
The code effectively implements this approach to find and return the longest palindromic substring in the input string s. Manacher's algorithm is more efficient than naive methods because it takes advantage of the properties of palindromes and avoids redundant comparisons, making it a good choice for solving this problem.

Complexity 🚁
🏹 Time complexity: O(N)
The time complexity of Manacher's algorithm is O(N), where N is the length of the input string s. This is because the algorithm processes each character of the modified string exactly once (with some constant factor overhead) in a linear pass. The key factor in achieving this efficiency is the "center expansion" technique used to find palindromes, which avoids unnecessary character comparisons.

🏹 Space complexity: O(N)
The space complexity of the code is O(N) as well. This is primarily due to the creation of the modified string T, which is constructed by adding extra characters, such as '^', '#', and '$', to the original string. The P array used to store the lengths of palindromes at each position also has a space complexity of O(N) because it is an array of the same length as the modified string. The other variables used in the algorithm (e.g., C, R, and loop counters) have constant space requirements and do not significantly contribute to the space complexity.

So, in terms of both time and space complexity, this code is very efficient for finding the longest palindromic substring in a string.
