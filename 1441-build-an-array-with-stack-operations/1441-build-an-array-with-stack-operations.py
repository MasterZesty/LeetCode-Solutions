class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        stack = []
        
        for i in range(1,n+1):
            #print(f'element is {i}')
            if stack == target:
                return ans
            
            ans.append("Push")
            stack.append(i)
            if i not in target:
                ans.append("Pop")
                stack.pop(-1)
            
            
        return ans