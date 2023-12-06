class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        
        i = 0
        j = len(removable)
        ans = 0
        
        while i <= j:
            mid = i + (j - i) // 2
            s1 = list(s)
            
            for k in range(mid):
                s1[removable[k]] = 'A'
            
            l = len(p)
            k = 0
            
            for char in s1:
                if k < l and char == p[k]:
                    k += 1
            
            if k == l:
                ans = mid
                i = mid + 1
            else:
                j = mid - 1
        
        return ans

            
                
            
        