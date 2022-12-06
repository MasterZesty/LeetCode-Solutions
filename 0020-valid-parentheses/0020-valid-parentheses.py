class Solution:
    def isValid(self, s: str) -> bool:
        open_para = ['{','[','(']
        # close_para = ['}',']',')']
        lookup = {"}":"{",")":"(","]":"["}

        # from collections import deque
        from collections import deque

        stack = deque()

        for char in s:
            if char in open_para:
                # print('char ',char)
                stack.append(char)

            elif (len(stack) != 0) and (lookup[char] == stack[-1]):
                stack.pop()
            
            else:
                return False

        return (len(stack) == 0)

                


