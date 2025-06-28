class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        n = len(height)
        l = 0
        r =  n - 1

        while l < r:
            print(f"l {l} r {r}")

            w = (r - l)
            h = min(height[l], height[r])
            amount_water = w * h 
            print(f"amount_water: {amount_water}")

            max_water = max(max_water, amount_water)

            # we want to keep taller height so move shorter height pointer
            if height[l] < height[r]:
                l += 1
            else:
                r-= 1

        return max_water