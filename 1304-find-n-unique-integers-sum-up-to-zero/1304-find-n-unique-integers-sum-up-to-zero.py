class Solution:
    def sumZero(self, n: int) -> List[int]:
        last_element:int
        
        unique_int = [x for x in range(1,n)]
        N = n-1
        last_element = N*(N+1)//2
        unique_int.append(-last_element)
        
        return unique_int