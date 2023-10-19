class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        stack_s = []
        stack_t = []
        
        for char in s:
            if char == '#':
                if len(stack_s) != 0:
                    stack_s.pop()
                
            else:
                stack_s.append(char)
                
        # print(f'stack_s : {stack_s}')
        
        for char in t:
            if char == '#':
                if len(stack_t) != 0:
                    stack_t.pop()
            else:
                stack_t.append(char)
                
        #print(f'stack_t : {stack_t}')
        
        if ''.join(stack_s) == ''.join(stack_t):
            return True
        
        return False