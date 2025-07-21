class Solution:
    def makeFancyString(self, s: str) -> str:
        count = 0
        prev_char = s[0]
        ans = ''

        for i, c in enumerate(s):
            # print(f"itr char{c} at {i}")

            # take descision if we want to remove it 
            # if prev_char == c and count > 2:
            #     # remove
            #     print(f"remove char{c} at {i}")

            if prev_char == c and count < 2:
                ans = ans + c

            if prev_char != c:
                count = 0
                ans = ans + c



            count += 1
            prev_char = c


        return ans