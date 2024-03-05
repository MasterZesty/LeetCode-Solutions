class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        one = s.count('1')
        zero = s.count('0')
        
        print(f"{one} {zero}")
        
        if one == 1:
            return "0"*zero + "1"
        
        return "1"*(one-1) + "0"*zero + "1"