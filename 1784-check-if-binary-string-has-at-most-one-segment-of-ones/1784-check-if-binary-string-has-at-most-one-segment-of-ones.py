class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        #
        #
        '''
        Solution 1: Check for "01"
        Since the input string cannot s cannot have any leading zeroes 
        and must contain at most one contiguous segment of 1s, we need 
        to check if "01" is present in s or not. If it is present, we 
        can return False, else True.

        A few testcases to help understand the intuition:

        1100 - True
        11001 - False (since 01 is present).
        111111000000 - True
        1101010100 - False
        1 - True
        1111110000111 - False
        '''
        return "01" not in s