class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        
        # approch 1 : brutceforce approch
        
        ans = []
        n = len(A)
        
        for i in range(n):
            # print(f'index {i}')
            count = self.helper_check_common_element(A[:i+1],B[:i+1])
            ans.append(count)
        
        return ans
    
    def helper_check_common_element(self,A,B):
        '''this function return count of numbers that are present
        in A and B both'''
        
        # print(f'arr A : {A} | arr B : {B}')
        
        common_elements = 0
        
        hmap_a = {}
        hmap_b = {}
        
        n = len(A)
        
        # populate hasmap
        for i in range(n):
            if A[i] not in hmap_a:
                hmap_a[A[i]] = 1
            else:
                hmap_a[A[i]] += 1
                
            if B[i] not in hmap_b:
                hmap_b[B[i]] = 1
            else:
                hmap_b[B[i]] += 1
            
            
        # print(f'{hmap_a} {hmap_b}')     
        
        for i in hmap_a.keys():
            if i in hmap_b.keys():
                # print(f'{i}')
                common_elements += min(hmap_a[i],hmap_b[i])
                # print(f'count : {count}')
        
        # print(f'arr A : {A} | arr B : {B} | count: {common_elements}')
        return common_elements