class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        c = 0
        c1 = 0
        for i in range(n):
            

            if nums[i] == 1:

                if c < k and c1 > 0:
                    return False
                
                c = 0
                c1 += 1

            if nums[i] == 0:
                c+= 1

            # print(f"i:{i} | c:{c}")

        return True
