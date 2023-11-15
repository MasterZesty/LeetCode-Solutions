class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        print(f'arr before sort : {arr}')
        arr.sort()
        print(f'sorted arr : {arr}')
        
        # The value of the first element in arr must be 1
        if arr[0] != 1:
            arr[0] = 1
            
        n = len(arr)
        
        for i in range(1,n):
            
            if (arr[i] - arr[i-1]) > 1:
                arr[i] = arr[i-1] + 1
                
        print(f'final arr : {arr}')
        
        return arr[-1]
            
        