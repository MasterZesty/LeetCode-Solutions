class Solution:
    def maxArea(self, height: List[int]) -> int:
        # approch 1 : TC O(n^2)
        '''
        max_area = 0
        lptr = 0
        rptr = 0
        n = len(height)
        
        while lptr < n:
            # print(f'lptr {lptr} rptr {rptr}')
            rptr = lptr
            while rptr < n-1:
                # print(f'-- lptr {lptr} rptr {rptr}')
                rptr += 1
                w = rptr - lptr
                h = min(height[rptr], height[lptr])
                t_area =  w*h
                max_area = max(max_area,t_area)
                
            lptr += 1
            
        return max_area
        '''
        
        # approch 2 : The two-pointer approach  reduce the time complexity to O(n).
        max_area = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            # Calculate the width and height
            width = right - left
            min_height = min(height[left], height[right])
            
            # Calculate the current area
            current_area = width * min_height
            
            # Update the maximum area
            max_area = max(max_area, current_area)
            
            # Move the pointers
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area