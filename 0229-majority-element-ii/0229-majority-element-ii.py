class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # approch 1 : TC O(n)
        n =len(nums)
        t = n // 3
        ans = set()
        hmap = {}
        
        for num in nums:
            hmap[num] = hmap.get(num,0) + 1
            
            if hmap[num] > t and num not in ans:
                ans.add(num)
        
        return list(ans)