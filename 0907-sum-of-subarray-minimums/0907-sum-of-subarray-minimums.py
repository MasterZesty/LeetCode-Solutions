class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        '''
        Apporch1: TC O(n^2)
        ref: https://codecurse.medium.com/sum-of-all-subarrays-of-an-array-438045da7897
        '''
        '''
        MOD = 10**9 + 7
        ans = 0
        n = len(arr)
        
        for i in range(n):
            
            for j in range(i,n):
                
                # print(f"subarray from i: {i} to j: {j}")
                print(arr[i:j+1])
                ans += min(arr[i:j+1])
                ans %= MOD
                
        return ans
        '''
        
        '''
        ref: https://youtu.be/aX1F2-DrBkQ?si=pJ-R6QpyX9Bay0cT
        '''
        MOD = 10**9 + 7
        stack = [] # (index, num)
        res = 0

        for i, n in enumerate(arr):
            # Pop elements from the stack while they are greater than the current element
            while stack and n < stack[-1][1]:
                j, m = stack.pop()
                left = j - stack[-1][0] if stack else j + 1
                right = i - j
                res =  ( res + m*left*right) % MOD
                
            stack.append((i,n))
            
        
        for i in range(len(stack)):
            j, n = stack[i]
            left = j - stack[i - 1][0] if i > 0 else j + 1
            right = len(arr) - j
            res = (res + n*left*right) % MOD
            
        return res