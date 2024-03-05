class Solution:
    def minimumLength(self, s: str) -> int:
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