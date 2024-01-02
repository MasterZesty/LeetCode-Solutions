class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        
        for i,num in enumerate(nums):
            
            # process for num
            if i == 0:
                ans.append([num])
                
            else:
                flag = True
                for i,a in enumerate(ans):
                    if num not in a:
                        ans[i].append(num)
                        flag = False
                        break
                        
                if flag:
                    ans.append([num])
        
        # print(f"ans: {ans}")
        
        return ans