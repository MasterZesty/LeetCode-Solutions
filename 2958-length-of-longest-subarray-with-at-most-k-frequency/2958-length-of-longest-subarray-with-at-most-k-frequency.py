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
            
        