class Solution(object):
    def moveZeroes(self, nums):
        append_times=nums.count(0)
        for i in range(append_times):
            nums.remove(0) #  Delete the front zero
            nums.append(0) # append it at the end of nums, the times of the addition and substraction shall be equal