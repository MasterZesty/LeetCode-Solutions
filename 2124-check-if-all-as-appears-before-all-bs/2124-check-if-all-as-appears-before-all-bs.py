class Solution:
    def checkString(self, s: str) -> bool:
        # approch
        
        n = len(s)
        
        # handle base case
        if n == 0 or n ==1:
            return True
        
        prev_char = s[0]
        temp_flag = False
        start_char = s[0]
        for i in range(1,len(s)):
            
            # detect second jump point i.e. jump from b to a
            if prev_char!= s[i] and temp_flag == True:
                #print(f'detected second jump')
                if prev_char == 'b' and s[i] == 'a':
                    temp_flag = False
                    break
                else:
                    return False
            
            
            # detect first chnage point i.e. jump from a to b not b to a
            if prev_char != s[i] and temp_flag == False:
                #print(f'detected first jump {s[i]}')
                if prev_char == 'a' and s[i] == 'b':
                    temp_flag = True
                    prev_char = s[i]
                else:
                    return False
                
            # what if there is no jump point
            if i == len(s)-1 and temp_flag == False:
                if start_char == s[i]:
                    if start_char == 'b' and s[i] == 'b':
                        return True
                    if start_char == 'a' and s[i] == 'a':
                        return True
                
            
            
        #print(f'temp_flag {temp_flag}')
        
        
        return temp_flag
                
            
            