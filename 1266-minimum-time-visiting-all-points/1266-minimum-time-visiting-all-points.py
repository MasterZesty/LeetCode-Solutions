class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        
        def find_path_with_min_time(source:List[int], destination: List[int]) -> int:
            '''
            x1, y1 | x2 y2
            1 , 1  | 3 , 4
            x: 1 == 3 -> 2
            y: 1 == 4 -> 3
            read this articles 
            1. https://iq.opengenus.org/euclidean-vs-manhattan-vs-chebyshev-distance/
            2. https://iq.opengenus.org/chebyshev-distance/
            3. https://en.wikipedia.org/wiki/Taxicab_geometry
            '''
            sx, sy = source
            fx, fy = destination
            
            d = max( abs (sx-fx), abs(sy-fy) )
            
            # print(d)
            
            return d
        
        min_time = 0
        
        n = len(points)
        
        for i in range(1, n):
            print(f"source: {points[i-1]} target: {points[i]}")
            source = points[i-1]
            destination = points[i]
            min_time += find_path_with_min_time(source, destination)
            
            
        return min_time