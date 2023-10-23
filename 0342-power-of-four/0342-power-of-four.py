class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        from math import log
        from math import modf
        
        if n == 0:
            return False
        
        if n > 0:
        
            x = log(n)/log(4)

            # print(x)

            dec, integer = modf(x)

            if dec == 0:
                return True

            return False
        else:
            return False
        