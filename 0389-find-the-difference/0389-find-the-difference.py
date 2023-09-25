class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        if len(s) == 0:
            return t
        
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))
        
        n = len(s)
        m = len(t)
        
        ptr = 0
        while ptr < n:
            if s[ptr] != t[ptr]:
                return t[ptr]
            ptr += 1
        
        
        return t[-1]