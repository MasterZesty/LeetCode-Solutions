class Solution:
    def countHomogenous(self, s: str) -> int:
        # approch 1
        n = len(s)
        i = 0
        j = 0
        count = 0
        MODULO = 10**9 + 7
        
        while i < n or j < n:
            # print(f'i : {i} | j : {j}')
            
            while j < n and s[i] == s[j]:
                j += 1
                
            # print(f'i : {i} | j : {j} => substring : {s[i:j]} len : {j - i}')
            
            l = j - i
            count += (l*(l+1))//2
            
            i = j
        
        return count % MODULO