class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        n = len(num)
        ans = "-1"
        
        # print(f"num str : {num} | n: {n}")
        
        i = 0
        while i <= n - 3:
            print(i)
            number = num[i:i+3]
            print(number)
            
            if number.count(number[0]) == 3:
                
                if int(number) > int(ans):
                    ans = number
                    
            i += 1
                
        if ans != "-1":
            return ans
        
        return ""