class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # approch 1 : TC O(n)
        # note : if you use list and check k in list TC is O(n) for set it is O(1) hence used 
        # set not list as ans
        n =len(nums)
        t = n // 3
        ans = set()
        hmap = {}
        
        for num in nums:
            hmap[num] = hmap.get(num,0) + 1
            
            if hmap[num] > t and num not in ans:
                ans.add(num)
        
        return list(ans)