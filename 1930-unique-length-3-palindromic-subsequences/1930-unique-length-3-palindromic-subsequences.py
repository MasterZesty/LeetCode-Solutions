class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # approch 3
        first = {}
        last = {}
        
        n = len(s)
        
        for i in range(n):
            if s[i] not in first:
                first[ s[i] ] = i
                
        for j in range(n-1,-1,-1):
            if s[j] not in last:
                last[ s[j] ] = j
        
        
        # print(f'first : {first} last : {last}')
        
        ans = 0
        
        for c in first:
            f = first[c]
            l = last[c]
            # print(f,l,s[f+1:l])
            count = len(set(s[f+1:l]))
            ans += count
        
        return ans