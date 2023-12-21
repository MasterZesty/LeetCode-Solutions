class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        #Approch 1 : Tc O(n + nlogn)
        
        # sort the point array
        points.sort()
        
        max_area =  -1
        
        n = len(points)
        
        for i in range(1,n):
            max_area = max(max_area, ( points[i][0] - points[i-1][0]) )
        
        return max_area