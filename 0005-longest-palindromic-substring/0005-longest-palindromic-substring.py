class Solution:
    
    max_len = 0
    low = 0
    
    def expandAroundCenter(self, j, k, s):
            '''
            j expands to l
            k expands to r
            '''
            # print(f'expand around centre palindrome.. {s[j:k]}')
            
            # print(f'start : j : {j} k : {k}')
            
            n = len(s)
            
            while ( (j >= 0) and ( k < n) and (s[k] == s[j]) ):
                j -= 1
                k += 1
            
            # print(f'end : j : {j} k : {k}')
            # print(f'm len : {self.max_len} t len : {k - j - 1}')
            
            
            if self.max_len < (k - j - 1):
                # new palindrome max length and low
                self.max_len = k - j - 1
                self.low = j + 1
                
            # print(self.max_len, self.low)
                
    def longestPalindrome(self, s: str) -> str:
        '''
        we can selec and index and can expand l and r (valid expansion)
        TC : O(n^2)
        SC : 
        '''
        
        n = len(s)
        
        if n < 2:
            return s
        
        
                
        
        # in first iteration let us select index to expand around
        for i in range(n):
            
            # Odd-Length Palindromes:
            self.expandAroundCenter(i, i, s)
            
            # Even-Length Palindromes:
            self.expandAroundCenter(i, i + 1, s)
        
        
        #print(f'low : {self.low} len: {self.max_len} ans: {s[self.low:self.low+self.max_len]}')
        return s[self.low:self.low+self.max_len]
        
        
        
        