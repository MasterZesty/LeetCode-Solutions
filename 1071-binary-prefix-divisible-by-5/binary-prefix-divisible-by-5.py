class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        n = len(nums)
        ans = []
        # Binary to decimal rule: new_number = old_number * 2 + current_bit
        cur = 0

        for bit in nums:
            cur  = ( (cur * 2 ) + bit ) % 5
            ans.append(cur == 0)


        return ans