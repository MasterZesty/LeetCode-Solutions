class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        
        t = ''.join(map(str,num))
        
        num = str(k + int(t))
        
        num = list(num)
        
        t2 = list(map(int,num))
        
        return t2