class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
#         def check_valid_para(s):
#             stack = []
#             for i in s:
#                 if i == '(':
#                     stack.append(i)
                
#                 if i == ')' and len(stack) != 0:
#                     e = stack.pop(-1)
                    
                
#             if len(stack) == 0:
#                 return True
            
#             return False
            
            
            
#         s = '()'
#         t = s*n
#         print(t)
        
#         import itertools
#         a_string = t
#         string_permutations = itertools.permutations(a_string)
#         string_permutations = list(string_permutations)
#         string_permutations = list(set([''.join(permutation) for permutation in string_permutations]))

#         print((string_permutations))
        
#         para_l = []
#         for i,val in enumerate(string_permutations):
#             if val[0] != ')':
#                 #print(val)
#                 if check_valid_para(val):
#                     print(val)
#                     para_l.append(val)
                    
#         return para_l

          # apporch 2
            
        ans = []
            
        stack = [('(',n-1,n)] #  ==> [('(',no of opening para, no of closing para)]
        
        while stack:
            item = stack.pop()
            
            string = item[0]
            open_para = item[1]
            close_para = item[2]
            
            if open_para == 0 and close_para == 0:
                ans.append(string)
            else:
                if open_para != 0:
                    stack.append((string+'(',open_para-1,close_para))
                if close_para > open_para:
                    stack.append((string+')',open_para,close_para-1))
            
        return ans
            
            
          