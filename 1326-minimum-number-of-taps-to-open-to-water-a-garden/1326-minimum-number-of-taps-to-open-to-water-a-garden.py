class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        # we have garden of length n stating from [o,n]
        # now at each point there is a tap such that total n + 1 taps
        # and each taps is having range 
        # tap at ith position having range [i-range(i), i+ range(i)]
        # now we have to find what is min mumber of taps we should select/open
        # such that our garden is covred in water
        
        # ref : https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/discuss/3983458/simple-beginner-friendly-c-solution-with-intuition-and-explanation/
        # rf : https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/discuss/3982763/VideoBeat-95-solution-with-Python-JavaScript-Java-and-C%2B%2B
        
        max_range = [0] * (n + 1)
        
        for i in range(len(ranges)):
            left = max(0, i - ranges[i])
            right = min(n, i + ranges[i])
            max_range[left] = max(max_range[left], right)
        
        end = farthest = taps = 0
        i = 0
        
        while end < n:
            while i <= end:
                farthest = max(farthest, max_range[i])
                i += 1
            
            if farthest <= end:
                return -1  # Unable to cover the entire garden
            
            end = farthest
            taps += 1
        
        return taps   
        
        
        