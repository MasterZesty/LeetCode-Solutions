class Solution:
    def largestOddNumber(self, num: str) -> str:

        last_odd_index = -1
        
        for i,n in enumerate(num):
            if int(n) % 2 != 0:
                last_odd_index = i
                
        if last_odd_index != -1:
            return num[:last_odd_index+1]
        
        return ""