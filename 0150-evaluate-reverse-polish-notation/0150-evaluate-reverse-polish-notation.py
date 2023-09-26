class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
                
        op = ['+', '-', '*', '/']
        
        if len(tokens) == 1:
            if tokens[0] not in op:
                return int(tokens[0])
        
        
        stack = []
        
        for t in tokens:
            #print(stack)
            if t not in op:
                stack.append(t)
            else:
                
                if len(stack) < 1:
                    #print('stack len < 1 .. breaking')
                    return
                    
                b = int( stack.pop() )
                a = int( stack.pop() )
                
                if t == '+':
                    stack.append(a+b)
                    
                if t == '-':
                    stack.append(a-b)
                    
                if t == '*':
                    stack.append(a*b)
                    
                if t == '/':
                    stack.append(a/b)
                    
        #print(stack)
        
        return int( stack.pop() )
                
                
        