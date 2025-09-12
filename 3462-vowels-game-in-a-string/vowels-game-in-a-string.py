class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = ["a", "e", "i", "o", "u"]

        for v in vowels:
            if v in s:
                return True # alice wins

        
        return False
