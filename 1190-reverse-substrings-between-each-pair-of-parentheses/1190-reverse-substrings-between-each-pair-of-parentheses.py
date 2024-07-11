class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        stack = []
        n = len(s)
        i = 0
        while i < n:
            
            c = s[i]
            # print(f"c:{c}")
            
            if c == "(" or (ord(c) >= 97 and ord(c)<=122):
                stack.append(c)
                
            if c == ")":
                ts = ""
                while stack[-1] != "(":
                    e = stack.pop()
                    ts = ts + e
                    
                e = stack.pop()
                    
                for t in ts:
                    stack.append(t)
                
            # print(f"i:{i} stack:{stack}")
            i += 1
        
        # print(f"final stack:{stack}")
        ans = ""
        for x in stack:
            ans = ans + x
        
        return ans
            
                