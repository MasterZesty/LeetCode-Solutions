class Solution:
    def minimumLength(self, s: str) -> int:
        '''
        We are asked to find the minimum possible length of the string after performing the given operation
        any number of times on a given string. The operation is to remove a prefix and a suffix from the
        string if and only if both are formed from the same characters. Note that both the prefix and
        suffix must be of non-zero length. This implies that if length of the string is 1, or the first
        and last characters of the string are different, we cannot do further operations on it.
        TC : O(n) where n is lenght of string
        SC : O(1)
        '''
        n = len(s)
        l = 0
        r = n -1
        
        while l < r and s[l] == s[r]:
            l += 1
            r -= 1
            
            while l < n and s[l] == s[l-1]:
                l += 1
            
            while r >= 0 and s[r] == s[r+1]:
                r -= 1
                
        return max(0, r-l+1)