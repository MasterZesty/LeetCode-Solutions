class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        '''
        This code maintains a sliding window represented by the left and right pointers. 
        It uses a dictionary freq to keep track of the frequency of each element within 
        the current window. Whenever the frequency of any element exceeds k, it shrinks 
        the window from the left side until all frequencies become less than or equal to 
        k. The maximum length of such a valid window is continuously updated and returned 
        at the end.
        '''
        
        freq = {}
        left = 0
        max_length = 0

        for right, num in enumerate(nums):
            freq[num] = freq.get(num, 0) + 1

            while freq[num] > k:
                freq[nums[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
        
#         # step 1 : do pre processing
        
#         m = len(nums)
        
#         running_max_k = [ 0 for i in range(m)]
#         running_max_k[0] = 1
        
#         hm = {}
        
#         for i,n in enumerate(nums):
            
#             hm[n] = hm.get(n,0) + 1
            
#             t = hm.get(n,0)
            
#             if t > running_max_k[i-1] and i != 0:
#                 running_max_k[i] = t
                
#             elif i !=0:
#                 running_max_k[i] = running_max_k[i-1]
                
#         print(f"running_max_k {running_max_k}")
        
#         start = running_max_k.index(1)
#         end = 0
        
#         for i,n in enumerate(running_max_k):
#             if n <= k:
#                 end = i
                
#         print(f"start : {start} end: {end} {nums[start]}| ans is : {nums[start:end+1]}")
        
#         return len(nums[start:end+1])
            
        