class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # TC O(m+n) SC (m+n) O(1)
        # use merge sort kind of : ref : https://www.interviewbit.com/blog/merge-two-sorted-arrays/
        
        m = len(nums1)
        n = len(nums2)
        
        # array to store nums1+nums2 sorted array
        nums = [None]*(m+n)
        
        i = 0
        j = 0
        k = 0
        
        while i < m and j < n:
            
            if nums1[i] < nums2[j]:
                nums[k] = nums1[i]
                i += 1
                k += 1
                
            else:
                nums[k] = nums2[j]
                j += 1
                k += 1
                
        #print(nums,i,j,k,m,n)
        
        while i < m:
            nums[k] = nums1[i]
            k += 1
            i += 1
        
        while j < n:
            nums[k] = nums2[j]
            k += 1
            j += 1
            
        #print(nums,i,j,k)
        
        x = len(nums)
        mid = x//2
        if x % 2 != 0:
            return nums[mid]
        
        return (nums[mid]+nums[mid-1])/2
        
        # return -1