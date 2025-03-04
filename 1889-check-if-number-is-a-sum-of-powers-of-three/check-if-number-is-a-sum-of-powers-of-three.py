class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        """
         figure out whether a number can be represented by a base 3 ternary system where 
         none of the powers of 3 are duplicated, i.e. the powers of 3 must be distinct.
        """
        while n > 0:
            if n % 3 == 2:
                return False

            n = n // 3

        
        return True