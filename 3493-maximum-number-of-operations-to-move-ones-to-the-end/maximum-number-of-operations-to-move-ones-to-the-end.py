class Solution:
    def maxOperations(self, s: str) -> int:
        '''
        Scan the string.
        As we scan, count how many 1s we've seen so far (counted_ones).
        Every time we start a new zero block (0 after 1), all previous 1s will cross it eventually -> so add counted_ones to the answer.
        '''
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