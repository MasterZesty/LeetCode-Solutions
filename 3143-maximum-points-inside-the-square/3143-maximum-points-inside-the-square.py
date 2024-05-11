class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        
        hm = defaultdict(list)
        
        for tag, point in zip(s, points):
            r = max(abs(point[0]), abs(point[1]))
            hm[r].append(tag)
            
            
        count = 0
        seen = set()
        for radius in sorted(hm):
            count_at_radius = 0
            for tag in hm[radius]:
                if tag in seen:
                    return count
                
                seen.add(tag)
                count_at_radius += 1
                
            count += count_at_radius
                
        return count