class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        n = len(nums)
        i = 0
        j = n - 1
        count = 0
        mod = pow(10,9) + 7

        while i <= j:

            if nums[i] + nums[j] <= target:

                n_sub = pow(2, j - i)
                count = (count+n_sub)%mod
                # print(n_sub, count, i, j)
                i += 1
            else:
                j -= 1
        


        return count