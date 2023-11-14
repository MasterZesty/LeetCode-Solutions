## Intuitionn/Approch
​
1. we have a string s of length 3 <= s.length <= 10^5
2. find all subsequence of length 3 from s => let us say count is m
3. now from m subsequences find uniqie count of palindromes which is our ans.
​
## Appproch 2
this problem is kind of similar to  The Longest Palindrome Subsequence
​
## Approch 3
1. find first occurance of char
2. find last occurance of same char
3. now we have first and last occurance so we have _ _ _ => a _ a
4. to fill gap find numer of unique chars between first and last occurance
5. entire logic is based on we need too find palindrome of lenght 3
​
https://leetcode.com/problems/unique-length-3-palindromic-subsequences/discuss/4285072/Iterative-Solution-oror-Explained-Intuition
https://leetcode.com/problems/unique-length-3-palindromic-subsequences/discuss/4285239/VideoGive-me-8-minutes-How-we-think-about-a-solution
https://leetcode.com/problems/unique-length-3-palindromic-subsequences/discuss/4285483/Beats-96.16-oror-Easiest-Approach-oror-Beginner-Friendly-Explanation