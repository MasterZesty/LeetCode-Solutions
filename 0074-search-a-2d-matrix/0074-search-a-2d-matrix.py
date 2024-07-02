class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        TC - O(mlogn) ==> O(log(m * n)) (flattening the matrix virtually)
        '''
        '''
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
        '''
        
        m = len(matrix)
        n = len(matrix[0])

        i = 0
        j = m*n - 1
        
        while i <= j:
            
            mid = (i+j)//2
            mid_value = matrix[mid // n][mid % n]
            
            if mid_value == target:
                return True
            
            if mid_value > target:
                j = mid - 1
                
            if mid_value < target:
                i = mid + 1
                
        return False