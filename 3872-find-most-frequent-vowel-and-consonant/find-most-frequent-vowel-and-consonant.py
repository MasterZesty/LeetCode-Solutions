class Solution:
    def maxFreqSum(self, s: str) -> int:
        map = {}

        for char in s:
            map[char] = map.get(char, 0) + 1

        max_v = 0
        max_c = 0

        for chr, freq in map.items():
            if  chr in ('a', 'e', 'i', 'o', 'u'):
                max_v = max(max_v, freq)
            else:
                max_c = max(max_c, freq)

        return max_v + max_c