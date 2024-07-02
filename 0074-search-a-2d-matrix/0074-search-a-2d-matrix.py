class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def bs(arr, key):
            n = len(arr)
            i = 0
            j  = n -1 
            
            while i <=j:
                mid = (i+j)//2
                
                if arr[mid] == key:
                    return True
                
                if arr[mid] > key:
                    j = mid - 1
                    
                if arr[mid] < key:
                    i = mid + 1
                
            return False
        
        
        for i, row in enumerate(matrix):
            tgt = bs(row, target)
            if tgt:
                return True
            
            
        return False