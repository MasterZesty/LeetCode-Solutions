class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        
        n = len(s)
        ans = []
        
        i = 0
        j = 0
        
        while j < n:
            
            j += k
            
            if len(s[i:j]) != k:
                ans.append( s[i:j] + fill*(k - len(s[i:j]) ) )
            
            else:
                
                ans.append(s[i:j])
            
            i = j

            
        return ans
            