class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        
        nums.sort(reverse=True)
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                '''
                Now, the reason for ans += i + 1 is that i represents the index of 
                the current element in the sorted list, and i + 1 corresponds to 
                the count of elements smaller than the current one. As we traverse the 
                sorted list from the highest number to the lowest, for each new unique 
                number encountered, all the previous numbers (smaller than the current one) 
                need to be increased to match the current number. 
                
                Therefore, i + 1 signifies the count of elements that need to be operated on 
                to make them equal to the current number.
                '''
                ans += i + 1
                
        return ans