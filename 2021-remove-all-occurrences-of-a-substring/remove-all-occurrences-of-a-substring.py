class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        
        stack = []

        for i,v in enumerate(s):
            # print(f"------- i:{i}, v:{v} -------")
            stack.append(v)
            temp_s = ""
            if v == part[-1]:
                for i in range(len(part)-1,-1 , -1):
                    if len(stack) != 0:
                        m = stack.pop()
                        # print(f"pop m :{m}")
                        temp_s += m
                        # print(f"temp_s:{temp_s}, part[i]:{part[i]}")
                        if m != part[i]:
                            break

            # print(f"i:{i} stack:{stack}")
        
            # print(f"temp_s:{temp_s}")

            if temp_s[::-1] != part:
                for t in temp_s[::-1]:
                    stack.append(t)

            # print(f"stack:{stack}")

        # print(stack)
        ans = ""
        while stack:
            ans += stack.pop()

        return ans[::-1]