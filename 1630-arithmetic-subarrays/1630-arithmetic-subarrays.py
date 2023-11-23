class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        n = len(l)
        ans = [True]*n
        idx = 0
        
        
        for left,right in zip(l,r):
            
            # print(left,right)
            
            arr = nums[left:right+1]
            
            arr.sort()
            
            diff = arr[1] - arr[0]
            
            for i in range(2,len(arr)):
                
                if arr[i] - arr[i-1] != diff:
                    ans[idx] = False
            
            idx += 1
            
            
            
        return ans