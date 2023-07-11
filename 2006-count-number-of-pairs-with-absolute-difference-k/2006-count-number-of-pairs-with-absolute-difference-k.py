class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        # approch 1 
        # time complexity - O(n2)
        # space complexity O(1)
        
        # n = len(nums)
        # ans = 0
        
        # for i in range(n):
            
            # for j in range(i+1,n):
                
                # if abs(nums[i]-nums[j]) == k:
                    # print(nums[i],nums[j])
                    # ans += 1
                
        # return ans
        
        # apporch 2 following apporch does not work due to 
        # we make hashmap first and then finding paris which violtes i<j ==> i>j => we are geeting extra paris
        # hence we are geeting wrong answers. we need to make hmap on the go.
        # ans = 0
        # hm_nums = dict()
        
#         for i,val in enumerate(nums):
#             if val not in hm_nums.keys():
#                 hm_nums[val] = 1
                
#             else:
#                 hm_nums[val] += 1
                
#         for i,val in enumerate(nums):
#             # abs_val = abs(val-k)
#             if abs_val in hm_nums.keys():
#                 if k == 0:
#                     ans += hm_nums[val] - 1
                
#                 else:
#                     ans += hm_nums[val]

        # apporch 3 - make hmap on the go and consider |x-y|=k => y = x + k and y = x - k
        ans = 0
        f = {}
        for i in nums:
            ans += f.get(i - k, 0) + f.get(i + k, 0)
            f[i] = f.get(i, 0) + 1

        return ans
            
        