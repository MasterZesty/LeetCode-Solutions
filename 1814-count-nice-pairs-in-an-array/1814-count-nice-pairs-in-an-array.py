class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        
        # approch 1 : TC : O(n^2) => TLE
#         nice_pair = 0
        
#         MOD = 10**9 + 7
        
#         n  = len(nums)
        
        
#         for i in range(n-1):
            
#             for j in range(i+1,n):
                
#                 is_nice_pair = ( nums[i] - int(str(nums[i])[::-1] ) )  == ( nums[j] - int(str(nums[j])[::-1] ) )
                
#                 if is_nice_pair:
#                     # print(f' {nums[i]} - {int(str(nums[i])[::-1] )} == {nums[j]} - {int(str(nums[j])[::-1] )} ')
#                     nice_pair += 1
                
#         return nice_pair

        differences = {}
        nice_pair = 0
        MOD = 10**9 + 7
        
        for num in nums:
            diff = num - int(str(num)[::-1])
            nice_pair +=  differences.get(diff,0)
            differences[diff] = differences.get(diff,0) + 1
            
        return nice_pair % MOD
                                                            