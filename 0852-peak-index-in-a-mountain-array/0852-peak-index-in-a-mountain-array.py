class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        left = 0
        right = n - 1
        
        
        while left < right:
            
            mid = (left+right)//2
            
            if mid + 1 <= n - 1 and mid - 1 >= 0 and arr[mid] > arr[mid+1] and arr[mid] > arr[mid-1]:
                return mid
            
            if mid + 1 <= n - 1 and mid - 1 >= 0 and arr[mid] < arr[mid+1] and arr[mid] > arr[mid-1]:
                left = mid + 1
                
            else:
                right = mid
                
                
        return left