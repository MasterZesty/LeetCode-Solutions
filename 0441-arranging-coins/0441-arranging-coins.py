class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        def get_sum(n):
            
            s = (n * (n + 1))/2
            
            return s
        
        left = 1
        right = n
        
        if n == 1:
            return 1
        
        while left <= right:
            
            mid =  ( left + right )//2
            
            if get_sum(mid) == n:
                return mid
            
            if get_sum(mid) > n:
                right = mid - 1
                
            if get_sum(mid) < n:
                left = mid + 1
                
            # print(f"l{left} r{right} m{mid}")
                
        # print(f"l{left} r{right} m{mid}")       
        return right