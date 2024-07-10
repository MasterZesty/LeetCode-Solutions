class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        
        for i, log in enumerate(logs):
            
            if log == "../" and count > 0:
                count -= 1
                
            if log ==  "./" and count > 0:
                count += 0
            
            if log.count(".") == 0:
                count += 1
            
            # print(f"i {i} log:{log} count:{count}")
                
        return count