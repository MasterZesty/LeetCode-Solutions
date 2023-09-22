class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower = s.lower()
        
        str_p = ''.join(char for char in lower if char.isalnum())
        
        # print(str_p)
        if str_p == str_p[::-1]:
            # print(str_p)
            # print(str_p[::-1])
            return True
        
        return False