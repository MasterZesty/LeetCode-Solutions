class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        """
        this solution is from : 
        1. https://leetcode.com/problems/find-all-possible-stable-binary-arrays-i/discuss/5080485/Python-solution-in-strict-O(n3)
        2. https://leetcode.com/problems/find-all-possible-stable-binary-arrays-i/discuss/5080450/python-11-lines
        submitting for ref 
        """

        MOD = 10 ** 9 + 7
        def dp(zeros, ones, remaining, memo):
            if ones <0 or zeros < 0:
                return 0
            if zeros == 0 and ones == 0:
                return 1
            if (zeros, ones, remaining) in memo:
                return memo[(zeros, ones, remaining)]

            res = 0
            res = (res + (dp(zeros - 1, ones, remaining-1, memo) if remaining > 0 else 0)) % MOD
            res = (res + dp(ones-1, zeros, limit-1, memo)) % MOD
                    
            memo[zeros, ones, remaining] = res
            return res
        memo = {}
        return dp(zero, one, limit, memo)