class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        0 1 2
        '''
        hm =  {}
        for n in nums:
            hm[n] = hm.get(n, 0) + 1

        n = len(nums)

        for i in range(n):

            if hm.get(0, 0) != 0:
                nums[i] = 0
                hm[0] = hm.get(0, 0) - 1
            elif hm.get(1, 0) != 0:
                nums[i] = 1
                hm[1] = hm.get(1, 0) - 1
            elif hm.get(2, 0) != 0:
                nums[i] = 2
                hm[2] = hm.get(2, 0) - 1

            # print(nums)
        