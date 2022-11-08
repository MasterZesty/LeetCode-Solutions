class Solution:
    def maximum69Number (self, num: int) -> int:
        def toggle_num(digit):
            if digit == 9:
                return '6'
            
            return '9'
        
        max_num = num
        
        num_string = str(num)
        # print(num_string)
        
        for i in range(len(num_string)):
            # print(i)
            temp_num =  num_string[:i] + toggle_num(int(num_string[i])) + num_string[i+1:]
            # print(temp_num)
            if int(temp_num) >= max_num:
                max_num = int(temp_num)
                    
        return max_num