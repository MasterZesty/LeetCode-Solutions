class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        
        # Chebyshev distance
        d = max( abs (sx-fx), abs(sy-fy) )
        
        # handle special case
        if d == 0:
            return (t > 1 or t == 0)
        
        # time required t should be leass than or equal to max distance
        return d <= t
            
        