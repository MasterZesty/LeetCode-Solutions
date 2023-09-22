class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0 for _ in nums]
        # print(f'ans 1 : {ans}')
        
        product = 1
        f = False
        count_zero = 0
        for n in nums:
            if n != 0:
                product *= n
                f = True
            else:
                count_zero += 1
                
        # print(f'product : {product} | zero count {count_zero}')
        
        if not f:
            return ans
        
        for i,n in enumerate(nums):
            if n != 0:
                if count_zero > 0:
                    ans[i] = 0
                else:
                    ans[i] = product//n
                
            else:
                if count_zero >= 2:
                    ans[i] = 0
                else:
                    ans[i] = product
                
                
        # print(f'ans 2 : {ans}')
        
        return ans
        