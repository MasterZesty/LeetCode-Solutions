class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # approch 1
        s_ptr = 0
        t_ptr = 0
        
        len_t = len(t)
        len_s = len(s)
        
        if len_s == 0:
            return True
        
        if len_s > len_t:
            return False
        
        count = 0
        
        while t_ptr < len_t and s_ptr < len_s:
            
            if t[t_ptr] == s[s_ptr]:
                # we got the same chars
                count += 1
                s_ptr += 1
                t_ptr += 1
            else:
                t_ptr += 1
                
        if count == len_s:
            return True
        
        return False