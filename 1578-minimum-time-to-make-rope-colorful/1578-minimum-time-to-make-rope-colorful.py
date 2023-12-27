class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        n = len(colors)
        i = 0
        rm_color = list(colors)
        # print(f"rm_color {rm_color}")
        ans = 0
        
        while i < n:
            curr_char = colors[i]
            start = i
            while i+1 < n and curr_char == colors[i+1]:
                rm_color[i] = '_'
                i += 1
            
            end = i
            
            if start != end:
                # print(f"rm from {start} end {end} \n {colors[start:end+1]} \n {neededTime[start:end+1]}")
                min_time = sum(neededTime[start:end+1]) - max(neededTime[start:end+1])
                ans += min_time
            
            i += 1
            
        # print(f"rm_color {rm_color}")
        
        return ans