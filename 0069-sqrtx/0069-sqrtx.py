class Solution:
    def mySqrt(self, x: int) -> int:
        
        # nums = [m*m for m in range(1,x+1)]
        target = x
        # print(f"nums:{nums} | target:{target}") 
        
        if x == 0:
            return 0
        
        if x == 1:
            return 1

        
        n = x*x
        i = 0
        j = n -1
        
        while i <= j:
            
            mid = (i+j)//2
            
            nums_mid = mid*mid
            
            if nums_mid == target:
                return mid
            
            if nums_mid > target:
                j = mid - 1
                
            if nums_mid < target:
                i = mid + 1
        
        # print(f"mid : {mid} | i:{i} |  j:{j}")
        
        if nums_mid < target:
            return mid
        
        return mid - 1