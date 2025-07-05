class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hm = {}

        for i, v in enumerate(arr):
            hm[v] = hm.get(v, 0) + 1

        lucky_num = -1

        for n, freq in hm.items():

            if n == freq:
                lucky_num = max(n, lucky_num)

        return lucky_num