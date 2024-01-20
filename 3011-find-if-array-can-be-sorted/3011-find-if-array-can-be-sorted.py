class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        sorted_nums = sorted(nums)
        n = len(nums)
        # print(f"sorted nums {sorted_nums}")
        # print(f"unsorted nums {nums}")
        for i in range(n):
            for j in range(0, n-i-1):
                if (str(bin(nums[j])).count('1') == str(bin(nums[j+1])).count('1')):
                    if nums[j] > nums[j+1]:
                        nums[j], nums[j+1] = nums[j+1], nums[j]
                    
        # print(f"final nums {nums}")
        
        return sorted_nums == nums
        