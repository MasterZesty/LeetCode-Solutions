class Solution:
    def smallestNumber(self, n: int) -> int:
        ans = -1
        b_n = bin(n)
        b = b_n[2:]
        ans = int('1'*len(b), 2)

        return ans

