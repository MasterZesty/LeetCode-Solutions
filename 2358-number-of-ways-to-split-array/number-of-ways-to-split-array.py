class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0

        prefix_sum = [0 for _ in range(n+1)]
        prefix_sum[0] = nums[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]

        # print(prefix_sum)

        for i in range(n-1):
            #lets say i is potential valid split
            l = prefix_sum[i]
            r = prefix_sum[n-1] - l
            # print(i,l,r)
            if l >= r:
                count += 1

        return count