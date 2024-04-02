class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mp = {}
        pm = {}
        
        for sc, tc in zip(s,t):
            
            if mp.get(sc, 0) == 0:
                if pm.get(tc, 0) == 0:
                    pm[tc] = sc
                
                if pm[tc] != sc:
                    return False
                
                mp[sc] = tc
                continue
                
            if mp[sc] != tc:
                return False
        
        return True