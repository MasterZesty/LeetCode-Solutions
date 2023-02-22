class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def check(w,weights,days):
            day = 1
            wt = 0
            for i in range(len(weights)):
                if (wt+weights[i]>w):
                    wt = weights[i]
                    if (wt>w):
                        return 0
                    day += 1
                else:
                    wt += weights[i]
                    
            return day<=days
                
        
        
        
        
        
        
        
        l = 1;
        r = sum(weights)
        
        ans = -1
        
        while(l<=r):
            mid = l + (r-l)//2
            
            if (check(mid,weights,days)):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
                
        return ans