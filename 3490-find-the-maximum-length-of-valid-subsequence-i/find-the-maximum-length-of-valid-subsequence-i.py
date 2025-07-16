class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        c_odd = 0
        c_even = 0
        first_odd = False
        first_even = False
        c_eo = 0
        c_oe = 0
        for i,v in enumerate(nums):
            r = v % 2 
            if r == 0:
                c_even += 1
            
            if r != 0:
                c_odd += 1

            if first_even and r != 0:
                c_eo += 1
                first_even = False

            if first_odd and r == 0:
                c_oe += 1
                first_odd = False

            if r == 0 and not first_even:
                first_even = True
                c_eo += 1

            if r != 0 and not first_odd:
                first_odd = True
                c_oe += 1


        print([ans, c_odd, c_even, c_eo, c_oe])
        ans = max([ans, c_odd, c_even, c_eo, c_oe])

        return ans

