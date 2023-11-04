class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        
        if len(left) == 0:
            
            # check edge
            if len(right) == 1 and right[0] == 0:
                return 0
            
            return n - min(right)
        
        if len(right) == 0:
            
            # check if left ant is at edge or not
            if len(left) == 1 and left[0] == 0:
                return 0
            
            return max(left)
                

        
        # in general case time for last ant either from left or right 
        return max(max(left),n - min(right))
        