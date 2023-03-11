class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        
        if event1[0] <= event2[0] <= event1[1]:
            return True
        
        if event2[0] <= event1[0] <= event2[1]:
            return True
        
        return False
        
        
        
        