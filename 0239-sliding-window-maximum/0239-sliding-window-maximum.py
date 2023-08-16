class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # approch 1 : bruteforce - > Time Limit Exceeded :))
        
        # print(f'nums arr : {nums}')
        
#         l = 0
#         r = k
#         n = len(nums)
        
#         m_s_w = []
        
#         while r<=n:
#             # print(f'l {l} r {r} curr window is : {nums[l:r]}  max {max(nums[l:r])}')
            
#             t_max = max(nums[l:r])
            
#             m_s_w.append(t_max)
            
#             l += 1
#             r += 1
        
#         # print(f'm_s_w : {m_s_w}')
        
#         return m_s_w
        
        # apporch 2 : reduce time complexity and space complexity aka optimization
        # ref : https://youtu.be/EHCGAZBbB88
        #       https://youtu.be/xFJXtB5vSmM
        

        '''
        1. calculations (make a list and if i'm at j then remove all elements < j )
        2. ans -> calculations (list.front)
        3. slide the window ---> i++ j++
                            |
                            ---> calculation remove (before doing i++ check if that elemet
                                                     is present in list list.front = element -> pop element
        '''

#         i=0
#         j=0
#         n = len(nums)
        
#         ans = []  # stores max of subarrays
        
#         helper = []
        
#         while j<n:
            
#             # 1. calculation
#             while len(helper) > 0 and helper[-1] < nums[j]:
#                 helper.pop()
            
#             helper.append(nums[j])
            
#             #2. ans
#             # append the maximum value to the ans list
#             # ans.append(helper[0])
#             if j - i + 1 == k:
#                 ans.append(helper[0])
            
#             # 3. slide the window
#             if i <= j - k:
#                 helper.pop(0)
                
#             i += 1
#             j += 1
            
#         return ans
                
        n = len(nums)
        ans = []  # stores max of subarrays
        helper = []  # stores indices, not values
        i, j = 0, 0

        while j < n:
            # Remove indices that are out of the current window
            while len(helper) > 0 and helper[0] < j - k + 1:
                helper.pop(0)

            # Remove indices of smaller elements as they are no longer useful
            while len(helper) > 0 and nums[helper[-1]] < nums[j]:
                helper.pop()

            helper.append(j)

            # Add the maximum value for the current window to the answer
            if j >= k - 1:
                ans.append(nums[helper[0]])

            i += 1
            j += 1

        return ans





            
            
            
            
            
            
            
            
            
            
            
            
        
        
        
        