class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_d = -1
        n = len(nums)

        for i in range(0,n-1):

            for j in range(i+1, n):
                # print(i,j)

                if nums[i] < nums[j]:
                    curr_d =  nums[j] - nums[i]
                    max_d = max(max_d, curr_d)


        return max_d
