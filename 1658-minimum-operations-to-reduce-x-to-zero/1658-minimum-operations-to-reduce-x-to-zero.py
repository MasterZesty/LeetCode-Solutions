class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        """
        consider the big array
        now we can divide this array in [leftArray + MiddleSubArray + rightArray]
        now as per question leftArray + rightArray == x
        that means MiddleSubArray =  totalsum - x
        and we have to minimize left and right so we need to maximize MiddleSubArray
        
        so ultimately this problem reduces to find a largest subarray from given array nums
        whose sum is equal to totalsum - x
        
        ref here : https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/discuss/4066508/C%2B%2BEasy-solution-with-explanation-in-O(N)-time-complexity
        """
        """
        n = len(nums)
        total_sum = sum(nums)
        k = total_sum - x
        
        curr_sum = 0
        max_length = -1
        
        left = right = 0
        
        while right < n:
            curr_sum += nums[right]
            
            while (left <= right and curr_sum > k):
                left += 1
                curr_sum -= nums[left]
            
            if curr_sum == k :
                max_length = max(max_length, right - left + 1)
                print(max_length)
                
            right += 1
                
        if max_length == -1:
            return -1
        
        return n - max_length
        """

        n = len(nums)
        i = 0
        j = 0
        maxi = 0
        total_sum = sum(nums)

        if total_sum < x:
            return -1
        if total_sum == x:
            return n

        req_sum = total_sum - x
        curr_sum = 0

        while j < n:
            curr_sum += nums[j]

            while curr_sum > req_sum:
                curr_sum -= nums[i]
                i += 1

            if curr_sum == req_sum:
                maxi = max(maxi, j - i + 1)

            j += 1

        return n - maxi if maxi != 0 else -1




        