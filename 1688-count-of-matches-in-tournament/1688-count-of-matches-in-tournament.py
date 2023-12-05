class Solution:
    def numberOfMatches(self, n: int) -> int:
        
        matches = 0
        
        while n > 0:
            # print(f"matches : {matches} start n : {n}")
            
            if n%2 == 0:
                n = n //2
                matches += n
                
            else:
                n = (n-1) //2
                matches += n
                n += 1
                
            if n == 1:
                n = 0
            
            # print(f"matches : {matches} end n {n}")
                
        return matches