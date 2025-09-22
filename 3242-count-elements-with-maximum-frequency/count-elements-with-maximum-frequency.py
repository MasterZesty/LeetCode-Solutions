class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        max_freq = {}
        max_f = -1
        for n in nums:
            max_freq[n] = max_freq.get(n, 0) + 1
            max_f = max(max_f, max_freq[n])

        ans = 0
        for k, v in max_freq.items():
            if v == max_f:
                ans += v

        return ans
        