class Solution:
    def customSortString(self, order: str, s: str) -> str:
        hm = {}
        for char in s:
            hm[char] = hm.get(char, 0) + 1
            
        ans = ""
        
        for o in order:
            ans = ans + hm.get(o,0)*o
            
            if hm.get(o, 0) != 0:
                hm[o] = 0
            
        for c, f in hm.items():
            if f != 0:
                ans = ans + c*f
        
        return ans