class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # array is sorted so we can use binary search
        # as we want TC (log n)
        s = -1
        e = -1
        
        n = len(nums)
        
        
        # find first elemnt staring of target
        
        l = 0
        r = n - 1
        
        while l <= r:
            print(nums[l:r])
            
            mid = l + (r - l)//2
            
            if nums[mid] == target:
                # print(f'got the key at idx : {mid} but making sure first ocurrnace')
                if mid == 0 or nums[mid-1] != target:
                    s = mid
                    break
                else:
                    r = mid - 1
            
            if nums[mid] > target:
                # elemnt is greter than target search in left
                r = mid - 1
                
            if nums[mid] < target:
                # elemen is smaller than target search in right
                l = mid + 1
                
        # find last element of target
        l = 0
        r = n - 1
        
        while l <= r:
            print(nums[l:r])
            
            mid = l + (r - l)//2
            
            if nums[mid] == target:
                # print(f'got the key at idx : {mid} but making sure last ocurrnace')
                if mid == (n - 1) or nums[mid+1] != target:
                    e = mid
                    break
                else:
                    l = mid + 1
            
            if nums[mid] > target:
                # elemnt is greter than target search in left
                r = mid - 1
                
            if nums[mid] < target:
                # elemen is smaller than target search in right
                l = mid + 1
                
        return [s,e]
        
        