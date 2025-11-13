class Solution:
    def maxOperations(self, s: str) -> int:
        n = len(s)
        i = 0
        c_ones = 0
        ans = 0

        while i < n:

            if s[i] == '1':
                c_ones += 1


            if i > 0 and i - 1 < n and s[i] == '0' and s[i-1] == '1':
                ans += c_ones
                # print(f"ans {ans}")
                
            
            i += 1

        return ans