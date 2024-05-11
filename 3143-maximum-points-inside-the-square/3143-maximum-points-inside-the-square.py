class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        # ref : https://leetcode.com/problems/maximum-points-inside-the-square/discuss/5144001/Simple-Maths-Explanation-Python3-O(nlog(n))
        
        """
        explanation: 
        1. let us say we have n points in array. now if we consider first point
           then the locaii of that point to form a reactangle should be
           r = max(abs(x), abs(y))
        2. we get such r1, r2, r3 radius consider it as ripple but rectangular 
           ripple
        3. now each of this ripple will number of tags assciated with it beacause
           radius r of this ripple is calculated from that point pi(xi,yi) which have
           tag s[i] assciated with it
        4. so will be having number of rectangular ripples with some tags with it
        5. will sort this ripple frm smaller to larger and will check at each ripple
           if tag is repeated (will store track of tags in set) if it repeated then will
           return count till that point
        """
        
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